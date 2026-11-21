# Definición de generación de los clips — Hola, granja (16 tomas, borrador 480p)

- **Estado:** PENDIENTE
- **Costo total cotizado:** 44 créditos (88 s × 0,5; clips a 480p, sin audio, un intento por toma)
- **Autorizado por el dueño:** no

<!--
Estado: PENDIENTE → REVISADA POR EL EQUIPO → AUTORIZADA. Solo con AUTORIZADA se genera.
Una pieza por toma. Cada pieza se genera una sola vez (video-studio/generacion.md): si no cumple,
no se repite; se informa al dueño y a qué costo se rehacería.
Cotización (coordinación, Higgsfield, 2026-11-21): seedance_2_0_mini, imagen→video, 16:9, 480p, sin audio.
4 s = 2 créditos · 5 s = 2,5 · 6 s = 3 · 7 s = 3,5 (0,5 por segundo). Total 88 s = 44 créditos.
No entra en esta autorización: el remate a 720p (1 crédito por segundo), la música ni la voz.
Antes de enviar cada toma se vuelve a cotizar y se compara con lo autorizado (generacion.md, sección 2).
Medidas de composición: fracciones del ancho y del alto del cuadro (1376×768) leídas sobre los cuatro
PNG de 03_keyframes/. Son estimaciones visuales con tolerancia de ±3 %, no mediciones con instrumento.
Los clips se guardan en 04_clips/borradores/toma_NN_480p.mp4 y, si cumplen, se copian a seleccionados/.
-->

## Resumen de las 16 piezas

| Toma | Segundos | Costo | Imagen de partida | Depende de |
|---|---|---|---|---|
| 1 Entrada al patio | 5 | 2,5 | Keyframe C-entrada | — |
| 2 Saludo a cámara | 5 | 2,5 | Último fotograma de la toma 1 | 1 |
| 3 Lumi dice hola | 7 | 3,5 | Keyframe B | — |
| 4 Tiky saluda hacia un lado | 6 | 3 | Keyframe C | — |
| 5 Tiky saluda a Lumi y ella contesta | 7 | 3,5 | Keyframe C | — |
| 6 Tiky pregunta con el ala | 7 | 3,5 | Keyframe A | — |
| 7 Tiky espera | 5 | 2,5 | Último fotograma de la toma 6 | 6 |
| 8 Tiky responde hola | 6 | 3 | Último fotograma de la toma 7 | 7 (y 6) |
| 9 Lumi pregunta con la pezuña | 7 | 3,5 | Keyframe B | — |
| 10 Lumi espera | 5 | 2,5 | Último fotograma de la toma 9 | 9 |
| 11 Lumi responde hola | 6 | 3 | Último fotograma de la toma 10 | 10 (y 9) |
| 12 Caminan a su lugar | 4 | 2 | Keyframe C-entrada | — |
| 13 Quietos en su lugar | 4 | 2 | Último fotograma de la toma 12 | 12 |
| 14 Espera viva con el adulto 1 | 4 | 2 | Keyframe C | — |
| 15 Espera viva con el adulto 2 | 4 | 2 | Último fotograma de la toma 14 | 14 |
| 16 Despedida | 6 | 3 | Keyframe C | — |
| **Total** | **88** | **44** | | |

## Listas comunes

Se aplican a cada pieza que las cita en «Debe verse» y «No debe verse». Vienen de las fichas
(`personajes/tiky/ficha.md`, `personajes/lumi/ficha.md`) y del entorno (`series/granja/entorno.md`).

**[T] Tiky debe verse:** cuerpo de huevo sin cuello · amarillo con panza crema · copete de 3 plumas rojo anaranjado, discreto, la del centro más alta · ojos marrón oscuro con un brillo blanco · sin cejas · pico coral pequeño · mejillas rosadas · dos alas (nunca manos) pegadas a los lados · dos patas coral de tres dedos · sin ropa ni objetos · le llega a Lumi a los ojos con el copete.

**[L] Lumi debe verse:** cuerpo de huevo sin cuello · blanco crema con dos manchas negras (una cruza panza y espalda, otra sobre la cabeza entre los cuernos; ninguna alrededor de los ojos) · crayón lila corto y grueso detrás de la oreja derecha (a la izquierda de quien mira), apoyado sobre la mancha negra de la cabeza, entero y visible siempre · dos cuernos crema pequeños y redondeados · orejas caídas con interior lila · ojos miel con un brillo blanco · cejas suaves · hocico lila ancho con dos puntos · antebrazos y parte baja de las patas negros como calcetines · cuatro pezuñas lila · sin cencerro, flor ni bombilla · es la más alta.

**[P] Patio debe verse:** granero rojo de madera con vetas verticales a la izquierda, con el techo blanco tal como lo muestra la imagen de partida (el techo aprobado tiene un quiebre a cada lado; el clip no lo cambia) · puerta rectangular abierta y oscura y una sola abertura cuadrada encima · cerca baja blanca de postes redondeados y dos travesaños detrás de los personajes · fieltro verde claro liso · pared azul cielo pastel lisa con zócalo blanco · luz de día pareja desde arriba a la izquierda, sombras suaves, sin cambios de luz durante la toma.

**[N-comunes] No debe verse en ninguna toma:** texto, letras, rótulos, marca de agua, logo · otros personajes, animales, humanos o manos humanas · objetos en las manos de nadie · algo que salga o se mueva dentro de la puerta del granero · zoom, paneo, acercamiento, sacudida, corte o cambio de cámara · movimiento rápido, desenfoque de movimiento, destellos o parpadeos de luz · caras que asustan, dientes a la vista · noche, sombras oscuras, fuego, armas · el crayón de Lumi usado para marcar o dibujar (M1) · música o sonido (el clip no lleva audio) · un último fotograma distinto del que describe la acción.

**[N-T] Tiky, no debe verse:** copete grande, esponjado o brillante (fallo conocido) · más alto de lo debido junto a Lumi (fallo conocido: casi tan alto como ella) · ropa, accesorios, cejas, ojos verdes, aspecto adulto o punk · manos en lugar de alas · patas con menos de tres dedos o una sola pata · pico o patas naranja en lugar de coral.

**[N-L] Lumi, no debe verse:** crayón omitido, en la oreja izquierda o fuera de la cabeza (fallo conocido) · antebrazos blancos o claros · pezuñas que no sean lila · cuerpo mayormente negro, manchas alrededor de los ojos, una tercera mancha · hocico rosado, cencerro, campana, flor, bombilla o brillo de «idea» · pezuña que llegue al mentón o a la boca · parecerse a una vaca conocida de la animación infantil.

**[N-P] Patio, no debe verse:** ventana en la pared, sobre todo a la derecha (fallo conocido del patio) · cuadros, enchufes, letreros, veleta · animales o cosas dentro del granero · techo del granero que cambie de forma respecto de la imagen de partida (el techo aprobado tiene un quiebre por lado; no debe alisarse, duplicarse ni moverse) · flores o piedras en el fieltro · objetos nuevos o fuera de lugar en el patio · cambios de luz o de color de la pared.

## Piezas

### Toma 01 — Entrada al patio

