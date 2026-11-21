<!-- Copia archivada. Se edita en proyectos/2026-11-20_hola_granja/02_prompt/prompt.md y se vuelve a archivar. -->
# Prompt de video — Hola, granja

## 1. Ficha técnica

- **Proyecto:** proyectos/2026-11-20_hola_granja
- **Tipo:** capítulo
- **Número:** 1
- **Serie:** granja
- **Objetivo de aprendizaje:** levanta y mueve la mano para saludar cuando se le dice «saluda con la mano» o cuando Tiky o Lumi lo saludan a cámara.
- **Generador:** Higgsfield: keyframes con Nano Banana 2; clips con Seedance 2.0 Mini, imagen→video, sin audio
- **Aspecto:** 16:9 (video largo de YouTube, según formatos.md; las imágenes de referencia de los personajes son 9:16, así que cada keyframe se pide en 16:9)
- **Duración total:** 88 s
- **Resolución de borrador:** 480p
- **Resolución final:** clips a 720p (solo las tomas aprobadas); máster de 1920x1080 al ensamblar
- **Precio por segundo:** 0.5
- **Intentos estimados por toma:** 2

## 2. Elenco

| Personaje | Papel en este video | Vestuario | Referencia que se sube |
|---|---|---|---|
| @tiky | El niño: saluda con el ala, se equivoca una vez y repite | base | personajes/tiky/referencias/3d_principal.png (ID de Higgsfield 6cff1fa4-a734-402c-9384-7a76c5ee6bd3) |
| @lumi | El adulto que acompaña: espera, muestra el saludo despacio y contesta | base | personajes/lumi/referencias/3d_principal.png (ID de Higgsfield aea1a3a4-5067-48ed-beb3-226b70e1ff8f) |

## 3. Idea en una línea

Tiky y Lumi llegan al patio de la granja y saludan con el ala y la pezuña; el niño aprende a levantar y mover la mano para decir hola, con calma, y termina saludando en casa a un peluche.

## 4. Estilo global

Bloque que se pega igual al final de todos los prompts de imagen y de video (copiado de series/granja/serie.md).

```text
Modern 3D cartoon render, soft matte vinyl toy figures, children's animation style, simple rounded shapes, clean bright colors, soft even daylight, gentle soft shadows, uncluttered background, calm and slow, eye-level camera at the chick's height.
```

**Negativo global:**

```text
text, letters, watermark, logo, extra characters, extra animals, humans, realistic fur, scary faces, sharp teeth, dark shadows, night, fire, weapons, fast motion, motion blur, camera shake, flashing lights
```

## 5. Escenarios

- **patio:** bloque del lugar de series/granja/entorno.md, pegado tal cual en cada prompt de keyframe. Siempre de día, luz pareja, mismo patio en las 16 tomas.

```text
A toy farmyard at toy scale on a sunny playroom floor: a small red wooden toy barn with a white roof on the left, a low white wooden fence behind, a soft pastel green felt mat as grass, plain pastel sky-blue wall in the background.
```

## 6. Tomas

Reutilización de keyframes (para ahorrar): el episodio tiene solo tres encuadres, A (Tiky solo), B (Lumi sola) y C (los dos). Se generan 4 imágenes en total: Keyframe A (toma 6), Keyframe B (tomas 3 y 9), Keyframe C (tomas 4, 5, 14 y 16) y Keyframe C-entrada (tomas 1 y 12; es el encuadre C con los dos al fondo, para que entren caminando). Las tomas encadenadas (2, 7, 8, 10, 11, 13 y 15) parten del último fotograma de la toma anterior y no necesitan keyframe nuevo. Los keyframes se repiten hasta que los personajes salgan fieles a su ficha, antes de animar.

Planos continuos: las tomas 6, 7 y 8 forman el plano 5–7 (18 s) y las tomas 9, 10 y 11 el plano 8–10 (18 s), sin corte visible. Las pausas (tomas 7 y 10) son tomas vivas generadas, no imagen congelada.

### Toma 1 — Entrada al patio

- **Duración:** 5 s
- **Personajes:** @tiky, @lumi
- **Método:** imagen→video
- **Escenario:** patio
- **Encuadre:** plano general, cuerpo completo, Encuadre C (inicio al fondo), a la altura de los ojos de Tiky
- **Cámara:** fija
- **Acción:** Los dos caminan despacio hacia cámara, uno al lado del otro, y se detienen mirando a cámara. Camina 4 s y queda quieto 1 s.
- **Audio:** Música suave de 0 a 4 s con fundido lento en los últimos 2 s; pasos sobre fieltro. La voz «Esta es la granja» empieza hacia el s 4 de la toma, sobre silencio y pájaros lejanos, sin gesto.
- **Referencia:** Plano 1 (0–5 s). Keyframe de partida: Keyframe C-entrada: se genera una vez y se reutiliza en las tomas 1 y 12.

**Prompt de keyframe:**

```text
Tiky, an adorable baby chick shaped like a smooth upright egg with no neck, warm sunflower yellow body with a pale butter-cream belly, a small discreet tuft of three short rounded flame-shaped feathers in red-orange on top of his head, big round dark-brown eyes with a white sparkle, no eyebrows, a small rounded coral-peach beak, soft rosy cheeks, tiny stubby wings, short coral-peach feet with three round toes.
Lumi, an adorable gentle cow shaped like a big smooth upright egg with no neck, about one and a half times as tall as Tiky, mostly creamy white with two large irregular black patches with soft wavy edges (one across her back and belly, one on top of her head between her horns), black lower legs like little socks, small lilac purple hooves, small cream rounded horns, small floppy ears with lilac insides, big warm honey-brown eyes with a white sparkle, soft gentle eyebrows, a wide rounded soft lilac muzzle with two small dot nostrils, a short chunky lilac crayon tucked behind her right ear.
Wide full-body shot of both characters standing far back near the low white fence, small in the frame, facing the camera, Lumi on the left of Tiky, wings and forelegs down. Fixed eye-level camera at the chick's height.
A toy farmyard at toy scale on a sunny playroom floor: a small red wooden toy barn with a white roof on the left, a low white wooden fence behind, a soft pastel green felt mat as grass, plain pastel sky-blue wall in the background.
Modern 3D cartoon render, soft matte vinyl toy figures, children's animation style, simple rounded shapes, clean bright colors, soft even daylight, gentle soft shadows, uncluttered background, calm and slow, eye-level camera at the chick's height.
```

**Prompt de video:**

```text
CRITICAL: no written words, letters, brand marks or watermarks anywhere.
CRITICAL: Tiky and Lumi keep exactly the same design, colors and proportions as in the start image from the first frame to the last; nothing is added or removed.
CRITICAL: fixed camera, no zoom, no pan, no cut inside the clip; slow, gentle movement only.
CRITICAL: nothing comes out of or moves inside the barn door; no other characters or animals appear.
Tiky and Lumi walk slowly toward the camera side by side with small steady steps, Lumi on the left. They stop at the center of the yard, look at the camera and stand still for the last second.
Fixed camera, no zoom, no pan.
Modern 3D cartoon render, soft matte vinyl toy figures, children's animation style, simple rounded shapes, clean bright colors, soft even daylight, gentle soft shadows, uncluttered background, calm and slow, eye-level camera at the chick's height.
```

