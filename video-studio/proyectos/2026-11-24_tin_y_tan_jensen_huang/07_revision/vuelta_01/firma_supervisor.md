# Firma del supervisor de continuidad — short 3 de Tin & Tan, vuelta 1

- **Fecha:** 2026-11-24.
- **Pieza revisada:** `06_final/tin_y_tan_short03_v1.mp4` (archivo del 2026-11-24 02:19; 1080×1920, 30 fps, H.264, yuv420p, AAC 48 kHz, 930 fotogramas, 31,0 s), `06_final/portada_short03.png` y la carpeta `08_entrega/TIN-EN-S-003/` (`video.mp4` recomprimido a 2,92 MB, `miniatura.png`, los dos `.srt`, `ficha.json`).
- **Cómo se revisó:** de cero, sin copiar `notas.md`. Hojas propias a 2 fotogramas por segundo (las cuatro vistas); los 930 fotogramas extraídos del archivo final y los 930 de la entrega; fotogramas 0 a 14 y 894 a 929 uno por uno (firma del lápiz); ampliaciones de la suelta (f912–f919), de las caras de la portada y de frente, del calendario (5,83 · 10,67 · 11,50 · 11,93 · 12,83 s), de las barras (14,40 · 18,67 · 21,33 · 22,07 · 23,33 · 26,33 s), de los cortes de 3,5 · 6,5 y 30,0 s y del pase del lápiz; portada reducida al 25 %; caja de dibujo y hueco subtítulo–cabeza medidos en los fotogramas; cuentas rehechas con `datetime` y `calendar`. Evidencias en `07_revision/vuelta_01/supervisor/`.
- **No revisado por mí:** control 3 (no oigo: nadie ha escuchado la voz ni la mezcla); los hechos de noviembre de 2026 sobre Jensen Huang en una fuente externa (siguen siendo los de Wikipedia leídos por el equipo el 2026-11-24; el comunicado de Nvidia no se abrió); la redacción de la sección 3b (es del director de fotografía y no existe: `direccion.md` está entera en plantilla).

## Veredicto general

**RECHAZADO (`CAMBIOS`).** Firmo 2 (Cifras, con salvedad), 7 (Marca) y 8 (Color, solo la medición). No firmo 1 (Texto en el video), 4 (Imagen), 4.5 (Portada, falta una decisión escrita), 5 (Video) ni el punto 2 de la lista de la firma del lápiz. Todo lo que bloquea se arregla por código: 0 créditos, un render de ≈ 160 s. **La voz no se toca.** Nada de esto está publicado: el código `TIN-EN-S-003` no figura en `registro_codigos.md`.

## Tabla por control

