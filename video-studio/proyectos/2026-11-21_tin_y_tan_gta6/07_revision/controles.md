# Controles de calidad — short 2 de Tin & Tan (la espera de GTA 6)

Regla: `video-studio/manual/12_controles_de_calidad.md`. Estado: **video renderizado (v1), revisado con medidas; falta la escucha y faltan las firmas** (ver «Vuelta 1» al final).

## Control de texto (2026-11-21, Generador)

- `revisar_texto.py 02_prompt/subtitulos.srt --idioma en`: 9 textos, **no pasa** por un solo motivo: falta el
  corrector ortográfico (`pyspellchecker`), que se instala con el sí del dueño. Ningún otro hallazgo.
- **Lectura a mano, palabra por palabra** (mientras no haya corrector), de las 9 líneas de voz/subtítulos, los 19
  textos de pantalla de §12 del prompt y el título: sin faltas. Nombres propios: no aparece ninguno en pantalla;
  «GTA» va en mayúsculas por ser sigla. Todas las cifras son enteras (13, 365, 4,745, 3, 4,748, 63, 4,811): no
  hay decimales ni fracciones, así que no hace falta «≈». Separador de miles con coma, correcto en inglés.
- **Falta** (no es de esta etapa): la firma del supervisor de continuidad, y repetir el control sobre la ficha de
  publicación, la miniatura y el texto dibujado en el código cuando existan.

## Control de texto con corrector (2026-11-21, Generador)

El dueño autorizó instalar `pyspellchecker` («sí a todo, instala el corrector»). Instalado con `pip install
pyspellchecker`. «GTA» se añadió a `video-studio/glosario.txt` con su porqué.
`revisar_texto.py 02_prompt/subtitulos.srt --idioma en`: 9 textos, **PASA: 0 errores**.
Falta la firma del supervisor de continuidad y repetirlo sobre la ficha de publicación, la miniatura y el código.

## Vuelta 1 del video (2026-11-21, montaje y render por código)

Pieza: `06_final/tin_y_tan_short02_v1.mp4` (28,5 s, 855 fotogramas). Evidencia y detalle: `07_revision/vuelta_01/notas.md`
(hojas de contacto en `vuelta_01/analisis/`, salidas en `comprobar_video.txt`, `revisar_color.txt`, `revisar_texto.txt`,
`fotogramas/revision.md`; niveles en `05_audio/medidas_audio.json`). Quien montó se revisó primero; **ningún control
está firmado por su responsable todavía**.

| Control (manual 12) | Resultado | Quién | Evidencia |
|---|---|---|---|
| 1. Texto: `revisar_texto.py` sobre `subtitulos.srt`, `codigo/render.py` y `codigo/miniatura.py` (`--idioma en`) | **PASA: 0 errores** (44 textos) | quien montó; **falta la firma del supervisor de continuidad** | `vuelta_01/revisar_texto.txt` |
| 1. Texto leído a mano en las hojas de contacto, glifos y zona segura | PASA: igual que la tabla de §12, sin cuadros, las 12 filas dentro de la zona segura | quien montó; falta el supervisor | `vuelta_01/analisis/hoja_01..03.jpg` |
| 2. Cifras | PASA en pantalla: 13, 365, 4,745, 3, 4,748, 63, 4,811 y 13, enteras y las mismas que la voz del guion y los subtítulos; **no recalculadas en esta vuelta** (la cuenta está en §3 del prompt) | falta el supervisor | prompt §3 |
| 3. Voz y audio: sonoridad | **PASA con medida**: −14,0 LUFS, pico real −1,3 dBTP (archivo final) | quien montó | `comprobar_video.txt`, `medidas_audio.json` |
| 3. Voz y audio: transcripción contra guion, clics, música que tape la voz | **NO COMPROBADO: nadie ha escuchado la voz ni la mezcla** | **falta el diseñador de sonido** | `notas.md`, «No se pudo comprobar» |
| 4. Imagen: personajes contra ficha, nada tapado | PASA a la vista (lados, espejo, colores, objetos de mano de las fichas); el mando sale de la zona segura en las tomas 1 y 13 y el calendario 6 px en la 12 | falta el supervisor | `notas.md`, defectos 1 y 2 |
| 4.5 Portada del Short | `06_final/portada_short02.png` (1080x1920; texto en x 114–850, y 484–686, dentro de la zona útil). En el video el «GTA 5?» va en y = 288, fuera de esa zona | falta el supervisor | `notas.md`, defecto 10 |
| 5. Video: formato | PASA: 1080x1920, 30 fps, H.264, yuv420p, AAC, 28,5 s | quien montó | `comprobar_video.txt` |
| 5. Video: `revisar_fotogramas.py` | PASA: «Sin marcas» (ni congelados, ni vacíos, ni destellos) | quien montó | `vuelta_01/fotogramas/revision.md` |
| 5. Video: bucle | PASA con medida (el último fotograma empalma con el 0) | quien montó | `comprobar_video.txt` |
| 5. Video: cortes contra la voz | Con medida: ningún corte llega tarde; cuatro pisan el final de la línea anterior (0,04 a 0,15 s) y el de 25,5 no tiene margen. **Falta comprobarlo al oído** | falta el editor y el diseñador de sonido | `notas.md`, defecto 3 |
| 8. Color: `revisar_color.py` | PASA con medida: ≈ 93 % en paleta, saturación ≈ 17 %, variación ±2 %; mostaza único acento y tomate solo en las tomas 10 y 12 | quien montó; **falta la firma del supervisor** | `vuelta_01/revisar_color.txt` |
| Rúbrica (`07_revision/`) | sin puntuar | — | — |
| 6. Entrega | no corresponde todavía (faltan la escucha y las firmas) | — | — |
