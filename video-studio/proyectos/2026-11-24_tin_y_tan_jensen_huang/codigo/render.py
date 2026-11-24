#!/usr/bin/env python3
"""Short 3 de Tin & Tan, «Jensen Huang Is Back: GeForce 256 vs RTX 5090», dibujado 100 % con código.

Uso (desde la carpeta del proyecto):
    python3 codigo/render.py                         # audio + 915 fotogramas + 06_final/tin_y_tan_short03_v0_sin_voz.mp4
    python3 codigo/render.py --hoja salida.jpg       # hoja de contacto rápida (un fotograma cada 0,5 s), sin video
    python3 codigo/render.py --fotograma 450 f.png   # un solo fotograma
    python3 codigo/render.py --medidas               # cajas de personajes y textos por toma (zona segura)
    python3 codigo/render.py --sin-audio             # no rehace el audio (usa 05_audio/mezcla.wav)

1080x1920, 30 fps, 30,5 s (915 fotogramas). Es el primer video del canal con profundidad y efectos: cada plano se
compone por capas con `herramientas/efectos.py` (cámara, paralaje, foco, niebla, sombras) y los personajes salen de
`herramientas/palitos.py` 1.3, sin tocarlo. Los objetos (tarjeta de 1999, tarjeta actual, PC, placa base, chip, muro de
4.000 minitarjetas) son genéricos: sin logotipos, sin letras y sin ningún verde. Jensen Huang no aparece dibujado.
No usa ningún servicio de pago: Pillow, numpy y ffmpeg. Todo depende del número de fotograma.

VERSIÓN 0, SIN VOZ: los tiempos de abajo son los ESTIMADOS del prompt (sección 7). Cuando existan las voces y
`armar_dialogo.py` escriba `05_audio/linea_de_tiempo_voz.md`, se reajustan SOLO las tres tablas de aquí arriba
(VOZ, CORTES y MARCAS): todo lo demás (textos, efectos, golpes de sonido, comprobaciones) se calcula a partir de ellas.
"""
import argparse
import json
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
import efectos as fx  # noqa: E402
import palitos  # noqa: E402
from efectos import K, R, T, Camara, Capa, Marco  # noqa: E402
from palitos import PALETA  # noqa: E402

# ================================================================= TABLAS DE TIEMPO (lo único que se reajusta con la voz)
# Líneas de voz: (número, quién, empieza, termina, texto como se lee). ESTIMADOS (prompt, sección 7).
VOZ = [
    (1, "Tan", 0.00, 2.30, "Remember putting one of these in your PC?"),
    (2, "Tin", 2.55, 5.68, "That's the GeForce 256, from 1999."),
    (3, "Tin", 6.08, 9.06, "Nvidia's board brought Jensen Huang back as CEO."),
    (4, "Tan", 9.31, 11.26, "How many of those are in a new one?"),
    (5, "Tin", 11.51, 13.36, "We're counting transistors, not speed."),
    (6, "Tin", 13.61, 16.38, "That card had up to 23 million transistors."),
    (7, "Tin", 16.63, 20.03, "The RTX 5090 has about 92 billion."),
    (8, "Tin", 20.28, 20.98, "Divide them."),
    (9, "Tin", 21.38, 22.48, "More than 4,000."),
    (10, "Tan", 22.73, 24.48, "Four thousand of these in one of those?"),
    (11, "Tin", 24.73, 27.16, "That whole wall, in transistors, is one chip."),
    (12, "Tan", 27.50, 28.80, "Subscribe and count with us."),
]
# Inicio de cada toma (1 a 14) y duración total. Todo en la rejilla de 0,5 s.
CORTES = [0.0, 1.0, 2.5, 6.0, 9.0, 11.5, 13.5, 16.5, 20.0, 21.0, 24.0, 25.5, 27.5, 29.5]
DUR = 30.5
CONTINUAS = (4, 10, 12)          # tomas que siguen el plano anterior sin corte (3-4, 9-10 y 11-12)
# Palabras dentro de una línea (segundo estimado en que empiezan): mueven un texto o un gesto.
MARCAS = {
    "1999": 4.40,                # línea 2: «from nineteen ninety-nine»
    "back_as_ceo": 7.60,         # línea 3: «back as C E O» (a mitad de la toma 4: Tin levanta el lápiz)
    "four_thousand": 22.00,      # línea 9: «four thousand»
}
# =================================================================

W, H, FPS = 1080, 1920, 30
N = int(round(DUR * FPS))        # 915
SALIDA = PROY / "06_final" / "tin_y_tan_short03_v0_sin_voz.mp4"
REVISION = PROY / "07_revision" / "vuelta_00_sin_voz"

PAPEL, SOMBRA, TINTA = PALETA["papel"], PALETA["papel_sombra"], PALETA["tinta"]
MARRON, MOSTAZA, TOMATE = PALETA["marron"], PALETA["mostaza"], PALETA["tomate"]
SEG_X0, SEG_X1, SEG_Y0, SEG_Y1 = fx.SEG_X0, fx.SEG_X1, fx.SEG_Y0, fx.SEG_Y1


def C(n):
    """Segundo en que empieza la toma n (C(15) = final del video)."""
    return CORTES[n - 1] if n <= len(CORTES) else DUR


def L(n):
    """(empieza, termina) de la línea de voz n."""
    return VOZ[n - 1][2], VOZ[n - 1][3]


def F(t):
    return int(round(t * FPS))


# ---------------------------------------------------------------- instantes derivados de las tablas
F_CRECE = 12                                 # toma 1: la tarjeta crece en 12 fotogramas
F_GOLPE_BACK = 6                             # toma 1: golpe de la palabra clave
T_BAJA = C(2) - 4 / FPS                      # la tarjeta empieza a bajar 4 fotogramas antes del corte
T_ASIENTA = C(3) - 0.3                       # toma 2: la tarjeta asienta en la ranura
FOCO = (L(2)[1], L(3)[0])                    # cambio de foco de la tarjeta a Tin, en la pausa entre líneas 2 y 3
T_REVELA = F(L(4)[0]) / FPS                  # toma 5: la tarjeta nueva aparece cuando Tan empieza a hablar
F_REVELA = 8
T_GARABATO = C(6) + 0.45                     # toma 6: el círculo de tinta
F_GARABATO = 12
BARRIDO = (F(C(8)) - 3, F(C(8)) + 3)         # 6 fotogramas alrededor del corte 7 -> 8
SUBIDA = (C(9) + 0.15, L(8)[1])              # subida de sonido bajo «Divide them.»
SILENCIO = (L(8)[1], L(9)[0])                # silencio total de 12 fotogramas antes de la cifra
CONTADOR = (C(10), C(10) + 1.2, 250, 4000)   # (inicio, fin, de, a)
PARED = (C(11), C(11) + 1.0)                 # el muro se llena en 30 fotogramas
PLIEGUE = (C(12), C(12) + 1.2)               # el muro se encoge en 36 fotogramas
F_CONGELA = 22                               # toma 14: congelado con marco
BORRONES = [C(6)]                            # corte con borrón (5 -> 6)
BORRON_PX = 18


def valor_contador(t):
    return fx.contador(t, *CONTADOR)


F_LLEGA = next(f for f in range(N) if valor_contador(f / FPS) == CONTADOR[3])     # primer fotograma con 4,000
T_LLEGA = F_LLEGA / FPS

# ---------------------------------------------------------------- escenario (coordenadas de reposo)
SUELO = 0.86 * H                 # 1651
ALTO_PJ = 0.34 * H               # 653
X_TAN, X_TIN = 0.30 * W, 0.70 * W
ZONA_G = (518.0, 979.0)          # zona de gráficos (27 % a 51 %)
Y_GRAF = 0.39 * H                # 749: centro de los gráficos
APERTURA, CAMPO, NIEBLA = 0.018, 150.0, 0.30


def bote(t, fase=0.0, amp=0.022):
    """Rebote de los personajes al pulso de 0,5 s (del short 2): ningún plano queda congelado."""
    tau = (t / 0.5 + fase) % 1.0
    return 1 + amp * math.exp(-4.0 * tau) * math.sin(math.pi * min(1.0, tau * 5)) + 0.006 * math.sin(2 * math.pi * tau)


def respira(t, fase=0.0):
    """Respiración: amplitud pequeña, para los planos en que hay que leer una cifra."""
    return 1 + 0.006 * math.sin(2 * math.pi * (t / 1.0 + fase))


