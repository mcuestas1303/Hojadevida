# Revisión, vuelta 1 — short 2 de Tin & Tan («How Many Days Did We Wait for GTA 6?»)

Fecha: 2026-11-21. Pieza: `06_final/tin_y_tan_short02_v1.mp4` (no se sube al repositorio; se rehace con
`python3 codigo/render.py`, unos 90 s). Todo lo de aquí se comprobó **con medidas y mirando las hojas de contacto**.
**Nadie ha escuchado ni la voz ni la mezcla**: lo que depende del oído está en «No se pudo comprobar».

## Ajustes pedidos por la coordinación tras ver las hojas (2026-11-21, mismo archivo de salida, vuelto a renderizar)

1. **«4,811 days»:** el contador va de 21,4 a **22,5** (antes 22,8): llega mientras la voz dice «eight hundred eleven»
   (segundo tramo desde 22,23). El texto, en tomate con trazo de tinta, **se queda toda la toma 11** y sale en 25,4
   (antes 23,4): la cifra final en tomate se ve 2,9 s (antes 0,6 s). La toma 11 pasa a tener acento tomate (único).
   El ding suena en 22,5.
2. **«GTA 6»:** de 19,4 a 20,9 (1,5 s; antes 0,7 s). «+63 days» sale en 19,3 (antes 20,1). La vuelta de hoja se
   adelanta a 19,4–19,7 (antes 19,9–20,2): «Sep 17, 2026» de 18,6 a 19,4 y «Nov 19, 2026» de 19,7 a 21,0. Por la
   envolvente de la voz, «to November…» empieza hacia 19,6 (hay un valle en 19,58); **sin escucha no es seguro**.
3. **Tan en la toma 5:** expresión `curiosidad` en vez de `concentrado` (se leía como enojo). Visto a tamaño
   completo (fotograma 300): ya no se lee enojada. Era el único plano con `concentrado`.
4. **Mando (tomas 1 y 13):** 800 px de ancho (antes 864), con el mismo empuje a 106 %. Medido en todos los fotogramas
   de las dos tomas: x de 109 a 971 (zona segura 100–980). El bucle sigue empalmando. Portada rehecha.

Las tablas de abajo ya tienen los valores de este render.

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
| Dibujo en zona segura | medida de la caja de todo lo que no es papel | tomas 1 a 11 y 13: dentro (mando: x 109–971). **Fuera:** toma 12, 6 px (ver defecto 2) |
| Cortes en el archivo | `comprobar_video.py` | 9 de 12 cortes se ven como salto grande en su fotograma; los de 11,0, 13,5 y 15,0 son cambios pequeños (ver defecto 4) |
| Imagen congelada, vacíos, destellos | `herramientas/revisar_fotogramas.py` → `fotogramas/revision.md` | «Sin marcas» (tras añadir el rebote al pulso; antes marcaba 5,4–8,7, 18,8–19,8 y 23,7–25,3) |
| Tramos sin cambio | `comprobar_video.py` | ninguno de 0,5 s o más; mitad de abajo nunca vacía |
| Bucle | `render.py` y `comprobar_video.py` | el fotograma 855 se dibuja con la misma función que el 0 (idénticos); la toma 13 llevada a t = 28,5 difiere del fotograma 0 en media 0,020 de 255 (máximo 76 en píxeles sueltos de borde, por redondeo del ángulo); en el archivo, del fotograma 854 al 0 hay 2,5 de 255, igual que entre dos fotogramas vecinos de la toma 13 (2,0): **empalma** |
| Color | `herramientas/revisar_color.py` → `revisar_color.txt` | ≈ 93 % dentro de la paleta (mínimo 85 %); saturación ≈ 17 %, luminosidad ≈ 89 %; variación entre segundos ±2 %: **cumple** |
| Contrastes | `revisar_color.py --contraste` | tinta/papel 12,6:1 (pasa 7:1); tomate/papel 3,6:1 (no pasa 4,5:1: por eso «4,811» y «13» llevan trazo de tinta de 0,06 em, como dice el prompt); mostaza/papel 1,6:1 (ídem) |
| Acento por plano | hojas de contacto, plano por plano | mostaza: clave + un elemento en las tomas 1–9 y 13; tomate solo en la 10 y la 11 («4,811», desde que llega) y la 12 («13» y bloque 13): **cumple** (ver duda 7) |
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