### Toma 2 — Saludo a cámara

- **Duración:** 5 s
- **Personajes:** @tiky, @lumi
- **Método:** imagen→video
- **Escenario:** patio
- **Encuadre:** plano general, cuerpo completo, Encuadre C
- **Cámara:** fija
- **Acción:** Los dos miran a cámara; hacia el s 1,5 levantan a la vez el ala y la pezuña, los mueven dos veces despacio y los dejan en alto 2 s.
- **Audio:** Voz: «Hola» cae entre los s 2 y 3 de la toma, sobre el segundo movimiento. El final de «Esta es la granja» suena hasta cerca del s 1. Del s 3 al 5, silencio con el ala y la pezuña en alto.
- **Referencia:** Plano 1 (5–10 s). Keyframe de partida: Último fotograma de la Toma 1 (encadenada, no se genera keyframe nuevo; el prompt de abajo es solo el respaldo si hay que regenerarlo).

**Prompt de keyframe:**

```text
Tiky, an adorable baby chick shaped like a smooth upright egg with no neck, warm sunflower yellow body with a pale butter-cream belly, a small discreet tuft of three short rounded flame-shaped feathers in red-orange on top of his head, big round dark-brown eyes with a white sparkle, no eyebrows, a small rounded coral-peach beak, soft rosy cheeks, tiny stubby wings, short coral-peach feet with three round toes.
Lumi, an adorable gentle cow shaped like a big smooth upright egg with no neck, about one and a half times as tall as Tiky, mostly creamy white with two large irregular black patches with soft wavy edges (one across her back and belly, one on top of her head between her horns), black lower legs like little socks, small lilac purple hooves, small cream rounded horns, small floppy ears with lilac insides, big warm honey-brown eyes with a white sparkle, soft gentle eyebrows, a wide rounded soft lilac muzzle with two small dot nostrils, a short chunky lilac crayon tucked behind her right ear.
Full-body shot of both characters facing the camera, standing side by side and centered, Lumi on the left of Tiky, wings and forelegs down, small gentle smiles. Fixed eye-level camera at the chick's height.
This is the last frame of Toma 1; keep pose, position, size and light.
A toy farmyard at toy scale on a sunny playroom floor: a small red wooden toy barn with a white roof on the left, a low white wooden fence behind, a soft pastel green felt mat as grass, plain pastel sky-blue wall in the background.
Modern 3D cartoon render, soft matte vinyl toy figures, children's animation style, simple rounded shapes, clean bright colors, soft even daylight, gentle soft shadows, uncluttered background, calm and slow, eye-level camera at the chick's height.
```

**Prompt de video:**

```text
CRITICAL: no written words, letters, brand marks or watermarks anywhere.
CRITICAL: Tiky and Lumi keep exactly the same design, colors and proportions as in the start image from the first frame to the last; nothing is added or removed.
CRITICAL: fixed camera, no zoom, no pan, no cut inside the clip; slow, gentle movement only.
CRITICAL: nothing comes out of or moves inside the barn door; no other characters or animals appear.
Tiky and Lumi look at the camera. After a moment Tiky raises his right wing slowly and waves it twice with small gentle movements, never flapping while Lumi raises her right foreleg slowly and waves the lilac hoof twice with small gentle movements, never stamping, both at the same slow pace. Then both keep the wing and the hoof raised and keep looking at the camera until the end.
Fixed camera, no zoom, no pan.
Modern 3D cartoon render, soft matte vinyl toy figures, children's animation style, simple rounded shapes, clean bright colors, soft even daylight, gentle soft shadows, uncluttered background, calm and slow, eye-level camera at the chick's height.
```

### Toma 3 — Lumi dice hola

- **Duración:** 7 s
- **Personajes:** @lumi
- **Método:** imagen→video
- **Escenario:** patio
- **Encuadre:** plano general, cuerpo completo, Encuadre B (misma cámara y mismo tamaño que el keyframe B)
- **Cámara:** fija
- **Acción:** Lumi mira a cámara, levanta la pezuña, la mueve dos veces despacio y la baja después de la voz.
- **Audio:** «Muu» suave al empezar (s 0 a 1), con Lumi mirando a cámara. Voz «Lumi dice hola.»: «Lumi dice» de 2,5 a 3,5 s y «hola» de 3,5 a 4,5 s, sobre el segundo movimiento. Pezuña baja hacia el s 5,5. Nada después de «hola».
- **Referencia:** Plano 2. Keyframe de partida: Keyframe B: se genera una vez y se reutiliza.

**Prompt de keyframe:**

```text
Lumi, an adorable gentle cow shaped like a big smooth upright egg with no neck, about one and a half times as tall as Tiky, mostly creamy white with two large irregular black patches with soft wavy edges (one across her back and belly, one on top of her head between her horns), black lower legs like little socks, small lilac purple hooves, small cream rounded horns, small floppy ears with lilac insides, big warm honey-brown eyes with a white sparkle, soft gentle eyebrows, a wide rounded soft lilac muzzle with two small dot nostrils, a short chunky lilac crayon tucked behind her right ear.
Full-body shot of Lumi alone, centered in the frame in front of the red barn, facing the camera, forelegs down at her sides, a small gentle smile, with space above her horns and below her hooves. Fixed eye-level camera.
A toy farmyard at toy scale on a sunny playroom floor: a small red wooden toy barn with a white roof on the left, a low white wooden fence behind, a soft pastel green felt mat as grass, plain pastel sky-blue wall in the background.
Modern 3D cartoon render, soft matte vinyl toy figures, children's animation style, simple rounded shapes, clean bright colors, soft even daylight, gentle soft shadows, uncluttered background, calm and slow, eye-level camera at the chick's height.
```

**Prompt de video:**

```text
CRITICAL: no written words, letters, brand marks or watermarks anywhere.
CRITICAL: Lumi keeps exactly the same design, colors and proportions as in the start image from the first frame to the last; nothing is added or removed.
CRITICAL: fixed camera, no zoom, no pan, no cut inside the clip; slow, gentle movement only.
CRITICAL: nothing comes out of or moves inside the barn door; no other characters or animals appear.
Lumi looks at the camera. She raises her right foreleg slowly and waves the lilac hoof twice with small gentle movements, never stamping, then lowers the hoof slowly at about five and a half seconds and keeps looking at the camera with a gentle smile.
Fixed camera, no zoom, no pan.
Modern 3D cartoon render, soft matte vinyl toy figures, children's animation style, simple rounded shapes, clean bright colors, soft even daylight, gentle soft shadows, uncluttered background, calm and slow, eye-level camera at the chick's height.
```

### Toma 4 — Tiky saluda hacia un lado

