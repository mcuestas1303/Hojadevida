#!/usr/bin/env python3
"""Render del short 3 de Tin & Tan, «Jensen Huang Is Back as Nvidia CEO After 11 Days», dibujado 100 % con código.

Uso (desde la carpeta del proyecto):
    python3 codigo/render.py                      # diálogo + audio + fotogramas + 06_final/tin_y_tan_short03_v1.mp4
    python3 codigo/render.py --hoja salida.jpg    # hoja de contacto rápida (un fotograma por pulso), sin video
    python3 codigo/render.py --fotograma 450 f.png
    python3 codigo/render.py --sin-audio          # no rehace el diálogo ni el audio (usa 05_audio/mezcla.wav)

La especificación es 02_prompt/prompt.md (14 tomas) y, para abrir y cerrar, la firma del canal
(canales/nostalgia-tin-y-tan/FIRMA_LAPIZ_BUMERAN.md, que manda sobre el prompt): Tan lanza el lápiz al final y lo atrapa
al principio; el último fotograma y el primero son dos instantes seguidos del mismo vuelo.
1080x1920, 30 fps. Los tiempos salen de la voz real (codigo/tiempos.py lee 05_audio/linea_de_tiempo.json).
Personajes: herramientas/palitos.py 1.4. Capas, cámara, sombras, garabatos, texto y firma: herramientas/efectos.py 1.1.
No usa ningún servicio de pago: Pillow, numpy y ffmpeg. Nada de Nvidia (ni logotipo, ni letra, ni verde) y ninguna
persona real dibujada: solo nombres en la voz y en los subtítulos.
"""
import argparse
import math
import subprocess
import sys
import time
from functools import lru_cache
from multiprocessing import Pool
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw

PROY = Path(__file__).resolve().parent.parent
ESTUDIO = PROY.parent.parent
sys.path.insert(0, str(ESTUDIO / "herramientas"))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import palitos  # noqa: E402
import efectos as fx  # noqa: E402
import tiempos as tm  # noqa: E402
from efectos import K, R, T, Capa, Camara, LienzoCapa, Marco, clamp, eio, eo, lerp, muelle, muelle_exacto  # noqa: E402
from palitos import PALETA, SS  # noqa: E402
from tiempos import C, F, FPS, N, DUR  # noqa: E402

W, H = 1080, 1920
SALIDA = PROY / "06_final" / "tin_y_tan_short03_v1.mp4"
PAPEL, SOMBRA, TINTA = PALETA["papel"], PALETA["papel_sombra"], PALETA["tinta"]
MARRON, MOSTAZA, TOMATE, BLANCO = PALETA["marron"], PALETA["mostaza"], PALETA["tomate"], PALETA["blanco"]
POP, SLIDE, SELLO = fx.POP, fx.SLIDE, fx.SELLO

SEG_X0, SEG_X1, SEG_Y0, SEG_Y1 = 100, 980, 250, 1670         # zona segura (formatos.md)
SUELO = 0.86 * H                 # 1651
ALTO_PJ = 505.0                  # 26,3 % (el prompt pedía 29 %, 557 px): con 557 y con 540 el rodete y la gorra quedaban
                                 # pegados al panel de subtítulos de dos renglones (y con 520 quedaban a 9 px); cabeza más alta en y ≈ 1120.
                                 # El hueco panel-cabeza se mide en todos los fotogramas con --medir-subtitulos (≥ 12 px)
X_TAN, X_TIN, X_SOLO = 0.30 * W, 0.70 * W, 0.50 * W
ZONA_G0, ZONA_G1 = 518, 893      # zona de gráficos
BANDA_Y0, BANDA_Y1 = 905, 1085   # banda de subtítulos en español

# ---------------------------------------------------------------- portada y firma del lápiz bumerán
ALTO_PORTADA = 487.0             # R = 88 px
X_PORTADA = (0.24 * W, 0.75 * W)    # Tin en 75 %: con 76 % la gorra salía 2 px de la zona útil (x 960)
SILLA_PORTADA = dict(cx=540.0, base=1100.0, alto=380.0)      # y 720-1100
TAM_PORTADA = 0.07 * H           # 134 px: dos renglones entre y = 400 y 700 (a 12 % no caben dos renglones)
Y_PORTADA = (414.0, 566.0)       # tope de las letras altas de cada renglón
DX_CUERPO = 0.5                  # el desplazamiento del cuerpo de Tan de la firma, a la mitad (-4/+5 px): que no patine
PORTADA_GEO = dict(R=ALTO_PORTADA / 5.53, x_tan=X_PORTADA[0], x_tin=X_PORTADA[1], suelo=SUELO,
                   texto=(108, 400, 700, 700), objeto=(540 - 181, 720, 540 + 181, 1100),
                   cara_tan=(121, 1201, 303, 1364), cara_tin=(741, 1163, 944, 1364))
# el lazo 10 px más abajo (la silla llega a y = 1100). Las cabezas se miden como círculos en TODOS los fotogramas.
GEO = fx.geometria_firma(PORTADA_GEO, subir=-10.0, dx_cuerpo=DX_CUERPO)

# Cara neutra (línea editorial, vuelta 2): nadie sonríe sobre la renuncia ni sobre la reposición. Se arma con piezas
# que ya existen en las fichas (ojos de punto, cejas en reposo, boca suave) y sin rubor.
palitos.EXPRESIONES.setdefault("neutra", {"ojos": "punto", "cejas": (0, 0, 0), "boca": "suave", "rubor": False})


# ---------------------------------------------------------------- movimiento
def vaiven(tl, amp=0.3, f=0.9):
    """Viento de la bufanda de Tan: oscila y se va calmando sin pararse nunca."""
    return amp * (0.6 + 0.4 * math.exp(-0.8 * tl)) * math.cos(2 * math.pi * f * tl)


def sacudida(tl):
    """Movimiento secundario del lápiz en la mano: ±3 grados, una sacudida de muelle por segundo."""
    tau = tl % 1.0
    return 3 * math.exp(-2.2 * tau) * math.sin(2 * math.pi * 2.0 * tau)


def bote(t, fase=0.0, amp=0.012):
    """Rebote de los personajes al pulso (0,5 s): la figura crece desde los pies y vuelve (los pies no se mueven)."""
    tau = (t / 0.5 + fase) % 1.0
    return 1 + amp * math.exp(-4.0 * tau) * math.sin(math.pi * min(1.0, tau * 5)) + 0.004 * math.sin(2 * math.pi * tau)


def pop(t, t0):
    """Escala de entrada de un gráfico: 0 antes de t0, de 0,85 a 1 con muelle."""
    return 0.0 if t < t0 else 0.85 + 0.15 * muelle(t - t0, POP)


