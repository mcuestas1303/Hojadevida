#!/usr/bin/env python3
"""Crea la carpeta de un video nuevo a partir de la plantilla.

Uso:
    python3 nuevo_proyecto.py <nombre> [video_de_referencia] [--serie <serie> | --redes]

Si se pasa un video de referencia, lo copia a 01_referencia/ y lo analiza.
Con --serie, el proyecto nace como episodio de video-studio/series/<serie>/ y
recibe la ficha pedagogica, el guion y la revision que llena el equipo creativo.
Con --redes, usa la plantilla de prompt para redes (gancho, ritmo, texto y sonido);
no se combina con una serie infantil.
"""
import datetime
import re
import shutil
import subprocess
import sys
import unicodedata
from pathlib import Path

ESTUDIO = Path(__file__).resolve().parent.parent


def main():
    redes = "--redes" in sys.argv
    if redes:
        sys.argv.remove("--redes")
    serie = None
    if "--serie" in sys.argv:
        i = sys.argv.index("--serie")
        if i + 1 >= len(sys.argv):
            sys.exit(__doc__)
        serie = sys.argv[i + 1].lower()
        del sys.argv[i:i + 2]
        if not (ESTUDIO / "series" / serie / "serie.md").is_file():
            sys.exit(f"No existe la serie: series/{serie}/serie.md")
    if len(sys.argv) not in (2, 3):
        sys.exit(__doc__)
    limpio = unicodedata.normalize("NFKD", sys.argv[1]).encode("ascii", "ignore").decode()
    slug = re.sub(r"[^a-z0-9]+", "_", limpio.lower()).strip("_")
    if not slug:
        sys.exit("El nombre no tiene letras ni números.")
    destino = ESTUDIO / "proyectos" / f"{datetime.date.today():%Y-%m-%d}_{slug}"
    if destino.exists():
        sys.exit(f"Ya existe: {destino}")
    shutil.copytree(ESTUDIO / "plantillas" / "proyecto", destino)
    if redes and serie:
        shutil.rmtree(destino)
        sys.exit("--redes no se combina con --serie: el ritmo de redes no es para series infantiles.")
    if redes:
        shutil.copy2(ESTUDIO / "plantillas" / "prompt_video_redes.md", destino / "02_prompt" / "prompt.md")
    if serie:
        guion = destino / "02_prompt"
        for nombre in ("ficha_pedagogica", "guion", "revision", "ficha_tecnica", "publicacion", "voz_idiomas"):
            shutil.copy2(ESTUDIO / "infantil" / f"plantilla_{nombre}.md", guion / f"{nombre}.md")
        prompt = guion / "prompt.md"
        prompt.write_text(prompt.read_text().replace(
            '[nombre de la serie en video-studio/series/, o "ninguna"]', serie))
        brief = destino / "00_brief.md"
        brief.write_text(brief.read_text().replace("- **Título:**", f"- **Serie:** {serie}\n- **Título:**"))
    print(f"Proyecto creado: {destino}")
    if len(sys.argv) == 3:
        ref = Path(sys.argv[2])
        if not ref.is_file():
            sys.exit(f"No existe el video de referencia: {ref}")
        copia = destino / "01_referencia" / f"referencia{ref.suffix.lower()}"
        shutil.copy2(ref, copia)
        subprocess.run([sys.executable, str(Path(__file__).with_name("analizar_video.py")),
                        str(copia), str(destino / "01_referencia" / "analisis")], check=True)


if __name__ == "__main__":
    main()
