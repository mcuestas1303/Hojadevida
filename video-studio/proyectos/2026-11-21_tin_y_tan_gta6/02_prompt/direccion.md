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

Esta pieza no tiene cámara ni generador de video: es 2D dibujado por código (`palitos.py`), 0 créditos de imagen y video. «Cámara» aquí es el encuadre fijo del render; lo único que se mueve son los objetos (muelle, contador, balanceo del mando) y el `borrón` de transición, que es edición. Por eso no hay lente, ni profundidad, ni luz modelada: se escribe lo que el video es.

- **Luz y paleta por escenario:** un solo escenario, el papel crema. Luz plana, sin fuente ni sombra proyectada (cap. 11, regla 7: sin degradados, sin resplandor). Fondo `#F3E9D2`, suelo `#E6D8B8` a 86 % de la altura, hoja de calendario `#FFF8EC`. Es igual en las 13 tomas. El fondo (saturación ≈ 17 %) es más apagado que los dos personajes, así que no compite con el naranja de Tin ni con el verde azulado de Tan. Paleta completa en 3b.

| Toma | Dur. | Emoción | Plano | Ángulo | Lente | Movimiento (cámara) | Luz | Frase de cámara (inglés) |
|---|---|---|---|---|---|---|---|---|
| 1 | 0,0–1,0 s | gancho, curiosidad | detalle: mando a pantalla completa | frontal | plano 2D | fija; el mando retumba y el botón late (objeto) | papel plano | `Locked-off flat frontal frame, controller filling the frame, no camera movement` |
| 2 | 1,0–2,0 s | nostalgia | medio: Tan con el mando | frontal | plano 2D | fija | papel plano | `Locked-off flat frontal medium shot, no camera movement` |
| 3 | 2,0–5,0 s | pregunta, expectativa | objeto grande: hoja de calendario (revelado 2013 → 2026) | frontal | plano 2D | fija; la hoja pasa (objeto) | papel plano | `Locked-off flat frontal insert of a calendar page, no camera movement` |
| 4 | 5,0–9,0 s | nostalgia, saludo | abierto: Tan y Tin con la hoja encima (héroe abierto) | frontal | plano 2D | fija | papel plano | `Locked-off flat frontal wide two-shot, Tan left, Tin right, no camera movement` |
| 5 | 9,0–11,0 s | cálculo, duda | detalle: tira de 13 bloques y Tan | frontal | plano 2D | fija; los bloques se llenan (objeto) | papel plano | `Locked-off flat frontal detail of a block strip with Tan below, no camera movement` |
| 6 | 11,0–13,5 s | cálculo, duda | detalle: tira y Tan | frontal | plano 2D | fija; contador sube | papel plano | `Locked-off flat frontal detail, counter rising, no camera movement` |
| 7 | 13,5–15,0 s | sorpresa pequeña | detalle: marcas bisiestas sobre la tira | frontal | plano 2D | fija | papel plano | `Locked-off flat frontal detail, three small marks pop above the strip, no camera movement` |
| 8 | 15,0–17,5 s | cálculo | detalle: tira, corchete y Tan | frontal | plano 2D | fija | papel plano | `Locked-off flat frontal detail, counter rising, no camera movement` |
| 9 | 17,5–21,0 s | expectativa | objeto grande: hoja que va de «Sep 17, 2026» a «Nov 19, 2026», con Tan | frontal | plano 2D | fija | papel plano | `Locked-off flat frontal calendar insert with Tan below, no camera movement` |
| 10 | 21,0–23,5 s | pico, sorpresa | abierto: Tan y Tin; cifra «4,811 days» (héroe principal) | frontal | plano 2D | fija; el contador sube y cae en tomate (objeto) | papel plano | `Locked-off flat frontal wide two-shot, no camera movement` |
| 11 | 23,5–25,5 s | asombro | medio cercano: Tan solo | frontal | plano 2D | fija | papel plano | `Locked-off flat frontal close medium shot of Tan alone, no camera movement` |
| 12 | 25,5–27,5 s | remate, ternura | abierto: Tan y Tin celebrando, con la tira | frontal | plano 2D | fija | papel plano | `Locked-off flat frontal wide two-shot, Tan left, Tin right, no camera movement` |
| 13 | 27,5–28,5 s | bucle | igual que la toma 1 | frontal | plano 2D | fija | papel plano | `Locked-off flat frontal frame, controller filling the frame, no camera movement` |

