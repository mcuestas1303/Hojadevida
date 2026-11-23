#!/usr/bin/env python3
"""Prueba de efectos y profundidad de Tin & Tan, dibujada 100 % con código (prueba técnica: NO se publica).

Uso (desde la carpeta del proyecto):
    python3 codigo/render.py                         # audio + 660 fotogramas + 06_final/prueba_efectos_v1.mp4
    python3 codigo/render.py --hoja salida.jpg       # hoja de contacto rápida (un fotograma cada 0,5 s), sin video
    python3 codigo/render.py --fotograma 450 f.png   # un solo fotograma
    python3 codigo/render.py --comparacion           # 06_final/prueba_efectos_antes_despues.png
    python3 codigo/render.py --sin-audio             # no rehace el audio (usa 05_audio/mezcla.wav)

1080x1920, 30 fps, 22 s (660 fotogramas). Recorre las técnicas de `herramientas/efectos.py` una por una, cada una
con su rótulo numerado, y cierra con 2,6 s de «todo junto». Los personajes salen de `herramientas/palitos.py` 1.3
(sin tocarlo); los objetos (casete, televisor de tubo, teléfono de disco) son genéricos, sin marcas, y están
dibujados aquí con el trazo del canal. Sin voz ni música: solo golpes hechos con código (los sonidos de
`2026-11-21_tin_y_tan_gta6/codigo/audio.py`). No usa ningún servicio de pago: Pillow, numpy y ffmpeg.
Todo depende del número de fotograma.
"""
import argparse
import importlib.util
import json
import math
import subprocess
import sys
import time
from functools import lru_cache
from multiprocessing import Pool
from pathlib import Path

import numpy as np
from PIL import Image

PROY = Path(__file__).resolve().parent.parent
ESTUDIO = PROY.parent.parent
sys.path.insert(0, str(ESTUDIO / "herramientas"))
import efectos as fx  # noqa: E402
import palitos  # noqa: E402
from efectos import K, T, Camara, Capa, Marco  # noqa: E402
from palitos import PALETA  # noqa: E402

W, H, FPS = 1080, 1920, 30
DUR = 22.0
N = int(round(DUR * FPS))        # 660
SALIDA = PROY / "06_final" / "prueba_efectos_v1.mp4"
COMPARACION = PROY / "06_final" / "prueba_efectos_antes_despues.png"

PAPEL, SOMBRA, TINTA = PALETA["papel"], PALETA["papel_sombra"], PALETA["tinta"]
MARRON, MOSTAZA, BLANCO = PALETA["marron"], PALETA["mostaza"], PALETA["blanco"]

# ---------------------------------------------------------------- la escena (coordenadas de reposo)
SUELO = 1560.0                   # los pies de Tin y Tan (z = 0)
HORIZONTE = 1190.0               # donde la pared toca el suelo, al fondo
X_TAN, X_TIN = 330.0, 720.0
ALTO_PJ = 600.0
Z_PARED, Z_TV, Z_TEL, Z_CASETE, Z_CERCA = 1400.0, 800.0, 450.0, -120.0, -450.0
CASETE_XY, CASETE_W = (540.0, 700.0), 440.0
TV_X, TV_W = 540.0, 360.0
TEL_X, TEL_W = 915.0, 210.0
APERTURA, NIEBLA, CAMPO = 0.018, 0.36, 150.0


def suelo_en(z):
    """Altura (y de reposo) a la que un objeto a profundidad z toca el suelo: cuanto más lejos, más cerca del horizonte."""
    return HORIZONTE + (SUELO - HORIZONTE) * 1000.0 / (1000.0 + z)


def region(x0, y0, x1, y1, dens=1.0):
    """Lienzo transparente para dibujar el trozo (x0, y0)-(x1, y1) de la escena a `dens` px por px de reposo."""
    return fx.LienzoCapa(int(round((x1 - x0) * dens)), int(round((y1 - y0) * dens)))


def capa_de(lz, x0, y0, dens, z, salida=1.0, **kw):
    return Capa(lz.resultado(salida), z=z, x=x0, y=y0, esc=dens * salida, **kw)


# ---------------------------------------------------------------- objetos genéricos (sin marcas), con el trazo del canal
def casete(lz, cx, cy, ancho, giro=0.0, rot=0.0):
    """Casete genérico: cuerpo, etiqueta con franja mostaza (el acento), ventana con dos carretes que giran `giro`
    grados y la base trapezoidal. Mide ancho x 0,64 ancho. El hueco del carrete izquierdo está en
    (cx - 0,17 ancho, cy + 0,01 ancho) y tiene 0,040 ancho de radio."""
    m = Marco(lz, cx, cy, ancho, rot)
    b = 0.014
    m.caja(-0.5, -0.32, 0.5, 0.32, SOMBRA, b, radio=0.045)
    m.caja(-0.43, -0.265, 0.43, 0.13, BLANCO, b * 0.8, radio=0.03)
    m.rect(-0.43 + b * 0.8, -0.265 + b * 0.8, 0.43 - b * 0.8, -0.17, MOSTAZA, radio=0.02)
    m.rect(-0.43 + b * 0.8, -0.2, 0.43 - b * 0.8, -0.17, MOSTAZA)
    m.rect(-0.43, -0.175, 0.43, -0.165, TINTA)
    m.linea([(-0.36, -0.115), (0.36, -0.115)], 0.007, MARRON)
    m.caja(-0.31, -0.08, 0.31, 0.10, PAPEL, b * 0.8, radio=0.04)
    m.disco(-0.17, 0.01, 0.076, MARRON)                       # la cinta: más en el carrete izquierdo
    m.disco(0.17, 0.01, 0.062, MARRON)
    for sx in (-0.17, 0.17):
        m.anillo(sx, 0.01, 0.052, 0.012, PAPEL)
        for i in range(6):
            a = math.radians(giro + 60 * i)
            m.linea([(sx + 0.040 * math.cos(a), 0.01 + 0.040 * math.sin(a)),
                     (sx + 0.027 * math.cos(a), 0.01 + 0.027 * math.sin(a))], 0.009, TINTA)
    m.poli_borde([(-0.30, 0.313), (-0.245, 0.18), (0.245, 0.18), (0.30, 0.313)], SOMBRA, 0.012)
    for x, y, r in ((-0.2, 0.26, 0.014), (0.2, 0.26, 0.014), (-0.07, 0.275, 0.011), (0.07, 0.275, 0.011),
                    (-0.455, -0.275, 0.011), (0.455, -0.275, 0.011), (-0.455, 0.275, 0.011), (0.455, 0.275, 0.011)):
        m.disco(x, y, r, TINTA)


