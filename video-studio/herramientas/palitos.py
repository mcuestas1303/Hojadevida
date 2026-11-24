#!/usr/bin/env python3
"""Tin & Tan: los personajes de palitos del canal de nostalgia, dibujados con código.

Este archivo ES el diseño: la misma función que pinta las hojas de personaje pinta cada fotograma de los videos.
Así el personaje sale idéntico en todas partes y no gasta créditos.

Uso:
    palitos.py hojas <carpeta>          # vueltas, expresiones, poses y la imagen principal de los dos
    palitos.py muestra <salida.png> --personaje tin --pose senala --expresion sorpresa [--vista frente]

Desde otro script (render de un video):
    from palitos import Lienzo, dibujar
    lz = Lienzo(1920, 1080)                       # supermuestreo incluido (líneas suaves)
    dibujar(lz, "tan", x=600, suelo=900, alto=520, pose="pregunta", expresion="curiosidad")
    lz.guardar("fotograma_0001.png")

Requiere Pillow (y nada más). Probado con Pillow 12.3.0.

Versiones:
    1.0 (2026-11-21)  diseño aprobado.
    1.1 (2026-11-21)  espejo.
    1.2 (2026-11-21)  objetos de mano por video (fichas de Tin y Tan, «Objetos de mano por video»): `objeto` acepta
                      también un nombre ("lapiz", "control", "calendario"). `objeto=True` sigue siendo el objeto icónico
                      del personaje (el lápiz de Tin; Tan no tiene) y `objeto=False` ninguno: lo anterior se dibuja igual.
                      Nuevo `giro_objeto` (grados; 0 por defecto) para el movimiento secundario del objeto. Gráfico
                      `mando()` (mando genérico, sin logotipos ni símbolos; las dos palancas a la misma altura)
                      y `calendario_de_mano()`.
    1.3 (2026-11-23)  inclinación de cabeza: `cabeza_giro` en `dibujar` y `giro` en `cabeza` (grados; 0 por defecto, y con 0
                      todo se dibuja igual que antes). La cabeza gira como un bloque (cara, rodete, gorra, lentes)
                      alrededor de la base del cuello; la bufanda y el cuerpo no. Sirve para mirar arriba o abajo
                      (hasta ±25 grados, variación permitida en las fichas). No cambia ningún rasgo.
"""
import argparse
import math
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

VERSION = "1.4"  # 1.0: diseño aprobado (2026-11-21) · 1.1: espejo · 1.2: objetos de mano · 1.3: inclinación de cabeza · 1.4: pose como dict y pose_entre (firma del lápiz bumerán)
SS = 3  # supermuestreo: se dibuja 3 veces más grande y se reduce (Pillow no suaviza las líneas)

# ---------------------------------------------------------------- paleta del canal (años 70, papel crema)
PALETA = {
    "papel": "#F3E9D2",
    "papel_sombra": "#E6D8B8",
    "tinta": "#2B2420",
    "naranja": "#E07A2E",
    "naranja_claro": "#F2A35E",
    "marron": "#7A4B2A",
    "marron_claro": "#9C6A44",
    "verde_azulado": "#2F7F7A",
    "verde_azulado_osc": "#23615D",
    "mostaza": "#E8B33B",
    "mostaza_osc": "#C9932A",
    "tomate": "#C8553D",
    "rubor": "#E9967A",
    "blanco": "#FFF8EC",
}

# ---------------------------------------------------------------- personajes
# Medidas en radios de cabeza (R). Lo que está aquí no se cambia sin pasar por la bitácora del personaje.
PERSONAJES = {
    "tin": {
        "nombre": "Tin",
        "cabeza": "naranja",
        "accesorios": ["gorra", "lentes"],
        "objeto": "lapiz",          # su objeto icónico: el lápiz amarillo (el de rebobinar casetes)
        "cara": {"ojo_y": 0.1, "ceja_y": -0.24, "boca_y": 0.52},   # la gorra ocupa la frente
    },
    "tan": {
        "nombre": "Tan",
        "cabeza": "verde_azulado",
        "accesorios": ["rodete", "bufanda"],
        "objeto": None,
        "cara": {"ojo_y": 0.02, "ceja_y": -0.3, "boca_y": 0.44, "pestanas": True},
    },
}

# Proporciones comunes (en R)
CUELLO, TORSO, BRAZO, ANTEBRAZO, MUSLO, PIERNA = 0.18, 1.45, 0.78, 0.72, 0.85, 0.80
GROSOR = 0.15      # línea del cuerpo
CONTORNO = 0.075   # contorno de cabeza y accesorios

# ---------------------------------------------------------------- poses
# Ángulos en grados desde la vertical hacia abajo; positivo = hacia afuera del cuerpo.
# (brazo, antebrazo) para cada lado y (muslo, pierna) para cada pierna. El antebrazo es absoluto: 180 = hacia arriba.
POSES = {
    "parado":   {"bi": (18, 8),    "bd": (18, 8),    "pi": (9, 4),    "pd": (9, 4)},
    "saluda":   {"bi": (18, 8),    "bd": (100, 155), "pi": (9, 4),    "pd": (9, 4)},
    "senala":   {"bi": (16, 6),    "bd": (92, 88),   "pi": (10, 4),   "pd": (8, 4)},
    "piensa":   {"bi": (48, -40),  "bd": (75, 205),  "pi": (9, 4),    "pd": (6, 2)},
    "celebra":  {"bi": (120, 145), "bd": (120, 145), "pi": (22, 8),   "pd": (22, 8)},
    "encoge":   {"bi": (62, 125),  "bd": (62, 125),  "pi": (9, 4),    "pd": (9, 4)},
    "explica":  {"bi": (32, 78),   "bd": (40, 105),  "pi": (10, 4),   "pd": (8, 4)},
    "pregunta": {"bi": (18, 8),    "bd": (40, 150),  "pi": (9, 4),    "pd": (12, 6)},
    "camina":   {"bi": (-14, -20), "bd": (24, 34),   "pi": (-18, -6), "pd": (24, 10)},
}

