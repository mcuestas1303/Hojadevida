#!/usr/bin/env python3
"""Control de color del estudio: mide el color de una imagen o un video ya terminados (gratis).

Regla del dueño (2026-11-21): cada video lleva su decisión de color, y esa decisión se explica por el objetivo.
Este script no decide nada: mide, para que el director de fotografía y el supervisor comparen lo medido con lo que
se decidió en `02_prompt/direccion.md` (sección «Color con intención»). Manual: `manual/13_color_con_intencion.md`.

Uso:
  revisar_color.py <imagen|video> [--paleta DESIGN.md|"#hex,#hex,..."] [--por-segundo 1]
  revisar_color.py --contraste "#2B2420" "#F3E9D2"          # contraste de texto sobre fondo (WCAG)

Qué mide:
  - colores dominantes (k-medias en Lab) con su porcentaje del cuadro
  - cuánto del cuadro está dentro de la paleta declarada (ΔE76 < 12) → «fuera de paleta» si baja del 85 %
  - temperatura (cálidos frente a fríos), saturación y luminosidad medias
  - en video: cuánto varía la luminosidad y la saturación entre segundos (saltos de color entre planos)
Avisos fijos: fondo saturado que compite con el personaje, contraste bajo para público mayor, paleta fuera de lo
declarado. El contraste de texto usa la fórmula de WCAG 2.x (4,5:1 mínimo; 7:1 recomendado para 45+).
"""
import argparse
import re
import subprocess
import sys
import tempfile
from pathlib import Path

import numpy as np
from PIL import Image

VIDEO = {".mp4", ".mov", ".webm", ".mkv"}


# ---------- color ----------
def hex_rgb(h):
    h = h.strip().lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def _lin(c):
    c = c / 255.0
    return np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)


def rgb_lab(rgb):
    """rgb: array (...,3) 0–255 → Lab (D65)."""
    r, g, b = [_lin(np.asarray(rgb, dtype=float)[..., i]) for i in range(3)]
    x = (0.4124 * r + 0.3576 * g + 0.1805 * b) / 0.95047
    y = 0.2126 * r + 0.7152 * g + 0.0722 * b
    z = (0.0193 * r + 0.1192 * g + 0.9505 * b) / 1.08883
    f = lambda t: np.where(t > 0.008856, np.cbrt(t), 7.787 * t + 16 / 116)  # noqa: E731
    fx, fy, fz = f(x), f(y), f(z)
    return np.stack([116 * fy - 16, 500 * (fx - fy), 200 * (fy - fz)], axis=-1)


