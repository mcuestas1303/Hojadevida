# Firma del supervisor de continuidad — short 3 de Tin & Tan, vuelta 2 (render 2)

- **Fecha:** 2026-11-24.
- **Pieza revisada:** `06_final/tin_y_tan_short03_v1.mp4` del 2026-11-24 03:02 (1080×1920, 30 fps, H.264, yuv420p, AAC, 930 fotogramas, 31,0 s), `06_final/portada_short03.png` de la misma hora y `08_entrega/TIN-EN-S-003/` del 03:06 (`video.mp4` de 2,93 MB, `miniatura.png` idéntica a la portada, los dos `.srt`, `ficha.json`).
- **Cómo se revisó:** de cero. Hojas propias a 2 fotogramas por segundo (las cuatro vistas); los 930 fotogramas del archivo final y los 930 de la entrega; f0 a f14 y f900 a f929 uno por uno, y f8–f11 y f913–f920 ampliados; portada a tamaño completo; calendario (5,83 · 10,00 · 11,00 · 12,00 s), barras (13,67 · 18,00 · 18,67 · 21,33 · 22,10 · 22,33 · 23,33 · 26,33 s), 16 caras ampliadas, seis recortes de subtítulo con cabezas, cuatro planos reducidos a 390 px de ancho (teléfono); medidas propias de lápiz–cabezas, hueco bajo el subtítulo y zona segura en los fotogramas. Evidencias en `07_revision/vuelta_02/supervisor/`.
- **No revisado por mí:** control 3 (no oigo). Los hechos de noviembre de 2026 sobre Jensen Huang en una fuente externa. La sección 3b de `direccion.md` (sigue en plantilla).

## Veredicto general

**`CAMBIOS`, por un solo punto.** Los cuatro bloqueantes de la vuelta 1 están resueltos y firmo Texto (salvo una tarjeta), Cifras, Imagen, Portada, Firma del lápiz, Marca y Color. Lo único que no pasa: **la tarjeta «4.382 días.» se ve 9 fotogramas a plena opacidad (0,3 s): no se lee.** Arreglo de dos números en `codigo/tiempos.py`, 0 créditos, un render. Si el nuevo render solo cambia eso, me basta revisar 19,0–24,5 s y el hueco de esa tarjeta para firmar Texto y Video.

## Los cuatro bloqueantes de la vuelta 1

| # | Qué era | Lo que vi y medí en el render 2 | Resultado |
|---|---|---|---|
| 1 | El lápiz pasaba por delante de la cara de Tan (f915–f917) | Brazo extendido hacia delante en todo el plano de firma. En f0–f14 y f900–f929 el lápiz no toca ninguna cabeza: siempre hay papel entre los dos. Mi medida sobre el cuerpo del lápiz: mínimo **56 px** a la cabeza de Tan (f915) y **102 px** a la de Tin (f0); la del equipo, con goma y contorno, 28,8 y 46,2 px. `_despejes` ya mide todos los fotogramas. Atrapada en f10 con retroceso; suelta en f915; un solo lápiz por fotograma. El abanico de copias ya no se ve | **RESUELTO** |
| 2 | La «q» tocaba el rodete y el panel velaba cabezas | Personajes a 505 px. En los 756 fotogramas con tarjeta, entre la última tinta del subtítulo y lo primero dibujado debajo hay **24 px o más** de papel (medida mía). Rodete y botón de la gorra enteros en los seis recortes. El equipo mide 12 px de panel a cabezas en la tarjeta 8 y 25 px o más en el resto | **RESUELTO** |
| 3 | Barras sin nombre | «Huang 11», «Altman 5» y «Jobs 4,382» en tinta sobre cada marca, filas separadas; «Jobs 4,382» entra con la llegada del contador (22,07 s). La barra de 12.274 ya no lleva la marca mostaza. Filas en la tabla de §12 del prompt | **RESUELTO** (ver «Dos cosas a juzgar») |
| 4 | Cara de Tan en la portada | `sorpresa`: boca en «o», ojo con brillo y ceja alta. Se lee sorpresa, también al 25 %. Es la misma cara en todo el plano de firma y en el empalme | **RESUELTO** |

