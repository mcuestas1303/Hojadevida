#!/usr/bin/env python3
"""Une los clips aprobados en un solo video, sin costo.

Uso:
    python3 ensamblar.py <proyecto> [--ancho 1080 --alto 1920 --fps 30] [--musica archivo]

Toma los videos de <proyecto>/04_clips/seleccionados/ en orden alfabetico
(nombralos toma_01.mp4, toma_02.mp4, ...) y escribe <proyecto>/06_final/final.mp4.
"""
import argparse
import subprocess
import sys
from pathlib import Path

VIDEOS = {".mp4", ".mov", ".webm", ".mkv"}


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("proyecto")
    p.add_argument("--ancho", type=int, default=1080)
    p.add_argument("--alto", type=int, default=1920)
    p.add_argument("--fps", type=int, default=30)
    p.add_argument("--musica", help="pista que reemplaza el audio de los clips")
    a = p.parse_args()

    proyecto = Path(a.proyecto)
    clips = sorted(f for f in (proyecto / "04_clips" / "seleccionados").glob("*") if f.suffix.lower() in VIDEOS)
    if not clips:
        sys.exit("No hay clips en 04_clips/seleccionados/.")
    salida = proyecto / "06_final" / "final.mp4"
    salida.parent.mkdir(exist_ok=True)

    cmd = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y"]
    for c in clips:
        cmd += ["-i", str(c)]
    # Todos los clips al mismo lienzo: se escalan sin deformar y se rellena con negro.
    filtros = [(f"[{i}:v]scale={a.ancho}:{a.alto}:force_original_aspect_ratio=decrease,"
                f"pad={a.ancho}:{a.alto}:(ow-iw)/2:(oh-ih)/2,setsar=1,fps={a.fps},format=yuv420p[v{i}]")
               for i in range(len(clips))]
    filtros.append("".join(f"[v{i}]" for i in range(len(clips))) + f"concat=n={len(clips)}:v=1:a=0[v]")
    cmd += ["-filter_complex", ";".join(filtros), "-map", "[v]"]
    if a.musica:
        cmd[-4:-4] = ["-i", a.musica]
        cmd += ["-map", f"{len(clips)}:a", "-shortest", "-c:a", "aac", "-b:a", "160k"]
    cmd += ["-c:v", "libx264", "-crf", "18", "-preset", "medium", "-movflags", "+faststart", str(salida)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f"ffmpeg falló:\n{r.stderr}")
    print(f"{len(clips)} clips -> {salida}" + ("" if a.musica else "  (sin audio: pasa --musica o añade la voz en edición)"))


if __name__ == "__main__":
    main()
