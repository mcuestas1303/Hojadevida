#!/usr/bin/env python3
"""Identidad visual del canal «Tin & Tan» en YouTube, dibujada con código (0 créditos).

Uso:  python3 video-studio/canales/nostalgia-tin-y-tan/marca/marca.py [carpeta_salida]

Genera:
- perfil.png        800x800   foto de perfil (YouTube la muestra en círculo: todo va dentro del círculo central)
- banner.png        2560x1440 imagen del banner (lo importante va en la zona segura central de 1546x423)
- marca_de_agua.png 150x150   marca de agua de los videos (fondo transparente)

Versión 2 (2026-11-24), por el cambio de parámetros del canal (`../PARAMETROS.md`): el banner ya no dice
«she remembers. he does the math.» ni lleva el casete (el canal dejó de definirse por la nostalgia). Lema nuevo:
«she asks. he does the math.» (Tan pregunta; Tin cuenta: cierto con cualquier tema). Motivo neutro: una pregunta que
se vuelve cifra («?» → 1 2 3) sobre una regla. Sombras de contacto de `herramientas/efectos.py` (DESIGN.md,
«Profundidad y efectos»). La foto de perfil y la marca de agua NO cambian: son solo las dos cabezas.
Ya no importa código del short 1: los textos salen de `efectos.py` (dígitos `ss01`, contorno de 0,045 em).
Las versiones del 2026-11-21 están en `anterior_2026-11-21/`.
"""
import sys
from pathlib import Path

from PIL import Image

RAIZ = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(RAIZ / "herramientas"))
import efectos as E  # noqa: E402
import palitos  # noqa: E402
from palitos import PALETA, SS, Lienzo  # noqa: E402

LEMA = (E.T("she asks. he does the "), E.K("math"), E.T("."))     # minúsculas: estilo del canal; sin nombres propios
NOMBRE = (E.T("Tin "), E.K("&"), E.T(" Tan"))                       # nombres propios con mayúscula (regla del dueño)
SEGURA = (507, 508, 2053, 931)                                      # zona segura del banner: 1546x423 centrada


def texto(img, segs, tam, x, y, centrado=False):
    """Pega `segs` con el tope del cuerpo en `y`. Devuelve la caja (x0, y0, x1, y1) que ocupa el texto."""
    t, margen, _ = E.imagen_texto(segs, tam)
    k = 1 / SS
    chico = t.resize((int(t.width * k), int(t.height * k)), Image.LANCZOS)
    ancho = chico.width - 2 * margen * k
    x0 = int((x - ancho / 2) - margen * k) if centrado else int(x - margen * k)
    img.paste(chico, (x0, int(y)), chico)
    caja = chico.getbbox()
    return (x0 + caja[0], int(y) + caja[1], x0 + caja[2], int(y) + caja[3])


def sombra(lz, x, y, ancho, opacidad=0.30):
    """Sombra de contacto centrada en (x, y), pegada en el lienzo antes de dibujar lo que se apoya."""
    s = E.sombra_contacto(ancho * SS, opacidad=opacidad)
    lz.img.paste(s, (int(x * SS - s.width / 2), int(y * SS - s.height / 2)), s)


def ficha(lz, cx, base, lado, relleno="blanco"):
    """Ficha de contador (cuadro redondeado) apoyada en `base`."""
    d = lz.d
    caja = [(cx - lado / 2) * SS, (base - lado) * SS, (cx + lado / 2) * SS, base * SS]
    d.rounded_rectangle(caja, radius=int(lado * 0.16 * SS), fill=PALETA[relleno], outline=PALETA["tinta"],
                        width=int(lado * 0.055 * SS))


def flecha(lz, x0, x1, y, grosor=10):
    d = lz.d
    d.line([(x0 * SS, y * SS), (x1 * SS, y * SS)], fill=PALETA["tinta"], width=grosor * SS)
    p = 26
    d.line([((x1 - p) * SS, (y - p) * SS), (x1 * SS, y * SS), ((x1 - p) * SS, (y + p) * SS)], fill=PALETA["tinta"],
           width=grosor * SS, joint="curve")
    r = grosor / 2
    for px, py in ((x0, y), (x1, y), (x1 - p, y - p), (x1 - p, y + p)):
        d.ellipse([(px - r) * SS, (py - r) * SS, (px + r) * SS, (py + r) * SS], fill=PALETA["tinta"])