def vaiven(tl, amp=0.3, f=0.9):
    """Viento de la bufanda de Tan: oscila y se va calmando sin pararse nunca."""
    return amp * (0.6 + 0.4 * math.exp(-0.8 * max(0.0, tl))) * math.cos(2 * math.pi * f * tl)


def sacudida_objeto(tl):
    """Movimiento secundario del lápiz: ±3 grados, una sacudida de muelle por segundo."""
    tau = tl % 1.0
    return 3 * math.exp(-2.2 * tau) * math.sin(2 * math.pi * 2.0 * tau)


def golpe(fl, ida=5, asiento=8):
    """Golpe de escala: sube de 0 a 1 en `ida` fotogramas con frenada y vuelve a 0 en `asiento`. fl = fotogramas
    desde el golpe."""
    if fl <= 0:
        return 0.0
    if fl <= ida:
        return fx.eo(fl / ida)
    return 1 - fx.eio((fl - ida) / asiento)


def region(x0, y0, x1, y1, dens=1.0):
    """Lienzo transparente para dibujar el trozo (x0, y0)-(x1, y1) de la escena a `dens` px por px de reposo."""
    return fx.LienzoCapa(int(round((x1 - x0) * dens)), int(round((y1 - y0) * dens)))


def capa_de(lz, x0, y0, dens, z, salida=1.0, **kw):
    return Capa(lz.resultado(salida), z=z, x=x0, y=y0, esc=dens * salida, **kw)


def cam_hacia(avance, punto, **kw):
    """Cámara que se mete `avance` unidades dejando quieto en pantalla el punto `punto` del plano z = 0."""
    p = 1000.0 / (1000.0 - avance)
    return Camara(x=punto[0] - (punto[0] - W / 2) / p, y=punto[1] - (punto[1] - H / 2) / p, avance=avance, **kw)


def en_pantalla(cam, z, u, v):
    """Dónde cae en pantalla el punto de reposo (u, v) de la capa z."""
    k, tx, ty = cam.proyeccion(z)
    return k * u + tx, k * v + ty


def en_reposo(cam, z, xs, ys):
    """Punto de reposo de la capa z que cae en el píxel (xs, ys)."""
    k, tx, ty = cam.proyeccion(z)
    return (xs - tx) / k, (ys - ty) / k


# ---------------------------------------------------------------- objetos genéricos (sin marcas, sin letras, sin verde)
def tarjeta_1999(lz, x0, y0, ancho, dedos=MOSTAZA, giro=0.0):
    """Tarjeta gráfica genérica de la época, del lado de los componentes. Esquina superior izquierda de la placa en
    (x0, y0); la placa mide ancho x 0,42 ancho y, con los dedos del conector, 0,47 ancho de alto. dedos: color de los
    dedos (mostaza si la tarjeta es el acento del plano; marrón si no) o None (metidos en una ranura: no se ven).
    giro: grados del ventilador."""
    m = Marco(lz, x0, y0, ancho)
    b = 0.012
    if dedos:
        m.caja(0.12, 0.40, 0.74, 0.47, dedos, 0.008)
        for i in range(14):
            x = 0.12 + 0.62 * (i + 1) / 15
            m.rect(x - 0.002, 0.428, x + 0.002, 0.462, TINTA)
    m.caja(0.0, 0.0, 1.0, 0.42, MARRON, b, radio=0.02)
    m.caja(0.0, 0.0, 0.05, 0.42, SOMBRA, b * 0.8, radio=0.008)                 # escuadra metálica
    for y in (0.07, 0.35):
        m.disco(0.025, y, 0.008, TINTA)
    m.anillo(0.36, 0.21, 0.15, b, SOMBRA)                                      # ventilador
    for i in range(5):
        a0 = math.radians(giro + 72 * i)
        pts = []
        for j in range(7):
            u = j / 6
            a = a0 + math.radians(48) * u
            rr = 0.036 + 0.088 * u
            pts.append((0.36 + rr * math.cos(a), 0.21 + rr * math.sin(a)))
        m.linea(pts, 0.022, TINTA)
    m.anillo(0.36, 0.21, 0.034, 0.009, PAPEL)
    for fx0 in (0.64, 0.86):                                                   # memorias: 4 rectángulos de tinta
        for fy0 in (0.085, 0.265):
            m.rect(fx0, fy0, fx0 + 0.07, fy0 + 0.05, TINTA, radio=0.006)
    for cx, cy in ((0.775, 0.11), (0.775, 0.29), (0.585, 0.36)):               # condensadores (neutros)
        m.anillo(cx, cy, 0.017, 0.006, SOMBRA)
    for cy in (0.045, 0.375):                                                  # dos pistas finas
        m.rect(0.60, cy - 0.002, 0.95, cy + 0.002, TINTA)


def tarjeta_actual(lz, x0, y0, ancho, dedos=MARRON, giro=0.0):
    """Tarjeta gráfica genérica moderna: carcasa de tinta con tres ventiladores. La carcasa mide ancho x 0,34 ancho y,
    con los dedos, 0,38 ancho de alto. Sin logotipos, sin letras, sin luces de color."""
    m = Marco(lz, x0, y0, ancho)
    b = 0.012
    if dedos:
        m.caja(0.12, 0.325, 0.74, 0.38, dedos, 0.008)
        for i in range(14):
            x = 0.12 + 0.62 * (i + 1) / 15
            m.rect(x - 0.002, 0.346, x + 0.002, 0.373, TINTA)
    m.rect(0.0, 0.0, 1.0, 0.34, TINTA, radio=0.03)
    m.caja(0.0, 0.0, 0.05, 0.34, SOMBRA, b * 0.8, radio=0.008)                 # escuadra
    for y in (0.06, 0.28):
        m.disco(0.025, y, 0.008, TINTA)
    for i, cx in enumerate((0.2, 0.5, 0.8)):
        m.disco(cx, 0.17, 0.15, SOMBRA)
        for j in range(7):
            a0 = math.radians(giro * (1 if i != 1 else -1) + 360 * j / 7 + 17 * i)
            pts = []
            for q in range(6):
                u = q / 5
                a = a0 + math.radians(40) * u
                rr = 0.04 + 0.095 * u
                pts.append((cx + rr * math.cos(a), 0.17 + rr * math.sin(a)))
            m.linea(pts, 0.012, TINTA)
        m.anillo(cx, 0.17, 0.038, 0.008, MARRON)


def capa_tarjeta(cual, cx, cy, ancho, z=0.0, dedos=MOSTAZA, giro=0.0, sombra=None, dens=1.0, centro_total=True,
                 recorte_y=None, **kw):
    """Capa con una tarjeta centrada en (cx, cy) de reposo. centro_total: el centro vertical es el del objeto con los
    dedos (0,47 o 0,38 del ancho). recorte_y: fila de reposo por debajo de la cual la tarjeta no se ve (la ranura)."""
    alto_total = (0.47 if cual == "1999" else 0.38) * ancho
    alto_placa = (0.42 if cual == "1999" else 0.34) * ancho
    y0 = cy - (alto_total if centro_total else alto_placa) / 2
    x0 = cx - ancho / 2
    m = 12
    lz = region(x0 - m, y0 - m, x0 + ancho + m, y0 + alto_total + m, dens)
    (tarjeta_1999 if cual == "1999" else tarjeta_actual)(lz, m * dens, m * dens, ancho * dens, dedos, giro)
    img = lz.resultado(1.0)
    if recorte_y is not None:
        fila = int(round((recorte_y - (y0 - m)) * dens))
        if fila < img.height:
            a = np.array(img)
            a[max(0, fila):, :, 3] = 0
            img = Image.fromarray(a)
    return Capa(img, z=z, x=x0 - m, y=y0 - m, esc=dens, sombra=sombra, nombre=f"tarjeta_{cual}", **kw)


SOMBRA_FLOTA = dict(dx=14, dy=10, radio=10, opacidad=0.22)


@lru_cache(maxsize=2)
def capa_suelo():
    lz = region(0, SUELO - 10, W, SUELO + 10)
    lz.d.line([(SEG_X0 * 3, 10 * 3), (SEG_X1 * 3, 10 * 3)], fill=SOMBRA, width=4 * 3)
    return capa_de(lz, 0, SUELO - 10, 1.0, 0.0, nombre="suelo")


