# 09 · Prompts maestros

Cada toma lleva **dos prompts**: el del keyframe (imagen) y el del video (movimiento). Van en inglés, en positivo y en
este orden, porque los modelos le dan más peso a lo primero.

## Fórmula del keyframe

```
1. Estilo y tipo de imagen          (del estilo global de la serie o del personaje)
2. Bloque de identidad              (pegado TAL CUAL de personajes/<id>/ficha.md)
3. Expresión y pose inicial         (verbos de cap. 04, panel de la hoja de emociones)
4. Escenario                        (bloque del lugar, pegado tal cual)
5. Plano, ángulo y lente            (cap. 02)
6. Luz y paleta                     (cap. 03)
7. Formato                          (vertical 9:16)
```

## Fórmula del video

```
1. Quién, por referencia            ("the character from the reference image" + 2-3 rasgos fijados)
2. UNA acción con principio y fin   (anticipación → acción → pose final)
3. Actuación secundaria             (lo que acompaña: copete que rebota, boa que se balancea)
4. Cámara                           (un movimiento, velocidad, de dónde a dónde)
5. Ritmo                            (slowly / in a quick snap / holds for a beat)
6. Estilo y luz                     (igual que el keyframe)
7. Cierre negativo corto            (solo si el modelo insiste en algo: "no text, no extra characters")
```

## Ejemplo 1 · Tiky, curiosidad (serie `granja`, 1–3 años)

**Emoción:** curiosidad → alegría. **Objetivo:** que el niño mire y nombre «caja». **Cámara:** acercamiento lento.

Keyframe (`gpt_image_2_6` calidad baja para probar · `nano_banana_2` para el final):

```text
Modern 3D cartoon render, soft matte vinyl toy figures, children's animation style, simple rounded shapes, clean bright colors. Tiky, an adorable baby chick shaped like a smooth upright egg with no neck, warm sunflower yellow body with a pale butter-cream belly, a small discreet tuft of three short rounded flame-shaped feathers in red-orange on top of his head, big round dark-brown eyes with a white sparkle, no eyebrows, a small rounded coral-peach beak, soft rosy cheeks, tiny stubby wings, short coral-peach feet with three round toes. He stands on tiptoes leaning forward, head tilted, eyes wide with interest, looking at a small closed wooden box on the floor in front of him. A toy farmyard at toy scale on a sunny playroom floor: a small red wooden toy barn with a white roof on the left, a low white wooden fence behind, a soft pastel green felt mat as grass, plain pastel sky-blue wall in the background. Medium shot at the chick's eye level, 35mm lens. Soft even daylight, gentle soft shadows. Vertical 9:16.
```

Video (`seedance_2_0_mini`, 5 s, 480p para el borrador):

```text
The yellow chick from the reference image, with his small red-orange tuft, slowly leans closer to the wooden box on tiptoes, tilts his head to one side, then gently taps the lid with one tiny wing and his eyes light up with a happy smile. His tuft bounces softly as he moves. The camera very slowly pushes in from medium shot to close-up on his face. Calm, slow, gentle movement. Modern 3D cartoon render, soft matte vinyl toy, soft even daylight.
```

## Ejemplo 2 · Lumi, ternura

**Emoción:** ternura. **Cámara:** fija, lente de retrato.

```text
The gentle cow from the reference image, creamy white with black patches and a lilac muzzle, slowly lifts one hoof to her chin, smiles softly with half-closed eyes, then takes the lilac crayon from behind her right ear and draws a small heart on the felt mat. Static locked-off camera, close-up at the chick's eye level, 50mm lens with shallow depth of field. Slow, warm and calm. Modern 3D cartoon render, soft matte vinyl toy, warm soft daylight.
```

## Ejemplo 3 · Spike, humor absurdo (3 tomas, 12 s)

**Emoción:** humor deadpan. **Gancho:** acción a la mitad. **Objetivo:** que lo compartan.

| Toma | Plano y cámara | Acción |
|---|---|---|
| 1 (0–3 s) | medio frontal, `static locked-off camera` | Spike explica con total seriedad un «método científico» para hacer tostadas con un teclado |
| 2 (3–8 s) | primer plano, `slow push-in` | aprieta una tecla con un dedo dramático; pausa total |
| 3 (8–12 s) | general, `static` | la tostada sale disparada; él no cambia la cara; la boa sigue balanceándose |

Video de la toma 2:

```text
The extremely tall, stick-thin man from the reference image, with a giant crown of neon-orange punk spikes, purple velvet tracksuit and neon-yellow feather boa, stares into the camera with a completely serious face, slowly raises one long finger and presses a single key on a small keyboard with dramatic precision, then freezes completely. The camera slowly pushes in from medium shot to close-up. Seamless white infinity studio, soft even light, realistic photo style, deadpan comedy.
```

## Lo que hace un prompt de nivel profesional

- **Verbos físicos y medidas** («leans forward on tiptoes», «each spike as long as his forearm»), no adjetivos vagos.
- **El mismo texto para lo que no cambia** (identidad, escenario, estilo): se copia, nunca se reescribe.
- **La emoción se muestra con el cuerpo** y se refuerza con cámara, luz y ritmo de la misma fila de la tabla (cap. 01).
- **Una acción por toma**, con principio, desarrollo y pose final legible.
- **Nada de texto, logos ni marcas** dentro de la imagen.
- **Nombres de artistas, estudios o personajes ajenos: nunca.** Se describe el efecto («warm soft light»), no a quién se imita.
