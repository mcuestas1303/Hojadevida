#!/usr/bin/env python3
"""Muestra en que punto del manual esta cada personaje, serie y proyecto.

Uso:
    python3 estado.py

No cambia nada. Sirve para saber que falta antes de pedir un prompt o de generar.
"""
import re
from pathlib import Path

ESTUDIO = Path(__file__).resolve().parent.parent
IMAGENES = {".png", ".jpg", ".jpeg", ".webp"}


def marca(ok):
    return "[x]" if ok else "[ ]"


def campo(texto, etiqueta):
    m = re.search(rf"\*\*{etiqueta}:\*\*[ \t]*(.*)", texto)
    return m.group(1).strip() if m else ""


def sin_plantilla(ruta):
    return ruta.is_file() and not re.search(r"\[[^\]\n]*\]", re.sub(r"<!--.*?-->|\[[ xX]\]|\]\(", "", ruta.read_text(), flags=re.S))


def main():
    print("PERSONAJES (manual, fase 1)")
    for c in sorted(p for p in (ESTUDIO / "personajes").iterdir() if p.is_dir() and not p.name.startswith("_")):
        f = (c / "ficha.md").read_text() if (c / "ficha.md").is_file() else ""
        bloque = re.search(r"## Bloque de identidad.*?```text\n(.*?)```", f, re.S)
        refs = [x for x in (c / "referencias").glob("*") if x.suffix.lower() in IMAGENES] if (c / "referencias").is_dir() else []
        prompts = [x for x in c.glob("prompts/*/*.md") if not x.name.endswith(("_ficha.md", "_voz.md"))]
        print(f"  @{c.name}")
        print(f"    {marca(bool(bloque) and bloque.group(1).strip() not in ('', 'PENDIENTE'))} bloque de identidad")
        print(f"    {marca('## Definición para generar' in f and '(medidas contra' not in f)} definición para generar")
        print(f"    {marca(bool(refs))} imagen aprobada en referencias/ ({len(refs)})")
        print(f"    prompts archivados: {len(prompts)}")

    print("\nSERIES (manual, fase 2)")
    for c in sorted(p for p in (ESTUDIO / "series").iterdir() if p.is_dir()):
        print(f"  {c.name}")
        for nombre in ("serie.md", "entorno.md", "temario.md"):
            print(f"    {marca(sin_plantilla(c / nombre))} {nombre} completo")
        refs = [x for x in (c / "referencias").glob("*") if x.suffix.lower() in IMAGENES] if (c / "referencias").is_dir() else []
        print(f"    {marca(bool(refs))} imagen de referencia del lugar ({len(refs)})")

    print("\nPROYECTOS (manual, fases 3 a 9)")
    for c in sorted(p for p in (ESTUDIO / "proyectos").iterdir() if p.is_dir()):
        g = c / "02_prompt"
        rev = campo((g / "revision.md").read_text(), "Veredicto") if (g / "revision.md").is_file() else "—"
        kf = [x for x in (c / "03_keyframes").glob("*") if x.suffix.lower() in IMAGENES]
        clips = [x for x in (c / "04_clips" / "seleccionados").glob("*.mp4")]
        ft = campo((g / "ficha_tecnica.md").read_text(), "Estado") if (g / "ficha_tecnica.md").is_file() else "—"
        dk = campo((c / "03_keyframes" / "definicion.md").read_text(), "Estado") if (c / "03_keyframes" / "definicion.md").is_file() else "—"
        dc = campo((c / "04_clips" / "definicion.md").read_text(), "Estado") if (c / "04_clips" / "definicion.md").is_file() else "—"
        print(f"  {c.name}")
        print(f"    {marca(sin_plantilla(c / '00_brief.md'))} brief")
        for nombre in ("ficha_pedagogica.md", "guion.md", "voz_idiomas.md", "publicacion.md", "prompt.md"):
            if (g / nombre).is_file():
                print(f"    {marca(sin_plantilla(g / nombre))} {nombre}")
        print(f"    revisión del guion: {rev}")
        print(f"    keyframes: {len(kf)} · definición de keyframes: {dk}")
        print(f"    clips aprobados: {len(clips)} · definición de clips: {dc}")
        print(f"    {marca((c / '06_final').is_dir() and any((c / '06_final').glob('*.mp4')))} video final")
        print(f"    rúbrica: {ft}")

    cambios = sorted((ESTUDIO / "cambios").glob("*.md"))
    abiertos = [x.name for x in cambios if "APLICADA" not in campo(x.read_text(), "Estado") and "DESCARTADA" not in campo(x.read_text(), "Estado")]
    print(f"\nSOLICITUDES DE CAMBIO: {len(cambios)} en total; abiertas: {', '.join(abiertos) or 'ninguna'}")


if __name__ == "__main__":
    main()