def televisor(lz, cx, base_y, ancho, fase=0.0, mueble=True):
    """Televisor de tubo genérico sobre su mueble: caja marrón, pantalla redondeada, dos perillas, parlante y antena
    de conejo. `fase` mueve las líneas de la pantalla. Con mueble mide 1,6 anchos de alto; (cx, base_y) = suelo."""
    m = Marco(lz, cx, base_y, ancho)
    ty = 0.0
    if mueble:
        for sx in (-1, 1):
            m.linea([(sx * 0.5, -0.06), (sx * 0.54, -0.012)], 0.028, TINTA)
        m.caja(-0.6, -0.44, 0.6, -0.05, SOMBRA, 0.014, radio=0.02)
        m.linea([(0, -0.42), (0, -0.07)], 0.008, TINTA)
        for sx in (-0.05, 0.05):
            m.disco(sx, -0.25, 0.016, TINTA)
        ty = -0.44
    m.linea([(0.0, ty - 0.77), (-0.26, ty - 1.12)], 0.012, TINTA)
    m.linea([(0.05, ty - 0.77), (0.30, ty - 1.16)], 0.012, TINTA)
    m.disco(-0.26, ty - 1.12, 0.022, TINTA)
    m.disco(0.30, ty - 1.16, 0.022, TINTA)
    m.disco(0.025, ty - 0.78, 0.05, TINTA)
    m.caja(-0.5, ty - 0.78, 0.5, ty, MARRON, 0.016, radio=0.07)
    m.caja(-0.43, ty - 0.70, 0.17, ty - 0.09, SOMBRA, 0.016, radio=0.10)
    for i in range(3):                                          # la señal: tres líneas que ondulan
        y = ty - 0.55 + 0.14 * i
        m.linea([(-0.36 + 0.046 * j, y + 0.018 * math.sin(fase + 0.9 * j + 1.3 * i)) for j in range(11)], 0.012, BLANCO)
    m.linea([(-0.37, ty - 0.60), (-0.31, ty - 0.645)], 0.014, BLANCO)
    for ky, ang in ((0.58, -50 + 25 * math.sin(fase * 0.5)), (0.38, 40)):
        m.anillo(0.335, ty - ky, 0.075, 0.014, BLANCO)
        a = math.radians(ang)
        m.linea([(0.335, ty - ky), (0.335 + 0.045 * math.cos(a), ty - ky + 0.045 * math.sin(a))], 0.012, TINTA)
    for i in range(4):
        m.linea([(0.25, ty - 0.24 + i * 0.035), (0.42, ty - 0.24 + i * 0.035)], 0.009, TINTA)


def telefono(lz, cx, base_y, ancho, giro=0.0, mesa=True):
    """Teléfono de disco genérico sobre una mesita: base, disco con diez huecos que gira `giro` grados, horquilla,
    auricular y cable rizado. Con mesa mide 1,43 anchos de alto; (cx, base_y) = suelo."""
    m = Marco(lz, cx, base_y, ancho)
    ty = 0.0
    if mesa:
        ty = -0.75
        for sx in (-1, 1):
            m.linea([(sx * 0.5, ty + 0.06), (sx * 0.56, -0.012)], 0.028, TINTA)
        m.linea([(-0.53, ty + 0.45), (0.53, ty + 0.45)], 0.014, TINTA)
        m.caja(-0.62, ty, 0.62, ty + 0.07, MARRON, 0.014, radio=0.02)
    m.linea([(-0.50 - 0.04 * (i % 2) - 0.006 * i, ty - 0.05 + 0.035 * i) for i in range(9)], 0.012, TINTA)
    for sx in (-1, 1):
        m.caja(sx * 0.23 - 0.07, ty - 0.48, sx * 0.23 + 0.07, ty - 0.37, SOMBRA, 0.012)
    m.poli_borde([(-0.46, ty - 0.008), (-0.33, ty - 0.40), (0.33, ty - 0.40), (0.46, ty - 0.008)], BLANCO, 0.016)
    m.anillo(0, ty - 0.19, 0.17, 0.014, SOMBRA)
    for i in range(10):
        a = math.radians(giro + 60 + 30 * i)
        m.anillo(0.118 * math.cos(a), ty - 0.19 + 0.118 * math.sin(a), 0.028, 0.008, PAPEL)
    m.anillo(0, ty - 0.19, 0.055, 0.011, MOSTAZA)
    m.linea([(0.12, ty - 0.055), (0.185, ty - 0.03)], 0.014, TINTA)
    m.linea([(-0.36, ty - 0.565), (0.36, ty - 0.565)], 0.10, TINTA)
    for sx in (-0.40, 0.40):
        m.disco(sx, ty - 0.53, 0.095, TINTA)