- **Tipo:** clip (imagen→video)
- **Modelo y ajustes:** `seedance_2_0_mini`, imagen→video, 16:9, 480p, sin audio, 5 s
- **Costo cotizado:** 2,5 créditos (5 s × 0,5)
- **Imagen de partida:** Keyframe C-entrada, ID `83e54673-d116-47dc-bcb0-051ede05f51c` (`03_keyframes/keyframe_C_entrada.png`). Se sube como imagen de partida del clip (no se sube otra referencia). La misma imagen arranca también la toma 12.
- **Depende de:** Ninguna (no encadenada).
- **Personajes:** @tiky y @lumi; Lumi mide una vez y media la altura de Tiky (a Tiky el copete le llega a los ojos de Lumi), Lumi a la izquierda.
- **Lugar:** patio (`series/granja/entorno.md`), referencia `series/granja/referencias/patio.png`; el patio sale de la imagen de partida, no se describe de nuevo en el clip.
- **Composición:** Encuadre C-entrada (la del keyframe C-entrada, no cambia). Cámara fija a la altura de los ojos de Tiky, de frente. Los dos pequeños y al fondo, junto a la cerca: Lumi a la izquierda (del 32 % al 50 % del ancho, cuernos hacia el 34 % del alto, pezuñas hacia el 81 %) y Tiky a su derecha (del 52 % al 67 %, copete hacia el 43 %, dedos hacia el 81 %). Granero a la izquierda (del 0 % al 33 % del ancho); gran tramo de fieltro verde delante de ellos, por donde caminan hacia cámara. Cámara fija durante los 5 s: sin zoom, sin paneo, sin corte.
- **Debe verse:** [T] [L] [P] (listas en «Listas comunes») + **acción (5 s):** Caminan despacio hacia cámara, uno al lado del otro, Lumi a la izquierda, con pasos pequeños y parejos, de 0 a 4 s. Se detienen en el centro del patio, miran a cámara y quedan quietos en el último segundo (4 a 5 s). La voz «Esta es la granja» entra hacia el s 4: en ese momento ya están quietos y sin gesto. Terminan de cuerpo entero, de frente, alas y antebrazos abajo.
- **No debe verse:** [N-comunes] [N-T] [N-L] [N-P] + Tropiezos, choques, caídas, carrera o saltos; que uno pase por delante del otro. Que lleguen a cámara tan grandes que se pierda el encuadre. Gestos de saludo antes del s 4 (el saludo es en la toma 2). Música, sonido y cualquier cambio del granero.
- **Prompt:** el bloque «Prompt de video» de la **Toma 1** en `02_prompt/prompt.md` (copia idéntica archivada en `personajes/tiky/prompts/capitulos/granja_cap01_hola_granja.md`), pegado completo y sin cambios. Empieza con las cuatro líneas CRITICAL (sin palabras escritas, mismo diseño, cámara fija sin corte, nada en la puerta del granero) y sigue con la acción, «Fixed camera, no zoom, no pan.» y el estilo global.

### Toma 02 — Saludo a cámara

- **Tipo:** clip (imagen→video)
- **Modelo y ajustes:** `seedance_2_0_mini`, imagen→video, 16:9, 480p, sin audio, 5 s
- **Costo cotizado:** 2,5 créditos (5 s × 0,5)
- **Imagen de partida:** Último fotograma del clip de la toma 1: se extrae con ffmpeg del clip aprobado de la toma 1 (`ffmpeg -sseof -0.1 -i <clip_toma_01.mp4> -frames:v 1 -update 1 ultimo_toma_01.png`) y se sube como imagen de partida. Depende de la toma 1: no se puede pedir hasta que esa toma esté generada y cumpla su definición.
- **Depende de:** Toma 1 (cadena 1 → 2).
- **Personajes:** @tiky y @lumi; Lumi mide una vez y media la altura de Tiky (a Tiky el copete le llega a los ojos de Lumi), Lumi a la izquierda.
- **Lugar:** patio (`series/granja/entorno.md`), referencia `series/granja/referencias/patio.png`; el patio sale de la imagen de partida, no se describe de nuevo en el clip.
- **Composición:** La del último fotograma de la toma 1: los dos de frente en el centro del patio, mirando a cámara, en el tamaño y la posición con que salgan al final de la toma 1 (no medibles antes de generarla; esa toma fija el encuadre de toda la cadena). Misma cámara, mismo tamaño y misma posición entre tomas, sin saltos. Cámara fija durante los 5 s: sin zoom, sin paneo, sin corte.
- **Debe verse:** [T] [L] [P] (listas en «Listas comunes») + **acción (5 s):** Parten de la pose final de la toma 1. Miran a cámara. Hacia el s 1,5 Tiky levanta el ala izquierda (la de la derecha del cuadro) y Lumi la pezuña derecha a la vez, despacio; cada uno la mueve dos veces con movimientos pequeños (el segundo movimiento cae entre los s 2 y 3, donde va «Hola»); del s 3 al 5 los dos mantienen el ala y la pezuña en alto, mirando a cámara. El último fotograma (miniatura, criterio C2) muestra a los dos de cuerpo completo, de frente, con el ala y la pezuña en alto.
- **No debe verse:** [N-comunes] [N-T] [N-L] [N-P] + Aleteo de vuelo o golpes de pezuña; sacudidas. Que el ala o la pezuña toque el pico, la boca o el mentón. Que bajen antes del s 5 (deben quedar en alto 2 s). Salto de luz, posición o tamaño respecto del último fotograma de la toma 1.
- **Prompt:** el bloque «Prompt de video» de la **Toma 2** en `02_prompt/prompt.md` (copia idéntica archivada en `personajes/tiky/prompts/capitulos/granja_cap01_hola_granja.md`), pegado completo y sin cambios. Empieza con las cuatro líneas CRITICAL (sin palabras escritas, mismo diseño, cámara fija sin corte, nada en la puerta del granero) y sigue con la acción, «Fixed camera, no zoom, no pan.» y el estilo global.

### Toma 03 — Lumi dice hola

- **Tipo:** clip (imagen→video)
- **Modelo y ajustes:** `seedance_2_0_mini`, imagen→video, 16:9, 480p, sin audio, 7 s
- **Costo cotizado:** 3,5 créditos (7 s × 0,5)
- **Imagen de partida:** Keyframe B, ID `cef6a8ab-e934-4e05-a0d3-94ab263be1a9` (`03_keyframes/keyframe_B_lumi.png`). Se sube como imagen de partida del clip (no se sube otra referencia). La misma imagen arranca también la toma 9.
- **Depende de:** Ninguna (no encadenada).
- **Personajes:** @lumi sola.
- **Lugar:** patio (`series/granja/entorno.md`), referencia `series/granja/referencias/patio.png`; el patio sale de la imagen de partida, no se describe de nuevo en el clip.
- **Composición:** Encuadre B (la del keyframe B, no cambia). Cámara fija a la altura de los ojos de Tiky, de frente. Lumi sola, de cuerpo entero (el keyframe B salió de cuerpo entero, no en plano medio), centrada: cuerpo del 36 % al 64 % del ancho, puntas de los cuernos hacia el 20 % del alto, ojos hacia el 34 %, hocico hacia el 43 %, pezuñas traseras hacia el 93 %. Los antebrazos negros con la pezuña lila cuelgan a ambos lados del tronco (hacia el 68 % del alto). Granero a la izquierda (del 0 % al 40 % del ancho); a la derecha, cerca, pared y fieltro. Cámara fija durante los 7 s: sin zoom, sin paneo, sin corte.
- **Debe verse:** [L] [P] (listas en «Listas comunes») + **acción (7 s):** Lumi mira a cámara con sonrisa leve (de 0 a 1 s, sin gesto: ahí va el «muu»). Levanta la pezuña derecha despacio, la mueve dos veces con movimientos pequeños (segundo movimiento entre los s 3,5 y 4,5, donde va «hola») y baja la pezuña despacio hacia el s 5,5. Sigue mirando a cámara con sonrisa suave hasta el s 7. Los dos antebrazos negros con pezuña lila siempre enteros y a la vista.
- **No debe verse:** [N-comunes] [N-L] [N-P] + Cara seria, fría, con ceño fruncido, ojos muy abiertos o dientes a la vista. Pezuña que suba al mentón o a la boca, golpe de pezuña. Lumi que se acerque a cámara o cambie de tamaño. Que el crayón desaparezca o cambie de oreja durante el gesto. Antebrazos que se vuelvan blancos o claros.
- **Prompt:** el bloque «Prompt de video» de la **Toma 3** en `02_prompt/prompt.md` (copia idéntica archivada en `personajes/tiky/prompts/capitulos/granja_cap01_hola_granja.md`), pegado completo y sin cambios. Empieza con las cuatro líneas CRITICAL (sin palabras escritas, mismo diseño, cámara fija sin corte, nada en la puerta del granero) y sigue con la acción, «Fixed camera, no zoom, no pan.» y el estilo global.

### Toma 04 — Tiky saluda hacia un lado

