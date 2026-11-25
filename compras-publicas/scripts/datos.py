"""Carga y limpieza de procesos de COMPRASAL exportados por la extensión de Chrome.

- Lee TODOS los .csv de una carpeta (cada uno puede venir de un prompt distinto).
- Quita procesos repetidos entre archivos (mismo código).
- Clasifica cada proceso según el PERFIL del producto (uniformes, generico, ...).
- Une municipios antiguos (antes de la reorganización de 2024) con el nuevo cuando los datos nombran el distrito.
- Marca repetidos con otro código, relanzamientos y partidas de presupuesto del mismo mes.

Para agregar un producto nuevo: escribir una función clasificar_<producto>(nombre, tipo, institucion) que devuelva
(categoría o None, motivo de exclusión), un diccionario PESO_<producto> y registrarlos en PERFILES.
"""
import glob
import os
import re
import unicodedata
import pandas as pd

COLS = {"Codigo": "Código", "Institucion compradora": "Institución", "Monto US$": "Monto",
        "Año PAC": "Año", "Mes previsto (PAC)": "MesPAC", "Mes previsto de ejecución (MM/AAAA)": "MesPAC",
        "Fecha publicacion": "Publicado", "Fecha de publicación": "Publicado",
        "Proveedor adjudicado": "Proveedor", "Proveedor adjudicado (si hay)": "Proveedor"}


def sin_tildes(s):
    return "".join(c for c in unicodedata.normalize("NFD", str(s).upper()) if unicodedata.category(c) != "Mn")


def tiene(n, *pal):
    return any(re.search(p, n) for p in pal)


# ============================================================ perfil: uniformes y prendas
PRENDA_SIN_UNIF = r"CAMIS|POLO|GABACHA|CHUMPA|PANTALON|JEANS|VESTUARIO|PRENDA|TRAJE|BLUSA|FILIPINA"


def clasificar_uniformes(nombre, tipo="", institucion=""):
    n = sin_tildes(nombre)
    t = tipo or ""
    if tiene(n, r"TOMACORRIENTE", r"COREOGRAF", r"DESCARTABLE", r"POLIPROPILENO", r"INSUMOS MEDICOS - GABACHAS",
             r"LAVANDERIA", r"DESTRUCCION", r"OVERHAUL", r"MOTOR", r"CINTA DE SEGURIDAD PARA", r"CINTA REFLECTIVA PARA",
             r"SUBLIMACION DE CODIGO", r"MATERIALES PARA", r"COSTURERIA", r"KIT DE ASISTENCIA", r"SEGURIDAD INDUSTRIAL"):
        return None, "No es prenda (servicio, insumo o equipo)"
    if tiene(n, r"PACIENTES"):
        return None, "Ropa hospitalaria"
    if "escolar" in t.lower() or tiene(n, r"ESCOLAR", r"CENTROS EDUCATIVOS", r"ESTUDIANTES DE BACHILLERATO"):
        return None, "Uniformes escolares"
    if "materia prima" in t or tiene(n, r"MATERIA PRIMA"):
        return None, "Tela / materia prima"
    if tiene(n, r"\bTELAS?\b", r"TEXTILES PARA ELABORA") and not tiene(n, r"PRENDAS", r"CONFECCIONAD", r"CAMIS", r"CHUMPA", r"UNIFORME"):
        return None, "Tela / materia prima"
    if tiene(n, r"HOSPITALARI", r"ROPA DE CAMA", r"ROPA QUIRURG", r"SABANA") and not tiene(n, r"UNIFORME"):
        return None, "Ropa hospitalaria"
    if re.search(r"^\W*(\w+\s+){0,3}(DE\s+)?(CALZADO|BOTAS|ZAPATOS)\b", n) or \
            (tiene(n, r"CALZADO", r"\bBOTAS?\b", r"ZAPATO") and not tiene(n, PRENDA_SIN_UNIF, r"UNIFORME")):
        return None, "Solo calzado"
    if tiene(n, r"SERVICIO DE (ELABORACION PARA )?BORDADO", r"SERVICIO DE ESTAMPADO", r"BORDADO DE", r"ESTAMPADO DE", r"SERVICIO DE SERIGRAF"):
        return "Bordado / estampado (servicio de logo)", ""
    if tiene(n, r"DEPORTIV", r"FUTBOL", r"TORNEO", r"BALONCESTO", r"BASQUET", r"VOLEIBOL", r"\bLIGA", r"ATLET", r"PANTS"):
        return "Deportivo", ""
    if tiene(n, r"BANDA", r"BALLET", r"ORQUESTA", r"\bGALA\b", r"DANZA", r"FOLKLOR", r"CORO\b", r"BATUCADA", r"CACHIPORR"):
        return "Grupos culturales (banda, ballet, orquesta)", ""
    if tiene(n, r"AGENTES", r"\bCAM\b", r"POLICIA", r"VIGILAN", r"BOMBER", r"CUSTODI", r"CADETES", r"MILITAR", r"SUPERNUMERARIO",
             r"PERSONAL DE SEGURIDAD", r"DGME", r"CONTROL MIGRATORIO", r"GUARDAPARQUE", r"GUARDARRECURSO"):
        return "Agentes / seguridad", ""
    if tiene(n, r"OPERATIV", r"CAMPO", r"DESECHOS", r"RECOLEC", r"MANTENIMIENTO", r"REFLECTIV", r"JEANS", r"DE TRABAJO", r"OVEROL", r"BRIGAD", r"RESCATE"):
        return "Operativo / de campo", ""
    if tiene(n, r"CAMISETA", r"\bPOLOS?\b", r"PLAYERA", r"GORRA", r"GORRO", r"CHUMPA", r"PROMOCIONAL", r"ESTAMPAD", r"BORDAD",
             r"SERIGRAF", r"\bLOGO", r"IDENTIFICACI", r"DISTINTIVO", r"INDUMENTARIA", r"CHALECO") or \
            (tiene(n, r"CAMISA") and not tiene(n, r"UNIFORME")):
        return "Camisas / promocional / identificación", ""
    if tiene(n, r"UNIFORME", r"GABACHA", r"FILIPINA", r"PRENDAS", r"CONFECCION", r"PANTALON", r"VESTUARIO DE", r"ROPA", r"CAMISA"):
        return "Uniforme institucional", ""
    if tiene(n, r"TEXTIL", r"VESTUARIO"):
        if "HOSPITAL" in sin_tildes(institucion):
            return None, "Ropa hospitalaria"
        return "Textiles y vestuario (sin detalle)", ""
    return None, "No es prenda (servicio, insumo o equipo)"