# ---------------------------------------------------------------- capas que no cambian (una vez por proceso)
@lru_cache(maxsize=2)
def capa_pared():
    """La pared del fondo (z = 1400): papel tapiz de rayas, dos cuadros, el zócalo y el suelo."""
    x0, y0, x1, y1, dens = -420, -320, 1500, 2240, 0.5
    lz = region(x0, y0, x1, y1, dens)
    m = Marco(lz, -x0 * dens, -y0 * dens, dens)
    for x in range(x0 + 60, x1, 150):
        m.linea([(x, y0 + 20), (x, HORIZONTE)], 9, SOMBRA)
    for cx, cy, w, h in ((205, 700, 190, 240), (880, 760, 170, 200)):
        m.caja(cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2, BLANCO, 9)
        m.disco(cx, cy + 10, w * 0.22, SOMBRA)
        m.linea([(cx, cy - h / 2), (cx, cy - h / 2 - 60)], 4, TINTA)
    m.poli([(x0, HORIZONTE), (x1, HORIZONTE), (x1, y1), (x0, y1)], SOMBRA)
    m.linea([(x0, HORIZONTE), (x1, HORIZONTE)], 9, TINTA)
    m.linea([(x0, HORIZONTE + 34), (x1, HORIZONTE + 34)], 4, MARRON)
    return capa_de(lz, x0, y0, dens, Z_PARED, salida=1.5, nombre="pared")


@lru_cache(maxsize=2)
def capa_alfombra():
    x0, y0, x1, y1 = 40, 1460, 1040, 1700
    lz = region(x0, y0, x1, y1)
    m = Marco(lz, -x0, -y0)
    for rx, ry, col in ((450, 84, MARRON), (444, 79, BLANCO), (410, 66, MARRON), (406, 63, BLANCO)):
        lz.d.ellipse([m.p(530 - rx, 1582 - ry), m.p(530 + rx, 1582 + ry)], fill=col)
    return capa_de(lz, x0, y0, 1.0, 0.0, nombre="alfombra")


@lru_cache(maxsize=2)
def capa_cerca():
    """Primer plano (z = -450): el lápiz amarillo del canal y la esquina de otro casete, pegados a la cámara."""
    x0, y0, x1, y1 = -340, 1520, 1420, 2260
    lz = region(x0, y0, x1, y1)
    casete(lz, 1010 - x0, 1850 - y0, 640, giro=20, rot=-13)
    pl = palitos.Pluma(lz, 150 - x0, 1760 - y0, 560)
    palitos.lapiz(pl, 0, 0, angulo=-24, largo=0.95)
    return capa_de(lz, x0, y0, 1.0, Z_CERCA, nombre="primer plano")


@lru_cache(maxsize=4)
def capa_tv(fase10):
    base = suelo_en(Z_TV)
    x0, y0, x1, y1 = TV_X - 260, base - 640, TV_X + 260, base + 40
    lz = region(x0, y0, x1, y1)
    televisor(lz, TV_X - x0, base - y0, TV_W, fase=fase10 / 10)
    return capa_de(lz, x0, y0, 1.0, Z_TV, salida=1.5, nombre="televisor",
                   sombra=dict(dx=16, dy=8, radio=14, opacidad=0.16))


@lru_cache(maxsize=2)
def capa_telefono():
    base = suelo_en(Z_TEL)
    x0, y0, x1, y1 = TEL_X - 170, base - 360, TEL_X + 170, base + 30
    lz = region(x0, y0, x1, y1)
    telefono(lz, TEL_X - x0, base - y0, TEL_W)
    return capa_de(lz, x0, y0, 1.0, Z_TEL, salida=1.5, nombre="teléfono",
                   sombra=dict(dx=14, dy=8, radio=12, opacidad=0.16))


@lru_cache(maxsize=2)
def capa_linea_de_suelo():
    lz = region(0, SUELO - 10, W, SUELO + 10)
    lz.d.line([(100 * 3, 10 * 3), (980 * 3, 10 * 3)], fill=SOMBRA, width=4 * 3)
    return capa_de(lz, 0, SUELO - 10, 1.0, 0.0, nombre="línea de suelo")


@lru_cache(maxsize=2)
def capa_mesa():
    """Tablero de los planos de detalle: una franja de suelo con su borde, detrás del objeto."""
    x0, y0, x1, y1, dens = -420, 1180, 1500, 2300, 0.5
    lz = region(x0, y0, x1, y1, dens)
    m = Marco(lz, -x0 * dens, -y0 * dens, dens)
    m.poli([(x0, 1260), (x1, 1260), (x1, y1), (x0, y1)], SOMBRA)
    m.linea([(x0, 1260), (x1, 1260)], 8, TINTA)
    return capa_de(lz, x0, y0, dens, 500.0, salida=1.5, nombre="tablero")


# ---------------------------------------------------------------- capas que se mueven
def bote(t, fase=0.0, amp=0.022):
    """Rebote de los personajes al pulso de 0,5 s (del short 2): ningún plano queda congelado."""
    tau = (t / 0.5 + fase) % 1.0
    return 1 + amp * math.exp(-4.0 * tau) * math.sin(math.pi * min(1.0, tau * 5)) + 0.006 * math.sin(2 * math.pi * tau)


def capa_personaje(pid, x, t, pose, expresion, luz, sombras, plano):
    """Devuelve las capas de un personaje: sombra de contacto, sombra tumbada en el suelo y el personaje."""
    lz = region(0, 0, 700, 900)
    es_tan = pid == "tan"
    palitos.dibujar(lz, pid, 350, 860, ALTO_PJ * bote(t, 0.0 if es_tan else 0.5), pose=pose, expresion=expresion,
                    viento=0.25 * math.cos(2 * math.pi * 0.9 * t) if es_tan else 0.0, espejo=es_tan,
                    giro_objeto=3 * math.sin(2 * math.pi * 1.0 * t))
    img = lz.resultado(1.5)
    x0, y0 = x - 350, SUELO - 860
    capas = []
    if not plano and sombras > 0:
        capas.append(fx.capa_sombra_contacto(x, SUELO + 4, 250, opacidad=0.30 * sombras))
        capas.append(Capa(fx.sombra_de_suelo(img, 860 * 1.5, aplastado=0.20, sesgo=luz, radio=9, opacidad=0.17 * sombras),
                          z=0.0, x=x0, y=y0, esc=1.5, nombre=f"sombra de {pid}"))
    capas.append(Capa(img, z=0.0, x=x0, y=y0, esc=1.5, nombre=pid))
    return capas