- **Tipo:** clip (imagen→video)
- **Modelo y ajustes:** `seedance_2_0_mini`, imagen→video, 16:9, 480p, sin audio, 6 s
- **Costo cotizado:** 3 créditos (6 s × 0,5)
- **Imagen de partida:** Keyframe C, ID `b7fc0c43-4acc-40f1-9b0f-ea377f2012ed` (`03_keyframes/keyframe_C_los_dos.png`). Se sube como imagen de partida del clip (no se sube otra referencia). La misma imagen arranca también las tomas 5, 14 y 16.
- **Depende de:** Ninguna (no encadenada).
- **Personajes:** @tiky y @lumi; Lumi mide una vez y media la altura de Tiky (a Tiky el copete le llega a los ojos de Lumi), Lumi a la izquierda.
- **Lugar:** patio (`series/granja/entorno.md`), referencia `series/granja/referencias/patio.png`; el patio sale de la imagen de partida, no se describe de nuevo en el clip.
- **Composición:** Encuadre C (la del keyframe C, no cambia). Cámara fija a la altura de los ojos de Tiky, de frente. Lumi a la izquierda (cuerpo del 23 % al 50 % del ancho, cuernos hacia el 20 % del alto, pezuñas hacia el 91 %) y Tiky a su derecha (del 52 % al 75 %, punta del copete hacia el 33 %, dedos hacia el 91 %); Tiky le llega a Lumi a los ojos con el copete. Granero a la izquierda (del 0 % al 33 % del ancho), cerca baja detrás de los dos, de lado a lado. Cámara fija durante los 6 s: sin zoom, sin paneo, sin corte.
- **Debe verse:** [T] [L] [P] (listas en «Listas comunes») + **acción (6 s):** Tiky mira hacia un lado, no a Lumi; levanta el ala izquierda (la de la derecha del cuadro), hace un solo movimiento pequeño y corto, y la baja (el «pío» cae hacia el s 1). Lumi, a la izquierda, lo mira tranquila y atenta, con la cabeza un poco inclinada y la cara relajada, sin cambiar de pose: no levanta la pezuña, no se aleja, no le da la espalda. Los dos terminan juntos en su sitio.
- **No debe verse:** [N-comunes] [N-T] [N-L] [N-P] + Que Tiky se gire de golpe. Que Tiky mire a Lumi o la salude (aquí mira a otro lado). Que Lumi se vea seria, fría, con ceño fruncido, que le dé la espalda, que se aleje o que levante la pezuña y responda. Aleteo de Tiky. Que el ala toque el pico. Ver pregunta 8 sobre «su derecha».
- **Prompt:** el bloque «Prompt de video» de la **Toma 4** en `02_prompt/prompt.md` (copia idéntica archivada en `personajes/tiky/prompts/capitulos/granja_cap01_hola_granja.md`), pegado completo y sin cambios. Empieza con las cuatro líneas CRITICAL (sin palabras escritas, mismo diseño, cámara fija sin corte, nada en la puerta del granero) y sigue con la acción, «Fixed camera, no zoom, no pan.» y el estilo global.

### Toma 05 — Tiky saluda a Lumi y ella contesta

- **Tipo:** clip (imagen→video)
- **Modelo y ajustes:** `seedance_2_0_mini`, imagen→video, 16:9, 480p, sin audio, 7 s
- **Costo cotizado:** 3,5 créditos (7 s × 0,5)
- **Imagen de partida:** Keyframe C, ID `b7fc0c43-4acc-40f1-9b0f-ea377f2012ed` (`03_keyframes/keyframe_C_los_dos.png`). Se sube como imagen de partida del clip (no se sube otra referencia). La misma imagen arranca también las tomas 4, 14 y 16.
- **Depende de:** Ninguna (no encadenada).
- **Personajes:** @tiky y @lumi; Lumi mide una vez y media la altura de Tiky (a Tiky el copete le llega a los ojos de Lumi), Lumi a la izquierda.
- **Lugar:** patio (`series/granja/entorno.md`), referencia `series/granja/referencias/patio.png`; el patio sale de la imagen de partida, no se describe de nuevo en el clip.
- **Composición:** Encuadre C (la del keyframe C, no cambia). Cámara fija a la altura de los ojos de Tiky, de frente. Lumi a la izquierda (cuerpo del 23 % al 50 % del ancho, cuernos hacia el 20 % del alto, pezuñas hacia el 91 %) y Tiky a su derecha (del 52 % al 75 %, punta del copete hacia el 33 %, dedos hacia el 91 %); Tiky le llega a Lumi a los ojos con el copete. Granero a la izquierda (del 0 % al 33 % del ancho), cerca baja detrás de los dos, de lado a lado. Cámara fija durante los 7 s: sin zoom, sin paneo, sin corte.
- **Debe verse:** [T] [L] [P] (listas en «Listas comunes») + **acción (7 s):** Tiky gira hacia Lumi con un giro lento (no de golpe) y la mira (pío hacia el s 1,2). Levanta el ala izquierda (la de la derecha del cuadro), la mueve despacio y la baja. Lumi lo mira, levanta la pezuña derecha, la mueve despacio (el «muu» cae hacia el s 3,2) y la baja hacia el s 4,5. Del s 4,5 al 7 los dos se miran con sonrisas suaves, quietos (la voz «Tiky saludó a Lumi.» va de 5 a 7 s con ambos ya sin gesto).
- **No debe verse:** [N-comunes] [N-T] [N-L] [N-P] + Giro brusco de Tiky al mirar a Lumi. Aleteo de Tiky o golpe de pezuña de Lumi. Que la pezuña o el ala suba a la boca, al pico o al mentón. Que Lumi responda antes de que Tiky termine de saludar. Que uno de los dos se mueva de su lugar o cambien de tamaño.
- **Prompt:** el bloque «Prompt de video» de la **Toma 5** en `02_prompt/prompt.md` (copia idéntica archivada en `personajes/tiky/prompts/capitulos/granja_cap01_hola_granja.md`), pegado completo y sin cambios. Empieza con las cuatro líneas CRITICAL (sin palabras escritas, mismo diseño, cámara fija sin corte, nada en la puerta del granero) y sigue con la acción, «Fixed camera, no zoom, no pan.» y el estilo global.

### Toma 06 — Tiky pregunta con el ala

- **Tipo:** clip (imagen→video)
- **Modelo y ajustes:** `seedance_2_0_mini`, imagen→video, 16:9, 480p, sin audio, 7 s
- **Costo cotizado:** 3,5 créditos (7 s × 0,5)
- **Imagen de partida:** Keyframe A, ID `0b4b497b-8dc2-4441-8fd0-d6e151ac6a22` (`03_keyframes/keyframe_A_tiky.png`). Se sube como imagen de partida del clip (no se sube otra referencia). Solo arranca esta toma.
- **Depende de:** Ninguna (no encadenada).
- **Personajes:** @tiky solo.
- **Lugar:** patio (`series/granja/entorno.md`), referencia `series/granja/referencias/patio.png`; el patio sale de la imagen de partida, no se describe de nuevo en el clip.
- **Composición:** Encuadre A (la del keyframe A, no cambia). Cámara fija a la altura de los ojos de Tiky, de frente. Tiky solo, de cuerpo completo, centrado: cuerpo del 40 % al 60 % del ancho, punta del copete hacia el 25 % del alto, ojos hacia el 50 %, base de los dedos hacia el 92 %. Granero a la izquierda (del 4 % al 46 % del ancho; el cuerpo de Tiky roza su borde derecho); a la derecha solo cerca blanca, pared y fieltro. Cámara fija durante los 7 s: sin zoom, sin paneo, sin corte.
- **Debe verse:** [T] [P] (listas en «Listas comunes») + **acción (7 s):** De 0 a 2 s Tiky mira su ala izquierda (la de la derecha del cuadro), mira a cámara y vuelve a mirar su ala, con giros suaves de la cabeza. De 2 a 4 s levanta el ala izquierda (la de la derecha del cuadro) despacio y la mueve dos veces (el «hola» cae sobre el saludo). Desde el s 4 mira a cámara, baja el ala despacio y espera con el ala abajo, mirando a cámara, hasta el s 7. El último fotograma tiene el ala abajo y la mirada a cámara (la toma 7 parte de él).
- **No debe verse:** [N-comunes] [N-T] [N-P] + Giros bruscos de la cabeza al mirar el ala y a cámara. Aleteo (el ala debe subir y moverse despacio, dos veces). Que el ala suba al pico. Que Tiky cambie de lugar o de tamaño. Que el ala no quede abajo al final de la toma. Granero tapado por Tiky más de lo que muestra el keyframe A.
- **Prompt:** el bloque «Prompt de video» de la **Toma 6** en `02_prompt/prompt.md` (copia idéntica archivada en `personajes/tiky/prompts/capitulos/granja_cap01_hola_granja.md`), pegado completo y sin cambios. Empieza con las cuatro líneas CRITICAL (sin palabras escritas, mismo diseño, cámara fija sin corte, nada en la puerta del granero) y sigue con la acción, «Fixed camera, no zoom, no pan.» y el estilo global.

### Toma 07 — Tiky espera (pausa viva)