- **Duración:** 6 s
- **Personajes:** @tiky, @lumi
- **Método:** imagen→video
- **Escenario:** patio
- **Encuadre:** plano general, cuerpo completo, Encuadre C
- **Cámara:** fija
- **Acción:** Tiky levanta el ala, hace un movimiento pequeño y corto mirando hacia un lado, no a Lumi. Lumi lo mira tranquila y atenta, con la cabeza un poco inclinada.
- **Audio:** Sin voz ni música. Un «pío» suave de Tiky hacia el s 1. Lumi, silencio.
- **Referencia:** Plano 3. Keyframe de partida: Keyframe C: se genera una vez y se reutiliza.

**Prompt de keyframe:**

```text
Tiky, an adorable baby chick shaped like a smooth upright egg with no neck, warm sunflower yellow body with a pale butter-cream belly, a small discreet tuft of three short rounded flame-shaped feathers in red-orange on top of his head, big round dark-brown eyes with a white sparkle, no eyebrows, a small rounded coral-peach beak, soft rosy cheeks, tiny stubby wings, short coral-peach feet with three round toes.
Lumi, an adorable gentle cow shaped like a big smooth upright egg with no neck, about one and a half times as tall as Tiky, mostly creamy white with two large irregular black patches with soft wavy edges (one across her back and belly, one on top of her head between her horns), black lower legs like little socks, small lilac purple hooves, small cream rounded horns, small floppy ears with lilac insides, big warm honey-brown eyes with a white sparkle, soft gentle eyebrows, a wide rounded soft lilac muzzle with two small dot nostrils, a short chunky lilac crayon tucked behind her right ear.
Full-body shot of both characters facing the camera, standing side by side and centered, Lumi on the left of Tiky, wings and forelegs down, small gentle smiles. Fixed eye-level camera at the chick's height.
A toy farmyard at toy scale on a sunny playroom floor: a small red wooden toy barn with a white roof on the left, a low white wooden fence behind, a soft pastel green felt mat as grass, plain pastel sky-blue wall in the background.
Modern 3D cartoon render, soft matte vinyl toy figures, children's animation style, simple rounded shapes, clean bright colors, soft even daylight, gentle soft shadows, uncluttered background, calm and slow, eye-level camera at the chick's height.
```

**Prompt de video:**

```text
CRITICAL: no written words, letters, brand marks or watermarks anywhere.
CRITICAL: Tiky and Lumi keep exactly the same design, colors and proportions as in the start image from the first frame to the last; nothing is added or removed.
CRITICAL: fixed camera, no zoom, no pan, no cut inside the clip; slow, gentle movement only.
CRITICAL: nothing comes out of or moves inside the barn door; no other characters or animals appear.
Tiky looks away to his right, away from Lumi, raises his right wing and makes one small short wave, then lowers it. Lumi, on the left, looks calmly at Tiky with her head tilted a little and a soft relaxed face, waiting.
Fixed camera, no zoom, no pan.
Modern 3D cartoon render, soft matte vinyl toy figures, children's animation style, simple rounded shapes, clean bright colors, soft even daylight, gentle soft shadows, uncluttered background, calm and slow, eye-level camera at the chick's height.
```

### Toma 5 — Tiky saluda a Lumi y ella contesta

- **Duración:** 7 s
- **Personajes:** @tiky, @lumi
- **Método:** imagen→video
- **Escenario:** patio
- **Encuadre:** plano general, cuerpo completo, Encuadre C
- **Cámara:** fija
- **Acción:** Tiky se gira hacia Lumi, la mira y la saluda con el ala, despacio. Después Lumi levanta la pezuña y le contesta.
- **Audio:** «Pío» suave hacia el s 1,2 y «muu» suave hacia el s 3,2, antes de la voz. Voz «Tiky saludó a Lumi.» de 5 a 7 s, cuando Lumi ya bajó la pezuña. Sin música.
- **Referencia:** Plano 4. Keyframe de partida: Keyframe C: se genera una vez y se reutiliza.

**Prompt de keyframe:**

```text
Tiky, an adorable baby chick shaped like a smooth upright egg with no neck, warm sunflower yellow body with a pale butter-cream belly, a small discreet tuft of three short rounded flame-shaped feathers in red-orange on top of his head, big round dark-brown eyes with a white sparkle, no eyebrows, a small rounded coral-peach beak, soft rosy cheeks, tiny stubby wings, short coral-peach feet with three round toes.
Lumi, an adorable gentle cow shaped like a big smooth upright egg with no neck, about one and a half times as tall as Tiky, mostly creamy white with two large irregular black patches with soft wavy edges (one across her back and belly, one on top of her head between her horns), black lower legs like little socks, small lilac purple hooves, small cream rounded horns, small floppy ears with lilac insides, big warm honey-brown eyes with a white sparkle, soft gentle eyebrows, a wide rounded soft lilac muzzle with two small dot nostrils, a short chunky lilac crayon tucked behind her right ear.
Full-body shot of both characters facing the camera, standing side by side and centered, Lumi on the left of Tiky, wings and forelegs down, small gentle smiles. Fixed eye-level camera at the chick's height.
A toy farmyard at toy scale on a sunny playroom floor: a small red wooden toy barn with a white roof on the left, a low white wooden fence behind, a soft pastel green felt mat as grass, plain pastel sky-blue wall in the background.
Modern 3D cartoon render, soft matte vinyl toy figures, children's animation style, simple rounded shapes, clean bright colors, soft even daylight, gentle soft shadows, uncluttered background, calm and slow, eye-level camera at the chick's height.
```

**Prompt de video:**

```text
CRITICAL: no written words, letters, brand marks or watermarks anywhere.
CRITICAL: Tiky and Lumi keep exactly the same design, colors and proportions as in the start image from the first frame to the last; nothing is added or removed.
CRITICAL: fixed camera, no zoom, no pan, no cut inside the clip; slow, gentle movement only.
CRITICAL: nothing comes out of or moves inside the barn door; no other characters or animals appear.
Tiky turns toward Lumi and looks at her. He raises his right wing and waves it slowly, then lowers it. Lumi looks back at him, raises her right foreleg, waves the lilac hoof slowly and lowers it at about four and a half seconds. Both end looking at each other with gentle smiles.
Fixed camera, no zoom, no pan.
Modern 3D cartoon render, soft matte vinyl toy figures, children's animation style, simple rounded shapes, clean bright colors, soft even daylight, gentle soft shadows, uncluttered background, calm and slow, eye-level camera at the chick's height.
```

### Toma 6 — Tiky pregunta con el ala

- **Duración:** 7 s
- **Personajes:** @tiky
- **Método:** imagen→video
- **Escenario:** patio
- **Encuadre:** plano general, cuerpo completo, Encuadre A
- **Cámara:** fija
- **Acción:** Tiky mira su ala, mira a cámara y vuelve a su ala; la levanta, la mueve dos veces; mira a cámara y baja el ala despacio. Toma continua con las tomas 7 y 8.
- **Audio:** Sin música. Voz «Tiky dice hola.» de 2 a 4 s, con «hola» sobre el saludo; «¿Y tú? Saluda con la mano.» de 4 a 7 s, con Tiky mirando a cámara y bajando el ala. Los primeros 2 s, silencio.
- **Referencia:** Plano 5 (inicio del plano continuo 5–7). Keyframe de partida: Keyframe A: se genera una vez y se reutiliza.

**Prompt de keyframe:**