def capa_casete(t, luz, plano):
    cx, cy = CASETE_XY[0], CASETE_XY[1] + 8 * math.sin(2 * math.pi * 0.5 * t)
    x0, y0, x1, y1 = cx - 290, cy - 210, cx + 290, cy + 210
    lz = region(x0, y0, x1, y1)
    casete(lz, cx - x0, cy - y0, CASETE_W, giro=150 * t, rot=-4 + 1.5 * math.sin(2 * math.pi * 0.5 * t + 1))
    return capa_de(lz, x0, y0, 1.0, 0.0 if plano else Z_CASETE, salida=1.5, nombre="casete",
                   sombra=None if plano else dict(dx=34 * luz, dy=30, radio=18, opacidad=0.24))


def capas_heroe(t, plano=False, sombras=1.0, luz=0.55, tan=("pregunta", "curiosidad"), tin=("explica", "feliz")):
    """El plano de los dos, por capas. plano=True lo deja como los shorts 1 y 2: sin fondo, sin primer plano ni
    sombras, con la línea de suelo."""
    capas = []
    if plano:
        capas.append(capa_linea_de_suelo())
    else:
        capas += [capa_pared(), capa_alfombra()]
    tv, tel = capa_tv(int(t * 20) % 63), capa_telefono()
    if not plano and sombras > 0:
        capas.append(fx.capa_sombra_contacto(TV_X, suelo_en(Z_TV), 470, z=Z_TV, opacidad=0.26 * sombras))
        capas.append(fx.capa_sombra_contacto(TEL_X, suelo_en(Z_TEL), 300, z=Z_TEL, opacidad=0.26 * sombras))
    if plano:                                  # mismos objetos, sin su sombra
        tv, tel = Capa(tv.img, tv.z, tv.x, tv.y, tv.esc), Capa(tel.img, tel.z, tel.x, tel.y, tel.esc)
    capas += [tv, tel]
    capas += capa_personaje("tan", X_TAN, t, tan[0], tan[1], luz, sombras, plano)
    capas += capa_personaje("tin", X_TIN, t, tin[0], tin[1], luz, sombras, plano)
    capas.append(capa_casete(t, luz, plano))
    if not plano:
        capas.append(capa_cerca())
    return capas


def fondo_papel(textura=1.0):
    """Papel plano (0), con textura y viñeta (1) o una mezcla (para hacerla aparecer)."""
    if textura <= 0:
        return fx.papel(grano=0, vineta=0)
    if textura >= 1:
        return fx.papel()
    return Image.blend(fx.papel(grano=0, vineta=0), fx.papel(), textura)


def heroe(t, cam=None, plano=False, sombras=1.0, luz=0.55, textura=1.0, **kw):
    if plano:
        return fx.componer(capas_heroe(t, plano=True, **kw), Camara(), fondo=fondo_papel(0))
    return fx.componer(capas_heroe(t, sombras=sombras, luz=luz, **kw), cam or camara_base(), fondo=fondo_papel(textura),
                       sombras=sombras)


def camara_base(**kw):
    base = dict(apertura=APERTURA, niebla=NIEBLA, foco=0.0, campo=CAMPO)
    base.update(kw)
    return Camara(**base)


# ---------------------------------------------------------------- planos de detalle
MACRO_W = 820.0
MACRO_XY = (540.0, 930.0)


def detalle_casete(t, cam=None):
    cam = cam or camara_base()
    x0, y0, x1, y1 = MACRO_XY[0] - 480, MACRO_XY[1] - 330, MACRO_XY[0] + 480, MACRO_XY[1] + 330
    lz = region(x0, y0, x1, y1)
    casete(lz, MACRO_XY[0] - x0, MACRO_XY[1] - y0, MACRO_W, giro=150 * t)
    obj = capa_de(lz, x0, y0, 1.0, 0.0, salida=1.25, nombre="casete grande",
                  sombra=dict(dx=24, dy=34, radio=24, opacidad=0.26))
    capas = [capa_pared(), capa_mesa(), fx.capa_sombra_contacto(MACRO_XY[0], MACRO_XY[1] + 330, 760, z=0.0, opacidad=0.22),
             obj, capa_cerca()]
    return fx.componer(capas, cam)


def hueco_del_casete(cam):
    """Centro y radio en pantalla del hueco del carrete izquierdo del casete grande, visto con `cam`."""
    k, tx, ty = cam.proyeccion(0.0)
    return (k * (MACRO_XY[0] - 0.17 * MACRO_W) + tx, k * (MACRO_XY[1] + 0.01 * MACRO_W) + ty), k * 0.040 * MACRO_W


def detalle_tv(t, cam=None):
    cam = cam or camara_base()
    x0, y0, x1, y1 = 60, 330, 1020, 1560
    lz = region(x0, y0, x1, y1)
    televisor(lz, 540 - x0, 1500 - y0, 700, fase=t * 6)
    obj = capa_de(lz, x0, y0, 1.0, 0.0, salida=1.25, nombre="televisor grande",
                  sombra=dict(dx=26, dy=14, radio=22, opacidad=0.20))
    capas = [capa_pared(), fx.capa_sombra_contacto(540, 1500, 900, z=0.0, opacidad=0.28), obj, capa_cerca()]
    return fx.componer(capas, cam)


def detalle_telefono(t, cam=None):
    cam = cam or camara_base()
    x0, y0, x1, y1 = 60, 520, 1020, 1580
    lz = region(x0, y0, x1, y1)
    giro = 150 * fx.eio((t * 1.2) % 1.0) * (1 - fx.eio((t * 1.2) % 1.0)) * 4      # el disco gira y vuelve
    telefono(lz, 540 - x0, 1520 - y0, 660, giro=giro)
    obj = capa_de(lz, x0, y0, 1.0, 0.0, salida=1.25, nombre="teléfono grande",
                  sombra=dict(dx=26, dy=14, radio=22, opacidad=0.20))
    capas = [capa_pared(), fx.capa_sombra_contacto(540, 1520, 820, z=0.0, opacidad=0.28), obj, capa_cerca()]
    return fx.componer(capas, cam)