- **Tipo:** clip (imagen→video)
- **Modelo y ajustes:** `seedance_2_0_mini`, imagen→video, 16:9, 480p, sin audio, 5 s
- **Costo cotizado:** 2,5 créditos (5 s × 0,5)
- **Imagen de partida:** Último fotograma del clip de la toma 6: se extrae con ffmpeg del clip aprobado de la toma 6 (`ffmpeg -sseof -0.1 -i <clip_toma_06.mp4> -frames:v 1 -update 1 ultimo_toma_06.png`) y se sube como imagen de partida. Depende de la toma 6: no se puede pedir hasta que esa toma esté generada y cumpla su definición.
- **Depende de:** Toma 6 (cadena 6 → 7).
- **Personajes:** @tiky solo.
- **Lugar:** patio (`series/granja/entorno.md`), referencia `series/granja/referencias/patio.png`; el patio sale de la imagen de partida, no se describe de nuevo en el clip.
- **Composición:** La del último fotograma de la toma 6, que mantiene el Encuadre A del keyframe de la toma 6: misma cámara, mismo tamaño y misma posición, sin saltos. Encuadre A (la del keyframe A, no cambia). Cámara fija a la altura de los ojos de Tiky, de frente. Tiky solo, de cuerpo completo, centrado: cuerpo del 40 % al 60 % del ancho, punta del copete hacia el 25 % del alto, ojos hacia el 50 %, base de los dedos hacia el 92 %. Granero a la izquierda (del 4 % al 46 % del ancho; el cuerpo de Tiky roza su borde derecho); a la derecha solo cerca blanca, pared y fieltro. Cámara fija durante los 5 s: sin zoom, sin paneo, sin corte.
- **Debe verse:** [T] [P] (listas en «Listas comunes») + **acción (5 s):** Parte del último fotograma de la toma 6: Tiky de frente, ala abajo, mirando a cámara. Durante 5 s: parpadea dos veces, respira suave (el cuerpo sube y baja apenas), sonríe levemente y ladea un poco la cabeza. Las alas siguen abajo todo el tiempo. Hay movimiento vivo pero ningún gesto nuevo; no hay fotograma idéntico durante toda la toma.
- **No debe verse:** [N-comunes] [N-T] [N-P] + Imagen congelada o ningún parpadeo. Que Tiky haga un gesto nuevo (levantar el ala, dar un paso, girar). Que el ala o el cuerpo salten respecto del último fotograma de la toma 6 (luz, posición, tamaño). Cámara que se acerque.
- **Prompt:** el bloque «Prompt de video» de la **Toma 7** en `02_prompt/prompt.md` (copia idéntica archivada en `personajes/tiky/prompts/capitulos/granja_cap01_hola_granja.md`), pegado completo y sin cambios. Empieza con las cuatro líneas CRITICAL (sin palabras escritas, mismo diseño, cámara fija sin corte, nada en la puerta del granero) y sigue con la acción, «Fixed camera, no zoom, no pan.» y el estilo global.

### Toma 08 — Tiky responde hola

- **Tipo:** clip (imagen→video)
- **Modelo y ajustes:** `seedance_2_0_mini`, imagen→video, 16:9, 480p, sin audio, 6 s
- **Costo cotizado:** 3 créditos (6 s × 0,5)
- **Imagen de partida:** Último fotograma del clip de la toma 7: se extrae con ffmpeg del clip aprobado de la toma 7 (`ffmpeg -sseof -0.1 -i <clip_toma_07.mp4> -frames:v 1 -update 1 ultimo_toma_07.png`) y se sube como imagen de partida. Depende de la toma 7: no se puede pedir hasta que esa toma esté generada y cumpla su definición.
- **Depende de:** Toma 7 (cadena 6 → 7 → 8).
- **Personajes:** @tiky solo.
- **Lugar:** patio (`series/granja/entorno.md`), referencia `series/granja/referencias/patio.png`; el patio sale de la imagen de partida, no se describe de nuevo en el clip.
- **Composición:** La del último fotograma de la toma 7, que mantiene el Encuadre A del keyframe de la toma 6: misma cámara, mismo tamaño y misma posición, sin saltos. Encuadre A (la del keyframe A, no cambia). Cámara fija a la altura de los ojos de Tiky, de frente. Tiky solo, de cuerpo completo, centrado: cuerpo del 40 % al 60 % del ancho, punta del copete hacia el 25 % del alto, ojos hacia el 50 %, base de los dedos hacia el 92 %. Granero a la izquierda (del 4 % al 46 % del ancho; el cuerpo de Tiky roza su borde derecho); a la derecha solo cerca blanca, pared y fieltro. Cámara fija durante los 6 s: sin zoom, sin paneo, sin corte.
- **Debe verse:** [T] [P] (listas en «Listas comunes») + **acción (6 s):** Parte del último fotograma de la toma 7: ala abajo, mirando a cámara. Hacia el s 1 levanta el ala izquierda (la de la derecha del cuadro) despacio y la mueve dos veces con movimientos pequeños (el «hola» cae entre los s 2 y 3 con el ala en alto); la baja hacia el s 4 y sonríe en silencio a cámara hasta el s 6. El «pío» de 0 a 1 s es de montaje: Tiky no hace gesto de boca exagerado.
- **No debe verse:** [N-comunes] [N-T] [N-P] + Aleteo de vuelo; saludo apurado (el ala debe tardar en subir y bajar, dos movimientos, en 3 s). Ala al pico. Salto de luz, posición o tamaño respecto de la toma 7. Que el ala baje antes del s 3.
- **Prompt:** el bloque «Prompt de video» de la **Toma 8** en `02_prompt/prompt.md` (copia idéntica archivada en `personajes/tiky/prompts/capitulos/granja_cap01_hola_granja.md`), pegado completo y sin cambios. Empieza con las cuatro líneas CRITICAL (sin palabras escritas, mismo diseño, cámara fija sin corte, nada en la puerta del granero) y sigue con la acción, «Fixed camera, no zoom, no pan.» y el estilo global.

### Toma 09 — Lumi pregunta con la pezuña

- **Tipo:** clip (imagen→video)
- **Modelo y ajustes:** `seedance_2_0_mini`, imagen→video, 16:9, 480p, sin audio, 7 s
- **Costo cotizado:** 3,5 créditos (7 s × 0,5)
- **Imagen de partida:** Keyframe B, ID `cef6a8ab-e934-4e05-a0d3-94ab263be1a9` (`03_keyframes/keyframe_B_lumi.png`). Se sube como imagen de partida del clip (no se sube otra referencia). La misma imagen arranca también la toma 3.
- **Depende de:** Ninguna (no encadenada).
- **Personajes:** @lumi sola.
- **Lugar:** patio (`series/granja/entorno.md`), referencia `series/granja/referencias/patio.png`; el patio sale de la imagen de partida, no se describe de nuevo en el clip.
- **Composición:** Encuadre B (la del keyframe B, no cambia). Cámara fija a la altura de los ojos de Tiky, de frente. Lumi sola, de cuerpo entero (el keyframe B salió de cuerpo entero, no en plano medio), centrada: cuerpo del 36 % al 64 % del ancho, puntas de los cuernos hacia el 20 % del alto, ojos hacia el 34 %, hocico hacia el 43 %, pezuñas traseras hacia el 93 %. Los antebrazos negros con la pezuña lila cuelgan a ambos lados del tronco (hacia el 68 % del alto). Granero a la izquierda (del 0 % al 40 % del ancho); a la derecha, cerca, pared y fieltro. Cámara fija durante los 7 s: sin zoom, sin paneo, sin corte.
- **Debe verse:** [L] [P] (listas en «Listas comunes») + **acción (7 s):** De 0 a 2 s Lumi mira su pezuña derecha, mira a cámara y vuelve a mirar la pezuña, con giros suaves. De 2 a 4 s levanta el antebrazo derecho despacio y mueve la pezuña lila dos veces (el «hola» cae sobre el saludo). Desde el s 4 mira a cámara, baja la pezuña despacio y espera con la pezuña abajo, mirando a cámara, hasta el s 7. La pezuña no sube al mentón ni a la boca. El último fotograma tiene la pezuña abajo y la mirada a cámara (la toma 10 parte de él).
- **No debe verse:** [N-comunes] [N-L] [N-P] + Giros bruscos de la cabeza. Pezuña que suba al mentón o a la boca, golpes de pezuña. Cara con dientes a la vista o ojos muy abiertos. Crayón que desaparezca o cambie de oreja. Antebrazos claros. Que la pezuña no quede abajo al final de la toma.
- **Prompt:** el bloque «Prompt de video» de la **Toma 9** en `02_prompt/prompt.md` (copia idéntica archivada en `personajes/tiky/prompts/capitulos/granja_cap01_hola_granja.md`), pegado completo y sin cambios. Empieza con las cuatro líneas CRITICAL (sin palabras escritas, mismo diseño, cámara fija sin corte, nada en la puerta del granero) y sigue con la acción, «Fixed camera, no zoom, no pan.» y el estilo global.

