# Ficha técnica — Jensen Huang Is Back: GeForce 256 vs RTX 5090

Resumen de una página del video. El detalle de cada bloque está en el archivo que se cita. Escrita el 2026-11-24 con el prompt versión 1: **la voz no está generada, los tiempos son estimados y el video no está renderizado.**

## 1. Identificación

| Campo | Valor |
|---|---|
| Código | `TIN-EN-S-003` |
| Canal | Tin & Tan, inglés, EE. UU. |
| Tipo | Short n.º 3 (el primero con profundidad y efectos) |
| Título | Jensen Huang Is Back: GeForce 256 vs RTX 5090 (45 caracteres; filtro de títulos: pasa, 0 errores y 0 avisos) |
| Objetivo comercial | Entrar al Programa de socios de YouTube lo antes posible (dueño, 2026-11-23; ver 1b) |
| Público | EE. UU., adultos de 45 a 62 años que armaban o compraban una PC en 1999; secundario, de 30 a 45 que juegan hoy |
| Qué queremos que haga | Verlo entero y mandárselo a quien armó una PC con él; después, suscribirse |
| Estado | Prompt escrito y validado; falta el sí del dueño para la voz (≈ 3,3 créditos), el render y la escucha. Fecha límite para publicar: 2026-12-01 (estimación del comercial) |

## 1b. Objetivos comerciales

**Fijado por el dueño el 2026-11-23:** entrar al Programa de socios de YouTube a la mayor brevedad posible. Textual:
«Entonces el objetivo inicial es entrar al programa de socios; todo debe girar en torno a lograr el objetivo a la mayor brevedad posible».

| Umbral del Programa (fuente oficial, leída el 2026-11-20) | Antes del 1-feb-2027 | Desde el 1-feb-2027 |
|---|---|---|
| Suscriptores | 1.000 | 1.000 |
| Camino de Shorts | 10 millones de vistas de Shorts en 90 días | 20 millones en 90 días |
| Camino de video largo | 4.000 horas públicas en 12 meses | 8.000 horas en 365 días |

| Qué aporta este video al objetivo | Cómo se mide | Meta |
|---|---|---|
| Vistas de Shorts que cuentan para el umbral (públicas y en el feed de Shorts); el tema (un objeto de 1999 y una cuenta) sigue valiendo cuando la noticia se enfríe | Vistas desde el feed de Shorts, a 7 y 28 días; «engaged views» entre vistas totales | Línea base (3.er video) |
| Se quedó a mirar frente a deslizó, que el short 1 midió en 20,7 % (cuatro de cada cinco deslizaron) | Visto frente a deslizado, retención por segundo | Superar el 20,7 % del short 1 |
| **Suscriptores nuevos: este es el primer video que los pide** (una sola frase de Tan, 27,5–28,8 s) | Suscriptores ganados desde este video, por cada mil vistas | Línea base (el short 1 dio 0; el short 2 no los pedía) |
| Compartidos (que el que lo vivió se lo mande a otro) | Compartidos por cada mil vistas; comentarios «yo también» | Línea base (el short 1 dio 0) |
| Aprender qué efectos retienen, para repetirlos | Retención de cada tramo con efecto (tabla B de la sección 11 del prompt) | Un pico visible en 22,2 s |

**Lo que este video hace nuevo por el objetivo:** pide la suscripción una sola vez (`plan_programa_de_socios.md`, P6c) y usa los efectos de `manual/14_efectos_y_emocion.md`, sección 7, contra los tres problemas medidos en el short 1.

## 2. Formato

| Campo | Valor |
|---|---|
| Aspecto y tamaño | 9:16, 1080×1920 |
| Duración | 30,5 s estimados (915 fotogramas a 30 por segundo), en bucle |
| Cómo se hizo | Dibujado por código (`palitos.py` 1.3, `efectos.py` 1.0 y gráficos propios); sin generador de imagen ni de video. Render estimado: 5 a 6 minutos |
| Archivo | `06_final/tin_y_tan_short03_v1.mp4` (por renderizar) |
| Portada | El fotograma 0: `06_final/portada_short03.png` (por guardar con `miniatura.py`) |
| Subtítulos | `02_prompt/subtitulos.srt`, 12 líneas con tiempos estimados |