def pose_entre(a, b, p):
    """Pose intermedia (dict) entre dos poses (nombre de `POSES` o dict): interpola cada ángulo, así las manos y los
    pies describen arcos. p de 0 (a) a 1 (b); quien llama pone la curva (nada lineal en lo vivo)."""
    pa = a if isinstance(a, dict) else POSES[a]
    pb = b if isinstance(b, dict) else POSES[b]
    return {k: tuple(pa[k][i] + (pb[k][i] - pa[k][i]) * p for i in (0, 1)) for k in ("bi", "bd", "pi", "pd")}


def mano_de(x, suelo, alto, pose="parado", vista="frente", mira=1, espejo=False):
    """Dónde cae la mano que gesticula (brazo `bd`) y el radio de cabeza R, en px: ((mx, my), R). Las mismas cuentas
    que `dibujar`. Sirve para soltar o atrapar un objeto justo en la mano."""
    ps = pose if isinstance(pose, dict) else POSES[pose]
    R = alto / (2 + CUELLO + TORSO + MUSLO + PIERNA + 0.25)
    hombro = (0, -(MUSLO + PIERNA) - TORSO + 0.22)
    lado = mira if vista == "perfil" else 1
    codo = segmento(hombro, ps["bd"][0], BRAZO, lado)
    mano = segmento(codo, ps["bd"][1], ANTEBRAZO, lado)
    sx = -1 if espejo else 1
    return (x + sx * mano[0] * R, suelo + mano[1] * R), R


# ---------------------------------------------------------------- expresiones
# ojos: punto | grandes | felices (arcos) | arriba | entrecerrados | cerrados_suave
# cejas: (alto_izq, alto_der, inclinacion) ; alto negativo = sube ; inclinacion + = el extremo interior baja (enojo/concentración)
# boca: sonrisa | abierta | o | plana | ladeada | suave | risa | dientes
EXPRESIONES = {
    "feliz":       {"ojos": "punto",          "cejas": (0, 0, 0),        "boca": "sonrisa", "rubor": True},
    "nostalgia":   {"ojos": "cerrados_suave", "cejas": (-0.04, -0.04, -0.25), "boca": "suave", "rubor": True},
    "curiosidad":  {"ojos": "grandes",        "cejas": (-0.16, 0.02, 0),  "boca": "ladeada", "rubor": False},
    "pensando":    {"ojos": "arriba",         "cejas": (-0.08, 0.04, 0.1), "boca": "plana",  "rubor": False},
    "concentrado": {"ojos": "entrecerrados",  "cejas": (0.04, 0.04, 0.35), "boca": "plana",  "rubor": False},
    "sorpresa":    {"ojos": "grandes",        "cejas": (-0.2, -0.2, -0.1), "boca": "o",      "rubor": False},
    "risa":        {"ojos": "felices",        "cejas": (-0.06, -0.06, 0),  "boca": "risa",   "rubor": True},
    "eureka":      {"ojos": "grandes",        "cejas": (-0.14, -0.14, 0),  "boca": "dientes", "rubor": True},
}

VISTAS = ("frente", "perfil", "espalda")


# ---------------------------------------------------------------- lienzo con supermuestreo
class Lienzo:
    def __init__(self, ancho, alto, fondo=PALETA["papel"]):
        self.ancho, self.alto = ancho, alto
        self.img = Image.new("RGB", (ancho * SS, alto * SS), fondo)
        self.d = ImageDraw.Draw(self.img)

    def resultado(self):
        return self.img.resize((self.ancho, self.alto), Image.LANCZOS)

    def guardar(self, ruta):
        self.resultado().save(ruta)


def color(nombre):
    return PALETA.get(nombre, nombre)


def fuente(tam):
    for f in ("InterDisplay-Medium.otf", "/usr/share/fonts/opentype/inter/InterDisplay-Medium.otf",
              "DejaVuSans.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
              "segoeui.ttf", "arial.ttf"):
        try:
            return ImageFont.truetype(f, tam)
        except OSError:
            continue
    return ImageFont.load_default()