| Control | Qué miré | Evidencia | Resultado | Firma |
|---|---|---|---|---|
| 1. Texto | `revisar_texto.py` sobre `ficha.json`, los dos `subtitulos.srt` (prompt y entrega, idénticos entre sí), `textos_pantalla_en.txt`, `render.py` y `miniatura.py` (`--idioma en`); los dos `subtitulos_es.srt` y `textos_pantalla_es.txt` (`--idioma es`); lectura a mano de cada texto en la imagen | Inglés: 87 textos, **0 errores, 0 avisos**. Español: 34 textos, **0 errores, 0 avisos**. Leído en pantalla: «Back In / 11 Days?», «11 days?», «Nov 12», «Nov 17», «+6 days», «Nov 23», «11 days», «12,274 days», «5 days», contador «2,754 / 3,241 / 4,243 days», «4,382 days», «11 days», «Who else?», «Subscribe». Tarjetas: «¿Fue rápido el regreso / de Jensen Huang?», «Renunció a Nvidia / tras un escándalo.», «La junta dijo que no / lo repondría.», «Lo repuso como CEO.», «Antes: más de 33 / años al mando.», «¿Rápido comparado / con quién?», «Sam Altman, OpenAI:», «Steve Jobs, Apple:», «¿Son 12 años?», «Más rápido que Jobs. / Más lento que Altman.», «¿Quién más volvió?», «Suscríbete al próximo / conteo.». Sin faltas, tildes y «¿» correctos, sin cuadros, dígitos `ss01` limpios, ningún nombre propio en minúscula («Tin & Tan» en descripción y etiquetas). Descripción de `ficha.json` idéntica a la de §8 del prompt (comparada carácter por carácter; 1.448 bytes). **Falla la legibilidad (punto 1.7):** defectos 2, 3 y 6 | **NO PASA** (ortografía pasa; lo que falla es que el texto toca al personaje y lo que el hispanohablante pierde) | **NO FIRMADO** |
| 2. Cifras | Recalculé todo; comparé voz (guion y transcripción), pantalla, los dos `.srt`, descripción y ficha técnica; contador fotograma a fotograma con `tiempos.contador` | 12-nov → 23-nov-2026 = **11**; 17 → 23 = **6**; 5-abr-1993 → 12-nov-2026 = **12.274** (33,6 años: «more than 33» correcto); Altman 17 → 22-nov-2023 = **5**; Jobs 17-sep-1985 → 16-sep-1997 = **4.382** (≈ 11,9975 años; ≈ 398 veces 11). Noviembre de 2026: el 1 es domingo, el 12 jueves, el 17 martes, el 23 lunes: coincide con la hoja dibujada. Cruces: 13 y 14, 15 a 21, 22 y 23 = **11**. Contador: solo sube, máximo 4.382, llega en f662 (22,07 s = 71,2 %). La misma cifra en voz, pantalla, `.srt` EN («eleven», «thirty-three», «five», «four thousand, three hundred eighty-two»), `.srt` ES (11, 33, 5, 4.382 con punto), descripción (12,274 y 4,382 con coma, 5, 6, 11, «≈ 12 years») y ficha técnica §4. Coma de miles correcta para EE. UU. | **PASA CON SALVEDAD** (defecto 7: «twelve years» / «12 años» sin palabra de aproximación) | **FIRMADO** |
| 4. Imagen | Tin y Tan contra sus fichas; lados y `espejo`; objetos; zona segura en los 930 fotogramas; terceros | Colores, rodete, bufanda con dos puntas, gorra con botón y dos costuras, lentes con brillo, manos de punto, zapatos: iguales en las 14 tomas. Tan a la izquierda y Tin a la derecha en todos los planos de dos. Ningún logotipo, cara, tipografía ni color de terceros: silla, mesa, calendario y barras son dibujo propio sin letras; nada verde de Nvidia. Zona segura: nada fuera por arriba ni por la derecha; **toma 3 (f105–f194) la silla de primer plano llega a x = 6** (zona desde 100) y a y = 1673. **Fallan:** defectos 1, 2, 4 y 5 | **NO PASA** | **NO FIRMADO** |
| 4.5 Portada | Fotograma 0 y `portada_short03.png` (= `miniatura.png`, mismo archivo), regla punto por punto | Tabla de abajo | **PASA CON SALVEDAD en lo medido; falta una decisión escrita** | **NO FIRMADO** |
| 5. Video | `ffprobe`, `revisar_fotogramas.py`, `postpro.py destellos` (final y entrega), hojas, diferencia entre fotogramas, tiempos de `.srt` contra `linea_de_tiempo.json` | Formato correcto en los dos archivos (930 fotogramas a paso fijo). «Sin marcas»: ni congelados ni vacíos. 0 destellos en los dos. Bucle: f929 contra f0 = 0,79 de 255 (vecinos: 0,29 y 0,25): un paso de vuelo, empalma; en la entrega 1,34. Entrega contra final: 1,0 de 255 (compresión). Los 11 tiempos de los `.srt` son los de la línea de tiempo (+0,05 s de cola). −14,0 LUFS y −1,0 dB de pico medidos por mí en los dos archivos (es medida, no escucha). **No firmo:** el punto 5.4 exige 1 y 3 sobre el archivo final y hay que renderizar otra vez; además defecto 8 | **PASA en lo técnico; pendiente del nuevo render** | **NO FIRMADO** |
| Firma del lápiz (`FIRMA_LAPIZ_BUMERAN.md` §11) | Los 10 puntos, en fotogramas | Tabla de abajo | **NO PASA** (punto 2) | **NO FIRMADO** |
| 7. Marca | Paleta, tipografía, capitalización, lados, motivos contra `DESIGN.md`; solo este Short y su portada | Solo colores de la paleta más el blanco del calendario. Inter Display Medium, rótulos en minúscula a la izquierda con «Nov» en mayúscula; portada con mayúscula inicial. Dígitos `ss01` con contorno. Lápiz de Tin presente (tomas 3 a 5, 7, 9, 12, 13). Sin degradados en formas | **PASA** | **FIRMADO** |
| 8. Color (medición) | `revisar_color.py` sobre video final, portada y video de entrega; `--contraste` de cada par; acento plano por plano | Video ≈ 93 % en paleta, saturación ≈ 16 %, luminosidad ≈ 89 %, ±1 % entre segundos. Portada ≈ 93 %. Entrega ≈ 93 %. Tinta/papel 12,6:1 (subtítulos y rótulos; pasa 7:1); tinta/blanco 14,5:1; tinta/mostaza 8,0:1; tinta/tomate 3,5:1; mostaza/papel 1,6:1; tomate/papel 3,6:1: toda clave en mostaza o tomate lleva contorno de tinta. Acento: coincide con la tabla del prompt en las 14 tomas; tomate solo en 22,07–24,4 s y Tin sin lápiz en la toma 10 | **PASA CON SALVEDAD**: tinta/tomate 3,5:1 (se lee por contorno y tamaño); **el punto 8.1 no se cumple**: la sección 3b de `direccion.md` no existe y falta la firma del director de fotografía | **FIRMADO** (solo la medición) |

