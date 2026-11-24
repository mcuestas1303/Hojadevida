# Ficha técnica — Jensen Huang Is Back as Nvidia CEO After 11 Days

Resumen de una página del video. El detalle de cada bloque está en el archivo que se cita. Escrita el 2026-11-24 con el prompt versión 2: **actualizada el 2026-11-24 con la voz real y el render 2 (vuelta 2): los tiempos de las secciones 2, 5 y 6 son los reales; el resto del contenido no cambió.** La apertura y el cierre siguen la firma del canal (`canales/nostalgia-tin-y-tan/FIRMA_LAPIZ_BUMERAN.md`): Tan lanza el lápiz al final y lo atrapa al principio; la voz entra en el fotograma 14. Sustituye a la ficha de la tarjeta de 1999 (descartada).

## 1. Identificación

| Campo | Valor |
|---|---|
| Código | `TIN-EN-S-003` |
| Canal | Tin & Tan, inglés, EE. UU. (con subtítulos en español quemados y pista `subtitulos_es.srt`) |
| Tipo | Short n.º 3 (primero de actualidad; primero con profundidad, efectos, pregunta final y firma del lápiz bumerán) |
| Título | Jensen Huang Is Back as Nvidia CEO After 11 Days (48 caracteres; filtro de títulos 1.1 flexible: pasa, 0 errores y 0 avisos) |
| Objetivo comercial | Entrar al Programa de socios de YouTube lo antes posible (dueño, 2026-11-23; ver 1b) |
| Público | Quien sigue la noticia en EE. UU., sin edad fija (manda el dato de Studio); hispanohablantes con los subtítulos |
| Qué queremos que haga | Verlo entero, mandarlo y suscribirse para ver el siguiente conteo |
| Estado | Prompt escrito y validado; falta el sí del dueño para la voz (por cotizar), el render y la escucha. Fecha límite para publicar: lo antes posible (la noticia es del 23 de noviembre y cada día pierde demanda) |

## 1b. Objetivos comerciales

**Fijado por el dueño el 2026-11-23:** entrar al Programa de socios de YouTube a la mayor brevedad posible. Textual: «Entonces el objetivo inicial es entrar al programa de socios; todo debe girar en torno a lograr el objetivo a la mayor brevedad posible».

| Umbral del Programa (fuente oficial, leída el 2026-11-20) | Antes del 1-feb-2027 | Desde el 1-feb-2027 |
|---|---|---|
| Suscriptores | 1.000 | 1.000 |
| Camino de Shorts | 10 millones de vistas de Shorts en 90 días | 20 millones en 90 días |
| Camino de video largo | 4.000 horas públicas en 12 meses | 8.000 horas en 365 días |

| Qué aporta este video al objetivo | Cómo se mide | Meta |
|---|---|---|
| Vistas calificadas de Shorts (el tema tiene demanda hoy; el bucle no suma) | «Engaged views» de Studio a 7 y 28 días, frente a vistas totales | Línea base (3.er video) |
| Se quedó a mirar frente a deslizó (cuatro de cada cinco deslizaron en el short 1) | Visto frente a deslizado, retención por segundo | Superar el 20,7 % del short 1 |
| **Suscriptores nuevos:** una pregunta nueva («¿quién más volvió?») y una sola invitación de Tan | Suscriptores ganados desde este video, por cada mil vistas | Línea base (el short 1 dio 0; comparar con un video de cierre sin pregunta) |
| Compartidos (la comparación con Jobs y Altman) | Compartidos por cada mil vistas | Línea base (el short 1 dio 0) |
| Aprender qué efectos y qué cierre retienen | Retención por tramo con efecto (tabla B de la sección 11 del prompt) | Un pico visible en 22,07 s |

## 2. Formato

| Campo | Valor |
|---|---|
| Aspecto y tamaño | 9:16, 1080×1920 |
| Duración | 31,0 s reales (930 fotogramas a 30 por segundo), en bucle (el vuelo del lápiz); pico en 22,07 s (71,2 %) |
| Cómo se hizo | Dibujado por código (`palitos.py` 1.4, `efectos.py` 1.1 y gráficos propios); sin generador de imagen ni de video. Render real: ≈ 160 s |
| Archivo | `06_final/tin_y_tan_short03_v1.mp4` (por renderizar) |
| Portada | El fotograma 0: `06_final/portada_short03.png` (por guardar con `miniatura.py`) |
| Subtítulos | `02_prompt/subtitulos.srt` (inglés, 11 líneas) y `02_prompt/subtitulos_es.srt` (español, 11 líneas); además, 12 tarjetas en español quemadas en el video (banda de y 905 a 1085) |

