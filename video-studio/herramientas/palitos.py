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
"""
import argparse
import math
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

VERSION = "1.1"  # 1.0: diseño aprobado (2026-11-21) · 1.1: espejo
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


# ---------------------------------------------------------------- cabeza (sirve sola para primeros planos)
def cabeza(lz, pid, cx, cy, radio, expresion="feliz", vista="frente", mira=1, espejo=False):
    """Dibuja solo la cabeza con sus accesorios, centrada en (cx, cy) y con ese radio en píxeles."""
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
            objeto=True, espejo=False):
    """Dibuja a Tin o Tan con los pies en (x, suelo) y una altura total de `alto` píxeles.

    mira: 1 mira a la derecha, -1 a la izquierda (solo en perfil). viento: puntas de la bufanda (-1 a 1).
    espejo: dibuja la figura entera reflejada. Por defecto el brazo que hace el gesto queda a la DERECHA del cuadro;
    con espejo=True queda a la IZQUIERDA. Regla de los planos de dos: cada uno gesticula del lado contrario al otro
    (Tan, a la izquierda del cuadro, va con espejo=True; Tin, a la derecha, sin espejo).
    """
    if pid not in PERSONAJES:
        sys.exit(f"Personaje desconocido: {pid}. Hay: {', '.join(PERSONAJES)}")
    pj, ps = PERSONAJES[pid], POSES[pose]
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
    cabeza(lz, pid, x, suelo + cabeza_y * R, R, expresion, vista, s, espejo)

    # objeto icónico en la mano derecha (vista de frente) o en la de adelante (perfil)
    if objeto and pj["objeto"] == "lapiz" and vista != "espalda":
        m = manos[1]
        lapiz(pl, m[0] + 0.05, m[1] - 0.25, angulo=-60 if pose in ("saluda", "celebra", "pregunta") else -35)
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
        dibujar(lz, a.personaje, 540, 960, 820, pose=a.pose, expresion=a.expresion, vista=a.vista, mira=a.mira)
        lz.guardar(a.salida)
        print(f"Muestra -> {a.salida}")


if __name__ == "__main__":
    main()