## Portada, punto por punto (`ENTREGA_YOUTUBE.md`)

| # | Regla | Lo que medí o vi | Resultado |
|---|---|---|---|
| 1 | Primeros 0,5 a 1 s = portada | Misma composición de f0 a f29; el texto sale en 0,9 s; el lápiz se mueve desde f0 | cumple |
| 2 | 1080×1920 | 1080×1920, 1,26 MB; contra f0: 1,5 de 255 | cumple |
| 3 | Zona útil x 60–960, y 380–1440 | Texto x 105–608, y 416–693. Cabeza de Tan x 114–329, y 1194–1379. Cabeza de Tin **x 745–962**: 2 px del contorno de la gorra fuera (la misma salvedad aceptada en el short 2) | cumple con salvedad |
| 4 | Hasta 4 palabras en 2 líneas, y 400–700, letra de unos 120 px, mayúscula inicial, clave en amarillo, sin la respuesta ni el número | 4 palabras, 2 líneas, «11» en mostaza. **Mayúscula de 98 px de alto** (cuerpo 134 px; en el short 2 eran ≈ 190 px): al 25 % se lee, pero es la mitad de grande. La cifra a la vista está decidida y razonada (prompt §3.7, `PARAMETROS.md`) | cumple con salvedad |
| 5 | Objeto en y 720–1100; caras con curiosidad o sorpresa mirando el objeto | Silla x 348–731, y 715–1111 con su sombra; hueco texto–silla **22 px**. Tin: boca en «o» y ojo grande: sorpresa, se lee. **Tan: ver punto 1 de «Lo que se pidió mirar con lupa»** | **pendiente de decisión** |
| 6 | El video cumple lo que promete | Pregunta por los 11 días y el video los compara | cumple |

`portada_medidas.txt` da el lápiz en x 520–649 (130 px, 12 %): mide solo parte del cuerpo. Con punta y goma es **x 484–674, y 1221–1271 (190 px, ≈ 18 %)**; a la cabeza de Tin quedan 71 px (no 103) y a la silla 110 px (no 124). Sigue despejado, pero las cifras de `notas.md` están mal: corregir la medida en `codigo/miniatura.py`.

