#!/usr/bin/env python3
"""Revisa un video ya generado y marca sus fotogramas "muertos", sin gastar creditos.

Uso:
    python3 revisar_fotogramas.py <video> <carpeta_salida> [--serie granja]

Busca: imagen congelada, fotogramas vacios, destellos (accesibilidad: no mas de
3 por segundo), cortes mas seguidos de lo que admite la serie y tramos largos
sin ningun cambio. Escribe revision.md, revision.json y una hoja de contacto con
los momentos marcados. No decide si el video sirve: senala donde mirar.
"""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

import numpy as np

ESTUDIO = Path(__file__).resolve().parent.parent
FPS = 10            # fotogramas por segundo que se analizan
ANCHO, ALTO = 96, 54
CONGELADO = 0.35    # diferencia media (0-255) por debajo de la cual no hay movimiento
CONGELADO_S = 1.0   # segundos seguidos sin movimiento para marcarlo
VACIO = 6.0         # desviacion tipica por debajo de la cual el fotograma es plano
DESTELLO = 40.0     # salto de luminancia media entre fotogramas seguidos
CORTE = 28.0        # diferencia media que se toma como corte
MAX_DESTELLOS_S = 3


def leer(video):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-i", str(video),
                        "-vf", f"fps={FPS},scale={ANCHO}:{ALTO},format=gray", "-f", "rawvideo", "-"],
                       capture_output=True)
    if r.returncode != 0 or not r.stdout:
        sys.exit(f"No se pudo leer el video: {r.stderr.decode()[:300]}")
    return np.frombuffer(r.stdout, dtype=np.uint8).reshape(-1, ALTO, ANCHO).astype(np.float32)


def tramos(mascara, minimo):
    """Tramos consecutivos verdaderos de al menos `minimo` fotogramas -> [(inicio_s, fin_s)]."""
    out, ini = [], None
    for i, v in enumerate(list(mascara) + [False]):
        if v and ini is None:
            ini = i
        elif not v and ini is not None:
            if i - ini >= minimo:
                out.append((round(ini / FPS, 1), round(i / FPS, 1)))
            ini = None
    return out


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("video")
    p.add_argument("salida")
    p.add_argument("--serie", help="aplica la duración mínima de toma de series/<serie>/serie.md")
    a = p.parse_args()
    video, out = Path(a.video), Path(a.salida)
    if not video.is_file():
        sys.exit(f"No existe: {video}")
    out.mkdir(parents=True, exist_ok=True)

    f = leer(video)
    dur = len(f) / FPS
    dif = np.abs(np.diff(f, axis=0)).mean(axis=(1, 2))          # movimiento entre fotogramas
    luz = f.mean(axis=(1, 2))
    salto = np.abs(np.diff(luz))

    congelados = tramos(dif < CONGELADO, int(CONGELADO_S * FPS))
    vacios = tramos(f.std(axis=(1, 2)) < VACIO, 1)
    cortes = [round((i + 1) / FPS, 1) for i in np.where(dif > CORTE)[0]]
    cortes = [c for i, c in enumerate(cortes) if i == 0 or c - cortes[i - 1] > 0.25]
    destellos = [round((i + 1) / FPS, 1) for i in np.where(salto > DESTELLO)[0]]
    por_segundo = {}
    for d in destellos:
        por_segundo[int(d)] = por_segundo.get(int(d), 0) + 1
    exceso = sorted(s for s, n in por_segundo.items() if n > MAX_DESTELLOS_S)

    minimo = None
    if a.serie:
        biblia = ESTUDIO / "series" / a.serie / "serie.md"
        m = re.search(r"\*\*Duración mínima de toma:\*\*\s*(\d+)", biblia.read_text()) if biblia.is_file() else None
        minimo = int(m.group(1)) if m else None
    limites = [0.0] + cortes + [round(dur, 1)]
    planos = [(limites[i], limites[i + 1]) for i in range(len(limites) - 1)]
    cortos = [pl for pl in planos if minimo and pl[1] - pl[0] < minimo]

    marcas = []
    marcas += [("Imagen congelada", f"{i}–{j} s", i) for i, j in congelados]
    marcas += [("Fotograma vacío", f"{i}–{j} s", i) for i, j in vacios]
    marcas += [("Más de 3 destellos en un segundo", f"segundo {s}", float(s)) for s in exceso]
    marcas += [("Plano más corto que el mínimo de la serie", f"{i}–{j} s", i) for i, j in cortos]

    datos = {"video": video.name, "duracion_s": round(dur, 1), "cortes_s": cortes,
             "planos": len(planos), "plano_mas_corto_s": round(min(j - i for i, j in planos), 1),
             "congelados": congelados, "vacios": vacios, "destellos_s": destellos,
             "segundos_con_exceso_de_destellos": exceso,
             "marcas": [{"tipo": t, "donde": d} for t, d, _ in marcas]}
    (out / "revision.json").write_text(json.dumps(datos, indent=2, ensure_ascii=False) + "\n")

    hoja = None
    if marcas:
        momentos = sorted({m[2] for m in marcas})[:12]
        sel = "+".join(f"eq(n\\,{int(t * FPS)})" for t in momentos)
        hoja = out / "marcados.jpg"
        subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(video), "-vf",
                        f"fps={FPS},select='{sel}',scale=320:-2,tile=4x3:padding=6:margin=6:color=white",
                        "-frames:v", "1", "-q:v", "4", str(hoja)])

    lineas = [f"# Revisión de fotogramas — {video.name}", "",
              f"- Duración: {dur:.1f} s · planos detectados: {len(planos)} · plano más corto: {datos['plano_mas_corto_s']} s",
              f"- Cortes en: {', '.join(str(c) for c in cortes) or 'ninguno'}", ""]
    if marcas:
        lineas += ["| Qué | Dónde |", "|---|---|"] + [f"| {t} | {d} |" for t, d, _ in marcas]
        lineas += ["", f"Fotogramas marcados: `{hoja.name}` (en el orden de la tabla, por tiempo)." if hoja and hoja.exists() else ""]
    else:
        lineas.append("Sin marcas: no hay imagen congelada, fotogramas vacíos ni destellos de más.")
    lineas += ["", "Esto señala dónde mirar; no reemplaza la rúbrica (`ficha_tecnica.md`) ni la revisión del equipo.",
               "Una marca no autoriza a regenerar: se informa al dueño (`video-studio/generacion.md`)."]
    (out / "revision.md").write_text("\n".join(lineas) + "\n")
    print("\n".join(lineas[2:4 + len(marcas) + 3]))


if __name__ == "__main__":
    main()
