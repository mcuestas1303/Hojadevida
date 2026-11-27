# Reporte de publicación — TIN-EN-S-004 · What Is GTA 6, and Is a GTA 7 Coming?

> Escrito el 2026-11-26; **puesto al día el 2026-11-27 con la versión 5.** Estado: **la pieza pasó la puerta de
> presentación** (los cinco oficios aprobaron, `07_revision/firmas.md`) y el dueño dio el sí a preparar la entrega. **No
> publicado.** Publicación prevista: miércoles 2026-12-02, 16:00 (hora de El Salvador), hueco H01.
> Video: `06_final/tin_y_tan_short04_v5.mp4` (32,87 s, 1080×1920, sha256 `df6b8a638e86`). Entrega:
> `08_entrega/TIN-EN-S-004/` (`video.mp4`, `miniatura.png`, `ficha.json`; `entrega.py`: lista para entregar, 0 errores).
> Versiones: v1 sin revisar; v2 no aprobada por el dueño («intentan correr y casi no se mueven»); v3 y v4 frenadas en
> la puerta; v5 aprobada por los cinco oficios. Qué falló en cada una: `metodo/registro_de_fallos.md`.

## 1. Qué es

Short de acción de Tin & Tan (primer video del formato de acción, hueco H01 de la tanda 01). Tan pregunta «Will there
be a GTA 7?»; la pregunta se dibuja sola como rival y Tin y Tan la bajan a golpes: qué es GTA, qué es GTA 6, su
clasificación, cuánto se esperó, y la respuesta honesta: Rockstar no ha anunciado ninguno, a la fecha.

## 2. Objetivos

| Objetivo | Métrica | Meta | Plazo | Cómo acerca al Programa de socios |
|---|---|---|---|---|
| Entrar al Programa de socios lo antes posible (dueño, 2026-11-23) | «Se quedó a mirar» | 5 puntos o más sobre el short 2 a la misma edad | 48 h | Casi todo el tráfico es feed de Shorts: la vista calificada se decide en los 3 primeros segundos |
| Apoyo | Vistas | 500 o más | 48 h | Vistas de Shorts hacia el umbral |
| Apoyo | Suscriptores por mil vistas | Sin dato propio (hoy 0): primera medida | 7 días | Se estrena el pedido de suscripción antes del final |
| Apoyo | Porcentaje medio visto | No más de 5 puntos bajo el short 2 | 48 h | Retención |
| Límite | Avisos de YouTube | Ninguno | Siempre | Un aviso cuesta la admisión |

## 3. Lo que se consideró

| Capa | Qué se tomó en cuenta | Fuente y fecha |
|---|---|---|
| Estadísticas del canal | Short 2 (GTA) es el mejor del canal; público menor de 45, mayoría hombres, tramo fuerte de 13 a 17; 0 suscriptores; a los últimos segundos llega menos de la mitad | Studio, lectura de Keter, 2026-11-26 (`estadisticas/datos/`, no se sube) |
| Calendario y temporada | GTA 6 salió el 2026-11-19; el interés baja cada día; límite del comercial 2026-12-03 | `comercial/radar_de_tendencias.md`, 2026-11-26 |
| Interés y preguntas de búsqueda | En YouTube «gta 7» pesa más que «what is gta 6» (16 frente a 12, media de 7 días); en la web es al revés (7 frente a 49) | Trends, EE. UU., Keter, 2026-11-26; `cambios/2026-11-26_gancho_gta7_short4.md` |
| Hechos (qué se afirma y qué no) | Sigla y 1997 (Wikipedia); Rockstar Games y fecha (comunicado de Take-Two); Mature 17+ (ESRB); 4.811 días = 13 años y 63 días; **ausencia** de anuncio de GTA 7. No se afirma que no vaya a haber, ni fecha, ni rumor. **Se quitó «Each numbered game tells a new story»** | `comercial/2026-11-26_hechos_short4_gancho_gta7.md` |
| Filtro de políticas de YouTube | F1 a F13: pasado sobre el tema y el guion del brief; **falta repetirlo sobre el video terminado** (F8 y F9 sobre todo) | `MOTOR_DE_CONTENIDO.md`, 5b |
| Forma (acción, tiempos, color, sonido) | 7 golpes con tiempos medidos, 23 planos, paleta C, fuego plano, humo con contorno, percusión por código, voz al 110 % | `02_prompt/direccion.md`; `05_audio/linea_de_tiempo.md` |
| Ajustes por limitantes (regla de adaptación) | La voz de Tin salió ≈ 2,8 s más larga: se quitó una frase y se cerraron pausas (32.87 s). La suscripción pasó a 16.1 s. Dibujos planos: los «laterales» y el POV se filmaron de frente. Mostrador en gris claro y tienda de 9 u de ancho | `05_audio/linea_de_tiempo.md`; `07_revision/controles.md` |