@lru_cache(maxsize=1)
def lapiz_que_cruza():
    """El lápiz del canal, enorme y fuera de foco, para esconder un corte al cruzar por delante."""
    lz = fx.LienzoCapa(700, 2200)
    pl = palitos.Pluma(lz, 350, 1100, 1750)
    palitos.lapiz(pl, 0, 0, angulo=-82, largo=1.0)
    return fx.desenfocar(lz.resultado(1.0), 10)


# ---------------------------------------------------------------- bloques: (inicio, rótulo). Cada uno, una técnica.
ROTULOS = [
    (0.0, T("0 · plano, como los videos 1 y 2")),
    (1.2, T("1 · capas con paralaje")),
    (3.0, T("2 · cambio de foco")),
    (4.8, T("3 · sombras y papel con textura")),
    (6.2, T("4 · revelado desde desenfoque")),
    (7.7, T("5 · atravesar la escena")),
    (9.3, T("6 · barrido de obturador")),
    (10.9, T("7 · acercamiento de golpe y sacudida")),
    (12.4, T("8 · destello y negativo")),
    (14.0, T("9 · garabatos de tinta")),
    (15.6, T("10 · texto: vidrio, contador y cascada")),
    (17.4, T("11 · cruce, congelado y salida")),
    (19.4, T("12 · todo junto, como en un video")),
]
INICIOS = [r[0] for r in ROTULOS] + [DUR]
TXT_X, TXT_TOPE, TXT_TAM = 108.0, 372.0, 112.0
TAM_VIDRIO = 84.0


def texto(s):
    """Frase con la palabra clave entre asteriscos -> segmentos (tinta, mostaza con contorno, tinta). Va entera en una
    sola cadena para que `revisar_texto.py` la lea como se ve en pantalla (con su «¿» y su «?»)."""
    antes, clave, despues = s.split("*")
    return (T(antes), K(clave), T(despues))


PREGUNTA = texto("¿te *acuerdas*?")
MINUTOS = texto("¿cuántos *minutos*?")
TITULARES = ((T("casete"),), (T("televisor de tubo"),), (T("teléfono de disco"),))


def bloque_de(t):
    for i in range(len(ROTULOS)):
        if INICIOS[i] <= t < INICIOS[i + 1]:
            return i
    return len(ROTULOS) - 1


def b0(t, f):
    return heroe(t, plano=True)


def b1(t, f):
    """Paralaje: la cámara barre a los lados y empuja; nada más (sin desenfoque ni sombras todavía)."""
    tl = t - 1.2
    cam = Camara(x=540 + 95 * math.sin(2 * math.pi * tl / 1.8), avance=150 * fx.eio(tl / 1.8), niebla=NIEBLA)
    return heroe(t, cam, sombras=0.0, textura=0.0)


def foco_b2(tl):
    """El foco va de los personajes al televisor del fondo, de ahí al lápiz del primer plano, y vuelve."""
    if tl < 0.3:
        return 0.0
    if tl < 0.9:
        return fx.lerp(0.0, Z_TV, fx.eio((tl - 0.3) / 0.35))
    if tl < 1.45:
        return fx.lerp(Z_TV, Z_CERCA, fx.eio((tl - 0.9) / 0.35))
    return fx.lerp(Z_CERCA, 0.0, fx.eio((tl - 1.45) / 0.3))


def b2(t, f):
    tl = t - 3.0
    cam = Camara(avance=60 + 40 * tl, foco=foco_b2(tl), apertura=APERTURA * 1.3, niebla=NIEBLA, campo=CAMPO)
    return heroe(t, cam, sombras=0.0, textura=0.0)


def b3(t, f):
    """Las sombras y el papel aparecen en 0,5 s; después la luz se mueve de un lado al otro."""
    tl = t - 4.8
    s = fx.eio(tl / 0.5)
    luz = 0.55 * math.cos(math.pi * fx.eio((tl - 0.55) / 0.8))
    return heroe(t, camara_base(avance=132), sombras=s, textura=s, luz=luz)


def cam_detalle(t, t0):
    return camara_base(avance=70 * fx.eo((t - t0) / 3.1), apertura=APERTURA * 0.8)


def b4(t, f):
    return fx.revelar_desde_desenfoque(detalle_casete(t, cam_detalle(t, 6.2)), (t - 6.2) / 0.9)


ATRAVESAR = (8.0, 9.0)


def b5(t, f):
    cam_a = cam_detalle(min(t, ATRAVESAR[0]), 6.2)             # la cámara del detalle se queda quieta al entrar
    if t < ATRAVESAR[0]:
        return detalle_casete(t, cam_a)
    b = heroe(t, camara_base(avance=90 * fx.eo((t - ATRAVESAR[0]) / 1.3)), tan=("celebra", "sorpresa"), tin=("saluda", "eureka"))
    if t >= ATRAVESAR[1]:
        return b
    centro, radio = hueco_del_casete(cam_a)
    return fx.atravesar(detalle_casete(t, cam_a), b, (t - ATRAVESAR[0]) / (ATRAVESAR[1] - ATRAVESAR[0]), centro, radio)


BARRIDOS = ((9.6, 9.95, "derecha"), (10.3, 10.65, "arriba"))


def b6(t, f):
    (a0, a1, d1), (c0, c1, d2) = BARRIDOS
    if t < a0:
        return heroe(t, camara_base(avance=90))
    if t < a1:
        return fx.barrido_obturador(heroe(t, camara_base(avance=90)), detalle_tv(t), (t - a0) / (a1 - a0), d1)
    if t < c0:
        return detalle_tv(t)
    if t < c1:
        return fx.barrido_obturador(detalle_tv(t), detalle_telefono(t), (t - c0) / (c1 - c0), d2)
    return detalle_telefono(t)


GOLPES = (11.15, 11.8)
CARA_TIN, CARA_TAN = (X_TIN, 1090.0), (X_TAN, 1090.0)


