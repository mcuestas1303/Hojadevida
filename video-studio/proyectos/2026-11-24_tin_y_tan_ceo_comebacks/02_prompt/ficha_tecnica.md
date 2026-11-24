# Ficha técnica — CEO Comebacks Ranked: Jensen Huang vs. Steve Jobs

Resumen de una página del video. El detalle de cada bloque está en el archivo que se cita. Escrita el 2026-11-24 con el prompt versión 1 (tiempos estimados: la voz y el render no existen). Cumple la promesa de cierre del short 3 («Who else came back? Subscribe for the next count.»). La apertura y el cierre siguen la firma del canal (`canales/nostalgia-tin-y-tan/FIRMA_LAPIZ_BUMERAN.md`): Tan atrapa el lápiz en el fotograma 10 y lo lanza al final; la voz entra en el fotograma 14.

## 1. Objetivos comerciales

**Fijado por el dueño el 2026-11-23, para todos los canales:** entrar al Programa de socios de YouTube a la mayor brevedad posible. Textual: «Entonces el objetivo inicial es entrar al programa de socios; todo debe girar en torno a lograr el objetivo a la mayor brevedad posible».

| Umbral del Programa (fuente oficial, leída el 2026-11-20) | Antes del 1-feb-2027 | Desde el 1-feb-2027 |
|---|---|---|
| Suscriptores | 1.000 | 1.000 |
| Camino de Shorts | 10 millones de vistas de Shorts en 90 días | 20 millones en 90 días |
| Camino de video largo | 4.000 horas públicas en 12 meses | 8.000 horas en 365 días |

| Qué aporta este video al objetivo | Métrica | Meta de línea base |
|---|---|---|
| Vistas calificadas de Shorts (el tema tiene demanda hoy; el bucle no suma) | «Engaged views» de Studio a 7 y 28 días, frente a vistas totales | Línea base: es el primer ranking del canal y el cuarto video |
| Se quedó a mirar frente a deslizó | Visto frente a deslizado y retención por segundo | Superar el 20,7 % del short 1 y quedar a la par o por encima del short 3 (la portada de los dos nombra al sujeto) |
| **Suscriptores nuevos:** una pregunta nueva («¿cuánto duraron tras volver?») y una sola invitación de Tan | Suscriptores ganados desde este video, por cada mil vistas | Línea base (el short 1 dio 0); comparar con el short 3 (cierre «Who else came back?») |
| Compartidos (el ranking y «solo Altman fue más rápido que Huang») | Compartidos por cada mil vistas | Línea base (el short 1 dio 0) |
| Aprender si repetir el dato de Jobs resta o suma | Retención de 16 a 22 s frente al short 3 | No menor que la del short 3 en el mismo tramo |
| Aprender qué efectos retienen | Retención por tramo con efecto (tabla B de la sección 11 del prompt) | Un pico visible en 19,13 s |

## 2. Identificación

| Campo | Valor |
|---|---|
| Código | `TIN-EN-S-004` (por anotar en `registro_codigos.md` al entregar) |
| Canal | Tin & Tan, inglés, EE. UU. (con subtítulos en español quemados y pista `subtitulos_es.srt`) |
| Tipo | Short n.º 4 (primer ranking del canal; segundo con portada que nombra al sujeto; cumple la promesa del cierre del short 3) |
| Título | CEO Comebacks Ranked: Jensen Huang vs. Steve Jobs (49 caracteres; filtro de títulos 1.1: pasa, 0 errores y 0 avisos) |
| Objetivo comercial | Entrar al Programa de socios de YouTube lo antes posible (dueño, 2026-11-23; ver 1) |
| Público | Quien sigue la noticia de Huang o busca regresos de directores ejecutivos en EE. UU., sin edad fija (manda el dato de Studio); hispanohablantes con los subtítulos |
| Qué queremos que haga | Verlo entero, mandarlo y suscribirse para ver el siguiente conteo (permanencia tras volver) |
| Estado | Prompt escrito y validado; falta cotizar la voz y el sí del dueño para generarla, el render y la escucha. Fecha límite para publicar: lo antes posible, después del short 3 (la noticia es del 23 de noviembre y cada día pierde demanda) |

## 3. Formato