1. **0,0–1,0 y 27,5–28,5 (mando): CORREGIDO.** Con 864 px salía de la zona segura (x 74–1005 con el empuje); ahora
   mide 800 px y queda en x 109–971 en todos los fotogramas.
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
7. **Tomas 10, 11 y 12:** Tan conserva la bufanda mostaza y la risa de los dos lleva la lengua tomate de su expresión
   (identidad, no acento); en la toma 12 el calendario de la mano va con cabecera marrón. Es lo previsto en el prompt.
8. **21,0–23,5 (toma 10):** la zona de gráficos queda vacía a propósito (el pico es la cifra). **CORREGIDO** lo corto
   de la cifra: el «4,811» en tomate va de 22,5 a 25,4. Llega 0,27 s después de que empiece «eight hundred eleven
   days.» (22,23) y antes de que la voz termine de decir la cifra: si eso se siente adelantado, se oye, no se mide.
9. **19,4–20,9:** «GTA 6» ya dura 1,5 s (**CORREGIDO**). Duda nueva: entra en 19,4, cuando la hoja empieza a pasar,
   unos 0,2 s antes de «to November…» según la envolvente; y «Sep 17, 2026» queda 0,8 s en la hoja (18,6–19,4).
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
- Mando de 800 px (no 864) y Tan con `curiosidad` en la toma 5 (no `concentrado`); «4,811 days» sigue en la toma 11.
- Los gráficos `hoja_calendario` y `tira_13` quedaron en `codigo/render.py`; `mando()` está en `palitos.py` porque lo
  usa también el objeto de mano `control`.

## Falta

- Escucha completa (diseñador de sonido) y firmas del supervisor de continuidad y del director creativo.
- `03_keyframes/definicion.md` (entrada de «pieza por código» de `generacion.md`), `consumo.md`, el caso y la nota
  en `COORDINACION.md`: no se tocaron en esta vuelta.

## Tercer render (2026-11-23): defectos del supervisor de continuidad y del diseñador de sonido

Mismo archivo de salida (`06_final/tin_y_tan_short02_v1.mp4`, 28,5 s, 855 fotogramas, cortes sin cambios). Informes:
`firma_supervisor.md` y `firma_sonido.md`. **Las secciones de arriba describen los dos primeros renders; donde digan
otra cosa, vale esta.** Sigue sin escucharlo nadie.

### Bloqueantes