- **Motivos visuales que vuelven (1 o 2):** el mando (tomas 1, 2 y 13) y la hoja de calendario (3, 4, 9 y el calendario de la mano de Tin). Además la tira de 13 bloques (5 a 8 y 12) y el lápiz de Tin. Mismas formas y colores en todas.
- **Fondo que se mantiene entre planos de objeto:** el mismo papel crema, con el suelo en la misma línea (86 %) cada vez que hay personajes; el texto, arriba a la izquierda, siempre en la misma zona. Los planos de objeto (1, 3 y las tiras) no cambian de fondo.
- **Tipos de plano (videos de más de 20 s):** detalle: tomas 5 a 8. Héroe abierto: tomas 4, 10 y 12; el principal es la 10 (21,0 s), que cae hacia el 75 % del video y no hacia la mitad: es el pico de la cuenta, no un adorno; hacia la mitad (≈ 14 s) la toma es un detalle (la 7). Subjetivo: el mando a pantalla completa (1, 3 y 13). Revelado: la hoja que pasa de 2013 a 2026 (3) y la cifra que cae en 4,811 (10).
- **Referencias cargadas:** `canales/nostalgia-tin-y-tan/DESIGN.md`, `herramientas/palitos.py`, las hojas de `personajes/tin/referencias/` y `personajes/tan/referencias/`, y el short 1. No hay video de referencia.
- **Se resuelve en edición:** el `borrón` entre tomas (1→2, 2→3, 4→5, 8→9, 11→12 y 12→13); no hay zooms, cámara lenta ni reencuadre. No se pide ningún movimiento caro (órbita, FPV, dolly zoom), así que no hay versión segura que elegir.
- **Tomas encadenadas (último fotograma → primero):** no hay encadenado por keyframe porque no se genera video. El único empalme es la toma 13 → toma 1 (mismo plano, para el bucle). Eje: Tan siempre a la izquierda del cuadro y Tin a la derecha en todas las tomas con los dos (`DESIGN.md`); la 180° no se cruza.
- **Grabación propia:** no aplica; no hay grabación.

## 3b. Color con intención — director-de-fotografia

Esta sección manda sobre el bloque «Color con intención» de `02_prompt/prompt.md` (§12) en lo que difiera. Revisada con las hojas de contacto de `07_revision/vuelta_01/analisis/` (cada 0,5 s) y con `revisar_color.txt`. Fecha 2026-11-23.

- **Neutros (2):**
  - Papel `#F3E9D2`: fondo de todos los planos (con `#FFF8EC` en el cuerpo de la hoja y `#E6D8B8` en el suelo, que son variantes del mismo papel).
  - Tinta `#2B2420`: líneas, contornos de todo lo que sea acento y todo texto que no sea clave. Tinta sobre papel 12,6:1.
