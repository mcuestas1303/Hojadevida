#!/usr/bin/env python3
"""La Duda, versión 2 (2026-11-26): cuerpo de palitos con manos y pies; la madeja de tinta es la cabeza.

Pedido del dueño: «debe tener manos, pies y cuerpo; esa forma podría ser la cabeza; hacele un sheet de personaje».
Uso:  python3 duda_v2.py <hoja.png>
Aquí el torso sí se inclina (cosa que `palitos.py` 1.4 no hace): el esqueleto es el que hará falta también para Tin y Tan.
"""
import math
import sys
from pathlib import Path

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "herramientas"))
import palitos  # noqa: E402

SS = 3
PAPEL, TINTA, SOMBRA = (palitos.PALETA[k] for k in ("papel", "tinta", "papel_sombra"))
# Medidas en R (R = radio de cabeza de Tin y Tan, para comparar)
CABEZA, CUELLO, TORSO, BRAZO, ANTEBRAZO, MUSLO, PIERNA, GROSOR = 1.35, 0.15, 1.9, 0.95, 0.9, 1.05, 1.0, 0.19

POSES = {   # ángulos en pantalla, desde la vertical hacia abajo; positivo = hacia la derecha del cuadro
    "parado":  {"torso": 0,   "bi": (-14, -6),   "bd": (14, 6),     "pi": (-9, -4),  "pd": (9, 4)},
    "guardia": {"torso": 10,  "bi": (40, 150),   "bd": (70, 165),   "pi": (-28, -8), "pd": (30, 2)},
    "golpe":   {"torso": 24,  "bi": (-30, 60),   "bd": (92, 90),    "pi": (-40, -20), "pd": (38, -6)},
    "patada":  {"torso": -22, "bi": (-70, -120), "bd": (40, 130),   "pi": (-8, -2),  "pd": (96, 92)},
    "recibe":  {"torso": -30, "bi": (-110, -150), "bd": (-60, -20), "pi": (-34, -10), "pd": (16, 40)},
    "caido":   {"torso": -88, "bi": (-150, -175), "bd": (-70, -95), "pi": (70, 96),  "pd": (84, 60)},
}


def seg(o, ang, largo):
    a = math.radians(ang)
    return (o[0] + math.sin(a) * largo, o[1] + math.cos(a) * largo)


def madeja(hervor=0.0):
    pts, n = [], 520
    for i in range(n):
        t = i / (n - 1) * 2 * math.pi
        x = 0.62 * math.sin(7 * t + 0.4 + 0.05 * hervor) + 0.34 * math.sin(11 * t + 1.3) + 0.06 * math.sin(29 * t + hervor)
        y = 0.58 * math.cos(5 * t + 0.9) + 0.36 * math.cos(13 * t + 0.2 + 0.05 * hervor) + 0.06 * math.cos(31 * t - hervor)
        pts.append((x, y * 0.92))
    return pts


