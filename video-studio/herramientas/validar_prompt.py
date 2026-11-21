#!/usr/bin/env python3
"""Revisa un prompt de video antes de gastar un solo credito.

Uso:
    python3 validar_prompt.py <proyecto>/02_prompt/prompt.md

Falla (codigo 1) si el elenco no esta definido, si se usa un personaje que no
existe en personajes/, o si falta algun dato que el generador necesita.
Si el prompt pertenece a una serie, aplica ademas las reglas de series/<serie>/serie.md.
"""
import re
import sys
from pathlib import Path

ESTUDIO = Path(__file__).resolve().parent.parent
PERSONAJES = ESTUDIO / "personajes"
IMAGENES = {".png", ".jpg", ".jpeg", ".webp"}
METODOS_PAGADOS = ("imagen", "texto")
MAX_TOMA_S = 10
TIPOS = ("intro", "capitulo", "short", "otro")
# Formatos de salida (video-studio/formatos.md)
ASPECTO = {"capitulo": "16:9", "intro": "16:9", "short": "9:16"}
SHORT_MAX_S, SHORT_REDES_S = 180, 60


def seccion(texto, numero):
    m = re.search(rf"^## {numero}\..*?$(.*?)(?=^## \d+\.|\Z)", texto, re.M | re.S)
    return m.group(1) if m else None


def campo(bloque, etiqueta):
    m = re.search(rf"\*\*{etiqueta}:\*\*[ \t]*(.*)", bloque)
    return re.sub(r"<!--.*?-->", "", m.group(1)).strip() if m else None


def ids(texto):
    return re.findall(r"@([a-z0-9_]+)", texto or "")


def numero(texto):
    m = re.search(r"\d+(?:[.,]\d+)?", texto or "")
    return float(m.group().replace(",", ".")) if m else None


def bloque_identidad(pid):
    ficha = PERSONAJES / pid / "ficha.md"
    if not ficha.is_file():
        return None
    m = re.search(r"## Bloque de identidad.*?```text\n(.*?)```", ficha.read_text(), re.S)
    return " ".join(m.group(1).split()) if m else ""


def lista(texto):
    return [x.strip().lower() for x in (texto or "").split(",") if x.strip()]


