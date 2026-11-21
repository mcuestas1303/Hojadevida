# Revisión de producción — supervisor de continuidad

## Revisión 1 — 2026-11-21 — final (`06_final/tin_y_tan_short01_v1.mp4`)

**Qué se revisó:** el video final (30,0 s, 1080x1920, 30 fps, con audio). Lo miré yo por mi cuenta, sin repetir lo que ya
revisó el Generador (`vuelta_01/`, `vuelta_02/`, `decisiones_de_render.md`).

**Herramientas:**

- `analizar_video.py --cada 0.5`: 60 fotogramas en 3 hojas, miradas una por una.
- Fotogramas a resolución completa en 0,75 · 1,20 · 5,57 · 5,60 · 6,47 · 6,50 · 16,30 · 27,40 s.
- `postpro.py destellos`.
- `silencedetect` sobre `05_audio/dialogo_110.mp3` (con el retraso de 1,0 s), para cruzar las pausas de la voz con los cortes.

Las copias de trabajo quedan en el scratchpad de la sesión y no se suben.

**Contra qué comparé:**

- Las fichas de `@tin` y `@tan`: «Definición para generar», «Lo que nunca cambia» y «Prohibido».
- `02_prompt/prompt.md`, secciones 5, 6, 11, 12 y 13.
- `canales/nostalgia-tin-y-tan/DESIGN.md`.
- `manual/11_retencion_y_revision.md`, regla 20.
- `02_prompt/direccion.md`: **está sin llenar** (es la plantilla vacía). La dirección quedó metida dentro de
  `prompt.md` (mapa de ritmo, rejilla, golpes), así que comparé contra eso.

**Nota de proceso:** no cuesta créditos. Todo es dibujo por código; no hay nada que regenerar ni que pagar.