## Firma del lápiz bumerán (§11 de la especificación)

| # | Punto | Lo que vi | Resultado |
|---|---|---|---|
| 1 | Empalme | f929 → f0: un paso (0,79 de 255); mismas caras, texto y fondo; `comprobar_firma`: 5,4 y 4,7 px/f, 4,4 y 4,0 °/f | cumple |
| 2 | Despejes: 0 px a las caras | **No cumple.** f915 (30,50 s): la goma del lápiz tapa la boca de Tan; f916: cruza la mejilla y roza el ojo; f917: tapa la zona entre ojo y ceja. ≈ 40 px dentro de la cabeza durante 3 fotogramas. En la atrapada (f10) el extremo de abajo pisa el contorno de la mejilla. El «48 px a las caras» de `render.log` **no mide estos fotogramas**: `efectos._despejes` los excluye a propósito («junto a la mano no se mide») | **NO PASA** |
| 3 | Fotograma 0 | Lápiz entero y nítido, ≈ 18 % del ancho, texto entero, silla completa, dos caras | cumple |
| 4 | Anticipación | f906–f911: el brazo baja y va atrás, lápiz junto a la cadera | cumple |
| 5 | Suelta | f915; un solo lápiz en cada fotograma; Tin sin lápiz | cumple |
| 6–7 | Giro, velocidad, escala | 330°, 24,9 °/f y 66 px/f máximos, escala 1,7 (según `render.log`; a la vista, sin saltos) | cumple |
| 8 | Atrapada | Contacto en f10, retroceso del brazo y asiento hasta f14 | cumple |
| 9 | Cámara y seguridad | Fija; 0 destellos | cumple |
| 10 | Sonido | Voz en f14 y fin en 30,05 s (c = −28); atrapada medida en 0,33 s. Picos del chasquido y del whoosh de ida −16,8 dBFS (la especificación pide −20). **No oído** | pendiente del oído |

En f4 a f7 el obturador pinta 6 copias separadas y el lápiz se ve como un abanico, no como un borrón: 4 fotogramas, no bloquea.

## Lo que se pidió mirar con lupa