## 3. Elenco

| Personaje | Papel | Voz | Objeto de mano |
|---|---|---|---|
| Tan | Abre con la pregunta, hace las preguntas del público, dice la pregunta final con la invitación y lanza el lápiz | Zelda, al 110 % | lápiz (tomas 13 y 14) |
| Tin | Responde con datos; va sin lápiz en el plano de firma (lo lanza y lo atrapa Tan, en el fotograma 10) | Kevin, al 110 % | lápiz (tomas 1 a 9 y 12 a 13) |

Jensen Huang, Sam Altman y Steve Jobs no aparecen dibujados ni imitados ni se les cita: solo se les nombra.

## 4. Contenido: los hechos y las cuentas

| Dato | Valor | Fuente |
|---|---|---|
| Renuncia | 12 de noviembre de 2026 | Wikipedia en inglés, «Jensen Huang», leída el 2026-11-24; títulos de cadenas en YouTube |
| «No lo repondremos» | 17 de noviembre de 2026 (la junta) | Wikipedia, leída el 2026-11-24 |
| Reposición | 23 de noviembre de 2026, presidente y director ejecutivo, con efecto inmediato | Wikipedia y títulos de CNN, BBC, NBC, CBS, ABC y Fox News; **el comunicado de Nvidia no se pudo abrir** |
| Días fuera | 12 → 23 de noviembre = **11** | cálculo con `datetime` (2026-11-24) |
| Del «no» a la reposición | 17 → 23 = **6** | cálculo |
| Al mando antes | 5 abril 1993 → 12 nov 2026 = **12.274 días** (33,6 años) | Wikipedia, «Nvidia» (constitución); cálculo |
| Sam Altman, OpenAI | destituido 17 nov 2023, repuesto 22 nov 2023 = **5 días** | Wikipedia, «Removal of Sam Altman from OpenAI», leída el 2026-11-24 |
| Steve Jobs, Apple | carta de renuncia 17 sep 1985, nombrado director ejecutivo interino 16 sep 1997 = **4.382 días** (≈ 12 años; ≈ 398 veces los 11 días) | Wikipedia, «Steve Jobs», leída el 2026-11-24; cálculo. Volvió antes a Apple (febrero de 1997, compra de NeXT); un título del NYT es del 17 de sep de 1997 (un día de diferencia) |
| **Lo que se dice** | Más rápido que Jobs; más lento que Altman | cálculo |

**Por qué el pico es Jobs y no la proporción «1 día fuera por cada ≈ 1.116 al mando»:** el asombro es magnitud comparada con algo conocido, y Jobs es la referencia que el público ya usa para esta noticia; la proporción es abstracta. La proporción queda en reserva.

No se dice: el motivo de la renuncia más allá de «after a scandal» (una sola vez), detalles de la vida privada, terceros, investigaciones o comparecencias, el papel del gobierno, el motivo de la junta, cifras de bolsa o fortuna, citas, que «fue despedido», que sea «el regreso más corto», superlativos ni predicciones. Del fabricante solo se dice el nombre: sin logotipo, letra de marca ni su verde.

## 5. Guion de voz (tiempos reales, 05_audio/linea_de_tiempo_voz.md)

| N.º | Quién | De–a (s) | Texto |
|---|---|---|---|
| 1 | Tan | 0,47–3,46 | Was Jensen Huang's comeback in eleven days fast? |
| 2 | Tin | 3,69–6,55 | He resigned from Nvidia on November twelfth after a scandal. |
| 3 | Tin | 6,78–9,10 | On the seventeenth the board said it would not bring him back. |
| 4 | Tin | 9,33–11,74 | Six days later it reinstated him as C E O. |
| 5 | Tin | 11,97–14,23 | Before that: more than thirty-three years in charge. |
| 6 | Tan | 14,46–16,12 | Fast compared to who? |
| 7 | Tin | 16,35–18,77 | Sam Altman at OpenAI: five days. |
| 8 | Tin | 19,00–22,48 | Steve Jobs at Apple: four thousand, three hundred eighty-two days. |
| 9 | Tan | 22,71–24,49 | That is twelve years? |
| 10 | Tin | 24,72–26,73 | Faster than Jobs. Slower than Altman. |
| 11 | Tan | 26,96–30,05 | Who else came back? Subscribe for the next count. |

