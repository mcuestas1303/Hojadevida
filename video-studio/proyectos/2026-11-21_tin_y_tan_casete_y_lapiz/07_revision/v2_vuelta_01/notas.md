# v2 · vuelta 1 — notas del equipo de producción (2026-11-21)

Video: `06_final/tin_y_tan_short01_v2.mp4` (no va al repo; se rehace con `python3 codigo/render_v2.py` en ~1 min).
Hecho con `codigo/render_v2.py` y `codigo/audio_v2.py` (copias del v1 del Generador con los cambios de abajo). 0 créditos.

## Qué cambió respecto del v1

| Cambio | Por qué (revisión del v1) |
|---|---|
| Voz v2 (`dialogo_110_v2.mp3`): pulgadas y pies, «For one side.» | Remate falso y unidades ajenas a EE. UU. (cambio aprobado por el dueño) |
| Texto 1: «**pencil** turns?» al 7 %, sale en 0,95 s | «pencil» nunca salía en pantalla; el texto seguía encima del plano siguiente |
| Lápiz en el carrete desde el fotograma 0 (y en el bucle) | El lápiz no se veía hasta el 3,5 |
| Personajes 18 % más grandes, pies al 86 % del alto | El tercio de abajo quedaba vacío |
| Casete de las tomas 3, 5 y 6 al 46 % del ancho y en y = 31 % | Que no toque el rodete de Tan |
| Carretes girando y otro encuadre en la toma 6; borrón en el corte de 6,5 | Valle de 5,0 a 9,5 s sin cambio visible |
| Toma 7: una pulgada por marca, tira de 10 % del alto | La tira de 77 px era un hilo |
| Toma 9: carrete de 280 px, arco y segmento de 10 px; el segmento mide una vuelta (880 px) | El plano héroe era el más débil |
| Barra de la toma 11 el doble de alta | Igual |
| Tan reacciona con sorpresa al cerrar el arco (16,1 s) | Una reacción por dato |
| Cortes y golpes retemporizados a la voz v2; golpes bajo la voz a −26 LUFS (antes −38) | No se oían |

## Comprobado

- 30,00 s, 1080x1920, 30 fps; fotograma 900 = fotograma 0 (bucle), lo comprueba el render.
- Contadores: 0 → 421 ft y 0 → 1,170 turns, solo suben (comprobado en el código).
- 45 golpes, todos en su tiempo (`05_audio/medidas_audio_v2.json`).
- Destellos: 0. Mezcla final normalizada a −14 LUFS con techo de −1 dBTP.
- Glifos ⅞ ⅓ ÷ presentes en Inter Display Medium.
- `revisar_fotogramas.py` marca «imagen congelada» en 7,8–9,2, 10,0–11,7, 15,2–16,2 y 17,8–19,2 s: a 96x54 px no ve los
  carretes ni la cinta que corre; a resolución completa hay movimiento. Igual que en el v1, es movimiento pequeño.

## Pendiente (no bloquea subir en privado)

- La toma 7 (tira de cinta) y la toma 11 (barra) siguen dejando la mitad de abajo vacía.
- El gancho todavía tiene 1,0 s sin voz (la voz entra en el segundo 1,0): adelantar la voz exige retemporizar todo.
- Que el dueño escuche la mezcla del video completo (la voz v2 sola ya la aprobó: «se escucha bien»).
