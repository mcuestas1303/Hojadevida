# 04 · Animación y actuación

El modelo de video anima lo que se le describe. Si el prompt dice «está feliz», sale una sonrisa quieta; si dice
**qué hace el cuerpo**, sale actuación. Se escribe siempre el **verbo físico**, no la emoción.

## Principios que sí se pueden pedir en un prompt

| Principio | Cómo se pide | Ejemplo |
|---|---|---|
| **Anticipación** | un pequeño movimiento contrario antes de la acción | `crouches down slightly, then jumps up` |
| **Acción secundaria** | algo que acompaña sin robar atención | `while walking, his tuft of feathers bounces` |
| **Seguimiento (follow-through)** | lo que sigue moviéndose al parar | `the feather boa keeps swinging after he stops` |
| **Squash & stretch** (juguetes) | el cuerpo se aplasta y se estira | `his egg-shaped body squashes on landing and stretches on the jump` |
| **Timing** | velocidad explícita por emoción | `slowly`, `in a quick snap`, `holds the pose for a beat` |
| **Pose clara (silueta)** | pose final legible en negro | `ends in a clear pose with wings raised high` |
| **Mirada** | dónde mira y cuándo cambia | `looks at the box, then turns his eyes to the camera` |
| **Pausa (hold)** | quietud antes del remate | `freezes completely for a moment` |

## Verbos por emoción

| Emoción | Verbos para el cuerpo | Cara |
|---|---|---|
| Alegría | bounces, hops, claps, spins, wiggles | eyes squeezed in a big smile |
| Tristeza | slumps, drags his feet, sighs, droops | teary eyes, trembling lower lip |
| Enojo (suave) | stomps, puffs up, crosses arms | puffed cheeks, furrowed brow |
| Miedo | shrinks back, trembles, hides behind | wide eyes, tiny pupils |
| Sorpresa | jumps back, freezes, drops what he holds | eyes wide open, mouth in a round O |
| Curiosidad | tilts head, leans forward on tiptoes, sniffs, pokes gently | eyes widen with interest |
| Ternura | hugs, nuzzles, rocks gently | soft half-closed eyes |
| Orgullo | puffs chest out, lifts chin, plants feet wide | confident grin |
| Vergüenza | looks away, covers face, shuffles | blushing cheeks |
| Determinación | plants feet, raises fist, nods once | focused narrow eyes |
| Aburrimiento | slumps, rests chin on hand, taps foot | half-closed eyes |
| Humor deadpan | moves minimally, precise deliberate gestures | completely serious face |

## Banco de gestos del elenco (no se cambian)

| Personaje | Gesto propio | Cómo se mueve | Nunca |
|---|---|---|---|
| **Tiky** | se inclina hacia adelante en puntas y ladea la cabeza ante algo nuevo | saltitos cortos, alas que aletean rápido al emocionarse, el copete rebota | movimientos bruscos o peligrosos, burlarse |
| **Lumi** | se lleva una pezuña al mentón antes de mostrar algo; saca el crayón lila solo para marcar o dibujar | lenta, segura, pasos pesados y suaves | regañar, hacer las cosas por Tiky |
| **Spike** | explica con las dos manos, dedo dramático sobre la tecla | movimientos largos por sus brazos larguísimos, poses de estrella de rock; la boa sigue moviéndose | perder la seriedad antes del remate |
| **«M»** (solo adultos) | por definir con el dueño | movimientos atléticos, controlados | cruzarse con contenido infantil |

## Usar las hojas de personaje

Las hojas de `02 Hojas de personaje` (vueltas + 16 emociones) son la **referencia de actuación**:

1. Para el keyframe, se elige el panel de la emoción de esa toma y se describe esa expresión con las palabras de la
   hoja (`creador-personajes/hojas/tiky-y-lumi.md`).
2. Para un ángulo de espaldas o de perfil, se pasa la hoja de vueltas como referencia adicional.
3. La imagen principal (`01 Diseño aprobado`) va **siempre** como referencia 1; la hoja, como apoyo.

## Transferencia de movimiento

Cuando la actuación es difícil de describir (un baile, un trend, un gesto exacto), se graba y se transfiere:

| Herramienta | Qué hace | Cuándo |
|---|---|---|
| `motion_control` (Kling 3.0 Motion Control) | anima una imagen del personaje con el movimiento y la cámara de un clip | un personaje, un clip guía; `scene_control: image` mantiene el fondo del personaje |
| `generate_video` con modelo `hf_mult_motion_control` (Genjutsu) | copia movimiento, gestos o cámara de un clip a los personajes de las imágenes | uno o varios personajes, trend o baile |
| `generate_video` con `hf_mult_replace_object` | cambia un objeto, prenda o personaje dentro de un clip existente | el clip ya está bien y solo hay que cambiar algo |

Reglas (decisión del dueño): **el clip guía es propio** (lo graba el dueño o alguien con permiso), no un video de
terceros calcado. Grabar con el cuerpo entero en cuadro, fondo limpio, buena luz, sin cortes, y la duración exacta
que se va a usar (se paga por segundo).