## Dos cosas a juzgar

1. **Tarjeta «4.382 días.» (segundo renglón de la tarjeta 8).** No pasa. Aparece en f662, llega a plena opacidad en f664 y se va en f673: **9 fotogramas nítidos**. Se ve como un parpadeo bajo la cifra grande. El dato no se pierde (queda «4,382 days» en tomate 2,3 s y luego «¿Casi 12 años?»), pero un texto que no da tiempo a leer es un defecto de texto, no una salvedad. **Corrección exacta**, en `SUBTITULOS` de `codigo/tiempos.py` (y la tabla de tarjetas de §12): tarjeta 8, fin de 22,47 a **23,10 s**; tarjeta 9, inicio de 22,715 a **23,15 s** (fin sin cambio, 24,47 s). Así «4.382 días.» dura 1,03 s, cruza el corte de 22,5 s sobre un plano que sigue mostrando la barra y la cifra de Jobs, y «¿Casi 12 años?» entra 0,3 s antes de que Tan diga «twelve years?» (23,45 s) y dura 1,32 s. No se adelanta el pico. Volver a correr `render.py --medir-subtitulos`: la tarjeta 8 de dos renglones pasa a estar también sobre Tan sola (toma 11).
2. **Rótulos de las barras.** Se leen en teléfono. A 390 px de ancho, «Huang 11», «Altman 5» y «Jobs 4,382» quedan con un cuerpo de ≈ 20 px: es el texto más chico de la pieza, pero nítido, en tinta sobre papel (12,6:1) y quieto varios segundos. De 20,9 a 22,1 s la cámara abierta los baja ≈ 9 %; siguen legibles. Pasa con salvedad: no bajar de 56 px en piezas siguientes.

## Tabla por control

