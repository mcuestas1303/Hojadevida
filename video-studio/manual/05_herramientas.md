# 05 · Herramientas y costos

El equipo conoce **qué hace cada herramienta, cuánto cuesta y cuál es la ruta más barata** para cada necesidad.
Regla general: *gratis → web ilimitada → borrador barato → final caro, y cada escalón solo si el anterior se aprobó.*

## Precios verificados (Higgsfield, plan Plus)

Cotizados con `estimate_*_cost` el **2026-11-20** (no generan nada ni gastan). Antes de cada generación se vuelve a
cotizar: los precios cambian.

| Necesidad | Modelo (ID) | Ajuste | Créditos | Por segundo |
|---|---|---|---|---|
| Keyframe barato | `gpt_image_2_6` | calidad baja, 9:16 | **0,25** | — |
| Keyframe bueno | `nano_banana_2` | 9:16 | 1,5 | — |
| Keyframe final | Nano Banana Pro | 1k–2k | 2 (2026-11-07) | — |
| Borrador de movimiento | `seedance_2_0_mini` | 5 s · 480p | **2,5** | 0,5 |
| Borrador de escena | `seedance_2_0_mini` | 12 s · 480p | 6 | 0,5 |
| Final económico | `seedance_2_0_mini` | 5 s · 720p | 5 | 1 |
| Multi-toma, audio, movimiento | `kling3_0` | 5 s / 10 s | 10 / 20 | 2 |
| Keyframes 2K o referencias mezcladas | `minimax_h3` | 5 s | 10 | 2 |
| Calidad alta | `seedance_2_0` | 5 s · 720p | 22,5 | 4,5 |
| Calidad máxima (rara vez vale) | `seedance_2_5` | 5 s | 35 | 7 |
| Sincronía de labios | `sync_so` | 5 s | 18 | 3,6 |
| Transferir movimiento (Genjutsu) | `hf_mult_motion_control` | 12 s · 480p / 720p | 36 / 84 (2026-11-07) | 3 / 7 |
| Voz (TTS) | `seed_audio` | una frase | **0,3** | — |
| Efecto de sonido | `mirelo_text_to_audio` | 3 s | 0,75 | 0,25 |
| Música | ElevenLabs Music v2 | 12 s | 0,77 (2026-11-07) | — |

`suno_music` no está disponible en esta cuenta (la cotización respondió «modelo desconocido»).

**Gratis:** imágenes con modelos marcados «Unlimited» en la **web** de higgsfield.ai (no por la conexión de Claude);
bocetos con FLUX.1 schnell en Colab (`creador-personajes/colab/`); todo lo que hace `postpro.py` y `ensamblar.py`
(ffmpeg en esta máquina); CapCut y DaVinci Resolve en la computadora o el celular del dueño.

## Qué herramienta para qué

| Quiero… | Ruta barata | Ruta de calidad |
|---|---|---|
| Probar si una acción funciona | `seedance_2_0_mini` 5 s 480p (2,5) | — |
| Toma con personaje, sin diálogo | keyframe `gpt_image_2_6` → `seedance_2_0_mini` 720p | keyframe `nano_banana_2` → `kling3_0` |
| Varias tomas en una generación | dividir en tomas de 5 s y unir en edición | `kling3_0` multi-toma |
| Que el personaje hable a cámara | voz `seed_audio` + `sync_so` sobre la toma | `kling3_0` con audio (si el modelo lo soporta para esa toma) |
| Copiar un baile / trend | el dueño lo graba → `motion_control` 720p | `hf_mult_motion_control` |
| Cambiar el estilo de un clip propio sin perder el movimiento | Genjutsu Styles (p. ej. *Rounded Toy CGI*, cercano al estilo de Tiky y Lumi) | — |
| Cambiar un objeto o prenda en un clip | `hf_mult_replace_object` | — |
| Pasar de 16:9 a 9:16 | `postpro.py vertical` (gratis) | `reframe` de Higgsfield |
| Más resolución | exportar bien desde edición | `upscale_video` (no se puede cotizar antes: solo con aprobación) |
| Cámara lenta, zoom, repetición, títulos | `postpro.py` (gratis) | — |
| Voz de un personaje fija | `create_voice` una vez y reutilizar el ID | — |

## Disciplina de gasto (la cumple todo el equipo)

1. **Cotizar antes** con `estimate_video_cost`, `estimate_image_cost` o `estimate_audio_cost` y decir el número.
   Sin aprobación del dueño no se genera (`.claude/settings.json` lo obliga).
2. **Imagen antes que video.** El personaje se acierta en el keyframe (0,25–1,5) y recién después se anima.
3. **Borrador antes que final:** 480p y 5 s. Solo la toma aprobada se repite en 720p.
4. **`count: 1` en video.** Las variantes se exploran en imagen.
5. **Tomas de 5 s o menos**, una acción cada una.
6. **Lo editable no se genera** (texto, zooms, transiciones, cámara lenta, repeticiones, color).
7. **Reusar:** mismos IDs de referencia, mismo bloque de identidad, último fotograma como siguiente keyframe,
   escenarios y voces ya creados.
8. **Freno de pérdidas:** dos intentos fallidos en una toma → no hay tercero; se revisa el prompt o se parte la toma.
9. **Clips sin audio** salvo que el audio del modelo sea el objetivo; la música la pone el dueño o se genera aparte.
10. **Registrar cada intento** en `costos.md` del proyecto (modelo, ajuste, créditos, veredicto).
11. **Medir el retorno:** el costo de cada video se cruza con sus resultados (cap. 10). Lo que no rinde no se repite.

## Presupuesto tipo

| Pieza | Ruta | Créditos aprox. |
|---|---|---|
| Short de 15 s, 3 tomas, personaje sin hablar | 3 keyframes baratos + 3 borradores + 3 finales Mini 720p | 0,75 + 7,5 + 15 ≈ **23** |
| El mismo, con 1 frase hablada y labios | + voz 0,3 + `sync_so` 5 s 18 | ≈ **41** |
| Trend con movimiento transferido, 12 s | grabación propia + `hf_mult_motion_control` 480p | ≈ **36** |
| Clip propio reestilizado | Genjutsu Styles, según duración | cotizar en el formulario |
