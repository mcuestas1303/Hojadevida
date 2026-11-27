# Revisión de continuidad — short 4 (TIN-EN-S-004), versión 5 con el sello de fecha

Fecha: 2026-11-27. Qué se revisó: **final**, solo la recomposición del sello de fecha.
Pieza: `06_final/tin_y_tan_short04_v5_sello.mp4`. Se compara contra la pieza que aprobé,
`06_final/tin_y_tan_short04_v5.mp4` (informe `revision_v5_continuidad.md`). Todo lo de ese informe sigue valiendo,
incluidos los cuatro roces anotados (W1 a W4); aquí solo se comprueba que nada más cambió.

## Lo comprobado (medido por mí, no tomado del parte de producción)

| Control | Resultado |
|---|---|
| sha256 v5 | `df6b8a638e86b7227a7f087a6df30fb78e407e82f72184cf06f1de36330b59c3` (coincide con lo aprobado) |
| sha256 v5_sello | `361070e1426341d03f943e0bc8fccf87463681aeef72e9f77989d58f7e708097` (coincide con lo esperado) |
| Formato | Las dos: h264 1080×1920, 30 fps, 986 fotogramas, 32,87 s; AAC 48 kHz mono, 1542 paquetes |
| Audio | MD5 del audio decodificado idéntico en las dos: `3ff1006e4a4e69bb3f4150302db28fe6` |
| Fotogramas que difieren | 82 de 986: **f875–f956** (filtro psnr, `stats_file`). Los otros 904 (f0–f874 y f957–f985) dan error cuadrático 0,00; en f300, f870 y f970, comparados píxel a píxel, diferencia máxima 0 |
| Código | `git diff codigo/componer.py`: solo `VERSION` («v5» → «v5_sello») y `FECHA_SELLO` («Nov 26, 2026» → «Nov 27, 2026») |

### Dónde está la diferencia dentro del cuadro

La tarjeta de la respuesta va de f890 a f954 (línea de tiempo: T10 f0 = 888, +2; cierre 956, −2).

| Fotograma | PSNR | Diferencia fuerte (> 60 de 255) | Resto del cuadro |
|---|---|---|---|
| f878 (antes de la tarjeta) | ≈ 51 dB | ninguna; máximo 41, 12 píxeles sobre 24 | ruido de compresión |
| f892 | ≈ 33 dB | en el sello, x 355–542, y 679–716 | máximo ≈ 30 fuera de la tarjeta |
| f900 | ≈ 33 dB | caja x 350–534, y 663–729 (≈ 3 770 píxeles); **0 píxeles** por debajo de y 730 | hasta 60, disperso en contornos |
| f940 | ≈ 33 dB | la misma caja x 350–534, y 663–729 (≈ 3 770 píxeles); 0 por debajo de y 730 | hasta 37 |
| f953 (la tarjeta se va) | ≈ 36 dB | máximo 82, en la misma franja del sello | hasta 56 |

La caja de la diferencia es el tramo «6, 2026» → «7, 2026» más el borde derecho del recuadro del sello: el «7» es más
angosto que el «6», así que la coma, el año y el borde se corren unos píxeles a la izquierda. «as of Nov 2» no cambia.
Los fotogramas f875–f889 y f955–f956 difieren solo por compresión (comparten grupo de imágenes, f719–f956, con la
tarjeta; el siguiente fotograma clave es f957 y desde ahí las piezas son iguales). No hay ningún cambio de dibujo,
personaje, subtítulo ni fondo fuera del sello.

### Lectura de la tarjeta a resolución completa (f900 y f940, letra por letra)

- Renglón 1: «GTA 7:» con subrayado amarillo. Mayúsculas bien.
- Renglón 2: «not announced» sobre placa amarilla. Sin errores.
- Renglón 3 (sello): «as of Nov 27, 2026» en su recuadro de tinta; «Nov» con mayúscula inicial, coma y espacio en su
  sitio, dígitos enteros. El texto queda dentro del recuadro, con margen a los dos lados, y el recuadro dentro de la
  tarjeta. Sin desbordes ni glifos rotos. Idéntico en los dos fotogramas.
- Subtítulo en f900: «Rockstar no ha anunciado ninguno. Hasta hoy.», sin cambios respecto de la v5.

### La fecha

- Hoy es 2026-11-27 y la publicación está programada para hoy a las 16:00 (−06:00). El sello dice Nov 27, 2026: coincide.
- La misma fecha en lo que acompaña al video: descripción de `08_entrega/TIN-EN-S-004/ficha.json` y de
  `publicacion.md` («Facts as of November 27, 2026», «as of November 27, 2026»); `fecha_sugerida`
  2026-11-27T16:00:00-06:00; `medidas_composicion.json` «Nov 27, 2026». No queda ningún «Nov 26» como fecha del sello
  en la entrega. La dirección (línea 413) todavía cita el sello del día 26 y remite a D5, que manda recomponerlo el
  día de publicar: es historia, no un texto que salga al público.
- Las notas de la ficha dicen «la imagen solo cambia en la tarjeta de la respuesta, f875–f956»: el rango es el medido;
  lo exacto es que el cambio de dibujo está en el sello (f890–f954) y el resto del rango es ruido de compresión.

## Lo que no pude comprobar

1. **La relectura del remate.** No tengo acceso a la web en esta revisión. Lo que sigue es lo que informa producción,
   no lo que yo leí: en la lista de comunicados de Take-Two el último es del 2026-11-20 y ninguno nombra un GTA 7; la
   página de juegos de Rockstar muestra GTA VI como el más reciente. **El Newswire de Rockstar no se pudo leer** (se
   dibuja con scripts), así que la ausencia de anuncio está comprobada en dos de las tres fuentes. Conviene que una
   persona abra el Newswire antes de las 16:00; cuesta un minuto y es el único hueco de la afirmación del sello.
2. **El adelanto de la fecha.** `publicacion.md` dice que el dueño adelantó la publicación al 27 («Sí, adelántalo», vía
   el Manager de redes). No vi ese mensaje; lo tomo como dicho por el archivo.
3. **Oír el audio.** No se volvió a escuchar: es bit a bit el mismo que el de la v5, y siguen pendientes de oído humano
   los mismos puntos de `firmas.md`.
4. La portada, el color y el resto de controles no se repitieron: f0–f874 son idénticos a la v5 y la miniatura no se
   tocó. `firmas.md` sigue apuntando a `df6b8a638e86`; no lo modifiqué (fuera de mi encargo).
5. El sello dice el día en hora de El Salvador; quien lo vea después de la medianoche de su zona leerá una fecha de
   ayer. Es lo que pide D5 y no es un defecto.

## Veredicto por toma

| Toma | Personaje fiel | Emoción se lee | Cámara | Actuación | Continuidad | Defectos | Veredicto |
|---|---|---|---|---|---|---|---|
| Tarjeta de la respuesta (f890–f954) | igual que v5 | igual que v5 | igual que v5 | igual que v5 | sello con la fecha de hoy; texto correcto | ninguno nuevo | APROBADA |
| Resto (f0–f874, f957–f985) | idéntico a v5 (diferencia 0) | — | — | — | — | los de v5 (W1 a W4, anotados) | APROBADA |

Firma: supervisor de continuidad, 2026-11-27, sobre `361070e14263`.

Veredicto: APROBADO
