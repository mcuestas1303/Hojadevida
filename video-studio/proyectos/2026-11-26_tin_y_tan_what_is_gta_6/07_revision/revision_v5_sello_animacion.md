# Revisión de animación: short 4, v5 con el sello de fecha recompuesto

Pieza: `06_final/tin_y_tan_short04_v5_sello.mp4` (sha256 `361070e14263`). Pieza que aprobé: `06_final/tin_y_tan_short04_v5.mp4` (`df6b8a638e86`), informe `revision_v5_animacion.md`.
Pregunta: ¿cambió algo del movimiento o de la actuación? Respuesta: no.

## Qué leí y miré
- Leí enteros `revision_v5_sello_continuidad.md` y `revision_v5_sello_edicion.md`.
- Miré con mis ojos, de la carpeta `continuidad_sello` del scratchpad, los fotogramas de las dos piezas en f900 (`a_0900.png` v5, `b_0900.png` v5_sello) y f940 (`a_0940.png`, `b_0940.png`), más el mapa de diferencia `diff_940.png`.

## Lo que vi
- **f900** (tramo f875–f956, tarjeta en pantalla): Tin (naranja, gorra, lápiz) y Tan en el mismo sitio, misma pose del brazo con el bate negro, misma cámara, mismo escombro y mismo subtítulo. Solo cambia el sello: «Nov 26, 2026» pasa a «Nov 27, 2026».
- **f940**: Tin de pie con el lápiz a un costado, Tan (verde, pañuelo amarillo) con la misma pose y la misma mirada hacia Tin, mismo plano, mismo fondo. De nuevo la única diferencia visible es el sello.
- **Mapa de diferencia f940**: lo brillante es el tramo «6, 2026» y el borde del recuadro del sello. Sobre los personajes y el decorado solo hay un trazo tenue de contornos, que es ruido de recodificación. No hay dobles siluetas ni desplazamientos.

## En qué me apoyo
1. **Audio.** MD5 del audio decodificado idéntico en las dos piezas (dos revisores lo midieron). No cambia el ritmo ni el tiempo de la actuación.
2. **Formato.** 986 fotogramas, 30 fps en ambas, así que el timing no se movió.
3. **Medición de continuidad por fotograma.** Filtro psnr sobre los 986 fotogramas: 904 dan error 0,00 (f0–f874 y f957–f985). Difieren 82 (f875–f956), todos dentro de un mismo grupo de imágenes con la tarjeta. Esto cubre todas las tomas de actuación y el bucle.
4. **Medición dentro del tramo distinto.** En f900 y f940 la diferencia fuerte está en una caja fija (x 350–534, y 663–729) y no hay ningún píxel de diferencia fuerte por debajo de y 730. Ahí están los personajes. El resto es ruido de compresión.
5. **Código.** `git diff` de `componer.py`: solo `VERSION` y `FECHA_SELLO`. No se tocó ninguna animación ni muelle.
6. **Portada y último fotograma** idénticos píxel a píxel (edición).

Esta prueba me basta. La medición descarta cambios de movimiento en 904 de 986 fotogramas con error cero, y en los 82 restantes la diferencia es una caja del tamaño del sello. Mis ojos confirman en f900 y f940 que las poses de los personajes son las mismas. Como el audio y el código también coinciden, la actuación, el timing y las poses finales son los que firmé. Los roces que anoté en la v5 siguen siendo los mismos y no se agregó ninguno.

## Lo que no pude comprobar por mí mismo
- No tengo consola: no medí ni reproduje nada, no vi el video en movimiento. Me fío de los psnr y de los md5 de los dos revisores, que coinciden entre sí (82 fotogramas, mismo audio).
- Solo vi f900 y f940, no los 82 fotogramas del tramo. La continuidad del movimiento entre ellos la deduzco de la medición y no la vi.
- La entrada y salida de la tarjeta (muelle) no la vi en movimiento. Que coincida con la v5 sale de que la diferencia fuerte se limita a la caja del sello también en f892 y f953, según el informe de continuidad.
- La exactitud de la fecha («Nov 27») y la relectura de que no hay anuncio de GTA 7 (queda sin leer el Newswire de Rockstar) no son asunto de animación. No las evalúo.

Firma: director de animación, 2026-11-27, sobre `361070e14263`.

Veredicto: APROBADO