PESO_UNIFORMES = {"Camisas / promocional / identificación": 1.0, "Deportivo": 1.0, "Bordado / estampado (servicio de logo)": 1.0,
                  "Uniforme institucional": 0.7, "Operativo / de campo": 0.7, "Agentes / seguridad": 0.3,
                  "Textiles y vestuario (sin detalle)": 0.0, "Grupos culturales (banda, ballet, orquesta)": 0.0}


# ============================================================ perfil: genérico (cualquier producto)
def clasificar_generico(nombre, tipo="", institucion=""):
    """Sin reglas propias: incluye todo lo que trajo la extensión, en una sola categoría."""
    return "General", ""


PERFILES = {
    "uniformes": (clasificar_uniformes, PESO_UNIFORMES),
    "generico": (clasificar_generico, {"General": 1.0}),
}

# ============================================================ instituciones y municipios
MANUAL = {"9801": "9451",          # La Unión Norte: dos códigos (2025 y 2026)
          "86520411": "861411",    # Secretaría de la Mujer de San Salvador: dos códigos
          "8614": "8652"}          # Alcaldía de San Salvador -> San Salvador Centro (reorganización 2024)
DEPTO = {"81": "Ahuachapán", "82": "Santa Ana", "83": "Sonsonate", "84": "Chalatenango", "85": "La Libertad",
         "86": "San Salvador", "87": "Cuscatlán", "88": "La Paz", "89": "Cabañas", "90": "San Vicente",
         "91": "Usulután", "92": "San Miguel", "93": "Morazán", "94": "La Unión"}


def es_muni_antiguo(c):
    return bool(re.fullmatch(r"[89]\d{3}", c)) and c[:2] in DEPTO and int(c[2:]) <= 50


def es_muni_nuevo(c):
    return bool(re.fullmatch(r"[89]\d{3}", c)) and c[:2] in DEPTO and int(c[2:]) >= 51


def limpiar_muni(s):
    s = sin_tildes(s)
    s = re.sub(r"^(ALCALDIA MUNICIPAL DE|ALCALDIA DE|MUNICIPIO DE|MUNICIPALIDAD DE)\s+", "", s)
    return s.strip()


def unir_municipios(d):
    """Une un municipio antiguo con el nuevo de su departamento cuando los procesos del nuevo nombran el distrito."""
    texto = {}
    for c, g in d[d["Clave"].map(es_muni_nuevo)].groupby("Clave"):
        texto[c] = " || ".join(sin_tildes(x) for x in list(g["Nombre del proceso"]) + list(g["Institución"]))
    mapa, evidencia = {}, {}
    antiguos = d[d["Clave"].map(es_muni_antiguo)].groupby("Clave")["Institución"].first()
    for c, nom in antiguos.items():
        if c in MANUAL:
            continue
        nm = limpiar_muni(nom)
        if len(nm) < 4:
            continue
        pat = re.compile(r"(DISTRITOS? (DE |DEL )?(LA |EL |LOS )?" + re.escape(nm) + r"\b)|(-\s?" + re.escape(nm) + r"\b)|(\|\| " + re.escape(nm) + r"( \|\||$))")
        cand = [k for k, tx in texto.items() if k[:2] == c[:2] and pat.search(tx)]
        if len(cand) == 1:
            mapa[c] = cand[0]
            evidencia[c] = pat.search(texto[cand[0]]).group(0).strip("| ")
    return mapa, evidencia


def normal(n):
    n = sin_tildes(n)
    n = re.sub(r"(SEGUNDA|TERCERA|2DA|3RA)\s+CONVOCATORIA|SEGUNDO PROCESO|SEGUNDA PUBLICACION|\d+", " ", n)
    return re.sub(r"[^A-Z]+", " ", n).strip()


