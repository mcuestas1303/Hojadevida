#!/usr/bin/env python3
"""Prueba técnica (0 créditos): Tin y Tan pelean contra «la Duda», 6 s, 1080x1920, 30 f/s.

No toca `herramientas/palitos.py`: usa `dibujar` tal como está (versión 1.4) y resuelve lo que le falta al código
(inclinar el cuerpo, agacharse, saltar) dibujando cada figura en una capa propia que se gira alrededor de los pies.
La Duda se dibuja aquí; si el dueño aprueba la ficha, pasa a `palitos.py` por la solicitud de cambio.

Uso:  python3 prueba_pelea.py <carpeta_salida>      # fotogramas PNG, hoja del personaje y hojas de contacto
"""
import math
import sys
from pathlib import Path

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "herramientas"))
import palitos  # noqa: E402

palitos.SS = 2                      # la prueba usa supermuestreo 2 (el render final usa 3)
SS = palitos.SS
W, H, FPS, N = 1080, 1920, 30, 180
PAPEL, TINTA, MOSTAZA, SOMBRA = (palitos.PALETA[k] for k in ("papel", "tinta", "mostaza", "papel_sombra"))
SUELO, ALTO = 1420, 520
R = ALTO / (2 + palitos.CUELLO + palitos.TORSO + palitos.MUSLO + palitos.PIERNA + 0.25)


def clamp(u):
    return max(0.0, min(1.0, u))


def eio(u):
    u = clamp(u)
    return u * u * (3 - 2 * u)


def eo(u):
    u = clamp(u)
    return 1 - (1 - u) ** 3


def tramo(f, a, b):
    return clamp((f - a) / float(b - a))


class Capa:
    def __init__(self, w, h):
        self.img = Image.new("RGBA", (w * SS, h * SS), (0, 0, 0, 0))
        self.d = ImageDraw.Draw(self.img)


# ------------------------------------------------------------------ poses de combate (dict, como admite palitos 1.4)
GUARDIA = {"bi": (28, 200), "bd": (42, 196), "pi": (16, 2), "pd": (20, 6)}       # puños arriba, cerca de la cara
CARGA = {"bi": (30, 120), "bd": (-30, 100), "pi": (22, 4), "pd": (14, 2)}          # anticipación: el brazo va atrás
GOLPE = {"bi": (35, 140), "bd": (92, 90), "pi": (26, 8), "pd": (4, -6)}            # brazo recto al frente
AGACHADA = {"bi": (70, 160), "bd": (70, 160), "pi": (58, -28), "pd": (58, -28)}
RECIBE = {"bi": (110, 150), "bd": (60, 30), "pi": (4, -10), "pd": (30, 12)}
PATADA = {"bi": (60, 150), "bd": (-40, -20), "pi": (20, -40), "pd": (88, 86)}      # pierna recta al frente
SALTO = {"bi": (120, 150), "bd": (120, 150), "pi": (40, -30), "pd": (40, -30)}


def encogimiento(pose):
    """Cuánto suben los pies (px) al doblar las piernas: se baja el cuerpo esa medida para que sigan en el suelo."""
    ps = pose if isinstance(pose, dict) else palitos.POSES[pose]
    lleno = palitos.MUSLO + palitos.PIERNA
    bajo = max(palitos.MUSLO * math.cos(math.radians(ps[k][0])) + palitos.PIERNA * math.cos(math.radians(ps[k][1]))
               for k in ("pi", "pd"))
    return (lleno - bajo) * R


def figura(base, pid, x, pose, expresion, espejo, inclina=0.0, sube=0.0, objeto=False, pegado=True):
    """Dibuja a Tin o Tan en una capa y la gira `inclina` grados alrededor de los pies. sube: px sobre el suelo."""
    lw, lh, pie = 1000, 1000, 820
    capa = Capa(lw, lh)
    baja = encogimiento(pose) if pegado else 0.0
    palitos.dibujar(capa, pid, lw / 2, pie + baja, ALTO, pose=pose, expresion=expresion, espejo=espejo, objeto=objeto)
    img = capa.img
    if inclina:
        img = img.rotate(inclina, resample=Image.BICUBIC, center=(lw / 2 * SS, pie * SS))
    img = img.resize((lw, lh), Image.LANCZOS)
    base.alpha_composite(img, (int(round(x - lw / 2)), int(round(SUELO - pie - sube))))