### Toma 10 — Lumi espera (pausa viva)

- **Tipo:** clip (imagen→video)
- **Modelo y ajustes:** `seedance_2_0_mini`, imagen→video, 16:9, 480p, sin audio, 5 s
- **Costo cotizado:** 2,5 créditos (5 s × 0,5)
- **Imagen de partida:** Último fotograma del clip de la toma 9: se extrae con ffmpeg del clip aprobado de la toma 9 (`ffmpeg -sseof -0.1 -i <clip_toma_09.mp4> -frames:v 1 -update 1 ultimo_toma_09.png`) y se sube como imagen de partida. Depende de la toma 9: no se puede pedir hasta que esa toma esté generada y cumpla su definición.
- **Depende de:** Toma 9 (cadena 9 → 10).
- **Personajes:** @lumi sola.
- **Lugar:** patio (`series/granja/entorno.md`), referencia `series/granja/referencias/patio.png`; el patio sale de la imagen de partida, no se describe de nuevo en el clip.
- **Composición:** La del último fotograma de la toma 9, que mantiene el Encuadre B del keyframe de la toma 9: misma cámara, mismo tamaño y misma posición, sin saltos. Encuadre B (la del keyframe B, no cambia). Cámara fija a la altura de los ojos de Tiky, de frente. Lumi sola, de cuerpo entero (el keyframe B salió de cuerpo entero, no en plano medio), centrada: cuerpo del 36 % al 64 % del ancho, puntas de los cuernos hacia el 20 % del alto, ojos hacia el 34 %, hocico hacia el 43 %, pezuñas traseras hacia el 93 %. Los antebrazos negros con la pezuña lila cuelgan a ambos lados del tronco (hacia el 68 % del alto). Granero a la izquierda (del 0 % al 40 % del ancho); a la derecha, cerca, pared y fieltro. Cámara fija durante los 5 s: sin zoom, sin paneo, sin corte.
- **Debe verse:** [L] [P] (listas en «Listas comunes») + **acción (5 s):** Parte del último fotograma de la toma 9: Lumi de frente, antebrazos abajo, mirando a cámara. Durante 5 s: parpadea dos veces, respira suave y sonríe levemente. Los antebrazos siguen abajo. Movimiento vivo, ningún gesto nuevo; no hay fotograma idéntico durante toda la toma.
- **No debe verse:** [N-comunes] [N-L] [N-P] + Imagen congelada o ningún parpadeo. Que Lumi haga un gesto nuevo (levantar la pezuña, llevársela al mentón, sacar el crayón). Sonrisa con dientes u ojos muy abiertos. Salto de luz, posición o tamaño respecto de la toma 9.
- **Prompt:** el bloque «Prompt de video» de la **Toma 10** en `02_prompt/prompt.md` (copia idéntica archivada en `personajes/tiky/prompts/capitulos/granja_cap01_hola_granja.md`), pegado completo y sin cambios. Empieza con las cuatro líneas CRITICAL (sin palabras escritas, mismo diseño, cámara fija sin corte, nada en la puerta del granero) y sigue con la acción, «Fixed camera, no zoom, no pan.» y el estilo global.

### Toma 11 — Lumi responde hola

- **Tipo:** clip (imagen→video)
- **Modelo y ajustes:** `seedance_2_0_mini`, imagen→video, 16:9, 480p, sin audio, 6 s
- **Costo cotizado:** 3 créditos (6 s × 0,5)
- **Imagen de partida:** Último fotograma del clip de la toma 10: se extrae con ffmpeg del clip aprobado de la toma 10 (`ffmpeg -sseof -0.1 -i <clip_toma_10.mp4> -frames:v 1 -update 1 ultimo_toma_10.png`) y se sube como imagen de partida. Depende de la toma 10: no se puede pedir hasta que esa toma esté generada y cumpla su definición.
- **Depende de:** Toma 10 (cadena 9 → 10 → 11).
- **Personajes:** @lumi sola.
- **Lugar:** patio (`series/granja/entorno.md`), referencia `series/granja/referencias/patio.png`; el patio sale de la imagen de partida, no se describe de nuevo en el clip.
- **Composición:** La del último fotograma de la toma 10, que mantiene el Encuadre B del keyframe de la toma 9: misma cámara, mismo tamaño y misma posición, sin saltos. Encuadre B (la del keyframe B, no cambia). Cámara fija a la altura de los ojos de Tiky, de frente. Lumi sola, de cuerpo entero (el keyframe B salió de cuerpo entero, no en plano medio), centrada: cuerpo del 36 % al 64 % del ancho, puntas de los cuernos hacia el 20 % del alto, ojos hacia el 34 %, hocico hacia el 43 %, pezuñas traseras hacia el 93 %. Los antebrazos negros con la pezuña lila cuelgan a ambos lados del tronco (hacia el 68 % del alto). Granero a la izquierda (del 0 % al 40 % del ancho); a la derecha, cerca, pared y fieltro. Cámara fija durante los 6 s: sin zoom, sin paneo, sin corte.
- **Debe verse:** [L] [P] (listas en «Listas comunes») + **acción (6 s):** Parte del último fotograma de la toma 10: pezuña abajo, mirando a cámara. Hacia el s 1 levanta el antebrazo derecho despacio y mueve la pezuña lila dos veces (el «hola» cae entre los s 2 y 3 con la pezuña en alto); la baja hacia el s 4 y sonríe en silencio a cámara hasta el s 6.
- **No debe verse:** [N-comunes] [N-L] [N-P] + Golpes de pezuña; saludo apurado. Pezuña al mentón o a la boca. Sonrisa con dientes, ojos muy abiertos. Salto de luz, posición o tamaño respecto de la toma 10. Que la pezuña baje antes del s 3.
- **Prompt:** el bloque «Prompt de video» de la **Toma 11** en `02_prompt/prompt.md` (copia idéntica archivada en `personajes/tiky/prompts/capitulos/granja_cap01_hola_granja.md`), pegado completo y sin cambios. Empieza con las cuatro líneas CRITICAL (sin palabras escritas, mismo diseño, cámara fija sin corte, nada en la puerta del granero) y sigue con la acción, «Fixed camera, no zoom, no pan.» y el estilo global.

### Toma 12 — Caminan a su lugar

- **Tipo:** clip (imagen→video)
- **Modelo y ajustes:** `seedance_2_0_mini`, imagen→video, 16:9, 480p, sin audio, 4 s
- **Costo cotizado:** 2 créditos (4 s × 0,5)
- **Imagen de partida:** Keyframe C-entrada, ID `83e54673-d116-47dc-bcb0-051ede05f51c` (`03_keyframes/keyframe_C_entrada.png`). Se sube como imagen de partida del clip (no se sube otra referencia). La misma imagen arranca también la toma 1.
- **Depende de:** Ninguna (no encadenada).
- **Personajes:** @tiky y @lumi; Lumi mide una vez y media la altura de Tiky (a Tiky el copete le llega a los ojos de Lumi), Lumi a la izquierda.
- **Lugar:** patio (`series/granja/entorno.md`), referencia `series/granja/referencias/patio.png`; el patio sale de la imagen de partida, no se describe de nuevo en el clip.
- **Composición:** Encuadre C-entrada (la del keyframe C-entrada, no cambia). Cámara fija a la altura de los ojos de Tiky, de frente. Los dos pequeños y al fondo, junto a la cerca: Lumi a la izquierda (del 32 % al 50 % del ancho, cuernos hacia el 34 % del alto, pezuñas hacia el 81 %) y Tiky a su derecha (del 52 % al 67 %, copete hacia el 43 %, dedos hacia el 81 %). Granero a la izquierda (del 0 % al 33 % del ancho); gran tramo de fieltro verde delante de ellos, por donde caminan hacia cámara. Cámara fija durante los 4 s: sin zoom, sin paneo, sin corte.
- **Debe verse:** [T] [L] [P] (listas en «Listas comunes») + **acción (4 s):** Caminan despacio desde el fondo hacia cámara, uno al lado del otro, Lumi a la izquierda, con pasos pequeños y parejos. Se detienen cerca del granero, en el centro del patio, en el último medio segundo, mirando a cámara. El patio queda ordenado y vacío. Terminan de cuerpo entero, de frente, alas y antebrazos abajo.
- **No debe verse:** [N-comunes] [N-T] [N-L] [N-P] + Tropiezos, choques, caídas, carrera. Que uno pase delante del otro. Animales, personas u objetos en el patio («patio ordenado y vacío»). Cualquier gesto de saludo. Cambio del granero.
- **Prompt:** el bloque «Prompt de video» de la **Toma 12** en `02_prompt/prompt.md` (copia idéntica archivada en `personajes/tiky/prompts/capitulos/granja_cap01_hola_granja.md`), pegado completo y sin cambios. Empieza con las cuatro líneas CRITICAL (sin palabras escritas, mismo diseño, cámara fija sin corte, nada en la puerta del granero) y sigue con la acción, «Fixed camera, no zoom, no pan.» y el estilo global.

