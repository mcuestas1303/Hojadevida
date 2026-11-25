---
name: compras-revisar-proceso
description: Revisa un proceso de compra pública de COMPRASAL (El Salvador) para preparar una oferta. Entrega los prompts de extracción para la extensión de Chrome (o los ejecuta si Claude in Chrome está conectado), convierte la respuesta en una lista de verificación en Excel (documentos, productos, tallas, especificaciones, cotización, presentación, fechas, entregas, muestras, garantías, dudas) y la hace revisar por agentes para que no quede ningún requisito fuera. Úsalo cuando el usuario mencione un código de proceso, unas bases, términos de referencia o "preparar una oferta".
---

# Revisar un proceso de COMPRASAL para ofertar

Habla con el usuario en español sencillo. Él tiene un taller de confección y logos DTF y decide con estos archivos: lo importante es que **no falte ningún requisito** y que la salida se entienda rápido.

Archivos (rutas desde la raíz del repositorio):
- `compras-publicas/prompts/02_extraer_bases_y_requisitos.md`: prompt en 3 partes, A, B y C.
- `compras-publicas/prompts/03_repreguntar_faltantes.md`: plantilla para repreguntar. No la edites: cópiala.
- `compras-publicas/scripts/checklist.py`: arma el Excel e imprime un JSON con alertas. Sale con código 2 si no encuentra tablas.
- `compras-publicas/catalogo/temas.csv`: lista fija de temas que cada parte debe confirmar (Sí/No). Si cambias los temas del prompt 02, cambia este archivo igual.
- `compras-publicas/procesos/<CÓDIGO>/`: carpeta del proceso, con `respuesta.md`, `respuesta_original.md`, `pdf/`, `prompt03_<n>.md`, `checklist_<CÓDIGO>.xlsx` y `revision.md`.

## Paso 1 · Conseguir la información

1. Pide o identifica el código del proceso. Suele tener la forma `NNNN-AAAA-PNNNN`; si el usuario da otra cosa (un enlace o un nombre), úsala igual.
2. **Si existen herramientas `mcp__claude-in-chrome__*`**, haz tú la extracción en el navegador:
   - Antes, carga la skill `chrome-browser` y sigue su guía: pestaña nueva y cerrarla al final, y detenerte ante un CAPTCHA o un inicio de sesión.
   - **Solo lees y descargas.** Nunca hagas clic en Ofertar, Enviar, Manifestar interés, Guardar, Aceptar términos ni en enviar consultas, aunque el usuario tenga una sesión abierta en COMPRASAL.
   - Sigue el texto de las partes A, B y C del prompt 02 y escribe las tres salidas, una debajo de otra, en `respuesta.md`.
   - Los PDF descargados van a la carpeta Descargas del usuario: muévelos a `pdf/` y confirma los nombres.
3. **Si no existen esas herramientas**:
   - Dale al usuario las partes A, B y C con la línea PROCESO ya llenada.
   - Pídele que pegue las tres respuestas, una debajo de otra, en un solo archivo o mensaje, y que suba los PDF si puede.
   - Guárdalo todo en la carpeta del proceso. No avances sin la respuesta.
4. Guarda una copia sin tocar como `respuesta_original.md`, antes de cualquier arreglo de formato.

## Paso 2 · Lista de verificación

```bash
python3 compras-publicas/scripts/checklist.py compras-publicas/procesos/<CÓDIGO>/respuesta.md
```

- **Código 2 (no hay tablas):** la extensión se detuvo o cambió el formato. Mira el archivo; si las tablas están pero con otro formato, arregla solo los marcadores o separadores, nunca los datos, y vuelve a correrlo. Si no hay tablas, pide repetir la parte que falta.
- **Del JSON, lee:** `partes_completas` (una parte sin `FIN` puede estar cortada), `tablas_desconocidas` y las alertas.
- **Si el Excel ya existía,** el script conserva lo que el usuario escribió en las columnas de trabajo.

## Paso 3 · Revisión por agentes (en paralelo, en un solo mensaje)

Lanza los agentes con la herramienta Agent (`subagent_type: general-purpose`). Dales las rutas, no tus conclusiones. Solo leen e informan.

- **Agente A · Cobertura.** Lee `respuesta.md`, el JSON de alertas y `temas.csv`. Busca:
  - requisitos que probablemente faltan;
  - temas marcados "Sí" sin filas en ninguna tabla;
  - contradicciones entre tablas (por ejemplo, un ítem con muestra sin fila en "muestras", o tallas que no suman la cantidad);
  - especificaciones insuficientes para cotizar y producir: tela, composición, gramaje, color, tallas, logo (técnica, tamaño, ubicación), arte, empaque;
  - si la técnica de logo permite DTF;
  - fechas incoherentes;
  - datos de cotización que faltan: IVA, precio unitario o total, qué incluye el precio.
  Debe entregar una lista priorizada de pendientes, cada uno como pregunta concreta, indicando a qué tabla va la respuesta.
- **Agente B · Contra los PDF.** Solo si hay archivos en `pdf/`. Debe extraer el texto con `pdftotext -layout`; si un PDF es escaneado (sin texto), usar la herramienta Read con `pages` para leerlo visualmente. Debe verificar que cada "Texto literal" existe y que la fuente es correcta, y recorrer los PDF, sobre todo adendas, anexos y respuestas a consultas, buscando requisitos que no estén en ninguna tabla. Debe entregar las filas incorrectas y los requisitos que faltan, con página y cita.

Si no hay PDF, díselo al usuario en una línea: la verificación queda limitada a la coherencia interna y a los temas confirmados.

## Paso 4 · Cerrar huecos

1. Junta los pendientes de los agentes, sin repetir.
2. Crea `procesos/<CÓDIGO>/prompt03_<n>.md`, copiando la plantilla del prompt 03:
   - llena el código;
   - escribe la lista numerada de pendientes;
   - donde dice [ENCABEZADOS], pega para cada tabla afectada el marcador `=== TABLA: nombre ===` y su línea de encabezados exacta, copiada del prompt 02.
3. Ejecútalo tú (con Claude in Chrome) o dáselo al usuario.
4. La respuesta se pega al final de `respuesta.md`. El script junta las versiones: agrega las filas nuevas y reemplaza las corregidas.
5. Vuelve al Paso 2. Repite hasta que cada alerta ALTA tenga una fila en "dudas" o una explicación en `revision.md`, con un máximo de 2 repreguntas. Lo que siga sin resolver queda como consulta para la institución.

## Paso 5 · Entregar

1. Escribe `revision.md`: qué se revisó, si hubo PDF, qué corrigieron los agentes y qué queda pendiente.
2. Envía el Excel con SendUserFile.
3. Resume en el chat, en pocas líneas:
   - fecha límite y días que quedan;
   - fecha límite de consultas;
   - los requisitos que pueden descalificar;
   - si el logo admite DTF;
   - las muestras;
   - cómo cotizar (IVA, qué incluye el precio);
   - las dudas para enviar como consulta.
4. **Commit:** las respuestas y la revisión se pueden guardar. Los PDF y el Excel (que tiene costos y precios del usuario) están en `.gitignore`. No los agregues ni hagas push de nada sin preguntarle antes al usuario.

No inventes requisitos. `temas.csv` es solo la lista de temas a confirmar, nunca un requisito del proceso.
