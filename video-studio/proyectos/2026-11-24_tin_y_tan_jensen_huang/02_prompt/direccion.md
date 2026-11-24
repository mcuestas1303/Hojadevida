# Dirección del video

> La llena el equipo, cada uno su sección, **antes** del prompt. `director-de-prompts` escribe `prompt.md` a partir
> de esto; `supervisor-de-continuidad` revisa contra esto. Manual: `video-studio/manual/`.

## 1. Objetivo y público — director-creativo

- **Objetivo comercial:** (copiado del brief: monetizar · presencia · recordación · comunidad · conversión · viralidad · otro)
- **KPI principal y meta:** (p. ej. compartidos por mil ≥ 15; meta inicial si aún no hay datos propios)
- **Cómo cambia el objetivo las decisiones:** (duración, gancho, llamada a la acción, formato)
- **Público objetivo:** (edad, intereses, plataforma, por qué lo compartiría)
- **Idea en una línea:**
- **Por qué funciona para ese público:**
- **Aprendizaje que aplicamos:** (del último informe de `video-studio/estadisticas/`, o «sin datos todavía»)

## 2. Emoción, arco y gancho — director-creativo

- **Duración total:**
- **Gancho A (0–1 s):** (movimiento desde el primer fotograma + afirmación de contraste o cifra con fuente)
- **Gancho B (para probar):**
- **Curiosidades encadenadas:** (qué pregunta abre cada tramo y dónde se resuelve)
- **Capítulos visibles:** (« 1/5 » o lista que crece; «no aplica» si no enumera)
- **Cierre que empalma con el inicio (loop):**
- **Llamado a la acción (uno solo):**

| Tiempo | Segundos | Emoción (fila del cap. 01) | Qué pasa |
|---|---|---|---|
| Gancho | | | |
| Tensión | | | |
| Giro / remate | | | |
| Salida | | | |

## 3. Cámara y luz — director-de-fotografia

- **Luz y paleta por escenario:**

| Toma | Dur. | Emoción | Plano | Ángulo | Lente | Movimiento | Frase de cámara (inglés) |
|---|---|---|---|---|---|---|---|
| 1 | | | | | | | |

- **Motivos visuales que vuelven (1 o 2):**
- **Fondo que se mantiene entre planos de objeto:**
- **Tipos de plano (videos de más de 20 s):** detalle · héroe abierto (cerca de la mitad) · subjetivo · revelado
- **Referencias cargadas:** (imagen aprobada, hoja de emociones, `DESIGN.md` si hay gráficos)
- **Se resuelve en edición:**
- **Tomas encadenadas (último fotograma → keyframe):**

## 3b. Color con intención — director-de-fotografia (valida director-creativo)

> `video-studio/manual/13_color_con_intencion.md`. Regla: 2 neutros + 1 acento; el acento va solo en el título y en
> un elemento.

Escrita el 2026-11-24 por el director de fotografía, sobre el render 3 (`06_final/tin_y_tan_short03_v1.mp4`). Revisada con las hojas de contacto de `07_revision/vuelta_02/analisis/` (cada 0,5 s), `par.jpg` de la vuelta 3, la portada y `revisar_color*.txt` de la vuelta 2 (el render 3 solo cambia las tarjetas de 22,5 a 24,5 s: fuera de ahí la diferencia es 0,25 de 255, firma del supervisor). Manda sobre el bloque «Color con intención» de `prompt.md` §12 en lo que difiera. La firma está en `07_revision/vuelta_03/firma_fotografia.md`.

- **Neutros (2):**
  - Papel `#F3E9D2`: fondo de todos los planos, con grano fijo y viñeta. Variantes del mismo papel: `#FFF8EC` (cuerpo del calendario) y `#E6D8B8` (suelo, lona de la silla). Marrón `#7A4B2A` solo como relleno de silla, mesa y barras: es objeto, no acento.
  - Tinta `#2B2420`: líneas, contornos, todo texto que no es clave (rótulos pequeños de las barras y subtítulos en español incluidos) y las marcas de 4 px de las barras. Tinta sobre papel 12,6:1.