### Toma 13 — Quietos en su lugar

- **Tipo:** clip (imagen→video)
- **Modelo y ajustes:** `seedance_2_0_mini`, imagen→video, 16:9, 480p, sin audio, 4 s
- **Costo cotizado:** 2 créditos (4 s × 0,5)
- **Imagen de partida:** Último fotograma del clip de la toma 12: se extrae con ffmpeg del clip aprobado de la toma 12 (`ffmpeg -sseof -0.1 -i <clip_toma_12.mp4> -frames:v 1 -update 1 ultimo_toma_12.png`) y se sube como imagen de partida. Depende de la toma 12: no se puede pedir hasta que esa toma esté generada y cumpla su definición.
- **Depende de:** Toma 12 (cadena 12 → 13).
- **Personajes:** @tiky y @lumi; Lumi mide una vez y media la altura de Tiky (a Tiky el copete le llega a los ojos de Lumi), Lumi a la izquierda.
- **Lugar:** patio (`series/granja/entorno.md`), referencia `series/granja/referencias/patio.png`; el patio sale de la imagen de partida, no se describe de nuevo en el clip.
- **Composición:** La del último fotograma de la toma 12: los dos de frente en el centro del patio, mirando a cámara, en el tamaño y la posición con que salgan al final de la toma 12 (no medibles antes de generarla; esa toma fija el encuadre de toda la cadena). Misma cámara, mismo tamaño y misma posición entre tomas, sin saltos. Cámara fija durante los 4 s: sin zoom, sin paneo, sin corte.
- **Debe verse:** [T] [L] [P] (listas en «Listas comunes») + **acción (4 s):** Parte del último fotograma de la toma 12: los dos de frente, quietos, mirando a cámara, Lumi a la izquierda. Durante 4 s solo parpadean y respiran suave, con sonrisas pequeñas. Nada más se mueve; el patio sigue despejado. No hay fotograma idéntico durante toda la toma.
- **No debe verse:** [N-comunes] [N-T] [N-L] [N-P] + Imagen congelada. Gestos (saludo, pasos, giros). Objetos o animales que aparezcan. Salto de luz, posición o tamaño respecto de la toma 12.
- **Prompt:** el bloque «Prompt de video» de la **Toma 13** en `02_prompt/prompt.md` (copia idéntica archivada en `personajes/tiky/prompts/capitulos/granja_cap01_hola_granja.md`), pegado completo y sin cambios. Empieza con las cuatro líneas CRITICAL (sin palabras escritas, mismo diseño, cámara fija sin corte, nada en la puerta del granero) y sigue con la acción, «Fixed camera, no zoom, no pan.» y el estilo global.

### Toma 14 — Espera viva con el adulto 1

- **Tipo:** clip (imagen→video)
- **Modelo y ajustes:** `seedance_2_0_mini`, imagen→video, 16:9, 480p, sin audio, 4 s
- **Costo cotizado:** 2 créditos (4 s × 0,5)
- **Imagen de partida:** Keyframe C, ID `b7fc0c43-4acc-40f1-9b0f-ea377f2012ed` (`03_keyframes/keyframe_C_los_dos.png`). Se sube como imagen de partida del clip (no se sube otra referencia). La misma imagen arranca también las tomas 4, 5 y 16.
- **Depende de:** Ninguna (no encadenada).
- **Personajes:** @tiky y @lumi; Lumi mide una vez y media la altura de Tiky (a Tiky el copete le llega a los ojos de Lumi), Lumi a la izquierda.
- **Lugar:** patio (`series/granja/entorno.md`), referencia `series/granja/referencias/patio.png`; el patio sale de la imagen de partida, no se describe de nuevo en el clip.
- **Composición:** Encuadre C (la del keyframe C, no cambia). Cámara fija a la altura de los ojos de Tiky, de frente. Lumi a la izquierda (cuerpo del 23 % al 50 % del ancho, cuernos hacia el 20 % del alto, pezuñas hacia el 91 %) y Tiky a su derecha (del 52 % al 75 %, punta del copete hacia el 33 %, dedos hacia el 91 %); Tiky le llega a Lumi a los ojos con el copete. Granero a la izquierda (del 0 % al 33 % del ancho), cerca baja detrás de los dos, de lado a lado. Cámara fija durante los 4 s: sin zoom, sin paneo, sin corte.
- **Debe verse:** [T] [L] [P] (listas en «Listas comunes») + **acción (4 s):** Los dos de frente, mirando a cámara, Lumi a la izquierda. Durante 4 s parpadean y respiran suave, con sonrisas pequeñas; alas y antebrazos abajo, sin gesto ni movimiento nuevo. No hay fotograma idéntico durante toda la toma.
- **No debe verse:** [N-comunes] [N-T] [N-L] [N-P] + Imagen congelada o sin parpadeo. Gestos con el ala o la pezuña. Sonrisas con dientes. Objetos o animales que aparezcan. Cambio de encuadre.
- **Prompt:** el bloque «Prompt de video» de la **Toma 14** en `02_prompt/prompt.md` (copia idéntica archivada en `personajes/tiky/prompts/capitulos/granja_cap01_hola_granja.md`), pegado completo y sin cambios. Empieza con las cuatro líneas CRITICAL (sin palabras escritas, mismo diseño, cámara fija sin corte, nada en la puerta del granero) y sigue con la acción, «Fixed camera, no zoom, no pan.» y el estilo global.

### Toma 15 — Espera viva con el adulto 2

- **Tipo:** clip (imagen→video)
- **Modelo y ajustes:** `seedance_2_0_mini`, imagen→video, 16:9, 480p, sin audio, 4 s
- **Costo cotizado:** 2 créditos (4 s × 0,5)
- **Imagen de partida:** Último fotograma del clip de la toma 14: se extrae con ffmpeg del clip aprobado de la toma 14 (`ffmpeg -sseof -0.1 -i <clip_toma_14.mp4> -frames:v 1 -update 1 ultimo_toma_14.png`) y se sube como imagen de partida. Depende de la toma 14: no se puede pedir hasta que esa toma esté generada y cumpla su definición.
- **Depende de:** Toma 14 (cadena 14 → 15).
- **Personajes:** @tiky y @lumi; Lumi mide una vez y media la altura de Tiky (a Tiky el copete le llega a los ojos de Lumi), Lumi a la izquierda.
- **Lugar:** patio (`series/granja/entorno.md`), referencia `series/granja/referencias/patio.png`; el patio sale de la imagen de partida, no se describe de nuevo en el clip.
- **Composición:** La del último fotograma de la toma 14, que mantiene el Encuadre C del keyframe de la toma 14: misma cámara, mismo tamaño y misma posición, sin saltos. Encuadre C (la del keyframe C, no cambia). Cámara fija a la altura de los ojos de Tiky, de frente. Lumi a la izquierda (cuerpo del 23 % al 50 % del ancho, cuernos hacia el 20 % del alto, pezuñas hacia el 91 %) y Tiky a su derecha (del 52 % al 75 %, punta del copete hacia el 33 %, dedos hacia el 91 %); Tiky le llega a Lumi a los ojos con el copete. Granero a la izquierda (del 0 % al 33 % del ancho), cerca baja detrás de los dos, de lado a lado. Cámara fija durante los 4 s: sin zoom, sin paneo, sin corte.
- **Debe verse:** [T] [L] [P] (listas en «Listas comunes») + **acción (4 s):** Parte del último fotograma de la toma 14: los dos de frente, mirando a cámara. Durante 4 s siguen parpadeando y respirando suave, con sonrisas pequeñas; nada más se mueve.
- **No debe verse:** [N-comunes] [N-T] [N-L] [N-P] + Imagen congelada. Gestos nuevos. Salto de luz, posición o tamaño respecto de la toma 14. Objetos o animales que aparezcan.
- **Prompt:** el bloque «Prompt de video» de la **Toma 15** en `02_prompt/prompt.md` (copia idéntica archivada en `personajes/tiky/prompts/capitulos/granja_cap01_hola_granja.md`), pegado completo y sin cambios. Empieza con las cuatro líneas CRITICAL (sin palabras escritas, mismo diseño, cámara fija sin corte, nada en la puerta del granero) y sigue con la acción, «Fixed camera, no zoom, no pan.» y el estilo global.

