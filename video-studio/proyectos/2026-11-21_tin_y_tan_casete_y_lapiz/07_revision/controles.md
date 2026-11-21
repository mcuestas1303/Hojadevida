# Controles de calidad · TIN-EN-S-001 (short 1, casete y lápiz)

> Controles de `video-studio/manual/12_controles_de_calidad.md`, creados el 2026-11-21 **después** de entregar y
> subir este video en privado. Este registro se hizo a posteriori.

## Decisión del dueño

«Deja este video así, pero que quede esa regla para los próximos» (2026-11-21). El video, la miniatura y la ficha
**no se cambian**. `entrega.py` ya no los aprueba (las cifras con fracción y decimales no llevan «≈»), y eso es
esperado: este código quedó entregado antes de la regla y no se vuelve a subir.

## Control 1 · Texto (supervisor de continuidad, 2026-11-21)

- `revisar_texto.py` sobre ficha, subtítulos, `render_v2.py`, `miniatura.py` y `marca.py`: sin errores de nombres,
  espacios, puntuación ni separador decimal. Lectura a mano, palabra por palabra, de título, descripción,
  etiquetas, subtítulos y textos en pantalla → sin errores de ortografía.
- Corrector Hunspell instalado con el sí del dueño (2026-11-21) y corrido después: **0 errores de ortografía** en
  ficha, subtítulos, textos en pantalla, miniaturas y banner. Glosario: «ft», «vol», «tech».
- Nombres: el banner y las hojas de personaje decían «tin & tan». Corregido a «Tin & Tan» y regenerado.

## Control 2 · Cifras (recalculadas)

- 2.700 s × 1⅞ in/s = 5.062,5 in ÷ 12 = **421,9 ft → ≈ 422**. La pantalla y la descripción dicen **421** (truncado);
  la voz dice «about four hundred twenty». **Hallazgo**: diferencia de 1 pie, por truncar en vez de redondear. Se
  deja así por decisión del dueño.
- π × 1,38 in = 4,34 in ≈ 4⅓ ✔ · 5.062,5 ÷ 4,34 = 1.167,8 ≈ 1.170 ✔ · 1.170 ÷ 2 = 585 s ≈ 9,75 min («almost ten
  minutes») ✔.
- Con la regla nueva, este video habría llevado «≈ 1.9 in/s», «≈ 422 ft», «≈ 4.3 in» y «≈ 4.8 cm/s» fuera de la
  cita de Philips.