# ---------------------------------------------------------------- primitivas (coordenadas ya multiplicadas por SS)
class Pluma:
    def __init__(self, lz, cx, cy, r, espejo=False):
        self.d, self.cx, self.cy, self.r = lz.d, cx * SS, cy * SS, r * SS
        self.espejo = espejo

    def p(self, x, y):
        return (self.cx + (-x if self.espejo else x) * self.r, self.cy + y * self.r)

    def caja(self, x0, y0, x1, y1):
        a, b = self.p(x0, y0), self.p(x1, y1)
        return [min(a[0], b[0]), min(a[1], b[1]), max(a[0], b[0]), max(a[1], b[1])]

    def angulos(self, desde, hasta):
        return (180 - hasta, 180 - desde) if self.espejo else (desde, hasta)

    def linea(self, puntos, ancho=GROSOR, tinta="tinta"):
        pts = [self.p(*q) for q in puntos]
        w = max(1, int(ancho * self.r))
        self.d.line(pts, fill=color(tinta), width=w, joint="curve")
        for q in pts:                       # puntas redondas
            self.d.ellipse([q[0] - w / 2, q[1] - w / 2, q[0] + w / 2, q[1] + w / 2], fill=color(tinta))

    def circulo(self, x, y, radio, relleno=None, contorno="tinta", ancho=CONTORNO):
        self.d.ellipse(self.caja(x - radio, y - radio, x + radio, y + radio), fill=color(relleno) if relleno else None,
                       outline=color(contorno) if contorno else None, width=max(1, int(ancho * self.r)))

    def elipse(self, x, y, rx, ry, relleno=None, contorno="tinta", ancho=CONTORNO):
        self.d.ellipse(self.caja(x - rx, y - ry, x + rx, y + ry), fill=color(relleno) if relleno else None,
                       outline=color(contorno) if contorno else None, width=max(1, int(ancho * self.r)))

    def arco(self, x, y, rx, ry, desde, hasta, ancho=0.07, tinta="tinta"):
        desde, hasta = self.angulos(desde, hasta)
        self.d.arc(self.caja(x - rx, y - ry, x + rx, y + ry), desde, hasta, fill=color(tinta), width=max(1, int(ancho * self.r)))

    def poligono(self, puntos, relleno, contorno="tinta", ancho=CONTORNO):
        self.d.polygon([self.p(*q) for q in puntos], fill=color(relleno),
                       outline=color(contorno) if contorno else None, width=max(1, int(ancho * self.r)))

    def cuerda(self, x, y, radio, desde, hasta, relleno, contorno="tinta", ancho=CONTORNO):
        desde, hasta = self.angulos(desde, hasta)
        self.d.chord(self.caja(x - radio, y - radio, x + radio, y + radio), desde, hasta, fill=color(relleno), outline=color(contorno),
                     width=max(1, int(ancho * self.r)))


def segmento(origen, angulo, largo, lado):
    a = math.radians(angulo)
    return (origen[0] + lado * math.sin(a) * largo, origen[1] + math.cos(a) * largo)


# ---------------------------------------------------------------- partes
def cara(pl, pid, expresion, vista, s):
    e = EXPRESIONES[expresion]
    con_lentes = "lentes" in PERSONAJES[pid]["accesorios"]
    ojos_x = [-0.36, 0.36] if vista == "frente" else [0.42 * s]
    medidas = PERSONAJES[pid]["cara"]
    ojo_y = medidas["ojo_y"]
    mx = 0.0 if vista == "frente" else 0.55 * s

    if e["rubor"]:
        for ox in ([-0.6, 0.6] if vista == "frente" else [0.35 * s]):
            pl.elipse(ox, ojo_y + 0.32, 0.16, 0.09, relleno="rubor", contorno=None)

    for i, ox in enumerate(ojos_x):
        t = e["ojos"]
        if t == "punto":
            pl.circulo(ox, ojo_y, 0.085, relleno="tinta", contorno=None)
        elif t == "grandes":
            pl.circulo(ox, ojo_y, 0.14, relleno="tinta", contorno=None)
            pl.circulo(ox + 0.045, ojo_y - 0.05, 0.045, relleno="blanco", contorno=None)
        elif t == "arriba":
            pl.circulo(ox + 0.04 * (1 if vista == "frente" else s), ojo_y - 0.08, 0.085, relleno="tinta", contorno=None)
        elif t == "entrecerrados":
            pl.circulo(ox, ojo_y + 0.02, 0.075, relleno="tinta", contorno=None)
            pl.linea([(ox - 0.13, ojo_y - 0.05), (ox + 0.13, ojo_y - 0.05)], ancho=0.06)
        elif t == "felices":
            pl.arco(ox, ojo_y + 0.06, 0.13, 0.11, 200, 340, ancho=0.065)
        elif t == "cerrados_suave":
            pl.arco(ox, ojo_y - 0.06, 0.13, 0.09, 20, 160, ancho=0.06)

    if medidas.get("pestanas") and e["ojos"] not in ("felices", "cerrados_suave"):
        for ox in ojos_x:
            hacia = (1 if ox > 0 else -1) if vista == "frente" else s
            r0 = 0.15 if e["ojos"] == "grandes" else 0.1
            pl.linea([(ox + hacia * r0 * 0.85, ojo_y - r0 * 0.45), (ox + hacia * (r0 + 0.08), ojo_y - r0 * 0.45 - 0.05)],
                     ancho=0.04)
    if con_lentes:
        for ox in ojos_x:
            pl.circulo(ox, ojo_y, 0.27, relleno=None, contorno="tinta", ancho=0.06)
            pl.arco(ox, ojo_y, 0.2, 0.2, 215, 245, ancho=0.04, tinta="blanco")    # brillo del vidrio
        if vista == "frente":
            pl.linea([(-0.09, ojo_y - 0.03), (0.09, ojo_y - 0.03)], ancho=0.055)
        else:
            pl.linea([(ojos_x[0] - 0.27 * s, ojo_y - 0.02), (0.05 * -s, ojo_y - 0.06)], ancho=0.05)

    alto_i, alto_d, incl = e["cejas"]
    ceja_y = medidas["ceja_y"]
    for i, ox in enumerate(ojos_x):
        alto = (alto_i, alto_d)[i] if vista == "frente" else alto_i
        interior = 1 if (vista == "frente" and ox < 0) or (vista != "frente" and s < 0) else -1
        # el extremo interior de la ceja es el que mira al centro de la cara
        x0, x1 = ox - 0.14, ox + 0.14
        y_int = ceja_y + alto + incl * 0.18
        y_ext = ceja_y + alto - incl * 0.08
        if interior == 1:
            pl.linea([(x0, y_ext), (x1, y_int)], ancho=0.07)
        else:
            pl.linea([(x0, y_int), (x1, y_ext)], ancho=0.07)

    b, by = e["boca"], medidas["boca_y"]
    if b == "sonrisa":
        pl.arco(mx, by - 0.14, 0.3, 0.18, 25, 155, ancho=0.075)
    elif b == "suave":
        pl.arco(mx, by - 0.1, 0.18, 0.1, 30, 150, ancho=0.065)
    elif b == "plana":
        pl.linea([(mx - 0.16, by), (mx + 0.16, by)], ancho=0.065)
    elif b == "ladeada":
        pl.linea([(mx - 0.17, by + 0.02), (mx + 0.15, by - 0.06)], ancho=0.065)
    elif b == "o":
        pl.elipse(mx, by + 0.02, 0.11, 0.14, relleno="tinta", contorno=None)
    elif b in ("abierta", "risa", "dientes"):
        ancho = 0.34 if b != "abierta" else 0.26
        pl.cuerda(mx, by - 0.12, ancho, 0, 180, relleno="tinta", contorno="tinta", ancho=0.04)
        if b == "risa":
            pl.cuerda(mx, by + 0.12, ancho * 0.45, 200, 340, relleno="tomate", contorno=None)
        if b == "dientes":
            pl.poligono([(mx - ancho * 0.8, by - 0.1), (mx + ancho * 0.8, by - 0.1),
                         (mx + ancho * 0.7, by - 0.02), (mx - ancho * 0.7, by - 0.02)], relleno="blanco", contorno=None)