1. **Cejas de Tan en la portada.** No se lee enfado: la ceja es un trazo corto, alto y lejos del ojo, que sube hacia el frente (lo contrario del ceño). Lo que sí pasa es que **tampoco se lee curiosidad**: boca de raya recta, sin sonrisa ni boca abierta; al 25 % Tan queda seria o escéptica. La regla pide «curiosidad o sorpresa» y en el short 2 se firmó con ceja levantada y sonrisa abierta. De frente (`curiosidad`, 1,0–3,5 · 6,5–9,0 · 14,5–16,0 · 19,0–22,0 · 27,0–30,0 s) pasa igual: una ceja más alta, boca de raya inclinada: duda, no enojo. No lo rechazo por enfado; lo dejo como decisión del director de animación: o lo acepta por escrito como «duda» o pone `sorpresa` a Tan en `plano_firma` (`codigo/render.py`, `expresion="curiosidad"`), que también es la cara del empalme.
2. **Barras de 11 y de 5 días.** No se entiende. En la toma 9 (16,3–19,0 s) son dos rayas verticales del mismo tamaño, una encima de otra: se leen como una línea partida, no como barras, y nada dice cuál es Huang y cuál Altman. Solo cobran sentido cuando crece la barra de Jobs (20,9 s), y aun entonces siguen sin nombre. La marca mostaza al final de la barra de 12.274 (toma 7) parece un remate de la barra: nadie la lee como «11 días» y la voz no la nombra. El mensaje grueso (dos motas contra una barra enorme) llega; quién es quién, no.
3. **Calendario.** Los números miden ≈ 20 px de alto: en un teléfono no se leen; la fecha la da el rótulo, y eso basta. **La flecha no se lee como flecha:** es un trazo de ≈ 45 px que nace entre el 16 y el 17 y muere dentro del círculo del 23 (las dos celdas son vecinas en diagonal); parece la cola del círculo. El 17 no lleva marca, así que «+6 days» no tiene origen a la vista. Además el círculo del 12 de la toma 3 **ya no está** en las tomas 5 y 6, y las cruces tapan los números del 13 al 23, incluidos el 17 y el 23.
4. **Lápiz en vuelo.** Apertura: se lee como un lápiz que va hacia Tan y ella lo atrapa (colgado y horizontal en f0, con la punta hacia ella; llega a la mano en f8–f10). Que «vuelve» solo se entiende en la segunda pasada del bucle, como prevé la especificación. Cierre: se lee como lanzado (brazo atrás, barrido, el lápiz sube girando y queda colgado). Falla lo del punto 2 de la tabla: sale por delante de la cara.
5. **Tarjetas en español.** Ortografía y sentido correctos, y cada una coincide con su línea de voz. Lo que pierde quien no lee inglés: (a) la palabra «días» no aparece nunca en español: todas las cifras dependen de «days»; (b) «12,274» y «4,382» con coma se leen como decimales en español, y la tarjeta «Steve Jobs, Apple:» ya se fue (20,48 s) cuando llega la cifra (20,88 s); lo salva «¿Son 12 años?»; (c) «el 17», «seis días después» y «5 días» quedan solo en inglés. La razón dada («no cabe») no vale para cuatro tarjetas: «El 17, la junta dijo / que no lo repondría.» (20 y 20 caracteres), «Seis días después, / lo repuso como CEO.» (18 y 19), «Sam Altman, OpenAI: / 5 días.» y «Steve Jobs, Apple: / 4.382 días.» caben en dos renglones de 21. La tarjeta 10 va a ≈ 20 caracteres por segundo (2,05 s): justa.
6. **Cortes de 6,5, 9,0 y 16,0 s.** Caen 0,05, 0,10 y 0,12 s (1,5 a 3,6 fotogramas) antes del final medido de la línea: la cola de «scandal», «back» y «who?» suena sobre el plano siguiente. En imagen no deja nada raro (las tarjetas 3 y 6 salen antes del corte). Es un solape corto de sonido sobre el corte, habitual; si molesta solo lo dice el oído. **Pendiente de escucha**, no lo doy por bueno ni lo marco como defecto.

## Preguntas fijas (cap. 11, regla 20)

| Pregunta | Respuesta | Evidencia |
|---|---|---|
| ¿Movimiento y corte antes del segundo 1? | Movimiento **sí**; corte **no** | El lápiz se mueve desde f0; el primer corte cae en 1,0 s justo |
| ¿Plano héroe cerca de la mitad? | **No** | Pico en 22,07 s (71,2 %); en la mitad (15,5 s) está Tan sola |
| ¿Picos y respiros? | **Sí** | Respiros en 3,5–9,0 y 24,5–27,0; pico en 20,9–22,5 |
| ¿Final que empalma con el inicio? | **Sí** | 0,79 de 255 entre f929 y f0 |
| ¿Cada corte con su sonido? | **Sin comprobar por mí** | `audio_verificar.txt`: 38 golpes, 0 fuera de tiempo; oírlo es del diseñador de sonido |
| ¿Algo genérico? | **No** | Todo dibujo propio |
| ¿Más de 3 destellos por segundo? | **No** | 0 |
| ¿Todo con licencia? | **Sí** | `licencias.md` cubre tipografía, dibujo, voces, música, efectos y mención nominativa (ver menor 14) |

## Defectos

### Bloquean (todos a 0 créditos)