## 3. Elenco

| Personaje | Papel | Voz | Objeto de mano |
|---|---|---|---|
| Tan | Abre con el recuerdo, hace las dos preguntas y dice la invitación a suscribirse | Zelda, al 110 % | ninguno |
| Tin | Da la noticia del regreso, aclara «transistores, no velocidad» y hace la división | Kevin, al 110 % | Lápiz (tomas 3, 4 y 5) |

Jensen Huang no aparece dibujado ni imitado: solo se le nombra.

## 4. Contenido: la cuenta

| Dato | Valor | Fuente |
|---|---|---|
| Regreso | La junta de Nvidia repuso a Jensen Huang como presidente y director ejecutivo el 23 de noviembre de 2026 | Wikipedia en inglés, «Jensen Huang», y títulos de cadenas en YouTube, leídos el 2026-11-24; **el comunicado de Nvidia no se pudo abrir** |
| GeForce 256 | Lanzada el 11 de octubre de 1999; 17 millones de transistores («Transistor count»); ≈ 23 millones según la prensa de 1999 (solo en un resumen de buscador) | Wikipedia en inglés, «GeForce 256» y «Transistor count», leídas el 2026-11-24 |
| RTX 5090 (GB202) | 92.200 millones de transistores; a la venta desde el 30 de enero de 2025 | Wikipedia en inglés, «Transistor count» y «GeForce RTX 50 series», leídas el 2026-11-24 |
| La cuenta | 92.200 millones ÷ 23 millones ≈ 4.009; ÷ 17 millones ≈ 5.424 | cálculo (Python, 2026-11-24) |
| **Lo que se dice** | **«más de 4.000»**, cierto con las dos cifras; el video usa la de 23 millones (la cautelosa) | cálculo |
| Aclaración | Se cuentan transistores, no velocidad: en voz (línea 5) y en pantalla (11,6–13,4 s y 21,4–27,4 s) | — |

No se dice: rendimiento, precio, bolsa, fortuna, motivo de la salida o del regreso, vida privada, los «11 días», que Jensen Huang diseñó la tarjeta o dirigía la empresa en 1999, ni que la RTX 5090 sea la más grande. Del fabricante solo se dice el nombre: no hay logotipo, letra de marca ni su verde.

## 5. Guion de voz (tiempos estimados)

| N.º | Quién | De–a (s) | Texto |
|---|---|---|---|
| 1 | Tan | 0,00–2,30 | Remember putting one of these in your PC? |
| 2 | Tin | 2,55–5,68 | That's the GeForce 256, from 1999. |
| 3 | Tin | 6,08–9,06 | Nvidia's board brought Jensen Huang back as CEO. |
| 4 | Tan | 9,31–11,26 | How many of those are in a new one? |
| 5 | Tin | 11,51–13,36 | We're counting transistors, not speed. |
| 6 | Tin | 13,61–16,38 | That card had up to 23 million transistors. |
| 7 | Tin | 16,63–20,03 | The RTX 5090 has about 92 billion. |
| 8 | Tin | 20,28–20,98 | Divide them. |
| 9 | Tin | 21,38–22,48 | More than 4,000. |
| 10 | Tan | 22,73–24,48 | Four thousand of these in one of those? |
| 11 | Tin | 24,73–27,16 | That whole wall, in transistors, is one chip. |
| 12 | Tan | 27,50–28,80 | Subscribe and count with us. |

La grafía para el generador (letras separadas, «G Force two fifty-six», «R T X fifty-ninety») está en la sección 7 del prompt. Los tiempos se reajustan con la voz real.

## 6. Tomas

