# Cambio: el rival, en fucsia neón

- **Pidió:** el dueño, 2026-11-27, en la conversación de producción. Textual: «con el rival ocupa un color fucsia neon».
  Responde a la decisión que la dirección del short 5 le dejaba abierta (11.1 k: lila `#B79CFF` y enmienda de la ficha).
- **Decisión del equipo (el tono exacto es técnico):** **`#FF2BD6`**, con hollín `#0B0F1F` para lo chamuscado.

## Por qué ese tono (medido el 2026-11-27, script de contraste y ΔE en Lab)

| Contra | `#FF2BD6` | Lila anterior `#B79CFF` |
|---|---|---|
| Fondo de noche `#141B33` (contraste) | 5,3:1 | 7,5:1 |
| Suelo `#27304F` (contraste) | 4,0:1 | — |
| Rojo del fuego `#B81414` (ΔE) | 91 | — |
| Línea de Tin y Tan `#F3E9D2` (ΔE) | 107 | ≈ 70 |
| Cian del acento `#4FE3FF` (ΔE) | 122 | — |
| Amarillo del fuego `#FFE45C` (ΔE) | 145 | — |

Tono 312°: del lado del magenta, no del rojo. Se probaron cuatro fucsias (`#FF1FC8`, `#FF3DDB`, `#FF00CC`); este separa
más del rojo del fuego sin perder contraste. **Se cumple «ningún rojo sobre el rival»** (regla 2.1.7 de la dirección).

## Qué toca de lo ya definido

- `personajes/duda/ficha.md`: decía «por ahora solo tinta» y prohibía pintarla. Se enmienda: en la hoja Noche su tinta es
  fucsia neón. En las hojas claras (A y C) sigue en tinta oscura hasta que el dueño diga otra cosa.
- `motor_de_accion/paletas/b_noche_de_tinta.json`: `rival` pasa de `#B79CFF` a `#FF2BD6`.
- Dirección del short 5, 3.4 y 11.1 k: donde dice lila se lee fucsia neón; el paquete de tinta lleva contorno fucsia.
- **Qué hay que rehacer: nada.** No hay nada dibujado ni renderizado del short 5. Costo: 0 créditos.

## Dudas que quedan (no bloquean la animática; sí se miden antes del render)

1. **Regla del color (2 neutros + 1 acento):** el fucsia es un segundo color saturado junto al cian del acento. Fotografía
   decide si el cian baja de papel en este video; lo mide `revisar_color.py`.
2. **Contraste con el suelo, 4,0:1:** menor que contra el fondo. Si el rival se pierde tendido en el suelo, se le pone el
   contorno de hollín que ya llevan los ojos. Se ve en la primera hoja de fotogramas.
3. **Destellos:** un color tan saturado en la explosión y la implosión pasa por `comprobar_destellos`.
4. **Alcance:** se entiende para la hoja Noche (short 5). Si el dueño lo quiere en todos los videos, se enmienda la ficha entera.
