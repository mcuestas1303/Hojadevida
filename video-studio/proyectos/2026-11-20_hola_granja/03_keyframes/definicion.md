# Definición de generación — Hola, granja (rehacer Keyframe A y Keyframe B)

- **Estado:** NO SE GENERA
- **Costo total cotizado:** 3 créditos (2 imágenes × 1,5)
- **Autorizado por el dueño:** sí, 2026-11-20, para rehacer A y B una vez cada uno

<!--
Estado: PENDIENTE → REVISADA POR EL EQUIPO → AUTORIZADA. Solo con AUTORIZADA se genera.
Una fila por pieza. Cada pieza se genera una sola vez (video-studio/generacion.md).
Los keyframes C_los_dos y C_entrada ya son válidos y no se rehacen. A y B anteriores
(IDs 0b4b497b-8dc2-4441-8fd0-d6e151ac6a22 y cef6a8ab-e934-4e05-a0d3-94ab263be1a9) quedan sustituidos.
Medidas: fracciones del alto y del ancho del cuadro, medidas en keyframe_C_los_dos.png (16:9). Tolerancia ±3 %.
-->

> **2026-11-20 — No se genera.** El dueño autorizó rehacer A y B porque la coordinación informó
> que el techo del granero era distinto. Al preparar esta definición se compararon los cuatro
> keyframes a tamaño completo y el granero es el mismo en todos; el informe estaba equivocado.
> Rehacerlos gastaría 3 créditos sin motivo. Esta definición queda como modelo de cómo se
> define una pieza, no como orden de generación.

## Piezas

### Keyframe A — Tiky solo (arranca la toma 6)

- **Tipo:** keyframe
- **Modelo y ajustes:** Nano Banana 2 (`nano_banana_2`), 16:9, una imagen. Resolución: la estándar del modelo (ver pregunta 5)
- **Costo cotizado:** 1,5 créditos
- **Referencias que se suben:**
  1. Tiky aprobado, ID `6cff1fa4-a734-402c-9384-7a76c5ee6bd3`: identidad (cara, color, copete, proporciones). No sirve para el encuadre.
  2. `keyframe_C_los_dos.png`, ID `b7fc0c43-4acc-40f1-9b0f-ea377f2012ed` (es la misma imagen que `series/granja/referencias/patio.png`): cámara, tamaño de Tiky en el cuadro, línea del suelo, posición del granero, cerca y pared. Lumi sale en ella y no debe aparecer.
  3. `keyframe_C_entrada.png`, ID `83e54673-d116-47dc-bcb0-051ede05f51c`: el granero entero y sin tapar (paredes rojas con vetas, puerta oscura, una abertura cuadrada).
- **Personajes:** @tiky solo. Altura de Tiky en el cuadro: 60 % del alto (copete incluido), igual que en `keyframe_C_los_dos.png`. En la ficha mide dos tercios de Lumi; aquí no hay Lumi y rige la medida del cuadro.
- **Lugar:** patio (`series/granja/entorno.md`), imagen de referencia `referencias/patio.png`
- **Composición:**
  - Cámara fija, a la altura de los ojos de Tiky, de frente, la misma que en `keyframe_C_los_dos.png`.
  - Tiky de cuerpo completo, **centrado** (eje del cuerpo en el 50 % del ancho; el cuerpo ocupa del 39 % al 61 % del ancho, un 22 %).
  - Punta del copete al 30 % del alto desde arriba; parte alta del cuerpo (sin copete) al 44 %; ojos al 56 %; la base de los dedos de las patas al 90 %. Bajo sus patas queda el 10 % de fieltro verde.
  - Mira a cámara, alas abajo pegadas al cuerpo, sonrisa leve, las dos patas visibles con tres dedos.
  - Granero a la izquierda y entero: fachada entre el 7 % y el 30 % del ancho, techo completo visible, sin que Tiky lo tape (entre el granero y Tiky queda un 9 % de ancho libre).
  - Cerca blanca baja detrás, de lado a lado; la pared azul pastel con zócalo blanco ocupa del borde superior hasta el 60 % del alto aproximadamente. A la derecha de Tiky, solo cerca, pared y fieltro.
- **Debe verse:**
  - Tiky: cuerpo de huevo sin cuello · amarillo con panza crema · copete de 3 plumas rojo anaranjado, discreto, la del centro más alta, un cuarto de la altura del cuerpo · ojos marrón oscuro con un brillo blanco · sin cejas · pico coral pequeño · mejillas rosadas · dos alas pegadas a los lados que llegan a la mitad del cuerpo · dos patas coral de tres dedos · sin ropa ni objetos.
  - Granero: madera roja con vetas verticales; **techo a dos aguas simple**, blanco, con alero: un plano recto a cada lado que se unen en una sola línea de cumbrera, sin quiebre; puerta rectangular abierta y oscura; **una sola abertura cuadrada** encima de la puerta.
  - Cerca baja blanca de postes redondeados y dos travesaños, detrás de Tiky. Suelo de fieltro verde claro liso. Pared azul cielo pastel lisa con zócalo blanco. Luz de día pareja desde arriba a la izquierda, sombras suaves.