# ------------------------------------------------------------------ la Duda
def trazo_duda(escala, hervor):
    """Madeja de tinta: una sola línea que se enreda. Devuelve puntos en unidades de la Duda (radio ≈ 1)."""
    pts = []
    n = 520
    for i in range(n):
        t = i / (n - 1) * 2 * math.pi
        x = 0.62 * math.sin(7 * t + 0.4 + 0.05 * hervor) + 0.34 * math.sin(11 * t + 1.3) + 0.06 * math.sin(29 * t + hervor)
        y = 0.58 * math.cos(5 * t + 0.9) + 0.36 * math.cos(13 * t + 0.2 + 0.05 * hervor) + 0.06 * math.cos(31 * t - hervor)
        pts.append((x * escala, y * 0.92 * escala))
    return pts


def gancho(escala):
    """El rizo de arriba: la curva de un signo de pregunta, sin el punto. Es lo único que la nombra."""
    pts = []
    for i in range(40):
        a = math.radians(-200 + i * 7.2)
        pts.append((0.34 * math.cos(a) * escala, (-1.42 + 0.3 * math.sin(a)) * escala))
    pts += [(0.02 * escala, (-1.1 + 0.02 * j) * escala) for j in range(8)]
    return pts


def duda(base, cx, cy, radio, f, dibujado=1.0, aplasta=1.0, brazo=None, ojos=True, resto=False):
    """dibujado: 0 a 1, cuánto de la madeja está trazado (aparece dibujándose y se va borrándose).
    aplasta: >1 la ensancha y la achata (reacción al golpe). brazo: (angulo_grados, largo) del zarpazo, o None."""
    lw = lh = int(radio * 4.4)
    capa = Capa(lw, lh)
    d, c = capa.d, lw / 2 * SS
    hervor = (f // 3) * 0.9                                       # el trazo «hierve» cada 3 fotogramas
    g = max(2, int(0.085 * radio * SS))

    def px(p):
        return (c + p[0] * radio * SS * aplasta, c + p[1] * radio * SS / aplasta)

    pts = trazo_duda(1.0, hervor)
    k = max(2, int(len(pts) * clamp(dibujado)))
    if resto:
        pts, k = pts[:60], 60
    d.line([px(p) for p in pts[:k]], fill=TINTA, width=g, joint="curve")
    if dibujado > 0.85 and not resto:
        d.line([px(p) for p in gancho(1.0)], fill=TINTA, width=g, joint="curve")
        if ojos:                                                  # dos huecos de papel: mira, pero no tiene cara
            for sx in (-0.3, 0.3):
                q = px((sx, -0.18))
                rx, ry = 0.17 * radio * SS, 0.21 * radio * SS / aplasta
                d.ellipse([q[0] - rx, q[1] - ry, q[0] + rx, q[1] + ry], fill=PAPEL, outline=TINTA, width=max(2, g // 2))
    if brazo and not resto:
        ang, largo = brazo
        a = math.radians(ang)
        arm = []
        for i in range(24):
            u = i / 23
            rr = 0.7 + largo * u
            onda = 0.1 * math.sin(u * 9 + hervor) * (1 - u)
            arm.append(((rr * math.cos(a) - onda * math.sin(a)), (rr * math.sin(a) + onda * math.cos(a))))
        d.line([px(p) for p in arm], fill=TINTA, width=g, joint="curve")
        q = px(arm[-1])
        d.ellipse([q[0] - g * 1.6, q[1] - g * 1.6, q[0] + g * 1.6, q[1] + g * 1.6], fill=TINTA)
    img = capa.img.resize((lw, lh), Image.LANCZOS)
    base.alpha_composite(img, (int(round(cx - lw / 2)), int(round(cy - lh / 2))))


# ------------------------------------------------------------------ impactos
def estrella(base, cx, cy, radio, giro=0.0):
    capa = Capa(int(radio * 3), int(radio * 3))
    c = radio * 1.5 * SS
    pts = []
    for i in range(16):
        r = (radio if i % 2 == 0 else radio * 0.48) * SS
        a = math.radians(giro + i * 22.5)
        pts.append((c + r * math.cos(a), c + r * math.sin(a)))
    capa.d.polygon(pts, fill=MOSTAZA, outline=TINTA, width=max(2, int(0.07 * radio * SS)))
    img = capa.img.resize((int(radio * 3), int(radio * 3)), Image.LANCZOS)
    base.alpha_composite(img, (int(cx - radio * 1.5), int(cy - radio * 1.5)))


def gotas(base, cx, cy, p, direccion, semilla=0):
    """Tinta que salpica: 5 gotas del color del trazo que salen del punto de contacto y caen. p de 0 a 1."""
    d = ImageDraw.Draw(base)
    for i in range(5):
        a = math.radians(direccion + (i - 2) * 24 + semilla * 7)
        v = 150 + 40 * ((i * 37 + semilla) % 5)
        x = cx + math.cos(a) * v * p
        y = cy + math.sin(a) * v * p + 260 * p * p
        r = (11 - i) * (1 - 0.6 * p)
        d.ellipse([x - r, y - r, x + r, y + r], fill=TINTA)


def lineas_de_velocidad(base, x0, y, largo, hacia):
    d = ImageDraw.Draw(base)
    for i in range(4):
        yy = y - 60 + i * 40
        d.line([(x0, yy), (x0 - hacia * (largo - i * 18), yy)], fill=TINTA, width=5)


# ------------------------------------------------------------------ guion de la prueba (fotograma → estado)
X_TAN, X_TIN, DX, DY = 165, 905, 540, SUELO - 265   # la Duda, a la altura de ellos, en el centro
GOLPE_1, GOLPE_2 = 72, 142                     # fotogramas de contacto
PAUSA = 3                                      # pausa de impacto (fotogramas que se sostienen)


def cuadro(f):
    base = Image.new("RGBA", (W, H), PAPEL)
    d = ImageDraw.Draw(base)
    d.line([(60, SUELO + 8), (W - 60, SUELO + 8)], fill=SOMBRA, width=10)

    # --- la Duda: tamaño, trazado, zarpazo
    radio, dib, apl, brazo, resto = 230.0, 1.0, 1.0, None, False
    cy = DY + 10 * math.sin(f / 9.0)
    if f < 30:                                                     # aparece dibujándose
        dib = eio(f / 28.0)
    if 30 <= f < 56:                                               # zarpazo a Tan: anticipación 8 f y barrido
        u = tramo(f, 30, 38)
        v = tramo(f, 38, 46)
        w = tramo(f, 46, 56)
        ang = 215 + 40 * eio(u) - 62 * eo(v) + 22 * eio(w)         # sube (255), barre a la altura de la cabeza de Tan (193) y vuelve
        brazo = (ang, 0.35 + 0.75 * eo(v) - 0.7 * eio(w))
    if f >= GOLPE_1:                                               # primer dato: se achata y se encoge
        u = tramo(f, GOLPE_1, GOLPE_1 + 14)
        apl = 1.0 + 0.28 * math.sin(math.pi * clamp(u * 1.4)) * (1 - u)
        radio = 230 - 60 * eo(u)
    if 92 <= f < 118:                                              # contraataca: se hincha y empuja a Tin
        u = tramo(f, 92, 100)
        v = tramo(f, 100, 106)
        w = tramo(f, 106, 118)
        radio = 170 + 45 * eio(u) - 15 * eio(w)
        brazo = (-40 + 42 * eo(v) - 10 * eio(w), 0.3 + 0.75 * eo(v) - 0.7 * eio(w))
    if 118 <= f < GOLPE_2:
        radio = 200.0
    if f >= GOLPE_2:                                               # segundo dato: se borra
        u = tramo(f, GOLPE_2 + PAUSA, GOLPE_2 + 24)
        radio = 200 - 40 * eo(u)
        apl = 1.0 + 0.3 * (1 - u) * math.sin(math.pi * clamp(u * 2))
        dib = 1.0 - eio(u)
        if dib < 0.14:
            resto = True                                           # queda un pedazo: lo que no está confirmado
    duda(base, DX, cy, radio, f, dibujado=dib, aplasta=apl, brazo=brazo, ojos=f < GOLPE_2 + PAUSA, resto=resto)

    # --- Tan (izquierda del cuadro; gesticula hacia el centro)
    pose, expr, incl, sube, x = GUARDIA, "curiosidad", 0.0, 0.0, X_TAN
    if f < 30:
        pose, expr = palitos.pose_entre("parado", GUARDIA, eio(tramo(f, 14, 28))), "sorpresa"
    if 38 <= f < 60:                                               # se agacha bajo el zarpazo
        u = eo(tramo(f, 38, 44)) - eio(tramo(f, 52, 60))
        pose, expr = palitos.pose_entre(GUARDIA, AGACHADA, u), "sorpresa"
    if 118 <= f < 160:                                             # salto y patada
        u = tramo(f, 118, 126)                                     # anticipación: se agacha
        v = tramo(f, 126, GOLPE_2)                                 # vuelo
        w = tramo(f, GOLPE_2 + PAUSA, 160)                         # cae
        if f < 126:
            pose = palitos.pose_entre(GUARDIA, AGACHADA, eio(u))
        elif f < GOLPE_2 + PAUSA:
            pose = palitos.pose_entre(SALTO, PATADA, eo(tramo(f, 132, GOLPE_2 - 2)))
            x = X_TAN + 120 * eo(v)
            sube = 150 * math.sin(math.pi * 0.62 * clamp(v))
            incl = -16 * eo(v)
            expr = "eureka"
        else:
            pose = palitos.pose_entre(PATADA, GUARDIA, eio(w))
            x = X_TAN + 120 - 120 * eio(w)
            sube = 150 * math.sin(math.pi * 0.62) * (1 - eio(tramo(f, GOLPE_2 + PAUSA, GOLPE_2 + 11)))
            incl = -16 * (1 - eio(w))
            expr = "eureka"
    if f >= 160:
        pose, expr = palitos.pose_entre(GUARDIA, "celebra", eo(tramo(f, 160, 170))), "risa"
    pegado = not (126 <= f < GOLPE_2 + 11)
    figura(base, "tan", x, pose, expr, espejo=False, inclina=incl, sube=sube, pegado=pegado)

    # --- Tin (derecha del cuadro; gesticula hacia el centro, por eso va con espejo)
    pose, expr, incl, sube, x = GUARDIA, "curiosidad", 0.0, 0.0, X_TIN
    if f < 30:
        pose, expr = palitos.pose_entre("parado", GUARDIA, eio(tramo(f, 16, 28))), "sorpresa"
    if 56 <= f < 92:                                               # carga, golpe recto, pausa y vuelta
        u = tramo(f, 56, 64)
        v = tramo(f, 64, GOLPE_1)
        w = tramo(f, GOLPE_1 + PAUSA, 92)
        if f < 64:
            pose, incl, x = palitos.pose_entre(GUARDIA, CARGA, eio(u)), -9 * eio(u), X_TIN + 30 * eio(u)
        elif f < GOLPE_1 + PAUSA:
            pose, incl, x = palitos.pose_entre(CARGA, GOLPE, eo(v)), -9 + 27 * eo(v), X_TIN + 30 - 115 * eo(v)
            expr = "eureka"
        else:
            pose, incl, x = palitos.pose_entre(GOLPE, GUARDIA, eio(w)), 18 * (1 - eio(w)), X_TIN - 85 + 85 * eio(w)
            expr = "eureka"
    if 100 <= f < 126:                                             # recibe el empujón y resbala
        v = tramo(f, 100, 108)
        w = tramo(f, 112, 126)
        pose = palitos.pose_entre(GUARDIA, RECIBE, eo(v) - eio(w))
        incl, x, expr = -12 * (eo(v) - eio(w)), X_TIN + 28 * eo(v) - 28 * eio(w), "sorpresa"
    if f >= 160:
        pose, expr = palitos.pose_entre(GUARDIA, "celebra", eo(tramo(f, 162, 172))), "risa"
    figura(base, "tin", x, pose, expr, espejo=True, inclina=incl, sube=sube, objeto=False)

    # --- impactos: un solo efecto por golpe (estrella + gotas breves); la sacudida, solo en el golpe final
    for g, (ex, ey, dire) in ((GOLPE_1, (DX + 190, SUELO - 255, 200)), (GOLPE_2, (DX - 185, SUELO - 300, -20))):
        if g <= f < g + 5:
            estrella(base, ex, ey, 86 + 10 * (f - g), giro=(f - g) * 9)
        if g + 1 <= f < g + 9:
            gotas(base, ex, ey, (f - g - 1) / 8.0, dire, semilla=g)
    if 66 <= f < GOLPE_1:
        lineas_de_velocidad(base, X_TIN + 60, SUELO - 300, 110, -1)
    if 134 <= f < GOLPE_2:
        lineas_de_velocidad(base, X_TAN - 40, SUELO - 380, 110, 1)

    img = base.convert("RGB")
    if GOLPE_2 + PAUSA <= f < GOLPE_2 + PAUSA + 8:                 # sacudida ≤ 16 px y ≤ 8 f (manual 14, sección 6)
        k = f - GOLPE_2 - PAUSA
        amp = 16 * (1 - k / 8.0)
        dx, dy = int(amp * math.cos(k * 2.4)), int(amp * math.sin(k * 3.1))
        lienzo = Image.new("RGB", (W, H), PAPEL)
        lienzo.paste(img, (dx, dy))
        img = lienzo
    return img


def tiempo_real(f):
    """Pausa de impacto: durante PAUSA fotogramas después de cada contacto se repite el fotograma del golpe."""
    for g in (GOLPE_1, GOLPE_2):
        if g <= f < g + PAUSA:
            return g
    return f


def hoja_personaje(ruta):
    base = Image.new("RGBA", (1920, 1080), PAPEL)
    d = ImageDraw.Draw(base)
    f = palitos.fuente(40)
    d.line([(60, 930), (1860, 930)], fill=SOMBRA, width=8)
    duda(base, 300, 560, 200, 0)
    figura_ref = Capa(600, 700)
    palitos.dibujar(figura_ref, "tin", 300, 640, ALTO, pose="parado", expresion="curiosidad", objeto=False)
    base.alpha_composite(figura_ref.img.resize((600, 700), Image.LANCZOS), (360, 290))
    duda(base, 980, 700, 120, 3, aplasta=1.25)
    duda(base, 1310, 660, 125, 6, brazo=(200, 0.8))
    duda(base, 1590, 690, 120, 9, dibujado=0.45, ojos=False)
    duda(base, 1800, 720, 110, 12, resto=True)
    f = palitos.fuente(32)
    for x, t in ((300, "Entera"), (660, "Tin, para la escala"), (980, "Golpeada"), (1310, "Zarpazo"),
                 (1590, "Borrándose"), (1800, "Resto")):
        w = d.textlength(t, font=f)
        d.text((x - w / 2, 965), t, font=f, fill=TINTA)
    d.text((60, 40), "Personaje sin nombre en pantalla · concepto: la duda · borrador del 2026-11-26", font=f, fill=TINTA)
    base.convert("RGB").save(ruta)


def main():
    salida = Path(sys.argv[1])
    (salida / "fotogramas").mkdir(parents=True, exist_ok=True)
    hoja_personaje(salida / "hoja_personaje_borrador.png")
    for f in range(N):
        cuadro(tiempo_real(f)).save(salida / "fotogramas" / f"f_{f:04d}.png")
    for n, ini in enumerate((0, 60, 120)):                         # hojas de contacto a 5 f/s (cada 6 fotogramas)
        hoja = Image.new("RGB", (5 * 270, 2 * 480), PAPEL)
        for i in range(10):
            im = Image.open(salida / "fotogramas" / f"f_{ini + i * 6:04d}.png").resize((270, 480), Image.LANCZOS)
            hoja.paste(im, ((i % 5) * 270, (i // 5) * 480))
        hoja.save(salida / f"contacto_{n + 1}.png")


if __name__ == "__main__":
    main()