Pregunta de apertura: línea 1. Pregunta de cierre: línea 11. Respuesta a la de apertura: línea 10.

## 6. Tomas

| N.º | Segundos | Qué se ve | Rótulo en inglés |
|---|---|---|---|
| 1 | 0,0–1,0 | Portada: silla de director vacía; el lápiz vuelve girando y Tan lo atrapa (f 10; firma del canal) | Back In / 11 Days? |
| 2 | 1,0–3,5 | Tan pregunta; la silla, lejos | 11 days? |
| 3 | 3,5–6,5 | Los dos con el calendario de noviembre; círculo en el 12 | Nov 12 |
| 4 | 6,5–9,0 | Mesa de junta (revelado) con la silla a la cabecera | Nov 17 |
| 5 | 9,0–11,5 | Flecha del 17 al 23; círculo en el 23; 11 cruces | +6 days, Nov 23 |
| 6 | 11,5–12,5 | Las 11 cruces; Tan asiente | 11 days |
| 7 | 12,5–14,5 | Barra de 12.274 días con una marca de 11 | 12,274 days |
| 8 | 14,5–16,0 | Tan: «¿rápido comparado con quién?» | — |
| 9 | 16,0–19,0 | Barras: Huang 11 y Altman 5 | 5 days |
| 10 | 19,0–22,5 | Pico: barra de Jobs, contador hasta 4.382, tomate y zoom | 4,382 days |
| 11 | 22,5–24,5 | Tan se asombra; la cifra queda quieta | 4,382 days |
| 12 | 24,5–27,0 | Remate: más rápido que Jobs, más lento que Altman | 11 days |
| 13 | 27,0–30,0 | Pregunta final, invitación; el lápiz pasa a Tan | Who else? / Subscribe |
| 14 | 30,0–31,0 | Tan lanza el lápiz; vuelve el fotograma 0 | Back In / 11 Days? |

## 7. Perfil de colores

| Color | Hex | Dónde va | Para qué |
|---|---|---|---|
| Papel (neutro) | `#F3E9D2` | Fondo | Calidez de papel impreso |
| Tinta (neutro) | `#2B2420` | Líneas y texto | Lectura: contraste 12,6:1 |
| Mostaza (acento) | `#E8B33B` | La palabra clave y un elemento por plano (lápiz, círculo, marca o barra) | Lleva el ojo al dato |
| Tomate (excepción del pico) | `#C8553D` | Solo la cifra «4,382», de 22,07 a 24,4 s | Marca el pico |

Medido (render 2, `revisar_color.py`): ≈ 93 % dentro de la paleta en el video y en la portada, saturación ≈ 16 %, ±1 % entre segundos. Ningún verde de Nvidia. Detalle: `prompt.md`, «Color con intención».

## 8. Animación, luz y velocidad

| Elemento | Qué hay |
|---|---|
| Animaciones | Capas con paralaje y sombras de contacto, silla que crece, lápiz bumerán, garabatos, 11 cruces que caen, barras que crecen, revelado desde desenfoque, golpe de zoom de +10 % en el pico |
| Efectos de luz | Sin destellos ni negativo; desenfoque fijo del fondo, niebla, sombras, paso de mostaza a tomate; sin cambio de foco (no cabe en la rejilla) |
| Velocidad del video | 14 tomas y 13 cortes; la toma más corta dura 1,0 s y la más larga 4,0 s |
| Velocidad del audio | Voz al 110 %; pausas internas acortadas, salvo 0,45 s tras «Apple:» |

## 9. Sonido

| Elemento | Valor |
|---|---|
| Voces | Zelda (Tan) y Kevin (Tin), una generación cada una, **sin generar** (costo por cotizar; pide el sí del dueño) |
| Música | Por código, mi menor a 120 BPM que pasa a mi mayor en el pico (distinta de la del short 2, en do mayor) |
| Efectos | Por código: whoosh con vibrato y golpe del lápiz, raspado de garabatos, tictac, subida, silencio de 12 fotogramas y ding en 22,07 s |
| Volumen | Por medir: objetivo −14,0 LUFS; golpes bajo la voz a unos −26 LUFS |
| Guion contra lo que se oye | Por comprobar con `revisar_voz.py` sobre la mezcla |

## 10. Emoción buscada