| Control | Evidencia | Resultado | Firma |
|---|---|---|---|
| 1. Texto | `revisar_texto.py`: inglés 90 textos (`ficha.json`, los dos `subtitulos.srt`, textos de pantalla, `render.py`, `miniatura.py`, `tiempos.py`), **0 errores, 0 avisos**; español 34 textos, **0 errores, 0 avisos**. Leído en la imagen: rótulos de antes más «Huang 11», «Altman 5», «Jobs 4,382». Tarjetas: «¿Jensen Huang volvió / rápido en 11 días?», «Renunció a Nvidia / tras un escándalo.», «El 17, la junta dijo / que no lo repondría.», «Seis días después, / lo repuso como CEO.», «Antes: más de 33 / años al mando.», «¿Rápido comparado / con quién?», «Sam Altman, OpenAI: / 5 días.», «Steve Jobs, Apple: / 4.382 días.», «¿Casi 12 años?», «Más rápido que Jobs. / Más lento que Altman.», «¿Quién más volvió?», «Suscríbete al próximo / conteo.»: sin faltas, tildes y «¿» correctos, punto de miles en español y coma en inglés, nombres propios con mayúscula. `subtitulos_es.srt` línea 9: «¿Casi 12 años?». `subtitulos.srt` en inglés sin cambios e igual a la voz. Descripción sin cambios | **NO PASA** por la duración de «4.382 días.»; todo lo demás pasa | **NO FIRMADO** (un punto) |
| 2. Cifras | Recalculado: 11, 6, 12.274, 5, 4.382; noviembre de 2026 con el 1 en domingo; 11 cruces del 13 al 23; contador solo sube y llega en f662 (22,07 s, 71,2 %). Tarjetas nuevas: «11 días», «El 17», «Seis días», «5 días», «4.382 días», «más de 33 años»: las mismas cifras que voz, rótulos, `.srt`, descripción y ficha técnica. «¿Casi 12 años?» ya lleva la aproximación en español y la descripción dice «≈ 12 years» | **PASA CON SALVEDAD** (la voz y el `.srt` en inglés dicen «That is twelve years?» sin palabra de aproximación; no se regenera; falta que el director creativo lo acepte por escrito) | **FIRMADO** |
| 4. Imagen | Tin y Tan iguales a sus fichas en las 14 tomas (colores, rodete, bufanda, gorra con botón y costuras, lentes, manos, zapatos); lados correctos; nada de terceros. Zona segura: nada fuera por arriba ni por los lados en los 930 fotogramas (solo 2 px de sombra bajo y = 1670). Silla de la toma 3 al centro, entre los dos. Renuncia (3,5–6,5 s): Tin sin sonrisa abierta ni rubor; reposición (9,0–11,5 s): Tan señala con `sorpresa`, sin festejo; pico: los dos con `sorpresa`; risa solo en el remate | **PASA CON SALVEDAD** (la cara `neutra` de Tin está hecha en `render.py` con piezas de la ficha y no figura en `personajes/tin/ficha.md`: falta que el director de animación la acepte o la lleve a `palitos.py`; menores 1 y 2) | **FIRMADO** |
| 4.5 Portada | f0 = `portada_short03.png` = `miniatura.png` (1080×1920, 1,26 MB; 1,5 de 255 contra f0). Texto x 105–608, y 416–693, 4 palabras en 2 líneas, «11» en mostaza. Silla y 715–1111. Cabeza de Tan x 114–310; de Tin **x 734–952** (ya dentro de 960). Lápiz x 484–674, y 1221–1273 (≈ 18 % del ancho), entero y nítido. Tan y Tin con sorpresa, mirando hacia la silla. Misma composición hasta 1,0 s. La cifra a la vista está decidida en el prompt y en `PARAMETROS.md` | **PASA CON SALVEDAD** (mayúsculas de 98 px y 22 px entre «Days?» y la silla, sin cambios) | **FIRMADO** |
| 5. Video | Formato correcto en final y entrega (930 fotogramas a paso fijo). `revisar_fotogramas.py`: sin marcas. 0 destellos en los dos. Bucle: f929 contra f0 = 0,77 de 255 (vecinos 0,28 y 0,25); en la entrega 1,33. Cortes en 11,5 y 12,5 s: «11 days» ya no coincide con «más de 33 años». −14,0 LUFS; pico −1,7 dB (medida, no escucha) | **Lo técnico pasa; pendiente del nuevo render** | **NO FIRMADO** |
| Firma del lápiz (§11) | Punto 2 resuelto (arriba). Empalme: 5,2 y 4,7 px/f, 4,4 y 4,0 °/f; 330°; 58 px/f y 24,9 °/f máximos; escala 1,7. Anticipación f906–f913, suelta f915, atrapada f10, voz en f14. Se lee como lápiz que llega y es atrapado, y como lanzado al final | **PASA**; el punto 10 (sonido) es del oído | **FIRMADO** (puntos 1 a 9) |
| 7. Marca | Paleta, tipografía, minúsculas a la izquierda, `ss01`, lados y lápiz: sin cambios | **PASA** | **FIRMADO** |
| 8. Color (medición) | Video ≈ 93 % en paleta, saturación ≈ 16 %, luminosidad ≈ 90 %, ±1 %; portada ≈ 93 %; entrega ≈ 93 %. Contrastes sin cambio. Círculos del 12 y del 17 en tinta en las tomas 5 y 6: sigue habiendo un solo acento por plano; tomate solo en la cifra del pico | **PASA CON SALVEDAD** (tinta/tomate 3,5:1; la sección 3b no existe y falta la firma del director de fotografía) | **FIRMADO** (solo la medición) |

Título: `revisar_titulo.py` con `--descripcion` y `--proyecto`: PASA, 0 errores, 0 avisos. `entrega.py`: lista, con el aviso fijo de portada. Preguntas fijas: iguales a la vuelta 1 (movimiento desde f0 y primer corte en 1,0 s justo; pico al 71,2 %; empalma; 0 destellos; todo con licencia; cada corte con su sonido, sin comprobar por mí).