| # | Defecto | Qué se hizo | Medida o evidencia |
|---|---|---|---|
| 1 | `.srt` con «G T A five / six» (0,00–5,12 s) | Líneas 1 y 2: «GTA 5» y «GTA 6». Revisado todo el archivo con el criterio «lo que se lee»: la línea 4 pasa de «Thirteen years times 365» a «13 years times 365» (como «13 × 365» en pantalla). Tiempos sin cambios | `revisar_texto.py`: 0 errores |
| 2 | Portada dentro del video (0,0–0,9 y 27,6–28,5 s): «GTA 5?» en y ≈ 288–380 | El texto de las tomas 1 y 13 va al 12 % del alto con el tope en y = 26 %: **el fotograma 0 es la portada**. `codigo/miniatura.py` ya no dibuja nada propio: guarda el fotograma 0 y comprueba la caja | Texto en x 116–848, y 492–682 (franja 400–700; zona útil 380–1440). Hueco con el mando en todo el balanceo y el empuje: 97 px como mínimo. Bucle: 2,5 de 255 entre el fotograma 854 y el 0 (vecinos de la toma 13: 2,2) |
| 3 | Dígitos clave deformados por el trazo | La causa no era el orden (Pillow ya pinta el trazo y encima el relleno): en Inter Display Medium las aberturas del 6, el 9, el 3 y el 5 son más estrechas que el trazo y se llenaban de tinta. Se probó abrir un canal dentro de las bahías (quedaban restos blancos: descartado). Solución: **dígitos abiertos de la propia Inter** (rasgo OpenType `ss01`) en todas las cifras del video y trazo de **0,045 em** (antes 0,06) | Recortes ampliados de «5», «6», «63», «4,734», «4,811», «13» mostaza, «13» tomate, «3» y «days»: sin línea interior; el 6 y el 9 quedan con el trazo recto y abierto. Queda una muesca de tinta corta en el cuello del «5» grande de la portada (es el fondo de su abertura) |
| 4 | «Xbox» y «Rockstar» fuera del glosario | Añadidos a `video-studio/glosario.txt` con su porqué. «PlayStation» y «Take-Two» no hicieron falta (el filtro no los marca) | `revisar_texto.py` sobre la descripción de §8 (`vuelta_01/descripcion_s8.txt`): 0 errores |

### Convienen

| # | Defecto | Qué se hizo | Medida o evidencia |
|---|---|---|---|
| 5 | Tan con `pensando` de 15,0 a 21,0 s | Toma 7 (13,5–15,0): `feliz`. Toma 8 (15,0–17,5): `curiosidad` y, al llegar el contador (16,7), `feliz`. Toma 9 (17,5–21,0): `curiosidad` y, cuando la hoja pasa a «Nov 19, 2026» (19,4), `nostalgia`. Ya no hay `pensando` ni `concentrado` en el video | Caras a tamaño completo en 1,5 · 6,7 · 10,0 · 12,0 · 14,3 · 15,7 · 17,3 · 18,7 · 20,0 · 24,7 s: ninguna se lee como enojo. `curiosidad` (una ceja arriba, boca ladeada) se lee escéptica; sale en 9,0–11,0, 15,0–16,7 y 17,5–19,4 |
| 6 y 7 | Palanca derecha fuera del cuerpo; disposición del mando | `mando()` de `palitos.py`: las dos palancas a la misma altura, en (−0,26 W, +0,04 W) y (+0,03 W, +0,04 W). También cambia el mando de la mano de Tan (toma 2). Fichas de Tin y Tan y §5 del prompt actualizados | Borde inferior de las palancas en +0,11 W (el cuerpo llega a +0,20 W): ya no cortan el contorno. Visto en el fotograma 0 |
| 9 | Desfase entre la llegada del número, el `pop` y el sonido | `pop`, cambio a tomate y ding atados al primer fotograma en que el contador muestra el valor final. Toma 10: llega en **22,53 s** (fotograma 676) y ahí van el tomate, el `pop` y el ding; el tictac calla al llegar. Toma 8: el contador se estiró para llegar a 4,748 en **16,70 s** (cuando la voz dice «forty-eight»), con el `pop` en ese fotograma y el tercer tic en 16,68 | `render.t_llegada` y `audio.LLEGA_4811` dan el mismo valor (22,533); 48 de 48 golpes en su tiempo |
| 10 | El lápiz de Tin no salía | **Decisión:** Tin lleva su lápiz en la toma 4 (5,0–9,0) en lugar del calendario de mano. Por qué: es el motivo del canal y el prompt y la dirección decían que estaba; el calendario de la mano repetía la hoja que ya está encima. Para no romper «un acento por plano», el lápiz es el elemento mostaza de la toma 4 y la cabecera de la hoja pasa a marrón (neutro). La goma tomate del lápiz es parte del objeto, como en el short 1. El calendario de mano queda solo en la toma 12 | Prompt (§2, toma 4, §11, tabla de acento) y `direccion.md` (lista de elementos de acento) actualizados |
| 11 | Toma 4 casi quieta 4 s | La hoja está en blanco de 5,0 a 6,6 y **en 6,6 s** (cuando la voz dice «September seventeenth») entra «Sep 17, 2013» con `pop` y un sonido; Tin sacude el lápiz 9 grados y Tan pasa de `nostalgia` a `feliz` | `revisar_fotogramas.py`: sin marcas |
| Sonido | Fundido final de «now» | `armar_dialogo.py`: de 0,12 a 0,20 s; `dialogo_110.mp3` rehecho; la línea de tiempo no cambia | `revisar_voz.py` sobre el mp4: 75 palabras, 0 diferencias |
| Herramienta | Falso «posible final cortado» sobre una mezcla | `revisar_voz.py`: opción `--voz-sola`; el aviso solo sale con ella. Sin ella, si el audio no acaba en silencio, lo dice y explica que en una mezcla no se puede saber | Probado sobre el mp4: ya no sale el aviso |

