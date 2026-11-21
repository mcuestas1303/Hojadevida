# Revisión, vuelta 1 — short 2 de Tin & Tan («How Many Days Did We Wait for GTA 6?»)

Fecha: 2026-11-21. Pieza: `06_final/tin_y_tan_short02_v1.mp4` (no se sube al repositorio; se rehace con
`python3 codigo/render.py`, unos 90 s). Todo lo de aquí se comprobó **con medidas y mirando las hojas de contacto**.
**Nadie ha escuchado ni la voz ni la mezcla**: lo que depende del oído está en «No se pudo comprobar».

## Qué se hizo

1. Diálogo al 110 % (`codigo/armar_dialogo.py` → `05_audio/dialogo_110.mp3`, `05_audio/linea_de_tiempo_voz.md`).
2. Cortes de las 13 tomas reajustados a la voz real, en la rejilla de 0,5 s (prompt, secciones 6, 7, 11, 12 y 13;
   `02_prompt/subtitulos.srt`).
3. `herramientas/palitos.py` 1.2: objetos de mano `control` y `calendario`, y el gráfico `mando()`.
4. Efectos, música y mezcla por código (`codigo/audio.py`); render por código (`codigo/render.py`); portada
   (`codigo/miniatura.py`).

## Tabla de cortes real (28,5 s, 855 fotogramas, 57 pulsos)

| Toma | De (s) | A (s) | Dura | Voz que le toca (inicio real) | Margen del corte sobre la voz |
|---|---|---|---|---|---|
| 1 Mando | 0,0 | 1,0 | 1,0 | línea 1, Tan (0,00) | la voz empieza en el fotograma 0 |
| 2 Tan con el mando | 1,0 | 2,0 | 1,0 | línea 1, sigue (acaba en 1,93) | corte dentro de la línea 1 |
| 3 Hoja grande | 2,0 | 5,0 | 3,0 | línea 2, Tan (2,16; «how many…» 2,83) | 0,16 s antes |
| 4 Dato 1, los dos | 5,0 | 9,0 | 4,0 | línea 3, Tin (5,35) | 0,35 s antes |
| 5 Tira, 13 × 365 | 9,0 | 11,0 | 2,0 | línea 4, Tin (9,06) | 0,06 s antes |
| 6 4,745 | 11,0 | 13,5 | 2,5 | línea 4, segundo tramo (11,13) | 0,13 s antes |
| 7 +3 leap days | 13,5 | 15,0 | 1,5 | línea 5, Tin (13,87) | 0,37 s antes |
| 8 4,748 | 15,0 | 17,5 | 2,5 | línea 5, segundo tramo (15,26) | 0,26 s antes |
| 9 +63 days, hoja | 17,5 | 21,0 | 3,5 | línea 6, Tin (17,77) | 0,27 s antes |
| 10 4,811 (revelación) | 21,0 | 23,5 | 2,5 | línea 7, Tin (21,38; «eight hundred…» 22,23) | 0,38 s antes |
| 11 Tan se asombra | 23,5 | 25,5 | 2,0 | línea 8, Tan (23,79; «that long?» 24,40) | 0,29 s antes |
| 12 Remate, age 13 | 25,5 | 27,5 | 2,0 | línea 9, Tin (25,50) | **0,00 s: sin margen** |
| 13 Mando, bucle | 27,5 | 28,5 | 1,0 | sin voz (la voz acaba en 27,33) | — |

Silencio de voz en el empalme del bucle: 1,17 s (límite 2 s). Duración 28,5 s (límite 30 s).

## Controles y resultado