### Toma 16 — Despedida

- **Tipo:** clip (imagen→video)
- **Modelo y ajustes:** `seedance_2_0_mini`, imagen→video, 16:9, 480p, sin audio, 6 s
- **Costo cotizado:** 3 créditos (6 s × 0,5)
- **Imagen de partida:** Keyframe C, ID `b7fc0c43-4acc-40f1-9b0f-ea377f2012ed` (`03_keyframes/keyframe_C_los_dos.png`). Se sube como imagen de partida del clip (no se sube otra referencia). La misma imagen arranca también las tomas 4, 5 y 14.
- **Depende de:** Ninguna (no encadenada).
- **Personajes:** @tiky y @lumi; Lumi mide una vez y media la altura de Tiky (a Tiky el copete le llega a los ojos de Lumi), Lumi a la izquierda.
- **Lugar:** patio (`series/granja/entorno.md`), referencia `series/granja/referencias/patio.png`; el patio sale de la imagen de partida, no se describe de nuevo en el clip.
- **Composición:** Encuadre C (la del keyframe C, no cambia). Cámara fija a la altura de los ojos de Tiky, de frente. Lumi a la izquierda (cuerpo del 23 % al 50 % del ancho, cuernos hacia el 20 % del alto, pezuñas hacia el 91 %) y Tiky a su derecha (del 52 % al 75 %, punta del copete hacia el 33 %, dedos hacia el 91 %); Tiky le llega a Lumi a los ojos con el copete. Granero a la izquierda (del 0 % al 33 % del ancho), cerca baja detrás de los dos, de lado a lado. Cámara fija durante los 6 s: sin zoom, sin paneo, sin corte.
- **Debe verse:** [T] [L] [P] (listas en «Listas comunes») + **acción (6 s):** Los dos de frente, mirando a cámara, Lumi a la izquierda. A los 2 s Tiky levanta el ala izquierda (la de la derecha del cuadro) y Lumi la pezuña derecha, despacio y a la vez; cada uno la mueve dos veces con movimientos pequeños (la voz «Adiós» cae de 2,8 a 3,8 s, sobre el saludo). Bajan el ala y la pezuña hacia el s 4,5 y quedan mirando a cámara, en calma, hasta el s 6. El último fotograma: los dos en calma, de frente, sin gesto.
- **No debe verse:** [N-comunes] [N-T] [N-L] [N-P] + Aleteo de vuelo, golpes de pezuña, saludo apurado (cada uno tiene 2 movimientos en unos 2,5 s). Ala o pezuña al pico, la boca o el mentón. Zoom o acercamiento de cámara en el final, elementos nuevos, un último fotograma que anuncie otro video, algo que se vea como invitación a seguir. Que alguno salga de cuadro.
- **Prompt:** el bloque «Prompt de video» de la **Toma 16** en `02_prompt/prompt.md` (copia idéntica archivada en `personajes/tiky/prompts/capitulos/granja_cap01_hola_granja.md`), pegado completo y sin cambios. Empieza con las cuatro líneas CRITICAL (sin palabras escritas, mismo diseño, cámara fija sin corte, nada en la puerta del granero) y sigue con la acción, «Fixed camera, no zoom, no pan.» y el estilo global.

## Orden de generación y dependencias

Cadenas (cada flecha usa el último fotograma del clip anterior): 1 → 2 · 6 → 7 → 8 · 9 → 10 → 11 · 12 → 13 · 14 → 15. Las tomas 3, 4, 5 y 16 no tienen dependientes.

**Etapa 1: Toma 4 (Tiky saluda hacia un lado), 6 s, 3 créditos. Acumulado: 3.**
Es una sola toma no encadenada y se queda como clip válido si cumple. La elijo porque, con el menor gasto, comprueba lo que más pesa del modelo antes de gastar el resto:
- Usa el Keyframe C, que arranca cuatro tomas (4, 5, 14 y 16): si el modelo conserva a los dos personajes y el patio desde esa imagen, queda probado el encuadre de más tomas.
- Pone a prueba a los dos a la vez: la identidad de Tiky y de Lumi (crayón, antebrazos negros, copete) y el saludo con el ala lento y pequeño, no aleteo (D4, M8).
- Contiene el único riesgo marcado como crítico de la psicóloga: la cara de Lumi al no responder (S1, «Plano 3»), junto con el giro suave de Tiky.
- Mide también las líneas CRITICAL (cámara fija, puerta del granero, sin texto).
- Ninguna otra toma depende de ella: si falla, no frena una cadena (solo avisa de cómo trata el modelo el Keyframe C).
Alternativas descartadas: la toma 14 cuesta 2 pero no tiene ningún saludo (no prueba lo difícil); la toma 3 prueba la pezuña de Lumi pero no la pareja; las entradas (1, 12) y los arranques de cadena (6, 9, 14) frenarían otras tomas si fallan.

**Etapa 2: tomas 5, 14 y 16 (Keyframe C), 3,5 + 2 + 3 = 8,5 créditos. Acumulado: 11,5.**
Mismo encuadre ya comprobado en la etapa 1. La 14 abre la cadena 14 → 15.

**Etapa 3: tomas 3, 6 y 9 (Lumi sola y Tiky solo), 3,5 + 3,5 + 3,5 = 10,5 créditos. Acumulado: 22.**
Abren las cadenas 6 → 7 → 8 y 9 → 10 → 11, que valen 9 y 9 con sus eslabones. Se piden después de las etapas 1 y 2 para llegar con el trato de saludo y de manos ya visto.

**Etapa 4: tomas 1 y 12 (caminar desde el fondo, Keyframe C-entrada), 2,5 + 2 = 4,5 créditos. Acumulado: 26,5.**
Caminar es lo que tiene más riesgo de tropiezos; va después de comprobar la identidad. De ellas dependen la 2 y la 13.

**Etapa 5a: tomas 2, 7, 10, 13 y 15 (primer eslabón de cada cadena), 2,5 + 2,5 + 2,5 + 2 + 2 = 11,5 créditos. Acumulado: 38.**
Cada una se pide solo cuando su toma anterior (1, 6, 9, 12, 14) cumple y se extrajo su último fotograma.

**Etapa 5b: tomas 8 y 11, 3 + 3 = 6 créditos. Acumulado: 44.**
La 8 depende de la 7 y la 11 de la 10.

**Regla de corte.** Si una toma no cumple su definición («Debe verse» y «No debe verse»), se detiene esa cadena (no se piden sus dependientes), se informa al dueño qué falló y cuánto costaría rehacerla, y no se regenera sin su autorización para esa pieza. Las demás cadenas independientes siguen. Si falla la etapa 1, no se pasa a la etapa 2 hasta que el dueño decida. Lo que falle se anota en las fichas («Fallos conocidos») y en `costos.md`.

Cada toma, antes de enviarse: se vuelve a cotizar y se compara con la tabla; se comprueba que la imagen de partida es la indicada (para encadenadas, que es el último fotograma del clip aprobado, no el de otro intento); se anota en `costos.md`.

## Cómo se revisa cada clip