### Menores

| # | Defecto | Qué se hizo |
|---|---|---|
| 13 | Toma 12 (25,5–27,5): dibujo hasta x = 989 y calendario pegado a la visera | El latido del bloque 13 crece hacia la izquierda; Tin va 14 px a la izquierda de x = 70 % solo en esa toma y el calendario 0,04 R más afuera. Medido en todos los fotogramas: x de 102 a 978 |
| 16 | «13 x 365» en la descripción | «13 × 365» en §8 del prompt |
| 17 | `licencias.md`: «(ID …)» | «(ID del trabajo de generación …)» en las dos voces |
| 19 | Salida de texto hasta y = 239 | La subida de salida se limita para que el tope no pase de y = 250. Caja de dibujo de **todos** los fotogramas sin borrón: x 100–980, y 256–1662: todo dentro de la zona segura |

### Controles sobre el archivo nuevo

| Control | Resultado |
|---|---|
| `comprobar_video.py` | 1080x1920, 30 fps, H.264, yuv420p, AAC, 855 fotogramas; sin tramos de 0,5 s sin cambio; sin vacíos; −14,0 LUFS y −1,3 dBTP; bucle 2,5 de 255. Los cortes de 11,0, 13,5 y 15,0 siguen siendo cambios pequeños |
| `analizar_video.py --cada 0.5` y hojas miradas | Sin texto cortado ni encimado; portada grande en las tomas 1 y 13; lápiz y cabecera marrón en la toma 4; «4,811 days» en tomate en las tomas 10 y 11 |
| `revisar_fotogramas.py` | Sin marcas |
| `revisar_color.py` | Video ≈ 93 % en paleta, ±2 % entre segundos; portada ≈ 95 % |
| `revisar_texto.py` (`subtitulos.srt`, `render.py`, `miniatura.py`, descripción) | 53 textos, PASA: 0 errores |
| `revisar_voz.py` sobre el mp4 con el guion completo (`revisar_voz_mp4.md`) | COINCIDE: 75 palabras, 0 diferencias |
| `revisar_titulo.py` con `--proyecto` y `--descripcion` (`revisar_titulo.txt`) | PASA: 0 errores, 0 avisos |
| `validar_prompt.py` | «Listo para generar», 0 errores |
| Short 1 | Fotogramas 0, 150, 450, 600 y 800 de `render_v2.py`: idénticos byte a byte a los de antes de tocar `palitos.py` |

### No se arregló (no es de código, o no es de este render)

