#!/usr/bin/env python3
"""Miniatura 1280x720 del short 1 de Tin & Tan, dibujada con código (mismo diseño que el video).

Uso (desde la carpeta del proyecto):  python3 codigo/miniatura.py <salida.png>

Composición: texto «how many pencil turns?» arriba a la izquierda, el casete con el lápiz en el carrete en el centro y
Tan (izquierda, con espejo) y Tin (derecha) mirando la pregunta. No adelanta la respuesta (1,170). El texto se pone
aquí, en edición, no dentro de una imagen generada (protocolo del publicador).
"""
import sys
from pathlib import Path

from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
import render_v2 as R  # noqa: E402
import palitos  # noqa: E402

W, H = 1280, 720


def main():
    salida = Path(sys.argv[1]) if len(sys.argv) > 1 else R.PROY / "08_entrega" / "miniatura.png"
    lz = palitos.Lienzo(W, H)
    # suelo
    lz.d.line([(120 * palitos.SS, 660 * palitos.SS), (1160 * palitos.SS, 660 * palitos.SS)],
              fill=R.SOMBRA, width=4 * palitos.SS)
    # casete con el lápiz en el carrete izquierdo, levemente inclinado
    R.casete(lz, 0.5 * W, 0.56 * H, 0.40 * W, 30, rot=-6, lapiz="izq")
    palitos.dibujar(lz, "tan", 0.14 * W, 660, 430, pose="pregunta", expresion="curiosidad", vista="frente",
                    viento=0.4, espejo=True)
    palitos.dibujar(lz, "tin", 0.86 * W, 660, 430, pose="piensa", expresion="pensando", vista="frente", objeto=True)
    img = lz.resultado()
    segs = (R.T("how many "), R.K("pencil"), R.T(" turns?"))
    tam = 92
    tx, margen, linea = R.imagen_texto(segs, tam)
    k = 1 / palitos.SS
    chico = tx.resize((int(tx.width * k), int(tx.height * k)), Image.LANCZOS)
    x = int((W - (chico.width - 2 * margen * k)) / 2 - margen * k)
    img.paste(chico, (x, 40), chico)
    salida.parent.mkdir(parents=True, exist_ok=True)
    img.save(salida, optimize=True)
    print(f"Miniatura -> {salida} ({salida.stat().st_size / 1024:.0f} KB)")


if __name__ == "__main__":
    main()