def b7(t, f):
    """Dos zooms de golpe: a la cara de Tin y, de ahí, a la de Tan. Cada golpe lleva una sacudida de 8 fotogramas."""
    g1, g2 = GOLPES
    cam = camara_base()
    tin, tan = ("explica", "feliz"), ("pregunta", "curiosidad")
    if t >= g1:
        u = fx.muelle(t - g1, fx.SELLO)
        cam.zoom = 1 + 0.75 * u
        cam.x, cam.y = fx.lerp(540, CARA_TIN[0], u), fx.lerp(960, CARA_TIN[1], u)
        cam.temblor = fx.sacudida(f - int(round(g1 * FPS)), 16)
        tin = ("celebra", "sorpresa")
    if t >= g2:
        u = fx.muelle(t - g2, fx.SLIDE)
        cam.zoom = 1.75
        cam.x, cam.y = fx.lerp(CARA_TIN[0], CARA_TAN[0], u), fx.lerp(CARA_TIN[1], CARA_TAN[1], u)
        cam.temblor = fx.sacudida(f - int(round(g2 * FPS)), 12, semilla=2.0)
        tan = ("encoge", "risa")
    return heroe(t, cam, tan=tan, tin=tin)


NEG_1, CORTE_8 = 13.0, 13.6
R_NEG_1, R_NEG_2 = 330.0, 250.0
RAMPA_NEG = (0.45, 1.0, 1.0, 1.0, 0.45)       # el negativo entra y sale en un fotograma a media fuerza: no parpadea


def b8(t, f):
    """Destello de 3 fotogramas en cada corte y negativo de 5 fotogramas, limitado a un círculo sobre el casete."""
    if t < CORTE_8:
        img = detalle_casete(t, camara_base(avance=40 * fx.eo((t - 12.4) / 1.1), apertura=APERTURA * 0.8))
        img = fx.destello(img, f - int(round(12.4 * FPS)), dur=3, opacidad=0.45)
        fl = f - int(round(NEG_1 * FPS))
        if 0 <= fl < len(RAMPA_NEG):
            img = fx.negativo_paleta(img, fx.mascara_circulo(MACRO_XY[0], MACRO_XY[1], R_NEG_1, 30.0), RAMPA_NEG[fl])
        return img
    img = heroe(t, camara_base(avance=60))
    return fx.destello(img, f - int(round(CORTE_8 * FPS)), dur=3, opacidad=0.45)


def subrayado_de(segs, tam, x, tope):
    """Trazo que subraya la palabra clave (el segmento K) de un texto puesto en (x, tope)."""
    antes = fx.ancho_texto(tuple(segs[:1]), tam)
    clave = fx.ancho_texto(tuple(segs[1:2]), tam)
    return fx.trazo_subrayado(x + antes - 6, x + antes + clave + 10, tope + 0.74 * tam + 0.16 * tam)


def b9(t, f):
    """Tres garabatos que se dibujan solos: un círculo alrededor del casete, una flecha al televisor y el subrayado."""
    tl = t - 14.0
    img = heroe(t, camara_base(avance=60))
    fx.poner_texto(img, PREGUNTA, TXT_X, TXT_TOPE, TXT_TAM)
    fx.garabato(img, fx.trazo_circulo(CASETE_XY[0], CASETE_XY[1] + 4, 292, 186), fx.eio((tl - 0.1) / 0.45), grosor=9, semilla=3)
    fx.garabato(img, fx.trazo_flecha((930, 700), (928, 1100), curva=-0.16), fx.eio((tl - 0.6) / 0.4), grosor=9, semilla=5)
    fx.garabato(img, subrayado_de(PREGUNTA, TXT_TAM, TXT_X, TXT_TOPE), fx.eio((tl - 1.0) / 0.35), grosor=10, semilla=7)
    return img


C_MIN = (16.0, 16.75, 0, 60)          # contador: de 0 a 60 minutos (un casete genérico de 60)


def b10(t, f):
    """Texto de vidrio con palabra clave, contador que solo sube y tres titulares en cascada."""
    tl = t - 15.6
    img = heroe(t, camara_base(avance=60, foco=Z_CERCA * 0.35, apertura=APERTURA * 0.9))
    if tl >= 0.1:
        fx.texto_vidrio(img, MINUTOS, TXT_X + 20, TXT_TOPE, TAM_VIDRIO, alfa=fx.clamp((tl - 0.1) * FPS / 3 + 0.34))
    if tl >= 0.35:
        n = fx.contador(t, *C_MIN)
        ancho = fx.ancho_texto((K("60"), T(" minutos")), 100)
        fx.texto_vidrio(img, (K(f"{n}"), T(" minutos")), TXT_X + 20, 524, 100, alfa=fx.clamp((tl - 0.35) * FPS / 3 + 0.34), ancho=ancho)
    if tl >= 1.0:
        fx.titulares_en_cascada(img, TITULARES, tl - 1.0, TXT_X + 20, 694, 48, paso=76)
    return img


CRUCE, CONGELA, SALE = (17.7, 18.2), (18.45, 19.2), (19.25, 19.5)


def b11(t, f):
    """El lápiz cruza por delante y esconde el corte; el plano se congela, queda como una foto con marco y cae; el
    plano siguiente entra con una salida del cuadro hacia arriba."""
    if t < CRUCE[0]:
        return heroe(t, camara_base(avance=60))
    if t < CRUCE[1]:
        return fx.cruce_por_delante(heroe(t, camara_base(avance=60)), detalle_tv(t), (t - CRUCE[0]) / (CRUCE[1] - CRUCE[0]),
                                    lapiz_que_cruza())
    if t < CONGELA[0]:
        return detalle_tv(t)
    if t < CONGELA[1]:
        # sin destello: viene 0,25 s después del cruce del lápiz y juntos pasaban de 3 cambios de luz en un segundo
        return fx.congelado_con_marco(detalle_tv(CONGELA[0]), detalle_telefono(t), (t - CONGELA[0]) / (CONGELA[1] - CONGELA[0]))
    if t < SALE[0]:
        return detalle_telefono(t)
    return fx.salida_del_cuadro(detalle_telefono(t), detalle_casete(t, cam_final_1(t)), (t - SALE[0]) / (SALE[1] - SALE[0]), "arriba")