1. **30,50–30,57 s (f915–f917): el lápiz pasa por delante de la cara de Tan** (boca, mejilla y ojo). Dónde: `herramientas/efectos.py`, punto de mano `H` de `geometria_firma` (`_B1_PRUEBA[0]`) y ángulos del brazo en la suelta y la atrapada de `lapiz_bumeran`: la mano tiene que soltar y recibir a ≥ 0,5 R más lejos del centro de la cabeza (H ≈ x de Tan + 1,6 R), de modo que el lápiz entero, con goma, quede fuera del círculo de la cabeza en c = −15 a −13 y en f8 a f10. Y quitar en `_despejes` (línea ≈ 1151) la exclusión de los fotogramas junto a la mano, para que `comprobar_firma` lo mida. `GEO = fx.geometria_firma(PORTADA_GEO, subir=-10.0)` en `codigo/render.py` no mueve la mano: no alcanza con tocar eso.
2. **15,0–15,97 s (toma 8, 23 fotogramas): la «q» de «con quién?» toca el rodete de Tan** (hueco de 1 a 2 px) y el panel del subtítulo vela la parte de arriba del rodete. El panel vela también el rodete y el botón de la gorra en las tarjetas de dos renglones de las tomas 7 y 12 (13,0–14,3 y 24,7–26,8 s). En las tomas 2, 3, 4 y 6 el hueco es de 17 a 18 px. Dónde: `codigo/render.py`, `capa_subtitulos` (subir el bloque de dos renglones ≈ 14 px o recortar el `+ 18` del alto del panel) o `ALTO_PJ` de 540 a ≈ 520. Criterio de paso: ≥ 12 px entre cualquier letra o el panel y la cabeza en los 930 fotogramas.
3. **Barras sin nombre (16,3–27,0 s).** Poner el nombre junto a cada marca, en tinta y pequeño, fuera de la barra: «Huang 11», «Altman 5», «Jobs» (y «11 days» junto a la marca mostaza de la toma 7, o quitar esa marca). Dónde: `_barras` y `marca_minima` en `codigo/render.py`, más las filas nuevas en la tabla de rótulos de §12 del prompt (hoy «todo texto en pantalla es el de las tablas»). Separar las dos marcas de la toma 9 lo bastante para que no parezcan una línea partida (`BARRA_SEP`). Si el director creativo prefiere dejarlas mudas, que lo escriba con su porqué en «Decisiones del equipo»; sin eso no firmo.

### Convienen

4. **9,3–12,0 s, flecha del 17 al 23:** marcar el 17 (círculo de tinta) y alargar la flecha por fuera de las celdas, o quitarla. Dónde: `_marcas_zona` (`fx.trazo_flecha(...)`) en `codigo/render.py`.
5. **Continuidad del calendario:** el círculo del 12 desaparece entre la toma 3 y las tomas 5 y 6. Dibujarlo en tinta en `_marcas_zona` (así no suma un segundo acento) para que las 11 cruces tengan de dónde salir.
6. **Tarjetas 3, 4, 7 y 8 con la cifra en español** (textos del punto 5 de arriba). Dónde: `SUBTITULOS` en `codigo/tiempos.py` y la tabla de tarjetas de §12; la 8 se alarga hasta 22,5 s. Repetir `revisar_texto.py --idioma es`.
7. **«That is twelve years?» / «¿Son 12 años?»:** son 4.382 días = 12 años menos un día; la descripción dice «≈ 12 years» y la voz y las tarjetas no llevan palabra de aproximación (control 2.2). En español cuesta 0: «¿Casi 12 años?» en la tarjeta 9 (`SUBTITULOS`) y en `subtitulos_es.srt`. La voz y el `.srt` en inglés no se pueden cambiar sin regenerar: **no lo recomiendo**; que el director creativo lo acepte por escrito.
8. **12,0–13,0 s (toma 6):** el rótulo «11 days» y el calendario salen mientras la voz y la tarjeta dicen «Before that: more than thirty-three years in charge» / «Antes: más de 33 años al mando». Viene de la voz real (la línea 5 empieza en 11,97 y no en 13,23): dos datos distintos a la vez durante 1 s. Arreglo: retrasar la tarjeta 5 a 13,0 s o llevar el corte 6 → 7 a 12,5 s (`CORTES` y `SUBTITULOS` en `codigo/tiempos.py`).
9. **Expresiones frente al contenido (línea editorial, la decide el director creativo):** Tin sonríe con rubor (`feliz`) mientras dice «He resigned… after a scandal» (3,7–6,5 s) y Tan celebra con los brazos arriba (`celebra` + `eureka`) cuando la voz dice que lo repusieron (10,3–12,0 s). El prompt pide que nada se lea como burla ni como juicio: una sonrisa sobre la renuncia y un festejo de la reposición son las dos cosas. Alternativa sin dibujo nuevo: `curiosidad` para Tin en `toma_3` y `sorpresa` + `senala` para Tan en `toma_5`.
10. **Tin con `curiosidad` en la toma 4 (6,5–9,0 s):** una ceja baja bajo la visera y boca de raya: serio, no enojado. No bloquea.