- **8. Portada sin caras:** el fotograma 0 es el mando con «GTA 5?», como pide el prompt. Aceptarlo por escrito o cambiarlo es del director creativo.
- **12. `direccion.md`** con secciones en plantilla: es de cada director.
- **14.** Tan «señala» en horizontal y la tira está arriba (9,0–11,0): la pose `senala` es así; no hay pose que señale hacia arriba.
- **15.** El brazo por detrás de la bufanda en `explica` y `piensa`: fallo conocido de la ficha de Tan (dibujo del personaje).
- **18.** Fichas contra dibujo (cinta del rodete, cejas de Tin en `eureka`): no es de este video.
- **Ficha y prompt no coinciden en la cabecera del calendario de mano:** las fichas dicen tomate y el prompt marrón; se dibujó marrón y quedó anotado en las fichas.
- **Lo que solo se resuelve al oído** (salvedades del diseñador de sonido): «now», el ataque de «eight» en 22,23 s, «G T A» y las cifras, las pausas acortadas y el golpe del fotograma 0. Además, que «GTA 6» (19,4) y la hoja de noviembre no se adelanten a «to November…».
- **Cortes** que pisan el final de la línea anterior (5,0, 13,5, 17,5 y 21,0) y el de 25,5 sin margen: siguen igual, vienen de la rejilla.
- **Portada alternativa** (`portada_short02_alternativa.png`): adelanta la respuesta.

## Cuarto render (2026-11-23): la portada cumple la regla del dueño punto por punto

Mismo archivo de salida (28,5 s, 855 fotogramas, cortes sin cambios). El supervisor firmó todo menos la portada (faltaba
el punto 5 de `ENTREGA_YOUTUBE.md`, «Portada de los Shorts»). **Donde las secciones de arriba digan otra cosa sobre las
tomas 1 y 13, vale esta.**

### Qué cambió

1. **Tomas 1 y 13 (0,0–1,0 y 27,5–28,5 s):** el plano es la portada. El mando baja a 600 px de ancho con centro en
   y = 910; debajo, Tan (x = 30 %) y Tin (x = 70 %) de cuerpo entero y de perfil, mirando hacia el centro, donde está el
   mando, con `sorpresa` (Tan) y `curiosidad` (Tin); `alto` 487 px, pies en el suelo (y = 1651). Todo está completo en
   el fotograma 0. Movimiento desde el fotograma 0: el mando retumba, el botón late y los dos rebotan al pulso. Se
   quitó el empuje de cámara de estas dos tomas (escala 100 %), para que las medidas valgan todo el segundo.
2. **«GTA 6» (toma 9):** entra en 19,5 s y sale al corte de 21,0 (1,5 s). La vuelta de hoja se adelantó a 19,25–19,55:
   la hoja deja de decir «Sep 17, 2026» en 19,40 y la nueva, con «Nov 19, 2026», sube de 19,40 a 19,55. «+63 days»
   sale en 19,4. «Sep 17, 2026» queda 0,65 s en la hoja (18,6–19,25).
3. **`DESIGN.md` del canal:** norma nueva de cifras (dígitos abiertos `ss01` y contorno de 0,045 em), con su porqué y
   la nota de que el short 1 quedó con los dígitos por defecto.

### Regla de portada sobre el fotograma 0 (medido en píxeles por `codigo/miniatura.py`)