def luminancia(rgb):
    r, g, b = [_lin(np.asarray(rgb, dtype=float)[..., i]) for i in range(3)]
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contraste(a, b):
    la, lb = sorted((float(luminancia(np.array(hex_rgb(a)))), float(luminancia(np.array(hex_rgb(b))))), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def paleta_de(arg):
    if not arg:
        return []
    p = Path(arg)
    texto = p.read_text(encoding="utf-8") if p.exists() else arg
    return list(dict.fromkeys(re.findall(r"#[0-9A-Fa-f]{6}", texto)))


# ---------- lectura ----------
def cuadros(ruta, por_segundo):
    if ruta.suffix.lower() not in VIDEO:
        return [Image.open(ruta).convert("RGB")]
    tmp = Path(tempfile.mkdtemp())
    subprocess.run(["ffmpeg", "-v", "error", "-i", str(ruta), "-vf", f"fps={por_segundo},scale=320:-1",
                    str(tmp / "c_%04d.png")], check=True)
    return [Image.open(f).convert("RGB") for f in sorted(tmp.glob("c_*.png"))]


def pixeles(img, lado=160):
    img = img.copy()
    img.thumbnail((lado, lado))
    return np.asarray(img, dtype=float).reshape(-1, 3)


def kmedias(lab, k=6, vueltas=12, semilla=0):
    rng = np.random.default_rng(semilla)
    centros = lab[rng.choice(len(lab), k, replace=False)]
    for _ in range(vueltas):
        d = ((lab[:, None, :] - centros[None]) ** 2).sum(-1)
        et = d.argmin(1)
        centros = np.array([lab[et == i].mean(0) if (et == i).any() else centros[i] for i in range(k)])
    return et, centros


def hsv(px):
    mx, mn = px.max(1), px.min(1)
    sat = np.where(mx > 0, (mx - mn) / np.maximum(mx, 1), 0)
    r, g, b = px[:, 0], px[:, 1], px[:, 2]
    tono = np.degrees(np.arctan2(np.sqrt(3) * (g - b), 2 * r - g - b)) % 360
    return tono, sat, mx / 255


# ---------- informe ----------
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("archivo", nargs="?", type=Path)
    ap.add_argument("--paleta", help="DESIGN.md del canal o lista de #hex separados por coma")
    ap.add_argument("--por-segundo", type=float, default=1.0)
    ap.add_argument("--contraste", nargs=2, metavar=("TEXTO", "FONDO"))
    a = ap.parse_args()

    if a.contraste:
        c = contraste(*a.contraste)
        nivel = "PASA 7:1 (recomendado para 45+)" if c >= 7 else ("PASA 4,5:1 (mínimo WCAG)" if c >= 4.5
                                                                  else "NO PASA (menos de 4,5:1)")
        print(f"Contraste {a.contraste[0]} sobre {a.contraste[1]}: {c:.1f}:1 → {nivel}")
        sys.exit(0 if c >= 4.5 else 1)
    if not a.archivo or not a.archivo.exists():
        sys.exit("Falta el archivo (imagen o video).")

    imgs = cuadros(a.archivo, a.por_segundo)
    todos = np.concatenate([pixeles(i) for i in imgs])
    lab = rgb_lab(todos)
    et, centros = kmedias(lab)
    tono, sat, val = hsv(todos)
    calidos = ((tono < 70) | (tono > 330)) & (sat > 0.15)
    frios = (tono > 160) & (tono < 290) & (sat > 0.15)

    print(f"Color · {a.archivo.name} · {len(imgs)} cuadro(s)")
    print("Dominantes:")
    orden = np.argsort(-np.bincount(et, minlength=len(centros)))
    for i in orden:
        parte = (et == i).mean()
        rgb = todos[et == i].mean(0) if (et == i).any() else np.zeros(3)
        print(f"  #{''.join(f'{int(v):02X}' for v in rgb)}  {parte * 100:5.1f} %")
    print(f"Saturación media ≈ {sat.mean() * 100:.0f} % · luminosidad media ≈ {val.mean() * 100:.0f} %")
    print(f"Cálidos ≈ {calidos.mean() * 100:.0f} % · fríos ≈ {frios.mean() * 100:.0f} % del cuadro")

    avisos = []
    pal = paleta_de(a.paleta)
    if pal:
        pal_lab = rgb_lab(np.array([hex_rgb(h) for h in pal]))
        de = np.sqrt(((lab[:, None, :] - pal_lab[None]) ** 2).sum(-1)).min(1)
        dentro = (de < 12).mean()
        print(f"Dentro de la paleta declarada ({len(pal)} colores): ≈ {dentro * 100:.0f} %")
        if dentro < 0.85:
            avisos.append(f"solo ≈ {dentro * 100:.0f} % del cuadro está en la paleta: revisar qué color entró y por qué")
    fondo = centros[orden[0]]
    croma_fondo = float(np.hypot(fondo[1], fondo[2]))
    if croma_fondo > 45:
        avisos.append("el color dominante (fondo) está muy saturado: puede competir con el personaje (cap. 03)")
    if len(imgs) > 1:
        lum = np.array([pixeles(i).mean() / 255 for i in imgs])
        sats = np.array([hsv(pixeles(i))[1].mean() for i in imgs])
        saltos = np.abs(np.diff(lum))
        print(f"Entre segundos: luminosidad varía ±{lum.std() * 100:.0f} %, saturación ±{sats.std() * 100:.0f} %")
        for s in np.where(saltos > 0.15)[0]:
            avisos.append(f"salto de luminosidad de ≈ {saltos[s] * 100:.0f} % entre el segundo {s / a.por_segundo:.0f}"
                          f" y el {(s + 1) / a.por_segundo:.0f}: ¿es intencional (giro) o un plano que no iguala?")
    for x in avisos:
        print(f"  AVISO  {x}")
    print("Comparar con la sección «Color con intención» de la dirección: lo medido tiene que contar lo decidido.")


if __name__ == "__main__":
    main()
