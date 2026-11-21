# Controles de calidad — short 2 de Tin & Tan (la espera de GTA 6)

Regla: `video-studio/manual/12_controles_de_calidad.md`. Estado: **prompt, antes de voz y render**.

## Control de texto (2026-11-21, Generador)

- `revisar_texto.py 02_prompt/subtitulos.srt --idioma en`: 9 textos, **no pasa** por un solo motivo: falta el
  corrector ortográfico (`pyspellchecker`), que se instala con el sí del dueño. Ningún otro hallazgo.
- **Lectura a mano, palabra por palabra** (mientras no haya corrector), de las 9 líneas de voz/subtítulos, los 19
  textos de pantalla de §12 del prompt y el título: sin faltas. Nombres propios: no aparece ninguno en pantalla;
  «GTA» va en mayúsculas por ser sigla. Todas las cifras son enteras (13, 365, 4,745, 3, 4,748, 63, 4,811): no
  hay decimales ni fracciones, así que no hace falta «≈». Separador de miles con coma, correcto en inglés.
- **Falta** (no es de esta etapa): la firma del supervisor de continuidad, y repetir el control sobre la ficha de
  publicación, la miniatura y el texto dibujado en el código cuando existan.
