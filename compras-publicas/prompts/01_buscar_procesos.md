# Prompt 01 · Buscar procesos de un producto (para el calendario)

**Para qué sirve:** traer de COMPRASAL los procesos de 2024 a 2026 de un producto, para armar el calendario de oportunidades.

**Cómo usarlo:**
1. Cambia solo las líneas **PRODUCTO**, **PALABRAS CLAVE**, **EXCLUIR** y **MODALIDAD**. Para copiar listas de palabras clave ya probadas, ver `../catalogo/palabras_clave.md`.
2. Pega el prompt en la extensión de Chrome.
3. Guarda el CSV en `compras-publicas/datos/<producto>/<modalidad o rango>_2024-2026.csv`. Cada corrida es un archivo; si un proceso sale repetido en varios archivos, el script lo cuenta una sola vez.
4. En Claude Code: `/compras-calendario <producto>`.

**Recomendación:** corre el prompt una vez por modalidad, y además una vez con el filtro de monto $2,000–$50,000. Si le pides todo de una vez, la extensión suele quedarse a medias.

---

```
Actúa como analista de compras públicas. Ve a https://www.comprasal.gob.sv y usa la búsqueda pública de procesos y de Planes Anuales de Compras (PAC). No inicies sesión ni envíes formularios que no sean de búsqueda.

PRODUCTO: [ej. uniformes y prendas con logo]
PALABRAS CLAVE (búscalas una por una): [ej. "uniforme", "camisa", "camiseta", "polo", "chumpa", "gabacha", "uniforme deportivo", "bordado", "promocional"]
EXCLUIR: [ej. uniformes escolares del MINEDUCYT, tela suelta y materia prima]
MODALIDAD: [Todas / Comparación de precios / Subasta inversa / Licitación competitiva / Contratación directa / Convenios / Subasta en plataformas privadas / Baja cuantía]
MONTO: [Todos / solo $2,000 a $50,000]
PERIODO: 2024, 2025 y 2026.

PASO 0: dime en 3 líneas qué nombres de modalidad ofrece el filtro (tal como aparecen) y si se puede filtrar por año y por monto.

PARA CADA PROCESO EXTRAE (encabezados exactos, una fila por proceso):
Código | Nombre del proceso | Institución | Modalidad | Monto US$ | Tipo de monto (ESTIMADO PAC / ADJUDICADO) | Año PAC | Mes previsto de ejecución (MM/AAAA) | Fecha de publicación | Estado | Proveedor adjudicado (si hay) | Enlace

REGLAS:
- No inventes datos: si algo no aparece, escribe N/D.
- No repitas procesos que salgan con varias palabras clave.
- Recorre TODAS las páginas de resultados de cada palabra clave. Si son más de 300 procesos, detente al llegar a 300 y dime en qué palabra y en qué página quedaste.
- Si aparece un CAPTCHA, un inicio de sesión o un error, detente y dime en qué palabra clave y en qué página quedaste.

ENTREGA: la tabla completa en formato CSV, con los encabezados exactos de arriba y todas las celdas entre comillas dobles.
```