```text
Tiky, an adorable baby chick shaped like a smooth upright egg with no neck, warm sunflower yellow body with a pale butter-cream belly, a small discreet tuft of three short rounded flame-shaped feathers in red-orange on top of his head, big round dark-brown eyes with a white sparkle, no eyebrows, a small rounded coral-peach beak, soft rosy cheeks, tiny stubby wings, short coral-peach feet with three round toes.
Full-body shot of Tiky centered in front of the red barn, facing the camera, wings down at his sides, a small gentle smile. Fixed eye-level camera at the chick's height.
A toy farmyard at toy scale on a sunny playroom floor: a small red wooden toy barn with a white roof on the left, a low white wooden fence behind, a soft pastel green felt mat as grass, plain pastel sky-blue wall in the background.
Modern 3D cartoon render, soft matte vinyl toy figures, children's animation style, simple rounded shapes, clean bright colors, soft even daylight, gentle soft shadows, uncluttered background, calm and slow, eye-level camera at the chick's height.
```

**Prompt de video:**

```text
CRITICAL: no written words, letters, brand marks or watermarks anywhere.
CRITICAL: Tiky keeps exactly the same design, colors and proportions as in the start image from the first frame to the last; nothing is added or removed.
CRITICAL: fixed camera, no zoom, no pan, no cut inside the clip; slow, gentle movement only.
CRITICAL: nothing comes out of or moves inside the barn door; no other characters or animals appear.
Tiky looks down at his right wing, looks up at the camera, then looks at his wing again (first two seconds). Then he raises his right wing slowly and waves it twice with small gentle movements, never flapping. From four seconds he looks at the camera, lowers the wing slowly and waits with the wing down, still looking at the camera.
Fixed camera, no zoom, no pan.
Modern 3D cartoon render, soft matte vinyl toy figures, children's animation style, simple rounded shapes, clean bright colors, soft even daylight, gentle soft shadows, uncluttered background, calm and slow, eye-level camera at the chick's height.
```

### Toma 7 — Tiky espera (pausa viva)

- **Duración:** 5 s
- **Personajes:** @tiky
- **Método:** imagen→video
- **Escenario:** patio
- **Encuadre:** plano general, cuerpo completo, Encuadre A
- **Cámara:** fija
- **Acción:** Tiky mira a cámara con el ala baja y se mueve poco: parpadea, respira suave, sonríe leve y ladea la cabeza. Sin gesto nuevo.
- **Audio:** Silencio: sin voz ni música. Solo ambiente muy suave.
- **Referencia:** Plano 6 (continuo con 5 y 7). Keyframe de partida: Último fotograma de la Toma 6 (encadenada, no se genera keyframe nuevo; el prompt de abajo es solo el respaldo si hay que regenerarlo).

**Prompt de keyframe:**

```text
Tiky, an adorable baby chick shaped like a smooth upright egg with no neck, warm sunflower yellow body with a pale butter-cream belly, a small discreet tuft of three short rounded flame-shaped feathers in red-orange on top of his head, big round dark-brown eyes with a white sparkle, no eyebrows, a small rounded coral-peach beak, soft rosy cheeks, tiny stubby wings, short coral-peach feet with three round toes.
Full-body shot of Tiky centered in front of the red barn, facing the camera, wings down at his sides, a small gentle smile. Fixed eye-level camera at the chick's height.
This is the last frame of Toma 6; keep pose, position, size and light.
A toy farmyard at toy scale on a sunny playroom floor: a small red wooden toy barn with a white roof on the left, a low white wooden fence behind, a soft pastel green felt mat as grass, plain pastel sky-blue wall in the background.
Modern 3D cartoon render, soft matte vinyl toy figures, children's animation style, simple rounded shapes, clean bright colors, soft even daylight, gentle soft shadows, uncluttered background, calm and slow, eye-level camera at the chick's height.
```

**Prompt de video:**

```text
CRITICAL: no written words, letters, brand marks or watermarks anywhere.
CRITICAL: Tiky keeps exactly the same design, colors and proportions as in the start image from the first frame to the last; nothing is added or removed.
CRITICAL: fixed camera, no zoom, no pan, no cut inside the clip; slow, gentle movement only.
CRITICAL: nothing comes out of or moves inside the barn door; no other characters or animals appear.
Tiky stands with his wing down and looks at the camera. He blinks twice, breathes softly, smiles slightly and tilts his head a little. He does nothing else and his wings stay down.
Fixed camera, no zoom, no pan.
Modern 3D cartoon render, soft matte vinyl toy figures, children's animation style, simple rounded shapes, clean bright colors, soft even daylight, gentle soft shadows, uncluttered background, calm and slow, eye-level camera at the chick's height.
```

### Toma 8 — Tiky responde hola

- **Duración:** 6 s
- **Personajes:** @tiky
- **Método:** imagen→video
- **Escenario:** patio
- **Encuadre:** plano general, cuerpo completo, Encuadre A
- **Cámara:** fija
- **Acción:** Tiky, con el ala baja, mira a cámara y saluda con el ala despacio, dos veces. La baja y sonríe en silencio.
- **Audio:** «Pío» suave al empezar (s 0 a 1), antes de la voz. Voz «Hola.» entre los s 2 y 3, sobre el saludo con el ala en alto, no cuando ya bajó. Del s 4 al 6, silencio. Sin música.
- **Referencia:** Plano 7 (final del plano continuo 5–7). Keyframe de partida: Último fotograma de la Toma 7 (encadenada, no se genera keyframe nuevo; el prompt de abajo es solo el respaldo si hay que regenerarlo).

**Prompt de keyframe:**

```text
Tiky, an adorable baby chick shaped like a smooth upright egg with no neck, warm sunflower yellow body with a pale butter-cream belly, a small discreet tuft of three short rounded flame-shaped feathers in red-orange on top of his head, big round dark-brown eyes with a white sparkle, no eyebrows, a small rounded coral-peach beak, soft rosy cheeks, tiny stubby wings, short coral-peach feet with three round toes.
Full-body shot of Tiky centered in front of the red barn, facing the camera, wings down at his sides, a small gentle smile. Fixed eye-level camera at the chick's height.
This is the last frame of Toma 7; keep pose, position, size and light.
A toy farmyard at toy scale on a sunny playroom floor: a small red wooden toy barn with a white roof on the left, a low white wooden fence behind, a soft pastel green felt mat as grass, plain pastel sky-blue wall in the background.
Modern 3D cartoon render, soft matte vinyl toy figures, children's animation style, simple rounded shapes, clean bright colors, soft even daylight, gentle soft shadows, uncluttered background, calm and slow, eye-level camera at the chick's height.
```

**Prompt de video:**

```text
CRITICAL: no written words, letters, brand marks or watermarks anywhere.
CRITICAL: Tiky keeps exactly the same design, colors and proportions as in the start image from the first frame to the last; nothing is added or removed.
CRITICAL: fixed camera, no zoom, no pan, no cut inside the clip; slow, gentle movement only.
CRITICAL: nothing comes out of or moves inside the barn door; no other characters or animals appear.
Tiky stands with his wing down and looks at the camera. At one second he raises his right wing slowly and waves it twice with small gentle movements, never flapping. He lowers the wing at about four seconds and smiles quietly at the camera until the end.
Fixed camera, no zoom, no pan.
Modern 3D cartoon render, soft matte vinyl toy figures, children's animation style, simple rounded shapes, clean bright colors, soft even daylight, gentle soft shadows, uncluttered background, calm and slow, eye-level camera at the chick's height.
```