| Campo | Valor |
|---|---|
| Aspecto y tamaño | 9:16, 1080×1920 |
| Duración | 31,0 s estimados (930 fotogramas a 30 por segundo), en bucle (el vuelo del lápiz); pico en 19,13 s (61,7 %) |
| Cómo se hizo | Dibujado por código (`palitos.py` 1.4, `efectos.py` 1.1 y gráficos propios); sin generador de imagen ni de video |
| Archivo | `06_final/tin_y_tan_short04_v1.mp4` (por renderizar) |
| Portada | El fotograma 0: `06_final/portada_short04.png` (por guardar con `miniatura.py`) |
| Subtítulos | `02_prompt/subtitulos.srt` (inglés, 9 líneas) y `02_prompt/subtitulos_es.srt` (español, 9 líneas); además, 12 tarjetas en español quemadas en el video (banda de y 905 a 1085) |

## 4. Elenco

| Personaje | Papel | Voz | Objeto de mano |
|---|---|---|---|
| Tan | Abre con la pregunta, reacciona a cada dato, dice la pregunta final con la invitación; atrapa y lanza el lápiz | Zelda, al 110 % | lápiz (en el plano de firma y en las tomas 11 y 12) |
| Tin | Responde con un nombre y una barra por plano; va sin lápiz en el plano de firma | Kevin, al 110 % | lápiz (tomas 3 a 6, 9, 10 y 11) |

Ninguna de las seis personas de la lista aparece dibujada ni imitada ni se la cita: solo se las nombra.

## 5. Contenido: los hechos y las cuentas

Método único para todos: del día en que la persona deja el puesto de director ejecutivo al día en que vuelve a él; cuentas con `datetime` el 2026-11-24; fuentes: Wikipedia en inglés leída ese día (detalle en `00_brief.md`).

| Persona y empresa | Sale del puesto | Vuelve al puesto | Días | Matiz |
|---|---|---|---|---|
| Sam Altman, OpenAI | 2023-11-17 | 2023-11-22 | **5** | Destituido por la junta |
| Jensen Huang, Nvidia | 2026-11-12 | 2026-11-23 | **11** | Renunció; el comunicado de Nvidia no se abrió |
| Bob Iger, Disney | 2020-02-25 | 2022-11-20 | **999** | Presidente ejecutivo hasta fines de 2021 |
| Michael Dell, Dell | 2004-03-04 | 2007-01-31 | **1.063** | Siguió de presidente; una sola página como fuente |
| Jack Dorsey, Twitter | 2008-10-16 | 2015-07-01 | **2.449** (≈ 6,7 años) | Siguió de presidente; volvió como interino |
| Steve Jobs, Apple | 1985-09-17 | 1997-09-16 | **4.382** (≈ 12 años) | Salió de verdad; volvió antes en febrero de 1997 con la compra de NeXT |
| **Lo que se dice** | Solo Altman fue más rápido que Huang; los otros cuatro tardaron más | | | cálculo |

**Por qué el pico es Jobs:** el asombro es magnitud comparada con algo conocido y Jobs es la barra más larga de la lista. **Repite el dato del short 3:** riesgo declarado en el perfil emocional y medido (retención de 16 a 22 s). **Quedan fuera:** Howard Schultz (sin día de salida en las fuentes y tres etapas) y Larry Page (sin día de salida), pendientes de fecha para otro conteo.

No se dice: cómo ni por qué salió nadie, detalles de la vida privada, terceros, cifras de bolsa o fortuna, citas, que sean «todos» los regresos o «el más largo» o «el más rápido de la historia», quién lidera hoy las empresas ni predicciones. De cada empresa solo se dice el nombre: sin logotipo, letra de marca ni color.

## 6. Guion de voz (tiempos estimados)

| N.º | Quién | De–a (s) | Texto |
|---|---|---|---|
| 1 | Tan | 0,47–4,08 | Jensen Huang came back as C E O in eleven days. Who took longer? |
| 2 | Tin | 4,31–7,29 | Bob Iger at Disney: nine hundred ninety-nine days. |
| 3 | Tin | 7,52–10,43 | Michael Dell at Dell: one thousand, sixty-three days. |
| 4 | Tin | 10,66–14,43 | Jack Dorsey at Twitter: two thousand, four hundred forty-nine days. |
| 5 | Tan | 14,83–15,80 | Almost seven years? |
| 6 | Tin | 16,20–20,27 | Steve Jobs at Apple: four thousand, three hundred eighty-two days. |
| 7 | Tan | 20,87–21,84 | Almost twelve years? |
| 8 | Tin | 22,19–26,61 | Only Sam Altman was faster than Huang: five days. The other four took longer. |
| 9 | Tan | 26,96–30,19 | How long did they stay after coming back? Subscribe for the next count. |