def gorra(pl, vista, s, delante):
    """La gorra marrón de Tin: copa redonda y visera. delante=False dibuja lo que va detrás de la cabeza."""
    if delante:
        base = -0.5
        pl.cuerda(0, base, 0.98, 180, 360, relleno="marron")
        pl.circulo(0, base - 0.98, 0.09, relleno="marron_claro")           # botón
        if vista == "frente":
            pl.linea([(-0.45, base - 0.12), (-0.36, base - 0.8)], ancho=0.035, tinta="marron_claro")   # costuras
            pl.linea([(0.45, base - 0.12), (0.36, base - 0.8)], ancho=0.035, tinta="marron_claro")
            pl.elipse(0, base + 0.02, 1.05, 0.15, relleno="marron_claro")   # visera vista de frente
        elif vista == "perfil":
            pl.poligono([(0.5 * s, base - 0.04), (1.6 * s, base + 0.06), (1.55 * s, base + 0.2), (0.5 * s, base + 0.14)],
                        relleno="marron_claro")
        else:
            pl.elipse(0, base + 0.03, 0.42, 0.07, relleno="papel_sombra")    # ajuste trasero


def rodete(pl, vista, s):
    if vista == "perfil":
        pl.circulo(-0.55 * s, -0.82, 0.38, relleno="verde_azulado_osc")
        pl.linea([(-0.25 * s, -0.62), (-0.3 * s, -0.88)], ancho=0.07, tinta="mostaza")
    else:
        pl.circulo(0, -1.18, 0.4, relleno="verde_azulado_osc")
        pl.linea([(-0.22, -0.86), (0.22, -0.86)], ancho=0.08, tinta="mostaza")   # cinta amarilla


def bufanda(pl, vista, s, cuello_y, viento=0.0):
    """La bufanda mostaza de Tan; viento (-1 a 1) mueve las puntas (sirve para animarla con muelle)."""
    y = cuello_y
    if vista == "perfil":
        b = -0.28 * s
        v = viento
        pl.poligono([(b, y + 0.1), (b - 0.12 * s, y + 0.12), (b - (0.62 + 0.45 * v) * s, y + 0.95 - 0.35 * v),
                     (b - (0.38 + 0.45 * v) * s, y + 1.0 - 0.35 * v)], relleno="mostaza_osc")
        pl.poligono([(b + 0.05 * s, y + 0.12), (b - 0.1 * s, y + 0.14), (b - (0.38 + 0.3 * v) * s, y + 0.78 - 0.25 * v),
                     (b - (0.14 + 0.3 * v) * s, y + 0.8 - 0.25 * v)], relleno="mostaza")
        pl.elipse(0.02 * s, y + 0.12, 0.4, 0.17, relleno="mostaza")
        pl.arco(0.02 * s, y + 0.1, 0.28, 0.08, 20, 160, ancho=0.035, tinta="mostaza_osc")
        return
    if vista == "frente":
        dx = -0.3 * viento
        # dos puntas que cuelgan del lado izquierdo, afinándose; se dibujan antes del rollo del cuello
        pl.poligono([(-0.5, y + 0.15), (-0.14, y + 0.2), (-0.24 + dx, y + 1.02), (-0.56 + dx, y + 0.98)],
                    relleno="mostaza_osc")
        pl.poligono([(-0.3, y + 0.18), (0.04, y + 0.2), (-0.02 + dx * 0.6, y + 0.78), (-0.32 + dx * 0.6, y + 0.74)],
                    relleno="mostaza")
        pl.linea([(-0.29 + dx * 0.55, y + 0.64), (-0.04 + dx * 0.55, y + 0.67)], ancho=0.035, tinta="mostaza_osc")
        pl.elipse(0, y + 0.12, 0.5, 0.17, relleno="mostaza")   # rollo alrededor del cuello
        pl.arco(0, y + 0.1, 0.36, 0.08, 20, 160, ancho=0.035, tinta="mostaza_osc")
    else:
        pl.elipse(0, y + 0.12, 0.5, 0.17, relleno="mostaza")
        pl.circulo(0, y + 0.2, 0.13, relleno="mostaza_osc")   # nudo visto de espaldas