| Toma | De–a (s) | Qué se ve | Texto en pantalla |
|---|---|---|---|
| 1 | 0,0–1,0 | Portada: la tarjeta de 1999 viene hacia la cámara; Tan y Tin debajo, de perfil, mirándola | Jensen Huang / Is Back |
| 2 | 1,0–2,5 | Subjetivo: dos manos meten la tarjeta en la ranura de una PC | — |
| 3 | 2,5–6,0 | La tarjeta en su pedestal, Tin y Tan a los lados, PC de 1999 al fondo; el foco pasa a Tin | GeForce 256, luego 1999 |
| 4 | 6,0–9,0 | El mismo plano: Tin da la noticia del regreso | Nov 23, luego Back as CEO |
| 5 | 9,0–11,5 | Aparece la tarjeta nueva desde el desenfoque; Tan pregunta | RTX 5090 |
| 6 | 11,5–13,5 | El chip con un círculo de tinta; «transistores, no velocidad» | transistors, not speed |
| 7 | 13,5–16,5 | La tarjeta de 1999 grande | up to 23 million |
| 8 | 16,5–20,0 | La RTX 5090 grande (barrido) | RTX 5090, ≈ 92 billion |
| 9 | 20,0–21,0 | La ecuación: una tarjeta entre la otra; subida de sonido y silencio | ≈ 92 billion, ÷ 23 million |
| 10 | 21,0–24,0 | El contador sube hasta la cifra; Tan y Tin celebran | 4,000+ |
| 11 | 24,0–25,5 | Un muro de 4.000 tarjetitas crece | 4,000+ y transistors, not speed |
| 12 | 25,5–27,5 | El muro se pliega y queda igual a una sola tarjeta nueva | = |
| 13 | 27,5–29,5 | Tin y Tan saludan; Tan pide la suscripción | Subscribe, Tin & Tan |
| 14 | 29,5–30,5 | El cierre se congela como foto y cae; vuelve la portada | Jensen Huang / Is Back |

## 7. Perfil de colores

| Color | Hex | Dónde va | Para qué |
|---|---|---|---|
| Papel (neutro) | `#F3E9D2` | Fondo | Calidez de papel impreso |
| Tinta (neutro) | `#2B2420` | Líneas y texto | Lectura: contraste 12,6:1 |
| Mostaza (acento) | `#E8B33B` | La palabra clave y un elemento por plano (dedos de la tarjeta, lápiz o chip) | Lleva el ojo al dato |
| Tomate (excepción del giro) | `#C8553D` | Solo la cifra «4,000+», de 22,2 a 27,4 s | Marca el pico |

Medido: pendiente. Con profundidad se espera ≈ 82 a 85 % dentro de la paleta (el short 2 midió 93 %): el desenfoque y la niebla crean mezclas que no están en la lista. Detalle: `prompt.md`, «Color con intención».

## 8. Animación, luz y velocidad

| Elemento | Qué hay |
|---|---|
| Animaciones | **Nuevas:** capas con paralaje y sombras de contacto, tarjeta que crece hacia la cámara, subjetivo de las manos, garabato, muro que crece, congelado con marco. Se mantienen: muelles con rebote, personajes al pulso, contadores que frenan al llegar |
| Efectos de luz | **Nuevos y sin destellos:** cambio de foco, revelado desde desenfoque, sombras, niebla en las capas lejanas, paso de mostaza a tomate. Cero destellos y cero negativos (`comprobar_destellos` debe pasar) |
| Velocidad del video | 14 tomas y 10 cortes (más 3 planos continuos); la toma más corta dura 1,0 s y la más larga 3,5 s |
| Velocidad del audio | Voz al 110 % (`atempo=1.10`); pausas internas acortadas; dos pausas de 0,40 s diseñadas |

## 9. Sonido

| Elemento | Valor |
|---|---|
| Voces | Zelda (Tan) y Kevin (Tin), una generación cada una, **sin generar** (≈ 3,3 créditos estimados; pide el sí del dueño) |
| Música | Hecha por código, re dórico (distinta de los shorts 1 y 2), un acorde cada 2 s |
| Efectos | ≈ 35 golpes por código; subida, silencio de 12 fotogramas y ding en la cifra (22,2 s) |
| Volumen | Por medir: objetivo −14,0 LUFS; golpes bajo la voz a unos −26 LUFS |
| Guion contra lo que se oye | Por comprobar con `revisar_voz.py` sobre la mezcla |