### Menores

11. **Toma 3 (3,5–6,5 s):** la silla de primer plano llega a x = 6 (zona segura desde 100). Es objeto, no texto ni cara, y cae donde tapa la interfaz. Dónde: `toma_3`, posición de `capa_silla`.
12. **Portada:** gorra de Tin 2 px fuera de x = 960; mayúsculas de 98 px; 22 px entre «Days?» y la silla. Si hay render, `X_PORTADA` a (0,24 W; 0,75 W).
13. **Fichas contra dibujo (no es de este video):** la cinta mostaza del rodete no se ve; Tin sin cejas en `eureka` (22,1 s).
14. **Documentos sin poner al día:** `ficha_tecnica.md` (estado «falta el render», «Tin atrapa el lápiz en el fotograma 15», tomate «de 23,05 a 24,5 s», pico «en 23,05 s», color «Medido: pendiente»); `perfil_emocional.md` (23,05 s, 75,6 % y 30,5 s en 13 líneas; lo real es 22,07 s, 71,2 % y 31,0 s); `direccion.md` entera en plantilla; `licencias.md` dice `palitos.py` 1.4 y `efectos.py` 1.1 y el prompt 1.3; `TIN-EN-S-003` sin anotar en `registro_codigos.md`; no existe `07_revision/controles.md`.
15. **Firma, sonido:** chasquido y whoosh de ida a −16,8 dBFS contra −20 de la especificación: lo decide el diseñador de sonido.

## Pendiente del oído humano (no lo doy por bueno)

- Pronunciación de «Nvidia», «Huang», «OpenAI» y «C E O»; la cola de «Altman»; la pausa alargada con silencio digital tras «Apple:» (medí 0,36 s de silencio total en 20,23–20,59 s).
- Si los golpes se oyen bajo la voz; el whoosh y el golpe de la firma; que el whoosh no tenga hueco en el empalme; la música.
- Los tres cortes del punto 6.
- `revisar_voz.py` da 87 palabras y 0 diferencias: dice que se entiende, no cómo suena.

## Título

`revisar_titulo.py "Jensen Huang Is Back as Nvidia CEO After 11 Days" --canal tin-y-tan --idioma en --formato short --frase "jensen huang is back" --marca "Jensen Huang" --marca "Nvidia" --descripcion … --proyecto …`: **PASA, 0 errores, 0 avisos.** Falta la revisión humana del director creativo (`revision_humana` en `ficha.json` sigue en `null`).

## Firmas

| Control | Firma |
|---|---|
| 1. Texto | **NO FIRMADO** (ortografía en 0 errores; defectos 2, 3 y 6) |
| 2. Cifras | **FIRMADO** (con salvedad: defecto 7) |
| 4. Imagen | **NO FIRMADO** (defectos 1, 2 y 3) |
| 4.5 Portada | **NO FIRMADO** (falta la decisión escrita sobre la cara de Tan) |
| 5. Video | **NO FIRMADO** (lo técnico pasa; pendiente del nuevo render y del control 3) |
| Firma del lápiz, §11 | **NO FIRMADO** (punto 2) |
| 7. Marca del canal | **FIRMADO** |
| 8. Color | **FIRMADO** (solo la medición; falta la sección 3b y la firma del director de fotografía) |

Supervisor de continuidad, 2026-11-24. Veredicto general: `CAMBIOS` (RECHAZADO).