def perfil(ruta):
    W = 800
    lz = Lienzo(W, W)
    # las dos cabezas, juntas y grandes, dentro del círculo central (radio 400)
    palitos.cabeza(lz, "tan", 285, 430, 165, expresion="feliz", espejo=True)
    palitos.cabeza(lz, "tin", 515, 450, 165, expresion="feliz")
    img = lz.resultado()
    img.save(ruta, optimize=True)


def banner(ruta):
    W, H = 2560, 1440
    suelo = 1040
    lz = Lienzo(W, H)
    d = lz.d
    # regla de medir que cruza el banner (motivo neutro: aquí se cuenta), fuera de la zona segura
    d.rectangle([0, suelo * SS, W * SS, (suelo + 64) * SS], fill=PALETA["papel_sombra"])
    d.line([(0, suelo * SS), (W * SS, suelo * SS)], fill=PALETA["tinta"], width=5 * SS)
    for i, x in enumerate(range(40, W, 40)):
        largo = 34 if i % 5 == 4 else 18
        d.line([(x * SS, suelo * SS), (x * SS, (suelo + largo) * SS)], fill=PALETA["tinta"], width=3 * SS)
    # la pregunta que se vuelve cifra: «?» → 1 2 3 (fichas de contador apoyadas en la regla; adorno)
    lado, paso = 104, 118
    fichas = [(1016, "?", "mostaza"), (1280, "1", "blanco"), (1280 + paso, "2", "blanco"), (1280 + 2 * paso, "3", "blanco")]
    for cx, _, relleno in fichas:
        sombra(lz, cx, suelo + 4, lado * 1.25, 0.26)
    sombra(lz, 720, suelo + 4, 250)
    sombra(lz, 1840, suelo + 4, 250)
    for cx, _, relleno in fichas:
        ficha(lz, cx, suelo - 3, lado, relleno)
    flecha(lz, 1016 + lado / 2 + 26, 1280 - lado / 2 - 26, suelo - 3 - lado / 2)
    # zona segura: 1546x423 centrada → x 507–2053, y 508–931
    palitos.dibujar(lz, "tan", 720, suelo, 520, pose="pregunta", expresion="curiosidad", viento=0.4, espejo=True)
    palitos.dibujar(lz, "tin", 1840, suelo, 520, pose="saluda", expresion="eureka")
    img = lz.resultado()
    for cx, s, _ in fichas:
        texto(img, (E.T(s),), 78, cx, suelo - 3 - lado + 6, centrado=True)
    # nombre y lema dentro de la zona segura (y 508–931), centrados
    cajas = [texto(img, NOMBRE, 170, 1280, 548, centrado=True), texto(img, LEMA, 60, 1280, 778, centrado=True)]
    for c in cajas:
        assert SEGURA[0] <= c[0] and c[2] <= SEGURA[2] and SEGURA[1] <= c[1] and c[3] <= SEGURA[3], \
            f"texto fuera de la zona segura: {c}"
    img.save(ruta, optimize=True)


def marca_de_agua(ruta):
    W = 150
    lz = Lienzo(W, W)
    palitos.cabeza(lz, "tan", 52, 80, 38, expresion="feliz", espejo=True)
    palitos.cabeza(lz, "tin", 99, 84, 38, expresion="feliz")
    img = lz.resultado().convert("RGBA")
    # papel transparente: se quita el fondo crema exacto
    datos = [(r, g, b, 0) if (r, g, b) == Image.new("RGB", (1, 1), PALETA["papel"]).getpixel((0, 0)) else (r, g, b, a)
             for r, g, b, a in list(img.getdata())]
    img.putdata(datos)
    img.save(ruta, optimize=True)


def main():
    salida = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent
    salida.mkdir(parents=True, exist_ok=True)
    E.comprobar_glifos(["".join(s for s, _ in NOMBRE + LEMA), "?123"])
    perfil(salida / "perfil.png")
    banner(salida / "banner.png")
    marca_de_agua(salida / "marca_de_agua.png")
    for n in ("perfil.png", "banner.png", "marca_de_agua.png"):
        p = salida / n
        print(f"{n}: {Image.open(p).size} · {p.stat().st_size / 1024:.0f} KB")


if __name__ == "__main__":
    main()