# ---------------------------------------------------------------- gráficos propios (genéricos, sin marca)
def silla_director(lz, cx, base, alto, esc=1.0):
    """Silla plegable de director, vacía y sin letras: patas en X y postes de madera marrón, asiento y respaldo de lona
    en papel sombra con dos costuras. (cx, base): centro del apoyo en el suelo. Ancho 0,95 del alto."""
    m = Marco(lz, cx, base, alto * esc)
    g, b = 0.066, 0.02

    def palo(p, q):
        m.linea([p, q], g + 2 * b, TINTA)
        m.linea([p, q], g, MARRON)
    palo((-0.40, -0.03), (0.40, -0.50))
    palo((0.40, -0.03), (-0.40, -0.50))
    m.disco(0, -0.265, 0.035, TINTA)                                  # perno del cruce
    for sx in (-1, 1):
        palo((sx * 0.42, -0.50), (sx * 0.42, -0.96))                  # postes
        m.caja(sx * 0.42 - 0.085, -0.74, sx * 0.42 + 0.085, -0.665, MARRON, b, radio=0.02)     # brazos, vistos de frente
    m.caja(-0.44, -0.575, 0.44, -0.47, SOMBRA, b, radio=0.02)        # asiento de lona
    m.caja(-0.44, -1.0, 0.44, -0.80, SOMBRA, b, radio=0.02)          # respaldo
    for y in (-0.965, -0.835):
        for i in range(11):                                           # costuras (puntadas)
            x = -0.38 + i * 0.076
            m.linea([(x, y), (x + 0.036, y)], 0.008, TINTA)


@lru_cache(maxsize=8)
def img_silla(alto, esc=2):
    """La silla como imagen RGBA (a `esc` px por px) con su caja: (img, ancho, alto de la capa en px de reposo)."""
    w, h = int(alto * 1.08) + 8, int(alto * 1.06) + 8
    lz = LienzoCapa(w, h)
    silla_director(lz, w / 2, h - 6, alto)
    return lz.resultado(esc), w, h


def capa_silla(cx, base, alto, z=0.0, **kw):
    img, w, h = img_silla(int(round(alto)))
    return Capa(img, z=z, x=cx - w / 2, y=base - (h - 6), esc=2, nombre="silla", **kw)


def texto_en_lienzo(lz, s, cx, cy, tam, color=TINTA, izquierda=False, esc=1.0):
    """Texto que es parte de un dibujo (números del calendario, nombres de las barras): centrado en (cx, cy), o con el
    borde izquierdo en cx si izquierda=True. esc: escala de entrada (pop), alrededor del punto dado."""
    img, margen, linea = fx.imagen_texto(((s, color),), tam)
    ancho = fx.ancho_texto(((s, color),), tam)
    if esc != 1.0:
        img = img.resize((max(1, int(img.width * esc)), max(1, int(img.height * esc))), Image.LANCZOS)
        y = (cy + 0.36 * tam * esc) * SS - linea * esc
        x = (cx - (0 if izquierda else ancho * esc / 2)) * SS - margen * esc
        lz.img.alpha_composite(img, (int(round(x)), int(round(y))))
        return
    x = (cx - (0 if izquierda else ancho / 2)) * SS - margen
    y = (cy + 0.36 * tam) * SS - linea
    lz.img.alpha_composite(img, (int(round(x)), int(round(y))))


DIAS = "SMTWTFS"