- **Acento (1): mostaza `#E8B33B`.** Va en la palabra clave del rótulo (el título del plano: «11», «12», «17», «6», «23», «12,274», «5», «else», «Subscribe») y en **un** elemento: el lápiz (cuerpo mostaza en `palitos.py`) o, cuando el plano trae otro gráfico, el círculo del 12 o del 23, la marca de 11 días o la barra de Altman. Siempre con contorno de tinta de 0,045 em en las letras. **No va en:** texto que no es clave, silla, calendario (salvo el círculo), barras (salvo las marcas citadas), suelo, subtítulos, personajes. La bufanda de Tan y el cuerpo del lápiz son identidad y no cuentan como acento (manual 13 §2.4).
- **Excepción declarada: tomate `#C8553D`, solo en el pico.** La cifra «4,382» pasa de tinta (mientras el contador sube) a tomate con contorno de tinta de 0,045 em al llegar (22,07 s, 71,2 %) y queda hasta 24,4 s (tomas 10 y 11, ≈ 2,3 s de 31). En esas dos tomas Tin va sin lápiz y no hay mostaza como acento: el único acento del plano es el tomate. En la toma 12 el acento vuelve a mostaza. `ficha.json` deja `acento` en mostaza y nombra el tomate como excepción del pico. Cumple «un acento por plano» y no «un acento por pieza» a la letra (hay dos tonos de acento en 31 s): lo acepto por las mismas razones del short 2 (está en la paleta del canal, cae en el giro, no hay dos acentos dentro de un plano). **Detalle que no es acento:** la goma del lápiz es tomate (`palitos.py`, `relleno="tomate"`), una franja de ≈ 8 px en todo plano donde el lápiz aparece. Es identidad del objeto; el negativo global del prompt («tomato red outside the reveal shots») debe leerse sin contarla.
- **Rótulos pequeños de las barras («Huang 11», «Altman 5», «Jobs 4,382»), 56 px (≈ 2,9 % del alto):** en **tinta, sin acento**. Por qué: son nombres y cifras de apoyo, no la clave; si llevaran mostaza serían un segundo y tercer acento dentro de un plano que ya tiene la clave grande, y sobre papel la mostaza da 1,6:1. Tinta sobre papel 12,6:1, sin pastel sobre pastel. Son el texto más chico del video (a 360 px de ancho de pantalla ≈ 19 px): se leen, pero están en el mínimo; no bajarlos. Las marcas de 4 px de Huang y de Altman van en tinta salvo donde el plano las vuelve acento (toma 9: Altman; toma 12: Huang). **Salvedad:** una marca mostaza de 4 px sobre papel no puede llevar contorno de tinta (lo taparía) y a 1,6:1 se ve como un hilo pálido en las hojas; no es lo que informa (lo dicen la clave «5 days» / «11 days» y el nombre de la barra en tinta). Siguiente video: marca de 8 px con borde de tinta de 2 px, o dejarla en tinta y llevar el acento solo a la clave.

| Tomas | Segundos | Acento del plano | Elemento acento | Neutros y identidad que no cuentan |
|---|---|---|---|---|
| 1 y 14 (portada y bucle) | 0,0–1,0 y 30,0–31,0 | mostaza | «11» de «Back In / 11 Days?» y el lápiz en vuelo | silla (marrón y papel sombra), bufanda, cabezas |
| 2 | 1,0–3,5 | mostaza | «11» de «11 days?» | silla lejana |
| 3 | 3,5–6,5 | mostaza | «12» y círculo del 12 (el lápiz es identidad) | calendario, silla |
| 4 | 6,5–9,0 | mostaza | «17» | mesa de junta (marrón y papel sombra) |
| 5 | 9,0–11,5 | mostaza | «6» / «23» y círculo del 23 | flecha y cruces en tinta |
| 6 | 11,5–12,5 | mostaza | «11» | calendario con cruces |
| 7 | 12,5–14,5 | mostaza | «12,274» y marca de 11 días | barra marrón |
| 8 | 14,5–16,0 | ninguno (respiro) | — | solo neutros e identidad |
| 9 | 16,0–19,0 | mostaza | «5» y barra de Altman | barra de Huang en tinta |
| 10 y 11 | 19,0–24,5 | tomate (cifra desde 22,07 s) | «4,382» | barra de Jobs marrón; sin lápiz; bufanda es identidad |
| 12 | 24,5–27,0 | mostaza | «11» y marca de Huang | lápiz vuelve como identidad |
| 13 | 27,0–30,0 | mostaza | «else» / «Subscribe» y el lápiz que pasa | silla |

