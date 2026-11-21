# 02 · Cámara

Una toma = **un encuadre + un movimiento**. El modelo obedece mejor cuando la cámara se describe con un verbo
claro, una velocidad y dónde empieza y dónde termina. Fórmula:

```
<plano> <ángulo>, <lente>, camera <movimiento> <velocidad> from <inicio> to <fin>
```

Ejemplo: `Medium shot at the chick's eye level, 35mm lens, camera slowly pushes in from medium shot to close-up on his face.`

## Planos

| Plano | Prompt | Para qué |
|---|---|---|
| Gran plano general | `extreme wide shot` | ubicar, asombro, soledad |
| General | `wide shot`, `full body` | acción completa, comedia física |
| Medio | `medium shot` (cintura arriba) | conversación, gestos |
| Primer plano | `close-up` | emoción, reacción |
| Primerísimo / detalle | `extreme close-up on the eyes`, `insert shot of the crayon` | tensión, pista visual |
| Sobre el hombro | `over-the-shoulder shot` | diálogo entre dos |
| Punto de vista | `POV shot from Tiky's eyes` | inmersión, curiosidad |

## Ángulos

| Ángulo | Prompt | Efecto |
|---|---|---|
| A la altura de los ojos | `eye-level` (en infantil: `at the chick's eye level`) | cercanía, neutralidad |
| Bajo | `low-angle shot` | poder, épica, gigantismo (Spike altísimo) |
| Alto | `high-angle shot` | fragilidad, tristeza, ternura |
| Cenital | `top-down overhead shot` | orden, juego, recetas, manualidades |
| Holandés | `dutch angle` | locura, desequilibrio (no infantil) |

## Lentes y foco

| Lente | Prompt | Efecto |
|---|---|---|
| Gran angular | `16mm wide-angle lens` / `24mm` | energía, comedia exagerada, espacios |
| Normal | `35mm lens` | natural, documental, por defecto |
| Retrato | `50mm` / `85mm portrait lens`, `shallow depth of field, creamy bokeh` | emoción, aislar al personaje |
| Macro | `macro lens` | mundo de juguete, detalles, texturas de vinilo |
| Cambio de foco | `rack focus from the box to Tiky` | dirigir la mirada sin cortar |

Para figuras de juguete (Tiky, Lumi) el `macro lens` y `tilt-shift miniature look` refuerzan que son juguetes.

## Movimientos

| Movimiento | Prompt (copiar tal cual) | Qué comunica | Cuidado |
|---|---|---|---|
| Fija | `static locked-off camera` | observación, humor deadpan, calma | la más barata y estable: úsala si dudas |
| Acercamiento lento | `camera slowly pushes in` / `slow dolly-in` | intimidad, revelación, tensión | — |
| Alejamiento lento | `camera slowly pulls back` / `slow dolly-out` | soledad, revelar contexto, final | — |
| Paneo | `slow pan left to right` | seguir, mostrar un espacio | rápido = mareo |
| Inclinación | `tilt up from his feet to his face` | revelar altura (Spike) | — |
| Seguimiento | `tracking shot following him from the side` | viaje, acción | describe hacia dónde camina |
| Órbita | `camera orbits 180 degrees around her` | momento clave, héroe, producto | consume más intentos; tomas cortas |
| Grúa | `crane up revealing the farm` | asombro, cierre épico | — |
| Cámara en mano | `handheld documentary camera, subtle shake` | realismo, comedia de oficina, urgencia | prohibida en infantil |
| Zoom brusco | `snap zoom` / `crash zoom into his face` | sorpresa cómica | prohibido en infantil |
| Paneo látigo | `whip pan` | transición enérgica | prohibido en infantil; mejor resolverlo en edición |
| Dron | `aerial drone shot` | escala, paisaje | — |
| FPV | `fpv drone diving through` | adrenalina («M») | alto riesgo de deformar al personaje |
| Vértigo | `dolly zoom` | shock, revelación | difícil; probar en borrador |

### Velocidades

`very slowly`, `slowly`, `smoothly`, `steadily`, `quickly`. En infantil, siempre `slowly` o `very slowly`.

## Reglas para no gastar de más

1. **Un movimiento por toma.** Dos movimientos (paneo + zoom) duplican los fallos.
2. **Lo que la edición hace gratis no se genera:** zoom sobre un fotograma, `whip pan` de transición, cámara lenta,
   repetición, reencuadre a 9:16 (`postpro.py`, cap. 07).
3. **El personaje grande en cuadro.** En planos generales el modelo deforma más la cara: para reconocerlo, plano medio
   o primer plano.
4. **Encadenar tomas:** el último fotograma de una toma (`postpro.py fotograma --ultimo`) es el keyframe de la
   siguiente. Así la continuidad sale gratis.
5. **Kling 3.0 y Seedance** respetan bien los movimientos descritos con inicio y fin. Si un modelo ignora la cámara,
   se prueba `static` + movimiento en edición antes que regenerar.
