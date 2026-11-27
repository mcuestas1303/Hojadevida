# Revisión de sonido: short 4 v5 con sello de fecha recompuesto

Fecha: 2026-11-27

## Qué comprobé

Comparé `06_final/tin_y_tan_short04_v5.mp4` (la que aprobé) con `06_final/tin_y_tan_short04_v5_sello.mp4` (la nueva).

| Prueba | v5 aprobada | v5_sello |
|---|---|---|
| sha256 (12 primeros) | df6b8a638e86 | 361070e14263 (coincide con lo esperado) |
| MD5 del audio decodificado (`-vn -f md5`) | 3ff1006e4a4e69bb3f4150302db28fe6 | 3ff1006e4a4e69bb3f4150302db28fe6 |

Los archivos son distintos, como era de esperar porque cambió la imagen. El audio decodificado es idéntico bit a bit. Por eso lo que aprobé en `revision_v5_sonido.md` (voz palabra por palabra contra el guion, mezcla, ausencia de clics) sigue valiendo sin cambios.

## Medidas de la pieza nueva (ebur128, peak=true)

- Sonoridad integrada: −14.0 LUFS (objetivo −14 ±1: pasa).
- Pico real: −1.4 dBTP (límite ≤ −1: pasa).
- Rango de sonoridad: 2.1 LU.
- Duración del audio: 32.86 s.

## Pendiente

- La escucha final del dueño, como en la v5 aprobada. No hay cambio de audio que la agrave, pero la escucha humana sigue siendo suya.
- No juzgué la imagen del sello: eso es del control de edición y de continuidad.

Firma: diseñador de sonido, 2026-11-27

Veredicto: APROBADO