- **No debe verse:**
  - Techo del granero quebrado, con dos pendientes por lado o tipo mansarda (fallo conocido del patio cuando el personaje sale solo, 2026-11-20).
  - Ventana a la derecha ni en ningún otro lugar de la pared (fallo conocido); cuadros, enchufes, letreros, veleta, animales dentro del granero.
  - Lumi ni ningún otro personaje o animal. Copete grande, esponjado o brillante (fallo conocido de Tiky). Ropa, accesorios, cejas, ojos verdes, manos en lugar de alas.
  - Tiky más grande o más pequeño que el 60 % del alto, o desplazado hacia la derecha.
  - Texto, letras, marca de agua, logo.
- **Prompt:**

```text
Reference 1 is the approved character image of Tiky: copy his face, colors, proportions and tuft exactly, but do not copy its framing. Reference 2 is an approved frame of the same toy yard: copy the camera position, the size of the chick in the frame, the floor line, the position of the barn, the fence and the wall; the cow in Reference 2 must not appear. Reference 3 is an approved frame showing the whole barn: copy the red wooden walls, the open dark door and the single square opening above it.
Tiky, an adorable baby chick shaped like a smooth upright egg with no neck, warm sunflower yellow body with a pale butter-cream belly, a small discreet tuft of three short rounded flame-shaped feathers in red-orange on top of his head, big round dark-brown eyes with a white sparkle, no eyebrows, a small rounded coral-peach beak, soft rosy cheeks, tiny stubby wings, short coral-peach feet with three round toes.
Full-body shot of Tiky alone, standing centered in the frame, facing the camera, with his two tiny wings down and pressed at his sides, a small gentle smile, both coral feet with three toes visible. Tiky fills 60 percent of the frame height: the tip of his tuft is at 30 percent from the top edge, his eyes at 56 percent, and his toes at 90 percent, with plain green felt below. His body spans the middle 22 percent of the frame width, centered. The tuft stays small and discreet, three feathers, not enlarged. The barn is on the left, fully visible and not covered by Tiky, its facade between 7 percent and 30 percent of the frame width. Fixed eye-level camera at the chick's height, same camera and same yard as Reference 2.
A toy farmyard at toy scale on a sunny playroom floor: a small red wooden toy barn with a white roof on the left, a low white wooden fence behind, a soft pastel green felt mat as grass, plain pastel sky-blue wall in the background.
Barn details: red wooden walls with vertical grain; the white roof is a SIMPLE GABLE roof with ONE straight flat slope on each side meeting at a single straight ridge, with a small eave, and NOT broken, NOT bent, NOT a gambrel or mansard roof; one open dark rectangular door in the facade and ONE single square opening above it; no sign, no weathervane, no animals inside. The low white fence has rounded posts and two rails and runs behind the character from side to side. Smooth light green felt floor with no flowers or stones, a strip of wooden floor at the far back. Plain smooth pastel sky-blue wall with a white baseboard and NO window anywhere. Daylight from the upper left, soft shadows.
Modern 3D cartoon render, soft matte vinyl toy figures, children's animation style, simple rounded shapes, clean bright colors, soft even daylight, gentle soft shadows, uncluttered background, calm and slow, eye-level camera at the chick's height.
Exclude: broken roof, bent roof, gambrel roof, mansard roof, window, picture, socket, sign, weathervane, cow, Lumi, any second character, extra characters, extra animals, humans, enlarged or fluffy or glowing tuft, clothes, accessories, eyebrows, hands, text, letters, watermark, logo, realistic fur, scary faces, sharp teeth, dark shadows, night, fire, weapons, fast motion, motion blur, camera shake, flashing lights.
```

### Keyframe B — Lumi sola, plano medio (arranca las tomas 3 y 9)

- **Tipo:** keyframe
- **Modelo y ajustes:** Nano Banana 2 (`nano_banana_2`), 16:9, una imagen. Resolución: la estándar del modelo (ver pregunta 5)
- **Costo cotizado:** 1,5 créditos
- **Referencias que se suben:**
  1. Lumi aprobada, ID `aea1a3a4-5067-48ed-beb3-226b70e1ff8f`: identidad (manchas, crayón, antebrazos negros, pezuñas lila, hocico). Es de cuerpo entero: sirve solo para identidad, no para el encuadre (se dice en el prompt).
  2. `keyframe_C_entrada.png`, ID `83e54673-d116-47dc-bcb0-051ede05f51c`: el granero entero (techo, puerta, abertura), cerca, suelo y pared. No se sube `keyframe_C_los_dos.png` para no empujar al generador a repetir el cuerpo entero de Lumi.
