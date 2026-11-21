#!/usr/bin/env python3
"""Identidad visual del canal «Tin & Tan» en YouTube, dibujada con código (0 créditos).

Uso:  python3 video-studio/canales/nostalgia-tin-y-tan/marca/marca.py <carpeta_salida>

Genera:
- perfil.png        800x800   foto de perfil (YouTube la muestra en círculo: todo va dentro del círculo central)
- banner.png        2560x1440 imagen del banner (lo importante va en la zona segura central de 1546x423)
- marca_de_agua.png 150x150   marca de agua de los videos (fondo transparente)
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw

RAIZ = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(RAIZ / "herramientas"))
sys.path.insert(0, str(RAIZ / "proyectos" / "2026-11-21_tin_y_tan_casete_y_lapiz" / "codigo"))
import palitos  # noqa: E402
from palitos import PALETA, SS, Lienzo  # noqa: E402
import render_v2 as R  # noqa: E402  (casete y textos del short 1: mismo dibujo)


def texto(img, segs, tam, x, y, centrado=False):
    t, margen, _ = R.imagen_texto(segs, tam)
    k = 1 / SS
    chico = t.resize((int(t.width * k), int(t.height * k)), Image.LANCZOS)
    ancho = chico.width - 2 * margen * k
    x0 = int((x - ancho / 2) - margen * k) if centrado else int(x - margen * k)
    img.paste(chico, (x0, int(y)), chico)


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
    lz = Lienzo(W, H)
    d = lz.d
    # franja de cinta de casete que cruza el banner (motivo del canal), fuera y dentro de la zona segura
    y0, y1 = 560, 880
    d.rectangle([0, 1040 * SS, W * SS, 1100 * SS], fill=PALETA["marron"])
    for x in range(0, W, 120):
        d.line([(x * SS, 1040 * SS), (x * SS, 1100 * SS)], fill=PALETA["tinta"], width=4 * SS)
    # zona segura: 1546x423 centrada → x 507–2053, y 508–931
    palitos.dibujar(lz, "tan", 720, 1040, 520, pose="saluda", expresion="feliz", viento=0.4, espejo=True)
    palitos.dibujar(lz, "tin", 1840, 1040, 520, pose="saluda", expresion="eureka")
    R.casete(lz, 1280, 1000, 240, 25, rot=-4, lapiz="izq")      # sobre la cinta, fuera de la zona segura (adorno)
    img = lz.resultado()
    # título y lema dentro de la zona segura (y 508–931), centrados
    texto(img, (R.T("tin "), R.K("&"), R.T(" tan")), 170, 1280, 560, centrado=True)
    texto(img, (R.T("she remembers. he does the "), R.K("math"), R.T(".")), 60, 1280, 790, centrado=True)
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
    perfil(salida / "perfil.png")
    banner(salida / "banner.png")
    marca_de_agua(salida / "marca_de_agua.png")
    for n in ("perfil.png", "banner.png", "marca_de_agua.png"):
        p = salida / n
        print(f"{n}: {Image.open(p).size} · {p.stat().st_size / 1024:.0f} KB")


if __name__ == "__main__":
    main()
