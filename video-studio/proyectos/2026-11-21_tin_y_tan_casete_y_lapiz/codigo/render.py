#!/usr/bin/env python3
"""Render del short «How many pencil turns to rewind a cassette?» (Tin & Tan), dibujado con código.

Uso (desde la carpeta del proyecto):
    python3 codigo/render.py                      # audio + 900 fotogramas + 06_final/tin_y_tan_short01_v1.mp4
    python3 codigo/render.py --hoja salida.jpg    # hoja de contacto rápida (un fotograma por pulso), sin video
    python3 codigo/render.py --fotograma 450 f.png

La especificación es 02_prompt/prompt.md. 1080x1920, 30 fps, 900 fotogramas (30,0 s). Todo depende del número de
fotograma. Los personajes salen de herramientas/palitos.py (dibujar), que dibuja con supermuestreo x3 y reduce.
No usa ningún servicio de pago: Pillow, numpy y ffmpeg.
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
from PIL import Image, ImageDraw, ImageFilter, ImageFont

PROY = Path(__file__).resolve().parent.parent
ESTUDIO = PROY.parent.parent
sys.path.insert(0, str(ESTUDIO / "herramientas"))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import palitos  # noqa: E402  (el diseño de Tin y Tan; no se modifica)
from palitos import PALETA, SS, Lienzo, Pluma  # noqa: E402

W, H, FPS, N = 1080, 1920, 30, 900
SALIDA = PROY / "06_final" / "tin_y_tan_short01_v1.mp4"
FUENTE = "/usr/share/fonts/opentype/inter/InterDisplay-Medium.otf"   # Inter Display Medium, SIL OFL 1.1

PAPEL, SOMBRA, TINTA = PALETA["papel"], PALETA["papel_sombra"], PALETA["tinta"]
MARRON, MOSTAZA, TOMATE, BLANCO = PALETA["marron"], PALETA["mostaza"], PALETA["tomate"], PALETA["blanco"]

# Zona segura (formatos.md): centro de 880x1420
SEG_X0, SEG_X1, SEG_Y0, SEG_Y1 = 100, 980, 250, 1670
SUELO = 0.80 * H                 # 1536
ALTO_PJ = 0.34 * H               # 653
X_TAN, X_TIN = 0.30 * W, 0.70 * W

# Cortes (s). Todos caen en la rejilla de 0,5 s.
CORTES = [0.0, 0.5, 1.0, 3.5, 5.0, 6.5, 9.5, 12.0, 14.5, 17.0, 18.5, 20.5, 23.5, 25.5, 27.0, 28.0, 30.0]
BORRONES = [1.0, 5.0, 9.5, 12.0, 17.0, 18.5, 23.5, 28.0]     # cortes con «borrón» según la sección 6
BORRON_PX = 18

# ---------------------------------------------------------------- movimiento
POP, SLIDE, SELLO = (220.0, 20.0), (120.0, 16.0), (320.0, 26.0)   # (rigidez, amortiguación), masa 1


def muelle(t, kc, m=1.0):
    """Respuesta de un muelle amortiguado que va de 0 a 1 (se pasa un poco y vuelve). t en segundos."""
    if t <= 0:
        return 0.0
    k, c = kc
    w0 = math.sqrt(k / m)
    z = c / (2 * math.sqrt(k * m))
    wd = w0 * math.sqrt(1 - z * z)
    return 1 - math.exp(-z * w0 * t) * (math.cos(wd * t) + z * w0 / wd * math.sin(wd * t))


def muelle_exacto(t, kc, dur):
    """Igual, pero normalizado para valer exactamente 1 en t = dur (para llegar justo a una pose)."""
    return muelle(min(t, dur), kc) / muelle(dur, kc)


def clamp(u, a=0.0, b=1.0):
    return max(a, min(b, u))


def eo(u):
    """Ease-out cúbico: no se pasa ni retrocede."""
    u = clamp(u)
    return 1 - (1 - u) ** 3


def eio(u):
    u = clamp(u)
    return 4 * u ** 3 if u < 0.5 else 1 - (-2 * u + 2) ** 3 / 2


def lerp(a, b, p):
    return a + (b - a) * p


# ---------------------------------------------------------------- dibujo con transformación (sobre el lienzo x3)
class Marco:
    """Sistema local: origen en (cx, cy) px del cuadro, escala y rotación (grados, sentido horario en pantalla)."""

    def __init__(self, lz, cx, cy, esc=1.0, rot=0.0):
        self.lz, self.d = lz, lz.d
        self.cx, self.cy, self.esc, self.rot = cx, cy, esc, rot
        a = math.radians(rot)
        self.ca, self.sa = math.cos(a), math.sin(a)

    def xy(self, x, y):
        """Punto local -> píxeles del cuadro (sin supermuestreo)."""
        return (self.cx + self.esc * (x * self.ca - y * self.sa), self.cy + self.esc * (x * self.sa + y * self.ca))

    def p(self, x, y):
        X, Y = self.xy(x, y)
        return (X * SS, Y * SS)

    def poli(self, pts, relleno):
        self.d.polygon([self.p(*q) for q in pts], fill=relleno)

    def disco(self, x, y, r, relleno):
        X, Y = self.p(x, y)
        R = r * self.esc * SS
        self.d.ellipse([X - R, Y - R, X + R, Y + R], fill=relleno)

    def linea(self, pts, ancho, relleno):
        P = [self.p(*q) for q in pts]
        w = max(1, int(round(ancho * self.esc * SS)))
        self.d.line(P, fill=relleno, width=w, joint="curve")
        for q in (P[0], P[-1]):
            self.d.ellipse([q[0] - w / 2, q[1] - w / 2, q[0] + w / 2, q[1] + w / 2], fill=relleno)

    def rect(self, x0, y0, x1, y1, relleno, radio=0.0):
        if radio <= 0:
            self.poli([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], relleno)
            return
        pts = []
        for cx, cy, a0 in ((x1 - radio, y0 + radio, -90), (x1 - radio, y1 - radio, 0),
                           (x0 + radio, y1 - radio, 90), (x0 + radio, y0 + radio, 180)):
            for i in range(9):
                a = math.radians(a0 + 90 * i / 8)
                pts.append((cx + radio * math.cos(a), cy + radio * math.sin(a)))
        self.poli(pts, relleno)

    def caja(self, x0, y0, x1, y1, relleno, borde, radio=0.0, tinta=TINTA):
        """Rectángulo con contorno hacia adentro."""
        self.rect(x0, y0, x1, y1, tinta, radio)
        self.rect(x0 + borde, y0 + borde, x1 - borde, y1 - borde, relleno, max(0.0, radio - borde))


def lapiz_grafico(lz, cx, cy, largo_px, angulo, esc=1.0):
    """El lápiz de palitos.lapiz, con su centro en (cx, cy) px y `largo_px` de punta a goma. angulo en grados."""
    if esc <= 0.02:
        return
    r = largo_px * esc / (1.34 * 0.95)          # punta 0,22 y goma 0,12 del cuerpo; cuerpo de 0,95 R
    a = math.radians(angulo)
    pl = Pluma(lz, cx, cy, r)
    palitos.lapiz(pl, -0.05 * 0.95 * math.cos(a), -0.05 * 0.95 * math.sin(a), angulo=angulo, largo=0.95)


def carrete(m, x, y, r, ang):
    """Carrete: disco de tinta con 6 dientes color papel."""
    m.disco(x, y, r, TINTA)
    for i in range(6):
        a = math.radians(ang + 60 * i)
        ux, uy, nx, ny = math.cos(a), math.sin(a), -math.sin(a), math.cos(a)
        r0, r1, h = 0.40 * r, 0.80 * r, 0.11 * r
        m.poli([(x + ux * r0 + nx * h, y + uy * r0 + ny * h), (x + ux * r1 + nx * h, y + uy * r1 + ny * h),
                (x + ux * r1 - nx * h, y + uy * r1 - ny * h), (x + ux * r0 - nx * h, y + uy * r0 - ny * h)], PAPEL)


def casete(lz, cx, cy, ancho, ang, rot=0.0, esc=1.0, lapiz=None, lapiz_esc=1.0, lapiz_dy=0.0):
    """El casete de la sección 5 (ancho W, alto 0,63 W), sin letras. lapiz: None, 'izq' o 'der' (carrete)."""
    m = Marco(lz, cx, cy, ancho * esc, rot)
    m.caja(-0.5, -0.315, 0.5, 0.315, MARRON, 0.012, radio=0.06)
    # etiqueta: blanca, franja tomate arriba y tres rayas. Sin letras.
    m.caja(-0.40, -0.29, 0.40, -0.06, BLANCO, 0.006, radio=0.012)
    m.rect(-0.394, -0.284, 0.394, -0.254, TOMATE)
    for y in (-0.205, -0.158, -0.111):
        m.linea([(-0.33, y), (0.33, y)], 0.008, SOMBRA)
    # ventana y carretes
    m.caja(-0.34, -0.02, 0.34, 0.20, SOMBRA, 0.006, radio=0.02)
    for sx in (-0.17, 0.17):
        carrete(m, sx, 0.09, 0.075, ang)
    for sx in (-0.45, 0.45):
        m.disco(sx, 0.268, 0.018, TINTA)
        m.disco(sx, 0.268, 0.010, SOMBRA)
    if lapiz:
        sx = -0.17 if lapiz == "izq" else 0.17
        X, Y = m.xy(sx, 0.09 + lapiz_dy)
        # largo 0,22 W: gira dentro de la ventana (0,22 W de alto, centrada en el carrete) y no toca la etiqueta
        lapiz_grafico(lz, X, Y, 0.22 * ancho * esc, ang + rot, lapiz_esc)
    return m


def suelo(lz):
    lz.d.line([(SEG_X0 * SS, SUELO * SS), (SEG_X1 * SS, SUELO * SS)], fill=SOMBRA, width=4 * SS)


def corchea(lz, cx, cy, alto, esc=1.0):
    """Corchea mostaza con contorno de tinta. `alto` px de la cabeza a la punta de la plica."""
    m = Marco(lz, cx, cy, alto * esc, 0)
    cab = [(-0.10 + 0.21 * math.cos(a) * math.cos(-0.35) - 0.15 * math.sin(a) * math.sin(-0.35),
            0.36 + 0.21 * math.cos(a) * math.sin(-0.35) + 0.15 * math.sin(a) * math.cos(-0.35))
           for a in [2 * math.pi * i / 40 for i in range(40)]]
    cab_ext = [(-0.10 + (x + 0.10) * 1.28, 0.36 + (y - 0.36) * 1.38) for x, y in cab]
    plica = [(0.07, 0.33), (0.07, -0.44)]
    bandera = [(0.07, -0.44), (0.20, -0.33), (0.28, -0.17), (0.25, -0.02)]
    m.poli(cab_ext, TINTA)
    m.linea(plica, 0.19, TINTA)
    m.linea(bandera, 0.19, TINTA)
    m.poli(cab, MOSTAZA)
    m.linea(plica, 0.09, MOSTAZA)
    m.linea(bandera, 0.09, MOSTAZA)


def lapiz_de_mano(lz, x, suelo_y, alto, pose, giro):
    """El lápiz de Tin, dibujado aparte para poder moverlo ±3 grados (toma 9). Repite la cuenta de palitos.dibujar:
    la mano derecha de la pose y palitos.lapiz en el mismo sitio, girado alrededor de la mano."""
    R = alto / (2 + palitos.CUELLO + palitos.TORSO + palitos.MUSLO + palitos.PIERNA + 0.25)
    hombro = (0, -(palitos.MUSLO + palitos.PIERNA) - palitos.TORSO + 0.22)
    a1, a2 = palitos.POSES[pose]["bd"]
    codo = palitos.segmento(hombro, a1, palitos.BRAZO, 1)
    mano = palitos.segmento(codo, a2, palitos.ANTEBRAZO, 1)
    base = -60 if pose in ("saluda", "celebra", "pregunta") else -35
    g = math.radians(giro)
    ox, oy = 0.05, -0.25                              # del centro del lápiz a la mano, como en palitos.dibujar
    cx = mano[0] + ox * math.cos(g) - oy * math.sin(g)
    cy = mano[1] + ox * math.sin(g) + oy * math.cos(g)
    palitos.lapiz(Pluma(lz, x, suelo_y, R), cx, cy, angulo=base + giro)


# ---------------------------------------------------------------- texto (capa aparte, no escala con la cámara)
TEXTO_X = 0.10 * W          # 108 px
TEXTO_Y = 0.15 * H          # 288 px: tope de las letras altas
TRAZO_EM = 0.05             # trazo de tinta de la palabra clave (mostaza sobre crema no contrasta)
ANCHO_MAX = (SEG_X1 - TEXTO_X) / 1.012     # el pop se pasa menos de 1 %: que ni así salga de la zona segura


@lru_cache(maxsize=64)
def fuente(tam):
    return ImageFont.truetype(FUENTE, tam)


def comprobar_glifos(textos):
    """Ningún cuadrado: cada carácter que se usa tiene que estar en la fuente (se compara con el glifo vacío)."""
    f = fuente(120)
    vacio = bytes(f.getmask("￿"))
    usados = sorted(set("".join(textos)) - {" "})
    faltan = [c for c in usados if bytes(f.getmask(c)) == vacio or f.getmask(c).getbbox() is None]
    if faltan or "≈" in usados or "→" in usados:
        sys.exit(f"La fuente no tiene estos caracteres (o están prohibidos): {faltan}")
    return usados


def _avances(f, s, col, tam):
    """Avance de cada carácter (px x3). La palabra con trazo lleva un espacio extra entre letras del ancho del trazo,
    para que los contornos de dos letras vecinas no se peguen."""
    if col in (MOSTAZA,):
        extra = TRAZO_EM * tam * SS
        return [f.getlength(c) + (extra if i < len(s) - 1 else 0) for i, c in enumerate(s)]
    return [f.getlength(s)]


def ancho_texto(segs, tam):
    f = fuente(int(round(tam * SS)))
    return sum(sum(_avances(f, s, col, tam)) for s, col in segs) / SS


@lru_cache(maxsize=512)
def imagen_texto(segs, tam):
    """segs: tupla de (texto, color). Los colores mostaza llevan trazo de tinta. Devuelve (RGBA x3, margen, línea base)."""
    f = fuente(int(round(tam * SS)))
    sw = max(1, int(round(TRAZO_EM * tam * SS)))
    asc, desc = f.getmetrics()
    margen = sw + 4
    ancho = int(ancho_texto(segs, tam) * SS) + 2 * margen + 4
    img = Image.new("RGBA", (ancho, asc + desc + 2 * margen), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    x = float(margen)
    for s, col in segs:
        if col == MOSTAZA:
            for c, av in zip(s, _avances(f, s, col, tam)):
                d.text((x, margen + asc), c, font=f, fill=col, anchor="ls", stroke_width=sw, stroke_fill=TINTA)
                x += av
        else:
            d.text((x, margen + asc), s, font=f, fill=col, anchor="ls")
            x += f.getlength(s)
    return img, margen, margen + asc


def ajustar(segs, pct):
    """Tamaño en px para el porcentaje del alto pedido; si el texto no cabe en la zona segura, se reduce lo justo."""
    tam = pct / 100 * H
    a = ancho_texto(segs, tam) + TRAZO_EM * tam
    if a > ANCHO_MAX:
        tam *= ANCHO_MAX / a
    return tam


# (entra, sale, tamaño en % del alto, segmentos). Texto exacto de la tabla de la sección 12.
def K(s):
    return (s, MOSTAZA)


def T(s):
    return (s, TINTA)


TEXTOS = [
    (0.2, 1.3, 6, (T("how many "), K("turns"), T("?"))),
    (1.5, 3.4, 5, (T("rewinding a "), K("cassette"))),
    (3.7, 6.4, 5, (T("how many "), K("turns"), T("?"))),
    (6.8, 9.4, 5, (K("45"), T(" min/side"))),
    (9.6, 11.9, 5, (K("4.76"), T(" cm/s"))),
    (12.2, 14.4, 7, "metros"),
    (14.7, 16.9, 5, (K("11"), T(" cm"))),
    (17.1, 18.4, 5, (K("128.5"), T(" m"))),
    (18.6, 20.3, 5, (T("÷ "), K("11"), T(" cm"))),
    (20.6, 23.4, 7, "vueltas"),
    (23.6, 25.4, 5, (K("2"), T(" turns/s"))),
    (25.6, 26.9, 5, (T("almost "), K("10"), T(" min"))),
    (27.1, 27.9, 5, (T("for one "), K("song"))),
]
CONTADOR_M = (12.2, 14.2, 128.5)       # de 0.0 a 128.5, ease-out cúbico, un decimal
CONTADOR_V = (20.6, 22.9, 1170)        # de 0 a 1,170, ease-out cúbico, enteros


def valor_metros(f):
    t0, t1, fin = CONTADOR_M
    return round(fin * 10 * eo((f / FPS - t0) / (t1 - t0))) / 10


def valor_vueltas(f):
    t0, t1, fin = CONTADOR_V
    return int(round(fin * eo((f / FPS - t0) / (t1 - t0))))


def segmentos(f, que):
    if que == "metros":
        return (K(f"{valor_metros(f):.1f}"), T(" m"))
    if que == "vueltas":
        v = valor_vueltas(f)
        return ((f"{v:,}", TOMATE if v >= CONTADOR_V[2] else MOSTAZA), T(" turns"))
    return que


def capa_texto(base, f):
    """Pega sobre `base` (RGB 1080x1920) el texto que toca en el fotograma f."""
    t = f / FPS
    for entra, sale, pct, que in TEXTOS:
        fi, fs = int(round(entra * FPS)), int(round(sale * FPS))
        if not (fi <= f < fs):
            continue
        segs = segmentos(f, que)
        ref = segs if not isinstance(que, str) else ((K("128.5"), T(" m")) if que == "metros" else (K("1,170"), T(" turns")))
        tam = ajustar(ref, pct)
        esc = 0.85 + 0.15 * muelle(t - entra, POP)              # pop de 0,85 a 1
        alfa = min(1.0, (f - fi + 1) / 2)
        dy = 0.0
        if que == "vueltas" and t >= CONTADOR_V[1]:             # al llegar a 1,170: pop de escala solo del texto
            esc *= 1 + 0.14 * (1 - muelle(t - CONTADOR_V[1], POP))
        if f >= fs - 3:                                         # salida: sube 2 % con ease-in en 3 fotogramas
            u = (f - (fs - 3) + 1) / 4
            dy = -0.02 * H * u * u
            alfa *= 1 - u * u
        img, margen, linea = imagen_texto(segs, tam)
        k = esc / SS
        chico = img.resize((max(1, int(round(img.width * k))), max(1, int(round(img.height * k)))), Image.LANCZOS)
        # ancla: borde izquierdo y media altura de las minúsculas; el tope de las letras altas queda en y = 15 %
        base_y = TEXTO_Y + 0.74 * tam
        ancla_y = base_y - 0.30 * tam
        x = TEXTO_X - margen * k
        y = ancla_y + dy - (linea - 0.30 * tam * SS) * k
        if alfa < 1:
            a = chico.getchannel("A").point(lambda v: int(v * alfa))
            chico.putalpha(a)
        base.paste(chico, (int(round(x)), int(round(y))), chico)
    return base


# ---------------------------------------------------------------- tomas: cada una dibuja en el lienzo y devuelve la cámara
def toma_1_2(lz, t):
    """Casete entra girando (0,0 a 0,5) y empuje al carrete izquierdo (0,5 a 1,0)."""
    p = muelle(t, SLIDE)
    cy = lerp(0.62, 0.46, p) * H
    m = casete(lz, 0.5 * W, cy, 0.70 * W, 720 * t, rot=-12 * (1 - p), esc=lerp(0.9, 1.0, p))
    if t < 0.5:
        return 1.0, (W / 2, H / 2)
    return 1 + 0.35 * muelle(t - 0.5, SELLO), m.xy(-0.17, 0.09)


def toma_3(lz, t):
    tl = t - 1.0
    suelo(lz)
    casete(lz, 0.5 * W, 0.34 * H, 0.52 * W, 720 * t, lapiz="der" if t >= 2.8 else None,
           lapiz_esc=0.85 + 0.15 * muelle(t - 2.8, POP))
    viento = 0.3 * math.exp(-0.45 * tl) * math.cos(2 * math.pi * 0.9 * tl)
    palitos.dibujar(lz, "tan", 0.5 * W, SUELO, ALTO_PJ, pose="pregunta", expresion="nostalgia", vista="frente",
                    mira=1, viento=viento, espejo=True)
    return 1 + 0.04 * eo(tl / 2.5), (W / 2, H / 2)


def toma_4(lz, t):
    tl = t - 3.5
    m = Marco(lz, W / 2, H / 2)
    r = 0.30 * W
    carrete(m, 0, 0, r, 720 * t)
    lapiz_grafico(lz, W / 2, H / 2, 0.9 * 2 * r, 720 * tl, 0.85 + 0.15 * muelle(tl, POP))
    return 1 + 0.20 * muelle(tl, SELLO), (W / 2, H / 2)


def toma_5(lz, t):
    tl = t - 5.0
    suelo(lz)
    casete(lz, 0.5 * W, 0.34 * H, 0.52 * W, 720 * t)
    p = muelle(tl, SLIDE)
    vel = (muelle(tl + 0.01, SLIDE) - muelle(tl - 0.01, SLIDE)) / 0.02
    palitos.dibujar(lz, "tan", lerp(0.5 * W, X_TAN, p), SUELO, ALTO_PJ, pose="pregunta", expresion="curiosidad",
                    vista="frente", viento=clamp(vel / 4.5, -1, 1) * 0.9, espejo=True)
    if tl < 0.6:
        x = lerp(1.18 * W, X_TIN, muelle_exacto(tl, SLIDE, 0.6))
        bote = -14 * abs(math.sin(math.pi * tl / 0.2))                 # un paso cada 0,2 s
        palitos.dibujar(lz, "tin", x, SUELO + bote, ALTO_PJ, pose="camina", expresion="feliz", vista="perfil", mira=-1)
    else:
        palitos.dibujar(lz, "tin", X_TIN, SUELO, ALTO_PJ, pose="parado", expresion="feliz", vista="frente", objeto=True)
    return 1.0, (W / 2, H / 2)


def toma_6(lz, t):
    tl = t - 6.5
    suelo(lz)
    casete(lz, 0.5 * W, 0.34 * H, 0.52 * W, 0)                         # carretes quietos: respiro
    palitos.dibujar(lz, "tan", X_TAN, SUELO, ALTO_PJ, pose="parado", expresion="curiosidad", vista="frente",
                    viento=0.12 * math.sin(2 * math.pi * 0.5 * tl), espejo=True)
    palitos.dibujar(lz, "tin", X_TIN, SUELO, ALTO_PJ, pose="explica", expresion="feliz", vista="frente", objeto=True)
    return 1 + 0.03 * eo(tl / 3.0), (W / 2, H / 2)


MARCA = 0.12 * W                 # un centímetro dibujado
VEL_CINTA = 4.76 * MARCA         # 4,76 marcas por segundo: es el dato


def toma_7(lz, t):
    tl = t - 9.5
    # arranque con muelle pop; después velocidad constante (la única velocidad lineal de la pieza, por ser el dato)
    pasos = int(round(tl * 600))
    avance = sum(muelle((i + 0.5) / 600, POP) for i in range(pasos)) / 600 * VEL_CINTA
    m = Marco(lz, 0, 0)
    yc, h = 0.45 * H, 0.04 * H
    m.rect(-20, yc - h / 2, W + 20, yc + h / 2, MARRON)
    for y in (yc - h / 2, yc + h / 2):
        m.linea([(-20, y), (W + 20, y)], 6, TINTA)
    x = W / 2 - (avance % MARCA) - 6 * MARCA
    while x < W + 20:
        m.linea([(x, yc - h / 2), (x, yc + h / 2)], 6, TINTA)
        m.linea([(x + MARCA / 2, yc + h / 2), (x + MARCA / 2, yc + h / 2 - 22)], 4, TINTA)
        x += MARCA
    # corchete tomate de un centímetro, fijo en x = 50 %, sin letras
    x0, x1, yb = W / 2 - MARCA / 2, W / 2 + MARCA / 2, yc - h / 2 - 34
    m.linea([(x0, yb + 20), (x0, yb), (x1, yb), (x1, yb + 20)], 8, TOMATE)
    return 1.0, (W / 2, H / 2)


def _camino_cinta():
    filas = [H * (0.33 + 0.10 * i) for i in range(5)]
    r = (filas[1] - filas[0]) / 2
    xi, xd = 0.12 * W + r, 0.88 * W - r
    xc, yc = 0.76 * W, 0.22 * H
    pts = [(xc, yc + 40), (xc, filas[0] - r)]

    def arco(cx, cy, a0, a1, n=24):
        return [(cx + r * math.cos(math.radians(lerp(a0, a1, i / n))), cy + r * math.sin(math.radians(lerp(a0, a1, i / n))))
                for i in range(1, n + 1)]
    pts += arco(xc - r, filas[0] - r, 0, 90)
    for i in range(5):
        if i % 2 == 0:                                   # hacia la izquierda
            pts.append((xi if i < 4 else 0.12 * W, filas[i]))
            if i < 4:
                pts += arco(xi, filas[i] + r, -90, -270)
        else:                                            # hacia la derecha
            pts.append((xd, filas[i]))
            pts += arco(xd, filas[i] + r, -90, 90)
    largos = [0.0]
    for a, b in zip(pts, pts[1:]):
        largos.append(largos[-1] + math.hypot(b[0] - a[0], b[1] - a[1]))
    return pts, largos


CAMINO, LARGOS = _camino_cinta()


def toma_8(lz, t, f):
    frac = valor_metros(f) / CONTADOR_M[2]               # el largo dibujado es proporcional al contador
    m = Marco(lz, 0, 0)
    meta = LARGOS[0] + 60 + frac * (LARGOS[-1] - 60)     # los primeros 60 px quedan bajo el casete
    pts = [CAMINO[0]]
    for i in range(1, len(CAMINO)):
        if LARGOS[i] <= meta:
            pts.append(CAMINO[i])
        else:
            u = (meta - LARGOS[i - 1]) / (LARGOS[i] - LARGOS[i - 1])
            pts.append((lerp(CAMINO[i - 1][0], CAMINO[i][0], u), lerp(CAMINO[i - 1][1], CAMINO[i][1], u)))
            break
    m.linea(pts, 0.01 * W, MARRON)
    casete(lz, 0.76 * W, 0.22 * H, 0.24 * W, 720 * t)
    return 1.0, (W / 2, H / 2)


def toma_9(lz, t):
    tl = t - 14.5
    suelo(lz)
    # diagrama: carrete de 160 px con el lápiz que da una vuelta, arco tomate y segmento de 11 cm
    cx, cy, r = 0.22 * W, 0.35 * H, 80.0
    u1 = eio((t - 14.8) / 1.0)
    u2 = eo((t - 15.8) / 0.8)
    ang = -90 + 360 * u1
    m = Marco(lz, cx, cy)
    carrete(m, 0, 0, r, ang)
    caja_arco = [(cx - r - 1.5) * SS, (cy - r - 1.5) * SS, (cx + r + 1.5) * SS, (cy + r + 1.5) * SS]
    a0, a1 = -90 + 360 * u2, -90 + 360 * u1
    if a1 - a0 > 0.5:
        lz.d.arc(caja_arco, a0, a1, fill=TOMATE, width=3 * SS)
    if u2 > 0:
        x0, largo = 0.34 * W, 2 * math.pi * r            # 503 px: de x = 34 % a x = 80,6 %
        Marco(lz, 0, 0).linea([(x0, cy), (x0 + largo * u2, cy)], 3, TOMATE)
    lapiz_grafico(lz, cx, cy, 0.9 * 2 * r, ang)
    palitos.dibujar(lz, "tan", X_TAN, SUELO, ALTO_PJ, pose="parado", expresion="curiosidad", vista="frente",
                    viento=0.1 * math.sin(2 * math.pi * 0.5 * tl), espejo=True)
    palitos.dibujar(lz, "tin", X_TIN, SUELO, ALTO_PJ, pose="explica", expresion="feliz", vista="frente", objeto=False)
    tau = tl if t < 15.8 else t - 15.8                  # el lápiz de la mano se sacude al empezar y al desenrollar
    lapiz_de_mano(lz, X_TIN, SUELO, ALTO_PJ, "explica", 3 * math.exp(-1.6 * tau) * math.sin(2 * math.pi * 2.0 * tau))
    return 1.0, (W / 2, H / 2)


def toma_10(lz, t):
    tl = t - 17.0
    suelo(lz)
    palitos.dibujar(lz, "tin", 0.5 * W, SUELO, 0.44 * H, pose="piensa", expresion="pensando", vista="frente",
                    objeto=False)
    return 1 + 0.06 * muelle(tl, SELLO), (W / 2, H / 2)


def toma_11(lz, t):
    m = Marco(lz, 0, 0)
    x0, x1, yc, h = 0.10 * W, 0.90 * W, 0.40 * H, 0.04 * H
    m.caja(x0, yc - h / 2, x1, yc + h / 2, MARRON, 5, radio=6)
    relleno = eo((t - 20.1) / 0.3)
    if relleno > 0:                                      # cuadrícula densa dentro de los 64 tramos
        yy = h / 2 - 5
        for i in range(1, 256):
            if i % 4:
                x = lerp(x0, x1, i / 256)
                m.linea([(x, yc - yy * relleno), (x, yc + yy * relleno)], 1.4, TOMATE)
    for nivel in range(1, 7):                            # 2, 4, 8, 16, 32 y 64 tramos: un paso cada 0,25 s
        p = muelle(t - (18.6 + 0.25 * (nivel - 1)), POP)
        if p <= 0:
            continue
        extra = (26, 20, 14, 9, 4, 0)[nivel - 1]
        for i in range(1, 2 ** nivel, 2):
            x = lerp(x0, x1, i / 2 ** nivel)
            alto = (h / 2 + extra) * p
            m.linea([(x, yc - alto), (x, yc + alto)], 3, TOMATE)
    return 1.0, (W / 2, H / 2)


def toma_12(lz, t):
    tl = t - 20.5
    suelo(lz)
    tau = tl if t < 22.9 else t - 22.9
    viento = 0.9 * math.exp(-1.3 * tau) * math.cos(2 * math.pi * 1.5 * tau)
    palitos.dibujar(lz, "tan", X_TAN, SUELO, ALTO_PJ, pose="celebra", expresion="sorpresa", vista="frente",
                    viento=viento, espejo=True)
    palitos.dibujar(lz, "tin", X_TIN, SUELO, ALTO_PJ, pose="saluda", expresion="eureka", vista="frente", objeto=True)
    return 1 + 0.02 * muelle(tl, SELLO), (W / 2, H / 2)


def reloj(lz, ang_lapiz, ang_aguja):
    """Cronómetro de 10 minutos: 10 marcas mayores y 50 menores, la de las 10 (arriba) en tomate, sin números."""
    D = 0.62 * W
    R = D / 2
    m = Marco(lz, 0.5 * W, 0.44 * H)
    m.caja(-36, -R - 40, 36, -R + 12, SOMBRA, 6, radio=10)          # botón
    m.disco(0, 0, R, TINTA)
    m.disco(0, 0, R - 0.012 * D, BLANCO)
    for i in range(60):
        a = math.radians(-90 + 6 * i)
        ux, uy = math.cos(a), math.sin(a)
        mayor = i % 6 == 0
        r0 = R * (0.78 if mayor else 0.86)
        col, ancho = (TOMATE, 12) if i == 0 else ((TINTA, 8) if mayor else (TINTA, 3))
        m.linea([(ux * r0, uy * r0), (ux * R * 0.92, uy * R * 0.92)], ancho, col)
    a = math.radians(-90 + ang_aguja)
    m.linea([(0, 0), (math.cos(a) * R * 0.74, math.sin(a) * R * 0.74)], 12, TOMATE)
    m.disco(0, 0, 20, TINTA)
    lapiz_grafico(lz, 0.5 * W, 0.44 * H, 0.40 * D, ang_lapiz)


def toma_13(lz, t):
    reloj(lz, 720 * (t - 23.5), 0)
    return 1.0, (W / 2, H / 2)


def toma_14(lz, t):
    # el lápiz sigue hasta 25,6 y se detiene con muelle pop (se pasa y vuelve); la aguja recorre 351 grados sin pasarse
    if t < 25.6:
        ang = 720 * (t - 25.5)
    else:
        tau = t - 25.6
        k, c = POP
        w0, z = math.sqrt(k), c / (2 * math.sqrt(k))
        wd = w0 * math.sqrt(1 - z * z)
        ang = 72 + 720 / wd * math.exp(-z * w0 * tau) * math.sin(wd * tau)
    reloj(lz, ang, 351 * eo((t - 25.6) / 1.0))
    return 1.0, (W / 2, H / 2)


NOTA_Y = 0.242 * H     # 465 px: el prompt pide 26 %, pero a esa altura la corchea pisa la etiqueta (ver decisiones)


def toma_15(lz, t):
    tl = t - 27.0
    suelo(lz)
    casete(lz, 0.5 * W, 0.34 * H, 0.40 * W, 720 * t)
    if t >= 27.1:
        tau = t - 27.1
        salto = -12 * math.exp(-4 * tau) * abs(math.sin(2 * math.pi * 2 * tau))
        corchea(lz, 0.5 * W, NOTA_Y + salto, 0.08 * W, 0.85 + 0.15 * muelle(tau, POP))
    palitos.dibujar(lz, "tan", X_TAN, SUELO, ALTO_PJ, pose="encoge", expresion="risa", vista="frente",
                    viento=0.4 * math.exp(-2 * tl) * math.cos(2 * math.pi * 2 * tl), espejo=True)
    palitos.dibujar(lz, "tin", X_TIN, SUELO, ALTO_PJ, pose="celebra", expresion="risa", vista="frente", objeto=True)
    return 1.0, (W / 2, H / 2)


def toma_16(lz, t):
    # igual que la toma 1 al revés: en 29,4 sale el lápiz y el casete baja a la pose del fotograma 0
    p = muelle_exacto(t - 29.4, SLIDE, 0.6) if t > 29.4 else 0.0
    u = clamp((t - 29.4) / 0.2)
    casete(lz, 0.5 * W, lerp(0.46, 0.62, p) * H, 0.70 * W, 720 * t, rot=-12 * p, esc=lerp(1.0, 0.9, p),
           lapiz="izq" if u < 1 else None, lapiz_esc=1 - u * u, lapiz_dy=-0.04 * u * u)
    return 1.0, (W / 2, H / 2)


def toma_de(f):
    t = f / FPS
    for i in range(len(CORTES) - 1):
        if CORTES[i] <= t < CORTES[i + 1]:
            return i + 1
    return 16


def borron_horizontal(img, px):
    """Desenfoque de movimiento horizontal (media móvil de `px` píxeles)."""
    a = np.asarray(img, dtype=np.float32)
    izq, der = px // 2, px - px // 2
    b = np.pad(a, ((0, 0), (izq + 1, der), (0, 0)), mode="edge")
    c = np.cumsum(b, axis=1)
    out = (c[:, px:px + a.shape[1]] - c[:, :a.shape[1]]) / px
    return Image.fromarray(np.clip(out + 0.5, 0, 255).astype(np.uint8))


def fotograma(f):
    """Devuelve el fotograma f (0 a 899) como imagen RGB de 1080x1920."""
    f = f % N                      # el fotograma 900 es el 0: bucle
    t = f / FPS
    n = toma_de(f)
    lz = Lienzo(W, H)
    if n <= 2:
        z, c = toma_1_2(lz, t)
    elif n == 8:
        z, c = toma_8(lz, t, f)
    else:
        z, c = {3: toma_3, 4: toma_4, 5: toma_5, 6: toma_6, 7: toma_7, 9: toma_9, 10: toma_10, 11: toma_11,
                12: toma_12, 13: toma_13, 14: toma_14, 15: toma_15, 16: toma_16}[n](lz, t)
    if abs(z - 1) < 1e-9:
        img = lz.resultado()
    else:                          # empuje de cámara: se recorta el lienzo grande y se reduce (no pierde nitidez)
        x0, y0 = c[0] - c[0] / z, c[1] - c[1] / z
        img = lz.img.resize((W, H), Image.LANCZOS, box=(x0 * SS, y0 * SS, (x0 + W / z) * SS, (y0 + H / z) * SS))
    if n == 13 and t < 24.0:       # revelado desde desenfoque: radio 24 px que baja a 0 en 24,0
        radio = 24 * (1 - eo((t - 23.5) / 0.5))
        if radio > 0.05:
            img = img.filter(ImageFilter.GaussianBlur(radio))
    for corte in BORRONES:         # borrón: 2 fotogramas antes y 2 después del corte
        fc = int(round(corte * FPS))
        if fc - 2 <= f < fc + 2:
            img = borron_horizontal(img, BORRON_PX)
    return capa_texto(img, f)


def _bytes(f):
    return fotograma(f).tobytes()


def todos_los_textos():
    fijos = ["".join(s for s, _ in que) for _, _, _, que in TEXTOS if not isinstance(que, str)]
    return fijos + ["0123456789.,", " m", " turns"]


def comprobaciones():
    """Lo que se puede comprobar antes de dibujar: glifos, rejilla, contadores, textos dentro de la zona segura."""
    usados = comprobar_glifos(todos_los_textos())
    assert all(abs(c * 2 - round(c * 2)) < 1e-9 for c in CORTES), "un corte no cae en la rejilla de 0,5 s"
    vm = [valor_metros(f) for f in range(N)]
    vv = [valor_vueltas(f) for f in range(N)]
    assert all(b >= a for a, b in zip(vm, vm[1:])) and max(vm) == 128.5, "el contador de metros retrocede o se pasa"
    assert all(b >= a for a, b in zip(vv, vv[1:])) and max(vv) == 1170, "el contador de vueltas retrocede o se pasa"
    notas = []
    for entra, sale, pct, que in TEXTOS:
        ref = que if not isinstance(que, str) else ((K("888.8"), T(" m")) if que == "metros" else (K("1,000"), T(" turns")))
        tam = ajustar(ref if not isinstance(que, str) else segmentos(int(sale * FPS) - 1, que), pct)
        ancho = ancho_texto(ref, tam) * (1.14 if que == "vueltas" else 1.0)
        assert TEXTO_X + ancho + TRAZO_EM * tam <= SEG_X1 + 0.5, f"texto fuera de la zona segura: {que}"
        if abs(tam - pct / 100 * H) > 0.01:
            notas.append(f"«{''.join(s for s, _ in ref)}»: {pct} % no cabe; queda en {tam / H * 100:.2f} % ({tam:.1f} px)")
    return usados, notas


def hoja(ruta, cada=15, cols=6):
    """Hoja de contacto rápida: un fotograma por pulso, a un cuarto de tamaño."""
    fs = list(range(0, N, cada))
    with Pool(4) as pool:
        imgs = pool.map(_mini, fs)
    w, h = W // 4, H // 4
    filas = math.ceil(len(fs) / cols)
    lienzo = Image.new("RGB", (cols * w, filas * h), "#888888")
    for i, b in enumerate(imgs):
        lienzo.paste(Image.frombytes("RGB", (w, h), b), ((i % cols) * w, (i // cols) * h))
    lienzo.save(ruta, quality=88)


def _mini(f):
    return fotograma(f).resize((W // 4, H // 4), Image.LANCZOS).tobytes()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--hoja", help="solo una hoja de contacto rápida (JPG)")
    ap.add_argument("--cada", type=int, default=15)
    ap.add_argument("--fotograma", nargs=2, metavar=("N", "PNG"), help="guarda un solo fotograma")
    ap.add_argument("--sin-audio", action="store_true", help="no rehace el audio (usa 05_audio/mezcla.wav)")
    a = ap.parse_args()

    usados, notas = comprobaciones()
    print(f"Glifos comprobados en Inter Display Medium: {''.join(usados)}")
    for n in notas:
        print("  ajuste de tamaño:", n)
    if a.fotograma:
        fotograma(int(a.fotograma[0])).save(a.fotograma[1])
        return
    if a.hoja:
        hoja(a.hoja, a.cada)
        return

    inicio = time.time()
    if not a.sin_audio:
        import audio
        audio.main()
    mezcla = PROY / "05_audio" / "mezcla.wav"
    SALIDA.parent.mkdir(exist_ok=True)
    cmd = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
           "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
           "-i", str(mezcla),
           "-vf", "scale=out_color_matrix=bt709:out_range=tv,format=yuv420p",
           "-c:v", "libx264", "-preset", "medium", "-crf", "16", "-pix_fmt", "yuv420p", "-r", str(FPS),
           "-colorspace", "bt709", "-color_primaries", "bt709", "-color_trc", "bt709", "-color_range", "tv",
           "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
           "-t", "30", "-map_metadata", "-1", "-fflags", "+bitexact", "-flags:v", "+bitexact", "-flags:a", "+bitexact",
           "-movflags", "+faststart", str(SALIDA)]
    ff = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    with Pool(4) as pool:
        for i, datos in enumerate(pool.imap(_bytes, range(N), chunksize=4)):
            ff.stdin.write(datos)
            if i % 150 == 0:
                print(f"  fotograma {i}/{N}  ({time.time() - inicio:.0f} s)", flush=True)
    ff.stdin.close()
    if ff.wait() != 0:
        sys.exit("ffmpeg falló")
    # bucle: el fotograma 900 se dibuja con la misma función que el 0
    assert fotograma(900).tobytes() == fotograma(0).tobytes()
    print(f"Video -> {SALIDA}  ({time.time() - inicio:.0f} s en total)")


if __name__ == "__main__":
    main()