### Toma 9 — Lumi pregunta con la pezuña

- **Duración:** 7 s
- **Personajes:** @lumi
- **Método:** imagen→video
- **Escenario:** patio
- **Encuadre:** plano general, cuerpo completo, Encuadre B (misma cámara y mismo tamaño que el keyframe B)
- **Cámara:** fija
- **Acción:** Lumi mira su pezuña, mira a cámara y vuelve a su pezuña; la levanta, la mueve dos veces; mira a cámara y baja la pezuña despacio. Toma continua con las tomas 10 y 11.
- **Audio:** Sin música. Voz «Lumi dice hola.» de 2 a 4 s, con «hola» sobre el saludo; «¿Y tú? Saluda con la mano.» de 4 a 7 s, con Lumi mirando a cámara y bajando la pezuña. Los primeros 2 s, silencio.
- **Referencia:** Plano 8 (inicio del plano continuo 8–10). Keyframe de partida: Keyframe B: se genera una vez y se reutiliza.

**Prompt de keyframe:**

```text
Lumi, an adorable gentle cow shaped like a big smooth upright egg with no neck, about one and a half times as tall as Tiky, mostly creamy white with two large irregular black patches with soft wavy edges (one across her back and belly, one on top of her head between her horns), black lower legs like little socks, small lilac purple hooves, small cream rounded horns, small floppy ears with lilac insides, big warm honey-brown eyes with a white sparkle, soft gentle eyebrows, a wide rounded soft lilac muzzle with two small dot nostrils, a short chunky lilac crayon tucked behind her right ear.
Full-body shot of Lumi alone, centered in the frame in front of the red barn, facing the camera, forelegs down at her sides, a small gentle smile, with space above her horns and below her hooves. Fixed eye-level camera.
A toy farmyard at toy scale on a sunny playroom floor: a small red wooden toy barn with a white roof on the left, a low white wooden fence behind, a soft pastel green felt mat as grass, plain pastel sky-blue wall in the background.
Modern 3D cartoon render, soft matte vinyl toy figures, children's animation style, simple rounded shapes, clean bright colors, soft even daylight, gentle soft shadows, uncluttered background, calm and slow, eye-level camera at the chick's height.
```

**Prompt de video:**

```text
CRITICAL: no written words, letters, brand marks or watermarks anywhere.
CRITICAL: Lumi keeps exactly the same design, colors and proportions as in the start image from the first frame to the last; nothing is added or removed.
CRITICAL: fixed camera, no zoom, no pan, no cut inside the clip; slow, gentle movement only.
CRITICAL: nothing comes out of or moves inside the barn door; no other characters or animals appear.
Lumi looks down at her right hoof, looks up at the camera, then looks at the hoof again (first two seconds). Then she raises her right foreleg slowly and waves the lilac hoof twice with small gentle movements, never stamping. From four seconds she looks at the camera, lowers the hoof slowly and waits with the hoof down, still looking at the camera.
Fixed camera, no zoom, no pan.
Modern 3D cartoon render, soft matte vinyl toy figures, children's animation style, simple rounded shapes, clean bright colors, soft even daylight, gentle soft shadows, uncluttered background, calm and slow, eye-level camera at the chick's height.
```

### Toma 10 — Lumi espera (pausa viva)

- **Duración:** 5 s
- **Personajes:** @lumi
- **Método:** imagen→video
- **Escenario:** patio
- **Encuadre:** plano general, cuerpo completo, Encuadre B (misma cámara y mismo tamaño que el keyframe B)
- **Cámara:** fija
- **Acción:** Lumi mira a cámara con la pezuña baja y se mueve poco: parpadea, respira suave y sonríe leve. Sin gesto nuevo.
- **Audio:** Silencio: sin voz ni música. Solo ambiente muy suave.
- **Referencia:** Plano 9 (continuo con 8 y 10). Keyframe de partida: Último fotograma de la Toma 9 (encadenada, no se genera keyframe nuevo; el prompt de abajo es solo el respaldo si hay que regenerarlo).

**Prompt de keyframe:**

```text
Lumi, an adorable gentle cow shaped like a big smooth upright egg with no neck, about one and a half times as tall as Tiky, mostly creamy white with two large irregular black patches with soft wavy edges (one across her back and belly, one on top of her head between her horns), black lower legs like little socks, small lilac purple hooves, small cream rounded horns, small floppy ears with lilac insides, big warm honey-brown eyes with a white sparkle, soft gentle eyebrows, a wide rounded soft lilac muzzle with two small dot nostrils, a short chunky lilac crayon tucked behind her right ear.
Full-body shot of Lumi alone, centered in the frame in front of the red barn, facing the camera, forelegs down at her sides, a small gentle smile, with space above her horns and below her hooves. Fixed eye-level camera.
This is the last frame of Toma 9; keep pose, position, size and light.
A toy farmyard at toy scale on a sunny playroom floor: a small red wooden toy barn with a white roof on the left, a low white wooden fence behind, a soft pastel green felt mat as grass, plain pastel sky-blue wall in the background.
Modern 3D cartoon render, soft matte vinyl toy figures, children's animation style, simple rounded shapes, clean bright colors, soft even daylight, gentle soft shadows, uncluttered background, calm and slow, eye-level camera at the chick's height.
```

**Prompt de video:**

```text
CRITICAL: no written words, letters, brand marks or watermarks anywhere.
CRITICAL: Lumi keeps exactly the same design, colors and proportions as in the start image from the first frame to the last; nothing is added or removed.
CRITICAL: fixed camera, no zoom, no pan, no cut inside the clip; slow, gentle movement only.
CRITICAL: nothing comes out of or moves inside the barn door; no other characters or animals appear.
Lumi stands with her hoof down and looks at the camera. She blinks twice, breathes softly and smiles slightly. She does nothing else and her forelegs stay down.
Fixed camera, no zoom, no pan.
Modern 3D cartoon render, soft matte vinyl toy figures, children's animation style, simple rounded shapes, clean bright colors, soft even daylight, gentle soft shadows, uncluttered background, calm and slow, eye-level camera at the chick's height.
```

### Toma 11 — Lumi responde hola

- **Duración:** 6 s
- **Personajes:** @lumi
- **Método:** imagen→video
- **Escenario:** patio
- **Encuadre:** plano general, cuerpo completo, Encuadre B (misma cámara y mismo tamaño que el keyframe B)
- **Cámara:** fija
- **Acción:** Lumi, con la pezuña baja, mira a cámara y saluda con la pezuña despacio, dos veces. La baja y sonríe en silencio.
- **Audio:** «Muu» suave al empezar (s 0 a 1), antes de la voz. Voz «Hola.» entre los s 2 y 3, sobre el saludo con la pezuña en alto, no cuando ya bajó. Del s 4 al 6, silencio. Sin música.
- **Referencia:** Plano 10 (final del plano continuo 8–10). Keyframe de partida: Último fotograma de la Toma 10 (encadenada, no se genera keyframe nuevo; el prompt de abajo es solo el respaldo si hay que regenerarlo).