| # | Regla | Medida | Resultado |
|---|---|---|---|
| 1 | Los primeros 0,5 a 1 s son la portada y el video sigue sin corte brusco | El plano dura de 0,0 a 1,0 s con la misma composición; las cajas medidas en los 26 fotogramas de 0,0 a 0,87 s (con balanceo y rebote): texto y 482–682, mando y 728–1092, caras y 1133–1357. Primer corte en 1,0 s | cumple |
| 2 | `miniatura.png` vertical de 1080×1920 | `06_final/portada_short02.png`, 1080×1920, 138 KB: es el fotograma 0 tal cual | cumple (el nombre `miniatura.png` lo pone la entrega) |
| 3 | Zona útil x 60–960, y 380–1440: fuera, solo fondo o cuerpos | Texto x 116–848, y 492–682. Cara de Tan (cabeza y rodete) x 242–405, y 1175–1355. Cara de Tin (cabeza y gorra con visera) x 624–837, y 1142–1356. Fuera de la zona útil solo quedan las piernas (hasta y = 1662) y la línea de suelo | cumple |
| 4 | Texto: máximo 4 palabras en 2 líneas, entre y 400 y 700, letra de 120 px o más, mayúscula inicial, clave en el amarillo del canal, sin la respuesta, sin copiar el título | «GTA 5?»: 2 palabras, 1 línea, y 492–682, letra de 230 px, «GTA» en mayúsculas por ser sigla, «5» en mostaza con contorno; no lleva 4,811 ni «days»; el título es «How Many Days Did We Wait for GTA 6?» | cumple |
| 5 | Objeto en el centro (y 720–1100); caras de Tin y Tan en la zona útil, con curiosidad o sorpresa, mirando el objeto | Mando x 239–840 (centrado en x = 540), y 744–1075. Tan con `sorpresa`, Tin con `curiosidad`, los dos de perfil hacia el centro (`mira=1` y `mira=-1`) | cumple, **con una salvedad**: la mirada de perfil es horizontal, hacia el centro del cuadro, y el mando está encima de sus cabezas; `palitos.py` no tiene mirada hacia arriba salvo `pensando`, que se descartó porque se lee como molestia |
| 6 | El video cumple lo que promete la portada | La portada pregunta por GTA 5 y el video cuenta los días desde GTA 5 hasta GTA 6 | cumple (juicio del director creativo) |

Además: nada tapa el texto ni el mando (hueco mínimo texto–mando 46 px y mando–cabezas 47 px en todo el segundo); todo
dentro de la zona segura del video (caja de dibujo de todos los fotogramas sin borrón: x 100–980, y 256–1662); mostaza
solo en el «5» y el mando (bufanda, gorra y cabezas son identidad). Bucle: del fotograma 854 al 0 hay 1,7 de 255 (entre
vecinos de la toma 13: 1,5).

### Controles sobre el archivo nuevo

| Control | Resultado |
|---|---|
| `comprobar_video.py` | formato correcto; sin tramos de 0,5 s sin cambio; sin vacíos; −14,0 LUFS y −1,3 dBTP; bucle 1,7 de 255. Los cortes de 11,0, 13,5 y 15,0 siguen siendo cambios pequeños |
| `analizar_video.py --cada 0.5` y hojas miradas | portada con mando y los dos personajes en 0,25, 0,75, 27,75 y 28,25 s; «GTA 6» ya con la hoja de noviembre; sin texto cortado ni encimado |
| `revisar_fotogramas.py` | sin marcas |
| `revisar_color.py` | video ≈ 93 % en paleta, luminosidad ±2 %, saturación ±1 %; portada ≈ 94 % (`revisar_color_portada.txt`) |
| `revisar_texto.py` (srt, `render.py`, `miniatura.py`, descripción) | 53 textos, PASA: 0 errores |
| `revisar_voz.py` sobre el mp4, guion completo | COINCIDE: 75 palabras, 0 diferencias |
| `validar_prompt.py` | «Listo para generar», 0 errores |
| Golpes | 48 de 48 en su tiempo |
| Short 1 | fotogramas 0, 150, 450, 600 y 800 idénticos byte a byte |

### No se pudo

- **Mirada hacia arriba:** ver la salvedad del punto 5. Arreglarlo pide una expresión o una vista nueva en `palitos.py`
  (cambio de diseño de los personajes: pasa por su bitácora, no se hizo aquí).
- **Caras chicas:** con el mando en y 720–1100 y las caras por debajo, sin salir de la zona útil ni de la zona segura,
  la cabeza mide 176 px de diámetro (R = 88 px); en el resto del video mide 236 px.
- **«GTA 6» y la voz:** la hoja pasa a noviembre en 19,40 s y «to November…» empieza hacia 19,6 s según la envolvente:
  unos 0,2 s antes de oírlo. Solo se confirma al oído.
- Sigue en pie todo lo de «No se arregló» del tercer render, salvo la portada sin caras.