def lapiz(pl, x, y, angulo=-35, largo=0.95):
    a = math.radians(angulo)
    dx, dy = math.cos(a) * largo, math.sin(a) * largo
    nx, ny = -math.sin(a) * 0.08, math.cos(a) * 0.08
    p0, p1 = (x - dx * 0.5, y - dy * 0.5), (x + dx * 0.5, y + dy * 0.5)
    pl.poligono([(p0[0] + nx, p0[1] + ny), (p1[0] + nx, p1[1] + ny), (p1[0] - nx, p1[1] - ny),
                 (p0[0] - nx, p0[1] - ny)], relleno="mostaza", ancho=0.04)
    punta = (p1[0] + dx * 0.22, p1[1] + dy * 0.22)
    pl.poligono([(p1[0] + nx, p1[1] + ny), punta, (p1[0] - nx, p1[1] - ny)], relleno="naranja_claro", ancho=0.04)
    goma = (p0[0] - dx * 0.12, p0[1] - dy * 0.12)
    pl.poligono([(p0[0] + nx, p0[1] + ny), (goma[0] + nx, goma[1] + ny), (goma[0] - nx, goma[1] - ny),
                 (p0[0] - nx, p0[1] - ny)], relleno="tomate", ancho=0.04)


# ---------------------------------------------------------------- objetos de mano por video (versión 1.2)
OBJETOS = ("lapiz", "control", "calendario")


class _Marco:
    """Sistema local para los objetos: origen en (cx, cy) px del cuadro, escala en px, rotación en grados (sentido
    horario en pantalla) y espejo horizontal opcional."""

    def __init__(self, lz, cx, cy, esc=1.0, rot=0.0, espejo=False):
        self.d, self.cx, self.cy, self.esc = lz.d, cx, cy, esc
        a = math.radians(rot)
        self.ca, self.sa, self.sx = math.cos(a), math.sin(a), (-1 if espejo else 1)

    def p(self, x, y):
        x *= self.sx
        return ((self.cx + self.esc * (x * self.ca - y * self.sa)) * SS, (self.cy + self.esc * (x * self.sa + y * self.ca)) * SS)

    def poli(self, pts, relleno):
        self.d.polygon([self.p(*q) for q in pts], fill=color(relleno))

    def disco(self, x, y, r, relleno):
        X, Y = self.p(x, y)
        R = r * self.esc * SS
        self.d.ellipse([X - R, Y - R, X + R, Y + R], fill=color(relleno))

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


def mando(lz, cx, cy, ancho, angulo=0.0, boton_pulsado=False, relleno="mostaza", tinta="tinta", contorno=0.012,
          detalles=True, espejo=False):
    """Mando de videojuego GENÉRICO (sin logotipos, sin símbolos en los botones, sin la forma de ningún mando comercial).

    (cx, cy): centro del contorno exterior, en px; ancho: W en px; el contorno mide W x 0,55 W. Cuerpo de W x 0,40 W
    (radio 0,16 W) y dos empuñaduras redondas de radio 0,16 W; dos palancas y cuatro botones de punto en rombo.
    angulo: grados, sentido horario. boton_pulsado: el botón de abajo del rombo pasa de tinta a papel (nunca a tomate).
    contorno: grosor del contorno en W. detalles=False dibuja solo la silueta (para una estela plana: pasar el mismo
    color en relleno y tinta)."""
    m = _Marco(lz, cx, cy, ancho, angulo, espejo)
    dy = -0.075                                    # el cuerpo queda 0,075 W por encima del centro del contorno
    c = contorno

    def silueta(crece, col):
        m.rect(-0.5 + crece, dy - 0.20 + crece, 0.5 - crece, dy + 0.20 - crece, col, 0.16 - crece)
        for sx in (-0.34, 0.34):
            m.disco(sx, dy + 0.19, 0.16 - crece, col)

    silueta(0.0, tinta)
    silueta(c, relleno)
    if not detalles:
        return
    # palancas: las dos a la misma altura y dentro del cuerpo (antes la derecha, en +0,14 W, cortaba el contorno de
    # abajo; a la misma altura se parece menos todavía a un mando comercial)
    for x, y in ((-0.26, 0.04), (0.03, 0.04)):
        m.disco(x, dy + y, 0.07, tinta)
        m.disco(x, dy + y, 0.035, "papel_sombra")
    for i, (x, y) in enumerate(((0.26, -0.11), (0.20, -0.05), (0.32, -0.05), (0.26, 0.01))):   # rombo; el último es el de abajo
        if i == 3 and boton_pulsado:
            m.disco(x, dy + y, 0.028 + c * 0.5, tinta)
            m.disco(x, dy + y, 0.028 - c * 0.5, "papel")
        else:
            m.disco(x, dy + y, 0.028, tinta)