**Prompt de keyframe:**

```text
Lumi, an adorable gentle cow shaped like a big smooth upright egg with no neck, about one and a half times as tall as Tiky, mostly creamy white with two large irregular black patches with soft wavy edges (one across her back and belly, one on top of her head between her horns), black lower legs like little socks, small lilac purple hooves, small cream rounded horns, small floppy ears with lilac insides, big warm honey-brown eyes with a white sparkle, soft gentle eyebrows, a wide rounded soft lilac muzzle with two small dot nostrils, a short chunky lilac crayon tucked behind her right ear.
Full-body shot of Lumi alone, centered in the frame in front of the red barn, facing the camera, forelegs down at her sides, a small gentle smile, with space above her horns and below her hooves. Fixed eye-level camera.
This is the last frame of Toma 10; keep pose, position, size and light.
A toy farmyard at toy scale on a sunny playroom floor: a small red wooden toy barn with a white roof on the left, a low white wooden fence behind, a soft pastel green felt mat as grass, plain pastel sky-blue wall in the background.
Modern 3D cartoon render, soft matte vinyl toy figures, children's animation style, simple rounded shapes, clean bright colors, soft even daylight, gentle soft shadows, uncluttered background, calm and slow, eye-level camera at the chick's height.
```

**Prompt de video:**

```text
CRITICAL: no written words, letters, brand marks or watermarks anywhere.
CRITICAL: Lumi keeps exactly the same design, colors and proportions as in the start image from the first frame to the last; nothing is added or removed.
CRITICAL: fixed camera, no zoom, no pan, no cut inside the clip; slow, gentle movement only.
CRITICAL: nothing comes out of or moves inside the barn door; no other characters or animals appear.
Lumi stands with her hoof down and looks at the camera. At one second she raises her right foreleg slowly and waves the lilac hoof twice with small gentle movements, never stamping. She lowers the hoof at about four seconds and smiles quietly at the camera until the end.
Fixed camera, no zoom, no pan.
Modern 3D cartoon render, soft matte vinyl toy figures, children's animation style, simple rounded shapes, clean bright colors, soft even daylight, gentle soft shadows, uncluttered background, calm and slow, eye-level camera at the chick's height.
```

### Toma 12 — Caminan a su lugar

- **Duración:** 4 s
- **Personajes:** @tiky, @lumi
- **Método:** imagen→video
- **Escenario:** patio
- **Encuadre:** plano general, cuerpo completo, Encuadre C (inicio al fondo)
- **Cámara:** fija
- **Acción:** Los dos caminan despacio desde el fondo hasta su lugar junto al establo y se detienen en el último medio segundo, mirando a cámara.
- **Audio:** Música suave (la misma del saludo) de 0 a 4 s, con fundido lento de 2 s que termina antes de la voz; pasos sobre fieltro. Sin voz en esta toma.
- **Referencia:** Plano 11 (0–4 s). Keyframe de partida: Keyframe C-entrada: se genera una vez y se reutiliza en las tomas 1 y 12.

**Prompt de keyframe:**

```text
Tiky, an adorable baby chick shaped like a smooth upright egg with no neck, warm sunflower yellow body with a pale butter-cream belly, a small discreet tuft of three short rounded flame-shaped feathers in red-orange on top of his head, big round dark-brown eyes with a white sparkle, no eyebrows, a small rounded coral-peach beak, soft rosy cheeks, tiny stubby wings, short coral-peach feet with three round toes.
Lumi, an adorable gentle cow shaped like a big smooth upright egg with no neck, about one and a half times as tall as Tiky, mostly creamy white with two large irregular black patches with soft wavy edges (one across her back and belly, one on top of her head between her horns), black lower legs like little socks, small lilac purple hooves, small cream rounded horns, small floppy ears with lilac insides, big warm honey-brown eyes with a white sparkle, soft gentle eyebrows, a wide rounded soft lilac muzzle with two small dot nostrils, a short chunky lilac crayon tucked behind her right ear.
Wide full-body shot of both characters standing far back near the low white fence, small in the frame, facing the camera, Lumi on the left of Tiky, wings and forelegs down. Fixed eye-level camera at the chick's height.
A toy farmyard at toy scale on a sunny playroom floor: a small red wooden toy barn with a white roof on the left, a low white wooden fence behind, a soft pastel green felt mat as grass, plain pastel sky-blue wall in the background.
Modern 3D cartoon render, soft matte vinyl toy figures, children's animation style, simple rounded shapes, clean bright colors, soft even daylight, gentle soft shadows, uncluttered background, calm and slow, eye-level camera at the chick's height.
```

**Prompt de video:**

```text
CRITICAL: no written words, letters, brand marks or watermarks anywhere.
CRITICAL: Tiky and Lumi keep exactly the same design, colors and proportions as in the start image from the first frame to the last; nothing is added or removed.
CRITICAL: fixed camera, no zoom, no pan, no cut inside the clip; slow, gentle movement only.
CRITICAL: nothing comes out of or moves inside the barn door; no other characters or animals appear.
Tiky and Lumi walk slowly toward the camera side by side with small steady steps, Lumi on the left, and stop at the center of the yard near the red barn, looking at the camera. The yard is tidy and empty.
Fixed camera, no zoom, no pan.
Modern 3D cartoon render, soft matte vinyl toy figures, children's animation style, simple rounded shapes, clean bright colors, soft even daylight, gentle soft shadows, uncluttered background, calm and slow, eye-level camera at the chick's height.
```

### Toma 13 — Quietos en su lugar

- **Duración:** 4 s
- **Personajes:** @tiky, @lumi
- **Método:** imagen→video
- **Escenario:** patio
- **Encuadre:** plano general, cuerpo completo, Encuadre C
- **Cámara:** fija
- **Acción:** Los dos están quietos mirando a cámara, en calma, con el patio despejado. Se mueven apenas: parpadean y respiran.
- **Audio:** Voz «Todo está en su lugar.» de 0 a 2,5 s y «Con la mano decimos hola.» de 2,5 a 4 s, sobre silencio. Sin música ni gestos.
- **Referencia:** Plano 11 (4–8 s). Keyframe de partida: Último fotograma de la Toma 12 (encadenada, no se genera keyframe nuevo; el prompt de abajo es solo el respaldo si hay que regenerarlo).

**Prompt de keyframe:**