1. `python3 video-studio/herramientas/revisar_fotogramas.py 04_clips/borradores/toma_NN_480p.mp4 07_revision/toma_NN --serie granja` (gratis). Marca imagen congelada, fotogramas vacíos, destellos (más de 3 por segundo), cortes y tramos sin cambio; no decide si el clip sirve, señala dónde mirar. En las esperas vivas (tomas 7, 10, 13, 14 y 15) el único movimiento son parpadeos y respiración: un aviso de tramo quieto ahí hay que mirarlo con la hoja de contacto, y es falla solo si el clip queda realmente congelado.
2. Se miran las hojas de contacto contra la lista de la pieza: cada punto de «Debe verse» con su segundo, y cada punto de «No debe verse».
3. En las encadenadas se compara el primer fotograma del clip con el último del anterior (luz, posición, tamaño, ala o pezuña en el mismo lugar).
4. El resultado va en `07_revision/` y en la tabla «Resultado» de este documento; después se puntúa la rúbrica con `puntuar_ficha.py`.

Qué criterio de `02_prompt/ficha_tecnica.md` cubre cada toma:

| Toma | Criterios que se comprueban en ese clip |
|---|---|
| 1 | D1, D5, D6, S2 (tropiezos), S3, C1 |
| 2 | D1, D2 (unión 1→2), D4, P6, M8, I2, S3, C2 (miniatura) |
| 3 | D1, D4, D5, D6, M2, M6, M8, S2 (cara de cerca, encuadre B), S3 |
| 4 | D1, D5, D6, M5, **S1 (crítico)**, S2, S3, M8 |
| 5 | D1, D4, D5, D6, M5, M6, M8, S2 (giro de Tiky), S3 |
| 6 | D1, D4, D5, D6, I1, I3 (inicio del plano continuo), M2, M3, M8 |
| 7 | **D2 (6→7), D3**, I3, M3, S5 |
| 8 | D2 (7→8), D4, I3, M8, P2 |
| 9 | D1, D4, D5, D6, I1, I3, M2, M3, M8, S2, S3 |
| 10 | **D2 (9→10), D3**, I3, M3, S5 |
| 11 | D2 (10→11), D4, I3, M8, P2, S2 |
| 12 | D1, D5, D6, S1 (juntos al final), S2 (tropiezos), M9 |
| 13 | D2 (12→13), D3, M9, S5 |
| 14 | D1, D3, D5, D6, I4, S5 |
| 15 | D2 (14→15), D3, I4, S5 |
| 16 | D1, D4, D5, D6, S2, S3, S6 |

Los criterios de voz, música y montaje (P2, P3, P5, P7, S4, M7, I2 en cuanto a la voz, C3 a C6) no se miran en el clip: el clip no lleva audio y se comprueban al montar.

## Datos por confirmar antes o con la primera toma

Los archivos no lo dicen y no se suponen. Se responden antes de enviar la etapa 1, o se registran con lo que devuelva la primera toma.

1. ¿Cuál es el nombre exacto del parámetro de `seedance_2_0_mini` en Higgsfield para generar sin audio (o el modelo ya sale sin audio por defecto), y cambia el costo cotizado al activarlo?
2. ¿A cuántos fotogramas por segundo sale el clip? Hace falta para recortar el primer fotograma de las tomas encadenadas y para ensamblar a los fps del generador (`ensamblar.py --formato largo`).
3. ¿El modelo respeta exactamente 7 s (y 4, 5 y 6 s), o devuelve un poco más o menos? Si una toma de 7 s dura menos, los tiempos del guion (por ejemplo la pezuña baja hacia el s 5,5) se corren.
4. ¿Cuántos fotogramas o décimas de segundo tarda en arrancar el movimiento? Sirve para saber si «a 1,5 s sube el ala» (toma 2) o «a 1 s» (tomas 8 y 11) llega a tiempo, y si el clip empieza con un tramo quieto que haya que recortar.
5. ¿La imagen subida se usa como el primer fotograma exacto del clip o solo como referencia de estilo? De eso depende que las tomas encadenadas empalmen sin salto.
6. ¿Cómo trata el modelo 480p una imagen de partida de 1376×768 (relación 1,79, no exactamente 16:9 = 1,78)? ¿Recorta, escala o deja bandas? Se mira en el primer clip; si recorta, cambia la composición medida.
7. ¿El modelo admite prompt negativo aparte, o todo va en un solo texto? Las líneas CRITICAL están redactadas en negativo («no written words», «nothing comes out of the barn door») dentro del prompt; algunos modelos leen la cosa nombrada y la dibujan (puerta, letras). Se observa en la etapa 1; si la puerta del granero cobra vida o aparecen letras, se informa antes de seguir.
8. **Toma 4, dirección de la mirada.** El prompt dice «Tiky looks away to his right, away from Lumi». Con Tiky de frente a cámara y Lumi a su derecha en el cuadro (a la izquierda de quien mira), el lado derecho de Tiky es el de Lumi, y «his right» contradice «away from Lumi». ¿Debe mirar hacia el lado contrario a Lumi (derecha de quien mira, que es lo que pide la acción del guion), y se corrige la palabra en `prompt.md` antes de generar? Lo mismo para «raises his right wing»: el ala izquierda (la de la derecha del cuadro) de Tiky es la más cercana a Lumi, a la izquierda de quien mira.
9. ¿Cuánto cambia el tamaño de los personajes entre el principio y el final de las tomas 1 y 12, y es aceptable que las tomas 2 y 13 (y la 14 y 16 que parten del Keyframe C) no tengan el mismo tamaño exacto? El criterio D6 pide que el encuadre C se vea igual en todas las tomas; las tomas 2 y 13 heredan el tamaño con que termine el caminar y eso no se puede medir antes. ¿Qué tolerancia se acepta?
10. ¿Cómo se sacan los últimos fotogramas: de qué clip (480p) y a qué resolución se suben? El último fotograma de un clip a 480p es la imagen de partida de la siguiente toma, y el remate a 720p (fuera de esta autorización) no reproduciría las mismas tomas encadenadas si se vuelve a generar; ¿se decide después si el 720p se hace toma por toma o se mantiene el borrador?
11. ¿Se confirma que Keyframe B de cuerpo entero es la imagen de partida de las tomas 3 y 9? Hay una solicitud de cambio abierta (`video-studio/cambios/2026-11-20_encuadre_lumi.md`) sobre ese encuadre; si cambia el keyframe B, cambian las tomas 3, 9, 10 y 11 (12,5 créditos).
12. `02_prompt/prompt.md`, sección 9, todavía dice «2 intentos por toma» y 182 créditos; con la regla de un intento por pieza, la cifra que vale para estos clips es 44 créditos. ¿Se actualiza esa sección? (No la toqué: la orden era no cambiar nada más del prompt.)
13. El techo del granero: `entorno.md` (corregido el 2026-11-20) dice que el aprobado tiene un quiebre por lado, y `03_keyframes/definicion.md` (no se genera) pedía techo recto. Estas piezas piden que el clip conserve el de la imagen de partida. ¿Se confirma?

## Preguntas ya resueltas por la coordinación (2026-11-21)

- **Pregunta 8 (mirada en la toma 4):** resuelta. Tiky mira hacia la derecha del cuadro, lejos de Lumi, y saluda siempre con el ala izquierda (la de la derecha del cuadro). Corregido en `prompt.md` y en las fichas; ver `video-studio/cambios/2026-11-21_lado_del_saludo.md`.
- **Pregunta 11 (encuadre de Lumi):** resuelta. El dueño aprobó el cuerpo entero el 2026-11-20; el Keyframe B vale tal cual.
- **Pregunta 12 (presupuesto):** resuelta. La sección 9 de `prompt.md` ya dice un intento por toma: 44 créditos en borrador.
- **Pregunta 13 (techo del granero):** resuelta. Vale el techo de la imagen de partida, que es el mismo en los cuatro keyframes.
- **Preguntas 1 a 7, 9 y 10:** siguen abiertas. No se pueden saber sin generar; se observan en la etapa 1 y se anotan antes de autorizar la etapa 2.

## Revisión del equipo

| Quién | Qué revisó | ¿Conforme? | Nota |
|---|---|---|---|
| director-de-prompts | Que cada dato venga de una ficha o del entorno, sin suposiciones | Sí, con preguntas abiertas | Rasgos, fallos conocidos y patio vienen de las fichas y de `entorno.md`; acciones y tiempos, de `prompt.md` (con las líneas CRITICAL ya añadidas); costos, de la cotización de la coordinación del 2026-11-21. Las medidas de composición son estimaciones visuales sobre los PNG. Preguntas 1 a 13 arriba; la 8 conviene resolverla antes de la etapa 1 |
| psicologa-infantil | Que nada de lo definido asuste, confunda o sea peligroso de imitar | | |

## Resultado

| Pieza | ID | ¿Cumple la definición? | Qué falló | Costo |
|---|---|---|---|---|
