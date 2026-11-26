#!/usr/bin/env python3
"""Hojas de contacto de una carpeta de fotogramas: python3 hojas.py <carpeta> <prefijo> <salida> [columnas] [ancho]"""
import glob, sys
from PIL import Image, ImageDraw
carp, pref, sal = sys.argv[1:4]
cols = int(sys.argv[4]) if len(sys.argv) > 4 else 6
aw = int(sys.argv[5]) if len(sys.argv) > 5 else 320
fs = sorted(glob.glob(f"{carp}/{pref}*.jpg")); ah = aw * 16 // 9; filas = 3
for k in range(0, len(fs), cols * filas):
    lote = fs[k:k + cols * filas]
    h = Image.new("RGB", (cols * aw, filas * ah), "white")
    for i, f in enumerate(lote):
        im = Image.open(f).resize((aw, ah)); d = ImageDraw.Draw(im); d.rectangle([0, 0, 58, 16], fill="white"); d.text((4, 2), f[-8:-4], fill="red"); h.paste(im, ((i % cols) * aw, (i // cols) * ah))
    h.save(f"{sal}_{k // (cols * filas):02d}.jpg", quality=86)
print(len(fs), "fotogramas")