- **Personajes:** @lumi sola. La ficha la mide a tres cuartos de la fachada del granero en cuerpo entero; en este plano medio la medida que rige es la del cuadro, de abajo.
- **Lugar:** patio (`series/granja/entorno.md`), imagen de referencia `referencias/patio.png` (cámara y luz; el granero, de la referencia 2)
- **Composición:**
  - Plano medio de Lumi, centrada (eje del cuerpo en el 50 % del ancho; el cuerpo, de brazo a brazo, ocupa del 25 % al 75 % del ancho), de frente, mirando a cámara.
  - **Dentro del cuadro:** de las puntas de los cuernos (al 8 % del alto desde arriba) hasta la cadera. El borde inferior del cuadro (100 %) corta justo en la cadera, donde nacen las patas. Dentro quedan cabeza completa con cuernos, orejas y crayón, hocico, tronco con las dos manchas, los dos brazos y las dos pezuñas.
  - **Fuera del cuadro:** las patas de abajo con sus calcetines negros y las dos pezuñas traseras, y el suelo bajo ella. No se ve el suelo bajo sus pies ni sus patas.
  - Brazos caídos a los lados del cuerpo, **separados del tronco, a la vista y enteros**: los antebrazos negros y las dos pezuñas lila terminan hacia el 68 % del alto, a cada lado del cuerpo (aprox. 26 % y 74 % del ancho), sin cortar por el borde ni quedar tapados por el cuerpo. La toma 3 levanta la pezuña derecha desde ahí.
  - Ojos al 30 % del alto, hocico lila al 40 %. Sonrisa leve, mirando a cámara.
  - Granero a la izquierda, detrás y a un lado de ella: la fachada llega hasta el 22 % del ancho y el borde izquierdo del cuadro corta su lado izquierdo; la cumbrera del techo y el plano derecho del techo se ven completos (ver pregunta 4). Sin granero a la derecha; a la derecha, cerca blanca y pared azul.
- **Debe verse:**
  - Lumi: cuerpo de huevo sin cuello · blanco crema con dos manchas negras (una cruza panza y espalda, otra sobre la cabeza entre los cuernos; ninguna alrededor de los ojos) · **crayón lila corto y grueso detrás de la oreja derecha (a la izquierda de quien mira), apoyado sobre la mancha negra de la cabeza, entero, visible contra el negro** · dos cuernos crema pequeños y redondeados · orejas caídas con interior lila · ojos miel con un brillo blanco · cejas suaves · hocico lila ancho con dos puntos · **antebrazos negros como calcetines, con la pezuña lila al final de cada uno** · sin cencerro, flor ni bombilla.
  - Granero con **techo a dos aguas simple**, blanco, con alero; puerta rectangular abierta y oscura; **una sola abertura cuadrada** encima. Cerca baja blanca, fieltro verde, pared azul pastel lisa con zócalo blanco. Luz de día pareja desde arriba a la izquierda.
- **No debe verse:**
  - Lumi de cuerpo entero, sus patas o el suelo bajo sus pies (fallo de la primera B).
  - Antebrazos blancos o claros (fallo conocido, 2026-11-20); pezuñas que no sean lila.
  - Omitir el crayón o mostrarlo fuera de la oreja derecha (fallo conocido).
  - Techo del granero quebrado, tipo mansarda (fallo conocido); ventana en la pared (fallo conocido); cuadros, enchufes, letreros, veleta.
  - Cuerpo mayormente negro, hocico rosado, cencerro, campana, flor, bombilla o brillo de «idea».
  - Tiky ni ningún otro personaje o animal. Texto, letras, marca de agua, logo.
- **Prompt:**

