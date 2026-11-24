# Firma del supervisor de continuidad — short 3 de Tin & Tan, vuelta 3 (render 3)

- **Fecha:** 2026-11-24.
- **Pieza revisada:** `06_final/tin_y_tan_short03_v1.mp4` del 2026-11-24 03:28 (1080×1920, 30 fps, H.264, yuv420p, AAC, 930 fotogramas, 31,0 s) y `08_entrega/TIN-EN-S-003/` del 03:29–03:30 (`video.mp4` de 2,94 MB, `miniatura.png`, los dos `.srt`, `ficha.json`).
- **Alcance:** el tramo 19,0–24,5 s, que es lo único que cambió, más la comprobación de que el resto es el render 2. Saqué yo los 930 fotogramas del final y los 930 de la entrega. Evidencias en `07_revision/vuelta_03/supervisor/`.
- **No revisado por mí:** control 3 (no oigo). Los hechos de noviembre de 2026 en una fuente externa.

## Veredicto

**Texto: FIRMADO. Video: FIRMADO.** Con esto quedan firmados todos los controles que me tocan. **Veredicto global del supervisor: `APROBADO`, con salvedades** (lista abajo). Publicar sigue pendiente de otros: ver «Lo que falta y de quién es».

## Qué comprobé

| Qué | Evidencia | Resultado |
|---|---|---|
| El render 3 solo cambia la tarjeta | Fotograma a fotograma contra el render 2: solo difieren f676 a f734 (22,53–24,47 s); fuera de ahí la diferencia máxima es 0,25 de 255 (compresión) | cumple |
| El audio es el del render 2 | Pista del render 3 contra la que extraje del render 2: **0 de diferencia** en las 496.299 muestras comparadas. Final y entrega llevan la misma pista (mismo MD5). −14,0 LUFS, pico −1,7 dB | cumple |
| «4.382 días.» se lee | Entra en f662 (22,07 s) como segundo renglón de «Steve Jobs, Apple:», nítida de f664 a f672; en el corte de 22,5 s se apaga y vuelve en un renglón, nítida de **f677 a f703**; se va en f704. Total nítido: **36 fotogramas (1,2 s)**, con 4 fotogramas de relevo en el corte (f673–f676), donde cambia todo el plano. Ya no parpadea: da tiempo a leerla | **PASA** |
| «¿Casi 12 años?» | Nítida de f707 a f733: **27 fotogramas (0,9 s)**; 13 caracteres. Coincide con «twelve years?» de la voz (23,45–24,49 s) | **PASA CON SALVEDAD** (justa: no acortar más) |
| Nada tapado | Tarjeta de dos renglones (f668): barra de Jobs hasta y = 876, texto en y 916–1068: 40 px por arriba; cabezas a 38 px o más por abajo. Tarjeta de un renglón (f690): barra hasta y = 907, texto en y 960–1024: 53 px por arriba y 104 px o más hasta el rodete. «¿Casi 12 años?» (f712): 76 px por arriba, 66 px o más por abajo. El equipo mide 12 px de panel a cabezas y 16 px a gráficos, con 0 píxeles bajo el panel | **PASA** |
| Texto | `revisar_texto.py`: inglés 79 textos (`ficha.json`, `subtitulos.srt`, textos de pantalla, `render.py`, `miniatura.py`, `tiempos.py`), **0 errores**; español 23 textos, **0 errores**. Leído en la imagen del final y de la entrega: «Steve Jobs, Apple: / 4.382 días.», «4.382 días.», «¿Casi 12 años?», «4,382 days», «Huang 11», «Altman 5», «Jobs 4,382»: sin faltas, punto de miles en español y coma en inglés. Los dos `.srt` de la entrega son idénticos a los del prompt; descripción y título sin cambios | **PASA** |
| Cifras del tramo | Contador solo sube y llega a 4.382 en f662; en f661 dice 4,380. La misma cifra en rótulo, nombre de la barra, tarjeta, `.srt` y voz | **PASA** |
| Técnico | Formato correcto en final y entrega (930 fotogramas). 0 destellos en los dos. `revisar_fotogramas.py`: sin marcas. Bucle: f929 contra f0 = 0,77 de 255; entrega 1,33. `miniatura.png` = `portada_short03.png` = f0 (1,5 de 255). `entrega.py`: lista, con el aviso fijo de portada | **PASA** |

## Firmas (estado final de mis controles)

| Control | Firma | Dónde está la evidencia |
|---|---|---|
| 1. Texto | **FIRMADO** | esta vuelta y vuelta 2 |
| 2. Cifras | **FIRMADO** (con salvedad) | vuelta 2 |
| 4. Imagen | **FIRMADO** (con salvedad) | vuelta 2 |
| 4.5 Portada | **FIRMADO** (con salvedad) | vuelta 2 |
| 5. Video | **FIRMADO** (el punto 5.4 depende además del control 3, que no es mío) | esta vuelta y vuelta 2 |
| Firma del lápiz, §11 puntos 1 a 9 | **FIRMADO** | vuelta 2 |
| 7. Marca del canal | **FIRMADO** | vuelta 2 |
| 8. Color | **FIRMADO** (solo la medición) | vuelta 2 |

## Salvedades que acepto (no bloquean)

1. «¿Casi 12 años?» dura 0,9 s nítida.
2. La flecha del calendario pasa sobre el «18» y tacha el «24» y el «25» (9,3–12,5 s); el círculo mostaza del 12 pisa los dígitos en la toma 3 (5,5–6,5 s). Para el siguiente video: `_marcas_zona` en `codigo/render.py`.
3. Portada: mayúsculas de 98 px y 22 px entre «Days?» y la silla.
4. Nombres de las barras a 56 px: se leen en teléfono, pero es el mínimo.
5. Tinta sobre tomate 3,5:1 en la cifra del pico: se lee por contorno y tamaño.
6. Primer corte en 1,0 s justo y pico al 71,2 %, no en la mitad: declarado en el prompt.

## Lo que falta y de quién es

| Qué | De quién |
|---|---|
| Control 3 (voz y audio). El dueño aprobó de oído el render 1; después bajaron los dos sonidos de la firma del lápiz. `notas.md` dice que se le avisó; no me consta su respuesta | diseñador de sonido y dueño |
| «That is twelve years?» sin palabra de aproximación en la voz y en `subtitulos.srt`: aceptarlo por escrito (no se regenera) | director creativo |
| Revisión humana del título (`revision_humana` en `ficha.json` sigue en `null`) y firma del control 6 (Entrega) | director creativo |
| Cara `neutra` de Tin: aceptarla o llevarla a `palitos.py` y a la ficha | director de animación |
| Sección 3b de `direccion.md` y firma de color (control 8.1); copiar ahí lo que medí | director de fotografía |
| Documentos: la tabla de tarjetas de §12 del prompt aún da la 8 hasta 22,47 s y la 9 desde 22,71 s (lo real: 8 hasta 23,5 s, 9 de 23,5 a 24,5 s); `ficha.json` cita la medición de color del render 2 y «falta la firma del supervisor»; `ficha_tecnica.md` con «por renderizar»; `07_revision/controles.md` no existe; `consumo.md` | editor y jefe de producción |
| Hechos de noviembre de 2026 sin comprobar en el comunicado de Nvidia (no se pudo abrir): la descripción ya lo declara | director creativo |
| El sí para publicar | dueño |

Supervisor de continuidad, 2026-11-24, tercera revisión. Veredicto general: `APROBADO` (con salvedades).