@lru_cache(maxsize=2)
def capa_suelo_largo():
    """Línea de suelo de los planos con cámara que se mueve: sale del cuadro por los dos lados."""
    lz = region(-300, SUELO - 10, W + 300, SUELO + 10)
    lz.d.line([(0, 10 * 3), ((W + 600) * 3, 10 * 3)], fill=SOMBRA, width=4 * 3)
    return capa_de(lz, -300, SUELO - 10, 1.0, 0.0, nombre="suelo")


Z_PC, Z_PED, Z_CABLE = 420.0, -260.0, -320.0
PED_X = 540.0
PED_TARJETA_W = 420.0
PED_TOPE = 700.0                              # parte alta de la tarjeta sobre el pedestal
PED_PLACA_Y = PED_TOPE + 0.42 * PED_TARJETA_W      # 876: la placa del pedestal (los dedos van dentro de su ranura)
PED_BASE = SUELO + 30.0                       # el pedestal está más cerca: toca el suelo un poco más abajo


@lru_cache(maxsize=2)
def capa_pc_beige():
    """Fondo de las tomas 3 y 4 (z = +420): una mesa con una torre y un monitor de tubo, en siluetas. Sin letras."""
    x0, y0, x1, y1, dens = -300.0, 540.0, 1380.0, 1140.0, 1.0
    lz = region(x0, y0, x1, y1, dens)
    m = Marco(lz, -x0 * dens, -y0 * dens, dens)
    mesa = 1062.0
    m.caja(x0 + 20, mesa, x1 - 20, mesa + 34, SOMBRA, 3.0)
    # torre: 250 x 430
    tx0, tx1, ty0 = 70.0, 320.0, mesa - 430.0
    m.caja(tx0, ty0, tx1, mesa, SOMBRA, 3.0, radio=10)
    for i in range(2):                                                # dos bahías de unidad
        m.rect(tx0 + 34, ty0 + 44 + 62 * i, tx1 - 34, ty0 + 78 + 62 * i, TINTA, radio=4)
    m.disco(tx0 + 60, ty0 + 215, 13, TINTA)
    for i in range(5):                                                # rejilla de ventilación
        m.rect(tx0 + 40, ty0 + 300 + 20 * i, tx1 - 40, ty0 + 306 + 20 * i, TINTA)
    # monitor de tubo: 300 x 270 con su pie
    mx0, mx1, my0 = 730.0, 1030.0, mesa - 300.0
    m.poli_borde([(mx0 + 90, mesa - 36), (mx1 - 90, mesa - 36), (mx1 - 60, mesa), (mx0 + 60, mesa)], SOMBRA, 3.0)
    m.caja(mx0, my0, mx1, mesa - 32, SOMBRA, 3.0, radio=22)
    m.caja(mx0 + 28, my0 + 26, mx1 - 28, mesa - 78, PAPEL, 3.0, radio=30)
    m.disco(mx1 - 44, mesa - 55, 7, TINTA)
    return capa_de(lz, x0, y0, dens, Z_PC, nombre="pc_beige")


@lru_cache(maxsize=2)
def capa_pedestal():
    """Columna de museo (150 px) con su placa (220 x 26 px), de la base de la tarjeta al suelo."""
    x0, y0, x1, y1, dens = PED_X - 130, PED_PLACA_Y - 10, PED_X + 130, PED_BASE + 30, 1.25
    lz = region(x0, y0, x1, y1, dens)
    m = Marco(lz, -x0 * dens, -y0 * dens, dens)
    m.caja(PED_X - 75, PED_PLACA_Y + 20, PED_X + 75, PED_BASE, SOMBRA, 5.0)
    m.caja(PED_X - 95, PED_BASE - 24, PED_X + 95, PED_BASE, SOMBRA, 5.0, radio=3)
    m.caja(PED_X - 110, PED_PLACA_Y, PED_X + 110, PED_PLACA_Y + 26, SOMBRA, 5.0, radio=3)
    return capa_de(lz, x0, y0, dens, Z_PED, nombre="pedestal")


@lru_cache(maxsize=2)
def capa_cable():
    """Primer plano (z = -320): un cable de tinta de 36 px en un lazo grande, abajo a la izquierda, siempre
    desenfocado (el lápiz de Tin no puede ir ahí: es mostaza y competiría con el acento)."""
    x0, y0, x1, y1, dens = -360.0, 1500.0, 620.0, 2200.0, 0.5
    lz = region(x0, y0, x1, y1, dens)
    m = Marco(lz, -x0 * dens, -y0 * dens, dens)
    pts = []
    for i in range(61):
        u = i / 60
        pts.append((-330 + 560 * u + 185 * math.sin(2 * math.pi * u), 1830 + 150 * u - 140 * math.cos(2 * math.pi * u)))
    m.linea(pts, 36, TINTA)
    return capa_de(lz, x0, y0, dens, Z_CABLE, desenfoque=11.0, nombre="cable")


# toma 2: la placa base (z = +60) y la ranura
Z_PLACA, Z_T2, Z_MANOS = 60.0, -120.0, -220.0
T2_W = 700.0
RANURA = (211.0, 1236.0, 771.0, 1280.0)            # x0, y0, x1, y1 de reposo (560 x 44 px)


@lru_cache(maxsize=2)
def capa_placa_base():
    """Placa base vista de cerca: ranura de 560 x 44 px con dos muescas, tres chips de 70 px y dos condensadores.
    Para que se lea como una placa (y no como una caja) lleva además dos ranuras vacías más cortas, un zócalo grande
    y dos bancos de memoria, todo en neutros y sin letras."""
    x0, y0, x1, y1, dens = 60.0, 620.0, 1020.0, 1600.0, 1.0
    lz = region(x0, y0, x1, y1, dens)
    m = Marco(lz, -x0 * dens, -y0 * dens, dens)
    m.caja(100, 660, 980, 1560, SOMBRA, 7.0, radio=14)
    rx0, ry0, rx1, ry1 = RANURA
    m.rect(rx0, ry0, rx1, ry1, TINTA, radio=10)
    for nx in (rx0 + 150, rx1 - 90):                                  # dos muescas
        m.rect(nx, ry0 - 9, nx + 18, ry0 + 4, TINTA)
        m.rect(nx, ry1 - 4, nx + 18, ry1 + 9, TINTA)
    for i, largo in enumerate((430, 430)):                            # ranuras vacías, más cortas
        yy = ry0 + 96 * (i + 1)
        m.rect(rx0, yy, rx0 + largo, yy + 30, TINTA, radio=8)
        m.rect(rx0 + 12, yy + 11, rx0 + largo - 12, yy + 19, SOMBRA)
    m.caja(180, 740, 400, 960, PAPEL, 6.0, radio=8)                   # zócalo
    m.caja(222, 782, 358, 918, SOMBRA, 5.0)
    for i in range(2):                                                # bancos de memoria (verticales)
        xx = 820 + 60 * i
        m.rect(xx, 720, xx + 26, 1120, TINTA, radio=8)
        m.rect(xx + 9, 734, xx + 17, 1106, SOMBRA)
    for cx, cy in ((690, 1380), (790, 1380), (890, 1380)):            # tres chips de tinta de 70 px
        m.rect(cx - 35, cy - 35, cx + 35, cy + 35, TINTA, radio=5)
    for cx, cy in ((690, 1480), (760, 1480)):                         # dos condensadores marrón de 34 px
        m.anillo(cx, cy, 17, 5.0, MARRON)
    for cx, cy in ((128, 688), (952, 688), (128, 1532), (952, 1532)):
        m.anillo(cx, cy, 10, 4.0, PAPEL)
    return capa_de(lz, x0, y0, dens, Z_PLACA, nombre="placa_base")


def capa_manos(izq, der, t):
    """Dos brazos de tinta de 36 px que entran por abajo y terminan en manos de punto de 34 px de radio. izq, der:
    dónde va cada mano (reposo de la capa de las manos). Son las del espectador: no llevan color."""
    x0, y0, x1, y1, dens = -80.0, 700.0, 1160.0, 2140.0, 0.75
    lz = region(x0, y0, x1, y1, dens)
    m = Marco(lz, -x0 * dens, -y0 * dens, dens)
    for (hx, hy), lado in ((izq, -1), (der, 1)):
        osc = math.radians(2.0) * math.sin(2 * math.pi * 1.1 * t + (0.0 if lado < 0 else 1.4))
        hombro = (540 + lado * 620, 2120.0)
        dx, dy = hx - hombro[0], hy - hombro[1]
        codo = (hombro[0] + 0.46 * dx + lado * 90 * math.cos(osc) - dy * math.sin(osc) * 0.2,
                hombro[1] + 0.52 * dy + 60 * math.sin(osc))
        pts = []
        for i in range(21):                                           # curva suave por el codo
            u = i / 20
            pts.append(((1 - u) ** 2 * hombro[0] + 2 * u * (1 - u) * codo[0] + u * u * hx,
                        (1 - u) ** 2 * hombro[1] + 2 * u * (1 - u) * codo[1] + u * u * hy))
        m.linea(pts, 36, TINTA)
        m.disco(hx, hy, 34, TINTA)
    return capa_de(lz, x0, y0, dens, Z_MANOS, salida=1.34, nombre="manos")


