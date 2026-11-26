#!/usr/bin/env python3
"""Exporta las cabezas de Tin, Tan y el rival (diseño oficial, `palitos.py` y `duda_v2.py`) como PNG transparentes para
la escena 3D, una carpeta por paleta. Las cabezas miran a la derecha; la escena las refleja.
Uso: python3 personajes/exportar_sprites.py sprites            (lee todas las paletas de paletas/*.json)"""
import json
import math
import sys
from pathlib import Path

from PIL import Image, ImageDraw

AQUI = Path(__file__).resolve()
sys.path.insert(0, str(AQUI.parents[2] / "herramientas"))
sys.path.insert(0, str(AQUI.parents[2] / "canales/nostalgia-tin-y-tan/pruebas/2026-11-26_pelea_con_la_duda"))
import palitos  # noqa: E402
import duda_v2  # noqa: E402

SS = palitos.SS
RAD, LADO = 112, 512                      # radio de cabeza en px y lado del sprite; el centro de la cabeza es el centro


class Capa:
    def __init__(self, lado):
        self.img = Image.new("RGBA", (lado * SS, lado * SS), (0, 0, 0, 0))
        self.d = ImageDraw.Draw(self.img)


def exportar(out, pal):
    """pal: la paleta (dict). `personajes` puede cambiar colores de palitos (p. ej. la línea de tinta en fondos oscuros)."""
    original = dict(palitos.PALETA)
    palitos.PALETA.update(pal.get("personajes", {}))
    linea, papel = pal["colores"]["rival"], pal["colores"]["fondo"]
    out.mkdir(parents=True, exist_ok=True)
    for pid in ("tin", "tan"):
        for ex in ("curiosidad", "sorpresa", "eureka", "risa", "concentrado"):
            c = Capa(LADO)
            if pid == "tan":                                   # la bufanda es de Tan siempre: va con la cabeza
                pl = palitos.Pluma(c, LADO / 2, LADO / 2, RAD)
                palitos.bufanda(pl, "perfil", 1, palitos.CUELLO + 0.95, 0.0)
            palitos.cabeza(c, pid, LADO / 2, LADO / 2, RAD, ex, "perfil", 1)
            c.img.resize((LADO, LADO), Image.LANCZOS).save(out / f"{pid}_{ex}.png")
    rad, lado = 150, 640                                        # rival: madeja de radio 150 px, centro en el centro
    for h in range(4):
        img = Image.new("RGBA", (lado * 3, lado * 3), (0, 0, 0, 0))
        d = ImageDraw.Draw(img)
        cx = cy = lado * 3 / 2
        r = rad * 3
        g = int(0.11 * r)
        pts = duda_v2.madeja(h * 0.9)
        d.line([(cx + p[0] * r, cy + p[1] * r) for p in pts], fill=linea, width=g, joint="curve")
        riz = []
        for i in range(40):
            a = math.radians(-200 + i * 7.2)
            riz.append((cx + 0.34 * math.cos(a) * r, cy + (-1.42 + 0.3 * math.sin(a)) * r))
        riz += [(cx + 0.02 * r, cy + (-1.1 + 0.02 * j) * r) for j in range(8)]
        d.line(riz, fill=linea, width=g, joint="curve")
        for i, ox in enumerate((0.12, 0.6)):
            e = 0.8 if i == 0 else 1.0
            qx, qy = cx + ox * r, cy - 0.16 * r
            d.ellipse([qx - 0.17 * r * e, qy - 0.22 * r * e, qx + 0.17 * r * e, qy + 0.22 * r * e], fill=papel,
                      outline=linea, width=g // 2)
        img.resize((lado, lado), Image.LANCZOS).save(out / f"duda_{h}.png")
    palitos.PALETA.clear()
    palitos.PALETA.update(original)


def main():
    out = Path(sys.argv[1])
    for f in sorted((AQUI.parents[1] / "paletas").glob("*.json")):
        pal = json.loads(f.read_text(encoding="utf-8"))
        exportar(out / pal["id"], pal)
        print("sprites de", pal["id"])


if __name__ == "__main__":
    main()
