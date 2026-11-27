# Revisión de edición · short 4 (TIN-EN-S-004) · versión 4

Revisor: editor de video (revisión independiente). Fecha: 2026-11-26.

## 1. Pieza y alcance

- **Pieza:** `06_final/tin_y_tan_short04_v4.mp4`, sha256 `f4c8224b3707` (12 primeros; calculado aquí, coincide).
- **Formato (ffprobe):** 1080×1920, 30/1 f/s, 986 f, 32,867 s; H.264 + AAC 48 kHz mono. Pico real −1,4 dBFS (tope −1: pasa). `miniatura.png` 1080×1920.
- **Qué miré:** fotogramas a resolución completa de los 12 subtítulos (f40, 120, 200, 280, 380, 450, 520, 590, 650, 790, 860, 930; recortes de la franja y 1340–1580, leídos uno por uno); las tarjetas de dato en f150, 235, 290, 380, 455, 575, 640, 800, 920; f590, 600, 612, 620 («rated M» contra el fin de T6); f717, f718, f780; el par f985 | f0; f0 y f30 (portada); detección de cortes y de movimiento por diferencia de fotogramas sobre `_sin_audio.mp4` (numpy, 108×192).
- **No miré / no puedo comprobar:** el video en movimiento ni el audio (no oigo); la sonoridad integrada (solo el pico); la ortografía por máquina (leí a mano); fotogramas intermedios que no extraje; el aspecto bajo la interfaz real de Shorts; `entrega.py` y `controles.md` (de otros).

## 2. Los 12 subtítulos grabados (resolución completa)

Todos legibles, 1 o 2 renglones, centrados, sin desbordes ni cambios de renglón raros, nunca dos paneles a la vez; la Inter Display 4.1 con raqm no rompe nada.

1 «¿Habrá un GTA 7?» · 2 «GTA es Grand Theft Auto:» · 3 «una serie de juegos / que empezó en 1997» · 4 «y que hoy hace / Rockstar Games.» · 5 «GTA 6 salió el 19 de / noviembre de 2026.» · 6 «Es el sexto juego numerado.» · 7 «Suscríbete. Aquí / comprobamos los datos.» · 8 «Clasificación M: mayores de 17.» · 9 «De GTA 5 a GTA 6:» · 10 «trece años y / sesenta y tres días.» · 11 «¿Y GTA 7?» · 12 «Rockstar no ha anunciado / ninguno. Hasta hoy.»

Ortografía y acentos correctos; nombres propios (GTA, Grand Theft Auto, Rockstar Games, M) con mayúscula. «Hasta hoy.» presente en el 12. Anchos máximos ≈ 810 px (x 135–945), dentro de 60–960.

## 3. Estado de los defectos de la v3

| ID v3 | Estado | Prueba |
|---|---|---|
| A-1 respiro largo f750–f874 | **Parcial** | Sigue siendo un solo plano de f719 a f873 (corte solo en f874): el respiro mide 4,1 s, sin partir. Lo que cambió es el reposo vivo: la diferencia de fotogramas en f750–f870 es de ≈ 24–32 por cada 10 f (v3: «casi no se mueven»), así que no es un pulso plano. Queda como M-1 (abajo). |
| A-2 `.srt` fuera de `06_final/` | **Ya no aplica** | Regla nueva del dueño: no se suben subtítulos; los `.srt` quedan en `02_prompt/`. En `06_final/` no hay `.srt`: correcto. |
| A-3 sección 6 de `direccion.md` con datos de la v2 | **No resuelto** | La sección 6 sigue con «Respiro 697–776, plano fijo de 80 f», subtítulos y 905–1085 con opacidad 0,82, datos x 100–980, bucle sobre 945 f. Contradice el video (franja 1376–1552, panel opaco, 986 f). Ver A-1 nuevo. |
| M-1 disco fuera de paleta f717–f718 | **No resuelto** | f717 y f718: disco gris azulado semitransparente de ≈ 280 px (≈ 14 % del cuadro) con llama roja y puntos amarillo oliva, tono que no está en la paleta C. Ver M-2. |
| b-2 tarjetas fuera de zona útil | **Parcial** | «La respuesta» ahora y ≈ 384–759: ya no sube de 380, pero baja ≈ 55 px dentro de la zona de acción (705). «De 5 a 6 / 13 años» y ≈ 384–719. La tarjeta «made today by Rockstar Games» llega a x ≈ 976 (> 960). No tapan caras ni acción. Sigue b. |
| b-3 «rated M» sin dato durante la voz | **Resuelto** | f596 y f600 con tarjeta; f612 (fin de T6) todavía con tarjeta; f620 ya con «from GTA 5 to GTA 6». |
| b-4 «GTA 6 out since…» entra 22 f tarde | Sin cambio | Decisión de animación (cuadro de impacto). b. |
| b-5 panel de 2 renglones hasta y 1551 | Sin cambio | 15 px dentro del 20 % inferior de la interfaz. b. |
| b-6 voz sin subtítulo f14–f30 | Sin cambio | La portada lleva «GTA 7?». b. |
| b-7 planos de firma de 1,0 s | Sin cambio | Cumple la firma. b. |
| b-8 lámpara de techo con forma de ojo | No verificada | No extraje f720–f750 a tamaño completo; en f780 el techo no se ve. Dejo b por si persiste. |
| b-9 audio mono | Sin cambio | Sin problema. |
| b-10 espacio de color sin etiquetar | No verificado | No lo reviso en la v4. |
| b-11 intermedio `_sin_audio.mp4` en `06_final/` | **Sin cambio** | Sigue allí (`tin_y_tan_short04_v4_sin_audio.mp4`); no debe subirse. b. |
| M-2 letra de 54 px | Sin cambio | Se lee con contraste alto; los paneles son la traducción completa (decisión del dueño). No bloquea. |