Pregunta de apertura: línea 1. Pregunta de cierre: línea 9. Respuesta a la de apertura: línea 8.

## 7. Tomas

| N.º | Segundos | Qué se ve | Rótulo en inglés |
|---|---|---|---|
| 1 | 0,0–1,0 | Portada: silla de director vacía; el lápiz vuelve girando y Tan lo atrapa (f 10; firma del canal) | CEO Comebacks / Huang 11 Days / vs. Jobs? |
| 2 | 1,0–4,0 | Tan pregunta; fila de Huang (la vara) | 11 days |
| 3 | 4,0–7,5 | Fila de Iger | 999 days |
| 4 | 7,5–10,5 | Fila de Dell | 1,063 days |
| 5 | 10,5–14,5 | Fila de Dorsey | 2,449 days |
| 6 | 14,5–16,0 | Tan: «¿casi siete años?» | almost 7 years? |
| 7 | 16,0–20,5 | Pico: fila de Jobs, contador hasta 4.382, tomate y zoom | 4,382 days |
| 8 | 20,5–22,0 | Tan: «¿casi doce años?»; la cifra queda quieta | 4,382 days |
| 9 | 22,0–25,0 | Fila de Altman: el único más rápido que Huang | 5 days |
| 10 | 25,0–27,0 | Remate: los otros cuatro tardaron más | 4 took longer |
| 11 | 27,0–30,0 | Pregunta final, invitación; el lápiz pasa a Tan | How long? / Subscribe |
| 12 | 30,0–31,0 | Tan lanza el lápiz; vuelve el fotograma 0 | CEO Comebacks / Huang 11 Days / vs. Jobs? |

## 8. Perfil de colores

| Color | Hex | Dónde va | Para qué |
|---|---|---|---|
| Papel (neutro) | `#F3E9D2` | Fondo | Calidez de papel impreso |
| Tinta (neutro) | `#2B2420` | Líneas y texto, nombres de las filas | Lectura: contraste 12,6:1 |
| Mostaza (acento) | `#E8B33B` | La palabra clave y un elemento por plano (lápiz, marca de 8 px o barra en curso) | Lleva el ojo al dato |
| Tomate (excepción del pico) | `#C8553D` | Solo la cifra «4,382», de 19,13 a 21,95 s | Marca el pico |
| Marrón (relleno neutro) | `#7A4B2A` | Barras ya contadas, silla | Objeto, no acento |

Medido: pendiente del render (`revisar_color.py` sobre el video, el fotograma 0 y los cuadros del pico; piso 85 %). Ningún color de marca de terceros. Detalle: `prompt.md`, «Color con intención».

## 9. Animación, luz y velocidad

| Elemento | Qué hay |
|---|---|
| Animaciones | Silla que crece, lápiz bumerán, una fila de ranking por plano (barras a escala con nombre y marca mínima de 8 px), contador de 36 f, golpe de zoom de +10 % en el pico; cámara fija |
| Efectos de luz | Sin destellos ni negativo; desenfoque fijo del fondo, niebla, sombras, paso de mostaza a tomate; sin cambio de foco, sin revelado y sin paralaje |
| Velocidad del video | 12 tomas y 11 cortes; la toma más corta dura 1,0 s y la más larga 4,5 s |
| Velocidad del audio | Voz al 110 %; pausas internas acortadas, salvo 0,45 s tras «Apple:» y 0,60 s antes de la reacción de Tan tras el pico |

## 10. Sonido

| Elemento | Valor |
|---|---|
| Voces | Zelda (Tan) y Kevin (Tin), una generación cada una, **sin generar** (costo por cotizar; pide el sí del dueño) |
| Música | Por código, re menor a 120 BPM que pasa a re mayor en el pico (distinta de las de los shorts 2 y 3) |
| Efectos | Por código: whoosh con vibrato y golpe del lápiz, pop y deslizar de cada fila, tictac, subida, silencio de 12 fotogramas y ding en 19,13 s |
| Volumen | Por medir: objetivo −14,0 LUFS; golpes bajo la voz a unos −26 LUFS; sonidos de la firma a −20 dBFS |
| Guion contra lo que se oye | Por comprobar con `revisar_voz.py` sobre la mezcla |

## 11. Emoción buscada

| Tramo | Segundos | Emoción |
|---|---|---|
| Gancho | 0 a 4 | Curiosidad y orientación |
| Lista | 4 a 14,5 | Asombro creciente |
| Pico | 19,13 | Asombro |
| Respiro | 19,13 a 22 | Alivio breve |
| Remate y cierre | 22 a 31 | Sorpresa cerrada, curiosidad nueva y gratitud |

