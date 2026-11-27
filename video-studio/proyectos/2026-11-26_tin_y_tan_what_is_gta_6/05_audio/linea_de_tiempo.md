# Línea de tiempo con la voz real — short 4 (986 f = 32.87 s)

Hecha por `codigo/tiempos.py` con `voz_tin_kevin.wav` y `voz_tan_zelda.wav` (una generación cada una; no se
regeneran). Cada línea al 110 % (`atempo=1.10`), pausas internas cerradas (0,07 a 0,22 s), respiro de 2 f entre líneas. **Ninguna persona ha escuchado el audio.**

| Línea | Quién | f inicio | f fin | s inicio | Dura (f) | Texto | Subtítulo |
|---|---|---|---|---|---|---|---|
| A | Tan | 14 | 60 | 0.47 | 46 | Will there be a GTA 7? | ¿Habrá un GTA 7? |
| T1 | Tin | 84 | 169 | 2.80 | 85 | GTA is short for Grand Theft Auto: | GTA es Grand Theft Auto: |
| T2 | Tin | 171 | 247 | 5.70 | 76 | a game series that started in 1997, | una serie de juegos que empezó en 1997 |
| T3 | Tin | 249 | 314 | 8.30 | 65 | made today by Rockstar Games. | y que hoy hace Rockstar Games. |
| T4 | Tin | 316 | 428 | 10.53 | 112 | GTA 6 came out on November 19, 2026. | GTA 6 salió el 19 de noviembre de 2026. |
| T5 | Tin | 430 | 481 | 14.33 | 51 | It's the sixth numbered game. | Es el sexto juego numerado. |
| C | Tan | 483 | 548 | 16.10 | 65 | Subscribe. We check the facts. | Suscríbete. Aquí comprobamos los datos. |
| T6 | Tin | 550 | 612 | 18.33 | 62 | Rated M: seventeen and over. | Clasificación M: mayores de 17. |
| T8 | Tin | 614 | 679 | 20.47 | 65 | From GTA 5 to GTA 6: | De GTA 5 a GTA 6: |
| T9 | Tin | 738 | 836 | 24.60 | 98 | thirteen years and sixty-three days. | trece años y sesenta y tres días. |
| B | Tan | 838 | 886 | 27.93 | 48 | So, GTA 7? | ¿Y GTA 7? |
| T10 | Tin | 888 | 969 | 29.60 | 81 | Rockstar hasn't announced one. As of today. | Rockstar no ha anunciado ninguno. Hasta hoy. |

## Contactos y momentos (fotogramas)

| Clave | f | s |
|---|---|---|
| rival_entra | 30 | 1.00 |
| rival_crece | 46 | 1.53 |
| pisoton | 60 | 2.00 |
| K1 | 82 | 2.73 |
| K2 | 169 | 5.63 |
| cartel | 257 | 8.57 |
| rival_ataca | 263 | 8.77 |
| salto_mostrador | 281 | 9.37 |
| K3 | 314 | 10.47 |
| dibuja_baston | 430 | 14.33 |
| dibuja_espada | 514 | 17.13 |
| KB | 548 | 18.27 |
| tele_punta | 562 | 18.73 |
| K4 | 574 | 19.13 |
| mazo | 586 | 19.53 |
| K5 | 612 | 20.40 |
| carrera | 671 | 22.37 |
| KR | 694 | 23.13 |
| tele_choque | 715 | 23.83 |
| invertidos | 717 | 23.90 |
| radiales | 719 | 23.97 |
| claro | 724 | 24.13 |
| bola | 728 | 24.27 |
| enfria | 739 | 24.63 |
| K6 | 886 | 29.53 |
| implosion | 888 | 29.60 |
| implosion_fin | 905 | 30.17 |
| armas_gotas | 908 | 30.27 |
| asterisco | 918 | 30.60 |
| escurre | 926 | 30.87 |
| escurre_fin | 941 | 31.37 |
| lapiz_a_tan | 943 | 31.43 |
| cierre | 956 | 31.87 |
| N | 986 | 32.87 |

## Decisiones del equipo (con su porqué)

1. **Se quita «Each numbered game tells a new story.»** Con todas las frases el video medía ≈ 34 a 35 s (la voz de
   Tin salió ≈ 2,8 s más larga que la estimada). Es la primera del orden de recorte de la dirección (sección 2) y la
   de fuente más débil. **El golpe del bastón (4) se conserva**: cae en «seventeen and over», como respuesta al
   bloqueo, y deja los siete golpes y la mecha del televisor.
2. **La suscripción va en f483–f548 (16.1 s; 49 % del video), no al cierre.**
   `PARAMETROS.md` («Pedir la suscripción», a prueba desde el 2026-11-26; el dueño lo confirmó hoy): una vez, con voz,
   antes del final, en la primera mitad y pegada al dato fuerte. Va justo después de «GTA 6 came out on November 19,
   2026. It's the sixth numbered game.» (el dato del título), en el único hueco donde Tin no habla y no hay contacto:
   mientras el rival dibuja su espada. No lleva texto en pantalla (solo su subtítulo). El cierre queda con la firma.
3. **«So, GTA 7?» la dice Tan** (D2 de la dirección) y el remate «Rockstar hasn't announced one. As of today.» termina
   en f969 (c −17; la firma pide c −17 o antes).
4. **Respiro entre líneas de 2 f** y la pausa de voz del remate recortada (el dato entra durante el enfriamiento de la
   explosión, no en el pico): es lo que deja el video dentro de 30 a 33 s sin tocar ninguna otra frase.
5. No se movieron: los desfases de cada golpe (anticipación K −12 a −7, pausa K −6 a −1, contacto K y K +1, voz en
   K +2) ni las reglas 2.1.
