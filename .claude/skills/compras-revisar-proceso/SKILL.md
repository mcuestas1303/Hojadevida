---
name: compras-revisar-proceso
description: Revisa un proceso de compra pública de COMPRASAL (El Salvador) para preparar una oferta. Entrega el prompt de extracción para la extensión de Chrome (o lo ejecuta si Claude in Chrome está conectado), convierte la respuesta en una lista de verificación en Excel (documentos, productos, especificaciones, forma de presentación, fechas, garantías, dudas) y la hace revisar por agentes para que no quede ningún requisito fuera. Úsalo cuando el usuario mencione un código de proceso, unas bases, términos de referencia o "preparar una oferta".
---

# Revisar un proceso de COMPRASAL para ofertar

Habla con el usuario en español sencillo. Él tiene un taller de confección y logos DTF y decide con estos archivos: lo importante es que **no falte ningún requisito** y que la salida se entienda rápido.

Archivos de este flujo (rutas desde la raíz del repositorio):
- `compras-publicas/prompts/02_extraer_bases_y_requisitos.md`: prompt de extracción.
- `compras-publicas/prompts/03_repreguntar_faltantes.md`: prompt para pedir solo lo que faltó.
- `compras-publicas/scripts/checklist.py`: arma el Excel e imprime las alertas en JSON.
- `compras-publicas/catalogo/requisitos_comunes.csv`: red de seguridad con los requisitos que suelen pedirse.
- `compras-publicas/procesos/<CÓDIGO>/`: carpeta de trabajo de cada proceso (`respuesta.md`, `pdf/`, `checklist_<CÓDIGO>.xlsx`, `revision.md`).

## Paso 1 · Conseguir la información del proceso

1. Identifica el código del proceso (formato `NNNN-AAAA-PNNNN`). Si el usuario no lo dio, pregúntaselo.
2. Si existen herramientas `mcp__claude-in-chrome__*` (la sesión corre en la computadora del usuario con la extensión conectada), haz tú la extracción en el navegador siguiendo al pie de la letra el texto del prompt 02. Guarda la salida en `compras-publicas/procesos/<CÓDIGO>/respuesta.md` y descarga los PDF a `pdf/`. Sigue la guía de la skill de Chrome (pestaña nueva, no iniciar sesión, detenerse ante un CAPTCHA).
3. Si no existen esas herramientas: dale al usuario el bloque del prompt 02 con la línea PROCESO ya llenada, listo para pegar. Pídele que suba la respuesta y, si puede, los PDF del proceso. Cuando lleguen, guárdalos en la carpeta del proceso. No avances sin la respuesta.

## Paso 2 · Armar la lista de verificación

```bash
python3 compras-publicas/scripts/checklist.py compras-publicas/procesos/<CÓDIGO>/respuesta.md
```

Lee el JSON que imprime: conteos, fecha límite y alertas (ALTA, MEDIA, VERIFICAR, RECORDATORIO). Si falla por formato (la extensión cambió los marcadores o los encabezados), corrige el formato del archivo sin cambiar ningún dato y vuelve a correrlo.

## Paso 3 · Revisión por agentes (en paralelo, en un solo mensaje)

Lanza estos agentes con la herramienta Agent (`subagent_type: general-purpose`). Dale a cada uno las rutas, no tus conclusiones. Cada uno solo lee e informa; no edita archivos.

- **Agente A · Cobertura.** Lee `respuesta.md`, el JSON de alertas y `requisitos_comunes.csv`. Busca:
  - requisitos que probablemente faltan;
  - contradicciones entre tablas (por ejemplo, un ítem con muestra pero sin instrucciones de entrega de la muestra en "presentacion");
  - especificaciones incompletas para poder cotizar y producir: tela, composición, gramaje, color, tallas, logo (técnica, tamaño, ubicación), empaque;
  - si la técnica de logo exigida permite DTF;
  - fechas incoherentes.
  Debe entregar una lista priorizada de pendientes, cada uno redactado como pregunta concreta para la extensión.
- **Agente B · Verificación contra los PDF.** Lánzalo solo si hay archivos en `pdf/`. Para cada fila con "Texto literal", debe confirmar que la cita existe en el PDF y que la fuente (página, numeral) es correcta. Además debe recorrer los PDF buscando requisitos que no estén en ninguna tabla, sobre todo en adendas, anexos y respuestas a consultas. Debe usar herramientas de texto de PDF (por ejemplo `pdftotext -layout`); si un PDF es escaneado, decirlo. Debe entregar: filas incorrectas, requisitos que faltan (con página y cita) y documentos ilegibles.

Si no hay PDF, díselo al usuario en una línea: la verificación queda limitada a la coherencia interna y a la lista de requisitos comunes.

## Paso 4 · Cerrar huecos

1. Junta los pendientes de los agentes y quita los repetidos.
2. Si hay pendientes, llena `prompts/03_repreguntar_faltantes.md` con el código y la lista numerada. Ejecútalo tú si tienes Claude in Chrome, o dáselo al usuario para pegar.
3. La respuesta se agrega al final de `respuesta.md`: el script usa la última versión de cada tabla.
4. Repite los pasos 2 a 4 hasta que no queden alertas ALTA sin explicar, con un máximo de 2 repreguntas. Lo que siga sin resolverse se queda en la hoja "Dudas y consultas" como pregunta para el período de consultas de la institución.

## Paso 5 · Entregar

1. Escribe `compras-publicas/procesos/<CÓDIGO>/revision.md` con: qué se revisó, si hubo PDF, qué corrigieron los agentes y qué quedó pendiente.
2. Envía el Excel al usuario con SendUserFile.
3. Resume en el chat, en pocas líneas: fecha límite y días que quedan; los requisitos que pueden descalificar; si el logo admite DTF; las muestras; y las dudas para enviar como consulta antes de su fecha límite.
4. Haz commit de la carpeta del proceso.

No inventes requisitos. Lo que viene de `requisitos_comunes.csv` es solo un recordatorio de temas a confirmar, nunca un requisito del proceso.
