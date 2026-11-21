# 03 · Luz, color y textura

La luz dice la emoción antes que la actuación. Se define **una vez por escenario** y se repite igual en todas las
tomas que pasan ahí (la parte 2 del Short 02 cambió de estudio porque el fondo se dijo distinto).

## Esquemas de luz

| Esquema | Prompt | Emoción |
|---|---|---|
| Clave alta | `bright high-key lighting, soft shadows` | alegría, infantil, comedia |
| Clave baja | `low-key lighting, deep shadows, single key light` | tensión, misterio, «M» |
| Hora dorada | `warm golden hour sunlight, long soft shadows` | ternura, nostalgia, final feliz |
| Hora azul | `cool blue hour light` | calma, tristeza suave |
| Contraluz | `strong backlight, rim light outlining the character` | épica, aparición, orgullo |
| Estudio infinito | `seamless white infinity studio, soft even light, no visible lights or ceiling` | humor de Spike, foco total en el personaje |
| Luz de ventana | `soft window light from the left` | intimidad, realismo |
| Neón | `neon magenta and cyan practical lights` | noche, música, energía (Spike) |
| Día parejo (infantil) | `soft even daylight, gentle soft shadows` | calma, seguridad |

## Paletas

> Cómo se elige y se justifica la paleta de cada video (2 neutros + 1 acento, color según el objetivo, medición):
> capítulo 13, `13_color_con_intencion.md`.

| Paleta | Prompt | Uso |
|---|---|---|
| Cálida saturada | `warm saturated colors` | alegría, energía |
| Pastel | `soft pastel palette` | ternura, bebés |
| Desaturada fría | `desaturated cool tones` | tristeza |
| Complementaria | `teal and orange color grade` | cine de acción («M») |
| Monocroma + acento | `muted background, the character is the only saturated element` | que el personaje salte del fondo (Spike naranja neón) |

**Color de marca de cada personaje:** el fondo nunca compite con su color icónico. Spike (naranja neón y morado) va
sobre blanco o colores fríos; Tiky (amarillo girasol) sobre verdes y azules suaves; Lumi (blanco, negro, lila) sobre
cálidos claros.

## Texturas y estilo

| Estilo | Prompt base | Personajes |
|---|---|---|
| Juguete de vinilo 3D | `modern 3D cartoon render, soft matte vinyl toy figures, subtle subsurface, clean bright colors` | Tiky, Lumi (principal) |
| Libro para colorear | `clean black-and-white coloring book line art, thick smooth outlines` | Tiky, Lumi 2D (imagen, no video) |
| Foto realista | `realistic photo, natural skin texture, 35mm film grain` | Spike, «M» |
| Cine | `cinematic film still, anamorphic, subtle film grain` | «M» |

## Corrección de color en edición (gratis)

`postpro.py color --estilo calido|frio|noche|vivo|suave` aplica un ajuste rápido; `--lut archivo.cube` aplica un LUT.
Usarlo para **igualar** tomas que salieron con tono distinto antes que regenerarlas.
