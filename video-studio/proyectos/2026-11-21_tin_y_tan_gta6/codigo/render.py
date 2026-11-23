#!/usr/bin/env python3
"""Render del short 2 de Tin & Tan, «How Many Days Did We Wait for GTA 6?», dibujado 100 % con código.

Uso (desde la carpeta del proyecto):
    python3 codigo/render.py                      # audio + 855 fotogramas + 06_final/tin_y_tan_short02_v1.mp4
    python3 codigo/render.py --hoja salida.jpg    # hoja de contacto rápida (un fotograma por pulso), sin video
    python3 codigo/render.py --fotograma 450 f.png
    python3 codigo/render.py --sin-audio          # no rehace el audio (usa 05_audio/mezcla.wav)

La especificación es 02_prompt/prompt.md (13 tomas). 1080x1920, 30 fps, 855 fotogramas (28,5 s = 57 pulsos de 0,5 s).
Los cortes están reajustados a la voz real (05_audio/linea_de_tiempo_voz.md): la voz empieza en el fotograma 0 y cada
corte cae en la rejilla, en el pulso anterior al inicio de la línea que le toca. Todo depende del número de fotograma.
Los personajes y el mando salen de herramientas/palitos.py 1.2 (dibujar, mando), con supermuestreo x3.
La estructura y las funciones comunes (muelles, Marco, texto, borrón, multiproceso) vienen de
`2026-11-21_tin_y_tan_casete_y_lapiz/codigo/render_v2.py`. No usa ningún servicio de pago: Pillow, numpy y ffmpeg.
Nada de Rockstar Games ni de Take-Two: el juego solo se nombra («GTA 5», «GTA 6») con la tipografía del canal.
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
from PIL import Image, ImageDraw, ImageFont

PROY = Path(__file__).resolve().parent.parent
ESTUDIO = PROY.parent.parent
sys.path.insert(0, str(ESTUDIO / "herramientas"))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import palitos  # noqa: E402  (el diseño de Tin y Tan, versión 1.2)
from palitos import PALETA, SS, Lienzo  # noqa: E402

W, H, FPS = 1080, 1920, 30
DUR = 28.5
N = int(round(DUR * FPS))        # 855
SALIDA = PROY / "06_final" / "tin_y_tan_short02_v1.mp4"
FUENTE = "/usr/share/fonts/opentype/inter/InterDisplay-Medium.otf"   # Inter Display Medium, SIL OFL 1.1

PAPEL, SOMBRA, TINTA = PALETA["papel"], PALETA["papel_sombra"], PALETA["tinta"]
MARRON, MOSTAZA, TOMATE, BLANCO = PALETA["marron"], PALETA["mostaza"], PALETA["tomate"], PALETA["blanco"]

# Zona segura (formatos.md): centro de 880x1420
SEG_X0, SEG_X1, SEG_Y0, SEG_Y1 = 100, 980, 250, 1670
SUELO = 0.86 * H                 # 1651
ALTO_PJ = 0.34 * H               # 653: cabeza más alta a 52 %
ALTO_SOLO = 0.44 * H             # 845: plano medio de uno solo (tomas 2 y 11)
X_TAN, X_TIN = 0.30 * W, 0.70 * W
ZONA_G0, ZONA_G1 = 0.27 * H, 0.51 * H      # zona de gráficos cuando hay personajes

# Cortes (s) de las 13 tomas, reajustados a la voz real. Todos caen en la rejilla de 0,5 s.
# Inicio de la voz de cada toma: 0,00 | (línea 1 sigue) | 2,16 | 5,35 | 9,06 | 11,13 | 13,87 | 15,26 | 17,77 | 21,38 |
# 23,79 | 25,50 | (sin voz desde 27,33).
CORTES = [0.0, 1.0, 2.0, 5.0, 9.0, 11.0, 13.5, 15.0, 17.5, 21.0, 23.5, 25.5, 27.5, 28.5]
BORRONES = [1.0, 2.0, 9.0, 17.5, 25.5, 27.5]     # 1→2, 2→3, 4→5, 8→9, 11→12 y 12→13 (sección 8)
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


def empuje(tl, dur):
    """Empuje de cámara de 0 a 1: golpe de muelle `sello` (70 %) y el resto con ease-out cúbico hasta el final de la
    toma, para que la imagen no quede congelada cuando el muelle se asienta."""
    return 0.7 * muelle(tl, SELLO) + 0.3 * eo(tl / dur)


def empuje_lento(tl, dur):
    """Empuje para tomas largas: mitad golpe de muelle `sello`, mitad ease in-out cúbico en toda la toma (la cámara
    sigue moviéndose a mitad de la toma, cuando el muelle ya se asentó)."""
    return 0.5 * muelle(tl, SELLO) + 0.5 * eio(tl / dur)


def acercar(p, total):
    """Cámara de las tomas con personajes: el encuadre final (escala 1) es el del diseño, con todo dentro de la zona
    segura, y la toma EMPIEZA más abierta (escala 1 / (1 + total)). Así el empuje se ve igual («de 100 % a 103 %»)
    pero nada sale nunca de la zona segura. p: avance de 0 a 1."""
    return (1 + total * p) / (1 + total)


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


def suelo(lz):
    lz.d.line([(SEG_X0 * SS, SUELO * SS), (SEG_X1 * SS, SUELO * SS)], fill=SOMBRA, width=4 * SS)


# ---------------------------------------------------------------- texto (capa aparte, no escala con la cámara)
TEXTO_X = 0.10 * W          # 108 px
Y_15 = 0.15 * H             # 288 px: tope de las letras altas de las filas en (10, 15)
Y_PORTADA = 0.26 * H        # 499 px: «GTA 5?» de las tomas 1 y 13, al 12 % del alto: el primer segundo ES la portada
                            # (texto entre y = 400 y 700, dentro de la zona útil de portada de Shorts, y 380-1440)
Y_132 = 0.14 * H            # 269 px: tope de las cifras al 7 % (el pop de llegada no pasa de y = 250)
TRAZO_EM = 0.045            # trazo de tinta de la palabra clave (mostaza o tomate sobre crema no contrastan); eran
                            # 0,06 em, que cerraban las aberturas de los dígitos (revisión del supervisor)
RASGOS = ["ss01"]           # dígitos abiertos de Inter (3, 4, 6 y 9 alternativos de la misma fuente)
CON_TRAZO = (MOSTAZA, TOMATE)
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


def _largo(f, s):
    return f.getlength(s, features=RASGOS)


def _avances(f, s, col, tam):
    """Avance de cada carácter (px x3). La palabra con trazo lleva un espacio extra entre letras del ancho del trazo,
    para que los contornos de dos letras vecinas no se peguen."""
    if col in CON_TRAZO:
        extra = TRAZO_EM * tam * SS
        return [_largo(f, c) + (extra if i < len(s) - 1 else 0) for i, c in enumerate(s)]
    return [_largo(f, s)]


def ancho_texto(segs, tam):
    f = fuente(int(round(tam * SS)))
    return sum(sum(_avances(f, s, col, tam)) for s, col in segs) / SS


@lru_cache(maxsize=1024)
def imagen_texto(segs, tam):
    """segs: tupla de (texto, color). Mostaza y tomate llevan trazo de tinta: Pillow pinta primero el trazo y encima
    el relleno. Todas las cifras usan los «dígitos abiertos» de la propia Inter (rasgo OpenType ss01): con los dígitos
    por defecto, las bahías del 6, el 9, el 3 y el 5 son tan estrechas que el trazo las llenaba de tinta y el número
    salía con una línea por dentro. Devuelve (RGBA x3, margen, línea base)."""
    f = fuente(int(round(tam * SS)))
    sw = max(1, int(round(TRAZO_EM * tam * SS)))
    asc, desc = f.getmetrics()
    margen = sw + 4
    ancho = int(ancho_texto(segs, tam) * SS) + 2 * margen + 4
    img = Image.new("RGBA", (ancho, asc + desc + 2 * margen), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    x = float(margen)
    for s, col in segs:
        if col in CON_TRAZO:
            for c, av in zip(s, _avances(f, s, col, tam)):
                d.text((x, margen + asc), c, font=f, fill=col, anchor="ls", stroke_width=sw, stroke_fill=TINTA,
                       features=RASGOS)
                x += av
        else:
            d.text((x, margen + asc), s, font=f, fill=col, anchor="ls", features=RASGOS)
            x += _largo(f, s)
    return img, margen, margen + asc


def ajustar(segs, pct):
    """Tamaño en px para el porcentaje del alto pedido; si el texto no cabe en la zona segura, se reduce lo justo."""
    tam = pct / 100 * H
    a = ancho_texto(segs, tam) + TRAZO_EM * tam
    if a > ANCHO_MAX:
        tam *= ANCHO_MAX / a
    return tam


def K(s):
    return (s, MOSTAZA)


def T(s):
    return (s, TINTA)


def R(s):
    return (s, TOMATE)


def eo_valor(t, t0, t1, a, b):
    """Contador: entero entre a y b con ease-out cúbico; solo sube y nunca pasa de b."""
    return a + int(round((b - a) * eo((t - t0) / (t1 - t0))))


# Contadores: (inicio, fin, valor inicial, valor final)
C_4745 = (11.15, 12.9, 0, 4745)   # empieza 2 fotogramas antes que su texto: nunca se ve «0 days»
C_4748 = (15.6, 18.0, 4745, 4748)   # llega a 4,748 en 16,7, cuando la voz acaba de decir «forty-eight»
C_63 = (17.75, 18.8, 0, 63)        # ídem: nunca se ve «+0 days»
C_4811 = (21.4, 22.8, 4748, 4811)   # llega a 4,811 en 22,53, mientras la voz dice «eight hundred eleven» (desde 22,23)

def t_llegada(c):
    """Segundo del primer fotograma en que el contador muestra su valor final (por el redondeo llega antes de que
    acabe el ease-out). A ese fotograma se atan el cambio a tomate, el pop del texto y el sonido."""
    return next(f for f in range(N) if eo_valor(f / FPS, *c) == c[3]) / FPS


LLEGA_4748, LLEGA_4811 = t_llegada(C_4748), t_llegada(C_4811)

# (entra, sale, tamaño en % del alto, tope de las letras, segmentos o nombre de contador, pop de llegada)
# Texto exacto de la tabla de la sección 12 del prompt.
TEXTOS = [
    (0.0, 0.9, 12, Y_PORTADA, (T("GTA "), K("5"), T("?")), None),
    (2.9, 4.9, 5, Y_15, (T("how many "), K("days"), T("?")), None),
    (5.1, 8.9, 7, Y_132, (T("GTA "), K("5")), None),
    (9.2, 10.9, 7, Y_132, (K("13"), T(" × 365")), None),
    (11.2, 13.4, 7, Y_132, "c4745", None),
    (13.7, 14.9, 7, Y_132, (T("+"), K("3"), T(" leap days")), None),
    (15.1, 17.4, 7, Y_132, "c4748", (LLEGA_4748, 0.10)),
    (17.8, 19.3, 7, Y_132, "c63", None),
    (19.4, 20.9, 7, Y_132, (T("GTA "), K("6")), None),
    (21.2, 25.4, 7, Y_15, "c4811", (LLEGA_4811, 0.14)),    # se queda toda la toma 11 (el pago del video)
    (25.7, 27.4, 7, Y_132, (T("age "), R("13")), None),
    (27.6, 28.5, 12, Y_PORTADA, (T("GTA "), K("5"), T("?")), None),
]


def segmentos(t, que):
    if que == "c4745":
        return (K(f"{eo_valor(t, *C_4745):,}"), T(" days"))
    if que == "c4748":
        return (K(f"{eo_valor(t, *C_4748):,}"), T(" days"))
    if que == "c63":
        return (T("+"), K(f"{eo_valor(t, *C_63)}"), T(" days"))
    if que == "c4811":
        v = eo_valor(t, *C_4811)
        return ((f"{v:,}", TOMATE if v >= C_4811[3] else TINTA), T(" days"))
    return que


def referencia(que):
    """El texto más ancho que puede mostrar la fila (fija el tamaño, para que no cambie mientras el contador sube)."""
    return {"c4745": (K("4,745"), T(" days")), "c4748": (K("4,748"), T(" days")), "c63": (T("+"), K("63"), T(" days")),
            "c4811": (R("4,811"), T(" days"))}.get(que, que) if isinstance(que, str) else que


def capa_texto(base, f):
    """Pega sobre `base` (RGB 1080x1920) el texto que toca en el fotograma f."""
    t = f / FPS
    for i, (entra, sale, pct, tope, que, llegada) in enumerate(TEXTOS):
        fi, fs = int(round(entra * FPS)), int(round(sale * FPS))
        if not (fi <= f < fs):
            continue
        segs = segmentos(t, que)
        tam = ajustar(referencia(que), pct)
        primero, ultimo = i == 0, i == len(TEXTOS) - 1
        if primero:                                             # ya entero en el fotograma 0: sin pop
            esc, alfa = 1.0, 1.0
        elif ultimo:                                            # llega a escala 1 exacta en el último fotograma (bucle)
            esc, alfa = 0.85 + 0.15 * muelle_exacto(t - entra, POP, sale - entra), min(1.0, (f - fi + 1) / 2)
        else:
            esc, alfa = 0.85 + 0.15 * muelle(t - entra, POP), min(1.0, (f - fi + 1) / 2)   # pop de 0,85 a 1
        dy = 0.0
        if llegada and t >= llegada[0]:                         # al llegar el contador: pop de escala solo del texto
            esc *= 1 + llegada[1] * (1 - muelle(t - llegada[0], POP))
        if f >= fs - 3 and not ultimo:                          # salida: sube 2 % con ease-in en 3 fotogramas
            u = (f - (fs - 3) + 1) / 4
            # sube 2 %, pero sin que el tope del texto pase de la zona segura (y = 250) mientras se desvanece
            dy = -min(0.02 * H * u * u, max(0.0, tope - TRAZO_EM * tam - 0.03 * tam - SEG_Y0 - 2))
            alfa *= 1 - u * u
        img, margen, linea = imagen_texto(segs, tam)
        k = esc / SS
        chico = img.resize((max(1, int(round(img.width * k))), max(1, int(round(img.height * k)))), Image.LANCZOS)
        # ancla: borde izquierdo y media altura de las minúsculas; el tope de las letras altas queda en `tope`
        base_y = tope + 0.74 * tam
        ancla_y = base_y - 0.30 * tam
        x = TEXTO_X - margen * k
        y = ancla_y + dy - (linea - 0.30 * tam * SS) * k
        if alfa < 1:
            chico.putalpha(chico.getchannel("A").point(lambda v: int(v * alfa)))
        base.paste(chico, (int(round(x)), int(round(y))), chico)
    return base


# ---------------------------------------------------------------- gráficos propios del video
def mando_grande(lz, t):
    """El mando a pantalla completa (sección 5): W = 800 px, centro en (50 %, 54 %), balanceo de ±5 grados con periodo
    de 0,5 s, estela plana de dos copias en papel sombra y botón de abajo que late 0,2 s en cada pulso (a papel)."""
    cx, cy, ancho = 0.5 * W, 0.54 * H, 800.0      # 800 px: con el balanceo y el empuje a 106 % queda en x 100-980

    def ang(tt):
        return 5 * math.sin(4 * math.pi * tt)
    for atras in (0.08, 0.04):
        palitos.mando(lz, cx, cy, ancho, ang(t - atras), relleno="papel_sombra", tinta="papel_sombra", detalles=False)
    # el latido se cuenta en fotogramas (6 de cada 15) para que no dependa del redondeo de t
    f = int(round(t * FPS))
    palitos.mando(lz, cx, cy, ancho, ang(t), boton_pulsado=(f % 15) < 6)
    return cx, cy


def texto_en_lienzo(lz, s, x_izq, y_centro, tam, esc=1.0, esc_y=1.0, alfa=1.0):
    """Texto en tinta que es parte del dibujo (la fecha de la hoja): alineado a la izquierda en x_izq, con el centro de
    las cifras en y_centro. Se pega en el lienzo grande, así que escala con la cámara."""
    img, margen, linea = imagen_texto(((s, TINTA),), tam)
    w, h = max(1, int(round(img.width * esc))), max(1, int(round(img.height * esc * esc_y)))
    if h < 3:
        return
    capa = img.resize((w, h), Image.LANCZOS)
    if alfa < 1:
        capa.putalpha(capa.getchannel("A").point(lambda v: int(v * alfa)))
    x = x_izq * SS - margen * esc
    y = (y_centro + 0.36 * tam * esc * esc_y) * SS - linea * esc * esc_y
    lz.img.paste(capa, (int(round(x)), int(round(y))), capa)


def hoja_calendario(lz, cx, y_top, ancho, alto, texto, pct, cabecera=MOSTAZA, esc_y=1.0, esc_texto=1.0, alfa_texto=1.0):
    """Hoja de calendario (sección 5): cuerpo blanco, cabecera (mostaza = acento del plano, o marrón), dos anillas y la
    pila de dos hojas en papel sombra. esc_y: escala vertical de la hoja de encima alrededor de su borde de arriba
    (vuelta de hoja). La fecha va en el cuerpo, alineada a la izquierda con 0,07 W de margen."""
    m = Marco(lz, cx, y_top)
    w, b, r = ancho / 2, 0.012 * ancho, 0.03 * ancho
    for k in (2, 1):                                         # la pila: dos hojas más, 14 px hacia abajo cada una
        m.caja(-w, 14 * k, w, alto + 14 * k, SOMBRA, b, radio=r)
    h = alto * esc_y
    if h > 4 * b:
        m.caja(-w, 0, w, h, BLANCO, b, radio=min(r, h / 2))
        yc = 0.22 * h
        m.rect(-w + b, b, w - b, yc, cabecera, max(0.0, min(r, h / 2) - b))
        m.rect(-w + b, yc / 2, w - b, yc, cabecera)
        m.rect(-w + b, yc - b / 2, w - b, yc + b / 2, TINTA)
        if texto:
            texto_en_lienzo(lz, texto, cx - w + 0.07 * ancho, y_top + yc + (h - yc) / 2, pct / 100 * H * esc_texto,
                            esc_y=esc_y, alfa=alfa_texto)
    for sx in (-0.25, 0.25):                                 # anillas
        m.disco(sx * ancho, 0, 0.02 * ancho, TINTA)
        m.disco(sx * ancho, 0, 0.02 * ancho - b * 0.6, PAPEL)


def vuelta(t, t0, sale=0.15, entra=0.15):
    """Vuelta de hoja que empieza en t0: la hoja baja de 1 a 0 (muelle sello) y la nueva sube de 0 a 1 (muelle pop).
    Devuelve (escala vertical, True si ya se ve la hoja nueva)."""
    tau = t - t0
    if tau < 0:
        return 1.0, False
    if tau < sale:
        return 1 - muelle_exacto(tau, SELLO, sale), False
    return muelle_exacto(tau - sale, POP, entra), True


# Tira de 13 años: 13 bloques de 60 x 200 px separados 8 px, centrada en x = 50 % y en y = 39 %
TIRA_Y = 0.39 * H
TIRA_X0 = 0.5 * W - (13 * 60 + 12 * 8) / 2          # 102 px; termina en 978
BISIESTOS = (3, 7, 11)                              # años de sept. 2015-16, 2019-20 y 2023-24 (29-feb de 2016, 2020, 2024)


def tira_13(lz, llenos=13, color_ultimo=MARRON, marcas=(), corchete=False, esc_bloque=None):
    """llenos: cuántos bloques están llenos (o función bloque -> escala de llenado 0..1). marcas: escalas (0..1) de las
    tres marcas bisiestas. esc_bloque: escala extra del bloque 13 (latido)."""
    m = Marco(lz, 0, 0)
    for i in range(13):
        x0 = TIRA_X0 + i * 68
        p = llenos(i) if callable(llenos) else (1.0 if i < llenos else 0.0)
        col = SOMBRA if p <= 0 else (color_ultimo if i == 12 else MARRON)
        e = (0.85 + 0.15 * p) if 0 < p else 1.0
        if i == 12 and esc_bloque:
            e *= esc_bloque
        # el latido del bloque 13 crece hacia la izquierda: su borde derecho no pasa de x = 978 (zona segura)
        mb = Marco(lz, x0 + 30 - (30 * (e - 1) if i == 12 and e > 1 else 0), TIRA_Y, e)
        mb.caja(-30, -100, 30, 100, col, 8)
    for k, esc in zip(BISIESTOS, marcas):
        if esc > 0.02:
            x = TIRA_X0 + (k - 1) * 68 + 30
            m.disco(x, TIRA_Y - 100 - 40, 18 * esc, TINTA)
            m.disco(x, TIRA_Y - 100 - 40, max(0.0, 18 * esc - 4), MOSTAZA)
    if corchete:
        y = TIRA_Y + 100 + 0.04 * H
        m.linea([(SEG_X0 + 5, y - 30), (SEG_X0 + 5, y), (SEG_X1 - 5, y), (SEG_X1 - 5, y - 30)], 10, TINTA)


def vaiven(tl, amp=0.3, f=0.9):
    """Viento de la bufanda de Tan: oscila y se va calmando sin pararse nunca (para que el plano no se congele)."""
    return amp * (0.6 + 0.4 * math.exp(-0.8 * tl)) * math.cos(2 * math.pi * f * tl)


def sacudida(tl):
    """Movimiento secundario del objeto de la mano: ±3 grados, una sacudida de muelle por segundo."""
    tau = tl % 1.0
    return 3 * math.exp(-2.2 * tau) * math.sin(2 * math.pi * 2.0 * tau)


def bote(t, fase=0.0, amp=0.022):
    """Rebote de los personajes al pulso (0,5 s): la figura crece hasta un 2,2 % desde los pies y vuelve, con caída
    exponencial (los pies no se mueven). Sirve para que ningún plano quede congelado. fase en pulsos."""
    tau = (t / 0.5 + fase) % 1.0
    return 1 + amp * math.exp(-4.0 * tau) * math.sin(math.pi * min(1.0, tau * 5)) + 0.006 * math.sin(2 * math.pi * tau)


# ---------------------------------------------------------------- tomas: cada una dibuja en el lienzo y devuelve la cámara
CENTRO = (W / 2, H / 2)
HOJA_G = dict(cx=0.5 * W, y_top=0.28 * H, ancho=0.80 * W, alto=1000)       # hoja grande, toma 3: centro en 54 %
# hoja de la zona de gráficos (tomas 4 y 9): 800 px de ancho; con la pila (28 px) va de 27 % a 48,5 %. El prompt pide
# 460 px de alto (27 % a 51 %), pero con la pila tocaba el rodete de Tan y la gorra de Tin (cabezas desde 52 %).
HOJA_Z = dict(cx=0.5 * W, y_top=ZONA_G0, ancho=800, alto=0.485 * H - ZONA_G0 - 28)


def toma_1(lz, t):
    c = mando_grande(lz, t)
    return 1 + 0.06 * empuje(t, 1.0), c


def toma_2(lz, t):
    tl = t - 1.0
    suelo(lz)
    palitos.dibujar(lz, "tan", 0.5 * W, SUELO, ALTO_SOLO * bote(t), pose="pregunta", expresion="nostalgia", vista="frente", mira=1,
                    viento=vaiven(tl), objeto="control", espejo=True,
                    giro_objeto=10 * math.exp(-3.0 * tl) * math.cos(2 * math.pi * 2.0 * tl))
    return acercar(empuje(tl, 1.0), 0.02), CENTRO


def toma_3(lz, t):
    tl = t - 2.0
    e, nueva = vuelta(t, 3.8)
    if nueva:
        hoja_calendario(lz, texto="Nov 19, 2026", pct=5.5, esc_y=e, **HOJA_G)
    else:
        hoja_calendario(lz, texto="Sep 17, 2013", pct=5.5, esc_y=e, esc_texto=0.85 + 0.15 * muelle(tl, POP), **HOJA_G)
    return acercar(empuje_lento(tl, 3.0), 0.06), (0.5 * W, 0.54 * H)


T4_FECHA = 6.6            # «September seventeenth» empieza hacia 6,6: ahí entra la fecha en la hoja


def toma_4(lz, t):
    """Tin lleva su lápiz (el motivo del canal): es el elemento mostaza del plano, y por eso aquí la cabecera de la hoja
    va en marrón (neutro) y no en mostaza. La hoja está en blanco mientras suena «G T A five came out» y la fecha entra
    con pop en 6,6 (cambio a mitad de toma); Tin sacude el lápiz y Tan pasa de saludar a sonreír."""
    tl = t - 5.0
    suelo(lz)
    if t < T4_FECHA:
        hoja_calendario(lz, texto=None, pct=4.6, cabecera=MARRON, **HOJA_Z)
    else:
        tf = t - T4_FECHA
        hoja_calendario(lz, texto="Sep 17, 2013", pct=4.6, cabecera=MARRON, esc_texto=0.85 + 0.15 * muelle(tf, POP),
                        alfa_texto=min(1.0, tf * FPS / 2 + 0.5), **HOJA_Z)
    palitos.dibujar(lz, "tan", X_TAN, SUELO, ALTO_PJ * bote(t), pose="saluda",
                    expresion="nostalgia" if t < T4_FECHA else "feliz", vista="frente", viento=vaiven(tl), espejo=True)
    giro = sacudida(tl) if t < T4_FECHA else 9 * math.exp(-2.5 * (t - T4_FECHA)) * math.cos(2 * math.pi * 2.5 * (t - T4_FECHA)) \
        + sacudida(tl) * (1 - math.exp(-2.5 * (t - T4_FECHA)))
    palitos.dibujar(lz, "tin", X_TIN, SUELO, ALTO_PJ * bote(t, 0.5), pose="explica", expresion="feliz", vista="frente",
                    objeto="lapiz", giro_objeto=giro)
    return acercar(empuje_lento(tl, 4.0), 0.03), CENTRO


T5_LLENADO = 9.2          # un bloque cada 0,1 s: de 9,2 a 10,4 (el 13 se llena en 10,4)


def toma_5(lz, t):
    tl = t - 9.0
    suelo(lz)
    tira_13(lz, llenos=lambda i: muelle(t - (T5_LLENADO + 0.1 * i), POP), color_ultimo=MOSTAZA)
    palitos.dibujar(lz, "tan", 0.5 * W, SUELO, ALTO_PJ * bote(t), pose="senala", expresion="curiosidad", vista="frente",
                    viento=vaiven(tl, 0.25), espejo=True)
    return 1.0, CENTRO


def toma_6(lz, t):
    tl = t - 11.0
    suelo(lz)
    tira_13(lz, color_ultimo=MOSTAZA, corchete=True)
    palitos.dibujar(lz, "tan", 0.5 * W, SUELO, ALTO_PJ * bote(t), pose="pregunta", expresion="sorpresa", vista="frente",
                    viento=0.9 * math.exp(-1.0 * tl) * math.cos(2 * math.pi * 1.5 * tl) + vaiven(tl, 0.15), espejo=True)
    return 1.0, CENTRO


T7_MARCAS = (13.9, 14.2, 14.5)


def toma_7(lz, t):
    tl = t - 13.5
    suelo(lz)
    tira_13(lz, marcas=[muelle(t - m, POP) for m in T7_MARCAS])
    palitos.dibujar(lz, "tan", 0.5 * W, SUELO, ALTO_PJ * bote(t), pose="explica", expresion="feliz", vista="frente",
                    viento=vaiven(tl, 0.25), espejo=True)
    return 1.0, CENTRO


def toma_8(lz, t):
    tl = t - 15.0
    suelo(lz)
    tira_13(lz, marcas=(1, 1, 1), corchete=True)
    palitos.dibujar(lz, "tan", 0.5 * W, SUELO, ALTO_PJ * bote(t), pose="parado",
                    expresion="curiosidad" if t < LLEGA_4748 else "feliz", vista="frente",   # reacciona al llegar
                    viento=vaiven(tl, 0.22, 0.6), espejo=True)
    return 1.0, CENTRO


T9_BLANCAS = [17.56 + 0.18 * k for k in range(6)]     # 6 hojas en blanco, una cada 0,18 s (la última acaba en 18,64)
T9_FECHA_1, T9_VUELTA = 18.6, 19.4      # la hoja pasa a «Nov 19, 2026» con «to November…» (hacia 19,6)


def toma_9(lz, t):
    tl = t - 17.5
    suelo(lz)
    if t < T9_FECHA_1:
        e = 1.0
        for tk in T9_BLANCAS:
            if t >= tk:
                e, _ = vuelta(t, tk, 0.09, 0.09)
        hoja_calendario(lz, texto=None, pct=4.6, esc_y=e, **HOJA_Z)
    else:
        e, nueva = vuelta(t, T9_VUELTA)
        if nueva:
            hoja_calendario(lz, texto="Nov 19, 2026", pct=4.6, esc_y=e, **HOJA_Z)
        else:
            p = muelle(t - T9_FECHA_1, POP)
            hoja_calendario(lz, texto="Sep 17, 2026", pct=4.6, esc_y=e, esc_texto=0.85 + 0.15 * p,
                            alfa_texto=min(1.0, (t - T9_FECHA_1) * FPS / 2 + 0.5), **HOJA_Z)
    palitos.dibujar(lz, "tan", 0.5 * W, SUELO, ALTO_PJ * bote(t), pose="piensa",
                    expresion="curiosidad" if t < T9_VUELTA else "nostalgia", vista="frente",   # cambia con la hoja
                    viento=vaiven(tl, 0.22, 0.7), objeto=False, espejo=True)
    return acercar(empuje_lento(tl, 3.5), 0.04), CENTRO


def toma_10(lz, t):
    tl = t - 21.0
    suelo(lz)
    tau = tl if t < LLEGA_4811 else t - LLEGA_4811
    viento = 0.9 * math.exp(-1.3 * tau) * math.cos(2 * math.pi * 1.5 * tau) + vaiven(tl, 0.12)
    palitos.dibujar(lz, "tan", X_TAN, SUELO, ALTO_PJ * bote(t), pose="celebra", expresion="sorpresa", vista="frente",
                    viento=viento, espejo=True)
    palitos.dibujar(lz, "tin", X_TIN, SUELO, ALTO_PJ * bote(t, 0.5), pose="saluda", expresion="eureka", vista="frente", objeto=False)
    return acercar(empuje(tl, 2.5), 0.03), CENTRO


def toma_11(lz, t):
    tl = t - 23.5
    suelo(lz)
    palitos.dibujar(lz, "tan", 0.5 * W, SUELO, ALTO_SOLO * bote(t), pose="encoge", expresion="sorpresa", vista="frente",
                    viento=0.5 * math.exp(-1.5 * tl) * math.cos(2 * math.pi * 1.5 * tl) + vaiven(tl, 0.15), objeto=False,
                    espejo=True)
    return acercar(empuje(tl, 2.0), 0.06), CENTRO


T12_LATIDOS = (26.0, 26.5, 27.0)


def toma_12(lz, t):
    tl = t - 25.5
    suelo(lz)
    lat = [t - x for x in T12_LATIDOS if t >= x]
    esc = 1 + 0.22 * (1 - muelle(lat[-1], POP)) if lat else 1.0
    tira_13(lz, color_ultimo=TOMATE if lat else MARRON, esc_bloque=esc)
    palitos.dibujar(lz, "tan", X_TAN, SUELO, ALTO_PJ * bote(t), pose="encoge", expresion="risa", vista="frente",
                    viento=0.4 * math.exp(-2 * tl) * math.cos(2 * math.pi * 2 * tl) + vaiven(tl, 0.15), espejo=True)
    # Tin 14 px a la izquierda de x = 70 %: con el brazo arriba el calendario no cabía en la zona segura sin tocar la visera
    palitos.dibujar(lz, "tin", X_TIN - 14, SUELO, ALTO_PJ * bote(t, 0.5), pose="celebra", expresion="risa", vista="frente",
                    objeto="calendario", giro_objeto=sacudida(tl))
    return 1.0, CENTRO


def toma_13(lz, t):
    tl = t - 27.5
    c = mando_grande(lz, t)
    p = 0.7 * muelle_exacto(tl, SELLO, 1.0) + 0.3 * eo(tl / 1.0)      # llega a 1 exacto en 28,5: escala 100 %
    return 1.06 - 0.06 * p, c


TOMAS = [toma_1, toma_2, toma_3, toma_4, toma_5, toma_6, toma_7, toma_8, toma_9, toma_10, toma_11, toma_12, toma_13]


def toma_de(f):
    t = f / FPS
    for i in range(len(CORTES) - 1):
        if CORTES[i] <= t < CORTES[i + 1]:
            return i + 1
    return 13


def borron_horizontal(img, px):
    """Desenfoque de movimiento horizontal (media móvil de `px` píxeles)."""
    a = np.asarray(img, dtype=np.float32)
    izq, der = px // 2, px - px // 2
    b = np.pad(a, ((0, 0), (izq + 1, der), (0, 0)), mode="edge")
    c = np.cumsum(b, axis=1)
    out = (c[:, px:px + a.shape[1]] - c[:, :a.shape[1]]) / px
    return Image.fromarray(np.clip(out + 0.5, 0, 255).astype(np.uint8))


def fotograma(f, envolver=True):
    """Devuelve el fotograma f (0 a 854) como imagen RGB de 1080x1920. Con envolver=False, el fotograma 855 se dibuja
    como el final de la toma 13 (sin texto ni borrón): sirve para comprobar que el bucle empalma con el fotograma 0."""
    crudo = not envolver and f >= N
    if envolver:
        f = f % N                  # el fotograma 855 es el 0: bucle
    t = f / FPS
    n = 13 if crudo else toma_de(f)
    lz = Lienzo(W, H)
    z, c = TOMAS[n - 1](lz, t)
    if abs(z - 1) < 1e-9:
        img = lz.resultado()
    elif z < 1:                    # encuadre más abierto que el lienzo: se reduce y se rodea de papel (el fondo es plano)
        w, h = int(round(W * z)), int(round(H * z))
        img = Image.new("RGB", (W, H), PAPEL)
        chico = lz.img.resize((w, h), Image.LANCZOS)
        img.paste(chico, (int(round(c[0] * (1 - z))), int(round(c[1] * (1 - z)))))
    else:                          # empuje de cámara: se recorta el lienzo grande y se reduce (no pierde nitidez)
        x0, y0 = c[0] - c[0] / z, c[1] - c[1] / z
        img = lz.img.resize((W, H), Image.LANCZOS, box=(x0 * SS, y0 * SS, (x0 + W / z) * SS, (y0 + H / z) * SS))
    if crudo:
        return img
    for corte in BORRONES:         # borrón: 2 fotogramas antes y 2 después del corte
        fc = int(round(corte * FPS))
        if fc - 2 <= f < fc + 2:
            img = borron_horizontal(img, BORRON_PX)
    return capa_texto(img, f)


def _bytes(f):
    return fotograma(f).tobytes()


def todos_los_textos():
    fijos = ["".join(s for s, _ in referencia(que)) for *_, que, _ in TEXTOS]
    return fijos + ["0123456789,", "Sep 17, 2013", "Nov 19, 2026", "Sep 17, 2026", "17"]


def comprobaciones():
    """Lo que se puede comprobar antes de dibujar: glifos, rejilla, contadores, textos dentro de la zona segura."""
    usados = comprobar_glifos(todos_los_textos())
    assert all(abs(c * 2 - round(c * 2)) < 1e-9 for c in CORTES), "un corte no cae en la rejilla de 0,5 s"
    assert abs(DUR * 2 - round(DUR * 2)) < 1e-9 and DUR <= 30
    for c in (C_4745, C_4748, C_63, C_4811):
        v = [eo_valor(f / FPS, *c) for f in range(N)]
        assert all(b >= a for a, b in zip(v, v[1:])) and max(v) == c[3] and min(v) == c[2], f"contador mal: {c}"
    notas = []
    for entra, sale, pct, tope, que, llegada in TEXTOS:
        ref = referencia(que)
        tam = ajustar(ref, pct)
        ancho = ancho_texto(ref, tam) * (1 + (llegada[1] if llegada else 0.0))
        assert TEXTO_X + ancho + TRAZO_EM * tam <= SEG_X1 + 0.5, f"texto fuera de la zona segura: {que}"
        alto_pop = tope - 0.44 * tam * (llegada[1] if llegada else 0.012) - TRAZO_EM * tam
        assert alto_pop >= SEG_Y0 - 0.5, f"texto por encima de la zona segura: {que} ({alto_pop:.0f} px)"
        assert len("".join(s for s, _ in ref).split()) <= 3, f"subtítulo de más de 3 palabras: {que}"
        if abs(tam - pct / 100 * H) > 0.01:
            notas.append(f"«{''.join(s for s, _ in ref)}»: {pct} % no cabe; queda en {tam / H * 100:.2f} % ({tam:.1f} px)")
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
    print(f"palitos.py {palitos.VERSION}. Glifos comprobados en Inter Display Medium: {''.join(usados)}")
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
    with Pool(4) as pool:
        for i, datos in enumerate(pool.imap(_bytes, range(N), chunksize=4)):
            ff.stdin.write(datos)
            if i % 150 == 0:
                print(f"  fotograma {i}/{N}  ({time.time() - inicio:.0f} s)", flush=True)
    ff.stdin.close()
    if ff.wait() != 0:
        sys.exit("ffmpeg falló")
    # bucle: (1) el fotograma 855 se dibuja con la misma función que el 0; (2) la toma 13 llevada a t = 28,5 (ángulo 0,
    # escala 100 %) es el mismo dibujo que el fotograma 0 sin texto, y el texto del cierre llega a escala 1 exacta.
    assert fotograma(N).tobytes() == fotograma(0).tobytes()
    fin_13 = np.asarray(capa_texto(fotograma(N, envolver=False), 0), dtype=np.int16)
    dif = np.abs(fin_13 - np.asarray(fotograma(0), dtype=np.int16))
    print(f"Bucle: toma 13 en t = {DUR} frente al fotograma 0: diferencia máxima {int(dif.max())} de 255, media {dif.mean():.4f}")
    print(f"Video -> {SALIDA}  ({time.time() - inicio:.0f} s en total; dibujo y codificación {time.time() - t_dibujo:.0f} s)")


if __name__ == "__main__":
    main()
