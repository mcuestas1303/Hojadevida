# Prompt 03 · Repreguntar lo que faltó o quedó dudoso

**Para qué sirve:** después de la revisión de los agentes, pedirle a la extensión SOLO lo que falta o lo que no cuadra, sin repetir toda la extracción.

**Cómo usarlo:** normalmente lo llena Claude Code al terminar `/compras-revisar-proceso`. A mano, cambia **PROCESO** y la lista de **PENDIENTES**. Cuando tengas la respuesta, agrégala al final de `respuesta.md`; el script toma la última versión de cada tabla.

---

```
Actúa como un auditor de licitaciones públicas. En COMPRASAL, abre de nuevo el proceso [CÓDIGO] (no inicies sesión ni envíes formularios).

En una revisión anterior quedaron estos PENDIENTES. Resuelve solo estos, uno por uno:
[1. ...]
[2. ...]

Para cada pendiente:
- búscalo en todos los documentos del proceso, incluidas adendas y respuestas a consultas;
- si lo encuentras, da el dato, la fuente (documento, página, numeral) y el texto literal (máximo 40 palabras);
- si de verdad no aparece, escribe "No aparece en los documentos" y lista los documentos que revisaste.

ENTREGA: usa el mismo formato del prompt anterior: "=== TABLA: nombre ===" y debajo un bloque csv con los mismos encabezados. Incluye SOLO las tablas que cambian, y en cada una TODAS sus filas (las anteriores corregidas más las nuevas), porque esta versión reemplaza a la anterior.
```
