# Formatos de salida

Dos formatos, según dónde se publica. El `Tipo` del prompt decide cuál toca y el validador lo
comprueba. Fuentes al final; las plataformas cambian sus límites, así que se revisan antes de
cada publicación.

## Video largo (capítulos e intro) — YouTube

| | |
|---|---|
| Aspecto | 16:9, horizontal |
| Máster | 1920 × 1080 px |
| Fotogramas | Los mismos con que sale del generador (24 o 30 fps); no se convierten |
| Archivo | MP4, video H.264 progresivo, audio AAC-LC a 48 kHz estéreo, `moov` al inicio |
| Bitrate de referencia | 8 Mbps de video a 1080p; 384 kbps de audio estéreo |
| Miniatura | 1280 × 720 px, 16:9 |

## Short — YouTube Shorts, reutilizable en Reels, TikTok y Facebook

| | |
|---|---|
| Aspecto | 9:16, vertical |
| Máster | 1080 × 1920 px |
| Duración | **60 s como máximo** (regla del estudio) |
| Fotogramas y archivo | Igual que el video largo |
| Zona segura | Personajes, objeto y gesto dentro del centro de 880 × 1420 px; nada importante en el borde superior, el inferior ni el derecho |
| Audio | Voz y música propias, sin pistas de terceros, para que el mismo archivo sirva en todas las redes |
| Marcas | Sin marca de agua ni logotipo de ninguna plataforma |

Por qué 60 s: YouTube clasifica como Short cualquier video vertical o cuadrado de hasta 3
minutos, pero los límites y lo que cada red favorece cambian de una a otra. Hasta 60 s el
mismo archivo entra en todas sin recortes. El validador rechaza un short de más de 180 s y
avisa si pasa de 60 s.

La zona segura es una regla conservadora del estudio: las fuentes no coinciden en la medida
exacta que tapa la interfaz de cada aplicación.

## Cómo se llega al máster

- Los clips finales se generan a 720p (lo más alto en el precio que usa el estudio) en el
  aspecto del formato: horizontales para largos, verticales para shorts.
- `ensamblar.py --formato largo` o `--formato short` los une y los lleva al máster de 1080.
  Subir a 1080 no agrega detalle, pero es el tamaño que piden las plataformas.
- **Un short no se recorta de un capítulo**: de un clip horizontal de 720p solo quedarían
  405 px de ancho. Se reutiliza el guion (un momento del capítulo), no los píxeles; el short
  lleva sus propios keyframes verticales.

## Contenido «hecho para niños» en YouTube

Con esa marca, YouTube desactiva los comentarios, la campanita de notificaciones, las
pantallas finales, las tarjetas y los anuncios personalizados. Por eso los videos no piden
suscribirse, comentar ni «ver el siguiente»: no funcionaría y va contra la guía de 1 a 3 años.

## Fuentes (consultadas el 2026-11-20)

- [YouTube: ajustes de codificación recomendados](https://support.google.com/youtube/answer/1722171?hl=en)
- [YouTube: resolución y relación de aspecto](https://support.google.com/youtube/answer/6375112?hl=en&co=GENIE.Platform%3DDesktop)
- [YouTube: Shorts de tres minutos](https://support.google.com/youtube/answer/15424877?hl=en)
- [YouTube: definir la audiencia del canal o del video](https://support.google.com/youtube/answer/9527654?hl=en-ZW&ref_topic=9689353)
- [YouTube: anuncios en contenido hecho para niños](https://support.google.com/youtube/answer/9713557?hl=en)
- [Kapwing: tamaños de video en redes sociales, guía 2026](https://www.kapwing.com/resources/social-media-video-aspect-ratios-and-sizes-the-2025-guide/)
- [Sprout Social: especificaciones de video en redes](https://sproutsocial.com/insights/social-media-video-specs-guide/?amp)