| Toma | Personaje fiel | Emoción se lee | Cámara | Actuación | Continuidad | Defectos | Veredicto |
|---|---|---|---|---|---|---|---|
| 1 (0,0–0,5) | — | Sí: el casete entra girando e inclinado | Fija, según el prompt | — | El fotograma 0 coincide con el cierre | Ninguno | APROBADA |
| 2 (0,5–1,0) | — | Sí | Empuje al carrete izquierdo | — | Bien | En 0,75 el borde derecho del casete sale del cuadro (lo pide el empuje del prompt; ya está anotado) | APROBADA |
| 3 (1,0–3,5) | Tan: cabeza `#2F7F7A`, rodete con cinta, bufanda de dos puntas. Bien | Sí: ojos cerrados con sonrisa, se lee «recuerdo» | Empuje lento | El lápiz cae al carrete en 2,8 | El rodete queda a 15 px del casete (ya anotado) | **De 1,0 a 1,3 s, «how many turns?» sigue a opacidad plena sobre el plano de Tan** (fotograma 1,20). Choca con la regla del prompt §11 «lo que sale se va antes de que entre lo siguiente», aunque la tabla §12 diga que sale en 1,3 | CORREGIR EN EDICIÓN: que el texto 1 salga en 0,8–0,9 (render.py, gratis) |
| 4 (3,5–5,0) | — | Sí | Empuje al centro del carrete | 3 vueltas del lápiz | Bien | Ninguno. A 2 fotogramas por segundo el lápiz sale siempre en el mismo ángulo porque da una vuelta por pulso; a 30 fps se ve girar | APROBADA |
| 5 (5,0–6,5) | Tin: cabeza naranja, gorra con visera, lentes, lápiz. La visera de perfil se lee como gorra (5,57) | Sí | Fija | Entra caminando; en 5,6 cambia de pose de golpe (lo pide el prompt) | Lados bien: Tan a la izquierda con espejo, Tin a la derecha | Ninguno grave | APROBADA |
| 6 (6,5–9,5) | Los dos, bien | Débil: los carretes paran y los personajes casi no se mueven durante 3 s | Empuje del 3 %, que casi no se nota | **En 6,5 los dos cambian de pose en el mismo fotograma** (Tan: de `pregunta` a `parado`; Tin: de `parado` a `explica`) con el mismo encuadre de la toma 5. Se ve como un tirón, no como un corte | **De 5,0 a 9,5 s (4,5 s) el encuadre es el mismo**: el corte de 6,5 no se percibe | Demasiado tiempo sin cambio + salto de pose | CORREGIR EN EDICIÓN (cambio de especificación, gratis): darle a la toma 6 otro encuadre (plano más cerrado de los dos o del casete) o un `borrón` en 6,5, y dejar girando los carretes o mover el lápiz de Tin |
| 7 (9,5–12,0) | — | Media: la cinta corre, pero es una tira de 77 px | Fija | — | Mismo papel crema | **2,5 s con unos dos tercios del cuadro vacíos**: solo la tira en y = 45 % y el texto | CORREGIR EN EDICIÓN (cambio de especificación): tira de al menos 8–10 % de alto o el casete pequeño a la vista, del que sale la cinta |
| 8 (12,0–14,5) | — | Sí: el contador sube y la cinta se alarga | Fija | — | El casete pequeño es el mismo diseño | Ninguno | APROBADA |
| 9 (14,5–17,0), plano héroe | Los dos, bien; las pestañas de Tan se ven | Media | Fija | El lápiz de Tin tiene movimiento secundario | Bien | **El plano héroe es el más débil del video**: carrete de 160 px arriba a la izquierda, arco y segmento de 3 px (16,30). En un teléfono el dato de 11 cm es un hilo | CORREGIR EN EDICIÓN (cambio de especificación): carrete de 300 px o más, trazo de 8 px o más, segmento centrado en la zona de gráficos |
| 10 (17,0–18,5) | Tin en plano medio, sin lápiz: es una variación permitida (`objeto=False` en `piensa`, ficha) | Sí: mano al mentón y cejas de `pensando` | Empuje del 6 % | Bien | Bien | Ninguno | APROBADA |
| 11 (18,5–20,5) | — | Sí | Fija | — | Bien | Los cortes de 3 px se leen como textura al final; aceptable para un símbolo | APROBADA |
| 12 (20,5–23,5) | Los dos, bien | Sí: es el pico. Tan con la boca en «o» y Tin con el lápiz en alto | Empuje del 2 % | Bien | El contador solo sube; 1,170 en tomate | Ninguno | APROBADA |
| 13 (23,5–25,5) | — | Sí: revelado desde el desenfoque | Fija | — | Bien | Observación: el lápiz gira desde el centro como una manecilla. Junto con la aguja tomate parecen dos manecillas de un reloj | APROBADA |
| 14 (25,5–27,0) | — | Sí | Fija | — | Mismo reloj | Observación: el lápiz queda parado hacia las 5 y la aguja justo antes de las 12. Se puede leer como una hora («5:58»). Menor | APROBADA |
| 15 (27,0–28,0) | Los dos con `risa`, bien | Sí | Fija | Bien | La corchea queda entre el texto y el casete sin tocarlos (27,40) | Ninguno | APROBADA |
| 16 (28,0–30,0) | — | Sí | Fija | — | El fotograma 29,75 vuelve a la posición del 0,25: el bucle empalma | Ninguno | APROBADA |
| Audio | — | No se puede oír (lo mido) | — | — | **Las pausas de la voz caen en los cortes**: 3,35–3,64 → corte 3,5 · 6,44–6,72 → 6,5 · 9,11–9,40 → 9,5 · 11,59–11,98 → 12,0 · 14,30–14,60 → 14,5 · 16,94–17,22 → 17,0 · 18,54–18,83 → 18,5 · 20,25–20,55 → 20,5 · 23,46–23,75 → 23,5 · 24,94–25,56 → 25,5 · 26,62–27,03 → 27,0. El corte de 5,0 cae a mitad de frase, como pide el prompt | 1) **El video lleva música, y el prompt §7 dice que «no entra al video hasta que el dueño lo decida»**. 2) Los golpes bajo la voz están a −38 LUFS (24 dB por debajo de ella): en un teléfono, lo más probable es que los clics de los cortes de 1,0 a 27,9 no se oigan | CORREGIR EN EDICIÓN: llevarle al dueño las dos mezclas (con y sin música) para que elija; subir `DB_BAJO_VOZ` en `codigo/audio.py` (de −24 a unos −12 dB) y comprobarlo al oído |

### Fichas de personaje

- **Tin:** se ven todos los puntos de la lista de comprobación.
  - Cabeza `#E07A2E` con contorno, gorra con visera clara, botón y costuras.
  - Lentes redondos con brillo y cejas visibles bajo la visera.
  - Lápiz con goma y punta. Falta solo en la toma 10, que es una variación permitida.
  - Brazo del gesto a la derecha del cuadro.
- **Tan:** cabeza verde azulado, rodete oscuro con cinta mostaza, pestañas cortas (no parecen cejas de enojo) y bufanda
  con dos puntas que no tapa el brazo. Siempre a la izquierda con espejo.