def calendario_de_mano(lz, cx, cy, ancho, alto, angulo=0.0, numero="17", cabecera="marron"):
    """Hoja de calendario pequeña (la que Tin lleva en la mano): cuerpo blanco, cabecera de 0,22 del alto, dos anillas
    y un número en tinta. (cx, cy): centro de la hoja en px; angulo en grados, sentido horario. El número no se refleja."""
    m = _Marco(lz, cx, cy, 1.0, angulo)
    w, h = ancho / 2, alto / 2
    b = max(2.0, 0.05 * ancho)                     # contorno
    m.rect(-w, -h, w, h, "tinta", 0.06 * ancho)
    m.rect(-w + b, -h + b, w - b, h - b, "blanco", 0.03 * ancho)
    y_cab = -h + 0.22 * alto
    m.rect(-w + b, -h + b, w - b, y_cab, cabecera, 0.03 * ancho)
    m.rect(-w + b, y_cab - b * 0.5, w - b, y_cab + b * 0.5, "tinta")
    for sx in (-0.25, 0.25):                       # anillas sobre el borde de arriba
        m.disco(sx * ancho, -h + b * 0.5, 0.075 * ancho, "tinta")
        m.disco(sx * ancho, -h + b * 0.5, 0.075 * ancho - b * 0.6, "papel")
    if numero:
        tam = int(round(0.52 * alto * SS))
        f = fuente(tam)
        caja = f.getbbox(numero, anchor="mm")
        lado = int(max(caja[2] - caja[0], caja[3] - caja[1]) * 1.5) + 8
        capa = Image.new("RGBA", (lado, lado), (0, 0, 0, 0))
        ImageDraw.Draw(capa).text((lado / 2, lado / 2), numero, font=f, fill=color("tinta"), anchor="mm")
        capa = capa.rotate(-angulo, resample=Image.BICUBIC)
        X, Y = m.p(0, (y_cab + h) / 2 - 0.01 * alto)
        lz.img.paste(capa, (int(round(X - lado / 2)), int(round(Y - lado / 2))), capa)


def objeto_de_mano(lz, pl, nombre, mano, pose, giro=0.0):
    """Dibuja el objeto `nombre` en la mano que gesticula. mano: (x, y) en R, sin reflejar. giro: grados extra."""
    if isinstance(pose, dict):                                  # pose libre (1.4): lo dice la pose; si no, por el antebrazo
        arriba = bool(pose.get("objeto_arriba", pose["bd"][1] >= 120))
    else:
        arriba = pose in ("saluda", "celebra", "pregunta")      # la misma regla de ángulo que el lápiz
    if nombre == "lapiz":
        lapiz(pl, mano[0] + 0.05, mano[1] - 0.25, angulo=(-60 if arriba else -35) + giro)
        return
    R = pl.r / SS
    sx = -1 if pl.espejo else 1
    if nombre == "control":
        # 1,1 R de ancho (x 0,6 R de alto), agarrado por la empuñadura de adentro
        ox, oy, base = (0.42, -0.30, -10) if arriba else (0.42, -0.22, 6)
        ang = (base + giro) * sx
        mando(lz, pl.cx / SS + sx * (mano[0] + ox) * R, pl.cy / SS + (mano[1] + oy) * R, 1.1 * R, angulo=ang,
              contorno=0.04, espejo=pl.espejo)
    elif nombre == "calendario":
        # 0,9 R x 1,0 R, agarrado por el borde de abajo (sin tapar la cabeza ni salir de la zona segura con x = 70 %)
        ox, oy, base = (0.38, -0.62, 6) if arriba else (0.15, -0.58, -6)
        ang = (base + giro) * sx
        calendario_de_mano(lz, pl.cx / SS + sx * (mano[0] + ox) * R, pl.cy / SS + (mano[1] + oy) * R, 0.9 * R, 1.0 * R,
                           angulo=ang)
    else:
        sys.exit(f"Objeto de mano desconocido: {nombre}. Hay: {', '.join(OBJETOS)}")


# ---------------------------------------------------------------- cabeza (sirve sola para primeros planos)
class _Capa:
    """Lienzo transparente del mismo trato que Lienzo (tiene .d), para dibujar una pieza aparte y girarla."""

    def __init__(self, lado_ss):
        self.img = Image.new("RGBA", (lado_ss, lado_ss), (0, 0, 0, 0))
        self.d = ImageDraw.Draw(self.img)


