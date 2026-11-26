#!/usr/bin/env python3
"""Genera `video-studio/mapa/MAPA.md` a partir de `video-studio/mapa/grafo.json` (nodos y enlaces).

Es el informe que se lee primero: nodos centrales, qué depende de qué, pendientes y nodos sueltos. La idea viene de
Graphify (un grafo de conocimiento con un informe de entrada); aquí el grafo se mantiene a mano.

Uso:  python3 video-studio/herramientas/mapa.py
"""
import json
from collections import Counter, defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
PENDIENTE = ("sin ", "pendiente", "falta", "incompleta", "por validar", "en prueba", "detenido", "de relleno", "propuesta")


def main():
    g = json.loads((RAIZ / "mapa" / "grafo.json").read_text(encoding="utf-8"))
    nodos = {n["id"]: n for n in g["nodes"]}
    grado, sale, entra = Counter(), defaultdict(list), defaultdict(list)
    for e in g["links"]:
        grado[e["source"]] += 1
        grado[e["target"]] += 1
        sale[e["source"]].append(e)
        entra[e["target"]].append(e)
    L = ["# Mapa del estudio", "",
         f"> Generado por `herramientas/mapa.py` desde `mapa/grafo.json` · actualizado: {g['graph']['actualizado']} · "
         f"{len(nodos)} nodos, {len(g['links'])} relaciones.",
         "> **Léelo antes de buscar en archivos.** Para cambiarlo se edita `grafo.json` y se vuelve a generar.", "",
         "## 1. Nodos centrales (los más conectados)", "", "| Nodo | Tipo | Relaciones | Dónde está | Estado |", "|---|---|---|---|---|"]
    for i, c in grado.most_common(10):
        n = nodos[i]
        L.append(f"| {n['nombre']} | {n['tipo']} | {c} | `{n['ruta']}` | {n['estado']} |" if n["ruta"] else
                 f"| {n['nombre']} | {n['tipo']} | {c} | — | {n['estado']} |")
    L += ["", "## 2. La cadena de trabajo", ""]
    for i in ("motor", "m_generador", "m_personajes", "m_produccion"):
        n = nodos[i]
        L.append(f"- **{n['nombre']}** (`{n['ruta']}`): " + "; ".join(f"{e['verbo']} {nodos[e['target']]['nombre']}" for e in sale[i]) + ".")
    L += ["", "## 3. Pendientes (nodos cuyo estado lo dice)", "", "| Nodo | Estado | De qué depende |", "|---|---|---|"]
    for n in g["nodes"]:
        if any(p in n["estado"].lower() for p in PENDIENTE):
            dep = "; ".join(f"{e['verbo']} {nodos[e['target']]['nombre']}" for e in sale[n["id"]]) or "—"
            L.append(f"| {n['nombre']} | {n['estado']} | {dep} |")
    L += ["", "## 4. Por tipo", ""]
    por = defaultdict(list)
    for n in g["nodes"]:
        por[n["tipo"]].append(n)
    for t in sorted(por):
        L.append(f"- **{t}:** " + "; ".join(f"{n['nombre']}" + (f" (`{n['ruta']}`)" if n["ruta"] else "") for n in por[t]))
    sueltos = [n["nombre"] for n in g["nodes"] if grado[n["id"]] == 0]
    hip = [e for e in g["links"] if e.get("certeza") != "hecho"]
    L += ["", "## 5. Sueltos e hipótesis", "",
          "- Nodos sin ninguna relación: " + (", ".join(sueltos) if sueltos else "ninguno") + ".",
          "- Relaciones que son hipótesis, no hechos: " + ("; ".join(f"{nodos[e['source']]['nombre']} {e['verbo']} {nodos[e['target']]['nombre']}" for e in hip) if hip else "ninguna") + ".", ""]
    (RAIZ / "mapa" / "MAPA.md").write_text("\n".join(L), encoding="utf-8")
    print("mapa/MAPA.md:", len(nodos), "nodos,", len(g["links"]), "relaciones")


if __name__ == "__main__":
    main()