- **Acento (1): mostaza `#E8B33B`.** Va en la palabra clave y en **un** elemento por plano (el mando, la cabecera de la hoja, el bloque 13 o las marcas bisiestas), siempre con contorno de tinta de 0,06 em. No va en: texto que no sea clave, el suelo, la tira (marrón), los personajes ni la revelación. La bufanda de Tan y el lápiz son identidad, no acento.
- **Excepción declarada: tomate `#C8553D`.** En las tomas 10 a 12 (22,5–27,5 s, ≈ 5 s de 28,5) el acento es el tomate, en la cifra «4,811» y luego en «age 13» y el bloque 13. No se mezcla con la mostaza como acento dentro de un plano. Ver juicios abajo: cumple «un acento por plano», no «un acento por pieza».
- **Por qué esta paleta (hipótesis, no significado fijo):** papel crema y tinta marrón remiten a impresos y fotos de los 70 y 80; son cálidos y de saturación baja (≈ 17 % medido) para una nostalgia que, en el público de EE. UU. de 30 a 50 años que compró el juego en 2013, se lee como algo propio y no como retro de museo. Es la paleta del canal: no se inventó ningún color. La mostaza lleva el ojo a la cifra; el tomate, guardado para el final, cambia el tono justo cuando la cuenta llega a 4,811, para que ese número se sienta como un golpe y no como un dato más. Es una hipótesis: una sola pieza no permite separar el efecto del color del efecto de la cifra.
- **Cómo ayuda al objetivo:** presencia y línea base (canal nuevo, sin historial) → la misma paleta y el mismo acento mostaza que el short 1 hacen que el canal se reconozca entre Shorts, y el giro a tomate marca el pico → se verá con retención del segundo 1 al 3, visto frente a deslizado, y regreso de espectadores a 7 y 28 días. El cambio a tomate cae en los 22,5 s, lejos del tramo 1–3 s, así que no explica esa métrica; si la retención cae cerca de los 21–23 s, es una pista, no una prueba.
- **Riesgos de lectura:**
  1. Texto de 45 o más: todo texto corrido va en tinta (12,6:1). El acento es solo la clave, con contorno.
  2. Pantalla chica: cifras al 7 % del alto; con contorno de 0,06 em se leen por silueta.
  3. Daltonismo: el tomate y el marrón de la tira se parecen en luminosidad (≈ 1,7:1); en el bloque 13 de la toma 12 lo que lo distingue es el tono más su posición (último, a la derecha) y el texto «age 13» al lado. No se pide cambio.
  4. Rojo contra verde: la cabeza de Tan y el tomate no llevan información entre sí.
  5. Naranja de Tin (`#E07A2E`) y tomate son vecinos de tono en la toma 12; se distinguen porque el bloque va arriba y Tin abajo, y por el contorno.
- **Juicio 1, ¿el tomate rompe «2 neutros + 1 acento»?** Cumple la regla por plano y la de `DESIGN.md` («tomate solo como alerta o cifra final, con contorno»), pero **no cumple a la letra** la regla de un acento por pieza del manual 13 §2: hay dos colores de acento en 28,5 s. Lo acepto como excepción porque (a) está escrita en la paleta del canal desde el short 1, (b) cae en el giro de la pieza, (c) dentro de cada plano sigue habiendo un solo acento, y (d) cuesta rehacer la pieza para una ganancia que no se puede medir. Condición: en `ficha.json` el campo `acento` queda en mostaza y el tomate se nombra como excepción del giro (3 tomas), no se oculta. Si se quiere pureza en los próximos shorts, el pico se marca con tamaño y movimiento y no con otro tono.
- **Juicio 2, la bufanda mostaza de Tan junto al tomate (tomas 10, 11 y 12):** es identidad, y el manual 13 §2.4 dice que no cuenta como acento. Pero literalmente está en el mismo plano, y `DESIGN.md` y el prompt dicen «nunca en el mismo plano que la mostaza». En las hojas, el ojo va al número (grande, de color, con contorno) y no a la bufanda, que es una forma delgada; en la toma 11, con Tan más grande, es donde más pesa y aun así no compite. **No pido cambio de video.** Pido aclarar el texto en `DESIGN.md` y `prompt.md`: «nunca comparten plano como acento (la bufanda de Tan es identidad)». Eso es una edición de documentación, no un re-render.
- **Juicio 3, mostaza 1,6:1 y tomate 3,6:1 frente al mínimo 7:1:** el mínimo de 7:1 no se aplica al relleno de una clave, sino al texto y al contorno (manual 13 §5.2: se mide el contorno contra el fondo). Contorno de tinta contra papel 12,6:1: pasa. Tinta contra mostaza 8,0:1: pasa 7:1. Tinta contra tomate 3,5:1: **no pasa 7:1 ni 4,5:1**; pasa 3:1 de texto grande. Es el punto débil, y lo acepto porque el relleno de tomate es un color, no la información: la forma del dígito se lee por el contorno (12,6:1) y por su tamaño (7 % del alto, ≈ 134 px), y no hay texto corrido en tomate. No se oscurece el tomate: sería salirse de la paleta del canal sin ganancia clara.
- **Medido (`revisar_color.py`, 29 cuadros, `07_revision/vuelta_01/revisar_color.txt`):** ≈ 93 % del cuadro dentro de la paleta declarada (mínimo 85 %); saturación media ≈ 17 %, luminosidad ≈ 89 %; entre segundos ±2 % de luminosidad y ±2 % de saturación (máximo 15 %). La medición es global: no aísla las tomas 10 a 12, y el tomate no aparece entre los dominantes (mostaza 3,0 %). Contrastes: los de `prompt.md` §12, que recalculé a mano y coinciden (tinta/mostaza 7,95, tinta/tomate 3,5, tomate/papel 3,6). Falta la firma del supervisor de continuidad (control 8).