def cabeza(lz, pid, cx, cy, radio, expresion="feliz", vista="frente", mira=1, espejo=False, giro=0.0):
    """Dibuja solo la cabeza con sus accesorios, centrada en (cx, cy) y con ese radio en píxeles.

    giro (grados, 0 por defecto): inclina la cabeza entera (cara, rodete, gorra y lentes, como un bloque) alrededor de
    la base del cuello, el punto (cx, cy + radio). Positivo = levanta la cara hacia donde mira (en perfil, hacia `mira`;
    de frente, hacia la derecha del cuadro, o la izquierda con espejo). Con 0 se dibuja exactamente como antes."""
    if giro:
        medio = int(math.ceil(3.2 * radio))                     # la capa cubre la cabeza girada con sus accesorios
        capa = _Capa(2 * medio * SS)
        cabeza(capa, pid, medio, medio, radio, expresion, vista, mira, espejo, 0.0)
        sentido = (mira if vista == "perfil" else 1) * (-1 if espejo else 1)
        girada = capa.img.rotate(giro * sentido, resample=Image.BICUBIC, center=(medio * SS, (medio + radio) * SS))
        lz.img.paste(girada, (int(round((cx - medio) * SS)), int(round((cy - medio) * SS))), girada)
        return
    pj = PERSONAJES[pid]
    pc = Pluma(lz, cx, cy, radio, espejo)
    if "rodete" in pj["accesorios"]:
        rodete(pc, vista, mira)
    pc.circulo(0, 0, 1.0, relleno=pj["cabeza"])
    if vista != "espalda":
        cara(pc, pid, expresion, vista, mira)
    if "gorra" in pj["accesorios"]:
        gorra(pc, vista, mira, delante=True)


# ---------------------------------------------------------------- personaje completo
def dibujar(lz, pid, x, suelo, alto, pose="parado", expresion="feliz", vista="frente", mira=1, viento=0.0,
            objeto=True, espejo=False, giro_objeto=0.0, cabeza_giro=0.0):
    """Dibuja a Tin o Tan con los pies en (x, suelo) y una altura total de `alto` píxeles.

    mira: 1 mira a la derecha, -1 a la izquierda (solo en perfil). viento: puntas de la bufanda (-1 a 1).
    espejo: dibuja la figura entera reflejada. Por defecto el brazo que hace el gesto queda a la DERECHA del cuadro;
    con espejo=True queda a la IZQUIERDA. Regla de los planos de dos: cada uno gesticula del lado contrario al otro
    (Tan, a la izquierda del cuadro, va con espejo=True; Tin, a la derecha, sin espejo).
    objeto: True = el objeto icónico del personaje (el lápiz de Tin; Tan no tiene); False o None = ninguno; o el
    nombre de un objeto de mano ("lapiz", "control", "calendario"), que vale para los dos personajes.
    giro_objeto: grados que se suman al ángulo del objeto (movimiento secundario).
    pose: nombre de `POSES` o, desde la 1.4, un dict {"bi": (a1, a2), "bd": (a1, a2), "pi": ..., "pd": ...} con los
    ángulos de una pose intermedia (ver `pose_entre`); la clave opcional "objeto_arriba" dice si el objeto de la mano va
    en el ángulo de brazo levantado. Con un nombre se dibuja exactamente como siempre.
    cabeza_giro: inclinación de la cabeza en grados (hasta ±25: variación permitida en las fichas); positivo = levanta
    la cara para mirar hacia arriba. La bufanda y el cuerpo no giran. Con 0, todo igual que siempre.
    """
    if pid not in PERSONAJES:
        sys.exit(f"Personaje desconocido: {pid}. Hay: {', '.join(PERSONAJES)}")
    pj, ps = PERSONAJES[pid], (pose if isinstance(pose, dict) else POSES[pose])
    R = alto / (2 + CUELLO + TORSO + MUSLO + PIERNA + 0.25)     # la gorra y el rodete suman ~0.25 R
    s = mira
    cabeza_y = -(MUSLO + PIERNA + TORSO + CUELLO + 1.0)
    pl = Pluma(lz, x, suelo, R, espejo)

    cadera = (0, -(MUSLO + PIERNA))
    cuello_base = (0, cadera[1] - TORSO)
    hombro = (0, cuello_base[1] + 0.22)

    def lado(k):
        return k if vista != "perfil" else s

    # piernas y zapatos
    for clave, k in (("pi", -1), ("pd", 1)):
        a1, a2 = ps[clave]
        if vista == "perfil":
            a1, a2 = (a1 * (1 if k > 0 else -0.6)), (a2 * (1 if k > 0 else -0.6))
        rodilla = segmento(cadera, a1, MUSLO, lado(k))
        pie = segmento(rodilla, a2, PIERNA, lado(k))
        pl.linea([cadera, rodilla, pie])
        punta = (s if vista == "perfil" else k) * 0.2
        pl.elipse(pie[0] + punta, pie[1] - 0.02, 0.22, 0.1, relleno="tinta", contorno=None)

    # torso
    pl.linea([cadera, cuello_base, (0, cabeza_y + 1.0)])

    # brazos
    manos = []
    for clave, k in (("bi", -1), ("bd", 1)):
        a1, a2 = ps[clave]
        if vista == "perfil":
            a1, a2 = (a1 * (1 if k > 0 else -0.7)), (a2 * (1 if k > 0 else -0.7))
        codo = segmento(hombro, a1, BRAZO, lado(k))
        mano = segmento(codo, a2, ANTEBRAZO, lado(k))
        pl.linea([hombro, codo, mano])
        pl.circulo(mano[0], mano[1], 0.12, relleno="tinta", contorno=None)
        manos.append(mano)

    if "bufanda" in pj["accesorios"]:
        bufanda(pl, vista, s, cuello_base[1] - 0.05, viento)
    cabeza(lz, pid, x, suelo + cabeza_y * R, R, expresion, vista, s, espejo, cabeza_giro)

    # objeto icónico en la mano derecha (vista de frente) o en la de adelante (perfil)
    nombre = pj["objeto"] if objeto is True else (objeto if isinstance(objeto, str) else None)
    if nombre and vista != "espalda":
        objeto_de_mano(lz, pl, nombre, manos[1], pose, giro_objeto)
    return R