## 4. Cómo se conecta

- **Con lo anterior:** vuelve el mando mostaza del short 2, quieto en la repisa del fondo; la firma del lápiz se atrapa por primera vez dentro de un mundo.
- **Con lo siguiente (generales; el significado está en el registro de pistas, privado):** queda la `caja_registradora_rota`; el rival no se borra, deja un asterisco; lo último del trazo se escurre por una grieta del suelo, a la derecha. Ninguna lleva voz ni texto y el video se entiende sin ellas.
- **Siguiente video:** hueco H02 de la tanda; el tema se cierra el jueves con el radar (`calendario_de_publicacion_2026-12.md`).

## 5. Producción

- Motor de acción (three.js grabado con Chromium) + composición 2D (`codigo/componer.py`) + sonido por código (`codigo/audio.py`). Guion: `motor_de_accion/guiones/tin_en_s_004.js`.
- Gasto: **3,1 créditos** (voz: Kevin 2,6 y Zelda 0,5; una generación cada una). Imagen, video, música y efectos: 0.
- Entorno nuevo en la biblioteca: `tienda_de_videojuegos`.

## 6. Cuándo se mide

48 horas, 7 días y 28 días después de publicar, contra el short 2 a la misma edad. Orden de lectura: «se quedó a mirar» y
segundo 3; segundos 5 a 10; retención en 16.1 s (la suscripción: ¿se van ahí?); pico en 23.1 s–24.6 s; caída o no
en 29.5 s (la respuesta honesta); suscriptores por mil vistas; comentarios; avisos.

## 7. Lo que queda antes de publicar (al 2026-11-27)

1. **Escucha del dueño.** Nadie del equipo puede oír. Por medida todo pasa (−14,0 LUFS, −1,4 dBTP, cada golpe un
   fotograma antes del contacto), pero falta oír: «GTA 6 came out on November 19, 2026» (el reconocedor oye un «it» de
   más; por medida, artefacto), «Subscribe. We check the facts.» (puede sonar áspera en los picos), «over» junto al mazazo
   y el silencio antes del remate. Si se oye el «it», regenerar esa línea cuesta créditos y necesita su sí.
2. **El día de publicar (2026-12-02): relectura del remate y sello de fecha.** Se releen las fuentes de «Rockstar hasn't
   announced one» (`publicacion.md`, «Antes de publicar»). Si sigue siendo cierto, se recompone el sello «as of» con la
   fecha de ese día (≈ 10 min, 0 créditos; cambia el archivo, así que edición y continuidad firman ese tramo) y se cambian
   las tres fechas «November 26, 2026» de la descripción. Si alguna fuente ya nombra la entrega siguiente, **no se publica**.
3. **Sin subtítulos subidos** (regla del dueño, 2026-11-26): el video los lleva grabados en español.
4. **Roces medios que continuidad dejó anotados y no frenaron:** segundo 21,5 (los pies del rival pasan por el borde de
   la cabeza de Tan, 2 fotogramas), 2,2 (el puño del rival en la punta de la visera de Tin), 17,1 (un fotograma) y 29,8
   (una gota de tinta cruza la cara de Tin). Un disco gris fuera de paleta 2 o 3 fotogramas en la explosión (edición).
5. **Empaque:** título, descripción y etiquetas en `08_entrega/TIN-EN-S-004/ficha.json`, ajustados al método de metadatos
   aprobado por el dueño (sin #Shorts, 3 hashtags, la primera línea repite el tema). El Manager de redes los revisa con la
   búsqueda del día. «No creado para niños» y «sin contenido sintético realista»: propuesta del equipo, los decide el dueño.
6. **Filtro de políticas sobre el video terminado** (F8 y F9): continuidad comprobó las reglas duras (sin sangre ni armas
   de fuego, nada del juego ni marcas como objeto, descargo en la descripción). No se releyeron las fuentes de los datos
   ni se auditaron las licencias en esta vuelta.
7. **Medición confundida** (sigue igual): cambian a la vez la forma, el gancho, la paleta, el universo y el lugar de la
   suscripción; lo que salga no se podrá atribuir a una sola cosa.