DIE_LADO = 320.0
DIE_XY = (540.0, 770.0)


def capa_die(esc=1.0, z=-100.0):
    """El chip visto de cerca: cuadrado mostaza con contorno de tinta y 12 x 12 puntos (144 «interruptores»)."""
    lado = DIE_LADO
    cx, cy = DIE_XY
    m0 = 16
    lz = region(0, 0, lado + 2 * m0, lado + 2 * m0, 1.25)
    m = Marco(lz, (lado / 2 + m0) * 1.25, (lado / 2 + m0) * 1.25, 1.25)
    m.caja(-lado / 2, -lado / 2, lado / 2, lado / 2, MOSTAZA, 8.0, radio=6)
    paso = (lado - 16) / 12
    for i in range(12):
        for j in range(12):
            m.disco(-lado / 2 + 8 + paso * (i + 0.5), -lado / 2 + 8 + paso * (j + 0.5), 0.3 * paso * 1.2, TINTA)
    lado_t = (lado + 2 * m0) * esc
    return Capa(lz.resultado(1.0), z=z, x=cx - lado_t / 2, y=cy - lado_t / 2, esc=1.25 / esc,
                sombra=dict(dx=14, dy=12, radio=12, opacidad=0.24), nombre="die")


PARED_COLS, PARED_FILAS = 80, 50                  # 4.000 minitarjetas, exactas
PARED_W, PARED_H = 880.0, 460.0
PARED_XY = (100.0, 518.0)


@lru_cache(maxsize=1)
def imagen_pared():
    """La pared entera a 2 px por px: 80 x 50 celdas de 11 x 9,2 px; cada minitarjeta es un rectángulo marrón de
    9 x 7,4 px con 2 px de papel de separación y un punto papel_sombra de 3 px (su ventilador)."""
    e = 10                                         # se dibuja a 10 px por px y se reduce
    cw, ch = 110, 92
    celda = Image.new("RGBA", (cw, ch), (0, 0, 0, 0))
    d = ImageDraw.Draw(celda)
    d.rounded_rectangle([10, 9, 10 + 90, 9 + 74], radius=8, fill=MARRON)
    d.ellipse([10 + 22 - 15, 46 - 15, 10 + 22 + 15, 46 + 15], fill=SOMBRA)
    fila = Image.new("RGBA", (cw * PARED_COLS, ch), (0, 0, 0, 0))
    for i in range(PARED_COLS):
        fila.paste(celda, (i * cw, 0))
    fila = fila.resize((int(PARED_W * 2), int(round(ch * 2 / e))), Image.LANCZOS)
    alto_fila = PARED_H * 2 / PARED_FILAS
    out = Image.new("RGBA", (int(PARED_W * 2), int(PARED_H * 2)), (0, 0, 0, 0))
    for j in range(PARED_FILAS):
        out.alpha_composite(fila, (0, int(round(j * alto_fila))))
    return out


def capa_pared(filas=PARED_FILAS, caja=None):
    """La pared con sus primeras `filas` filas, dibujada en `caja` (x0, y0, ancho) de reposo."""
    img = imagen_pared()
    if filas < PARED_FILAS:
        corte = int(round(filas * PARED_H * 2 / PARED_FILAS))
        if corte <= 0:
            return None
        img = img.crop((0, 0, img.width, corte))
    x0, y0, ancho = caja or (PARED_XY[0], PARED_XY[1], PARED_W)
    return Capa(img, z=0.0, x=x0, y=y0, esc=PARED_W * 2 / ancho, nombre="pared")


# ---------------------------------------------------------------- personajes
def mezcla(a, b, p):
    """Intercalado entre dos poses de `palitos.POSES` (para que un cambio de pose dentro de un plano no sea un salto).
    No inventa poses: con p = 0 es `a` y con p = 1 es `b`; lo de en medio dura 6 fotogramas."""
    if p <= 0:
        return a
    if p >= 1:
        return b
    A, B = palitos.POSES[a], palitos.POSES[b]
    palitos.POSES["_intercalado"] = {k: tuple(fx.lerp(A[k][i], B[k][i], p) for i in range(2)) for k in A}
    return "_intercalado"


def cambio(t, t0, dur=6 / FPS):
    """Avance con frenada del cambio de pose que empieza en t0."""
    return fx.eo((t - t0) / dur)


def pj(pid, x, t, pose="parado", expresion="feliz", alto=ALTO_PJ, vista="frente", mira=None, espejo=None, objeto=False,
       giro_objeto=0.0, cabeza_giro=0.0, viento=None, z=0.0, sombra=0.27, dens=1.25, quieto=False):
    """Capas de un personaje (sombra de contacto y figura) con los pies en (x, SUELO)."""
    es_tan = pid == "tan"
    espejo = es_tan if espejo is None else espejo
    mira = (1 if es_tan else -1) if mira is None else mira
    if viento is None:
        viento = 0.0
    if isinstance(pose, tuple):
        pose = mezcla(*pose)
    fase = 0.0 if es_tan else 0.5
    a = alto * (respira(t, fase) if quieto else bote(t, fase))
    w, h = int(alto * 1.6), int(alto * 1.2) + 40
    lz = fx.LienzoCapa(w, h)
    palitos.dibujar(lz, pid, w / 2, h - 30, a, pose=pose, expresion=expresion, vista=vista, mira=mira, viento=viento,
                    objeto=objeto, espejo=espejo, giro_objeto=giro_objeto, cabeza_giro=cabeza_giro)
    capas = []
    if sombra:
        capas.append(fx.capa_sombra_contacto(x, SUELO + 4, 0.42 * alto, z=z, opacidad=sombra))
    capas.append(Capa(lz.resultado(dens), z=z, x=x - w / 2, y=SUELO - (h - 30), esc=dens, nombre=pid))
    return capas


# ---------------------------------------------------------------- texto (pegado a la pantalla: no lo mueve la cámara)
X_T = 0.10 * W               # 108 px
Y_T = 0.14 * H               # 269 px: tope de las letras altas de las filas en (10, 14)
Y_T2 = 0.22 * H              # 422 px: subtítulo fijo bajo la cifra
PORTADA_TAM = 128.0          # 6,7 % del alto
PORTADA_TOPE = 415.0
PORTADA_L2 = PORTADA_TOPE + 0.74 * PORTADA_TAM + 0.42 * PORTADA_TAM       # tope de la segunda línea
ANCHO_MAX = (SEG_X1 - X_T) / 1.012
EQ_X = 0.385 * W             # 416 px: los dos textos de la ecuación
EQ_Y1, EQ_Y2 = 600.0, 770.0


def ajustar(segs, pct, x=X_T):
    """Tamaño en px para el porcentaje del alto pedido; si el texto no cabe en la zona segura, se reduce lo justo."""
    tam = pct / 100 * H
    a = fx.ancho_texto(tuple(segs), tam) + fx.TRAZO_EM * tam
    maximo = (SEG_X1 - x) / 1.012
    if a > maximo:
        tam *= maximo / a
    return tam


def pegar(base, segs, x, tope, tam, esc=1.0, alfa=1.0, dy=0.0, centrado=False):
    """Pega `segs` con el borde izquierdo en x y el tope de las letras altas en `tope`. esc escala alrededor del borde
    izquierdo (o del centro del texto, con centrado=True) y de la media altura de las minúsculas."""
    if alfa <= 0:
        return base
    img, margen, linea = fx.imagen_texto(tuple(segs), tam)
    k = esc / fx.SS
    chico = img.resize((max(1, int(round(img.width * k))), max(1, int(round(img.height * k)))), Image.LANCZOS)
    ancla_y = tope + 0.74 * tam - 0.30 * tam
    y = ancla_y + dy - (linea - 0.30 * tam * fx.SS) * k
    if centrado:
        ancho = fx.ancho_texto(tuple(segs), tam)
        x = x + ancho / 2 - ancho * esc / 2
    if alfa < 1:
        chico.putalpha(chico.getchannel("A").point(lambda v: int(v * alfa)))
    base.paste(chico, (int(round(x - margen * k)), int(round(y))), chico)
    return base