# «todo junto»: gancho de 4 planos en 0,6 s (19,4 a 20,0) y un respiro de 2 s
F_TV, F_TEL, F_HEROE, F_NEG = 19.6, 19.75, 19.9, 21.3


def cam_final_1(t):
    return camara_base(avance=60 + 200 * (t - 19.25), apertura=APERTURA * 0.8)


def b12(t, f):
    if t < SALE[1]:
        return b11(t, f)
    if t < F_TV:
        return detalle_casete(t, cam_final_1(t))
    if t < F_TEL:
        img = detalle_tv(t, camara_base(zoom=fx.golpe_de_zoom(t - F_TV, 0.10)))
        return fx.destello(img, f - int(round(F_TV * FPS)), dur=2, opacidad=0.3)
    if t < F_HEROE:
        return detalle_telefono(t, camara_base(zoom=fx.golpe_de_zoom(t - F_TEL, 0.10), x=540 - 60 * (t - F_TEL) / 0.15))
    tl = t - F_HEROE
    u = fx.muelle(tl, fx.SELLO)
    cam = camara_base(zoom=1.30 - 0.30 * u, avance=75 * fx.eio(tl / 2.1), x=540 - 30 * fx.eio(tl / 2.1), y=960 - 45 * fx.eio(tl / 2.1),
                      foco=fx.lerp(Z_CERCA, 0.0, fx.eio(tl / 0.45)), temblor=fx.sacudida(f - int(round(F_HEROE * FPS)), 14))
    reaccion = tl >= 0.9
    img = heroe(t, cam, tan=("celebra", "risa") if reaccion else ("pregunta", "curiosidad"),
                tin=("saluda", "eureka") if reaccion else ("explica", "feliz"))
    fx.palabra_clave(img, PREGUNTA, TXT_X, TXT_TOPE, TXT_TAM, tl - 0.1)
    fx.garabato(img, subrayado_de(PREGUNTA, TXT_TAM, TXT_X, TXT_TOPE), fx.eio((tl - 0.4) / 0.3), grosor=10, semilla=7)
    fl = f - int(round(F_NEG * FPS))
    if 0 <= fl < len(RAMPA_NEG):                               # la firma: el negativo vuelve una vez, sobre el casete
        k, tx, ty = cam.proyeccion(Z_CASETE)
        img = fx.negativo_paleta(img, fx.mascara_circulo(round(k * CASETE_XY[0] + tx), round(k * CASETE_XY[1] + ty),
                                                         round(R_NEG_2 * k), 30.0), RAMPA_NEG[fl])
    return img


BLOQUES = [b0, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12]


def fotograma(f, con_rotulo=True):
    """Devuelve el fotograma f (0 a 659) como imagen RGB de 1080x1920."""
    t = f / FPS
    i = bloque_de(t)
    img = BLOQUES[i](t, f)
    if con_rotulo:
        fx.rotulo(img, ROTULOS[i][1][0])
    return img


def _bytes(f):
    return fotograma(f).tobytes()