```text
Reference 1 is the approved character image of Lumi: copy her face, patches, crayon, black forearms, lilac hooves and colors exactly, but do not copy its framing, because it is a full-body image and this one is a medium shot. Reference 2 is an approved frame showing the whole barn and yard: copy the red wooden walls, the open dark door, the single square opening above it, the fence, the felt floor and the wall.
Lumi, an adorable gentle cow shaped like a big smooth upright egg with no neck, about one and a half times as tall as Tiky, mostly creamy white with two large irregular black patches with soft wavy edges (one across her back and belly, one on top of her head between her horns), black lower legs like little socks, small lilac purple hooves, small cream rounded horns, small floppy ears with lilac insides, big warm honey-brown eyes with a white sparkle, soft gentle eyebrows, a wide rounded soft lilac muzzle with two small dot nostrils, a short chunky lilac crayon tucked behind her right ear.
Medium shot of Lumi alone, centered, facing the camera, a small gentle smile. The frame starts just above the tips of her cream horns, 8 percent from the top edge, and the bottom edge of the frame cuts her at the hip, where her legs begin: her legs, back hooves and the floor under her feet are outside the frame and not visible. Her body spans the middle 50 percent of the frame width. Her eyes are at 30 percent of the frame height. Her two forelegs hang down at her sides, clearly separated from her body and fully in view: both black forearms and both small lilac hooves are completely visible on each side of her body at about 68 percent of the frame height, not cropped and not hidden. The forearms are solid black like socks, not white. The short chunky lilac crayon is clearly visible behind her right ear, which is on the left side of the image, resting on the black patch on top of her head. Fixed eye-level camera at the chick's height.
A toy farmyard at toy scale on a sunny playroom floor: a small red wooden toy barn with a white roof on the left, a low white wooden fence behind, a soft pastel green felt mat as grass, plain pastel sky-blue wall in the background.
Barn details: the barn is on the left, behind and beside her, its facade reaching 22 percent of the frame width and cropped by the left edge of the frame; red wooden walls with vertical grain; the white roof is a SIMPLE GABLE roof with ONE straight flat slope on each side meeting at a single straight ridge, with a small eave, and NOT broken, NOT bent, NOT a gambrel or mansard roof; one open dark rectangular door and ONE single square opening above it; no sign, no weathervane, no animals inside. On the right side of the frame only the low white fence with rounded posts and two rails, the plain wall and the felt. Plain smooth pastel sky-blue wall with a white baseboard and NO window anywhere. Daylight from the upper left, soft shadows.
Modern 3D cartoon render, soft matte vinyl toy figures, children's animation style, simple rounded shapes, clean bright colors, soft even daylight, gentle soft shadows, uncluttered background, calm and slow, eye-level camera at the chick's height.
Exclude: full-body view, legs, back hooves, floor under her feet, white forearms, light forearms, missing crayon, crayon on the wrong ear, broken roof, bent roof, gambrel roof, mansard roof, window, picture, socket, sign, weathervane, Tiky, the chick, any second character, extra characters, extra animals, humans, mostly black body, pink muzzle, cowbell, bell, flower, light bulb, glow, text, letters, watermark, logo, realistic fur, scary faces, sharp teeth, dark shadows, night, fire, weapons, fast motion, motion blur, camera shake, flashing lights.
```

## Revisión del equipo

| Quién | Qué revisó | ¿Conforme? | Nota |
|---|---|---|---|
| director-de-prompts | Que cada dato venga de una ficha o del entorno, sin suposiciones | Sí, con preguntas abiertas | Bloques de identidad, patio, estilo y negativo pegados tal cual; fallos conocidos prevenidos en el prompt. Las medidas vienen de las mediciones de la coordinación en `keyframe_C_los_dos.png`; las del plano medio de B (8 %, 30 %, 68 %, 50 %) son derivadas de esa medición y de las proporciones de la ficha, no medidas. Preguntas 1 a 5 abajo |
| psicologa-infantil | Que nada de lo definido asuste, confunda o sea peligroso de imitar | | |

## Resultado

| Pieza | ID | ¿Cumple la definición? | Qué falló | Costo |
|---|---|---|---|---|

## Preguntas abiertas

1. **Techo de los keyframes de referencia.** Al abrir `keyframe_C_entrada.png` y `keyframe_C_los_dos.png`, el techo del granero se ve con un leve quiebre (dos pendientes por lado) y no del todo recto, aunque la definición del patio pide dos aguas simple. Si el generador copia la referencia, repetirá ese quiebre. ¿Se mantienen esas imágenes como referencia del granero (el prompt ya exige techo recto con texto), o se prefiere subir solo la de Tiky/Lumi y describir el granero con texto?
2. **Toma 6, «centrado delante del granero».** El prompt aprobado dice que Tiky está centrado delante del granero; el granero está a la izquierda y Tiky al centro del cuadro. Esta definición los deja separados (Tiky al 50 %, granero al 7–30 %). ¿Se acepta, y se ajusta el texto del keyframe de la toma 6 en `prompt.md`?
3. **Tomas 3 y 9, «de la cabeza a la mitad del cuerpo».** El prompt dice eso; esta definición fija «de los cuernos a la cadera» según lo pedido. Hay que alinear el texto de `prompt.md` con esta medida antes de archivar.
4. **Granero en B.** Con Lumi en plano medio y la misma cámara, el granero no cabe entero junto a ella: queda recortado por el borde izquierdo, con cumbrera y plano derecho del techo visibles. ¿Se acepta?
5. **Ajustes del modelo.** Los archivos no dicen la resolución de salida ni el máximo de imágenes de referencia que admite `nano_banana_2` (A usa 3, B usa 2). ¿Se confirma antes de enviar?