def reglas_de_serie(ruta, ficha, elenco, tomas, total_s, errores):
    """Reglas propias de una serie (publico, elenco, ritmo, revision)."""
    nombre = (campo(ficha, "Serie") or "").strip().strip('"').lower()
    if nombre in ("", "ninguna"):
        return None
    biblia = ESTUDIO / "series" / nombre / "serie.md"
    if not biblia.is_file():
        errores.append(f"La serie '{nombre}' no existe (falta series/{nombre}/serie.md).")
        return nombre
    reglas = biblia.read_text()

    permitidos = ids(campo(reglas, "Elenco permitido"))
    for pid in elenco:
        if permitidos and pid not in permitidos:
            errores.append(f"@{pid} no puede salir en la serie '{nombre}' "
                           f"(elenco permitido: {', '.join('@' + x for x in permitidos)}).")

    objetivo = campo(ficha, "Objetivo de aprendizaje") or ""
    if not objetivo or objetivo.lower().startswith("no aplica"):
        errores.append("Falta el objetivo de aprendizaje en la ficha técnica.")

    maximo = numero(campo(reglas, "Duración máxima del episodio"))
    if maximo and total_s > maximo:
        errores.append(f"El episodio dura {total_s:g} s y la serie admite {maximo:g} s como máximo.")
    minimo = numero(campo(reglas, "Duración mínima de toma"))
    camaras = lista(campo(reglas, "Cámaras permitidas"))
    vetados = lista(campo(reglas, "Términos prohibidos en prompts"))
    for titulo, t in tomas:
        dur = numero(campo(t, "Duración"))
        if minimo and dur is not None and dur < minimo:
            errores.append(f"{titulo}: dura {dur:g} s; en esta serie ninguna toma baja de {minimo:g} s.")
        cam = (campo(t, "Cámara") or "").lower()
        if camaras and not any(cam.startswith(c) for c in camaras):
            errores.append(f"{titulo}: cámara '{cam or 'sin indicar'}' no permitida "
                           f"(usa: {', '.join(camaras)}).")
        prompts = " ".join(re.findall(r"```text\n(.*?)```", t, re.S)).lower()
        for palabra in vetados:
            if re.search(rf"\b{re.escape(palabra)}\b", prompts):
                errores.append(f"{titulo}: el prompt contiene '{palabra}', prohibido en esta serie.")

    if (campo(reglas, "Requiere revisión aprobada") or "").lower().startswith("s"):
        revision = ruta.parent / "revision.md"
        veredicto = campo(revision.read_text(), "Veredicto") if revision.is_file() else None
        if (veredicto or "").upper() != "APROBADO":
            errores.append("El guion no tiene la revisión aprobada "
                           f"({revision.name}: veredicto '{veredicto or 'no existe'}').")
    idiomas = [x.strip() for x in (campo(reglas, "Idiomas") or "").split(",") if x.strip()]
    if len(idiomas) > 1:
        voz = ruta.parent / "voz_idiomas.md"
        if not voz.is_file():
            errores.append(f"Falta voz_idiomas.md con la voz en: {', '.join(idiomas)}.")
        else:
            tabla = re.sub(r"<!--.*?-->", "", voz.read_text(), flags=re.S)
            cabecera = next((l for l in tabla.splitlines() if l.startswith("| Plano")), "")
            for idioma in idiomas:
                if f"| {idioma} " not in cabecera + " ":
                    errores.append(f"voz_idiomas.md no tiene la columna del idioma '{idioma}'.")
            if re.search(r"\[[^\]\n]*\]", tabla) or re.search(r"\|[ \t]*\|", tabla):
                errores.append("voz_idiomas.md tiene celdas vacías o sin llenar.")

    if (campo(reglas, "Requiere ficha técnica") or "").lower().startswith("s"):
        ficha_tecnica = ruta.parent / "ficha_tecnica.md"
        if not ficha_tecnica.is_file():
            errores.append("Falta la ficha técnica con la rúbrica (ficha_tecnica.md).")
        else:
            from puntuar_ficha import revisar
            fallos, _ = revisar(re.sub(r"<!--.*?-->", "", ficha_tecnica.read_text(), flags=re.S))
            errores.extend(f"Ficha técnica: {f}" for f in fallos)
    return nombre


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    ruta = Path(sys.argv[1])
    if not ruta.is_file():
        sys.exit(f"No existe: {ruta}")
    crudo = ruta.read_text()
    texto = re.sub(r"<!--.*?-->", "", crudo, flags=re.S)
    errores, avisos = [], []

    if re.search(r"\[[^\]\n]*\]", re.sub(r"\[[ xX]\]", "", texto)):
        pendientes = sorted(set(re.findall(r"\[[^\]\n]*\]", texto)))[:5]
        errores.append("Quedan campos de plantilla sin llenar: " + ", ".join(pendientes))

    for n, nombre in [(1, "Ficha técnica"), (2, "Elenco"), (4, "Estilo global"), (6, "Tomas")]:
        if seccion(texto, n) is None:
            errores.append(f"Falta la sección {n} ({nombre}).")

    tipo = (campo(seccion(texto, 1) or "", "Tipo") or "").lower().replace("í", "i")
    if tipo not in TIPOS:
        errores.append(f"Tipo '{tipo or 'sin indicar'}' no válido (usa: intro, capítulo, short u otro).")
    elif tipo in ("capitulo", "short") and numero(campo(seccion(texto, 1) or "", "Número")) is None:
        errores.append(f"Falta el número del {tipo}.")

    aspecto = (campo(seccion(texto, 1) or "", "Aspecto") or "").split(" ")[0]
    if tipo in ASPECTO and aspecto != ASPECTO[tipo]:
        errores.append(f"Un {tipo} va en {ASPECTO[tipo]} (formatos.md); el prompt dice '{aspecto or 'nada'}'.")

    # --- Elenco -----------------------------------------------------------
    elenco_txt = seccion(texto, 2) or ""
    sin_personajes = bool(re.search(r"Elenco:\s*ninguno", elenco_txt, re.I))
    elenco = list(dict.fromkeys(ids(elenco_txt)))
    if not elenco and not sin_personajes:
        errores.append("El elenco no está definido: lista los personajes como @id "
                       "o escribe 'Elenco: ninguno'.")
    if elenco and sin_personajes:
        errores.append("El elenco dice 'ninguno' pero también lista personajes.")

    identidad = {}
    for pid in elenco:
        carpeta = PERSONAJES / pid
        bloque = bloque_identidad(pid)
        if bloque is None:
            errores.append(f"@{pid} no existe en personajes/ (falta {carpeta.relative_to(ESTUDIO)}/ficha.md).")
            continue
        if not bloque or bloque == "PENDIENTE":
            errores.append(f"@{pid}: su ficha no tiene el bloque de identidad escrito.")
        else:
            identidad[pid] = bloque
        if "## Definición para generar" not in (carpeta / "ficha.md").read_text():
            errores.append(f"@{pid}: su ficha no tiene la sección «Definición para generar» "
                           "(proporciones, lista de comprobación, fallos conocidos).")
        refs = carpeta / "referencias"
        if not any(f.suffix.lower() in IMAGENES for f in refs.glob("*")) if refs.is_dir() else True:
            errores.append(f"@{pid}: no hay ninguna imagen en personajes/{pid}/referencias/.")

    # --- Tomas ------------------------------------------------------------
    tomas = re.split(r"^### ", seccion(texto, 6) or "", flags=re.M)[1:]
    if not tomas:
        errores.append("No hay ninguna toma (### Toma N — nombre).")
    usados, total_s, pagados_s, por_titulo = set(), 0.0, 0.0, []
    for t in tomas:
        titulo = t.splitlines()[0].strip()
        por_titulo.append((titulo, t))
        dur = numero(campo(t, "Duración"))
        metodo = (campo(t, "Método") or "").lower()
        quien = campo(t, "Personajes")
        if dur is None:
            errores.append(f"{titulo}: falta la duración.")
        else:
            total_s += dur
            if metodo.startswith(METODOS_PAGADOS):
                pagados_s += dur
                if dur > MAX_TOMA_S:
                    avisos.append(f"{titulo}: {dur:g} s en una sola generación; pártela en tomas de 5 s o menos.")
        if not metodo:
            errores.append(f"{titulo}: falta el método.")
        if quien is None or quien == "":
            errores.append(f"{titulo}: falta la línea de Personajes (usa @id o 'ninguno').")
            continue
        en_toma = ids(quien)
        if not en_toma and "ninguno" not in quien.lower():
            errores.append(f"{titulo}: Personajes debe llevar @id o 'ninguno' (dice: {quien}).")
        for pid in en_toma:
            usados.add(pid)
            if pid not in elenco:
                errores.append(f"{titulo}: usa @{pid}, que no está en el elenco.")
            elif pid in identidad and identidad[pid] not in " ".join(t.split()):
                avisos.append(f"{titulo}: el bloque de identidad de @{pid} no está pegado tal cual en el prompt.")
        for pid in set(ids(t)) - set(en_toma):
            errores.append(f"{titulo}: menciona @{pid} pero no está en su línea de Personajes.")
        if en_toma and metodo.startswith("texto"):
            avisos.append(f"{titulo}: lleva personajes con texto→video; usa imagen→video para que no cambien de cara.")
        if metodo.startswith(METODOS_PAGADOS) and "Prompt de video:" not in t:
            errores.append(f"{titulo}: falta el 'Prompt de video'.")
        if metodo.startswith("imagen") and "Prompt de keyframe:" not in t:
            errores.append(f"{titulo}: falta el 'Prompt de keyframe'.")
    for pid in elenco:
        if pid not in usados:
            errores.append(f"@{pid} está en el elenco pero no aparece en ninguna toma.")

    # --- Duracion y presupuesto --------------------------------------------
    ficha = seccion(texto, 1) or ""
    declarada = numero(campo(ficha, "Duración total"))
    if declarada is not None and tomas and abs(declarada - total_s) > 0.5:
        avisos.append(f"Las tomas suman {total_s:g} s y la ficha dice {declarada:g} s.")
    if tipo == "short" and total_s > SHORT_MAX_S:
        errores.append(f"Un short no puede pasar de {SHORT_MAX_S} s; este dura {total_s:g} s.")
    elif tipo == "short" and total_s > SHORT_REDES_S:
        avisos.append(f"El short dura {total_s:g} s: con más de {SHORT_REDES_S} s no se reutiliza igual en todas las redes.")
    serie = reglas_de_serie(ruta, ficha, elenco, por_titulo, total_s, errores)
    intentos = numero(campo(ficha, "Intentos estimados por toma")) or 1
    precio = numero(campo(ficha, "Precio por segundo"))

    print(f"Prompt: {ruta}")
    if serie:
        print(f"Serie: {serie}")
    print("Elenco: " + (", ".join("@" + p for p in elenco) if elenco else "ninguno"))
    print(f"Tomas: {len(tomas)} | {total_s:g} s en pantalla | {pagados_s:g} s generados (el resto es edición)")
    aprox = pagados_s * intentos
    linea = f"Presupuesto: ~{aprox:g} s de generación con {intentos:g} intentos por toma"
    if precio:
        linea += f" = ~{aprox * precio:.2f} en la moneda de tu plan"
    print(linea)
    for a in avisos:
        print(f"  AVISO  {a}")
    for e in errores:
        print(f"  ERROR  {e}")
    if errores:
        print(f"\nNO generes todavía: {len(errores)} error(es).")
        sys.exit(1)
    print("\nListo para generar.")


if __name__ == "__main__":
    main()