**Veredicto: APROBADO**, sin cambios de render. Documentación que no rehace la pieza: (1) en `ficha.json`, nombrar el tomate como excepción del giro (tomas 10–12) y dejar `acento` en mostaza; (2) en `DESIGN.md` y `prompt.md`, reescribir «nunca en el mismo plano que la mostaza» como «nunca como acento en el mismo plano (la bufanda de Tan es identidad)»; (3) que el supervisor mida por separado los cuadros de 21 a 27,5 s para confirmar el peso del tomate.

## 4. Actuación — director-de-animacion

| Toma | Personaje | Pose inicial (keyframe) | Anticipación → acción → pose final | Secundaria | Mirada | Panel de la hoja |
|---|---|---|---|---|---|---|
| 1 | | | | | | |

- **Frases de actuación (inglés), por toma:**
- **¿Hace falta grabar un clip propio para transferir movimiento?:**

## 5. Sonido — disenador-de-sonido

Lo que el audio ES (2026-11-23, medido; firma en `07_revision/vuelta_01/firma_sonido.md`: FIRMADO con salvedades, nadie lo ha oído). Hecho con código (`codigo/armar_dialogo.py`, `codigo/audio.py`), 0 créditos de audio nuevos; las voces son las del canal (Tan = Zelda, Tin = Kevin, `seed_audio`, `canales/nostalgia-tin-y-tan/voces.md`).

| Toma | Voz (texto exacto) | Efectos (segundo) | Música |
|---|---|---|---|
| 1 (0,0 a 1,0) | L1 Tan (0,00 a 1,93): «Remember buying G T A five at midnight?» | thunk y zumbido 0,0; botón 0,5 | patrón de 120 BPM, −24 LUFS, entra con el video |
| 2 (1,0 a 2,0) | sigue L1 | clic con borrón 1,0 | igual |
| 3 (2,0 a 5,0) | L2 Tan (2,16 a 5,12): «So, how many days did we wait for G T A six?» | clic con borrón 2,0; hoja 3,8; clic seco 5,0 | igual |
| 4 (5,0 a 9,0) | L3 Tin (5,35 a 8,83): «G T A five came out September seventeenth, twenty thirteen.» | ninguno (solo voz y música) | igual |
| 5 (9,0 a 11,0) | L4 Tin (9,06 a 13,64): «Thirteen years times three sixty-five: four thousand, seven hundred forty-five days.» | clic con borrón 9,0; 13 bloques de 9,2 a 10,4 (cada 0,1) | igual |
| 6 (11,0 a 13,5) | sigue L4 (2.º tramo en 11,13) | tictac del contador 11,15 | igual |
| 7 (13,5 a 15,0) | L5 Tin (13,87 a 17,54): «Add three leap days: four thousand, seven hundred forty-eight.» | pop 13,9; 14,2; 14,5; clic seco 15,0 | igual |
| 8 (15,0 a 17,5) | sigue L5 (2.º tramo en 15,26) | tictac 15,38 | igual |
| 9 (17,5 a 21,0) | L6 Tin (17,77 a 21,15): «Plus sixty-three days: September seventeenth to November nineteenth.» | clic con borrón 17,5; 6 hojas cortas de 17,56 a 18,46 (cada 0,18); hoja 19,4; clic seco 21,0 | igual |
| 10 (21,0 a 23,5) | L7 Tin (21,38 a 23,56): «Four thousand, eight hundred eleven days.» | tictac 21,4; ding 22,5; clic seco 23,5 | igual |
| 11 (23,5 a 25,5) | L8 Tan (23,79 a 25,27): «Wow, that long?» | silencio de efectos (solo voz y música); clic con borrón 25,5 | igual |
| 12 (25,5 a 27,5) | L9 Tin (25,50 a 27,33): «A baby born that day is a teenager now.» | pop grave 26,0; 26,5; 27,0 | igual; la voz acaba y la música sigue sola 170 ms |
| 13 (27,5 a 28,5) | sin voz | clic con borrón, whoosh y botón 27,5; botón 28,0 | cierra en el pulso; el thunk de 0,0 abre el bucle |

