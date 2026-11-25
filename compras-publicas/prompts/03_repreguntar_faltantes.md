# Prompt 03 · Repreguntar lo que faltó o quedó dudoso

**Para qué sirve:** después de la revisión, pedirle a la extensión SOLO lo que falta o no cuadra, sin repetir toda la extracción.

**Cómo usarlo:** normalmente lo llena Claude Code al terminar `/compras-revisar-proceso` y lo guarda en `procesos/<CÓDIGO>/prompt03_<n>.md`. Esta plantilla no se modifica.

1. Pega el prompt en la extensión.
2. Pega la respuesta **al final** de `respuesta.md`.
3. El script junta las versiones: las filas nuevas se agregan y las corregidas reemplazan a las anteriores. Así no se pierde nada de la primera extracción.

---

~~~
Actúa como un auditor de licitaciones públicas. En COMPRASAL, abre de nuevo el proceso [CÓDIGO].

SOLO LEER Y DESCARGAR: no hagas clic en Ofertar, Enviar, Manifestar interés, Guardar, Aceptar términos ni en enviar consultas. Si te pide iniciar sesión o un CAPTCHA, detente.

En una revisión anterior quedaron estos PENDIENTES. Resuelve solo estos, uno por uno:
[1. ...]
[2. ...]

Para cada pendiente:
- búscalo en todos los documentos del proceso, incluidas adendas y respuestas a consultas;
- si lo encuentras, da el dato, la fuente (documento, página, numeral) y el texto literal (máximo 40 palabras);
- si de verdad no aparece, escribe "N/D" y, en la tabla dudas, lista los documentos que revisaste.

REGLAS: no deduzcas ni inventes; fechas en formato DD/MM/AAAA; dentro de una celda no uses comillas dobles (para pulgadas escribe "pulg.").

ENTREGA: SOLO las filas nuevas o corregidas, en las tablas de abajo. Cada una va con su marcador, un bloque csv con estos encabezados exactos y todas las celdas entre comillas dobles y separadas por comas.
[ENCABEZADOS: Claude Code pega aquí, para cada tabla afectada, el marcador "=== TABLA: nombre ===" y su línea de encabezados]

Termina con esta línea exacta:
=== FIN REPREGUNTA ===
~~~
