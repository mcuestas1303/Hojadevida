# Registro de costos

Anota cada generación, también las fallidas: es lo que permite ver qué tomas están
quemando el presupuesto y corregir el prompt en vez de seguir tirando intentos.

| Fecha | Toma | Tipo (keyframe / borrador / final) | Segundos | Intento # | Costo | ¿Sirvió? | Qué falló |
|---|---|---|---|---|---|---|---|


## Cotización de voz (2026-11-26, `estimate_audio_cost`, `seed_audio`, sin generar)

| Pieza | Voz | Créditos | Estado |
|---|---|---|---|
| Líneas de Tin | Kevin (`f1373f24-3b96-433f-9a68-e595810ef608`) | 2,6 | Cotizado con el texto del brief; **falta el sí del dueño**; se vuelve a cotizar con el texto final de la dirección antes de generar |
| Líneas de Tan | Zelda (`b7aaea29-0c88-5925-90c0-8f66754cda53`) | 0,8 | Igual |
| **Total** | | **≈ 3,4** | Nada gastado |

Imagen y video: 0 créditos (dibujo por código con el motor de acción).

## Gasto real de voz (2026-11-26, con el sí del dueño: «1. autorizado»)

Recotizado con el texto final antes de generar. Las cifras van escritas con letras («nineteen ninety-seven», «GTA six»,
«November nineteenth, twenty twenty-six») para que la voz no pueda leerlas de otra manera: son las mismas palabras
habladas del brief.

| Pieza | Trabajo de Higgsfield (`seed_audio`) | Costo cotizado | Estado |
|---|---|---|---|
| Voz de Tin (Kevin), 5 bloques | `b0e934d1-3bd9-406a-8429-8cb87519b979` | 2,6 créditos | Una generación; no se regenera |
| Voz de Tan (Zelda), 3 líneas | `d9413cb4-1120-4735-979a-368b9d87dbbd` | 0,5 créditos | Una generación; no se regenera |
| **Total** | | **3,1 créditos** (autorizados: ≈ 3,4) | |

## Cierre de producción (2026-11-26)

| Pieza | Costo |
|---|---|
| Voz (2 generaciones, sin segundos intentos) | 3,1 créditos |
| Grabación del motor (2 pasadas completas de 986 f y varias parciales), composición, sonido | 0 créditos |
| **Total del video** | **3,1 créditos** |