```text
Tiky, an adorable baby chick shaped like a smooth upright egg with no neck, warm sunflower yellow body with a pale butter-cream belly, a small discreet tuft of three short rounded flame-shaped feathers in red-orange on top of his head, big round dark-brown eyes with a white sparkle, no eyebrows, a small rounded coral-peach beak, soft rosy cheeks, tiny stubby wings, short coral-peach feet with three round toes.
Lumi, an adorable gentle cow shaped like a big smooth upright egg with no neck, about one and a half times as tall as Tiky, mostly creamy white with two large irregular black patches with soft wavy edges (one across her back and belly, one on top of her head between her horns), black lower legs like little socks, small lilac purple hooves, small cream rounded horns, small floppy ears with lilac insides, big warm honey-brown eyes with a white sparkle, soft gentle eyebrows, a wide rounded soft lilac muzzle with two small dot nostrils, a short chunky lilac crayon tucked behind her right ear.
Full-body shot of both characters facing the camera, standing side by side and centered, Lumi on the left of Tiky, wings and forelegs down, small gentle smiles. Fixed eye-level camera at the chick's height.
This is the last frame of Toma 12; keep pose, position, size and light.
A toy farmyard at toy scale on a sunny playroom floor: a small red wooden toy barn with a white roof on the left, a low white wooden fence behind, a soft pastel green felt mat as grass, plain pastel sky-blue wall in the background.
Modern 3D cartoon render, soft matte vinyl toy figures, children's animation style, simple rounded shapes, clean bright colors, soft even daylight, gentle soft shadows, uncluttered background, calm and slow, eye-level camera at the chick's height.
```

**Prompt de video:**

```text
CRITICAL: no written words, letters, brand marks or watermarks anywhere.
CRITICAL: Tiky and Lumi keep exactly the same design, colors and proportions as in the start image from the first frame to the last; nothing is added or removed.
CRITICAL: fixed camera, no zoom, no pan, no cut inside the clip; slow, gentle movement only.
CRITICAL: nothing comes out of or moves inside the barn door; no other characters or animals appear.
Tiky and Lumi stand still side by side and look at the camera, Lumi on the left. Both blink slowly and breathe softly with small gentle smiles. Nothing else moves.
Fixed camera, no zoom, no pan.
Modern 3D cartoon render, soft matte vinyl toy figures, children's animation style, simple rounded shapes, clean bright colors, soft even daylight, gentle soft shadows, uncluttered background, calm and slow, eye-level camera at the chick's height.
```

### Toma 14 — Espera viva con el adulto 1

- **Duración:** 4 s
- **Personajes:** @tiky, @lumi
- **Método:** imagen→video
- **Escenario:** patio
- **Encuadre:** plano general, cuerpo completo, Encuadre C
- **Cámara:** fija
- **Acción:** Los dos miran a cámara en espera viva: parpadean y respiran suave, sin gestos ni sonidos, con el ala y la pezuña libres.
- **Audio:** Voz «Busca tu peluche. Salúdalo: hola.» de 0 a 4 s, sobre silencio. Sin música, sin sonidos de animal.
- **Referencia:** Plano 12 (0–4 s). Keyframe de partida: Keyframe C: se genera una vez y se reutiliza.

**Prompt de keyframe:**

```text
Tiky, an adorable baby chick shaped like a smooth upright egg with no neck, warm sunflower yellow body with a pale butter-cream belly, a small discreet tuft of three short rounded flame-shaped feathers in red-orange on top of his head, big round dark-brown eyes with a white sparkle, no eyebrows, a small rounded coral-peach beak, soft rosy cheeks, tiny stubby wings, short coral-peach feet with three round toes.
Lumi, an adorable gentle cow shaped like a big smooth upright egg with no neck, about one and a half times as tall as Tiky, mostly creamy white with two large irregular black patches with soft wavy edges (one across her back and belly, one on top of her head between her horns), black lower legs like little socks, small lilac purple hooves, small cream rounded horns, small floppy ears with lilac insides, big warm honey-brown eyes with a white sparkle, soft gentle eyebrows, a wide rounded soft lilac muzzle with two small dot nostrils, a short chunky lilac crayon tucked behind her right ear.
Full-body shot of both characters facing the camera, standing side by side and centered, Lumi on the left of Tiky, wings and forelegs down, small gentle smiles. Fixed eye-level camera at the chick's height.
A toy farmyard at toy scale on a sunny playroom floor: a small red wooden toy barn with a white roof on the left, a low white wooden fence behind, a soft pastel green felt mat as grass, plain pastel sky-blue wall in the background.
Modern 3D cartoon render, soft matte vinyl toy figures, children's animation style, simple rounded shapes, clean bright colors, soft even daylight, gentle soft shadows, uncluttered background, calm and slow, eye-level camera at the chick's height.
```

**Prompt de video:**

```text
CRITICAL: no written words, letters, brand marks or watermarks anywhere.
CRITICAL: Tiky and Lumi keep exactly the same design, colors and proportions as in the start image from the first frame to the last; nothing is added or removed.
CRITICAL: fixed camera, no zoom, no pan, no cut inside the clip; slow, gentle movement only.
CRITICAL: nothing comes out of or moves inside the barn door; no other characters or animals appear.
Tiky and Lumi stand side by side and look at the camera, Lumi on the left. Both blink and breathe softly with small gentle smiles. Their wings and forelegs rest down. Nothing else moves.
Fixed camera, no zoom, no pan.
Modern 3D cartoon render, soft matte vinyl toy figures, children's animation style, simple rounded shapes, clean bright colors, soft even daylight, gentle soft shadows, uncluttered background, calm and slow, eye-level camera at the chick's height.
```

### Toma 15 — Espera viva con el adulto 2

- **Duración:** 4 s
- **Personajes:** @tiky, @lumi
- **Método:** imagen→video
- **Escenario:** patio
- **Encuadre:** plano general, cuerpo completo, Encuadre C
- **Cámara:** fija
- **Acción:** Siguen mirando a cámara en espera viva: parpadean y respiran suave, sin gestos.
- **Audio:** Pausa corta de silencio (0 a 0,8 s) y voz «Saluden ustedes primero, y esperen.» de 0,8 a 4 s. Sin música, sin sonidos de animal.
- **Referencia:** Plano 12 (4–8 s). Keyframe de partida: Último fotograma de la Toma 14 (encadenada, no se genera keyframe nuevo; el prompt de abajo es solo el respaldo si hay que regenerarlo).

**Prompt de keyframe:**

```text
Tiky, an adorable baby chick shaped like a smooth upright egg with no neck, warm sunflower yellow body with a pale butter-cream belly, a small discreet tuft of three short rounded flame-shaped feathers in red-orange on top of his head, big round dark-brown eyes with a white sparkle, no eyebrows, a small rounded coral-peach beak, soft rosy cheeks, tiny stubby wings, short coral-peach feet with three round toes.
Lumi, an adorable gentle cow shaped like a big smooth upright egg with no neck, about one and a half times as tall as Tiky, mostly creamy white with two large irregular black patches with soft wavy edges (one across her back and belly, one on top of her head between her horns), black lower legs like little socks, small lilac purple hooves, small cream rounded horns, small floppy ears with lilac insides, big warm honey-brown eyes with a white sparkle, soft gentle eyebrows, a wide rounded soft lilac muzzle with two small dot nostrils, a short chunky lilac crayon tucked behind her right ear.
Full-body shot of both characters facing the camera, standing side by side and centered, Lumi on the left of Tiky, wings and forelegs down, small gentle smiles. Fixed eye-level camera at the chick's height.
This is the last frame of Toma 14; keep pose, position, size and light.
A toy farmyard at toy scale on a sunny playroom floor: a small red wooden toy barn with a white roof on the left, a low white wooden fence behind, a soft pastel green felt mat as grass, plain pastel sky-blue wall in the background.
Modern 3D cartoon render, soft matte vinyl toy figures, children's animation style, simple rounded shapes, clean bright colors, soft even daylight, gentle soft shadows, uncluttered background, calm and slow, eye-level camera at the chick's height.
```