def tope_siguiente(tope, tam, tam_sig):
    """Tope de la línea que va debajo de otra."""
    return tope + 0.74 * tam + 0.34 * tam_sig


CLAVE_PORTADA = K("Back")
LINEAS_PORTADA = ((T("Jensen Huang"),), (T("Is "), CLAVE_PORTADA))

# Filas de texto: id, entra, sale, x, tope y líneas [(% del alto, segmentos)]. Texto exacto de la sección 12 del prompt.
TEXTOS = [
    dict(id="portada", entra=0.0, sale=C(2), x=X_T, tope=PORTADA_TOPE, en_plano=True,
         lineas=[(PORTADA_TAM / H * 100, LINEAS_PORTADA[0]), (PORTADA_TAM / H * 100, LINEAS_PORTADA[1])]),
    dict(id="geforce", entra=F(L(2)[0] + 0.15) / FPS, sale=MARCAS["1999"] - 0.1, lineas=[(7, (T("GeForce "), K("256")))]),
    dict(id="1999", entra=MARCAS["1999"], sale=C(4) - 0.1, lineas=[(7, (K("1999"),))]),
    dict(id="nov23", entra=F(L(3)[0] + 0.12) / FPS, sale=MARCAS["back_as_ceo"] - 0.1, lineas=[(7, (T("Nov "), K("23")))]),
    dict(id="ceo", entra=MARCAS["back_as_ceo"], sale=C(5) - 0.1, lineas=[(7, (T("Back as "), K("CEO")))]),
    dict(id="rtx", entra=F(L(4)[0] + 0.1) / FPS, sale=C(6) - 0.1, lineas=[(7, (T("RTX "), K("5090")))]),
    dict(id="transistores", entra=C(6) + 0.1, sale=C(7) - 0.1, lineas=[(5.5, (K("transistors"), T(","))), (5.5, (T("not speed"),))]),
    dict(id="23m", entra=C(7) + 0.1, sale=C(8) - 0.1, lineas=[(4.5, (T("up to"),)), (7, (K("23"), T(" million")))]),
    dict(id="92b", entra=C(8) + 0.1, sale=C(9) - 0.1, lineas=[(4.5, (T("RTX 5090"),)), (7, (T("≈ "), K("92"), T(" billion")))]),
    dict(id="eq1", entra=C(9) + 0.1, sale=C(11) - 0.1, x=EQ_X, centro_y=EQ_Y1, lineas=[(5.5, (T("≈ 92 billion"),))]),
    dict(id="eq_div", entra=C(9) + 0.2, sale=C(11) - 0.1, x=float(SEG_X0), centro_y=EQ_Y2, lineas=[(5.5, (T("÷"),))]),
    dict(id="eq2", entra=C(9) + 0.2, sale=C(11) - 0.1, x=EQ_X, centro_y=EQ_Y2, lineas=[(5.5, (T("23 million"),))]),
    dict(id="cifra", entra=CONTADOR[0], sale=C(13) - 0.1, lineas=[(7, (R("4,000"), R("+")))]),
    dict(id="no_velocidad", entra=F(L(9)[0]) / FPS, sale=C(13) - 0.1, tope=Y_T2, lineas=[(3.5, (T("transistors, not speed"),))]),
    dict(id="igual", entra=PLIEGUE[1], sale=C(13) - 0.1, x=W / 2, centro_y=Y_GRAF, centrado=True, lineas=[(5.2, (T("="),))]),
    dict(id="suscribe", entra=C(13) + 0.2, sale=C(14) - 0.1, lineas=[(7, (K("Subscribe"),))]),
    dict(id="canal", entra=C(13) + 0.2, sale=C(14) - 0.1, tope=Y_T2, lineas=[(3.8, (T("Tin & Tan"),))]),
]


def geometria(fila):
    """[(tam, x, tope, segs)] de cada línea de una fila."""
    x = fila.get("x", X_T)
    out = []
    tope = fila.get("tope", Y_T)
    previo = None
    for pct, segs in fila["lineas"]:
        tam = ajustar(segs, pct, SEG_X0 if fila.get("centrado") else x)
        if "centro_y" in fila:
            tope = fila["centro_y"] - 0.37 * tam
        elif previo is not None:
            tope = (PORTADA_L2 if fila["id"] == "portada" else tope_siguiente(tope, previo, tam))
        lx = x - fx.ancho_texto(tuple(segs), tam) / 2 if fila.get("centrado") else x
        out.append((tam, lx, tope, segs))
        previo = tam
    return out


def texto_portada(base, fl):
    """«Jensen Huang / Is Back», entero y quieto desde el fotograma 0; en el fotograma 6 «Back» da su golpe (escala
    1,0 a 1,18 en 5 fotogramas y asiento en 7). fl: fotogramas desde el inicio de la toma 1 (negativo en la toma 14)."""
    (tam, x, tope, l1), (_, _, tope2, l2) = geometria(TEXTOS[0])
    pegar(base, l1, x, tope, tam)
    pegar(base, l2[:1], x, tope2, tam)
    xk = x + fx.ancho_texto(tuple(l2[:1]), tam)
    pegar(base, l2[1:], xk, tope2, tam, esc=1 + 0.18 * golpe(fl - F_GOLPE_BACK, 5, 7), centrado=True)
    return base


def capa_texto(base, f):
    """Pega sobre `base` (RGB) las filas de texto que tocan en el fotograma f."""
    t = f / FPS
    for fila in TEXTOS:
        if fila.get("en_plano"):
            continue
        fi, fs = F(fila["entra"]), F(fila["sale"])
        if not (fi <= f < fs):
            continue
        esc = 0.85 + 0.15 * fx.muelle(t - fila["entra"] + 1 / FPS, fx.POP)      # pop de 0,85 a 1
        alfa = min(1.0, (f - fi + 1) / 2)
        dy = 0.0
        if f >= fs - 3:                                                        # salida: sube 2 % en 3 fotogramas
            u = (f - (fs - 3) + 1) / 4
            dy = -min(0.02 * H * u * u, 14.0)
            alfa *= 1 - u * u
        for tam, x, tope, segs in geometria(fila):
            if fila["id"] == "cifra":
                v = valor_contador(t)
                if f < F_LLEGA:
                    pegar(base, (T(f"{v:,}"),), x, tope, tam, esc, alfa, dy)
                else:                                                          # llegó: tomate, y el «+» entra con pop
                    num = (R(f"{v:,}"),)
                    pegar(base, num, x, tope, tam, esc, alfa, dy)
                    xm = x + fx.ancho_texto(num, tam) + fx.TRAZO_EM * tam
                    pegar(base, (R("+"),), xm, tope, tam, esc * fx.muelle((f - F_LLEGA + 1) / FPS, fx.POP),
                          alfa, dy, centrado=True)
            else:
                pegar(base, segs, x, tope, tam, esc, alfa, dy)
    return base


def centro_cifra():
    tam, x, tope, segs = geometria(next(r for r in TEXTOS if r["id"] == "cifra"))[0]
    return (x + fx.ancho_texto(tuple(segs), tam) / 2, tope + 0.37 * tam)


# ---------------------------------------------------------------- tomas: cada una devuelve (capas, cámara)
PORT_X = (0.24 * W, 0.76 * W)
PORT_ALTO = 487.0
PORT_GIRO = 25.0
PORT_XY = (540.0, 910.0)
PORT_W = (600.0, 760.0)