def cargar(carpeta, perfil="uniformes"):
    clasificar, peso = PERFILES[perfil]
    partes = []
    rutas = sorted(glob.glob(os.path.join(carpeta, "*.csv")))
    if not rutas:
        raise SystemExit(f"No hay archivos .csv en {carpeta}")
    for ruta in rutas:
        d = pd.read_csv(ruta, dtype=str, encoding="utf-8-sig").fillna("").rename(columns=COLS)
        faltan = [c for c in ("Código", "Nombre del proceso", "Institución", "Modalidad", "Monto", "Año", "MesPAC") if c not in d.columns]
        if faltan:
            raise SystemExit(f"{os.path.basename(ruta)}: faltan columnas {faltan}. Usa los encabezados del prompt 01.")
        for c in ("Estado", "Publicado", "Enlace", "Proveedor"):
            if c not in d.columns:
                d[c] = "N/D"
        d["Fuente"] = os.path.splitext(os.path.basename(ruta))[0]
        d["Tipo"] = d.get("Cantidad y tipo de prenda", pd.Series("", index=d.index)).str.extract(r"tipo: (.*)\)$")[0].fillna("")
        partes.append(d)
    d = pd.concat(partes, ignore_index=True)
    d = d[d["Código"].str.strip() != ""].copy()
    d["Código"] = d["Código"].str.strip()
    d["Monto"] = pd.to_numeric(d["Monto"].str.replace(",", ""), errors="coerce")
    d = d[d["Monto"].notna()].copy()
    d["Año"] = d["Año"].astype(int)
    d["Mes"] = d["MesPAC"].str[:2].astype(int)
    d["AñoMes"] = d["MesPAC"].str[3:].astype(int)
    d["Abierto"] = d["Estado"].str.contains("En curso|En ejecuci|Recepci", regex=True)
    d["_info"] = (d["Publicado"] != "N/D").astype(int) + d["Enlace"].str.startswith("http").astype(int) + (d["Tipo"] != "").astype(int)
    n_en_dos = int(d["Código"].duplicated().sum())
    d = d.sort_values("_info", ascending=False).drop_duplicates("Código").copy()
    d["Clave"] = d["Código"].str.split("-").str[0]
    cat = [clasificar(n, t, i) for n, t, i in zip(d["Nombre del proceso"], d["Tipo"], d["Institución"])]
    d["Categoría"] = [c for c, _ in cat]
    d["Excluido por"] = [m for _, m in cat]
    n = d["Nombre del proceso"].map(sin_tildes)
    d["Otros bienes"] = n.str.contains(r"TROFEO|PELOTA|BALON|MEDALLA|IMPLEMENTOS|MATERIAL DEPORTIVO|INSUMOS|MEDICAMENT|CALZADO|BOTAS|BOLSAS|STICKER|ACCESORIOS|EQUIPO|RECONOCIMIENTO|PREMIO|MALLAS") \
        if perfil == "uniformes" else False

    mapa, evid = unir_municipios(d)
    d["Inst"] = d["Clave"].map(lambda c: MANUAL.get(c, mapa.get(c, c)))
    d["Unido desde"] = d.apply(lambda r: r["Institución"] if r["Inst"] != r["Clave"] else "", axis=1)
    d["Muni antiguo sin unir"] = d["Inst"].map(es_muni_antiguo)

    d = d.sort_values(["Inst", "Año", "Mes", "Código"]).reset_index(drop=True)
    d["Norm"] = d["Nombre del proceso"].map(normal)
    d["Cuenta como"] = "Concurso"
    d["Concurso"] = d["Código"]
    inc = d["Categoría"].notna()
    for _, g in d[inc].groupby(["Inst", "Año"]):
        vistos = {}
        for i, r in g.iterrows():
            k = (r["Norm"], round(r["Monto"], 2))
            if k in vistos:
                d.at[i, "Cuenta como"], d.at[i, "Concurso"] = "Posible repetido", vistos[k]
            else:
                vistos[k] = r["Código"]
        n_rel = g["Nombre del proceso"].map(sin_tildes).str.contains(r"CONVOCATORIA|DESIERT|SEGUNDO PROCESO|SEGUNDA PUBLICACION")
        for i in g[n_rel].index:
            if d.at[i, "Cuenta como"] != "Concurso":
                continue
            otros = g[(g.index != i) & (g["Categoría"] == d.at[i, "Categoría"]) & ~n_rel]
            if len(otros):
                d.at[i, "Cuenta como"], d.at[i, "Concurso"] = "Relanzamiento", otros.iloc[0]["Código"]
        gen = g[g["Categoría"] == "Textiles y vestuario (sin detalle)"]
        for _, gg in gen.groupby("Mes"):
            if len(gg) > 1:
                cid = f"{gg.iloc[0]['Código']}+{len(gg) - 1}"
                for i in gg.index:
                    if d.at[i, "Cuenta como"] == "Concurso":
                        d.at[i, "Cuenta como"], d.at[i, "Concurso"] = "Partida agrupada", cid
    return d, n_en_dos, mapa, evid, peso