## 10. Emoción buscada

| Tramo | Segundos | Emoción |
|---|---|---|
| Gancho | 0 a 2,5 | Reconocimiento, alerta leve y curiosidad |
| Presentación | 2,5 a 9 | Nostalgia y presencia tranquila |
| Cuenta | 9 a 21 | Anticipación que crece |
| Pico | 22,2 | Sorpresa y asombro |
| Remate | 24 a 27,5 | Asombro por el tamaño |
| Cierre | 27,5 a 30,5 | Calidez, gratitud y ganas de verlo otra vez |

Elemento por elemento, con su fundamento, su métrica y su riesgo: `02_prompt/perfil_emocional.md` (15 filas).

## 11. Publicación y medición

| Campo | Valor |
|---|---|
| Plataforma | YouTube Shorts primero; después TikTok e Instagram |
| Descripción | La cuenta, las fuentes con fecha, la aclaración de transistores, una línea de suscripción y «Not affiliated with Nvidia. Jensen Huang is not involved in this video.» |
| Categoría | 24 (Entertainment), la misma con la que YouTube aceptó el short 1 |
| Hecho para niños | No |
| Qué se mide | Visto frente a deslizado, duración media vista, vistas desde el feed de Shorts, compartidos, suscriptores, edad del público |
| Metas | Superar el 20,7 % del short 1; línea base de compartidos y suscriptores |
| Entrega | `08_entrega/TIN-EN-S-003/` (pasa los controles del publicador) |

## 12. Controles y firmas

| Control | Resultado | Firma |
|---|---|---|
| Texto y ortografía | Descripción, etiquetas y subtítulos: 0 errores (2026-11-24); falta el texto del render | Por firmar (supervisor de continuidad) |
| Cifras | Recalculadas con Python; falta compararlas con voz, pantalla, `.srt` y descripción cuando exista el video | Por firmar |
| Imagen | Por revisar: las dos tarjetas genéricas, sin logotipo, letra ni verde; los personajes contra su ficha | Por firmar |
| Portada | Por medir en el fotograma 0 (texto y 415–690; tarjeta y 720–1100; caras en la zona útil) | Por firmar |
| Video y bucle | Por revisar: `comprobar_destellos`, `revisar_fotogramas.py`, fotograma 915 igual al 0 | Por firmar |
| Marca del canal | Por revisar | Por firmar |
| Color | Por medir (se espera aviso por el desenfoque) | Por firmar (director de fotografía y supervisor) |
| Voz y audio | Por generar y oír | Por firmar (diseñador de sonido) |
| Título | Pasa el filtro; falta que el video cumpla lo que promete | Por firmar (director creativo) |
| Escucha de una persona | Pendiente | Dueño |

## 13. Costo

| Concepto | Costo |
|---|---|
| Voz de Tan | ≈ 0,8 créditos (estimado, sin cotizar) |
| Voz de Tin | ≈ 2,5 créditos (estimado, sin cotizar) |
| Imagen, video, música y efectos | 0 (por código) |
| **Total** | **≈ 3,3 créditos, por autorizar** |

## 14. Pendientes

1. Cotizar la voz con `estimate_audio_cost` y pedir el sí del dueño; generar una sola vez cada voz.
2. Reajustar los tiempos de las secciones 5, 6 y 7 con la voz real; volver a validar y a archivar el prompt.
3. Escribir el código del render (gráficos nuevos de la sección 14 del prompt), renderizar y correr los controles de la sección 12.
4. Medir el color con y sin desenfoque y anotar el resultado en `direccion.md` (sección 3b) y en `ficha.json`.
5. Armar `08_entrega/TIN-EN-S-003/` y pasar `entrega.py`; publicar solo con el sí del dueño.