- **Por qué esta paleta (hipótesis para este público, no significado fijo; manual 13 §1):** el público es quien sigue la noticia en EE. UU., sin edad fija, viendo Shorts en el teléfono. Papel crema y tinta son cálidos y de saturación baja (≈ 16–17 % medido): para una noticia sobre una persona real, el fondo apagado evita el tono de alarma o de burla que daría un rojo, un negro o un neón, y deja el peso en las cifras. Es la paleta del canal (no se inventó ningún color). La mostaza es el único cálido saturado del cuadro después de los personajes: lleva el ojo a la clave en un solo lugar (R33, respaldo del manual 14, como en el prompt). El tomate, guardado para la cifra de Jobs, cambia de tono justo cuando el contador llega a 4,382, para que ese número se sienta como golpe y no como un dato más. Es hipótesis: una sola pieza no separa el efecto del color del efecto de la cifra, de la subida de sonido y del silencio de 12 fotogramas (`PARAMETROS.md`: los resultados son «a prueba»).
- **Cómo ayuda al objetivo:** entrar al Programa de socios lo antes posible (dueño, 2026-11-23) pide vistas calificadas de Shorts y suscriptores. Retención: el acento único lleva la mirada a la clave desde el primer cuadro (la portada con «11» en mostaza), donde el short 1 perdió a cuatro de cada cinco (20,7 % se quedó) → métrica: visto frente a deslizado (meta > 20,7 %) y retención de los segundos 1 a 3. Compartidos: el giro a tomate hace del 71,2 % un pico visible que pide enviarse («mira cuánto tardó Jobs») → métrica: retención en 22,07–24,4 s frente a 19–21 s, compartidos por mil vistas. Reconocimiento: la misma paleta de los shorts 1 y 2 → espectadores que regresan y suscriptores por mil vistas. Lectura: el color solo no mueve estas métricas; si la retención cae en 21–23 s, es una pista sobre el tomate, no una prueba.
- **Riesgos de lectura:**
  1. **Mostaza doble en la portada y en las tomas con lápiz** («11» + lápiz): es el mismo tono usado en el título y en un elemento, exactamente la regla del manual 13 §2.3; no son dos acentos. Riesgo real solo si el lápiz fuera más grande que la clave: en `06_final/portada_short03.png` el lápiz mide ≈ 190 px de largo (leído en la imagen, no medido con código) y la clave «11» ≈ 105 px de alto con contorno, y el ojo va primero al texto.
  2. **Tinta sobre tomate 3,5:1 en la cifra del pico:** no pasa 4,5:1 ni 7:1. Por el manual 13 §5.2 se mide el contorno contra el fondo: tinta sobre papel 12,6:1, con trazo de 0,045 em y cifra al 7 % del alto (≈ 134 px). Además la misma cifra va en tinta en «days» (12,6:1), en el nombre de la barra («Jobs 4,382») y en la tarjeta «4.382 días.», así que el dato no depende del tomate. No hay texto corrido en tomate. No se oscurece: saldría de la paleta del canal.
  3. **Tomate y naranja de Tin:** el tomate y el naranja `#E07A2E` quedan a ΔE76 ≈ 24,7 (cálculo a mano; `DESIGN.md` pide ≥ 25 para el acento de partida). Es el acento del pico y no el de partida, y en los planos 10 y 11 el tomate va arriba (cifra) y el naranja abajo (cara), separados por la barra y por el contorno. Sin cambio; medir con `revisar_color.py` en el próximo video.
  4. **Daltonismo y rojo contra verde:** ninguna información se separa por rojo contra verde; el tomate y el verde azulado de Tan no llevan información entre sí, y el tomate se distingue del papel por luminosidad (3,6:1) y por el contorno.
  5. **Público de 45 o más:** texto corrido y subtítulos en tinta sobre papel (12,6:1 ≥ 7:1); nada de pastel sobre pastel. Los subtítulos en español llevan panel de papel translúcido (0,82) sin nada dibujado debajo (medido: 0 píxeles), de modo que el fondo efectivo es papel; sin acento. En los 3 fotogramas de entrada y de salida de cada tarjeta el texto baja a gris (se ve en las hojas): 0,1 s, aceptado.
  6. **Pantalla chica:** los rótulos de barras son el mínimo (ver arriba); el resto, a 86 px o más.