class Calendario:
    """Hoja de noviembre de 2026 (el 1 es domingo): 7 columnas y 6 filas, cabecera marrón con las iniciales."""

    def __init__(self, x0, y0, ancho, alto):
        self.x0, self.y0, self.w, self.h = x0, y0, ancho, alto
        self.cab = 0.16 * alto
        self.cw, self.ch = ancho / 7, (alto - self.cab) / 6

    def celda(self, dia):
        i = dia - 1                                       # el 1 de noviembre de 2026 cae en domingo (columna 0)
        return self.x0 + (i % 7 + 0.5) * self.cw, self.y0 + self.cab + (i // 7 + 0.5) * self.ch

    def dibujar(self, lz, cruces=None):
        m = Marco(lz, self.x0, self.y0)
        b = 0.012 * self.w
        m.caja(0, 0, self.w, self.h, BLANCO, b, radio=0.02 * self.w)
        m.rect(b, b, self.w - b, self.cab, MARRON, 0.02 * self.w - b)
        m.rect(b, self.cab / 2, self.w - b, self.cab, MARRON)
        m.rect(b, self.cab - b / 2, self.w - b, self.cab + b / 2, TINTA)
        for i in range(1, 7):
            m.linea([(i * self.cw, self.cab + 0.1 * self.ch), (i * self.cw, self.h - b - 0.1 * self.ch)], 2, SOMBRA)
        tam = 0.46 * self.ch
        for i, d in enumerate(DIAS):
            texto_en_lienzo(lz, d, self.x0 + (i + 0.5) * self.cw, self.y0 + self.cab * 0.52, 0.5 * self.cab, PAPEL)
        for dia in range(1, 31):                          # el número va en la parte de arriba de la celda
            cx, cy = self.celda(dia)
            texto_en_lienzo(lz, str(dia), cx, cy - 0.14 * self.ch, tam)
        for dia, e in (cruces or {}).items():             # cruces de tinta, con entrada de pop
            if e <= 0.02:
                continue
            cx, cy = self.celda(dia)                      # la cruz va debajo del número: no lo tapa
            r = 0.15 * self.ch * e
            mm = Marco(lz, cx, cy + 0.29 * self.ch)
            mm.linea([(-r, -r), (r, r)], 0.075 * self.ch, TINTA)
            mm.linea([(-r, r), (r, -r)], 0.075 * self.ch, TINTA)

    def circulo(self, dia):
        cx, cy = self.celda(dia)
        return fx.trazo_circulo(cx, cy - 0.14 * self.ch, 0.36 * self.cw, 0.33 * self.ch)

    def flecha(self, a, b):
        """Flecha larga del día a al día b (celdas vecinas en diagonal): sale por la derecha del círculo de a, da la
        vuelta por fuera de las dos celdas y entra por la derecha en el círculo de b. Cuerpo y punta."""
        (xa, ya), (xb, yb) = self.celda(a), self.celda(b)
        ya, yb = ya - 0.14 * self.ch, yb - 0.14 * self.ch
        p0, p3 = (xa + 0.42 * self.cw, ya), (xb + 0.46 * self.cw, yb + 0.04 * self.ch)
        p1, p2 = (xa + 1.9 * self.cw, ya - 0.1 * self.ch), (xa + 1.7 * self.cw, yb + 0.25 * self.ch)
        cuerpo = [fx._bezier((p0, p1, p2, p3), i / 28) for i in range(29)]
        ang = math.atan2(p3[1] - cuerpo[-3][1], p3[0] - cuerpo[-3][0])
        L = 0.42 * self.ch
        punta = [(p3[0] - L * math.cos(ang + q), p3[1] - L * math.sin(ang + q)) for q in (-0.55, 0.55)]
        return [cuerpo, [punta[0], p3, punta[1]]]


def garabato_mostaza(img, trazos, p, grosor, semilla=3):
    """Trazo a mano en mostaza con contorno de tinta (mostaza sobre blanco da 1,6:1: se lee por el contorno)."""
    fx.garabato(img, trazos, p, grosor=grosor + 6, color=TINTA, semilla=semilla)
    fx.garabato(img, trazos, p, grosor=grosor, color=MOSTAZA, semilla=semilla)


CAL_FONDO = Calendario(0, 0, 840, 364)                          # toma 3: capa lejana, por encima de la banda de
CAL_FONDO_XY = (120, 468)                                       # subtítulos (con 700 px de alto quedaba debajo del texto)
CAL_ZONA = Calendario(150, ZONA_G0 - 6, 780, ZONA_G1 - ZONA_G0 - 8)     # tomas 5 y 6: en la zona de gráficos


@lru_cache(maxsize=2)
def img_calendario_fondo():
    lz = LienzoCapa(CAL_FONDO.w + 8, CAL_FONDO.h + 8)
    c = Calendario(4, 4, CAL_FONDO.w, CAL_FONDO.h)
    c.dibujar(lz)
    return lz.resultado(), c


@lru_cache(maxsize=2)
def img_mesa():
    """Mesa de junta genérica: tablero marrón de 800 x 64 con dos patas, cinco sillas genéricas detrás y la silla de
    director vacía a la cabecera (izquierda). Ninguna persona, ningún papel. Capa de 880 x 375 (la zona de gráficos)."""
    w, h = 880, ZONA_G1 - ZONA_G0
    lz = LienzoCapa(w, h)
    m = Marco(lz, 0, 0)
    y_t = 232                                                       # tope del tablero
    for i in range(5):                                              # sillas genéricas detrás de la mesa
        cx = 250 + i * 142
        m.caja(cx - 45, y_t - 118, cx + 45, y_t + 32, SOMBRA, 6, radio=16)
    for x in (150, 800):                                            # patas
        m.caja(x - 20, y_t + 40, x + 20, h - 4, MARRON, 6, radio=4)
    m.caja(76, y_t, 876, y_t + 64, MARRON, 7, radio=10)            # tablero de 800 x 64
    silla_director(lz, 118, h - 4, 235)                              # la silla de director, vacía, a la cabecera
    return lz.resultado(2)


BARRA_H = 40                       # alto de las barras de la comparación (la de tenencia de la toma 7 mide 56)
FILA_ALTO, FILA_Y0 = 124, 522      # cada fila: el nombre (56 px) arriba y su barra debajo; tres filas en y 522-876
TAM_NOMBRE = 56
MARCA_MIN = 4                      # ancho mínimo dibujado de las barras de 11 y 5 días (a escala serían 2,2 y 1,0 px)
NOMBRES = ("Huang 11", "Altman 5", "Jobs 4,382")       # texto exacto (tabla de rótulos de la sección 12 del prompt)


def barra(lz, x0, y, largo, color, alto=BARRA_H):
    if largo < 1:
        return
    m = Marco(lz, x0, y + alto / 2, 1.0)
    m.caja(0, -alto / 2, largo, alto / 2, color, 5 if largo > 14 else 0, radio=6 if largo > 14 else 0)


def marca_minima(lz, x, y, color, esc=1.0):
    """Marca de 4 px (más 3 px de contorno de tinta a cada lado, para que se vea), del alto de la barra."""
    if esc <= 0.02:
        return
    m = Marco(lz, x, y + BARRA_H / 2)
    h = BARRA_H / 2 * esc
    m.rect(-3, -h - 3, MARCA_MIN + 3, h + 3, TINTA, 3)
    m.rect(0, -h, MARCA_MIN, h, color)


def fila_barra(lz, i, esc_nombre, color=TINTA, esc_marca=None, largo=None):
    """Fila i (0 Huang, 1 Altman, 2 Jobs): su nombre en tinta arriba, a la izquierda, y debajo su barra a escala
    (largo en px) o su marca mínima de 4 px."""
    y = FILA_Y0 + i * FILA_ALTO
    if esc_nombre > 0.02:
        texto_en_lienzo(lz, NOMBRES[i], SEG_X0 + 2, y + 0.37 * TAM_NOMBRE, TAM_NOMBRE, izquierda=True, esc=esc_nombre)
    yb = y + TAM_NOMBRE + 10
    if largo is not None:
        barra(lz, SEG_X0, yb, largo, color)
    else:
        marca_minima(lz, SEG_X0 + 3, yb, color, esc_nombre if esc_marca is None else esc_marca)


# ---------------------------------------------------------------- escena: capas, cámara y personajes
def suelo(lz):
    lz.d.line([(SEG_X0 * SS, SUELO * SS), (SEG_X1 * SS, SUELO * SS)], fill=SOMBRA, width=4 * SS)


def pj(lz, quien, x, t, pose, expresion, fase=0.0, alto=ALTO_PJ, amp=0.012, **kw):
    kw.setdefault("vista", "frente")
    if quien == "tan":
        kw.setdefault("espejo", True)
    palitos.dibujar(lz, quien, x, SUELO, alto * bote(t, fase, amp), pose=pose, expresion=expresion, **kw)


def sombras(*xs, ancho=200):
    return [fx.capa_sombra_contacto(x, SUELO + 3, ancho, opacidad=0.28) for x in xs]


def camara(avance=0.0, x=W / 2, zoom=1.0, ancla=None):
    """Cámara de trabajo del video (prompt, sección 5). El encuadre final de cada empuje es el de diseño (avance 0) y
    la toma EMPIEZA más abierta (avance negativo): así nada sale nunca de la zona segura. El empuje se ancla en la
    línea de suelo (los pies no se mueven y las cabezas no suben hacia la banda de subtítulos)."""
    pz = zoom * 1000.0 / (1000.0 - avance)
    ancla = SUELO if ancla is None else ancla
    return Camara(x=x, y=ancla - (ancla - H / 2) / pz, avance=avance, zoom=zoom, apertura=0.018, campo=150, niebla=0.30,
                  focal=1000)


@lru_cache(maxsize=1)
def fondo_papel():
    return fx.papel(W, H)


def componer(capas, cam=None):
    return fx.componer(capas, cam or Camara(), fondo=fondo_papel())


def principal(lz):
    return Capa(lz.resultado(), z=0.0, nombre="principal")


# ---------------------------------------------------------------- tomas (cada una devuelve la imagen RGB sin texto)
def plano_firma(c):
    """Tomas 1 y 14: la portada con la firma del lápiz bumerán. c: fotograma contado desde el empalme (c >= 0, apertura;
    c < 0, cierre). Cámara fija, todo nítido. La silla está completa y quieta (FIRMA, §5.1)."""
    est = fx.lapiz_bumeran(c, GEO)
    tan, tin = est["tan"], est["tin"]
    lz = LienzoCapa(W, H)
    suelo(lz)
    silla_director(lz, SILLA_PORTADA["cx"], SILLA_PORTADA["base"], SILLA_PORTADA["alto"])
    # Tan: `sorpresa` (decisión del equipo, vuelta 2: `curiosidad` se leía seria); la misma cara en la anticipación
    # (el prompt no admite `concentrado`: se lee como enojo)
    palitos.dibujar(lz, "tan", X_PORTADA[0] + DX_CUERPO * tan["dx"], SUELO, ALTO_PORTADA, pose=tan["pose"],
                    expresion="sorpresa", vista="perfil", mira=1, viento=tan["viento"], objeto=tan["objeto"],
                    giro_objeto=tan["giro_objeto"], cabeza_giro=tan["cabeza_giro"])
    palitos.dibujar(lz, "tin", X_PORTADA[1], SUELO + tin["dy"], ALTO_PORTADA, pose="parado", expresion="sorpresa",
                    vista="perfil", mira=-1, objeto=False, cabeza_giro=tin["cabeza_giro"])
    capas = sombras(X_PORTADA[0], X_PORTADA[1], ancho=180) + [fx.capa_sombra_contacto(540, 1100, 330, opacidad=0.25)]
    capas += [principal(lz)] + fx.pintar_lapiz_volador(est, GEO)
    return componer(capas)


def toma_1(t):
    return plano_firma(F(t))


def toma_2(t):
    tl = t - C(2)
    lz = LienzoCapa(W, H)
    suelo(lz)
    pose = palitos.pose_entre("saluda", "pregunta", muelle_exacto(tl, SLIDE, 0.4) if tl < 0.4 else 1.0)
    pj(lz, "tan", X_SOLO, t, pose, "curiosidad", mira=1, viento=vaiven(tl), objeto=False)
    capas = [capa_silla(540, 800, 230, z=420.0)] + sombras(X_SOLO) + [principal(lz)]
    return componer(capas, camara(avance=-40 * (1 - eio(tl / (C(3) - C(2))))))


def toma_3(t):
    tl, dur = t - C(3), C(4) - C(3)
    lz = LienzoCapa(W, H)
    suelo(lz)
    sorprendida = t >= tm.T3_CIRCULO[1]
    pj(lz, "tan", X_TAN, t, "senala", "sorpresa" if sorprendida else "curiosidad",
       viento=vaiven(tl, 0.25) + (0.6 * math.exp(-2 * (t - tm.T3_CIRCULO[1])) if sorprendida else 0.0))
    # Tin dice «resigned… after a scandal» con cara neutra y sin rubor (línea editorial)
    pj(lz, "tin", X_TIN, t, "explica", "neutra", fase=0.5, objeto="lapiz", giro_objeto=sacudida(tl))
    cal, c = img_calendario_fondo()
    p = clamp((t - tm.T3_CIRCULO[0]) / (tm.T3_CIRCULO[1] - tm.T3_CIRCULO[0]))
    if p > 0:
        cal = cal.copy()
        garabato_mostaza(cal, c.circulo(12), eo(p), 9)
    # la silla de primer plano va al centro, entre los dos: a la izquierda salía de la zona segura (x < 100)
    capas = [Capa(cal, z=260.0, x=CAL_FONDO_XY[0] - 4, y=CAL_FONDO_XY[1] - 4, nombre="calendario"),
             fx.capa_sombra_contacto(540, 1668, 150, z=-220.0, opacidad=0.25),
             capa_silla(540, 1668, 176, z=-220.0, desenfoque=0.0)] + sombras(X_TAN, X_TIN) + [principal(lz)]
    u = eio(tl / dur)
    return componer(capas, camara(avance=-90 * (1 - u), x=lerp(540, 562, u)))


def toma_4(t):
    tl, dur = t - C(4), C(5) - C(4)
    lz = LienzoCapa(W, H)
    suelo(lz)
    pj(lz, "tan", X_TAN, t, "pregunta", "curiosidad", viento=vaiven(tl, 0.25))
    pj(lz, "tin", X_TIN, t, dict(palitos.POSES["senala"], bd=(118.0, 142.0), objeto_arriba=True), "neutra", fase=0.5,
       objeto="lapiz", giro_objeto=sacudida(tl) - 10, espejo=True)       # señala la mesa: arriba y hacia el centro
    p = clamp((t - tm.T4_REVELADO[0]) / (tm.T4_REVELADO[1] - tm.T4_REVELADO[0]))
    q = 1 - eo(p)
    mesa = Capa(img_mesa(), z=180.0, x=100, y=ZONA_G0 - 54, esc=2, nombre="mesa", desenfoque=(42.0 * q ** 1.4) if q > 0.002 else None,
                opacidad=1 - 0.25 * q, sombra=dict(dx=14, dy=10, radio=10, opacidad=0.22))
    return componer([mesa] + sombras(X_TAN, X_TIN) + [principal(lz)], camara(avance=-60 * (1 - eio(tl / dur))))


def _calendario_zona(lz, t):
    cruces = {13 + i: (0.0 if t < tm.T5_CRUCES + 0.1 * i else 0.85 + 0.15 * muelle(t - tm.T5_CRUCES - 0.1 * i, POP))
              for i in range(11)}
    CAL_ZONA.dibujar(lz, cruces)


def _marcas_zona(img, t):
    """Marcas del calendario de las tomas 5 y 6: el círculo del 12 sigue a la vista (en tinta: no suma otro acento),
    círculo de tinta en el 17 (de ahí sale «+6 days»), flecha larga del 17 al 23 y círculo mostaza en el 23."""
    fx.garabato(img, CAL_ZONA.circulo(12), 1.0, grosor=6, semilla=3)
    p17 = clamp((t - tm.T5_MARCA_17[0]) / (tm.T5_MARCA_17[1] - tm.T5_MARCA_17[0]))
    if p17 > 0:
        fx.garabato(img, CAL_ZONA.circulo(17), eo(p17), grosor=6, semilla=7)
    pf = clamp((t - tm.T5_FLECHA[0]) / (tm.T5_FLECHA[1] - tm.T5_FLECHA[0]))
    if pf > 0:
        fx.garabato(img, CAL_ZONA.flecha(17, 23), eo(pf), grosor=8, semilla=5, temblor=1.5)
    pc = clamp((t - tm.T5_CIRCULO[0]) / (tm.T5_CIRCULO[1] - tm.T5_CIRCULO[0]))
    if pc > 0:
        garabato_mostaza(img, CAL_ZONA.circulo(23), eo(pc), 6)
    return img


def toma_5(t):
    tl = t - C(5)
    lz = LienzoCapa(W, H)
    suelo(lz)
    _calendario_zona(lz, t)
    # Reposición: sin festejo (línea editorial). Tan señala y se sorprende; Tin explica con cara neutra.
    repuesto = t >= tm.T5_CIRCULO[0]
    pj(lz, "tan", X_TAN, t, "senala", "sorpresa" if repuesto else "curiosidad",
       viento=vaiven(tl, 0.25) + (0.5 * math.exp(-2 * (t - tm.T5_CIRCULO[0])) * math.cos(9 * (t - tm.T5_CIRCULO[0])) if repuesto else 0))
    pj(lz, "tin", X_TIN, t, "explica", "neutra", fase=0.5, objeto="lapiz", giro_objeto=sacudida(tl))
    capa = Capa(_marcas_zona(lz.resultado(), t), z=0.0, nombre="principal")
    return componer(sombras(X_TAN, X_TIN) + [capa])


def toma_6(t):
    tl = t - C(6)
    lz = LienzoCapa(W, H)
    suelo(lz)
    _calendario_zona(lz, t)
    pj(lz, "tan", X_SOLO, t, "senala", "sorpresa", viento=vaiven(tl, 0.3, 1.2))
    capa = Capa(_marcas_zona(lz.resultado(), t), z=0.0, nombre="principal")
    return componer(sombras(X_SOLO) + [capa])


def toma_7(t):
    tl = t - C(7)
    lz = LienzoCapa(W, H)
    suelo(lz)
    p = eo((t - tm.T7_BARRA[0]) / (tm.T7_BARRA[1] - tm.T7_BARRA[0])) if t >= tm.T7_BARRA[0] else 0.0
    # 12.274 días = 880 px. Sin la marca mostaza de los 11 días al final (0,8 px a escala): parecía un remate de la barra.
    barra(lz, SEG_X0, 650, 880 * p, MARRON, alto=56)
    pj(lz, "tin", X_SOLO, t, "explica", "neutra", objeto="lapiz", giro_objeto=sacudida(tl))
    return componer(sombras(X_SOLO) + [principal(lz)])


def toma_8(t):
    tl = t - C(8)
    lz = LienzoCapa(W, H)
    suelo(lz)
    pj(lz, "tan", X_SOLO, t, palitos.pose_entre("parado", "encoge", muelle(tl, SLIDE)), "curiosidad", viento=vaiven(tl))
    capas = [capa_silla(540, 800, 230, z=420.0)] + sombras(X_SOLO) + [principal(lz)]
    return componer(capas, camara(avance=-30 * (1 - eio(tl / (C(9) - C(8))))))


def toma_9(t):
    tl = t - C(9)
    lz = LienzoCapa(W, H)
    suelo(lz)
    fila_barra(lz, 0, pop(t, tm.T9_HUANG))                               # Huang 11 (tinta)
    fila_barra(lz, 1, pop(t, tm.T9_ALTMAN), color=MOSTAZA)               # Altman 5 (mostaza: el acento del plano)
    pj(lz, "tin", X_SOLO, t, "explica", "neutra", objeto="lapiz", giro_objeto=sacudida(tl))
    return componer(sombras(X_SOLO) + [principal(lz)], camara(avance=-50 * (1 - eio(tl / (C(10) - C(9))))))


ASOMBRO = dict(palitos.POSES["encoge"], bi=(78.0, 150.0), bd=(78.0, 150.0))    # manos abiertas a la altura de la cara


def toma_10(t):
    tl = t - C(10)
    lz = LienzoCapa(W, H)
    suelo(lz)
    llego = t >= tm.LLEGA
    tau = t - tm.LLEGA
    fila_barra(lz, 0, 1.0)
    fila_barra(lz, 1, 1.0)
    # el nombre «Jobs 4,382» entra cuando el contador llega (no adelanta la cifra); la barra crece con el contador
    fila_barra(lz, 2, pop(t, tm.LLEGA), color=MARRON, largo=880 * tm.contador(t) / tm.VALOR_JOBS)
    # Asombro, sin festejo: Tan abre las manos con sorpresa; Tin levanta la mano vacía, también con sorpresa.
    # antes del contador el plano no se queda quieto: Tan pasa de `encoge` a `pregunta`, Tin baja la mano del lápiz y
    # la cámara empuja despacio hasta que arranca el contador (revisar_fotogramas marcaba 19,1-20,8 s como congelado)
    pose_tan = palitos.pose_entre("pregunta", ASOMBRO, muelle(tau, SLIDE)) if llego else \
        palitos.pose_entre("encoge", "pregunta", muelle(tl - 0.5, SLIDE))
    pj(lz, "tan", X_TAN, t, pose_tan, "sorpresa" if llego else "curiosidad", amp=0.022,
       viento=(0.9 * math.exp(-1.3 * tau) * math.cos(2 * math.pi * 1.5 * tau) if llego else 0.0) + vaiven(tl, 0.15))
    pose_tin = palitos.pose_entre("explica", "saluda", muelle(tau, SLIDE)) if llego else \
        palitos.pose_entre("parado", "explica", muelle(tl - 0.15, SLIDE))
    pj(lz, "tin", X_TIN, t, pose_tin, "sorpresa" if llego else "neutra", fase=0.5, objeto=False, amp=0.022)
    # Zoom de golpe de +10 % al llegar la cifra. Para que la barra de 880 px no salga de la zona segura, la cámara se
    # abre despacio un 9 % mientras el contador sube y el golpe la devuelve al encuadre de diseño (escala 1, nunca más).
    abierto = 1 / 1.10
    if llego:
        zoom = min(1.0, abierto * fx.golpe_de_zoom(tau, 0.10))
    else:
        zoom = lerp(1.0, abierto, eio((t - tm.CONTADOR[0]) / (tm.LLEGA - tm.CONTADOR[0]))) if t > tm.CONTADOR[0] else 1.0
    antes = clamp(tl / (tm.CONTADOR[0] - C(10)))
    cam = camara(zoom=zoom, avance=-40 * (1 - eio(antes)), ancla=(BANDA_Y0 + BANDA_Y1) / 2)     # anclada en la banda: ni las barras ni las cabezas la pisan
    cam.apertura = 0.0
    return componer(sombras(X_TAN, X_TIN) + [principal(lz)], cam)


def _tres_filas(lz, huang=TINTA):
    fila_barra(lz, 0, 1.0, color=huang)
    fila_barra(lz, 1, 1.0)
    fila_barra(lz, 2, 1.0, color=MARRON, largo=880)


def toma_11(t):
    tl = t - C(11)
    lz = LienzoCapa(W, H)
    suelo(lz)
    _tres_filas(lz)
    # La cifra queda quieta (capa de texto fija); para que el plano no se congele, Tan pasa de `pregunta` a `encoge`
    # cuando dice «twelve years?», la bufanda se mueve y la cámara empuja despacio (anclada al suelo).
    dicho = max(0.0, t - (tm.P(9) - 0.1))
    pose = palitos.pose_entre("pregunta", "encoge", muelle(dicho, SLIDE))
    pj(lz, "tan", X_SOLO, t, pose, "sorpresa", amp=0.02,
       viento=0.6 * math.exp(-1.2 * tl) * math.cos(2 * math.pi * 1.5 * tl) + vaiven(tl, 0.3, 1.1))
    cam = camara(avance=-45 * (1 - eio(tl / (C(12) - C(11)))))
    cam.apertura = 0.0
    return componer(sombras(X_SOLO) + [principal(lz)], cam)


def toma_12(t):
    """Remate: aquí sí se permite la alegría (risa de los dos)."""
    tl = t - C(12)
    lz = LienzoCapa(W, H)
    suelo(lz)
    _tres_filas(lz, huang=MOSTAZA)
    pj(lz, "tan", X_TAN, t, "encoge", "risa", viento=0.4 * math.exp(-2 * tl) * math.cos(2 * math.pi * 2 * tl) + vaiven(tl, 0.15))
    pj(lz, "tin", X_TIN, t, "explica", "risa", fase=0.5, objeto="lapiz", giro_objeto=sacudida(tl) + 8 * math.exp(-3 * tl))
    return componer(sombras(X_TAN, X_TIN) + [principal(lz)])


SILLA_13 = dict(cx=540.0, base=1651.0, alto=236.0)       # entre los dos, en el suelo (no cabe bajo la banda de subtítulos)


def toma_13(t):
    """Pregunta final e invitación; Tin le pasa el lápiz a Tan (que lo lanzará en el cierre)."""
    tl = t - C(13)
    lz = LienzoCapa(W, H)
    suelo(lz)
    silla_director(lz, SILLA_13["cx"], SILLA_13["base"], SILLA_13["alto"])
    a, b = tm.T13_PASE
    de_tan = t >= b
    pj(lz, "tan", X_TAN, t, "pregunta", "curiosidad", viento=vaiven(tl, 0.25), objeto="lapiz" if de_tan else False,
       giro_objeto=(12 * math.exp(-5 * (t - b)) * math.cos(14 * (t - b))) if de_tan else 0.0)
    pj(lz, "tin", X_TIN, t, "explica", "feliz", fase=0.5, objeto="lapiz" if t < a else False, giro_objeto=sacudida(tl))
    capas = sombras(X_TAN, X_TIN) + [fx.capa_sombra_contacto(540, SUELO + 3, 210, opacidad=0.25), principal(lz)]
    if a <= t < b:                                      # el lápiz libre, en un arco corto y con media vuelta
        u = eio((t - a) / (b - a))
        (x0, y0), r = palitos.mano_de(X_TIN, SUELO, ALTO_PJ, "explica")
        (x1, y1), _ = palitos.mano_de(X_TAN, SUELO, ALTO_PJ, "pregunta", espejo=True)
        x, y = lerp(x0 + 0.05 * r, x1 - 0.05 * r, u), lerp(y0 - 0.25 * r, y1 - 0.25 * r, u) - 40 * math.sin(math.pi * u)
        cl = LienzoCapa(W, H)
        palitos.lapiz(palitos.Pluma(cl, x, y, r * (1 + 0.15 * math.sin(math.pi * u))), 0, 0, angulo=lerp(-35, -240, u))
        capas.append(Capa(cl.resultado(), z=-60.0, niebla=0.0, desenfoque=0.0, sombra=dict(dx=14, dy=10, radio=10, opacidad=0.2)))
    return componer(capas)


def toma_14(t):
    return plano_firma(F(t) - N)


TOMAS = [toma_1, toma_2, toma_3, toma_4, toma_5, toma_6, toma_7, toma_8, toma_9, toma_10, toma_11, toma_12, toma_13, toma_14]


def toma_de(f):
    t = f / FPS
    for i in range(14):
        if tm.CORTES[i] <= t < tm.CORTES[i + 1]:
            return i + 1
    return 14


# ---------------------------------------------------------------- texto en pantalla (capa fija, encima de todo)
TEXTO_X = 0.10 * W
TAM_ROTULO = 0.07 * H            # 134 px
Y_ROTULO = 0.14 * H              # 269 px: tope de las letras altas
PORTADA_SEGS = ((T("Back In"),), (K("11"), T(" Days?")))
FIJOS = {
    "11 days?": (K("11"), T(" days?")), "Nov 12": (T("Nov "), K("12")), "Nov 17": (T("Nov "), K("17")),
    "+6 days": (T("+"), K("6"), T(" days")), "Nov 23": (T("Nov "), K("23")), "11 days": (K("11"), T(" days")),
    "12,274 days": (K("12,274"), T(" days")), "5 days": (K("5"), T(" days")), "Who else?": (T("Who "), K("else"), T("?")),
    "Subscribe": (K("Subscribe"),),
}
GOLPE_CLAVE = 14                 # fotograma del golpe de la clave «11» de la portada: con la primera sílaba de la voz


def segmentos(que, t):
    if que == "contador":
        v = tm.contador(t)
        return ((f"{v:,}", TOMATE if v >= tm.VALOR_JOBS else TINTA), T(" days"))
    return FIJOS[que]


def _pegar_texto(base, segs, x, tope, tam, esc=1.0, alfa=1.0, dy=0.0):
    fx.poner_texto(base, tuple(segs), x, tope + dy, tam, esc=esc, alfa=alfa)


def capa_rotulos(base, f):
    t = f / FPS
    for entra, sale, que in tm.ROTULOS:
        fi, fs = F(entra), F(sale)
        if not (fi <= f < fs):
            continue
        if que == "portada":                                    # entero y quieto desde el fotograma 0 (es la portada)
            alfa = 1.0 if f < fs - 3 else 1 - ((f - (fs - 3) + 1) / 4) ** 2
            g = 1 + 0.12 * max(0.0, fx.impulso_muelle((f - GOLPE_CLAVE) / FPS, POP))
            _pegar_texto(base, PORTADA_SEGS[0], TEXTO_X, Y_PORTADA[0], TAM_PORTADA, alfa=alfa)
            _pegar_texto(base, PORTADA_SEGS[1], TEXTO_X, Y_PORTADA[1], TAM_PORTADA, esc=g, alfa=alfa)
            continue
        if que == "portada_cierre":                             # entra con pop en c = -30 y llega a escala 1 exacta
            esc = 0.85 + 0.15 * muelle_exacto(t - entra, POP, sale - entra)
            alfa = min(1.0, (f - fi + 1) / 2)
            for segs, y in zip(PORTADA_SEGS, Y_PORTADA):
                _pegar_texto(base, segs, TEXTO_X, y, TAM_PORTADA, esc=esc, alfa=alfa)
            continue
        esc, alfa, dy = 0.85 + 0.15 * muelle(t - entra, POP), min(1.0, (f - fi + 1) / 2), 0.0
        if que == "contador" and t >= tm.LLEGA:                 # al llegar: pop del texto en el mismo fotograma
            esc *= 1 + 0.12 * (1 - muelle(t - tm.LLEGA, POP))
        if f >= fs - 3:                                         # salida: sube y se desvanece en 3 fotogramas
            u = (f - (fs - 3) + 1) / 4
            dy, alfa = -min(0.02 * H * u * u, 10.0), alfa * (1 - u * u)
        _pegar_texto(base, segmentos(que, t), TEXTO_X, Y_ROTULO, TAM_ROTULO, esc=esc, alfa=alfa, dy=dy)
    return base


TAM_SUB = 0.045 * H              # 86 px
SUB_MAX = 856                    # ancho máximo de un renglón
SUB_INTERLINEA = 88


def _linea_sub(s):
    return ((s, TINTA),)


def caja_subtitulo(f):
    """(tarjeta, renglones visibles con su alfa, caja del panel (x0, y0, x1, y1), tope del primer renglón, alfa) del
    subtítulo del fotograma f, o None. La usan el dibujo y la medición del hueco con las cabezas."""
    for k, entra, sale, renglones, aparece in tm.SUBTITULOS:
        fi, fs = F(entra), F(sale)
        if not (fi <= f < fs):
            continue
        alfa = min(1.0, (f - fi + 1) / 3, (fs - f) / 2)
        vis = []
        for i, r in enumerate(renglones):
            fa = F(aparece[i]) if aparece and aparece[i] is not None else fi
            if f >= fa:
                vis.append((r, min(1.0, (f - fa + 1) / 3)))
        anchos = [fx.ancho_texto(_linea_sub(r), TAM_SUB) for r, _ in vis]
        n = len(vis)
        alto_texto = 0.74 * TAM_SUB + (n - 1) * SUB_INTERLINEA
        cy = (BANDA_Y0 + BANDA_Y1) / 2
        tope = cy - alto_texto / 2 - 3
        w, h = max(anchos) + 2 * 12, alto_texto + 2 * 12 + 18
        x0, y0 = W / 2 - w / 2, max(BANDA_Y0, cy - h / 2)
        return k, vis, (x0, y0, x0 + w, min(BANDA_Y1, y0 + h)), tope, alfa
    return None


def capa_subtitulos(base, f):
    """Banda de subtítulos en español: panel de papel translúcido (0,82) con esquinas de 20 px y texto en tinta a 86 px,
    centrado en la banda y 905-1085. Entrada con fundido de 3 fotogramas. Un renglón puede aparecer más tarde que su
    tarjeta (la cifra de la tarjeta 8 entra cuando el contador llega)."""
    c = caja_subtitulo(f)
    if c is None:
        return base
    k, vis, caja, tope, alfa = c
    panel = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(panel).rounded_rectangle(list(caja), radius=20, fill=fx._rgb(PAPEL) + (int(255 * 0.82 * alfa),))
    base.paste(panel, (0, 0), panel)
    for i, (r, a_r) in enumerate(vis):
        a = fx.ancho_texto(_linea_sub(r), TAM_SUB)
        fx.poner_texto(base, _linea_sub(r), W / 2 - a / 2, tope + i * SUB_INTERLINEA, TAM_SUB, alfa=alfa * a_r)
    return base


def _hueco_subtitulo(f):
    """Para el fotograma f con subtítulo: (f, tarjeta, hueco en px entre el panel y lo dibujado más cercano por debajo
    —las cabezas—, hueco por encima —los gráficos—, píxeles dibujados que quedan debajo del propio panel)."""
    c = caja_subtitulo(f)
    if c is None:
        return None
    k, _, (x0, y0, x1, y1), _, _ = c
    a = np.asarray(escena(f), dtype=np.int16)
    dif = np.abs(a - np.asarray(fondo_papel(), dtype=np.int16)).sum(axis=2) > 60
    x0, y0, x1, y1 = int(x0), int(y0), int(math.ceil(x1)), int(math.ceil(y1))
    filas_abajo = np.nonzero(dif[y1:1500, :].any(axis=1))[0]
    filas_arriba = np.nonzero(dif[400:y0, :].any(axis=1))[0]
    abajo = int(filas_abajo[0]) if len(filas_abajo) else 999
    arriba = int(y0 - 400 - 1 - filas_arriba[-1]) if len(filas_arriba) else 999
    return f, k, abajo, arriba, int(dif[y0:y1, x0:x1].sum())


def medir_subtitulos():
    """Mide en TODOS los fotogramas con subtítulo el hueco entre el panel y las cabezas (criterio: 12 px o más) y
    comprueba que el panel no tapa nada dibujado. Devuelve líneas de informe y si pasa."""
    fs = [f for f in range(N) if caja_subtitulo(f)]
    with Pool(4) as pool:
        datos = [d for d in pool.map(_hueco_subtitulo, fs, chunksize=8) if d]
    lineas, pasa = [], True
    for k in sorted({d[1] for d in datos}):
        dk = [d for d in datos if d[1] == k]
        ab, ar, tap = min(d[2] for d in dk), min(d[3] for d in dk), max(d[4] for d in dk)
        ok = ab >= 12 and ar >= 12 and tap == 0
        pasa &= ok
        lineas.append(f"tarjeta {k:2d} ({len(dk)} fotogramas): hueco mínimo con las cabezas {ab} px; con los gráficos de arriba "
                      f"{ar} px; píxeles dibujados bajo el panel {tap}: {'pasa' if ok else 'NO PASA'}")
    lineas.append(f"mínimo general con las cabezas: {min(d[2] for d in datos)} px; con los gráficos: {min(d[3] for d in datos)} px "
                  f"(criterio: 12 px o más y nada bajo el panel): {'PASA' if pasa else 'NO PASA'}")
    return lineas, pasa


# ---------------------------------------------------------------- fotograma
def escena(f):
    """El fotograma f sin texto ni subtítulos (RGB 1080x1920)."""
    f = f % N
    return TOMAS[toma_de(f) - 1](f / FPS)


def fotograma(f):
    """El fotograma f (0 a N - 1; el N es el 0: bucle) como imagen RGB de 1080x1920."""
    f = f % N
    img = escena(f)
    for corte in tm.BORRONES:                 # borrón: 2 fotogramas antes y 2 después del corte
        fc = F(corte)
        if fc - 2 <= f < fc + 2:
            img = fx.borron(img, 18, "h")
    img = capa_rotulos(img, f)
    return capa_subtitulos(img, f)


def _bytes(f):
    return fotograma(f).tobytes()


def _mini(f):
    return fotograma(f).resize((W // 4, H // 4), Image.LANCZOS).tobytes()


def _lum(f):
    return fx.luminosidad(fotograma(f))


def todos_los_textos():
    """Todo lo que se escribe en pantalla (para `revisar_texto.py` y la comprobación de glifos)."""
    ingles = ["Back In", "11 Days?"] + list(FIJOS) + ["4,382 days"] + list(NOMBRES)
    espanol = [" ".join(r[3]) for r in tm.SUBTITULOS]
    return ingles, espanol


def comprobaciones():
    """Lo que se puede comprobar antes de dibujar: glifos, rejilla, contador, textos y subtítulos en su zona, firma."""
    ingles, espanol = todos_los_textos()
    usados = fx.comprobar_glifos(ingles + espanol + ["0123456789,", DIAS])
    assert "≈" not in usados and "→" not in usados
    assert all(abs(c * 2 - round(c * 2)) < 1e-9 for c in tm.CORTES), "un corte no cae en la rejilla de 0,5 s"
    v = [tm.contador(f / FPS) for f in range(N)]
    assert all(b >= a for a, b in zip(v, v[1:])) and max(v) == tm.VALOR_JOBS and min(v) == 0, "contador mal"
    for que, segs in list(FIJOS.items()) + [("contador", (R("4,382"), T(" days"))), ("portada 1", PORTADA_SEGS[0]),
                                            ("portada 2", PORTADA_SEGS[1])]:
        tam = TAM_PORTADA if que.startswith("portada") else TAM_ROTULO
        ancho = fx.ancho_texto(tuple(segs), tam) * 1.12
        assert TEXTO_X + ancho <= SEG_X1, f"rótulo fuera de la zona segura: {que} ({TEXTO_X + ancho:.0f} px)"
        assert len("".join(s for s, _ in segs).split()) <= 3, f"rótulo de más de 3 palabras: {que}"
    medidas = []
    for nombre in NOMBRES:
        assert SEG_X0 + 2 + fx.ancho_texto(((nombre, TINTA),), TAM_NOMBRE) * 1.02 <= SEG_X1 and len(nombre.split()) <= 3
    for k, entra, sale, renglones, _ap in tm.SUBTITULOS:
        assert len(renglones) <= 2 and F(sale) - F(entra) >= 30, f"tarjeta {k}: más de 2 renglones o menos de 30 fotogramas"
        assert entra >= C(2) and sale <= C(14), f"tarjeta {k} pisa la portada"
        for r in renglones:
            a = fx.ancho_texto(_linea_sub(r), TAM_SUB)
            assert a <= SUB_MAX, f"tarjeta {k}: «{r}» mide {a:.0f} px (máximo {SUB_MAX})"
            medidas.append((k, r, round(a)))
    firma = fx.comprobar_firma(GEO, N)
    assert firma["pasa"], f"la firma del lápiz bumerán no cumple: {firma}"
    assert tm.E(11) <= DUR - 17 / FPS + 1e-6 and tm.VOZ_ENTRA >= 14 / FPS - 1e-6, "la voz pisa la firma"
    return usados, medidas, firma


def escribir_srt():
    """Reescribe 02_prompt/subtitulos.srt (inglés) y subtitulos_es.srt (español, pista para YouTube) con los tiempos
    reales de la voz. El texto de cada entrada no cambia."""
    import re

    def marca(s):
        ms = int(round(s * 1000))
        return f"{ms // 3600000:02d}:{ms // 60000 % 60:02d}:{ms // 1000 % 60:02d},{ms % 1000:03d}"
    for nombre in ("subtitulos.srt", "subtitulos_es.srt"):
        ruta = PROY / "02_prompt" / nombre
        bloques = [b.strip().split("\n") for b in re.split(r"\n\s*\n", ruta.read_text(encoding="utf-8").strip())]
        assert len(bloques) == 11, f"{nombre}: se esperaban 11 entradas"
        out = []
        for i, b in enumerate(bloques, 1):
            fin = min(tm.E(i) + 0.05, tm.L(i + 1) - 0.02) if i < 11 else tm.E(i) + 0.05
            out.append(f"{i}\n{marca(tm.L(i))} --> {marca(fin)}\n" + "\n".join(b[2:]))
        ruta.write_text("\n\n".join(out) + "\n", encoding="utf-8")


def hoja(ruta, cada=15, cols=8):
    fs = list(range(0, N, cada))
    with Pool(4) as pool:
        imgs = pool.map(_mini, fs)
    w, h = W // 4, H // 4
    lienzo = Image.new("RGB", (cols * w, math.ceil(len(fs) / cols) * h), "#888888")
    for i, b in enumerate(imgs):
        lienzo.paste(Image.frombytes("RGB", (w, h), b), ((i % cols) * w, (i // cols) * h))
    lienzo.save(ruta, quality=88)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--hoja", help="solo una hoja de contacto rápida (JPG)")
    ap.add_argument("--cada", type=int, default=15)
    ap.add_argument("--fotograma", nargs=2, metavar=("N", "PNG"), help="guarda un solo fotograma")
    ap.add_argument("--tira", nargs=3, metavar=("DESDE", "HASTA", "JPG"), help="tira de fotogramas seguidos (a 1/3)")
    ap.add_argument("--medir-subtitulos", metavar="TXT", help="mide el hueco panel-cabezas en todos los fotogramas")
    ap.add_argument("--sin-audio", action="store_true", help="no rehace el diálogo ni el audio (usa 05_audio/mezcla.wav)")
    a = ap.parse_args()

    usados, medidas, firma = comprobaciones()
    print(f"palitos.py {palitos.VERSION}, efectos.py {fx.VERSION}. Glifos comprobados en Inter Display Medium: {''.join(usados)}")
    print(f"{N} fotogramas ({DUR} s). Cortes: {tm.CORTES}. Pico en {tm.LLEGA:.2f} s ({100 * tm.LLEGA / DUR:.1f} %).")
    print("Subtítulos (px por renglón, máximo 856):", ", ".join(f"{k}: {w}" for k, _, w in medidas))
    print("Firma del lápiz bumerán:", firma)
    if a.fotograma:
        fotograma(int(a.fotograma[0])).save(a.fotograma[1])
        return
    if a.medir_subtitulos:
        lineas, pasa = medir_subtitulos()
        Path(a.medir_subtitulos).write_text("\n".join(lineas) + "\n", encoding="utf-8")
        print("\n".join(lineas))
        sys.exit(0 if pasa else 1)
    if a.tira:
        d, h = int(a.tira[0]), int(a.tira[1])
        fs = [f % N for f in range(d, h + 1)]
        cols = 6
        w3, h3 = W // 3, H // 3
        lienzo = Image.new("RGB", (cols * w3, math.ceil(len(fs) / cols) * h3), "#888888")
        for i, f in enumerate(fs):
            lienzo.paste(fotograma(f).resize((w3, h3), Image.LANCZOS), ((i % cols) * w3, (i // cols) * h3))
        lienzo.save(a.tira[2], quality=88)
        return
    if a.hoja:
        hoja(a.hoja, a.cada)
        return

    inicio = time.time()
    if not a.sin_audio:
        import armar_dialogo
        import audio
        armar_dialogo.main()
        audio.main()
    escribir_srt()
    mezcla = PROY / "05_audio" / "mezcla.wav"
    SALIDA.parent.mkdir(exist_ok=True)
    cmd = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
           "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
           "-i", str(mezcla),
           "-vf", "scale=out_color_matrix=bt709:out_range=tv,format=yuv420p",
           "-c:v", "libx264", "-preset", "medium", "-crf", "16", "-pix_fmt", "yuv420p", "-r", str(FPS),
           "-colorspace", "bt709", "-color_primaries", "bt709", "-color_trc", "bt709", "-color_range", "tv",
           "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
           "-t", f"{DUR}", "-map_metadata", "-1", "-fflags", "+bitexact", "-flags:v", "+bitexact", "-flags:a", "+bitexact",
           "-movflags", "+faststart", str(SALIDA)]
    ff = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    lums = []
    with Pool(4) as pool:
        for i, datos in enumerate(pool.imap(_bytes, range(N), chunksize=4)):
            ff.stdin.write(datos)
            lums.append(fx.luminosidad(Image.frombytes("RGB", (W, H), datos)))
            if i % 150 == 0:
                print(f"  fotograma {i}/{N}  ({time.time() - inicio:.0f} s)", flush=True)
    ff.stdin.close()
    if ff.wait() != 0:
        sys.exit("ffmpeg falló")
    # seguridad: destellos sobre todos los fotogramas, con margen (máximo 2 cambios bruscos por segundo; el límite es 3)
    d = fx.comprobar_destellos(lums + [lums[0]], max_por_segundo=2, estricto=False)
    rev = PROY / "07_revision" / "vuelta_02"
    rev.mkdir(parents=True, exist_ok=True)
    import json
    (rev / "destellos.json").write_text(json.dumps(d, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Destellos: {d['cambios_bruscos']} cambios bruscos (fotogramas {d['fotogramas_con_cambio']}), máximo "
          f"{d['max_cambios_en_1_s']} en 1 s, mayor salto de luminosidad {d['mayor_salto_de_luminosidad']} de 255: "
          f"{'PASA' if d['pasa'] else 'NO PASA'}")
    # bucle: el fotograma N se dibuja con la misma función que el 0; el último (c = -1) es el paso anterior del vuelo
    assert fotograma(N).tobytes() == fotograma(0).tobytes()
    dif = np.abs(np.asarray(fotograma(N - 1), dtype=np.int16) - np.asarray(fotograma(0), dtype=np.int16))
    print(f"Bucle: último fotograma frente al 0: diferencia media {dif.mean():.3f} de 255 (un paso del vuelo del lápiz)")
    print(f"Video -> {SALIDA}  ({time.time() - inicio:.0f} s en total)")


if __name__ == "__main__":
    main()
