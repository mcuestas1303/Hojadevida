# Prompt para la hoja de personaje

Se usa una sola vez por personaje, en un generador de imagen, adjuntando la imagen de
referencia del personaje. El resultado se guarda en `personajes/<id>/referencias/hoja_personaje.png`
y de ahí se recortan `frente.png` y `cuerpo_completo.png`.

Sigue la estructura del documento "My Character Sheet" de tu Drive: un tablero en cuatro
franjas horizontales, separadas por divisores sutiles.

```text
Character reference board for [NAME], based strictly on the attached reference image.
Same character in every frame: identical face, hair, body proportions and outfit.
Neutral light grey background, flat even studio lighting, no props, no text other than the labels.

Row 1 (35% of height):
- Left 25%: one large frontal head-and-shoulders hero portrait.
- Center 25%: the name "[NAME]" in bold type and a short profile under the header "CHARACTER PROFILE".
- Right 50%: four full-body head-to-toe views at the same scale, labelled FRONT, 3/4, SIDE, BACK.

Row 2:
- Left half: exactly three portraits labelled FRONT, 3/4, PROFILE.
- Right half: 2x4 grid of eight portraits labelled NEUTRAL, HAPPY, ANGRY, SAD, SURPRISED,
  WORRIED, CONFIDENT, DETERMINED.

Row 3:
- Left 60%: six poses labelled STANDING, WALKING, SITTING, RELAXED, TENSE, ACTION-READY
  (sitting directly on the floor, no furniture).
- Right 40%: 2x3 grid of six costume close-ups (garment structure, materials, closures, shoes,
  key accessories), each with a label of at most three words.

Row 4 (full width): four main colour swatches and five material samples taken from the
reference, each labelled only with a short name and its HEX value.
```