| Control | Herramienta | Resultado |
|---|---|---|
| Formato | `codigo/comprobar_video.py` (ffprobe) | 1080x1920, 30 fps, H.264, yuv420p, AAC 48 kHz, 855 fotogramas, 28,500 s: **cumple** |
| Tramos de voz | `armar_dialogo.py` (`silencedetect` −35 dB, 0,25 s) | Tan 5 de 5 esperados, Tin 9 de 9: **coincide** |
| Rejilla y contadores | `render.py` (`comprobaciones`) | 12 cortes en múltiplos de 0,5 s; los 4 contadores solo suben y acaban en 4,745 / 4,748 / 63 / 4,811: **cumple** |
| Glifos | `render.py` (`comprobar_glifos`) | `+ , 0-9 ? × A G N S T a d e g h l m n o p s v w y` están en Inter Display Medium; sin «≈» ni «→»: **cumple** |
| Texto en zona segura | `render.py` (ancho y alto de cada fila, con su pop) | las 12 filas dentro de x 100–980, y ≥ 250; ninguna se tuvo que reducir: **cumple** |
| Dibujo en zona segura | medida de la caja de todo lo que no es papel, 1 de cada 3 fotogramas | tomas 2 a 11: dentro. **Fuera:** tomas 1 y 13 (mando) y toma 12 (ver defectos 1 y 2) |
| Cortes en el archivo | `comprobar_video.py` | 9 de 12 cortes se ven como salto grande en su fotograma; los de 11,0, 13,5 y 15,0 son cambios pequeños (ver defecto 4) |
| Imagen congelada, vacíos, destellos | `herramientas/revisar_fotogramas.py` → `fotogramas/revision.md` | «Sin marcas» (tras añadir el rebote al pulso; antes marcaba 5,4–8,7, 18,8–19,8 y 23,7–25,3) |
| Tramos sin cambio | `comprobar_video.py` | ninguno de 0,5 s o más; mitad de abajo nunca vacía |
| Bucle | `render.py` y `comprobar_video.py` | el fotograma 855 se dibuja con la misma función que el 0 (idénticos); la toma 13 llevada a t = 28,5 difiere del fotograma 0 en media 0,017 de 255 (máximo 73 en píxeles sueltos de borde, por redondeo del ángulo); en el archivo, del fotograma 854 al 0 hay 2,9 de 255, igual que entre dos fotogramas vecinos de la toma 13 (2,3): **empalma** |
| Color | `herramientas/revisar_color.py` → `revisar_color.txt` | ≈ 93 % dentro de la paleta (mínimo 85 %); saturación ≈ 17 %, luminosidad ≈ 89 %; variación entre segundos ±2 %: **cumple** |
| Contrastes | `revisar_color.py --contraste` | tinta/papel 12,6:1 (pasa 7:1); tomate/papel 3,6:1 (no pasa 4,5:1: por eso «4,811» y «13» llevan trazo de tinta de 0,06 em, como dice el prompt); mostaza/papel 1,6:1 (ídem) |
| Acento por plano | hojas de contacto, plano por plano | mostaza: clave + un elemento en las tomas 1–9 y 13; tomate solo en la 10 («4,811» al llegar) y la 12 («13» y bloque 13); toma 11 sin acento: **cumple** (ver duda 7) |
| Texto | `herramientas/revisar_texto.py` sobre `subtitulos.srt`, `codigo/render.py` y `codigo/miniatura.py`, `--idioma en` → `revisar_texto.txt` | 44 textos, **PASA: 0 errores** |
| Texto, lectura a mano en las hojas | `analisis/hoja_01..03.jpg` | «GTA 5?», «how many days?», «Sep 17, 2013», «Nov 19, 2026», «GTA 5», «13 × 365», «4,745 days», «+3 leap days», «4,748 days», «+63 days», «Sep 17, 2026», «GTA 6», «4,811 days», «age 13», «17»: igual que la tabla de §12; sin nombres propios en minúscula; cifras enteras |
| Sonoridad | `codigo/audio.py` y `comprobar_video.py` (ebur128) | mezcla.wav −14,0 LUFS, pico real −1,3 dBTP; el AAC del archivo −14,0 LUFS y −1,3 dBTP: **cumple** (−14 ±1, techo −1) |
| Niveles por pista | `05_audio/medidas_audio.json` | voz −14,7 LUFS; golpes bajo la voz −26,0 LUFS; golpes del arranque y el cierre con pico de −6 dBFS; música −24,0 LUFS; hizo falta limitador en la mezcla final (pico antes: −0,9 dBTP) |
| Golpes en su tiempo | `audio.py --verificar` | 47 de 47 empiezan a menos de 12 ms de su segundo |
| Rockstar / Take-Two | hojas de contacto | nada: ni logotipo ni tipografía; el mando no lleva símbolos (ver duda 6) |
| Prompt | `herramientas/validar_prompt.py` | 13 tomas, 28,5 s, «Listo para generar», 0 errores |
| Short 1 sigue igual | `render_v2.py --fotograma` 0, 150, 450, 600 y 800, antes y después de tocar `palitos.py` | los 5 PNG son idénticos byte a byte |

## No se pudo comprobar (hace falta oído)

1. Que cada tramo de voz diga lo que se supone. En particular: línea 7, que el tramo de 0,76 s sea «Four thousand,»;
   línea 9, que «now» no esté cortada (el archivo de Tin acaba en 25,60 s con la voz todavía en −24 dB, sin cola de
   silencio); y que «G T A» suene letra por letra.
2. Pronunciación, acento y naturalidad de las pausas acortadas a 0,15 s («So, | how many…», «Wow, | that long?»,
   y los dos puntos de las líneas 4 y 5). En la línea 5 la pausa quedó tan corta que `silencedetect` ya no la ve.
3. Que los golpes se oigan bajo la voz a −26 LUFS y que la música a −24 LUFS no tape la voz.
4. Que el limitador de la mezcla final no se note (actúa sobre picos de voz más música, unos 0,5 dB).
5. Que el golpe grave del fotograma 0 no ensucie la primera sílaba de Tan.
6. Clics o respiraciones en los empalmes (cada tramo lleva fundidos de 8 ms, pero no se oyó).

## Defectos y dudas (con el segundo)

1. **0,0–1,0 y 27,5–28,5 (mando):** el mando sale de la zona segura. A escala 100 % ocupa x 108–972 y con el
   balanceo llega a 95–983; con el empuje a 106 % que pide el prompt llega a x 74–1005 (hacia 0,3–1,0 s y
   27,5–27,8 s). No es texto, pero la empuñadura derecha queda donde YouTube pone sus botones. Arreglo gratis si se
   decide: mando de 800 px o empuje menor (cambia la medida del prompt, por eso no se tocó).
