---
name: compras-calendario
description: Arma o actualiza el calendario de oportunidades de compras públicas de COMPRASAL (El Salvador) para un producto (uniformes, zapatos, chalecos o cualquier otro), a partir de los CSV que trae la extensión de Chrome. Entrega un Excel para decidir (hoy, diciembre, Top 15, vista anual, por institución, procesos) revisado por agentes. Úsalo cuando el usuario quiera saber quién compra un producto, cuándo y por cuánto, o traiga CSV nuevos de COMPRASAL.
---

# Calendario de oportunidades de COMPRASAL

Habla con el usuario en español sencillo. Él tiene un taller pequeño y usa el calendario para decidir: lo general va primero, el detalle después, y las cifras no deben engañar.

Archivos de este flujo (rutas desde la raíz del repositorio):
- `compras-publicas/prompts/01_buscar_procesos.md`: prompt de búsqueda (una corrida por modalidad o rango de monto).
- `compras-publicas/catalogo/palabras_clave.md`: palabras clave por producto.
- `compras-publicas/datos/<producto>/*.csv`: datos de cada producto.
- `compras-publicas/scripts/datos.py`: carga, quita duplicados, clasifica por perfil, une municipios reorganizados y detecta repetidos y partidas de presupuesto.
- `compras-publicas/scripts/calendario.py`: arma el Excel.

## Paso 1 · Datos

1. Define el producto y su carpeta `compras-publicas/datos/<producto>/`.
2. Si el usuario subió CSV, cópialos ahí con un nombre descriptivo. Revisa que tengan los encabezados del prompt 01; si no, ajusta solo los nombres de las columnas, nunca los datos.
3. Si faltan datos, entrégale el prompt 01 con PRODUCTO, PALABRAS CLAVE y EXCLUIR llenados desde `palabras_clave.md`. Indícale qué corridas hacer: una por modalidad y una con el filtro de $2,000–$50,000.
4. Si existen herramientas `mcp__claude-in-chrome__*`, puedes hacer tú las corridas en el navegador siguiendo el prompt.

## Paso 2 · Perfil del producto

- **`uniformes`** ya existe.
- **Producto nuevo:** usa `generico` para una primera vista. Si el usuario lo va a usar seguido, agrega un perfil en `datos.py`, siguiendo `clasificar_uniformes`:
  - exclusiones (lo que no es el producto);
  - categorías;
  - pesos de qué le conviene más a un taller pequeño.
  Después revisa una muestra de 40 nombres por categoría y corrige las reglas.

## Paso 3 · Generar

```bash
python3 compras-publicas/scripts/calendario.py --datos compras-publicas/datos/<producto> --perfil <perfil> \
  --producto "<Nombre visible>" --anio <año a planificar> --salida compras-publicas/calendario_<producto>_<año>.xlsx
```

## Paso 4 · Revisión por agentes

Lanza un agente `general-purpose` que solo lea e informe. Dale las rutas de los CSV, de los scripts y del Excel, y pídele que revise dos cosas.

**Exactitud:**
- duplicados entre archivos y con otro código;
- falsos positivos y negativos del clasificador, citando códigos;
- cifras del Resumen que se inflen por el año más viejo;
- partidas de presupuesto contadas como compras;
- instituciones con dos códigos;
- municipios antiguos sin unir.

**Utilidad para decidir:**
- que el Top 15 premie concursos reales y frecuentes de monto manejable, y no la cantidad de filas;
- que "HOY" y "DICIEMBRE" estén arriba;
- que no haya columnas que no dicen nada.

Aplica las correcciones en los scripts, no a mano en el Excel, y vuelve a generar. Antes de entregar, convierte el Excel a PDF con `soffice --headless --convert-to pdf` y `pdftoppm`, y revisa visualmente las páginas 1 a 4.

## Paso 5 · Entregar

1. Envía el Excel con SendUserFile.
2. Resume: qué hacer hoy, qué preparar en diciembre, las cifras clave y lo que quedó sin resolver.
3. Haz commit de los datos, los scripts y el Excel.

## Errores conocidos que no deben repetirse

- Contar 2024 en los promedios anuales: duplica municipios antiguos y nuevos. Usar los dos años más recientes.
- Mostrar una regla como "se repite" sin aclarar que es "se planificó en el PAC".
- Desempatar el Top 15 por el número de filas, que premia las partidas de presupuesto.
- Prometer un mes exacto: mostrar el trimestre y desde cuándo vigilar.
- Marcar como OFERTAR a municipios que ya no existen: van como HISTÓRICO.