Elemento por elemento, con su fundamento, su métrica y su riesgo: `02_prompt/perfil_emocional.md` (17 filas, con «Cierre y bucle» y «Firma del canal»).

## 12. Publicación y medición

| Campo | Valor |
|---|---|
| Plataforma | YouTube Shorts primero; después TikTok e Instagram |
| Descripción | Las seis cuentas con sus fechas, el método único, los matices de cada salida, fuentes con fecha, aclaración de que no se abrieron los comunicados de las empresas, una línea de suscripción y el descargo de no afiliación |
| Categoría | 24 (Entertainment) o 25 (News and Politics): la decide el dueño al publicar; el equipo propone 24 |
| Hecho para niños | No |
| Qué se mide | Visto frente a deslizado, duración media vista, vistas calificadas del feed, compartidos, suscriptores, tráfico de búsqueda, vistas por idioma, retención de 16 a 22 s frente al short 3 |
| Metas | Superar el 20,7 % del short 1; línea base de compartidos y suscriptores |
| Entrega | `08_entrega/TIN-EN-S-004/` (por armar y pasar por `entrega.py`) |

## 13. Controles y firmas

La fila «Lo que el short 3 dejó resuelto» está en `prompt.md`, sección 14.

| Control | Resultado | Firma |
|---|---|---|
| Texto y ortografía | Descripción, etiquetas, `subtitulos.srt` y `subtitulos_es.srt`: 0 errores (2026-11-24); falta el texto del render | Por firmar (supervisor de continuidad) |
| Cifras | Recalculadas con Python; falta compararlas con voz, pantalla, `.srt` y descripción cuando exista el video | Por firmar |
| Imagen | Por revisar: silla y ranking genéricos, sin logotipo ni color de marca; los personajes contra su ficha; ninguna sonrisa en un dato de salida | Por firmar |
| Portada | Por medir en el fotograma 0 (texto y 400–700, silla y 720–1100, caras en la zona útil, hueco ≥ 30 px entre texto y silla) | Por firmar |
| Firma del lápiz | `comprobar_firma` y los 10 puntos de §11 | Por firmar |
| Video y bucle | `comprobar_destellos` con margen, `revisar_fotogramas.py`, fotograma 930 igual al 0 | Por firmar |
| Subtítulos en español | Por medir: banda de y 905 a 1085 sin tocar gráficos ni cabezas; líneas de 856 px o menos; tarjetas de 30 f o más | Por firmar |
| Marca del canal | Por revisar | Por firmar |
| Color | Por medir (piso 85 %; cuadros del pico por separado) | Por firmar (director de fotografía y supervisor) |
| Voz y audio | Por generar y oír | Por firmar (diseñador de sonido) |
| Título y línea editorial | Pasa el filtro; falta que el video cumpla lo que promete y que ninguna salida se cuente con motivo | Por firmar (director creativo) |
| Escucha de una persona | Pendiente | Dueño |

## 14. Costo

| Concepto | Costo |
|---|---|
| Voz de Tan | por cotizar con `estimate_audio_cost` |
| Voz de Tin | por cotizar con `estimate_audio_cost` |
| Imagen, video, música y efectos | 0 (por código) |
| **Total** | **por cotizar y por autorizar** (referencia por analogía con el short 3: 3,7 créditos) |

## 15. Pendientes

1. Cotizar la voz con `estimate_audio_cost` y pedir el sí del dueño; generar una sola vez cada voz.
2. Reajustar los tiempos de las secciones 6 y 7 y de los subtítulos con la voz real; comprobar que el pico siga entre el 60 y el 75 %; volver a validar y a archivar el prompt.
3. Programar el render (ranking, texto de portada, tarjetas; reutilizar silla, lápiz y banda de subtítulos del short 3), renderizar y correr los controles de la sección 13.
4. Medir el color con y sin efectos (cuadros de 17,9 a 22,0 s por separado y ΔE tomate–naranja).
5. **Compromiso del cierre:** preparar el conteo de permanencia tras volver (fechas ya leídas en `00_brief.md`: Jobs 5.090 días, Iger 1.214, Dorsey 2.343; Dell, Altman y Huang siguen) dentro de 7 días; si no sale, avisar en un comentario fijado.
6. Armar `08_entrega/TIN-EN-S-004/`, pasar `entrega.py` y anotar el código en `registro_codigos.md`; publicar solo con el sí del dueño.
