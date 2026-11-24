# Registro de costos

Anota cada generación, también las fallidas: es lo que permite ver qué tomas están
quemando el presupuesto y corregir el prompt en vez de seguir tirando intentos.

| Fecha | Toma | Tipo (keyframe / borrador / final) | Segundos | Intento # | Costo | ¿Sirvió? | Qué falló |
|---|---|---|---|---|---|---|---|

## Cotización de voz (2026-11-24, `estimate_audio_cost`, `seed_audio`, sin generar)

| Pieza | Texto | Créditos | Estado |
|---|---|---|---|
| Voz de Tan (Zelda), 4 líneas y coletilla en una sola generación | §7 del prompt | 1,2 | Cotizado; espera el sí del dueño |
| Voz de Tin (Kevin), 8 líneas y coletilla en una sola generación | §7 del prompt | 2,5 | Cotizado; espera el sí del dueño |
| **Total** | | **3,7** | Imagen y video: 0 (dibujado por código) |

## Cotización del 2026-11-24 (prompt de la noticia; la anterior de 3,7 créditos queda sin efecto)

| Pieza | Herramienta | Costo |
|---|---|---|
| Voz de Tan (Zelda), 4 líneas y coletilla | `seed_audio` | 1,1 créditos |
| Voz de Tin (Kevin), 7 líneas y coletilla | `seed_audio` | 2,6 créditos |
| Imagen, video, música, efectos y subtítulos | por código | 0 |
| **Total** | | **3,7 créditos** |

Estado: cotizado con `estimate_audio_cost`; **falta el sí del dueño**. No se ha gastado nada.