## 4. Cambios de la v4: comprobados

- Tarjeta «rated M»: dura hasta el fin de T6 (f612). OK.
- Tarjeta de la respuesta (GTA 7: / not announced / as of Nov 26, 2026): baja 25 px, texto íntegro, sin desbordes; el humo de fondo no resta lectura. El sello «as of Nov 26, 2026» se recompone el día de publicar (D5).
- Subtítulo T10 «Hasta hoy.»: OK.
- Tipografía con raqm: textos de las tarjetas y paneles sin desbordes ni renglones cambiados.
- Portada (f0, primer segundo): «GTA 7? / Facts, Checked», 4 palabras con mayúscula inicial, dentro de x 60–960 e y 380–1440; Tan mira el lápiz y el objeto; hacia f30 hay corte duro de firma (b-1, ya declarado, D20).
- Bucle f985 → f0: mismo lápiz, misma pose, mismo texto, misma cámara; solo cambia el fondo (excepción D6 declarada). Sin fotograma muerto. Aceptable.
- Cortes: lista medida igual que en la v3 (f30, 70, 100, 102, 157, 184, 283, 336, 338, 430, 442, 483, 512, 562, 564, 599, 719, 750 (entrada de tarjeta), 874, 906, 956); sin fotogramas muertos ni cortes nuevos.

## 5. Defectos de la v4

| ID | Gravedad | Dónde | Defecto y corrección |
|---|---|---|---|
| A-1 | A | `direccion.md` sección 6 | Sigue con los datos de la v2 (ver A-3 de la v3). La sección que me toca entregar contradice el video. Corrección: reescribirla con el mapa de ritmo medido (tabla de planos de la revisión v3 sección 3.1, actualizada a v4), franja 1376–1552 con panel opaco, datos y 380–760, respiro f719–f873, 986 f, bucle D6, sin `.srt` en la entrega. Es de papel, no de render; no toca el video. |
| M-1 | M | f750–f874 | Un solo plano de 4,1 s para el respiro (pedido 2–3 s). Mitigado por el reposo vivo; si se quiere cerrar, partir en f≈800 con un medio y empuje de 5 %. |
| M-2 | M | f717–f718 | Disco gris azulado translúcido fuera de paleta (2 f). `efectos_post`, rama `invertidos`: `mezcla=1.0` con borde de tinta y relleno de paleta, o quitar los dos cuadros. |
| b-2, b-4 a b-7, b-11 | b | ver sección 3 | Sin bloqueo. Retirar `_sin_audio.mp4` de `06_final/` antes de entregar. |

No hay defectos B de edición. El A-1 es documental y debe cerrarse antes de la entrega a YouTube; el render en sí es presentable al dueño.

Veredicto: APROBADO

Firma: editor de video · 2026-11-26 (sobre sha256 `f4c8224b3707`).
