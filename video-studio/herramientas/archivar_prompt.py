#!/usr/bin/env python3
"""Guarda un prompt validado en la carpeta de su personaje, ordenado por tipo.

Uso:
    python3 archivar_prompt.py <proyecto>/02_prompt/prompt.md
    python3 archivar_prompt.py --indice        (solo rehace los indices)

El prompt va a personajes/<protagonista>/prompts/<tipo>/, donde el protagonista
es el primer personaje del elenco. Cada personaje que sale en el video lo ve en
su propio personajes/<id>/prompts/INDICE.md.
"""
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

ESTUDIO = Path(__file__).resolve().parent.parent
PERSONAJES = ESTUDIO / "personajes"
# tipo -> (carpeta, prefijo del archivo, titulo en el indice)
TIPOS = {
    "intro": ("intro", "intro", "Intro"),
    "capitulo": ("capitulos", "cap", "Capítulos"),
    "short": ("shorts", "short", "Shorts"),
    "otro": ("otros", "otro", "Otros"),
}


def plano(texto):
    return unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode().lower()


def slug(texto):
    return re.sub(r"[^a-z0-9]+", "_", plano(texto)).strip("_")


def campo(texto, etiqueta):
    m = re.search(rf"\*\*{etiqueta}:\*\*[ \t]*(.*)", texto)
    return m.group(1).strip() if m else ""


def leer(ruta):
    texto = ruta.read_text()
    elenco = re.search(r"^## 2\..*?$(.*?)(?=^## \d+\.|\Z)", texto, re.M | re.S)
    titulo = re.search(r"^# (?:Prompt de video — )?(.*)", texto, re.M)
    numero = re.search(r"\d+", campo(texto, "Número"))
    serie = slug(campo(texto, "Serie"))
    return {
        "titulo": titulo.group(1).strip() if titulo else ruta.stem,
        "tipo": plano(campo(texto, "Tipo")),
        "numero": int(numero.group()) if numero else None,
        "serie": "" if serie in ("", "ninguna") else serie,
        "duracion": campo(texto, "Duración total"),
        "objetivo": campo(texto, "Objetivo de aprendizaje"),
        "elenco": list(dict.fromkeys(re.findall(r"@([a-z0-9_]+)", elenco.group(1) if elenco else ""))),
    }


def rehacer_indices():
    """Un INDICE.md por personaje con todos los prompts donde aparece."""
    todos = []
    for ruta in sorted(PERSONAJES.glob("*/prompts/*/*.md")):
        todos.append((ruta, leer(ruta)))
    for carpeta in sorted(p for p in PERSONAJES.iterdir() if p.is_dir() and not p.name.startswith("_")):
        pid = carpeta.name
        lineas = [f"# Prompts de @{pid}", "",
                  "Índice generado por `herramientas/archivar_prompt.py`; no se edita a mano.", ""]
        for tipo, (_, _, encabezado) in TIPOS.items():
            filas = [(r, d) for r, d in todos if d["tipo"] == tipo and pid in d["elenco"]]
            lineas += [f"## {encabezado}", ""]
            if not filas:
                lineas += ["_Ninguno todavía._", ""]
                continue
            lineas += ["| # | Título | Serie | Duración | Con | Archivo |", "|---|---|---|---|---|---|"]
            for r, d in sorted(filas, key=lambda x: (x[1]["serie"], x[1]["numero"] or 0, x[0].name)):
                otros = ", ".join(f"@{x}" for x in d["elenco"] if x != pid) or "—"
                enlace = Path("..") / ".." / r.relative_to(PERSONAJES)
                lineas.append(f"| {d['numero'] or '—'} | {d['titulo']} | {d['serie'] or '—'} | "
                              f"{d['duracion'] or '—'} | {otros} | [{r.name}]({enlace.as_posix()}) |")
            lineas.append("")
        (carpeta / "prompts").mkdir(exist_ok=True)
        (carpeta / "prompts" / "INDICE.md").write_text("\n".join(lineas))
    return len(todos)


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    if sys.argv[1] == "--indice":
        print(f"Índices rehechos ({rehacer_indices()} prompts).")
        return
    origen = Path(sys.argv[1])
    if origen.is_dir():
        origen = origen / "02_prompt" / "prompt.md"
    if not origen.is_file():
        sys.exit(f"No existe: {origen}")

    r = subprocess.run([sys.executable, str(Path(__file__).with_name("validar_prompt.py")), str(origen)],
                       capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(r.stdout + "\nNo se archiva un prompt que no pasa el validador.")

    d = leer(origen)
    if not d["elenco"]:
        sys.exit("El prompt no tiene personajes: no hay carpeta de personaje donde guardarlo.")
    carpeta, prefijo, _ = TIPOS[d["tipo"]]
    partes = [d["serie"], prefijo + (f"{d['numero']:02d}" if d["numero"] else ""), slug(d["titulo"])]
    destino = PERSONAJES / d["elenco"][0] / "prompts" / carpeta / ("_".join(p for p in partes if p) + ".md")
    destino.parent.mkdir(parents=True, exist_ok=True)
    try:
        fuente = origen.resolve().parent.parent.relative_to(ESTUDIO).as_posix()
    except ValueError:
        fuente = origen.parent.parent.name
    nota = f"<!-- Copia archivada. Se edita en {fuente}/02_prompt/prompt.md y se vuelve a archivar. -->\n"
    destino.write_text(nota + origen.read_text())
    rehacer_indices()
    print(f"Archivado: {destino.relative_to(ESTUDIO)}")
    print("Aparece en el índice de: " + ", ".join(f"@{p}" for p in d["elenco"]))


if __name__ == "__main__":
    main()