def plano_portada(tl):
    """Tomas 1 y 14: el primer segundo ES la portada. tl: segundos desde el inicio de la toma 1; en la toma 14 es
    negativo (t - DUR) y el plano es exactamente el del fotograma 0. La tarjeta crece de 600 a 760 px en 12
    fotogramas con frenada (ya tiene velocidad en el fotograma 0) y desde T_BAJA empieza a bajar 30 px."""
    p = fx.eo(tl * FPS / F_CRECE) if tl > 0 else 0.0
    ancho = fx.lerp(PORT_W[0], PORT_W[1], p)
    baja = 30.0 * fx.clamp((tl - T_BAJA) / (C(2) - T_BAJA)) ** 2 if tl > T_BAJA else 0.0
    capas = [capa_suelo()]
    capas += pj("tan", PORT_X[0], tl, "parado", "eureka", alto=PORT_ALTO, vista="perfil", mira=1, cabeza_giro=PORT_GIRO,
                viento=0.2 * math.sin(4 * math.pi * tl), sombra=0.25, dens=1.0)
    capas += pj("tin", PORT_X[1], tl, "parado", "sorpresa", alto=PORT_ALTO, vista="perfil", mira=-1, cabeza_giro=PORT_GIRO,
                sombra=0.25, dens=1.0)
    capas.append(capa_tarjeta("1999", PORT_XY[0], PORT_XY[1] + baja, ancho, z=fx.lerp(-100, -290, p), dedos=MOSTAZA,
                              giro=90 * tl, sombra=SOMBRA_FLOTA))
    return capas, Camara()


def toma_1(t, f):
    capas, cam = plano_portada(t - C(1))
    return texto_portada(fx.componer(capas, cam), f - F(C(1)))


def toma_2(t, f):
    """Subjetivo: dos manos de palitos bajan la tarjeta hasta que los dedos dorados entran en la ranura."""
    tl, dur = t - C(2), C(3) - C(2)
    cam = Camara(avance=110 * fx.eio(0.5 * fx.clamp(tl / dur)) * 2, foco=Z_T2, apertura=APERTURA, campo=120.0)
    placa = capa_placa_base()
    # la ranura, donde cae en pantalla ahora; la tarjeta se coloca respecto de ella
    _, ys_ranura = en_pantalla(cam, Z_PLACA, 0, RANURA[1])
    _, ys_medio = en_pantalla(cam, Z_PLACA, 0, (RANURA[1] + RANURA[3]) / 2)
    k = cam.proyeccion(Z_T2)[0]
    u = fx.clamp(tl / (T_ASIENTA - C(2)))
    recorrido = 250.0
    rebote = 0.0
    if tl > T_ASIENTA - C(2):
        v = (tl - (T_ASIENTA - C(2))) / 0.22
        rebote = 8.0 * math.sin(math.pi * min(1.0, v)) * (1 - min(1.0, v))
    ys_borde = ys_ranura + 5 - (recorrido * (1 - u) ** 2 + rebote)          # borde inferior de la placa de la tarjeta
    _, v_borde = en_reposo(cam, Z_T2, 0, ys_borde)
    _, v_recorte = en_reposo(cam, Z_T2, 0, ys_medio)
    y_tope = v_borde - 0.42 * T2_W
    cy = y_tope + 0.47 * T2_W / 2
    tarjeta = capa_tarjeta("1999", W / 2, cy, T2_W, z=Z_T2, dedos=MOSTAZA, giro=90 * t, recorte_y=v_recorte,
                           sombra=dict(dx=10, dy=14, radio=8, opacidad=fx.lerp(0.15, 0.30, u)))
    # manos: una en la escuadra (izquierda) y otra en el borde superior (derecha), en pantalla, pasadas a su capa
    xi, yi = en_pantalla(cam, Z_T2, W / 2 - T2_W / 2 + 6, y_tope + 0.20 * T2_W)
    xd, yd = en_pantalla(cam, Z_T2, W / 2 + T2_W / 2 - 80, y_tope + 2)
    manos = capa_manos(en_reposo(cam, Z_MANOS, xi, yi), en_reposo(cam, Z_MANOS, xd, yd), t)
    return fx.componer([placa, tarjeta, manos], cam)


T34_AVANCE = (0.0, 60.0, 100.0)          # al inicio de la toma 3, en el paso a la 4 y al final de la 4
T34_X = (540.0, 552.0, 560.0)
T34_TAN, T34_TIN = 0.26 * W, 0.74 * W


def camara_34(t):
    if t < C(4):
        u = fx.eio(0.5 * fx.clamp((t - C(3)) / (C(4) - C(3)))) * 2          # arranca suave y llega con velocidad
        av, x = fx.lerp(T34_AVANCE[0], T34_AVANCE[1], u), fx.lerp(T34_X[0], T34_X[1], u)
    else:
        u = 1 - (1 - fx.clamp((t - C(4)) / (C(5) - C(4)))) ** 2             # sigue y frena
        av, x = fx.lerp(T34_AVANCE[1], T34_AVANCE[2], u), fx.lerp(T34_X[1], T34_X[2], u)
    q = fx.eio((t - FOCO[0]) / (FOCO[1] - FOCO[0]))                         # 0 = foco en la tarjeta; 1 = en Tin y Tan
    p = 1000.0 / (1000.0 - av)
    return Camara(x=x, y=SUELO - (SUELO - H / 2) / p, avance=av, foco=fx.lerp(Z_PED, 0.0, q),
                  apertura=fx.lerp(0.030, 0.020, q), campo=fx.lerp(175.0, 100.0, q), niebla=NIEBLA)


def plano_34(t):
    """Tomas 3 y 4, un solo plano: la tarjeta en su pedestal, Tan y Tin a los lados y una PC al fondo."""
    cam = camara_34(t)
    capas = [capa_pc_beige(), capa_suelo_largo()]
    tl = t - C(3)
    if t < C(4):
        tan = dict(pose="pregunta", expresion="nostalgia")
        tin = dict(pose="saluda", expresion="feliz")
    else:
        p = cambio(t, C(4))
        tan = dict(pose=("pregunta", "parado", p), expresion="curiosidad")
        q = cambio(t, MARCAS["back_as_ceo"] - 0.1)                           # a mitad de la toma: Tin levanta el lápiz
        tin = dict(pose=("saluda", "explica", p) if q <= 0 else ("explica", "pregunta", q), expresion="feliz")
        tn = (t - (MARCAS["back_as_ceo"] - 0.1)) / 0.5                       # y Tan asiente
        if 0 < tn < 1:
            tan["cabeza_giro"] = -9 * math.sin(math.pi * tn) ** 2
    capas += pj("tan", T34_TAN, t, viento=vaiven(tl), **tan)
    # Tin va con espejo en este plano: el brazo del lápiz queda del lado de la tarjeta (hacia afuera se salía del cuadro)
    giro = sacudida_objeto(tl) - (38 if tin["pose"] != "saluda" and t >= C(4) else 0) * (cambio(t, C(4)) if t >= C(4) else 0)
    capas += pj("tin", T34_TIN, t, objeto="lapiz", espejo=True, giro_objeto=giro, **tin)
    capas.append(fx.capa_sombra_contacto(PED_X, PED_BASE + 2, 300, z=Z_PED, opacidad=0.30))
    capas.append(capa_pedestal())
    capas.append(capa_tarjeta("1999", PED_X, PED_TOPE + 0.21 * PED_TARJETA_W, PED_TARJETA_W, z=Z_PED, dedos=None,
                              giro=90 * t, dens=1.25, centro_total=False))
    capas.append(capa_cable())
    return capas, cam


def toma_3(t, f):
    return fx.componer(*plano_34(t))


toma_4 = toma_3


def toma_5(t, f):
    """Las dos tarjetas lado a lado; la nueva aparece desde el desenfoque en 8 fotogramas."""
    tl = t - C(5)
    capas = [capa_suelo()]
    capas += pj("tan", X_TAN, t, "pregunta", "curiosidad", viento=vaiven(tl))
    capas += pj("tin", X_TIN, t, "parado", "feliz")
    capas.append(capa_tarjeta("1999", 250, Y_GRAF, 300, z=0.0, dedos=MOSTAZA, giro=90 * t,
                              sombra=dict(dx=12, dy=9, radio=9, opacidad=0.20)))
    p = (f - F(T_REVELA)) / F_REVELA
    if p > 0:
        q = 1 - fx.eo(p)
        capas.append(capa_tarjeta("actual", 690, Y_GRAF, 500, z=-200.0, dedos=MARRON, giro=55 * t,
                                  sombra=dict(dx=14, dy=10, radio=10, opacidad=0.20 * (1 - q)),
                                  desenfoque=42 * q ** 1.4, opacidad=fx.clamp(0.25 + p * 1.5)))
    return fx.componer(capas, Camara(foco=0.0, apertura=APERTURA, campo=CAMPO))