- Los dos tienen el mismo alto en los planos de los dos.
- No aparecen personajes ajenos, logos, marcas ni letras en el casete.

### DESIGN.md

Se cumple lo siguiente:

- La paleta.
- Minúsculas alineadas a la izquierda.
- Ningún degradado.
- La palabra clave en mostaza con trazo.
- Contadores que solo suben.
- Los motivos que vuelven: el casete y el lápiz.

Hay un hueco: el documento solo trae la composición 16:9 (suelo a 86 %). El short usa 80 % porque lo dice el prompt.
Conviene añadir a `DESIGN.md` una sección «Composición 9:16» para que el próximo short no tenga que inventarla.

### Preguntas fijas (cap. 11, regla 20)

| Pregunta | Respuesta | Evidencia |
|---|---|---|
| ¿Movimiento y corte antes del segundo 1? | Sí | El casete se mueve desde el fotograma 0; hay corte en 0,5 y `borrón` en 1,0 |
| ¿Plano héroe cerca de la mitad? | Sí, pero flojo | La toma 9 (14,5–17,0) es el héroe que pide el prompt, pero el gráfico ocupa poco y las líneas son de 3 px |
| ¿Picos y respiros? | Sí | Respiros en 1,0–3,5, 6,5–9,5 y 28,0–30,0; pico en 20,5–23,5. Pero de 5,0 a 9,5 el encuadre no cambia: el respiro dura 4,5 s, no 3 |
| ¿Final que empalma con el inicio? | Sí | 29,75 ≈ 0,25 (casete inclinado abajo); el fotograma 900 es igual al 0 (render.py) |
| ¿Cada corte con su sonido? | Sí en el archivo, dudoso al oído | Los 44 golpes empiezan en su segundo (`medidas_audio.json`), pero los que caen bajo la voz están a −38 LUFS |
| ¿Algo genérico? | No | Sin degradados, sin mayúsculas centradas, sin brillos; dibujo propio |
| ¿Más de 3 destellos por segundo? | No | `postpro.py destellos`: 0 cambios fuertes de brillo |
| ¿Todo con licencia? | Sí, con dos pendientes antes de publicar | Todo está en `licencias.md`. Faltan: leer los términos completos de Higgsfield para la voz, y abrir la fuente de 4,76 cm/s (Philips Technical Review, 1970), que solo se vio en un resumen de buscador. El prompt §8 dice que hasta tener la fuente no se publica |

### Fotogramas muertos y tramos a rehacer (render por código, 0 créditos)

| Segundos | Qué pasa | Qué se rehace |
|---|---|---|
| 1,0–1,3 | Texto del gancho sobre el plano de Tan | Salida del texto 1 en 0,8–0,9 |
| 5,0–9,5 | El mismo encuadre durante 4,5 s y salto de pose doble en 6,5 | Toma 6 con otro encuadre o `borrón` en 6,5; más movimiento dentro de la toma |
| 9,5–12,0 | Dos tercios del cuadro vacíos | Toma 7 con una tira más alta o con el casete a la vista |
| 14,5–17,0 | Plano héroe con el gráfico pequeño y líneas finas | Toma 9 con el carrete y los trazos más grandes |
| 1,0–27,9 (audio) | Clics de corte probablemente inaudibles | Subir `DB_BAJO_VOZ` y escucharlo |

**Qué es gratis en código sin tocar la especificación:** la salida del texto en 0,9 y el nivel de los golpes. La salida
del texto contradice la tabla §12, pero cumple la regla §11.

**Qué es un cambio de especificación (también gratis):**

- El encuadre de la toma 6.
- El tamaño de la toma 7.
- El tamaño del gráfico de la toma 9.

Lo decide el equipo: `director-de-fotografia` y `director-de-prompts` actualizan `prompt.md` y vuelven a validar.

**Qué decide el dueño:** si la música entra al video o no.

**Antes de publicar:** escucharlo, confirmar la fuente de la velocidad y llenar `direccion.md`, o anotar que la
dirección vive en `prompt.md`.

Cada vuelta nueva se anota aquí como «Revisión 2».

**Veredicto general: CAMBIOS.** Los personajes son fieles y no hay defectos de identidad. Falta corregir el ritmo de
5,0 a 12,0 s, reforzar el plano héroe y aclarar el audio (la música y el nivel de los golpes). Todo se hace por código
y no cuesta créditos.