- **Medido (lo llena el supervisor):** `revisar_color.py` sobre el video (31 cuadros, vuelta 2): ≈ 93 % en paleta (mínimo 85 %), saturación ≈ 16 %, luminosidad ≈ 90 %, entre segundos ±1 %. Portada (fotograma 0): ≈ 93 %, saturación ≈ 17 %. Contrastes calculados: tinta/papel 12,6:1, tinta/mostaza 8,0:1, tinta/tomate 3,5:1, tomate/papel 3,6:1, mostaza/papel 1,6:1 (siempre con contorno). Pendiente: la medición separada de los cuadros de 21 a 24,5 s para confirmar el peso del tomate (en los dominantes del video completo no aparece). Firma de color del supervisor: «FIRMADO (solo la medición)», `07_revision/vuelta_03/firma_supervisor.md` (control 8).

## 4. Actuación — director-de-animacion

| Toma | Personaje | Pose inicial (keyframe) | Anticipación → acción → pose final | Secundaria | Mirada | Panel de la hoja |
|---|---|---|---|---|---|---|
| 1 | | | | | | |

- **Frases de actuación (inglés), por toma:**
- **¿Hace falta grabar un clip propio para transferir movimiento?:**

## 5. Sonido — disenador-de-sonido

| Toma | Voz (texto exacto) | Efectos (segundo) | Música |
|---|---|---|---|
| 1 | | | |

- **Lista de golpes** (cada corte, destello o salto del mapa de ritmo con su sonido):

| Segundo | Qué pasa en imagen | Sonido |
|---|---|---|
| | | |

- **Voz en off o labios:**
- **Música:** (la pone el dueño / prompt en `05_audio/audio.md`)

## 6. Montaje y salida — editor-de-video

- **Mapa de ritmo:** (tramos densos y respiros de 2–3 s; nunca pulso plano; acelera hacia el final y remata con el plano del inicio)

| Tramo | Segundos | Densidad (cambios) | Qué pasa |
|---|---|---|---|
| | | | |

- **Orden y duración de tomas:**
- **Cortes y transiciones:**
- **Loop:**
- **Subtítulos y texto en pantalla:**
- **Color:** (igualar tomas según la sección 3b; `postpro.py color` o LUT; nada fuera de la paleta decidida)
- **Salidas por plataforma:**

## 7. Ruta de producción y presupuesto — jefe-de-produccion

- **Modo:** (A clip propio · B réplica · C desde cero)

| Toma | Método | Borrador (modelo, ajuste) | Final (modelo, ajuste) | Intentos | Créditos |
|---|---|---|---|---|---|
| 1 | | | | 1 | |

- **Ahorro por edición:**
- **Total estimado / presupuesto del brief:**
- **Alternativa más barata:**

## 8. Publicación y medición — director-creativo

- **Plataforma(s) y hora:**
- **Título:**
- **Descripción y etiquetas:**
- **Llamada a la acción:**
- **Etiquetas para estadísticas:** (personaje, modo, gancho, emoción, duración, formato; van a `estadisticas/etiquetas.csv`)
- **Revisión de resultados:** (fecha: 72 h para Shorts, 7 días para videos largos)