def _mini(f):
    return fotograma(f).resize((W // 4, H // 4), Image.LANCZOS).tobytes()


# ---------------------------------------------------------------- comprobaciones previas
def todos_los_textos():
    textos = [r[1][0] for r in ROTULOS]
    for segs in (PREGUNTA, MINUTOS) + TITULARES:
        textos.append("".join(s for s, _ in segs))
    return textos + ["0123456789 minutos"]


def comprobaciones():
    usados = fx.comprobar_glifos(todos_los_textos())
    for _, (s, _) in ROTULOS:
        fin = fx.SEG_X0 + 8 + fx.ancho_texto((T(s),), 42) + 0.9 * 42
        assert fin <= fx.SEG_X1, f"rótulo fuera de la zona segura: {s} ({fin:.0f} px)"
    for segs, x, tam in ((PREGUNTA, TXT_X, TXT_TAM), (MINUTOS, TXT_X + 20, TAM_VIDRIO)):
        fin = x + fx.ancho_texto(segs, tam) + 0.55 * tam
        assert fin <= fx.SEG_X1, f"texto fuera de la zona segura: {segs} ({fin:.0f} px)"
    v = [fx.contador(f / FPS, *C_MIN) for f in range(N)]
    assert all(b >= a for a, b in zip(v, v[1:])) and max(v) == C_MIN[3], "el contador no sube bien"
    return usados


def hoja(ruta, cada=15, cols=8):
    fs = list(range(0, N, cada))
    with Pool(4) as pool:
        imgs = pool.map(_mini, fs)
    w, h = W // 4, H // 4
    filas = math.ceil(len(fs) / cols)
    lienzo = Image.new("RGB", (cols * w, filas * h), "#888888")
    for i, b in enumerate(imgs):
        lienzo.paste(Image.frombytes("RGB", (w, h), b), ((i % cols) * w, (i // cols) * h))
    lienzo.save(ruta, quality=88)


def comparacion(ruta=COMPARACION):
    """Hoja de antes y después: el mismo plano y el mismo instante, plano (como los shorts 1 y 2) y con profundidad."""
    t = 1.0
    antes = heroe(t, plano=True)
    despues = heroe(t, camara_base(avance=132))
    w, h, m, cab = 520, 924, 14, 76
    lienzo = Image.new("RGB", (2 * w + 3 * m, h + cab + m), BLANCO)
    for i, (img, s) in enumerate(((antes, T("antes: plano, como los videos 1 y 2")), (despues, T("después: con profundidad")))):
        x = m + i * (w + m)
        lienzo.paste(img.resize((w, h), Image.LANCZOS), (x, cab))
        fx.poner_texto(lienzo, (s,), x + 4, 22, 30)
    lienzo.save(ruta, optimize=True)
    return ruta


# ---------------------------------------------------------------- audio: solo golpes hechos con código
def audio():
    """Golpes atados a cada efecto, con los sonidos del short 2 (`audio.py` del proyecto GTA 6). Sin voz ni música.
    Nivel: pico de -6 dBFS (el criterio del short 2 para los golpes que suenan sin voz encima). Nadie lo ha escuchado."""
    ruta = ESTUDIO / "proyectos" / "2026-11-21_tin_y_tan_gta6" / "codigo" / "audio.py"
    spec = importlib.util.spec_from_file_location("audio_short2", ruta)
    au = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(au)
    rng = np.random.default_rng(20261123)
    pista = np.zeros((au.N, 2))
    eventos = [(r[0], "clic", "cambio de bloque") for r in ROTULOS[1:]]
    eventos += [(ATRAVESAR[0], "whoosh_largo", "atravesar"), (BARRIDOS[0][0], "whoosh", "barrido"), (BARRIDOS[1][0], "whoosh", "barrido"),
                (GOLPES[0], "thunk", "zoom de golpe"), (GOLPES[1], "thunk", "zoom de golpe"),
                (12.4, "clic_borron", "destello"), (NEG_1, "pop_grave", "negativo"), (CORTE_8, "clic_borron", "destello"),
                (14.1, "hoja_corta", "garabato"), (14.6, "hoja_corta", "garabato"),
                (15.0, "hoja_corta", "garabato"), (15.7, "pop", "texto de vidrio"), (15.95, "pop", "contador"),
                (16.6, "pop", "cascada"), (16.72, "pop", "cascada"), (16.84, "pop", "cascada"),
                (CRUCE[0], "whoosh", "cruce"), (CONGELA[0], "hoja", "congelado"), (SALE[0], "whoosh", "salida"),
                (F_TV, "clic_borron", "gancho"), (F_TEL, "clic", "gancho"), (F_HEROE, "thunk", "gancho"),
                (F_HEROE + 0.1, "pop", "palabra clave"), (F_NEG, "pop_grave", "firma")]
    for t, nombre, _ in eventos:
        if nombre == "whoosh":
            x = au.s_whoosh(rng, 0.35) * 0.6
        elif nombre == "whoosh_largo":
            x = au.s_whoosh(rng, 0.95) * 0.6
        else:
            x = au.sonido(nombre, rng)
        au.poner(pista, x, t)
    au.poner(pista, au.s_tictac(C_MIN[1] - C_MIN[0], [k / 12 for k in range(12)]), C_MIN[0])
    pista = pista[: int(DUR * au.SR)]
    pista *= 10 ** (-6 / 20) / np.abs(pista).max()
    destino = PROY / "05_audio"
    destino.mkdir(exist_ok=True)
    au.guardar(destino / "mezcla.wav", pista)
    lufs, pico = au.medir(destino / "mezcla.wav")
    print(f"Audio: {len(eventos) + 1} golpes, {lufs:.1f} LUFS integrados, pico real {pico:.1f} dBTP -> 05_audio/mezcla.wav")
    return destino / "mezcla.wav"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--hoja", help="solo una hoja de contacto rápida (JPG)")
    ap.add_argument("--cada", type=int, default=15)
    ap.add_argument("--fotograma", nargs=2, metavar=("N", "PNG"), help="guarda un solo fotograma")
    ap.add_argument("--comparacion", action="store_true", help="solo la hoja de antes y después")
    ap.add_argument("--sin-audio", action="store_true", help="no rehace el audio (usa 05_audio/mezcla.wav)")
    a = ap.parse_args()

    usados = comprobaciones()
    print(f"palitos.py {palitos.VERSION} · efectos.py {fx.VERSION}. Glifos comprobados: {''.join(usados)}")
    if a.fotograma:
        fotograma(int(a.fotograma[0])).save(a.fotograma[1])
        return
    if a.hoja:
        hoja(a.hoja, a.cada)
        return
    if a.comparacion:
        print("Comparación ->", comparacion())
        return

    inicio = time.time()
    mezcla = PROY / "05_audio" / "mezcla.wav"
    if not a.sin_audio:
        audio()
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
    medidas, por_bloque = [], [0.0] * len(BLOQUES)
    ultimo = time.time()
    with Pool(4) as pool:
        for i, datos in enumerate(pool.imap(_bytes, range(N), chunksize=2)):
            ff.stdin.write(datos)
            medidas.append(fx.luminosidad(Image.frombytes("RGB", (W, H), datos)))
            ahora = time.time()
            por_bloque[bloque_de(i / FPS)] += ahora - ultimo
            ultimo = ahora
            if i % 150 == 0:
                print(f"  fotograma {i}/{N}  ({ahora - inicio:.0f} s)", flush=True)
    ff.stdin.close()
    if ff.wait() != 0:
        sys.exit("ffmpeg falló")
    total = time.time() - inicio
    informe = fx.comprobar_destellos(medidas, FPS, estricto=False)
    tiempos = {"total_s": round(total, 1), "dibujo_y_codificacion_s": round(time.time() - t_dibujo, 1),
               "fotogramas": N, "s_por_fotograma_con_4_procesos": round((time.time() - t_dibujo) / N, 3),
               "por_bloque_s": {ROTULOS[i][1][0]: round(s, 1) for i, s in enumerate(por_bloque)}}
    (PROY / "07_revision").mkdir(exist_ok=True)
    (PROY / "07_revision" / "destellos.json").write_text(json.dumps(informe, indent=2, ensure_ascii=False) + "\n")
    (PROY / "07_revision" / "tiempos_de_render.json").write_text(json.dumps(tiempos, indent=2, ensure_ascii=False) + "\n")
    print(f"Destellos: {informe['cambios_bruscos']} cambios bruscos; máximo {informe['max_cambios_en_1_s']} en 1 s "
          f"(límite 3); mayor salto {informe['mayor_salto_de_luminosidad']} de 255 (límite 40) -> "
          f"{'PASA' if informe['pasa'] else 'NO PASA'}")
    print(f"Video -> {SALIDA}  ({total:.0f} s en total)")
    if not informe["pasa"]:
        sys.exit("comprobar_destellos NO PASA: mira 07_revision/destellos.json")


if __name__ == "__main__":
    main()