def duda(img, x, suelo, R, pose="parado", vista="perfil", mira=1, dibujado=1.0, hervor=0.0):
    """Pies en (x, suelo). vista: frente | perfil | espalda. mira: 1 derecha, -1 izquierda (refleja la pose)."""
    ps = POSES[pose] if isinstance(pose, str) else pose
    d = ImageDraw.Draw(img)
    m = mira
    cadera = (0.0, 0.0)
    cuello = seg(cadera, 180 - ps["torso"], TORSO)
    hombro = seg(cadera, 180 - ps["torso"], TORSO - 0.2)
    centro = seg(cuello, 180 - ps["torso"], CUELLO + CABEZA * 0.82)
    brazos = [(hombro, seg(hombro, ps[k][0], BRAZO)) for k in ("bi", "bd")]
    brazos = [(h, c, seg(c, ps[k][1], ANTEBRAZO)) for (h, c), k in zip(brazos, ("bi", "bd"))]
    piernas = [(cadera, seg(cadera, ps[k][0], MUSLO)) for k in ("pi", "pd")]
    piernas = [(c, r, seg(r, ps[k][1], PIERNA)) for (c, r), k in zip(piernas, ("pi", "pd"))]
    bajo = max([p[2][1] for p in piernas] + [b[2][1] for b in brazos] + [centro[1] + CABEZA * 0.75])

    def px(p):
        return ((x + m * p[0] * R) * SS, (suelo + (p[1] - bajo) * R) * SS)

    g = max(2, int(GROSOR * R * SS))

    def linea(pts, ancho=g):
        q = [px(p) for p in pts]
        d.line(q, fill=TINTA, width=ancho, joint="curve")
        for a in q:
            d.ellipse([a[0] - ancho / 2, a[1] - ancho / 2, a[0] + ancho / 2, a[1] + ancho / 2], fill=TINTA)

    # pierna y brazo de atrás, torso, pierna y brazo de delante
    orden = (0, 1) if m > 0 else (0, 1)
    for i in orden:
        c, r, pie = piernas[i]
        linea([c, r, pie])
        q = px(pie)
        dx = (1 if (ps["pi" if i == 0 else "pd"][1] >= -30) else -1) * m if vista != "frente" else (-1 if i == 0 else 1)
        rx, ry = 0.34 * R * SS, 0.15 * R * SS
        d.ellipse([q[0] - rx + dx * 0.2 * R * SS, q[1] - ry, q[0] + rx + dx * 0.2 * R * SS, q[1] + ry], fill=TINTA)
    linea([cadera, cuello])
    for h, c, mano in brazos:
        linea([h, c, mano])
        q = px(mano)
        rr = 0.21 * R * SS
        d.ellipse([q[0] - rr, q[1] - rr, q[0] + rr, q[1] + rr], fill=TINTA)

    # cabeza: la madeja, con el rizo de pregunta y dos huecos de papel
    cx, cy = px(centro)
    rad = CABEZA * R * SS
    gm = max(2, int(0.11 * rad))
    pts = madeja(hervor)
    k = max(2, int(len(pts) * max(0.0, min(1.0, dibujado))))
    d.line([(cx + p[0] * rad, cy + p[1] * rad) for p in pts[:k]], fill=TINTA, width=gm, joint="curve")
    if dibujado > 0.85:
        riz = []
        for i in range(40):
            a = math.radians(-200 + i * 7.2)
            riz.append((cx + m * 0.34 * math.cos(a) * rad, cy + (-1.42 + 0.3 * math.sin(a)) * rad))
        riz += [(cx + m * 0.02 * rad, cy + (-1.1 + 0.02 * j) * rad) for j in range(8)]
        d.line(riz, fill=TINTA, width=gm, joint="curve")
        if vista != "espalda":
            ojos = (-0.3, 0.3) if vista == "frente" else (0.12, 0.6)
            for i, ox in enumerate(ojos):
                esc = 1.0 if vista == "frente" or i == 1 else 0.8
                qx, qy = cx + m * ox * rad, cy - 0.16 * rad
                rx, ry = 0.17 * rad * esc, 0.22 * rad * esc
                d.ellipse([qx - rx, qy - ry, qx + rx, qy + ry], fill=PAPEL, outline=TINTA, width=max(2, gm // 2))


def hoja(ruta):
    W, H = 1920, 1080
    img = Image.new("RGB", (W * SS, H * SS), PAPEL)
    d = ImageDraw.Draw(img)
    f1, f2 = palitos.fuente(34 * SS), palitos.fuente(27 * SS)
    d.text((60 * SS, 30 * SS), "Rival de Tin y Tan · sin nombre en pantalla · concepto: la duda · hoja v2, borrador del 2026-11-26",
           font=f1, fill=TINTA)
    R = 31

    def rotulo(x, y, t):
        w = d.textlength(t, font=f2)
        d.text((x * SS - w / 2, y * SS), t, font=f2, fill=TINTA)

    for y in (505, 985):
        d.line([(60 * SS, (y + 6) * SS), ((W - 60) * SS, (y + 6) * SS)], fill=SOMBRA, width=7 * SS)
    fila1 = (("Frente", "parado", "frente", 1, R), ("Perfil", "parado", "perfil", 1, R), ("Espalda", "parado", "espalda", 1, R),
             ("Guardia", "guardia", "perfil", 1, R), ("Crecida (hasta 1,5 veces)", "guardia", "perfil", -1, R * 1.45))
    xs1 = (200, 470, 740, 1280, 1640)
    for (t, pose, vista, mira, r), x in zip(fila1, xs1):
        duda(img, x, 505, r, pose, vista, mira)
        rotulo(x, 518, t)
    capa = Image.new("RGBA", (400 * palitos.SS, 400 * palitos.SS), (0, 0, 0, 0))

    class C:
        pass
    c = C()
    c.img, c.d = capa, ImageDraw.Draw(capa)
    alto_tin = 5.53 * R
    palitos.dibujar(c, "tin", 200, 380, alto_tin, pose="parado", expresion="curiosidad", objeto=False)
    capa = capa.resize((400 * SS, 400 * SS), Image.LANCZOS)
    img.paste(capa, ((1010 - 200) * SS, (505 - 380) * SS), capa)
    rotulo(1010, 518, "Tin, a la misma escala")
    fila2 = (("Golpe", "golpe", 1), ("Patada", "patada", 1), ("Recibe", "recibe", 1), ("Caído", "caido", 1))
    for (t, pose, mira), x in zip(fila2, (230, 600, 960, 1310)):
        duda(img, x, 985, R, pose, "perfil", mira)
        rotulo(x, 998, t)
    duda(img, 1700, 985, R, "recibe", "perfil", 1, dibujado=0.5)
    rotulo(1700, 998, "Borrándose (empieza por la cabeza)")
    img.resize((W, H), Image.LANCZOS).save(ruta)


if __name__ == "__main__":
    hoja(sys.argv[1])