def toma_6(t, f):
    """El chip (die) con sus puntos; un círculo de tinta lo rodea, dibujado a mano."""
    tl = t - C(6)
    capas = [capa_suelo()]
    asiente = -7 * math.sin(math.pi * fx.clamp((tl - 1.0) / 0.5)) ** 2
    capas += pj("tan", X_TAN, t, "parado", "curiosidad", viento=vaiven(tl), cabeza_giro=asiente)
    capas += pj("tin", X_TIN, t, "explica", "feliz")
    capas.append(capa_die(esc=0.85 + 0.15 * fx.muelle(tl + 1 / FPS, fx.POP)))
    img = fx.componer(capas, Camara(foco=-100.0, apertura=APERTURA, campo=CAMPO))
    p = (f - F(T_GARABATO)) / F_GARABATO
    if p > 0:
        fx.garabato(img, fx.trazo_circulo(DIE_XY[0], DIE_XY[1], 246, 236), fx.eio(p), grosor=9, semilla=3)
    return img


def plano_objeto(cual, t, t0, dur, ancho, expresion, entra=False):
    """Tomas 7 y 8: una tarjeta grande que flota sobre el papel, con Tan debajo; la cámara se mete 70 unidades."""
    tl = t - t0
    cam = cam_hacia(70 * (1 - (1 - fx.clamp(tl / dur)) ** 2), (W / 2, Y_GRAF), foco=-150.0, apertura=APERTURA, campo=CAMPO)
    capas = [capa_suelo_largo()]
    capas += pj("tan", W / 2, t, "parado", expresion, viento=vaiven(tl))
    dx = 0.0
    if entra:                                              # entra con el barrido y se asienta con frenada
        dx = 90 * (1 - fx.eo((tl + 0.1) / 0.5))
    capas.append(capa_tarjeta(cual, W / 2 + dx, Y_GRAF, ancho, z=-150.0, dedos=MOSTAZA, giro=(90 if cual == "1999" else 55) * t,
                              sombra=SOMBRA_FLOTA, dens=1.1))
    return fx.componer(capas, cam)


def toma_7(t, f):
    return plano_objeto("1999", t, C(7), C(8) - C(7), 800, "curiosidad")


def toma_8(t, f):
    return plano_objeto("actual", t, C(8), C(9) - C(8), 800, "sorpresa", entra=True)


def ecuacion(t):
    """Las dos tarjetas pequeñas de la ecuación (dedos en marrón: plano de revelación) vuelan a sus filas."""
    capas = []
    for cual, cx, cy, ancho, retraso in (("actual", 230, EQ_Y1, 260, 0.0), ("1999", 280, EQ_Y2, 180, 0.1)):
        tl = t - C(9) - retraso
        if tl <= 0:
            continue
        u = fx.muelle(tl, fx.SLIDE) if t < C(10) else 1.0
        capas.append(capa_tarjeta(cual, cx + 420 * (1 - u), cy, ancho, z=0.0, dedos=MARRON,
                                  giro=(90 if cual == "1999" else 55) * min(t, C(10)), opacidad=fx.clamp(tl * FPS / 3),
                                  sombra=dict(dx=8, dy=6, radio=6, opacidad=0.18)))
    return capas


def toma_9(t, f):
    """«Divide them»: la ecuación entre dos objetos; en la toma 10 el contador llega a 4,000 y Tan celebra."""
    tl = t - C(9)
    capas = [capa_suelo()]
    if f < F_LLEGA:
        quieto = t >= C(10)
        capas += pj("tan", X_TAN, t, "parado", "curiosidad", viento=vaiven(tl) * (0.3 if quieto else 1.0), quieto=quieto)
        capas += pj("tin", X_TIN, t, ("parado", "saluda", cambio(t, C(9) + 0.1)), "feliz", quieto=quieto)
    else:                                                  # la cifra se lee: solo respiran
        p = cambio(t, T_LLEGA)
        capas += pj("tan", X_TAN, t, ("parado", "celebra", p), "sorpresa", viento=0.5 * vaiven(t - T_LLEGA, 0.5), quieto=True)
        capas += pj("tin", X_TIN, t, "saluda", "eureka", quieto=True)
    capas += ecuacion(t)
    return fx.componer(capas, Camara())


toma_10 = toma_9


def toma_11(t, f):
    """El muro de 4.000 minitarjetas se llena de arriba abajo; en la toma 12 se encoge y equivale a una tarjeta."""
    tl = t - C(11)
    capas = [capa_suelo()]
    if t < C(12):
        filas = int(math.ceil(PARED_FILAS * fx.eo((t - PARED[0] + 1 / FPS) / (PARED[1] - PARED[0]))))
        capas += pj("tan", X_TAN, t, "encoge", "sorpresa", viento=vaiven(tl), quieto=True)
        capas += pj("tin", X_TIN, t, "parado", "feliz", quieto=True)
        pared = capa_pared(filas)
        if filas >= PARED_FILAS:
            capas.append(fx.capa_sombra_contacto(W / 2, PARED_XY[1] + PARED_H + 4, PARED_W, opacidad=0.15, alto=16))
        if pared:
            capas.append(pared)
        return fx.componer(capas, Camara())
    u = fx.eio((t - PLIEGUE[0]) / (PLIEGUE[1] - PLIEGUE[0]))
    ancho = fx.lerp(PARED_W, 380.0, u)
    alto = ancho * PARED_H / PARED_W
    x0 = fx.lerp(PARED_XY[0], 100.0, u)
    cy = fx.lerp(PARED_XY[1] + PARED_H / 2, Y_GRAF, u)
    p = cambio(t, C(12))
    capas += pj("tan", X_TAN, t, "encoge", "risa", viento=vaiven(tl), quieto=True)
    capas += pj("tin", X_TIN, t, ("parado", "saluda", p), "eureka", quieto=True)
    capas.append(fx.capa_sombra_contacto(x0 + ancho / 2, cy + alto / 2 + 4, ancho, opacidad=0.15, alto=16))
    capas.append(capa_pared(caja=(x0, cy - alto / 2, ancho)))
    s = fx.muelle(t - C(12) - 0.25, fx.SLIDE)                # la tarjeta nueva entra desde la derecha y se asienta
    if s > 0:
        capas.append(capa_tarjeta("actual", 790 + 520 * (1 - s), Y_GRAF, 380, z=0.0, dedos=MARRON, giro=55 * t,
                                  sombra=dict(dx=10, dy=8, radio=8, opacidad=0.20)))
    return fx.componer(capas, Camara())


toma_12 = toma_11


def toma_13(t, f):
    """Cierre de firma: Tin y Tan saludan a cámara (el mismo gesto en todos los videos)."""
    tl = t - C(13)
    capas = [capa_suelo()]
    capas += pj("tan", X_TAN, t, "saluda", "feliz", viento=vaiven(tl))
    capas += pj("tin", X_TIN, t, "saluda", "feliz")
    return fx.componer(capas, Camara())


@lru_cache(maxsize=2)
def congelada():
    """El fotograma de la toma 13 que se congela (el del corte), con el texto que tuviera."""
    f = F(C(14))
    return capa_texto(toma_13(C(14), f), f)


def toma_14(t, f):
    """Congelado con marco (22 fotogramas) y vuelta al plano exacto del fotograma 0."""
    capas, cam = plano_portada(t - DUR)
    b = texto_portada(fx.componer(capas, cam), f - N)
    p = (f - F(C(14))) / F_CONGELA
    if p >= 1:
        return b
    return fx.congelado_con_marco(congelada(), b, p)


TOMAS = [toma_1, toma_2, toma_3, toma_4, toma_5, toma_6, toma_7, toma_8, toma_9, toma_10, toma_11, toma_12, toma_13, toma_14]


def toma_de(f):
    t = f / FPS
    for i in range(len(CORTES) - 1, -1, -1):
        if t >= CORTES[i] - 1e-9:
            return i + 1
    return 1


def plano(n, f):
    """La toma n en el fotograma f, con su texto."""
    img = TOMAS[n - 1](f / FPS, f)
    return img if n in (1, 14) else capa_texto(img, f)