## Puntos menores de la vuelta 1

| Punto | Render 2 | Resultado |
|---|---|---|
| Calendario | 17 con círculo de tinta, flecha larga con punta hasta el 23, círculo del 12 en tinta en las tomas 5 y 6, cruces debajo de los números. A tamaño de teléfono se lee «del 17 al 23» | resuelto, con el menor 1 |
| Tarjetas en español | Las seis nuevas, correctas y dentro de dos renglones | resuelto, salvo la duración de «4.382 días.» |
| Toma 6 | 11,5–12,5 s; «11 days» ya no pisa «más de 33 años». La tarjeta 4 sale en 11,47 s y la 5 entra en 12,5 s: «Before that:» (11,97–12,5 s) queda sin subtítulo 0,5 s | resuelto |
| Caras en renuncia y reposición | Neutras, sin sonrisa abierta ni festejo | resuelto |
| Silla de la toma 3 | x 452–628, dentro de la zona segura | resuelto |

## Lo que queda (ninguno bloquea salvo el primero)

1. **Bloquea:** «4.382 días.», 22,07–22,47 s. Corrección arriba.
2. **Menor 1, 9,3–12,5 s:** el trazo de la flecha pasa por encima del «18» y tacha el «24» y el «25», que no son días contados. Dónde: `_marcas_zona` en `codigo/render.py`; llevar el tramo de vuelta por debajo de la fila del 23 o acortar el lazo. Si hay render, conviene.
3. **Menor 2, 5,5–6,5 s:** el círculo mostaza del 12 (calendario lejano de la toma 3) queda más chico que antes y pisa los dígitos. La fecha la da el rótulo.
4. **Sonido, para el diseñador de sonido y el dueño:** la escucha del dueño fue sobre el render 1. En el render 2 cambiaron el chasquido y el whoosh de ida (−20,0 y −20,8 dBFS) y el pico pasó de −1,0 a −1,7 dB: la mezcla no es idéntica. `escucha_del_dueno.md` dice que se le avisa qué cambió; no está anotado que se haya hecho.
5. **Documentos:** `ficha.json` («notas») y `vuelta_02/notas.md` dicen «nadie ha escuchado el audio», y `escucha_del_dueno.md` dice que el dueño lo aprobó: corregir. `ficha_tecnica.md` sigue con «falta el sí del dueño para la voz» y «por renderizar»; `perfil_emocional.md` conserva una línea con los tiempos estimados; `TIN-EN-S-003` sin anotar en `registro_codigos.md`; no existen `07_revision/controles.md` ni la sección 3b de `direccion.md`.
6. **Decisiones escritas que faltan:** «twelve years» sin aproximación en la voz (director creativo); cara `neutra` de Tin (director de animación); revisión humana del título (`revision_humana` en `null`).

## Pendiente del oído humano

- Los dos sonidos de la firma con el nivel nuevo y el empalme del whoosh.
- Los cortes de 6,5, 9,0 y 16,0 s sobre la cola de la línea anterior, si el dueño no los oyó de forma expresa.

## Firmas

| Control | Firma |
|---|---|
| 1. Texto | **NO FIRMADO** (solo por «4.382 días.») |
| 2. Cifras | **FIRMADO** (con salvedad) |
| 4. Imagen | **FIRMADO** (con salvedad) |
| 4.5 Portada | **FIRMADO** (con salvedad) |
| 5. Video | **NO FIRMADO** (pendiente del render con la tarjeta corregida) |
| Firma del lápiz, §11 puntos 1 a 9 | **FIRMADO** |
| 7. Marca del canal | **FIRMADO** |
| 8. Color | **FIRMADO** (solo la medición) |

Supervisor de continuidad, 2026-11-24, segunda revisión. Veredicto general: `CAMBIOS` (un punto).
