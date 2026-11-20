#!/usr/bin/env python3
"""Calcula cuanto cumplio un video generado los objetivos de su ficha tecnica.

Uso:
    python3 puntuar_ficha.py <proyecto>/02_prompt/ficha_tecnica.md

Lee los puntajes (0, 1 o 2) que el equipo anoto en cada criterio, calcula el
cumplimiento por profesion y total, y escribe la seccion "Resultado".
Con la ficha aun sin puntajes, solo comprueba que este bien armada.
"""
import re
import sys
from pathlib import Path

SECCIONES = ["Pedagogía", "Método Montessori", "Psicología infantil", "Aprendizaje interactivo", "Producción"]
APROBADO = 80  # % minimo para dar el video por bueno


def criterios(texto, seccion):
    m = re.search(rf"^## {seccion}\s*$(.*?)(?=^## |\Z)", texto, re.M | re.S)
    if not m:
        return None
    filas = []
    for linea in m.group(1).splitlines():
        c = [x.strip() for x in linea.strip().strip("|").split("|")]
        if len(c) != 8 or c[0] in ("#", "") or set(c[0]) <= set("-: "):
            continue
        filas.append({"id": c[0], "objetivo": c[1], "indicador": c[2], "peso": c[4],
                      "critico": c[5].lower().startswith("s"), "puntaje": c[6], "evidencia": c[7]})
    return filas


def revisar(texto):
    """Devuelve (errores, datos) sin modificar nada."""
    errores, datos = [], {}
    for s in SECCIONES:
        filas = criterios(texto, s)
        if filas is None:
            errores.append(f"Falta la sección «{s}».")
            continue
        if not filas:
            errores.append(f"«{s}» no tiene ningún criterio.")
        for f in filas:
            if "[" in f["objetivo"] + f["indicador"] or not f["objetivo"] or not f["indicador"]:
                errores.append(f"{f['id']}: objetivo o indicador sin llenar.")
            if f["peso"] not in ("1", "2", "3"):
                errores.append(f"{f['id']}: el peso debe ser 1, 2 o 3.")
            if f["puntaje"] not in ("", "0", "1", "2"):
                errores.append(f"{f['id']}: el puntaje debe ser 0, 1 o 2.")
            if f["puntaje"] and not f["evidencia"]:
                errores.append(f"{f['id']}: tiene puntaje pero no evidencia.")
        datos[s] = filas
    return errores, datos


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    ruta = Path(sys.argv[1])
    if not ruta.is_file():
        sys.exit(f"No existe: {ruta}")
    texto = re.sub(r"<!--.*?-->", "", ruta.read_text(), flags=re.S)
    errores, datos = revisar(texto)
    todos = [f for filas in datos.values() for f in filas]
    if errores:
        sys.exit("\n".join(f"  ERROR  {e}" for e in errores))
    puntuados = [f for f in todos if f["puntaje"]]
    if not puntuados:
        print(f"Ficha bien armada: {len(todos)} criterios, {sum(f['critico'] for f in todos)} críticos. Sin evaluar todavía.")
        return
    if len(puntuados) < len(todos):
        faltan = ", ".join(f["id"] for f in todos if not f["puntaje"])
        sys.exit(f"  ERROR  Faltan puntajes en: {faltan}")

    def pct(filas):
        return round(100 * sum(int(f["puntaje"]) * int(f["peso"]) for f in filas)
                     / sum(2 * int(f["peso"]) for f in filas))

    total = pct(todos)
    fallos = [f for f in todos if f["critico"] and f["puntaje"] != "2"]
    if fallos:
        estado = "NO PUBLICAR"
    elif total >= APROBADO:
        estado = "CUMPLE"
    else:
        estado = "REHACER"
    lineas = ["## Resultado", "", f"- **Cumplimiento total:** {total} %", f"- **Veredicto:** {estado}", "",
              "| Disciplina | Criterios | Cumplimiento |", "|---|---|---|"]
    lineas += [f"| {s} | {len(datos[s])} | {pct(datos[s])} % |" for s in SECCIONES]
    lineas.append("")
    if fallos:
        lineas.append("Criterios críticos sin cumplir del todo: " + ", ".join(f["id"] for f in fallos) + ".")
    flojos = [f for f in todos if f["puntaje"] != "2" and not f["critico"]]
    if flojos:
        lineas.append("A corregir en la siguiente versión: " + ", ".join(f["id"] for f in flojos) + ".")
    lineas.append("")
    lineas.append(f"Regla: «CUMPLE» con {APROBADO} % o más y todos los críticos en 2. "
                  "Un crítico por debajo de 2 es «NO PUBLICAR» aunque el total sea alto.")
    original = ruta.read_text()
    nuevo = re.sub(r"^## Resultado.*\Z", "\n".join(lineas) + "\n", original, flags=re.M | re.S)
    nuevo = re.sub(r"(\*\*Estado:\*\*) .*", rf"\1 {estado} ({total} %)", nuevo, count=1)
    ruta.write_text(nuevo)
    print("\n".join(lineas[2:]))


if __name__ == "__main__":
    main()
