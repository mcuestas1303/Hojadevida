"""Convierte la respuesta de la extensión (prompt 02, y 03 si hubo) en una lista de verificación de oferta en Excel.

Uso:
  python3 compras-publicas/scripts/checklist.py compras-publicas/procesos/<CÓDIGO>/respuesta.md \\
      [--salida compras-publicas/procesos/<CÓDIGO>/checklist_<CÓDIGO>.xlsx]

- Lee los bloques "=== TABLA: nombre ===" seguidos de un csv. Si una tabla aparece varias veces (por el prompt 03),
  usa la ÚLTIMA versión.
- Genera alertas: tablas que faltan, celdas N/D en datos clave, documentos no leídos completos, dudas abiertas
  y requisitos frecuentes (catalogo/requisitos_comunes.csv) que la respuesta no menciona.
- Imprime un resumen de alertas en JSON para que Claude Code lo use en la revisión.
"""
import argparse
import csv
import datetime
import io
import json
import os
import re
import unicodedata
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

AQUI = os.path.dirname(os.path.abspath(__file__))
CATALOGO = os.path.join(AQUI, "..", "catalogo", "requisitos_comunes.csv")

ESPERADAS = {
    "ficha": ["Campo", "Valor", "Fuente"],
    "anexos": ["Nº", "Nombre del archivo o documento", "Tipo", "Fecha", "¿Leído completo? (Sí/No/Parcial)", "Páginas", "Enlace"],
    "documentos": ["Nº", "Documento requerido", "Categoría", "Aplica a", "Formato exigido", "Vigencia máxima", "¿Firma y sello?",
                   "¿Subsanable?", "¿Causa descalificación?", "Momento", "Formulario o anexo modelo", "Fuente", "Texto literal"],
    "items": ["Ítem/Lote", "Descripción", "Cantidad", "Unidad", "Precio de referencia US$", "¿Se adjudica por ítem?",
              "Tallas / colores / distribución", "Plazo de entrega", "Lugar de entrega", "¿Muestra?", "Fuente"],
    "especificaciones": ["Ítem/Lote", "Atributo", "Valor exigido", "Obligatorio o deseable", "¿Admite equivalente?", "Fuente", "Texto literal"],
    "presentacion": ["Nº", "Requisito de presentación", "Detalle exigido", "Fuente", "Texto literal"],
    "fechas": ["Hito", "Fecha (DD/MM/AAAA)", "Hora", "Medio o lugar", "Fuente"],
    "evaluacion": ["Criterio", "Tipo", "Puntaje máximo o regla", "Mínimo para pasar", "Fuente"],
    "garantias": ["Tipo", "Porcentaje o monto", "Vigencia", "Emisor aceptado", "Momento de entrega", "Fuente"],
    "condiciones": ["Tema", "Detalle", "Fuente"],
    "cobertura": ["Documento", "Sección o numeral", "¿Leída? (Sí/No/Parcial)", "Motivo si no"],
    "dudas": ["Nº", "Tipo", "Descripción", "Pregunta sugerida para el período de consultas", "Fuente"],
}
ND = {"", "N/D", "ND", "N.D.", "NO APLICA", "-", "—"}


def sin_tildes(s):
    return "".join(c for c in unicodedata.normalize("NFD", str(s).upper()) if unicodedata.category(c) != "Mn")


def leer_respuesta(ruta):
    texto = open(ruta, encoding="utf-8-sig").read()
    partes = re.split(r"^\s*=+\s*TABLA:\s*([A-Za-zÁÉÍÓÚáéíóúñÑ_ ]+?)\s*=+\s*$", texto, flags=re.M)
    tablas = {}
    for i in range(1, len(partes), 2):
        nombre = sin_tildes(partes[i]).lower().strip().replace(" ", "_")
        cuerpo = partes[i + 1]
        m = re.search(r"```(?:csv)?\s*\n(.*?)```", cuerpo, flags=re.S)
        bloque = m.group(1) if m else "\n".join(l for l in cuerpo.splitlines() if l.strip().startswith('"'))
        filas = [f for f in csv.reader(io.StringIO(bloque.strip())) if any(x.strip() for x in f)]
        if not filas:
            continue
        enc, datos = [h.strip() for h in filas[0]], filas[1:]
        tablas[nombre] = [dict(zip(enc, [x.strip() for x in f] + [""] * (len(enc) - len(f)))) for f in datos]
        tablas[nombre + "__enc"] = enc
    return tablas


def es_nd(v):
    return sin_tildes(v).strip() in ND