# ---------------------------------------------------------------- hojas de personaje
def titulo(lz, texto, x, y, tam=54, tinta="tinta"):
    lz.d.text((x * SS, y * SS), texto, font=fuente(tam * SS), fill=color(tinta))


def etiqueta(lz, texto, x, y, tam=26):
    f = fuente(tam * SS)
    w = lz.d.textlength(texto, font=f)
    lz.d.text((x * SS - w / 2, y * SS), texto, font=f, fill=color("marron"))


def suelo_linea(lz, y, x0, x1):
    lz.d.line([(x0 * SS, y * SS), (x1 * SS, y * SS)], fill=color("papel_sombra"), width=4 * SS)


def hoja_vueltas(pid, ruta):
    lz = Lienzo(1920, 1080)
    titulo(lz, f"{PERSONAJES[pid]['nombre']} · vueltas", 90, 60)
    suelo_linea(lz, 900, 120, 1800)
    for i, (vista, mira) in enumerate((("frente", 1), ("perfil", 1), ("perfil", -1), ("espalda", 1))):
        x = 330 + i * 420
        dibujar(lz, pid, x, 900, 640, vista=vista, mira=mira)
        etiqueta(lz, {0: "frente", 1: "perfil derecho", 2: "perfil izquierdo", 3: "espalda"}[i], x, 935)
    lz.guardar(ruta)


def hoja_expresiones(pid, ruta):
    lz = Lienzo(1920, 1080)
    titulo(lz, f"{PERSONAJES[pid]['nombre']} · expresiones", 90, 60)
    for i, exp in enumerate(EXPRESIONES):
        col, fila = i % 4, i // 4
        x, y = 300 + col * 440, 370 + fila * 420
        cabeza(lz, pid, x, y, 130, expresion=exp)
        etiqueta(lz, exp, x, y + 150)
    lz.guardar(ruta)


def hoja_poses(pid, ruta):
    lz = Lienzo(1920, 1080)
    titulo(lz, f"{PERSONAJES[pid]['nombre']} · poses", 90, 60)
    poses = ["parado", "saluda", "senala", "piensa", "pregunta", "explica", "encoge", "celebra", "camina"]
    expr = {"saluda": "feliz", "senala": "concentrado", "piensa": "pensando", "pregunta": "curiosidad",
            "explica": "feliz", "encoge": "pensando", "celebra": "eureka", "camina": "feliz", "parado": "feliz"}
    for i, pose in enumerate(poses):
        col, fila = i % 5, i // 5
        x, y = 210 + col * 375, 560 + fila * 440
        dibujar(lz, pid, x, y, 360, pose=pose, expresion=expr[pose], vista="perfil" if pose == "camina" else "frente")
        etiqueta(lz, pose.replace("senala", "señala"), x, y + 18)
    lz.guardar(ruta)


def hoja_principal(ruta):
    lz = Lienzo(1920, 1080)
    suelo_linea(lz, 930, 300, 1620)
    dibujar(lz, "tan", 720, 930, 720, pose="pregunta", expresion="curiosidad", viento=0.4, espejo=True)
    dibujar(lz, "tin", 1200, 930, 720, pose="explica", expresion="feliz")
    titulo(lz, "Tin & Tan", 90, 60, tam=72)
    lz.d.text((92 * SS, 150 * SS), "she remembers. he does the math.", font=fuente(34 * SS), fill=color("marron"))
    lz.guardar(ruta)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="orden", required=True)
    h = sub.add_parser("hojas")
    h.add_argument("carpeta")
    m = sub.add_parser("muestra")
    m.add_argument("salida")
    m.add_argument("--personaje", choices=sorted(PERSONAJES), default="tin")
    m.add_argument("--pose", choices=sorted(POSES), default="parado")
    m.add_argument("--expresion", choices=sorted(EXPRESIONES), default="feliz")
    m.add_argument("--vista", choices=VISTAS, default="frente")
    m.add_argument("--mira", type=int, choices=[-1, 1], default=1)
    m.add_argument("--objeto", choices=OBJETOS, help="objeto de mano (por defecto, el icónico del personaje)")
    m.add_argument("--espejo", action="store_true")
    a = p.parse_args()

    if a.orden == "hojas":
        c = Path(a.carpeta)
        c.mkdir(parents=True, exist_ok=True)
        for pid in PERSONAJES:
            hoja_vueltas(pid, c / f"{pid}_vueltas.png")
            hoja_expresiones(pid, c / f"{pid}_expresiones.png")
            hoja_poses(pid, c / f"{pid}_poses.png")
        hoja_principal(c / "tin_y_tan_principal.png")
        print(f"Hojas -> {c}")
    else:
        lz = Lienzo(1080, 1080)
        dibujar(lz, a.personaje, 540, 960, 820, pose=a.pose, expresion=a.expresion, vista=a.vista, mira=a.mira,
                objeto=a.objeto or True, espejo=a.espejo)
        lz.guardar(a.salida)
        print(f"Muestra -> {a.salida}")


if __name__ == "__main__":
    main()