2. **25,5–27,5 (toma 12):** la esquina del calendario de la mano de Tin llega a x ≈ 986 con el rebote (unos 6 px
   fuera de la zona segura). Con Tin en x = 70 % y el brazo arriba no cabe más adentro sin tapar la visera (se probó).
   Además, en la salida de cada texto (3 fotogramas, mientras se desvanece) el texto sube 2 % como pide §12 y su tope
   pasa de y = 250 (llega a ≈ 239 px): es la animación de salida, no el texto quieto.
3. **Cortes que pisan el final de la línea anterior** (consecuencia de «ningún corte llega tarde» con 0,23 s entre
   líneas): 5,0 (faltan 0,12 s de «six?»), 13,5 (0,14 s de «days.»), 17,5 (0,04 s de «forty-eight.») y 21,0 (0,15 s
   de «nineteenth.»). Y el corte de **25,5** coincide con el inicio de la línea 9 (25,50): cero margen, el borrón
   ocupa de 25,43 a 25,57.
4. **11,0, 13,5 y 15,0:** tres cortes seguidos sobre la misma tira con Tan debajo: solo cambian la pose de Tan, el
   texto y un detalle de la tira. Se leen como cambio de pose más que como corte (así está en el prompt).
5. **1,0:** el corte cae dentro de la línea 1 (hacia «G T A»); por la envolvente «at midnight?» empieza hacia 1,4–1,5,
   así que Tan aparece 0,4 s antes de decirlo. La alternativa (corte en 1,5) dejaba la toma 2 en 0,5 s.
6. **Mando:** dos palancas en diagonal y cuatro botones en rombo, como pide §5. No lleva logotipos ni símbolos, pero
   esa disposición es la habitual de los mandos modernos: que lo mire el director creativo.
7. **Tomas 10 y 12:** Tan conserva la bufanda mostaza y la risa de los dos lleva la lengua tomate de su expresión
   (identidad, no acento); en la toma 12 el calendario de la mano va con cabecera marrón. Es lo previsto en el prompt.
8. **21,0–23,5 (toma 10):** la zona de gráficos queda vacía a propósito (el pico es la cifra); el «4,811» en tomate se
   ve 0,6 s (de 22,8 a 23,4) y llega unos 0,1–0,3 s antes de que la voz termine de decirlo.
9. **20,2–20,9:** «GTA 6» está 0,7 s en pantalla; es corto para leerlo con calma.
10. **Portada:** en el video el «GTA 5?» va en y = 15 % (288 px), por encima de la zona útil de portada de Shorts
    (y 380–1440). `06_final/portada_short02.png` lo baja y lo agranda (x 114–850, y 484–686). La alternativa
    (`portada_short02_alternativa.png`, fotograma de 23,0 s) **adelanta la respuesta** y su texto queda en y ≈ 290.
    `DESIGN.md` pide en portada mayúscula inicial y hasta 4 palabras: «GTA 5?» lo cumple.
11. **Loudness de la voz:** `dialogo_110.mp3` mide −14,7 LUFS (el `loudnorm` de una pasada no clava −14); la mezcla
    completa sí queda en −14,0.

## Decisiones tomadas al renderizar (distintas del prompt original; ya están anotadas en el prompt)

- Toma 2: Tan a `alto` 44 % (no 34 %): a 34 % el mando de la mano medía 130 px.
- Hoja de la zona de gráficos: 385 px de alto (27 % a 48,5 % con la pila), no 460: tocaba el rodete y la gorra.
- Tomas con personajes y cámara (2, 3, 4, 9, 10, 11): la toma empieza más abierta y **termina** en el encuadre del
  diseño; así el empuje se ve igual y nada sale de la zona segura. Toma 9: empuje de 4 % (no 2 %) y, en las tomas
  largas, mitad muelle `sello` y mitad ease in-out, para que no se congele.
- Rebote de los personajes al pulso (crecen hasta 2,2 % desde los pies cada 0,5 s; Tin a contratiempo): sin él
  `revisar_fotogramas.py` marcaba imagen congelada en las tomas 4, 9 y 11.
- «GTA 5» se queda toda la toma 4 (5,1–8,9) en vez de salir a los 1,3 s.
- Los contadores empiezan 2 fotogramas antes que su texto: nunca se ve «0 days» ni «+0 days».
- El botón del mando late a papel (no a tomate), como dicen §5 y §14.
- Golpes del arranque y del cierre (sin voz encima) a pico de −6 dBFS en vez de llevar la pista de efectos a
  −18 LUFS: casi todo el video tiene voz.
- Los gráficos `hoja_calendario` y `tira_13` quedaron en `codigo/render.py`; `mando()` está en `palitos.py` porque lo
  usa también el objeto de mano `control`.

## Falta

- Escucha completa (diseñador de sonido) y firmas del supervisor de continuidad y del director creativo.
- `03_keyframes/definicion.md` (entrada de «pieza por código» de `generacion.md`), `consumo.md`, el caso y la nota
  en `COORDINACION.md`: no se tocaron en esta vuelta.