def fotograma(f):
    """Devuelve el fotograma f (0 a 914; el 915 es el 0) como imagen RGB de 1080x1920."""
    f = f % N
    n = toma_de(f)
    if BARRIDO[0] <= f < BARRIDO[1]:                         # barrido de obturador 7 -> 8 (6 fotogramas)
        img = fx.barrido_obturador(plano(7, f), plano(8, f), (f - BARRIDO[0] + 0.5) / (BARRIDO[1] - BARRIDO[0]), "derecha")
    else:
        img = plano(n, f)
    z = 1 + 0.10 * golpe(f - F_LLEGA, 5, 8)                  # golpe de zoom de +10 % al caer la cifra
    if z > 1.0005:
        img = fx.acercar(img, z, centro_cifra())
    for corte in BORRONES:                                   # borrón: 2 fotogramas antes y 2 después del corte
        fc = F(corte)
        if fc - 2 <= f < fc + 2:
            img = fx.borron(img, BORRON_PX, "h")
    return img


def _bytes(f):
    return fotograma(f).tobytes()


def _mini(f):
    return fotograma(f).resize((W // 4, H // 4), Image.LANCZOS).tobytes()


# ---------------------------------------------------------------- comprobaciones previas
def todos_los_textos():
    return ["".join(s for s, _ in segs) for fila in TEXTOS for _, segs in fila["lineas"]] + ["0123456789,+"]


def cajas_de_texto():
    """Caja (x0, y0, x1, y1) de cada fila de texto en su tamaño de reposo (con el contorno de la palabra clave)."""
    out = {}
    for fila in TEXTOS:
        xs0, ys0, xs1, ys1 = [], [], [], []
        for tam, x, tope, segs in geometria(fila):
            m = fx.TRAZO_EM * tam
            xs0.append(x - m)
            xs1.append(x + fx.ancho_texto(tuple(segs), tam) + m)
            ys0.append(tope - m)
            baja = any(c in "gjpqy," for s, _ in segs for c in s)
            ys1.append(tope + 0.74 * tam + (0.21 * tam if baja else 0) + m)
        out[fila["id"]] = (min(xs0), min(ys0), max(xs1), max(ys1))
    return out


def comprobaciones():
    """Lo que se puede comprobar antes de dibujar: glifos, rejilla, contador, textos dentro de la zona segura."""
    usados = fx.comprobar_glifos(todos_los_textos())
    assert len(VOZ) == 12 and len(CORTES) == 14
    assert all(abs(c * 2 - round(c * 2)) < 1e-9 for c in CORTES + [DUR]), "un corte no cae en la rejilla de 0,5 s"
    assert all(b > a for a, b in zip(CORTES, CORTES[1:] + [DUR])), "cortes desordenados"
    assert all(VOZ[i][3] <= VOZ[i + 1][2] for i in range(len(VOZ) - 1)), "líneas de voz que se pisan"
    v = [valor_contador(f / FPS) for f in range(N)]
    assert all(b >= a for a, b in zip(v, v[1:])) and max(v) == CONTADOR[3] and min(v) == CONTADOR[2], "contador mal"
    assert F(FOCO[1]) - F(FOCO[0]) >= 10, "el cambio de foco no cabe en la pausa entre las líneas 2 y 3"
    notas = []
    for fila in TEXTOS:
        for (pct, segs), (tam, x, tope, _) in zip(fila["lineas"], geometria(fila)):
            if abs(tam - pct / 100 * H) > 0.01:
                notas.append(f"«{''.join(s for s, _ in segs)}»: {pct} % no cabe; queda en {tam / H * 100:.2f} % ({tam:.1f} px)")
    for nombre, (x0, y0, x1, y1) in cajas_de_texto().items():
        assert x0 >= SEG_X0 - 0.5 and x1 <= SEG_X1 + 0.5, f"texto fuera de la zona segura en x: {nombre} ({x0:.0f}-{x1:.0f})"
        assert y0 >= SEG_Y0 - 0.5 and y1 <= SEG_Y1, f"texto fuera de la zona segura en y: {nombre} ({y0:.0f}-{y1:.0f})"
    x0, y0, x1, y1 = cajas_de_texto()["portada"]
    assert y0 >= 400 and y1 * 1.0 <= 700 and x0 >= 60 and x1 <= 960, f"texto de portada fuera de su franja: {(x0, y0, x1, y1)}"
    assert PORTADA_TAM >= 120 and len("Jensen Huang Is Back".split()) <= 4
    return usados, notas


def hoja(ruta, cada=15, cols=8):
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


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--hoja", help="solo una hoja de contacto rápida (JPG)")
    ap.add_argument("--cada", type=int, default=15)
    ap.add_argument("--fotograma", nargs=2, metavar=("N", "PNG"), help="guarda un solo fotograma")
    ap.add_argument("--sin-audio", action="store_true", help="no rehace el audio (usa 05_audio/mezcla.wav)")
    a = ap.parse_args()

    usados, notas = comprobaciones()
    print(f"palitos.py {palitos.VERSION} · efectos.py {fx.VERSION}. Glifos comprobados en Inter Display Medium: {''.join(usados)}")
    print(f"El contador llega a {CONTADOR[3]:,} en el fotograma {F_LLEGA} ({T_LLEGA:.3f} s)")
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
           "-t", f"{DUR}", "-map_metadata", "-1", "-fflags", "+bitexact", "-flags:v", "+bitexact", "-flags:a", "+bitexact",
           "-movflags", "+faststart", str(SALIDA)]
    ff = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    t_dibujo = time.time()
    medidas, por_toma = [], [0.0] * len(TOMAS)
    ultimo = time.time()
    with Pool(4) as pool:
        for i, datos in enumerate(pool.imap(_bytes, range(N), chunksize=2)):
            ff.stdin.write(datos)
            medidas.append(fx.luminosidad(Image.frombytes("RGB", (W, H), datos)))
            ahora = time.time()
            por_toma[toma_de(i) - 1] += ahora - ultimo
            ultimo = ahora
            if i % 150 == 0:
                print(f"  fotograma {i}/{N}  ({ahora - inicio:.0f} s)", flush=True)
    ff.stdin.close()
    if ff.wait() != 0:
        sys.exit("ffmpeg falló")
    total = time.time() - inicio
    # destellos: el límite del estudio es 3 cambios bruscos por segundo; aquí se exige margen (2 como máximo)
    medidas.append(medidas[0])                                # el bucle: después del último fotograma viene el 0
    informe = fx.comprobar_destellos(medidas, FPS, max_por_segundo=2, estricto=False)
    # bucle: el plano de la toma 14 llevado a t = DUR es el mismo dibujo que el fotograma 0
    capas, cam = plano_portada(0.0)
    fin = np.asarray(texto_portada(fx.componer(*plano_portada(DUR - DUR)), 0), dtype=np.int16)
    dif0 = np.abs(fin - np.asarray(fotograma(0), dtype=np.int16))
    difu = np.abs(np.asarray(fotograma(N - 1), dtype=np.int16) - np.asarray(fotograma(0), dtype=np.int16))
    bucle = {"toma_14_en_t_final_contra_fotograma_0_dif_max": int(dif0.max()),
             "ultimo_fotograma_contra_el_0_dif_media": round(float(difu.mean()), 4),
             "ultimo_fotograma_contra_el_0_dif_max": int(difu.max())}
    tiempos = {"total_s": round(total, 1), "dibujo_y_codificacion_s": round(time.time() - t_dibujo, 1), "fotogramas": N,
               "s_por_fotograma_con_4_procesos": round((time.time() - t_dibujo) / N, 3),
               "por_toma_s": {f"toma {i + 1}": round(s, 1) for i, s in enumerate(por_toma)}}
    REVISION.mkdir(parents=True, exist_ok=True)
    (REVISION / "destellos.json").write_text(json.dumps(informe, indent=2, ensure_ascii=False) + "\n")
    (REVISION / "tiempos_de_render.json").write_text(json.dumps(tiempos, indent=2, ensure_ascii=False) + "\n")
    (REVISION / "bucle.json").write_text(json.dumps(bucle, indent=2, ensure_ascii=False) + "\n")
    print(f"Destellos: {informe['cambios_bruscos']} cambios bruscos; máximo {informe['max_cambios_en_1_s']} en 1 s "
          f"(límite del estudio 3; aquí se exige 2); mayor salto {informe['mayor_salto_de_luminosidad']} de 255 "
          f"(límite 40) -> {'PASA' if informe['pasa'] else 'NO PASA'}")
    print(f"Bucle: {bucle}")
    print(f"Video -> {SALIDA}  ({total:.0f} s en total)")
    if not informe["pasa"]:
        sys.exit("comprobar_destellos NO PASA: mira destellos.json")


if __name__ == "__main__":
    main()