- **Lista de golpes** (47 golpes medidos; cada uno empieza en su segundo, ≤ 1 ms):

| Segundo | Qué pasa en imagen | Sonido |
|---|---|---|
| 0,0 | arranque, mando que retumba | thunk + zumbido (golpe seco, a propósito) |
| 0,5 | latido del botón | boton |
| 1,0 / 2,0 / 9,0 / 17,5 / 25,5 / 27,5 | corte con borrón | clic_borron |
| 5,0 / 15,0 / 21,0 / 23,5 | corte seco | clic |
| 3,8 / 19,4 | vuelta de hoja | hoja |
| 9,2 a 10,4 (13 pasos de 0,1) | bloque que se llena | bloque_0 a bloque_12 |
| 11,15 / 15,38 / 21,4 | contador que sube | tictac_4745 / tictac_4748 / tictac_4811 |
| 13,9 / 14,2 / 14,5 | marca bisiesta | pop |
| 17,56 a 18,46 (6, cada 0,18) | hoja en blanco | hoja_corta |
| 22,5 | llega a 4,811 | ding |
| 26,0 / 26,5 / 27,0 | latido del bloque 13 | pop_grave |
| 27,5 / 28,0 | retroceso de cámara y latido del botón | whoosh (27,5), boton (27,5 y 28,0) |

- **Voz en off o labios:** voz en off de dos personajes de palitos sin boca animada (Tan, Zelda; Tin, Kevin); un solo clip generado por voz (3 créditos en total, ya gastados), `atempo=1,10`, cada voz a −14 LUFS. Empieza en el fotograma 0.
- **Música:** hecha con código, patrón de 120 BPM (el pulso de 0,5 s de la rejilla), −24 LUFS, 28,5 s, 57 pulsos; sin material de terceros ni del juego (`licencias.md`). Si el dueño prefiere música licenciada, se pone dentro de la app al publicar.
- **Mezcla medida:** −14,0 LUFS, pico real −1,3 dBTP, LRA 1,9 LU; voz/fondo por línea de 5,8 a 8,6 dB; el guion se sigue reconociendo con el fondo +18 dB (se rompe a +24).
- **Pendiente solo al oído:** el final de «now» (la grabación llega cortada; fundido de 120 ms), el ataque de «eight» en 22,23 s, pronunciación de «G T A» y de las cifras, y las pausas acortadas (0,08 a 0,11 s).

## 6. Montaje y salida — editor-de-video

- **Mapa de ritmo:** (tramos densos y respiros de 2–3 s; nunca pulso plano; acelera hacia el final y remata con el plano del inicio)

| Tramo | Segundos | Densidad (cambios) | Qué pasa |
|---|---|---|---|
| | | | |

- **Orden y duración de tomas:**
- **Cortes y transiciones:**
- **Loop:**
- **Subtítulos y texto en pantalla:**
- **Color:**
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