def fecha(v):
    for fmt in ("%d/%m/%Y", "%d-%m-%Y", "%Y-%m-%d"):
        try:
            return datetime.datetime.strptime(v.strip()[:10], fmt).date()
        except ValueError:
            pass
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("respuesta")
    ap.add_argument("--salida")
    a = ap.parse_args()
    T = leer_respuesta(a.respuesta)
    carpeta = os.path.dirname(os.path.abspath(a.respuesta))
    ficha = {r.get("Campo", ""): r.get("Valor", "") for r in T.get("ficha", [])}
    codigo = ficha.get("Código") or os.path.basename(carpeta)
    salida = a.salida or os.path.join(carpeta, f"checklist_{codigo}.xlsx")

    # ------------------------------------------------------------ alertas
    alertas = []   # (nivel, texto)
    for t, enc in ESPERADAS.items():
        if t not in T:
            alertas.append(("ALTA", f"Falta la tabla '{t}' en la respuesta."))
        else:
            falt = [h for h in enc if h not in T[t + "__enc"]]
            if falt:
                alertas.append(("MEDIA", f"Tabla '{t}': faltan columnas {falt}."))
    for campo in ["Fecha y hora límite de ofertas", "Medio de presentación (COMPRASAL electrónica / física / ambas)", "Plazo de entrega",
                  "Lugar de entrega", "Forma de pago", "Vigencia de la oferta", "Fecha y hora límite de consultas"]:
        v = next((val for k, val in ficha.items() if sin_tildes(k).startswith(sin_tildes(campo)[:20])), "")
        if es_nd(v):
            alertas.append(("ALTA", f"Ficha: '{campo}' está vacío o N/D."))
    for r in T.get("documentos", []):
        if es_nd(r.get("Fuente", "")):
            alertas.append(("MEDIA", f"Documento sin fuente: {r.get('Documento requerido', '')}"))
    for r in T.get("especificaciones", []):
        if es_nd(r.get("Valor exigido", "")):
            alertas.append(("MEDIA", f"Especificación sin valor: ítem {r.get('Ítem/Lote', '')} · {r.get('Atributo', '')}"))
    for r in T.get("items", []):
        if es_nd(r.get("Cantidad", "")):
            alertas.append(("ALTA", f"Ítem sin cantidad: {r.get('Ítem/Lote', '')} {r.get('Descripción', '')[:60]}"))
        if sin_tildes(r.get("¿Muestra?", "")).startswith("SI"):
            alertas.append(("RECORDATORIO", f"Ítem {r.get('Ítem/Lote', '')} pide MUESTRA: revisar cómo, dónde y cuándo entregarla."))
    items_con_spec = {r.get("Ítem/Lote", "") for r in T.get("especificaciones", [])}
    for r in T.get("items", []):
        if r.get("Ítem/Lote", "") not in items_con_spec:
            alertas.append(("ALTA", f"Ítem {r.get('Ítem/Lote', '')} no tiene ninguna especificación."))
    for r in T.get("anexos", []):
        if not sin_tildes(r.get("¿Leído completo? (Sí/No/Parcial)", "")).startswith("SI"):
            alertas.append(("ALTA", f"Documento del proceso no leído completo: {r.get('Nombre del archivo o documento', '')}"))
    for r in T.get("cobertura", []):
        if not sin_tildes(r.get("¿Leída? (Sí/No/Parcial)", "")).startswith("SI"):
            alertas.append(("ALTA", f"Sección no leída: {r.get('Documento', '')} · {r.get('Sección o numeral', '')} ({r.get('Motivo si no', '')})"))
    n_dudas = len(T.get("dudas", []))
    if n_dudas:
        alertas.append(("MEDIA", f"Hay {n_dudas} dudas: enviarlas como consultas antes de la fecha límite de consultas."))

    texto_todo = sin_tildes(" ".join(" ".join(r.values()) for t in ESPERADAS if t in T for r in T[t]))
    if any(sin_tildes(r.get("¿Muestra?", "")).startswith("SI") for r in T.get("items", [])):
        texto_todo += " MUESTRA"
    no_mencionados = []
    with open(CATALOGO, encoding="utf-8") as f:
        for req in csv.DictReader(f):
            pat = req["Palabras clave (expresión regular, sin tildes, mayúsculas)"]
            if not re.search(pat, texto_todo):
                no_mencionados.append(req)
    for req in no_mencionados:
        alertas.append(("VERIFICAR", f"La respuesta no menciona: {req['Requisito']}. Confirmar en las bases si aplica."))

    hoy = datetime.date.today()
    limite = None
    for r in T.get("fechas", []):
        if "OFERTA" in sin_tildes(r.get("Hito", "")) and ("LIMITE" in sin_tildes(r.get("Hito", "")) or "RECEPCION" in sin_tildes(r.get("Hito", ""))):
            limite = fecha(r.get("Fecha (DD/MM/AAAA)", "")) or limite
    if limite is None:
        lim_txt = next((v for k, v in ficha.items() if "LIMITE DE OFERTAS" in sin_tildes(k)), "")
        limite = fecha(lim_txt)

    # ------------------------------------------------------------ Excel
    AZUL = PatternFill("solid", fgColor="1F4E78")
    fino = Side(style="thin", color="BFBFBF")
    BORDE = Border(left=fino, right=fino, top=fino, bottom=fino)
    WRAP = Alignment(wrap_text=True, vertical="top")
    NIVEL = {"ALTA": "F8CBAD", "MEDIA": "FFEB9C", "VERIFICAR": "DDEBF7", "RECORDATORIO": "E2EFDA"}
    wb = Workbook()

    def hoja(nombre, cols, filas, extra=(), anchos=None, lista=None):
        ws = wb.create_sheet(nombre)
        enc = list(cols) + list(extra)
        for j, h in enumerate(enc, 1):
            c = ws.cell(1, j, h)
            c.font, c.fill, c.border = Font(bold=True, color="FFFFFF"), AZUL, BORDE
            c.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center")
            ws.column_dimensions[get_column_letter(j)].width = (anchos or {}).get(h, 14 if h in extra else 22)
        for i, r in enumerate(filas, 2):
            for j, h in enumerate(cols, 1):
                c = ws.cell(i, j, r.get(h, ""))
                c.alignment, c.border = WRAP, BORDE
                if es_nd(str(r.get(h, ""))) and h not in ("Formulario o anexo modelo", "Motivo si no"):
                    c.fill = PatternFill("solid", fgColor="FCE4D6")
            for j in range(len(cols) + 1, len(enc) + 1):
                ws.cell(i, j).border = BORDE
        if lista and filas:
            dv = DataValidation(type="list", formula1=f'"{lista}"', allow_blank=True)
            ws.add_data_validation(dv)
            col = get_column_letter(len(cols) + 1)
            dv.add(f"{col}2:{col}{len(filas) + 1}")
        ws.freeze_panes = "B2"
        if filas:
            ws.auto_filter.ref = f"A1:{get_column_letter(len(enc))}{len(filas) + 1}"
        return ws

    ws = wb.active
    ws.title = "1. Resumen"
    ws.sheet_view.showGridLines = False
    ws.column_dimensions["A"].width = 34
    ws.column_dimensions["B"].width = 90
    ws["A1"] = f"Lista de verificación de oferta · {codigo}"
    ws["A1"].font = Font(bold=True, size=15, color="1F4E78")
    ws["A2"] = ficha.get("Nombre del proceso", "")
    ws["A3"] = ficha.get("Institución", "")
    ws["A2"].font = ws["A3"].font = Font(italic=True, color="595959")
    r = 5
    if limite:
        dias = (limite - hoy).days
        ws.cell(r, 1, "Fecha límite de ofertas").font = Font(bold=True)
        c = ws.cell(r, 2, f"{limite:%d/%m/%Y} · {'quedan ' + str(dias) + ' días' if dias >= 0 else 'YA VENCIÓ'}")
        c.font = Font(bold=True, color="C00000" if dias < 5 else "000000")
        r += 1
    for k in ["Modalidad", "Monto estimado US$", "Medio de presentación (COMPRASAL electrónica / física / ambas)", "Fecha y hora límite de consultas",
              "Plazo de entrega", "Lugar de entrega", "Forma de pago", "Vigencia de la oferta", "¿Adjudicación parcial por ítem?",
              "¿Reservado o con beneficio para MYPE?", "Enlace"]:
        v = next((val for kk, val in ficha.items() if sin_tildes(kk).startswith(sin_tildes(k)[:20])), "N/D")
        ws.cell(r, 1, k.split(" (")[0]).font = Font(bold=True)
        ws.cell(r, 2, v).alignment = WRAP
        r += 1
    r += 1
    resumen = [("Documentos a presentar", len(T.get("documentos", []))), ("Ítems", len(T.get("items", []))),
               ("Especificaciones", len(T.get("especificaciones", []))), ("Requisitos de presentación", len(T.get("presentacion", []))),
               ("Dudas para consultar", n_dudas)]
    for k, v in resumen:
        ws.cell(r, 1, k).font = Font(bold=True)
        ws.cell(r, 2, v)
        r += 1
    r += 1
    ws.cell(r, 1, f"ALERTAS ({len(alertas)})").font = Font(bold=True, size=12, color="C00000")
    r += 1
    for nivel, t in sorted(alertas, key=lambda x: list(NIVEL).index(x[0])):
        ws.cell(r, 1, nivel).fill = PatternFill("solid", fgColor=NIVEL[nivel])
        ws.cell(r, 1).font = Font(bold=True)
        ws.cell(r, 2, t).alignment = WRAP
        r += 1
    r += 1
    ws.cell(r, 1, "Cómo usar").font = Font(bold=True)
    for t in ["Marca el estado de cada fila en las hojas 2 a 5. Las celdas en naranja son datos N/D: confírmalos en las bases o pregúntalos en el período de consultas.",
              "Una alerta VERIFICAR no significa que el requisito exista: es un tema que las bases suelen pedir y que la respuesta no menciona."]:
        r += 1
        ws.cell(r, 2, t).alignment = WRAP

    hoja("2. Documentos", ESPERADAS["documentos"], T.get("documentos", []), extra=["Estado", "Responsable", "Observación"],
         anchos={"Documento requerido": 40, "Texto literal": 50, "Formato exigido": 28}, lista="Pendiente,En trámite,Listo,No aplica")
    hoja("3. Productos", ESPERADAS["items"], T.get("items", []), extra=["Costo unitario US$", "Precio a ofertar US$", "¿Muestra lista?"],
         anchos={"Descripción": 45, "Tallas / colores / distribución": 35})
    hoja("4. Especificaciones", ESPERADAS["especificaciones"], sorted(T.get("especificaciones", []), key=lambda x: x.get("Ítem/Lote", "")),
         extra=["¿Cumplimos?", "Evidencia (ficha, muestra, foto)"], anchos={"Valor exigido": 40, "Texto literal": 50},
         lista="Sí,No,Duda")
    hoja("5. Presentación", ESPERADAS["presentacion"], T.get("presentacion", []), extra=["Estado"],
         anchos={"Requisito de presentación": 34, "Detalle exigido": 50, "Texto literal": 50}, lista="Pendiente,Listo")
    hoja("6. Fechas", ESPERADAS["fechas"], sorted(T.get("fechas", []), key=lambda x: fecha(x.get("Fecha (DD/MM/AAAA)", "")) or datetime.date.max),
         anchos={"Hito": 40})
    hoja("7. Garantías y condiciones", ESPERADAS["garantias"], T.get("garantias", []), anchos={"Tipo": 34})
    ws7 = wb["7. Garantías y condiciones"]
    base = ws7.max_row + 2
    for j, h in enumerate(ESPERADAS["condiciones"], 1):
        c = ws7.cell(base, j, h)
        c.font, c.fill = Font(bold=True, color="FFFFFF"), AZUL
    for i, rr in enumerate(T.get("condiciones", []), base + 1):
        for j, h in enumerate(ESPERADAS["condiciones"], 1):
            ws7.cell(i, j, rr.get(h, "")).alignment = WRAP
    hoja("8. Evaluación", ESPERADAS["evaluacion"], T.get("evaluacion", []), anchos={"Criterio": 40, "Puntaje máximo o regla": 40})
    hoja("9. Dudas y consultas", ESPERADAS["dudas"], T.get("dudas", []), extra=["¿Enviada?", "Respuesta"],
         anchos={"Descripción": 45, "Pregunta sugerida para el período de consultas": 50}, lista="No,Sí")
    hoja("10. Documentos del proceso", ESPERADAS["anexos"], T.get("anexos", []), anchos={"Nombre del archivo o documento": 45, "Enlace": 40})
    hoja("11. Cobertura", ESPERADAS["cobertura"], T.get("cobertura", []), anchos={"Documento": 34, "Sección o numeral": 34, "Motivo si no": 40})
    for w in wb.worksheets:
        w.page_setup.orientation = "landscape"
        w.page_setup.fitToWidth, w.page_setup.fitToHeight = 1, 0
        w.sheet_properties.pageSetUpPr.fitToPage = True
    wb.save(salida)
    print(json.dumps({"salida": salida, "codigo": codigo, "fecha_limite": str(limite) if limite else None,
                      "conteos": dict(resumen), "alertas": [{"nivel": n, "texto": t} for n, t in alertas]}, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