| Tramo | Segundos | Emoción |
|---|---|---|
| Gancho | 0 a 2,5 | Curiosidad y orientación |
| Hechos | 2,5 a 13 | Tensión |
| Cuenta y comparación | 13 a 23 | Anticipación y asombro |
| Pico | 22,07 | Asombro |
| Remate y cierre | 24,5 a 31,0 | Sorpresa cerrada, curiosidad nueva y gratitud |

Elemento por elemento, con su fundamento, su métrica y su riesgo: `02_prompt/perfil_emocional.md` (17 filas, con «Cierre y bucle» y «Firma del canal»).

## 11. Publicación y medición

| Campo | Valor |
|---|---|
| Plataforma | YouTube Shorts primero; después TikTok e Instagram |
| Descripción | Cronología, comparaciones con el mismo método, fuentes con fecha, aclaración de que el comunicado oficial no se pudo abrir, una línea de suscripción y «Not affiliated with Nvidia. Jensen Huang is not involved in this video.» |
| Categoría | 24 (Entertainment) o 25 (News and Politics): la decide el dueño al publicar; el equipo propone 24, la que YouTube aceptó en el short 1 |
| Hecho para niños | No |
| Qué se mide | Visto frente a deslizado, duración media vista, vistas calificadas del feed, compartidos, suscriptores, tráfico de búsqueda, vistas por idioma |
| Metas | Superar el 20,7 % del short 1; línea base de compartidos y suscriptores |
| Entrega | `08_entrega/TIN-EN-S-003/` (pasa los controles del publicador) |

## 12. Controles y firmas

| Control | Resultado | Firma |
|---|---|---|
| Texto y ortografía | Descripción, etiquetas, `subtitulos.srt`, rótulos y `subtitulos_es.srt`: 0 errores (2026-11-24); falta el texto del render | Por firmar (supervisor de continuidad) |
| Cifras | Recalculadas con Python; falta compararlas con voz, pantalla, `.srt` y descripción cuando exista el video | Por firmar |
| Imagen | Por revisar: silla, calendario, mesa y barras genéricos, sin logotipo ni verde; los personajes contra su ficha | Por firmar |
| Portada | Por medir en el fotograma 0 (texto y 492–682; silla y 754–1066; caras en la zona útil) | Por firmar |
| Video y bucle | Render 2: `comprobar_destellos` con margen en 0 cambios, `revisar_fotogramas.py` sin marcas, fotograma 930 igual al 0 (`07_revision/vuelta_02/`) | Por firmar |
| Subtítulos en español | Por medir: banda de y 905 a 1085 sin tocar gráficos ni cabezas; líneas de 856 px o menos | Por firmar |
| Marca del canal | Por revisar (incluida la firma del lápiz, `FIRMA_LAPIZ_BUMERAN.md`) | Por firmar |
| Color | Por medir (se espera aviso por el desenfoque) | Por firmar (director de fotografía y supervisor) |
| Voz y audio | Por generar y oír | Por firmar (diseñador de sonido) |
| Título y línea editorial | Pasa el filtro; falta que el video cumpla lo que promete y que la única mención del motivo sea neutra | Por firmar (director creativo) |
| Escucha de una persona | Pendiente | Dueño |

## 13. Costo

| Concepto | Costo |
|---|---|
| Voz de Tan | por cotizar con `estimate_audio_cost` |
| Voz de Tin | por cotizar con `estimate_audio_cost` |
| Imagen, video, música y efectos | 0 (por código) |
| **Total** | **por cotizar y por autorizar** (referencia del plan anterior: 3,7 créditos) |

## 14. Pendientes

1. Cotizar la voz con `estimate_audio_cost` y pedir el sí del dueño; generar una sola vez cada voz.
2. Reajustar los tiempos de las secciones 5 y 6 y de los subtítulos con la voz real; comprobar que el pico siga entre el 70 y el 75 %; volver a validar y a archivar el prompt.
3. Reescribir el código del render (gráficos nuevos de la sección 14 del prompt, lápiz libre, banda de subtítulos), renderizar y correr los controles de la sección 12.
4. Leer `FIRMA_LAPIZ_BUMERAN.md` cuando exista y ajustar el prompt si difiere (manda la del canal).
5. Medir el color con y sin desenfoque y anotarlo en `direccion.md` (sección 3b) y en `ficha.json`.
6. Compromiso del cierre: preparar el siguiente conteo (otros regresos de directores ejecutivos) dentro de 7 días; si no sale, avisar en un comentario fijado.
7. Armar `08_entrega/TIN-EN-S-003/` y pasar `entrega.py`; publicar solo con el sí del dueño.