**Prompt de video:**

```text
CRITICAL: no written words, letters, brand marks or watermarks anywhere.
CRITICAL: Tiky and Lumi keep exactly the same design, colors and proportions as in the start image from the first frame to the last; nothing is added or removed.
CRITICAL: fixed camera, no zoom, no pan, no cut inside the clip; slow, gentle movement only.
CRITICAL: nothing comes out of or moves inside the barn door; no other characters or animals appear.
Tiky and Lumi stand side by side and keep looking at the camera, Lumi on the left. Both blink and breathe softly with small gentle smiles. Nothing else moves.
Fixed camera, no zoom, no pan.
Modern 3D cartoon render, soft matte vinyl toy figures, children's animation style, simple rounded shapes, clean bright colors, soft even daylight, gentle soft shadows, uncluttered background, calm and slow, eye-level camera at the chick's height.
```

### Toma 16 — Despedida

- **Duración:** 6 s
- **Personajes:** @tiky, @lumi
- **Método:** imagen→video
- **Escenario:** patio
- **Encuadre:** plano general, cuerpo completo, Encuadre C
- **Cámara:** fija
- **Acción:** Los dos miran a cámara; con la voz «Adiós» saludan con el ala y la pezuña, despacio, dos veces, bajan los brazos y quedan mirando a cámara en el último fotograma.
- **Audio:** Voz «Ahora, a jugar.» de 0 a 2,5 s y «Adiós» de 2,8 a 3,8 s, sobre el saludo. Sin música durante la voz; tras «Adiós» entra la música suave (hacia el s 4,5) y baja en un fundido lento de unos 2 s hasta el silencio al final de la toma.
- **Referencia:** Plano 13. Keyframe de partida: Keyframe C: se genera una vez y se reutiliza.

**Prompt de keyframe:**

```text
Tiky, an adorable baby chick shaped like a smooth upright egg with no neck, warm sunflower yellow body with a pale butter-cream belly, a small discreet tuft of three short rounded flame-shaped feathers in red-orange on top of his head, big round dark-brown eyes with a white sparkle, no eyebrows, a small rounded coral-peach beak, soft rosy cheeks, tiny stubby wings, short coral-peach feet with three round toes.
Lumi, an adorable gentle cow shaped like a big smooth upright egg with no neck, about one and a half times as tall as Tiky, mostly creamy white with two large irregular black patches with soft wavy edges (one across her back and belly, one on top of her head between her horns), black lower legs like little socks, small lilac purple hooves, small cream rounded horns, small floppy ears with lilac insides, big warm honey-brown eyes with a white sparkle, soft gentle eyebrows, a wide rounded soft lilac muzzle with two small dot nostrils, a short chunky lilac crayon tucked behind her right ear.
Full-body shot of both characters facing the camera, standing side by side and centered, Lumi on the left of Tiky, wings and forelegs down, small gentle smiles. Fixed eye-level camera at the chick's height.
A toy farmyard at toy scale on a sunny playroom floor: a small red wooden toy barn with a white roof on the left, a low white wooden fence behind, a soft pastel green felt mat as grass, plain pastel sky-blue wall in the background.
Modern 3D cartoon render, soft matte vinyl toy figures, children's animation style, simple rounded shapes, clean bright colors, soft even daylight, gentle soft shadows, uncluttered background, calm and slow, eye-level camera at the chick's height.
```

**Prompt de video:**

```text
CRITICAL: no written words, letters, brand marks or watermarks anywhere.
CRITICAL: Tiky and Lumi keep exactly the same design, colors and proportions as in the start image from the first frame to the last; nothing is added or removed.
CRITICAL: fixed camera, no zoom, no pan, no cut inside the clip; slow, gentle movement only.
CRITICAL: nothing comes out of or moves inside the barn door; no other characters or animals appear.
Tiky and Lumi look at the camera, Lumi on the left. At two seconds Tiky raises his right wing slowly and waves it twice with small gentle movements, never flapping while Lumi raises her right foreleg slowly and waves the lilac hoof twice with small gentle movements, never stamping, both at the same slow pace. They lower the wing and the hoof at about four and a half seconds and keep looking at the camera, calm, until the end.
Fixed camera, no zoom, no pan.
Modern 3D cartoon render, soft matte vinyl toy figures, children's animation style, simple rounded shapes, clean bright colors, soft even daylight, gentle soft shadows, uncluttered background, calm and slow, eye-level camera at the chick's height.
```

## 7. Audio

- **Voz:** narradora en off, cálida y lenta, en español; se genera o graba aparte y se monta en edición. Los textos exactos y su momento están en el campo Audio de cada toma. El generador no produce voz ni sonido (clips sin audio).
- **Música:** una pieza suave y corta que suena en el saludo (toma 1), el cierre (toma 12) y la despedida (toma 16), siempre con fundidos lentos y nunca debajo de la voz. Archivo pendiente en 05_audio/ y su licencia, por definir con el dueño (opción en el generador: ElevenLabs Music v2, 12 s, 0,77 créditos, fuera del presupuesto de video).
- **Efectos:** pasos sobre fieltro (tomas 1 y 12), pájaros lejanos (toma 1), «pío» suave de Tiky (tomas 4, 5 y 8) y «muu» suave de Lumi (tomas 3, 5 y 11), reales y siempre antes de la voz.

## 8. Montaje

- **Orden:** Toma 1 → Toma 2 → Toma 3 → Toma 4 → Toma 5 → Toma 6 → Toma 7 → Toma 8 → Toma 9 → Toma 10 → Toma 11 → Toma 12 → Toma 13 → Toma 14 → Toma 15 → Toma 16
- **Transiciones:** corte directo entre planos. Las uniones de tomas encadenadas (1→2, 6→7→8, 9→10→11, 12→13, 14→15) deben ser invisibles: se recorta el primer fotograma de la toma siguiente para no repetir el último de la anterior. No se congela ni se alarga ningún fotograma.
- **Texto en pantalla:** ninguno.
- **Formato de salida:** 1920x1080, 16:9, MP4 H.264 con audio AAC a 48 kHz, a los fps del generador (`ensamblar.py --formato largo`).

## 9. Presupuesto

| Concepto | Cantidad | Costo |
|---|---|---|
| Segundos generados (tomas × intentos) | 88 s de tomas × 2 intentos = 176 s a 480p (0,5 por segundo) | 88 créditos |
| Keyframes | 4 imágenes con Nano Banana 2 (1,5 cada una) | 6 créditos |
| Remates en resolución final | 88 s a 720p, un intento por toma aprobada (1 por segundo) | 88 créditos |
| **Total estimado** | | 182 créditos |
