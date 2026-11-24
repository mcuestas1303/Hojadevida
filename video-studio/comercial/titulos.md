# Títulos: qué penetra el algoritmo y la búsqueda, y cómo se escribe uno en este estudio

- **Autor:** comercial-inteligencia-digital
- **Fecha del estudio:** 2026-11-21. Toda página marcada «consultada 2026-11-21» se abrió ese día con `curl` y se leyó completa. Si una página cambia, este documento queda viejo: se vuelve a leer la fuente antes de tocar una regla.
- **Origen:** regla del dueño (2026-11-21), textual: «con respecto al título necesito que alguien del equipo estudie cuáles son los títulos que más penetran el algoritmo y el SEO para tener parámetros y referencias con base al público objetivo y eso volverlo instrucción y filtro; esto también debe quedar en la ficha».
- **Qué es:** el estudio (secciones 1 a 4), la instrucción (5), el filtro (6), los campos de la ficha (7), el chequeo de los títulos que ya existen (8) y lo que falta (9). De aquí sale el script `revisar_titulo.py` y la fila de la ficha técnica.
- **Etiquetas de fuente, en cada afirmación:**
  - **[oficial]**: página de ayuda o blog de YouTube/Google, TikTok o Meta. Lleva enlace y fecha.
  - **[tercero]**: estudio o artículo de una empresa o autor ajeno. Digo quién, muestra y si es correlación. Casi todos son blogs de empresas que venden herramientas: son pistas, no pruebas. Los que solo vi en el resumen del buscador van marcados **«visto en resumen de buscador»** (no los abrí: los hosts están bloqueados o fuera de la lista permitida, ver sección 9).
  - **[observación]**: lo que vi hoy en páginas públicas de YouTube (resultados de búsqueda y páginas de video, abiertos con `curl`). Es medido, pero es una foto de una sesión, personalizada y de la primera página: no es muestra ni estudio.
  - **[opinión mía]**: decisión del equipo comercial sin fuente que la fuerce.
- **Lo que este documento no hace:** no escribe títulos de videos nuevos ni toca guion o prompt. No hay volúmenes de búsqueda ni cifras de vistas fuera de lo que cito con su fuente.

## Parámetros flexibles (2026-11-24)

**Regla del dueño (2026-11-24), textual:** «Cambia esas limitantes y define nuevos parámetros; podría ser que los parámetros sean flexibles». La definición del canal Tin & Tan está en `video-studio/canales/nostalgia-tin-y-tan/PARAMETROS.md`, **que manda sobre este documento**. Su parámetro «Título»: *el que diga con las palabras que la gente busca lo que el video cumple; pregunta, afirmación, comparación, con o sin cifra, con o sin nombre propio; se mide con «se quedó a mirar» y el tráfico de búsqueda.*

**Por qué cambia el filtro.** Buena parte de la sección 6 estaba marcada en este mismo estudio como **[opinión mía]** o como **[tercero], sin verificar**: el rango 25–60, el corte de ≈ 40 caracteres, la lista de palabras, la coherencia de Title Case, «la cifra-respuesta nunca va en el título». Eran opinión, no dato de la plataforma, y bloqueaban títulos que la gente sí busca. Desde hoy, en `tin-y-tan`, **bloquea solo lo que es dato, regla del dueño o riesgo real**; lo demás es **aviso con su porqué** y se mide con los datos del canal. `revisar_titulo.py` pasa a la **versión 1.1**; `--estricto` devuelve el comportamiento de la 1.0.

**El perfil `tiky-lumi` no cambia en nada:** ahí manda `infantil/guia_1_a_3.md` y el veto de la psicóloga.

| Regla de la sección 6 | Antes (1.0) | Desde 1.1 en `tin-y-tan` | Por qué |
|---|---|---|---|
| M1 más de 100 caracteres | (no aplicaba: el tope era 60) | **ERROR** | Límite de YouTube (Y1, oficial) |
| M1 longitud fuera de 25–60 | ERROR | AVISO; se sigue recomendando 30–50 | El rango era [opinión mía]; el corte visible en el feed es de terceros, sin verificar |
| M1 menos de 3 palabras | ERROR | AVISO | Opinión |
| M2 espacios al inicio o al final, dobles, tabulación, salto de línea | ERROR | **ERROR** | Es un defecto, no un estilo |
| M2 signos repetidos («!!», «??», «?!») | ERROR | **ERROR** | YouTube lo llama «loud» (Y6, oficial) |
| M2 cierre en punto, dos puntos o guion; puntos suspensivos | ERROR | AVISO | Estilo del canal |
| M3 caracteres no permitidos (emoji, «#», «@», barra vertical, corchetes…) | ERROR | **ERROR** | «Invalid characters» (Y1) y control de glifos (`manual/12`) |
| M3 cantidad de «!», «?», «:» y paréntesis | ERROR | AVISO | Estilo del canal |
| M4 la frase de búsqueda no aparece una sola vez, no empieza al inicio o termina después del carácter 40 | ERROR | AVISO | «Lo importante al inicio» es recomendación (Y2); el carácter 40 es de terceros, sin dato oficial |
| M5 título en MAYÚSCULAS (salvo siglas) | ERROR | **ERROR** (2 o más palabras, o más del 45 % de las letras). Una sola palabra en mayúsculas fuera de la lista: AVISO; la grafía de una marca autorizada con `--marca` se acepta | Y3 y Y6 piden limitar las MAYÚSCULAS, no prohíben una sigla |
| M6 Title Case imperfecto | ERROR | AVISO | La coherencia dentro del canal era [opinión mía] |
| M7 nombres propios mal escritos («Tin & Tan», «Tiky», «Lumi») | ERROR | **ERROR** | Regla del dueño (2026-11-21) |
| M8 términos de la línea editorial (gender, woke, género, ideología, gênero, ideologia) | ERROR | **ERROR** | Línea editorial del dueño |
| M8 promesas engañosas evidentes (leaked, leak, official, exclusive, not clickbait, guaranteed, 100%) | ERROR | **ERROR** | Prometen lo que un canal que explica con fuentes públicas no puede dar (Y5, Y17) |
| M8 juicio o insulto sobre una persona (liar, crook, scammer, fraudster, thief, pervert, predator, creep, disgraced, evil, idiot, loser, clown) | (no existía) | **ERROR** | `PARAMETROS.md` sección 2: personas reales, solo hechos públicos verificables, sin burla. La máquina solo ve el insulto; afirmar de alguien algo no comprobado lo revisa y firma una persona (6.b) |
| M8 resto de la lista «sensacionalista» (shocking, insane, secret, exposed, viral, trending, free, subscribe, must watch, wait for it…) | ERROR | AVISO | La lista era [opinión mía]; YouTube no publica palabras. Solo se usan si el video las cumple |
| **Palabras de la noticia** («scandal», «resigns», «returns», «fired», «lawsuit», «arrested»…) | (no estaban en la lista) | **Ni error ni aviso** | `PARAMETROS.md`, «Mención de un hecho polémico»: se nombra con las palabras que la gente busca y que usan los medios serios, en título, voz y descripción; sin detalles de la vida privada ni juicio |
| M9 una palabra repetida 3 veces | ERROR | AVISO | Opinión; se cuida el relleno de palabras clave (Y18) |
| M11 marca ajena sin el descargo «Not affiliated with…» en la descripción | ERROR | **ERROR** | Riesgo de reclamo; `PARAMETROS.md` sección 2 |
| M12 la cifra-respuesta en el título | ERROR | AVISO | `PARAMETROS.md`: «la cifra en el título o en la portada se decide por video» y se mide con y sin cifra. Si va, coincide con el video |
| M12 decimal o fracción sin «≈»; «about» o «~» ante una cifra; separador de miles del idioma | ERROR | **ERROR** | Regla del dueño (`manual/12` §2) y ortografía |
| M13 título idéntico a uno ya usado | ERROR | **ERROR** | Duplicado |
| M13 parecido de 0,90 o más, sin ser idéntico | ERROR | AVISO | Se puede repetir una forma que funcionó si el contenido cambia |

**Qué más queda sin efecto en este documento para Tin & Tan** (se conserva escrito como estudio del 2026-11-21): en 3.a, el público «de 45 a 70 años» (sin edad fija: el que tenga la demanda del tema) y la definición del canal por una época; las tres fórmulas pasan a ser ejemplos, no las únicas formas; «la cifra que es la respuesta no va en el título» (5.6 y 6.b.7) pasa a decidirse por video; en 5.2 y 5.3, la posición de la frase y los 30–50 caracteres son recomendación. Las referencias de 4.a y los chequeos de 8.2 y 8.3 son de los shorts 1 y 2, definidos con los parámetros anteriores. **Sigue igual:** el estudio de fuentes (1 y 2), lo que revisa y firma una persona (6.b, salvo el punto 7), la ficha (7) y todo lo de Tiky y Lumi.

**Cómo se usa:** igual que antes; el bloque de la ficha trae `"filtro": {"version": "1.1", "modo": "flexible", …}`. Cada AVISO se lee y se explica por escrito en la ficha (decisión del equipo, con su porqué). Con 0 errores pasa.

## 1. Qué dicen las plataformas

### 1.1 YouTube

| # | Hecho | Cita corta (inglés, tal como está) | Fuente | Tipo |
|---|---|---|---|---|
| Y1 | Límite de caracteres: 100, y no admite «caracteres inválidos». La página no distingue Shorts de largos; supongo el mismo límite para Shorts | "Video titles have a character limit of 100 characters and cannot include invalid characters." | https://support.google.com/youtube/answer/57404?hl=en (consultada 2026-11-21) | oficial |
| Y2 | Cómo escribir un título: exacto, breve, lo importante al inicio, y la marca o el número de episodio al final | "put the most important words near the beginning. Save episode numbers and branding for the end." | https://support.google.com/youtube/answer/12340300?hl=en (2026-11-21) | oficial |
| Y3 | Se pide limitar MAYÚSCULAS TOTALES y emoji, y usarlos solo para énfasis | "Limit ALL CAPS and emoji." | https://support.google.com/youtube/answer/12340300?hl=en (2026-11-21) | oficial |
| Y4 | Dos tipos de título: el «buscable» (dice qué esperar, llega a quien busca) y el «intrigante» (despierta curiosidad, llega a quien no busca ese tema). YouTube recomienda elegir según quién lo verá y dónde | "Searchable titles that clearly outline what to expect" / "Intriguing titles that spark curiosity" | https://support.google.com/youtube/answer/12340300?hl=en (2026-11-21) | oficial |
| Y5 | Un título inexacto hace que el espectador deje de ver, y eso afecta el descubrimiento | "Make sure your title accurately represents the video. If not, viewers may stop watching, which can impact discoverability." | https://support.google.com/youtube/answer/12340300?hl=en (2026-11-21) | oficial |
| Y6 | Qué evitar en título y miniatura: engañoso o sensacionalista, chocante, repugnante, violencia gratuita, sugerente, y «ruidoso» (MAYÚSCULAS o !!!!!) | "Loud: Uses ALL CAPS or !!!!! to overemphasize titles" | https://support.google.com/youtube/answer/141805?hl=en (2026-11-21) | oficial |
| Y7 | Búsqueda: se ordena por relevancia (título, etiquetas, descripción y contenido frente a la consulta), interacción y calidad. YouTube no da pesos. La búsqueda no es una lista de lo más visto | "how well the title, tags, description, and video content match your search query" / "Search results are not a list of the most-viewed videos for a given search." | https://support.google.com/youtube/answer/16090438?hl=en y https://support.google.com/youtube/answer/141805?hl=en (2026-11-21) | oficial |
| Y8 | Recomendación: el sistema mira atractivo («¿eligieron verlo o lo ignoraron?»), interacción y satisfacción. El título y la miniatura «comunican valor y fijan expectativas»; los primeros segundos deben cumplir lo que prometen | "Your title and thumbnail are vital for communicating value, sparking intrigue, and setting clear expectations for viewers." / "Ensure your intro delivers on the promise made by your thumbnail and title" | https://support.google.com/youtube/answer/16559650?hl=en (2026-11-21) | oficial |
| Y9 | El sistema aprende «cuánto del video ve el espectador y si queda satisfecho»; no recomienda según si el video monetiza | "The system learns how much of the video the viewer watches and if they're satisfied." | https://support.google.com/youtube/answer/141805?hl=en (2026-11-21) | oficial |
| Y10 | El clickbait da clics pero poca duración media de visualización, y por eso se recomienda menos. YouTube da la señal para detectarlo: CTR alto con duración media baja e impresiones menores a las esperadas | "Clickbait videos tend to have low average view duration and therefore are less likely to get recommended by YouTube." | https://support.google.com/youtube/answer/7628154?hl=en (2026-11-21) | oficial |
| Y11 | Cambiar título o miniatura puede mover el alcance, pero por cómo reaccionan los espectadores, no por el cambio en sí | "don't change what's working" | https://support.google.com/youtube/answer/141805?hl=en (2026-11-21) | oficial |
| Y12 | CTR de referencia: la mitad de los canales y videos está entre 2 % y 10 %; en búsqueda el CTR suele ser más alto y en Inicio más bajo; no mirar el CTR justo después de subir; probar varios títulos en el mismo video es difícil porque el público cambia por fuente de tráfico | "Half of all channels and videos on YouTube have an impressions CTR that can range between 2% and 10%." | https://support.google.com/youtube/answer/7628154?hl=en y https://support.google.com/youtube/answer/16767369?hl=en (2026-11-21) | oficial |
| Y13 | **Prueba A/B de títulos: existe, con límites que nos dejan fuera.** Hasta 3 títulos y/o miniaturas; solo computadora, en YouTube Studio; requiere funciones avanzadas; el ganador es el de más tiempo de visualización (no el de más clics); termina en unas dos semanas. **No se puede en Shorts y no se puede en videos «hechos para niños»** | "You are not able to A/B test Shorts" / "You cannot use this feature on videos that are made for kids" / "we optimize tests for overall watch time over other metrics, like click-through-rate" | https://support.google.com/youtube/answer/16391400?hl=en (2026-11-21) | oficial |
| Y14 | Etiquetas: pesan poco; el título, la miniatura y la descripción son los metadatos importantes; sirven sobre todo para errores de ortografía. Demasiadas etiquetas va contra la política de spam | "Tags can be useful if the content of your video is commonly misspelled. Otherwise, tags play a minimal role in your video's discovery." | https://support.google.com/youtube/answer/146402?hl=en y https://support.google.com/youtube/answer/16559650?hl=en (2026-11-21) | oficial |
| Y15 | Hashtags: de los de la descripción, hasta tres aparecen junto al título; más de 60 en un video y se ignoran todos; los hashtags engañosos o sin relación se pueden sancionar | "up to three hashtags that are considered most engaging will appear by your video title" / "If a video or playlist has more than 60 hashtags, we'll ignore each hashtag on that content." | https://support.google.com/youtube/answer/6390658?hl=en (2026-11-21) | oficial |
| Y16 | Descripción: elegir 1 o 2 palabras principales y ponerlas «de forma destacada» en título y descripción; el informe «Cómo encuentran tu video» da los términos de búsqueda reales | "Identify 1-2 main words that describe your video and feature them prominently in both your description and title." | https://support.google.com/youtube/answer/12948449?hl=en (2026-11-21) | oficial |
| Y17 | Metadatos engañosos: el «clickbait malicioso» (título, miniatura o descripción que no cumplen lo prometido) viola la política de spam; la sanción puede ser suspender la monetización o cerrar el canal | "Using maliciously misleading titles, thumbnails, descriptions, or imagery to trick users into clicking on a video that does not deliver what was promised." | https://support.google.com/youtube/answer/2801973?hl=en (2026-11-21) | oficial |
| Y18 | **Contenido «hecho para niños»**: los principios de calidad marcan como baja calidad el título o miniatura que engaña con lo educativo y el «relleno de palabras clave» (usar palabras populares entre niños de forma repetida, alterada o exagerada). YouTube Kids no admite «keyword stuffing» en títulos | "content that uses titles or thumbnails to trick kids into thinking it's educational, when it's really not" / "Keyword stuffing in titles (i.e., excessive use of keywords)" | https://support.google.com/youtube/answer/10774223?hl=en, https://support.google.com/youtube/answer/1311392?hl=en y https://support.google.com/youtube/answer/10938174?hl=en (2026-11-21) | oficial |
| Y19 | Quien revisa un canal para el Programa de socios mira, entre otras cosas, los metadatos: títulos, miniaturas y descripciones | "Video metadata (including titles, thumbnails, and descriptions)" | https://support.google.com/youtube/answer/1311392?hl=en (2026-11-21); misma fila en `base_conocimiento.md` §1 | oficial |
| Y20 | Shorts: la métrica que hace el papel de impresiones y CTR es «Shown in feed» (cuántas veces salió en el feed) y la proporción de quienes lo vieron frente a quienes lo deslizaron | "Highlights the percentage of times that viewers viewed your Shorts versus swiped away." | https://support.google.com/youtube/answer/12942217?hl=en (2026-11-21). En esa página el nombre de la columna es «How many chose to view»; la comunidad de YouTube lo llama «Viewed vs swiped away» (resumen de buscador, https://support.google.com/youtube/community-video/273390203/new-youtube-shorts-metric-viewed-vs-swiped-away) | oficial |
| Y21 | Varios idiomas en un solo canal: la búsqueda lee los títulos y descripciones traducidos, y se pueden subir miniaturas por idioma en videos largos | "Our search systems look at these translated titles and descriptions to provide accurate results in the language they speak." | https://support.google.com/youtube/answer/13338784?hl=en (2026-11-20, de `base_conocimiento.md` §9) | oficial |

**Lo que YouTube no publica (sin dato oficial):**

- Cuántos caracteres del título se ven en el celular antes de cortarse, en Inicio, en búsqueda o en el feed de Shorts. Ninguna de las páginas que abrí da una cifra.
- Cuánto pesa cada elemento en la búsqueda (título frente a descripción).
- Si el título de un Short se ve en el feed de Shorts. Las fuentes de terceros se contradicen (sección 2.5).
- Si un Short «hecho para niños» entra al feed de Shorts de la misma forma. `base_conocimiento.md` §7 lo deja como sin verificar.
- Una regla sobre nombres de marcas de terceros en el título. La política de spam habla de clickbait y la de suplantación de canales, pero ninguna dice nada de nombrar un producto ajeno en el título (búsqueda del 2026-11-21, resumen de buscador restringido a `support.google.com`).

### 1.2 TikTok

| # | Hecho | Cita corta | Fuente | Tipo |
|---|---|---|---|---|
| T1 | TikTok recomienda usar la descripción («caption») para dar contexto, y hashtags solo si representan el video; más hashtags no dan más alcance; #FYP y similares funcionan como cualquier otro hashtag | "More hashtags won't guarantee a broader reach, and there's only so much space in your captions, so only add hashtags that best represent what your video is about." | https://newsroom.tiktok.com/5-tips-for-tiktok-creators?lang=en (publicada 2020-07-30; consultada 2026-11-21) | oficial |
| T2 | Búsqueda: la ayuda dice que los resultados más relevantes salen en la pestaña «Top». No pude abrir el texto | sin cita: la página `support.tiktok.com` devolvió solo la cáscara vacía | https://support.tiktok.com/en/using-tiktok/exploring-videos/discover-and-search (2026-11-21). Visto en resumen de buscador (oficial) | oficial, sin verificar |

**Sin dato oficial:** límite actual de caracteres de la descripción de TikTok y peso de las palabras de la descripción en la búsqueda. Los resultados del buscador son videos de creadores y páginas «discover» que dan 500, 2.200 o 4.000 caracteres y se contradicen; no los uso.

### 1.3 Instagram (Meta)

| # | Hecho | Cita corta | Fuente | Tipo |
|---|---|---|---|---|
| I1 | En la búsqueda de Instagram, el texto escrito por quien busca es «de lejos» la señal más importante; se compara con nombres de usuario, biografías, pies de foto («captions»), hashtags y lugares | "The text you enter in the search bar is by far the most important signal for Search." | https://about.instagram.com/blog/announcements/break-down-how-instagram-search-works (Adam Mosseri, 2021-08-25; consultada 2026-11-21) | oficial |
| I2 | Para que una publicación aparezca en la búsqueda, las palabras clave y hashtags van en el pie, no en los comentarios | "For a post to be found in Search, put keywords and hashtags in the caption, not the comments." | misma URL | oficial |
| I3 | La búsqueda por palabras clave se afinaba primero en inglés, con otros idiomas después (2021). Hoy: sin dato | "We’re currently focused on getting keyword search results right in English" | misma URL | oficial, de 2021 |
| I4 | Reels: instagram da como señales el audio, lo visual y la popularidad, y limita clickbait y «engagement bait» | ver `base_conocimiento.md` §10.1 (leídas 2026-11-20) | https://creators.instagram.com/faq | oficial |

Instagram no tiene «título»: el pie de foto cumple ese papel. **Sin dato oficial:** longitud visible del pie antes del «más».

### 1.4 Qué sale de esto

- **Es [oficial] que el título debe ser exacto, corto, con lo importante al inicio.** Que la palabra clave vaya primero es consejo oficial de visibilidad («most important words near the beginning»), no un peso medido en el ranking.
- **Es [oficial] que el clic no basta.** La búsqueda y la recomendación premian la interacción y la satisfacción. Un título que promete más de lo que el video da baja la duración vista y el sistema lo reparte menos (Y5, Y8, Y10).
- **En contenido infantil hay una regla extra [oficial]:** el «relleno de palabras clave» y el título que promete enseñar lo que no enseña bajan la calidad del contenido infantil y, con ella, la monetización (Y18).
- **La prueba A/B nativa no existe para nuestros dos canales [oficial]:** Tin & Tan publica solo Shorts y Tiky y Lumi está marcado «hecho para niños» (Y13). Las «dos alternativas para prueba A/B» de la ficha quedan como reserva, no como experimento (ver sección 7).

## 2. Qué dicen los estudios de terceros

Todos los estudios de esta sección los vi en **resumen de buscador** (consultas del 2026-11-21): los sitios están bloqueados desde esta red (`backlinko.com` devolvió «CONNECT tunnel failed, response 403» al probarlo) o fuera de la lista permitida, y no los intenté por otra vía. Ninguno es sobre contenido infantil ni sobre nostalgia. Todos son observacionales (correlación): ninguno prueba que cambiar un título cause más vistas. Casi todos son de empresas que venden herramientas.

### 2.1 Resumen por estudio

| Estudio | Quién | Muestra | Qué reporta | Limitaciones |
|---|---|---|---|---|
| «We Analyzed 1.3 Million YouTube Videos» (https://backlinko.com/youtube-ranking-factors) | Backlinko | ≈ 1,3 millones de videos | Palabra clave exacta en el título: correlación débil con el ranking; YouTube puede entender el sentido sin coincidencia exacta | Página con ≈ 3.500 días según el buscador (≈ 2017): es el YouTube de entonces. Correlación |
| «YouTube SEO: How to Rank YouTube Videos [Study]» (https://www.briggsby.com/reverse-engineering-youtube-search) | Briggsby | ≈ 100.000 videos | Los títulos de los 20 primeros resultados rondan 47 a 48 caracteres; el autor dice que la longitud no es un factor directo | Correlación; antiguo |
| «How to write YouTube titles that get views: a data study [2026]» (https://air.io/en/audience-growth/how-to-write-a-youtube-title-that-gets-clicked-research-across-11-niches) | AIR Media Tech | 18.080 canales en inglés, 11 nichos (de un grupo inicial de 22.294) | MAYÚSCULAS asociadas a mejor resultado; preguntas, a peor; números, apenas positivo; un resumen del buscador ubica lo mejor en 30 a 50 caracteres | Empresa de analítica; mide canales, no videos sueltos; el nicho infantil es 1 de 11 |
| «YouTube titles that get views: what 63,000 videos tell us» (https://returbe.com/blog/youtube-titles-that-get-views) | Returbe | 63.480 videos largos, 3.232 canales | Mide cada video contra el promedio de su canal («outlier»); la base es 11,1 %: signos de pregunta 9,6 %, emoji 9,6 %, corchetes 9,9 %, una palabra en mayúsculas 10,5 %, hábito de mayúsculas en todo el título 9,0 % | Solo videos largos; «outlier» es la métrica del autor |
| «YouTube Title Length: 100 Is the Limit, 55 Is What Breakouts Use» (https://outlierkit.com/resources/youtube-title-length/) | OutlierKit | 473 títulos de videos «breakout» | 29 % tenía un número; 3 % estaba mayormente en mayúsculas; la longitud típica del breakout fue 55 | Solo ganadores (sin comparación con los que no despegaron); vende una herramienta |
| «Best YouTube Title Length: 2,622 Titles Analyzed» y «Do Brackets…» (https://www.overseeros.com/blog/best-youtube-title-length-study y https://www.overseeros.com/blog/brackets-in-youtube-titles) | OverseerOS | 2.622 videos | Sin longitud óptima universal; con corchetes o paréntesis 8,1 % de «breakout» frente a 10,9 % sin ellos | Correlación; vendedor de herramientas |
| «YouTube Title Length: A 28,947-Video Study» (https://ytgrowth.io/blog/youtube-title-length) | ytgrowth.io | 28.947 videos | La longitud explica casi nada de la variación; números, corchetes, dos puntos, mayúsculas y emoji no marcaron diferencia medible | Correlación; vendedor |
| «Four Famous YouTube Title Rules, Tested» (https://creaticalc.com/blog/youtube-title-rules-tested) | Creaticalc | 1.022 videos, 10 nichos (52 a 180 por nicho) | Los números perjudican en tecnología; los títulos con emoji rinden menos (0,87 de la mediana, p = 0,034) | Muestra chica por nicho |
| «Do Emojis in YouTube Titles Help or Hurt Your Views?» (https://vidiq.com/blog/post/emojis-in-youtube-titles/, 2025-11-06) | vidIQ | 128,5 millones de videos (98,9 millones de Shorts y 29,8 millones largos) | Shorts con emoji: +49 % de vistas medianas; largos: no más vistas, algo más de interacción; sugiere 1 o 2 emoji | Observacional; vendedor. Otro análisis de vidIQ citado en el mismo resumen (1,5 millones con emoji frente a 7,5 millones sin) encontró peor alcance con emoji |
| «Best YouTube Shorts Title Length», «Should you put #Shorts in the title» (https://www.overseeros.com/blog/best-youtube-shorts-title-length y https://www.overseeros.com/blog/should-you-put-shorts-in-youtube-title) | OverseerOS | 18.436 Shorts (longitud) y 17.280 Shorts (hashtag) | Más vistas medianas con 21 a 40 caracteres, pero dentro de un mismo canal (54 canales) casi empata; los Shorts sin hashtags en el título tuvieron cerca del doble de vistas medianas | Correlación; los hashtags pueden ser marca de un tipo de canal |
| «10K+ Trending YouTube Shorts Videos Analyzed» (https://www.tunepocket.com/youtube-shorts-video-titles/) | Tunepocket | más de 10.000 Shorts en tendencia | Promedio ≈ 51 caracteres y 8 palabras; «#Shorts» en ≈ 17 % de los títulos | Solo Shorts en tendencia (sesgo de selección) |
| «Do you put the year in the title» (https://www.overseeros.com/blog/should-you-put-year-in-youtube-title) | OverseerOS | sin dato de muestra en el resumen | Poner el año actual rinde 1,02 veces la mediana: casi nada | Sin muestra visible |
| «vidIQ Research, July 2026» (https://vidiq.com/research/youtube-title-formulas-study/) | vidIQ | más de 4 millones de videos | Los marcos de historia específicos le ganan a las fórmulas genéricas | Solo vi el resumen del buscador; sin datos de posición de palabra clave |
| Pew Research, 2019 (https://www.pewresearch.org/internet/2019/07/25/3-certain-keywords-in-video-titles-and-descriptions-were-associated-with-more-views/) | Pew Research Center | canales populares de 2019 | Algunas palabras concretas en el título (por ejemplo «Fortnite», «ASMR») se asociaron con más vistas | De 2019; público general, no infantil |

### 2.2 Qué se puede decir por tema, y dónde se contradicen

| Tema | Lo que dicen los estudios | Qué decido |
|---|---|---|
| **Longitud** | Los números van de 21 a 40 (Shorts, OverseerOS), 30 a 50 (AIR), 47 a 48 (Briggsby, ranking), 51 (Shorts en tendencia), 55 (OutlierKit, breakouts) y «casi nada» (ytgrowth, OverseerOS en largos). **Se contradicen en el punto exacto y coinciden en el orden de magnitud: entre ≈ 30 y ≈ 55 caracteres, lejos de los 100 permitidos** | [opinión mía] objetivo 30 a 50, máximo 60 (sección 3). Coincide con lo oficial «sea breve» (Y2) |
| **Palabra clave al inicio** | Backlinko: correlación débil con tener la palabra en el título; ningún estudio que vi prueba la posición. Una cifra de «2,3 veces más impresiones» circula sin fuente: no la uso | Lo respalda lo **oficial** (Y2 y Y16: lo importante al inicio y la palabra principal en título y descripción). Es consejo oficial, no una medición de peso |
| **Números** | Débil positivo (AIR); 29 % de los breakouts llevan uno (OutlierKit); sin efecto (ytgrowth); perjudican en tecnología (Creaticalc) | Sin respaldo claro para ponerlos o quitarlos. Por regla del dueño los decimales llevan «≈» y la cifra-respuesta no va en el título (sección 6) |
| **Preguntas** | Peor (AIR); cerca de la base (Returbe, 9,6 % frente a 11,1 %) | Efecto pequeño o nulo. La pregunta se usa cuando es la búsqueda real (por ejemplo «cuántos días») |
| **MAYÚSCULAS** | Mejor (AIR); una palabra en mayúsculas, cerca de la base (Returbe 10,5 %); todo el título en mayúsculas, peor (Returbe 9,0 %); 3 % de los breakouts (OutlierKit) | **Aquí hay contradicción entre terceros, pero lo [oficial] es claro:** limitar mayúsculas (Y3, Y6). Cero mayúsculas totales |
| **Emoji** | Shorts +49 % (vidIQ, 128 M); largos sin efecto o peor (vidIQ); sin diferencia (ytgrowth); peor (Creaticalc, 0,87); inconsistente (OverseerOS) | **Se contradicen.** Lo oficial pide limitarlos (Y3). Cero emoji por ahora; se puede probar en un Short de Tin & Tan cuando haya línea base, ver 3.a |
| **Corchetes y paréntesis** | Peor con corchetes (OverseerOS 8,1 % frente a 10,9 %); cerca de la base (Returbe 9,9 %); sin diferencia (ytgrowth) | Efecto pequeño. Cero corchetes; un paréntesis como máximo (la edad, en niños) |
| **Año** | 1,02 veces: casi nada (OverseerOS) | Sin año en títulos que quieren durar. |
| **Hashtags en el título (Shorts)** | Sin «#Shorts» en el título, cerca del doble de vistas medianas (OverseerOS); 17 % de los Shorts en tendencia lo llevan (Tunepocket) | Cero hashtags en el título. YouTube ya muestra hasta tres de la descripción junto al título (Y15) |

### 2.3 Lo que veo en la vida real (observación)

Para tener una foto del terreno miré la primera página de resultados de YouTube el 2026-11-21 para las búsquedas del tema.

**Búsquedas de niños** (estos son los títulos que un adulto ve al buscar):

- Inglés, «teach baby to wave hello toddler»: 8 de 12 títulos tienen 80 caracteres o más, y varios llegan a 95 a 100, con barras «|», emoji y varias palabras de público seguidas.
- Español, «enseñar a saludar con la mano bebé»: 7 de 10 títulos con 80 caracteres o más.
- Portugués, «bebê aprender a dar tchau acenar»: 4 de 12 con 80 o más.
- Las cifras altas no son prueba de que alargar funcione: la primera página la arman señales de todo tipo. Los dos títulos más vistos de las búsquedas en español miden 47 y 86 caracteres. Son hechos, no una receta, y no copio ninguno (la regla de la serie es no copiar títulos).

**Búsquedas de Tin & Tan:** para «cassette pencil rewind», el 2026-11-21 la página mostraba Shorts con títulos de 47 a 103 caracteres, muchos con hashtags dentro del título; el más visto (4,3 millones de vistas) mide 99 caracteres y lleva «POV» y dos hashtags. Hay una muestra de por qué conviene ser breve y claro, no de que los hashtags funcionen: son canales de nostalgia grandes, con otro volumen.

## 3. Parámetros por público y canal

Cada fila dice el parámetro, su valor, el porqué y el tipo de fuente. «Frase de búsqueda» es lo que escribe quien busca, tal como queda escrita en la ficha de publicación del video.

### 3.a Tin & Tan: adultos de EE. UU., inglés, Shorts

> Estudio del 2026-11-21, con los parámetros anteriores del canal. Para Tin & Tan rige la sección «Parámetros flexibles (2026-11-24)»: sin edad fija, el canal no se define por una época y los valores de esta tabla son puntos de partida.

**Quién elige:** el propio espectador (adulto de 45 a 70 años según el brief del casete; la franja sigue sin confirmar por el dueño). Ve el Short en el feed de Shorts, casi sin miniatura: la portada es el fotograma del segundo 0. El título aparece en el feed, en búsqueda y en la página del canal.

| Parámetro | Valor | Porqué | Tipo |
|---|---|---|---|
| Longitud objetivo | 30 a 50 caracteres | Coincide con lo oficial «sea breve» y con los estudios de longitud, que difieren pero rondan ese rango | oficial (Y2) + tercero (2.2) |
| Longitud mínima y máxima | mínimo 25, máximo 60 | 60 es la regla de la ficha de los equipos (C4 de `hola_granja`); 100 es el límite duro (Y1). Los dos títulos del canal miden 48 y 36 | opinión mía, apoyada en Y1 |
| Caracteres visibles en el móvil | **sin dato oficial.** Los terceros dan ≈ 40 para el feed de Shorts, ≈ 50 en Inicio y 45 a 55 en búsqueda en celular, con variación por pantalla y tipografía (resumen de buscador de varias páginas de herramientas SEO, 2026-11-21; el resumen no atribuye cada cifra a una página) | Por eso el plan es **que la frase de búsqueda termine dentro de los primeros 40 caracteres** | tercero, sin verificar |
| Dónde va la frase de búsqueda | al inicio: la primera palabra de la frase empieza en el carácter 1 a 4 y la frase termina antes del carácter 40 | «lo importante al inicio» (Y2) y descripción y título con la misma palabra (Y16) | oficial |
| Fórmula 1: objeto o acto + pregunta sin respuesta | `[Acto buscado]: How Many/How Long [lo que se cuenta]?` Ejemplo ya publicado: «Rewind a Cassette With a Pencil: How Many Turns?» | Cumple el «buscable» (Y4) y no adelanta el resultado (decisión del dueño en el casete). Evita el «clickbait» porque el video sí calcula | oficial (Y4, Y5) + decisión del equipo |
| Fórmula 2: pregunta con el nombre propio del tema | `How Many Days Did We Wait for GTA 6?` | La pregunta es la búsqueda real; el nombre del producto va dentro de los primeros 40 caracteres | opinión mía |
| Fórmula 3: búsqueda + promesa de método | `[Búsqueda]: The Real Math Behind It` (alternativa «Cassette Pencil Rewind: The Real Math Behind It») | «Real math» es verdad en este canal (cada video calcula de verdad). Si un video no calcula, no se usa | opinión mía |
| Palabras que evitar | los gestos de clickbait y lo que YouTube cataloga como «ruidoso» o engañoso: «you won't believe», «shocking», «insane», «gone wrong», «must watch», «wait for it», «secret», «exposed», «leaked»; lista completa en 6.a | Y6, Y10, Y17 | oficial (categorías) + opinión mía (palabras) |
| Mayúsculas | «Title Case» en inglés (cada palabra con mayúscula, salvo artículos y preposiciones cortas); ninguna palabra en MAYÚSCULAS salvo siglas de una lista corta («GTA», «VHS», «CD», «TV», «DVD», «AI», «USA») | Y3 y Y6; la coherencia dentro del canal es [opinión mía]. El título del casete está en Title Case y el de GTA 6, hoy, en minúsculas de frase: se unifican | oficial + opinión mía |
| Signos | máximo 1 «:», 1 «?», 1 «!»; nunca «!!», «??» ni «?!»; sin barra vertical, corchetes, llaves, «#» ni «@» | Y6 (!!!!!) y el efecto de corchetes en 2.2 | oficial + opinión mía |
| Emoji | 0 | Y3 pide limitar. Los estudios se contradicen (2.2). Una prueba posterior con 1 emoji en un Short se puede hacer cuando haya línea base; además el texto pasa por `revisar_texto.py` y por el control de glifos (`manual/12`, 1.6) | oficial + opinión mía |
| Hashtags | 0 en el título; hasta 3 en la descripción, que YouTube muestra junto al título (Y15) | Y15 y OverseerOS (2.2) | oficial + tercero |
| Marcas de terceros | se permite nombrar el producto cuando es **el tema del video** («GTA 6»), nunca como gancho de otro tema; la descripción lleva la línea «Not affiliated with …» (ya la lleva GTA 6); sin «official», «leaked» ni «exclusive» | YouTube no publica regla sobre nombrar marcas en el título (1.1, sin dato). Esto es prudencia [opinión mía]: el riesgo es una queja de la empresa, no una regla de la plataforma | opinión mía |
| Cifras | decimales y fracciones con «≈» y a lo sumo un decimal; la cifra que es la respuesta del video no va en el título | `manual/12` §2 (regla del dueño, 2026-11-21) y la decisión del casete | regla del dueño |
| Idioma | inglés de EE. UU.: ortografía americana (color, not colour), pulgadas y pies, «,» de miles y «.» decimal | `manual/12` §1.5 | regla del dueño |
| Fuente que mide si funcionó | «Viewed vs swiped away» (a veces «How many chose to view») y «Shown in feed», más «YouTube search» en fuentes de tráfico | Y20 | oficial |

### 3.b Tiky y Lumi: el adulto que elige el video de un niño de 1 a 3 años

**Quién elige y para quién se escribe:** el adulto (madre, padre, cuidador). El título le habla a él; al niño solo le habla el video. Todo el contenido está marcado «hecho para niños»: sin comentarios, sin campana, sin tarjetas ni pantallas finales, sin anuncios personalizados (`base_conocimiento.md` §5). **La prueba A/B nativa no existe para este canal (Y13).** Formato largo 16:9 (capítulo) y Short 9:16.

| Parámetro | Capítulo (16:9) | Short (9:16) | Porqué y fuente |
|---|---|---|---|
| Longitud objetivo | 35 a 50 caracteres | 25 a 40 caracteres | La serie ya usa 37 a 50. El Short se ve en un feed más estrecho: lo pongo más corto [opinión mía, apoyada en Y2 y 2.2] |
| Mínimo y máximo | mínimo 20, máximo 60 | mínimo 15, máximo 50 | Máximo 60 es la regla actual de la ficha (C4). El Short, 50, para que la frase quede dentro de ≈ 40 [opinión mía] |
| Caracteres visibles en el móvil | **sin dato oficial**; terceros ≈ 50 en Inicio y 45 a 55 en búsqueda | ≈ 40 en feed de Shorts (tercero, sin verificar) | La frase de búsqueda va entera dentro de los primeros 45 (capítulo) o 40 (Short) |
| Dónde va la frase | la primera palabra en el carácter 1 a 4 | igual | Y2. Los títulos de la serie ya empiezan con la acción («Saludar con la mano…», «Wave Hello…», «Acenar com a mãozinha…») |
| Fórmula 1 (capítulo) | `[Acción del niño]: [nombre del capítulo] con Tiky y Lumi` | | Es la de la serie: acción al inicio, marca al final (Y2) |
| Fórmula 2 (capítulo con edad) | `[Acción] ([edad]): [nombre del capítulo]` | | Cuando la búsqueda lleva la edad. La edad va entre paréntesis y debe coincidir con la ficha pedagógica; sin edades por debajo de la ficha. Consume ≈ 13 caracteres |
| Fórmula 3 (capítulo, solo acción) | `[Acción] con Tiky y Lumi en la [lugar]` | | Cuando el nombre del capítulo no aporta búsqueda |
| Fórmula del Short | `[Acción] con Tiky` o `[Acción] con Lumi` (un solo personaje: el Short es un solo momento) | | Se mantiene corto. Ojo: «Wave Hello with [nombre]» ya aparece en títulos ajenos (2.3 y sección 4); se revisa el Short en inglés antes de fijarlo |
| Palabras que evitar | promesas de desarrollo («tu bebé hablará»), lenguaje médico, superlativos, gancho («no te lo pierdas»), «sorpresa», marcas y personajes ajenos, y la palabra del público repetida; lista completa por idioma en 6.a | Y5, Y17, Y18: el título que promete enseñar lo que no enseña y el relleno de palabras clave bajan la calidad infantil | oficial (Y18) + opinión mía (palabras) |
| Mayúsculas | español y portugués: mayúscula solo en la primera palabra, tras «:», y nombres propios; inglés: Title Case. **Nunca palabras en MAYÚSCULAS** | Y3, Y6. Las mayúsculas de frase son la norma de cada idioma [opinión mía] | oficial + opinión mía |
| Signos | un solo «:» como separador; sin «!», sin barra vertical, sin guiones como separador; como mucho un paréntesis (la edad) y un «?» | El tono calmado de la serie y `guia_1_a_3` [opinión mía]; la barra vertical es el signo del relleno que vi en las búsquedas (2.3) | opinión mía |
| Emoji | 0 | Y3 y Y18 (los títulos llenos de emoji y palabras clave son lo que YouTube describe como relleno) | oficial + opinión mía |
| Hashtags | 0 en el título; 0 a 3 en la descripción | Y15; no pude verificar si en «hecho para niños» cambia algo | oficial |
| Marcas de terceros | **0**: ni personajes ni canales ajenos, ni en título ni en etiquetas | La serie no imita ni copia; YouTube pone como baja calidad el contenido que se apoya en marcas (`base_conocimiento.md` §6) | opinión mía, apoyada en oficial |
| Idioma | cada idioma se escribe desde cero, con la palabra que usa el adulto del mercado | Los tres mercados no buscan igual (ver abajo) y YouTube busca por título traducido (Y21) | oficial (Y21) |
| Fuente que mide si funcionó | CTR de impresiones (largo), «Viewed vs swiped away» (Short), «YouTube search» en fuentes de tráfico | Y12, Y20 | oficial |

**Palabra de búsqueda por idioma (observación del 2026-11-21, sin volúmenes):**

- **Español (México):** los adultos y los canales usan «saludar» y «saludo» («Canción de SALUDO», «Aprender a Saludar», «Enseñándole a su bebé a saludar»). La frase «saludar con la mano» está respaldada por lo que se ve.
- **Inglés (EE. UU.):** aparecen «wave hello», «learn to wave», «say hi and bye», «wave bye bye». «Wave hello» está respaldada.
- **Portugués de Brasil:** **dominan «dar tchau» y «oi e tchau»**; «acenar» aparece poco («Vamos Acenar?»). Es decir, «acenar com a mãozinha» (la frase elegida) puede tener menos búsqueda que «dar tchau» u «oi e tchau». Como el capítulo enseña a saludar al llegar («oi») y no a despedirse, no cambio la frase sin decisión: lo dejo como **propuesta a la pedagoga** (qué palabra del gesto usa el adulto brasileño para el saludo de llegada) y como prueba para los datos del canal. Sin volumen que lo confirme.

## 4. Referencias

**Estado de las fuentes:** pude abrir las páginas públicas de YouTube (resultados y página de video) con `curl` el 2026-11-21. Las vistas y la antigüedad son las que mostraba la página ese día. Solo incluyo títulos que vi tal cual en esa página, no resúmenes de buscador. No se copian títulos, miniaturas, personajes ni canciones; son para aprender qué formas existen. Las fórmulas y las observaciones son [opinión mía].

### 4.a Para Tin & Tan (inglés, adultos de EE. UU., Shorts)

> Referencias del 2026-11-21, buscadas para el short 1 (casete) con los parámetros anteriores. Para un tema nuevo se buscan las referencias de ese tema el día que se escribe el título.

| # | Título tal cual | Canal y enlace | Formato y vistas (2026-11-21) | Qué se aprende |
|---|---|---|---|---|
| 1 | The cassette tape pencil mystery finally solved! | VWestlife, https://www.youtube.com/watch?v=vaSN4J3a_60 | largo, 11:24; 407.219 vistas; hace 4 años | Es el tema exacto del casete y de un canal adulto de nostalgia técnica. Los objetos van al inicio y la promesa («finally solved») la cumple el video. 48 caracteres |
| 2 | Rewinding a Tape with a Pen | Allan Hazle, https://www.youtube.com/watch?v=VtLpc_71vtA | largo, 1:09; 105.966 vistas; hace 10 años | Es el título más plano posible y sigue siendo el que se ve en búsqueda. 27 caracteres. Sirve de piso de claridad: gesto + objeto |
| 3 | Cassette adapters are remarkably simple | Technology Connections, https://www.youtube.com/watch?v=dH4n8fUjtLQ | largo, 9:32; 2.920.044 vistas; hace 6 años | Una afirmación con el objeto al inicio, sin pregunta. 39 caracteres. Otros títulos del canal en la misma búsqueda (por ejemplo «The VHS cassette was more clever than Beta») siguen la forma «objeto + juicio» |
| 4 | POV: It’s the #90s & you’re rewinding your cassette tape with a pencil. #nostalgia #90skids | MelissaKristinTV - DigitalMunchies, https://www.youtube.com/shorts/i3HdcjAVLbI | Short; 4,3 millones de vistas | Es el Short más visto de la búsqueda del casete y tiene 99 caracteres con dos hashtags dentro. Es un canal de nostalgia con gran alcance: no demuestra que los hashtags sirvan (2.2) |
| 5 | Rewinding a cassette tape with a pencil - it works! #80s #retro #80smusic #nostalgia #oldschool | Rerun the 80s, https://www.youtube.com/shorts/kHmq4pCyQ_4 | Short; 222 mil vistas | Misma lección que el anterior: títulos largos y llenos de hashtags son la norma del nicho en Shorts; el nuestro (48 caracteres, sin hashtags) se diferencia por claro |
| 6 | Animation vs. Math | Alan Becker, https://www.youtube.com/watch?v=B1J6Ou4q8vE | largo, 14:03; 168.391.667 vistas; hace 3 años | Muñecos de palitos y matemática: tres palabras, sin verbo. Muestra que un formato propio puede ser muy corto |
| 7 | Top Numbers to Survive a Zombie Apocalypse | Doodle Digest, https://www.youtube.com/watch?v=k4MwS_Dxhw0 | largo, 8:08; 189.901 vistas; hace 6 meses | **Doodle Digest existe** (la búsqueda del 2026-11-21 lo encontró; `publicacion.md` del casete decía que no se pudo encontrar). Es el canal que el `README` del canal dice que no hay que clonar. Su título repite una plantilla («Top X to Y»): aprendemos que una plantilla de título sostiene un canal, y que la nuestra tiene que ser propia |
| 8 | I Waited 13 Years for GTA 6: 4,811 Days in One Room. | Silent Timeline, https://www.youtube.com/watch?v=DZs_IPEqe7U | largo, 9:06; 242 vistas; hace 6 días | **Aviso para el video de GTA 6:** otro canal chico ya usa la misma cifra (4.811 días) en el título. No es un competidor que mueva el mercado (242 vistas), pero confirma que el tema se ve en la búsqueda del día y que nuestro título no debe llevar la cifra |

**Lo que no pude comprobar:** no hay un Short de 30 s «nostalgia con cálculo» entre los resultados de «cassette pencil rewind» que pueda servir de comparable por formato. Los Shorts de esa búsqueda son demostraciones del gesto, no cálculos.

### 4.b Para Tiky y Lumi (el adulto que busca para un niño de 1 a 3 años)

| # | Título tal cual | Canal y enlace | Formato y vistas (2026-11-21) | Qué se aprende |
|---|---|---|---|---|
| 1 | Learn To Wave With Miss Katie Toddler Learning Video | Miss Katie's Class- Toddler Learning Videos, https://www.youtube.com/watch?v=nX0F4gk1g3c | largo, 2:37; 162.236 vistas; hace 3 años | Verbo + gesto al inicio y la palabra del público («toddler») en el título: así busca el adulto en inglés. 52 caracteres. No copiamos «con [nombre del canal]» ni «Toddler Learning Video» |
| 2 | How to Teach Your Child to Wave Bye Bye | The SLP Mom, https://www.youtube.com/watch?v=7SUXoEhmNXM | largo, 6:43; 1.742 vistas; hace 2 años | Habla al adulto («your child») y es corto, 39 caracteres. Está escrito como instrucción al adulto: nuestro video no lo es (el título no debe prometer que enseña al adulto) |
| 3 | Learn How To Teach "Bye Bye Goodbye" \| Social Skills Lessons For Kids | Super Simple Learning, https://www.youtube.com/watch?v=YhvQoXdXpWw | largo, 3:17; 841.148 vistas; hace 7 años | Tiene barra vertical como separador y la palabra «lessons»; es un canal grande y establecido. Un ejemplo de lo que **no** hacemos (barra vertical como separador, 69 caracteres) aunque funcione para ellos |
| 4 | Hola, hola con las manos - Canción de SALUDO | Canta Maestra, https://www.youtube.com/watch?v=iC-9PKGI4Mk | largo, 1:54; 27.638.931 vistas; hace 3 años | 47 caracteres, la acción al inicio y la palabra «saludo» que usa el adulto en México. La palabra en mayúsculas y el emoji van contra Y3: se aprende la palabra, no el estilo |
| 5 | Hola hola ¿Cómo estás? La canción infantil para saludar (Preescolar) Saludar las manos | El Show De Pelina, https://www.youtube.com/watch?v=7wTkHmpDE9k | largo, 3:32; 122.131.856 vistas; hace 6 años | 86 caracteres con «saludar» dos veces. Es el video más visto de la búsqueda; muestra que la palabra «saludar» domina en español, pero repite palabras que para YouTube Kids serían relleno (Y18) |
| 6 | Oi e Tchau com a Tia Mary! Vamos Acenar? | Espacinho da Mary, https://www.youtube.com/watch?v=9w68IcGGG2A | Short, 0:30; 5.242.422 vistas; hace 5 meses | En portugués, «Oi e Tchau» y «Acenar» juntos. Prueba de que «acenar» existe en el mercado brasileño, pero acompañada de «tchau» |
| 7 | Quando os bebês começam a dar tchau? | PLOCPLAY, https://www.youtube.com/watch?v=QVx1vZMvZsI | Short, 0:55; 618 vistas; hace 3 años | Es una pregunta del adulto («cuándo empiezan los bebés a…»), no una acción del niño; así busca el adulto brasileño, pero esa promesa es de desarrollo (lenguaje médico para nosotros) |
| 8 | Wave Hello with Ms Rachel, now playing on Netflix! | Netflix Jr., https://www.youtube.com/watch?v=PMyCgujZkBk | largo, 1:08; 2.153.892 vistas; hace 1 año | La forma «Wave Hello with [nombre]» ya la usan otros (también «Wave Hello with Mimo»). Se aprende a no fijar nuestro Short de inglés con esa misma estructura |

## 5. La instrucción: cómo se escribe un título en este estudio

(Lista para pegarse en las definiciones de los agentes.)

1. El título le habla al **adulto o al espectador que elige**, no al niño. Dice lo que el video **de verdad** hace, en las palabras que ese público escribe en su mercado.
2. Antes de escribirlo, fija la **frase de búsqueda** (lo que se escribe, con su fuente y sin inventar volúmenes) y ponla **al inicio**, dentro de los primeros 40 caracteres.
3. Escribe **tres opciones**, de 30 a 50 caracteres (máximo 60; Shorts infantiles, máximo 50), con una de las fórmulas de la sección 3 de este documento. Se escribe **de nuevo en cada idioma**: no se traduce.
4. El título **no promete más de lo que el video da**: nada de «tu bebé hablará», «aprenderá rápido», lenguaje médico ni superlativos; nada de gancho (suspenso, «no te lo pierdas», «espera…»). El video cumple el título en sus primeros segundos.
5. **Sin MAYÚSCULAS TOTALES, sin emoji, sin hashtags, sin barra vertical ni corchetes.** Un solo «:». En títulos infantiles, sin «!».
6. **Nombres propios con mayúscula** («Tiky», «Lumi», «Tin & Tan»). Cifras con decimales o fracciones con «≈»; la cifra que es la respuesta del video no va en el título.
7. **Nada de marcas ni personajes de terceros** en el contenido infantil. En Tin & Tan, un producto ajeno solo si es el tema del video, con la línea «no afiliado» en la descripción.
8. **No se repite la palabra del público ni la palabra clave**; no se rellena con palabras populares (relleno de palabras clave).
9. Corre `revisar_texto.py` y `revisar_titulo.py` sobre las tres opciones y **escribe en la ficha el resultado y el recuento exacto de caracteres** (el filtro recalcula: no se cuenta a mano).
10. Elige una opción y deja **dos alternativas como reserva**: en este estudio no hay prueba A/B nativa (Shorts y «hecho para niños» no la admiten). No se cambia un título publicado antes de los 28 días y sin datos del canal.
11. La persona del equipo que firma comprueba **a mano** lo que la máquina no ve: que el video cumple el título, que no es engañoso y que pasa la línea editorial. Cualquier cambio dentro del video que pida un título lo deciden la pedagoga y la psicóloga.

## 6. El filtro (bloqueante)

> Desde el 2026-11-24, en `tin-y-tan` varias reglas de esta sección pasan de ERROR a AVISO: la tabla de «Parámetros flexibles (2026-11-24)», arriba, dice cuáles y por qué. Lo que sigue describe la versión 1.0, que es la que rige entera para `tiky-lumi` y la que devuelve `--estricto`.

Un título que no pasa el filtro no avanza a la ficha ni se publica. Dos partes: (a) lo que mide una máquina, con reglas exactas para `revisar_titulo.py`, y (b) lo que revisa una persona.

### 6.a Lo que mide la máquina (reglas para `revisar_titulo.py`)

**Entradas del script:** el título, `--canal` (`tin-y-tan` o `tiky-lumi`), `--idioma` (`en`, `es`, `pt-BR`), `--formato` (`short` o `largo`), la `frase_busqueda` y, de la ficha, las listas `respuesta_del_video` (cifras que son la respuesta), `marcas_de_terceros` y `cifras_aproximadas`. Lee el registro de títulos usados `video-studio/comercial/titulos_usados.json` (lo crea el script; lista con canal, idioma, título, fecha y video). Cada regla da **ERROR** (bloquea) o **AVISO** (se lee y se explica por escrito). Con 0 errores, el título pasa a la revisión humana.

**Perfiles de umbrales:**

| Parámetro | `tin-y-tan` Short (en) | `tiky-lumi` largo (es, en, pt-BR) | `tiky-lumi` Short (es, en, pt-BR) |
|---|---|---|---|
| Longitud mínima (caracteres) | 25 | 20 | 15 |
| Longitud máxima (caracteres) | 60 | 60 | 50 |
| Longitud recomendada (AVISO si queda fuera) | 30 a 50 | 35 a 50 | 25 a 40 |
| La frase de búsqueda termina antes del carácter | 40 | 45 | 40 |
| Palabras mínimas | 3 | 3 | 3 |
| Estilo de mayúsculas | Title Case | es y pt-BR: mayúscula de frase; en: Title Case | igual que el largo |
| Máximo de «!» | 1 | 0 | 0 |
| Máximo de «?» | 1 | 1 | 1 |
| Máximo de «:» | 1 | 1 | 1 |
| Máximo de paréntesis (pares) | 1 | 1 | 1 |
| Emoji | 0 | 0 | 0 |
| Hashtags en el título | 0 | 0 | 0 |
| Marcas de terceros | solo las de `marcas_de_terceros` | 0 | 0 |
| Cifras | permitidas; ver M12 | permitidas solo si son la edad entre paréntesis | igual |

**Reglas:**

| ID | Regla exacta | Tipo |
|---|---|---|
| M1 | Se cuenta en puntos de código Unicode con el texto normalizado a NFC. La longitud real debe estar entre el mínimo y el máximo del perfil. Fuera del rango recomendado: AVISO. La longitud real debe ser igual a la `caracteres` declarada en la ficha | ERROR (rango y coincidencia), AVISO (recomendada) |
| M2 | Sin espacios al inicio ni al final, sin espacios dobles, sin tabulaciones ni saltos de línea, sin punto final, sin terminar en «:» o «-», sin «...», sin signos repetidos («!!», «??», «?!»). Se permite terminar en «?» | ERROR |
| M3 | Conjunto de caracteres permitido: letras (con tildes, «ñ», «ç», «ã», «õ»), dígitos, espacio y `. , : ? ! ' ’ ( ) & ≈ – - " “ ” ¿ ¡`. Prohibidos: menor que, mayor que, barra vertical, corchetes, llaves, almohadilla, arroba, asterisco, guion bajo, tilde de «~», acento circunflejo, barra invertida y barra oblicua, emoji y emoticonos, y cualquier carácter de control | ERROR |
| M4 | **Frase de búsqueda:** el título normalizado (minúsculas, sin tildes, sin puntuación, espacios simples) contiene la frase normalizada completa, una sola vez, y esa frase termina antes del carácter de la tabla (40 o 45). La primera palabra de la frase empieza en el carácter 1 a 4 (la palabra puede ir precedida solo de «¿» o de comillas) **salvo** en las preguntas completas de Tin & Tan en las que la frase es el título entero | ERROR |
| M5 | **MAYÚSCULAS:** ninguna palabra de 2 o más letras, totalmente en mayúsculas, salvo las siglas de la lista `{GTA, VHS, CD, TV, DVD, AI, USA, UK, NES, PS5}` y solo en `tin-y-tan`. En `tiky-lumi`, cero palabras en mayúsculas. Más del 45 % de las letras en mayúscula: ERROR | ERROR |
| M6 | **Estilo de mayúsculas.** Inglés (Title Case): toda palabra empieza con mayúscula salvo `{a, an, the, and, but, or, nor, for, so, yet, at, by, in, of, on, to, up, as, vs, with, from}` (estas, en minúscula salvo al inicio o tras «:»; «with» y «from» se aceptan de las dos formas). Español y portugués: solo la primera palabra, la primera tras «:» o «?», los nombres de la lista de nombres propios y las siglas pueden empezar con mayúscula. Las demás, en minúscula | ERROR |
| M7 | **Nombres propios con mayúscula:** «Tiky», «Lumi», «Tin & Tan», «Tin and Tan», «Tin y Tan», «Tin e Tan», «Spike», más la lista de nombres de `glosario.txt`. Se busca sin distinguir mayúsculas y la forma escrita debe coincidir con la de la lista. «Tin», «Tan» y «Spike» sueltos dan AVISO (son palabras comunes en inglés), no error | ERROR («Tiky», «Lumi» y las parejas), AVISO (sueltos) |
| M8 | **Palabras y frases prohibidas** (comparación sin tildes ni mayúsculas, por palabra completa o frase): las listas de abajo, por idioma. Una coincidencia es ERROR | ERROR |
| M9 | **Relleno de palabras clave:** una palabra de 4 o más letras (que no sea de las palabras vacías del idioma) repetida 3 veces: ERROR; repetida 2 veces: AVISO (en `tiky-lumi`, también AVISO si la repite en otra forma, por ejemplo «saludar» y «saluda»). Más de 1 palabra de público («toddler», «baby», «kids», «bebé», «niños», «crianças») en `tiky-lumi`: ERROR | ERROR / AVISO |
| M10 | **Separadores:** en `tiky-lumi` no se admite « - » (guion con espacios) ni la barra vertical como separador; hasta 1 «:». El rango con «–» (por ejemplo «18–24») solo dentro del paréntesis de la edad | ERROR |
| M11 | **Marcas de terceros:** en `tiky-lumi`, 0: se comparan con la lista `marcas_ajenas` (Cocomelon, Peppa, Bluey, Pocoyo, Baby Shark, Ms Rachel, Miss Rachel, Disney, Mickey, Galinha Pintadinha, Mundo Bita y las que agregue el comercial) y con los nombres de canales de la sección 4. En `tin-y-tan`, una marca debe estar en `marcas_de_terceros` de la ficha, y entonces el script exige que la descripción contenga «Not affiliated with» (en), «Sin afiliación con» (es) o «Sem afiliação com» (pt-BR). Si el título trae «official», «leaked», «leak», «exclusive»: ERROR | ERROR |
| M12 | **Cifras:** (i) todo número con decimal («4.76», «4,76», «1.5») o fracción («1/2», «7/8») debe ir con «≈» delante («≈ 4.8»); (ii) «~», «about», «around», «almost», «casi», «cerca de», «unos» seguidos de cifra: ERROR (se usa «≈»); (iii) no se admite ninguna cifra que esté en `respuesta_del_video` de la ficha; (iv) separador de miles: inglés «,», español y portugués «.», decimal: inglés «.», español y portugués «,»; (v) en `tiky-lumi` las únicas cifras permitidas son las de la edad entre paréntesis, que deben coincidir con la `edad` de la ficha pedagógica | ERROR |
| M13 | **Duplicados:** se comparan con `titulos_usados.json`, en el mismo canal e idioma, sin tildes, sin mayúsculas y sin puntuación. Igual: ERROR. Parecido (`difflib.SequenceMatcher.ratio()`) de 0,90 o más: ERROR; de 0,80 a menos de 0,90: AVISO. Se comparan los títulos de **todos** los videos del canal, no solo los de la misma serie | ERROR / AVISO |
| M14 | **Nombres de canales ajenos de la lista de referencias** (sección 4): ninguno aparece en el título, y no se admite el título entero idéntico a uno de la sección 4 (ratio de 0,90 o más) | ERROR |
| M15 | `revisar_texto.py <título> --idioma` (en, es o pt, según el título) con 0 errores (ortografía, ¿? y ¡!, comillas, glifos). Cada AVISO se explica por escrito | ERROR |
| M16 | **Alternativas:** las dos alternativas pasan M1 a M15; cada una declara su `frase_busqueda` (la de la elegida o una variante escrita igual que en el título). La elegida no es idéntica a ninguna alternativa | ERROR |
| M17 | **Registro:** al terminar con 0 errores, el script añade el título al registro y escribe el resultado, la fecha y la versión del filtro en la ficha | — |

**Palabras y frases prohibidas por idioma** (lista inicial, en minúsculas; se amplía con el uso):

- **Inglés, ambos canales:** you won't believe, you wont believe, won't believe, shocking, shocked, insane, mind-blowing, mind blowing, gone wrong, must watch, must see, don't miss, dont miss, wait for it, watch till the end, watch until the end, secret, secrets, exposed, leaked, leak, official, exclusive, free, giveaway, subscribe, like and, click, viral, trending, best ever, number one, 100%, guaranteed, not clickbait, gender, woke.
- **Inglés, solo `tiky-lumi`:** cure, therapy, treatment, disorder, autism, autistic, adhd, delay, delayed, doctor, medical, genius, smarter, smart baby, iq, brain boost, brain development, will talk, will speak, talk faster, speak faster, learn fast, learn faster, in minutes, in days, scientifically, proven, surprise, challenge, prank, scary.
- **Español (`tiky-lumi`):** tu bebé hablará, hablará, habla más rápido, hablar más rápido, aprende rápido, aprenderá, garantizado, cura, terapia, tratamiento, trastorno, autismo, autista, tdah, retraso, médico, genio, más inteligente, coeficiente, cociente intelectual, desarrollo cerebral, científicamente, comprobado, sorpresa, reto, broma, susto, no te lo pierdas, increíble, impactante, no vas a creer, no creerás, secreto, final inesperado, gratis, suscríbete, dale like, viral, tendencia, oficial, el mejor, número 1, 100 %, género, ideología.
- **Portugués de Brasil (`tiky-lumi`):** seu bebê vai falar, vai falar, fala mais rápido, falar mais rápido, aprende rápido, garantido, cura, terapia, tratamento, transtorno, autismo, autista, tdah, atraso, médico, gênio, mais inteligente, qi, desenvolvimento cerebral, cientificamente, comprovado, surpresa, desafio, pegadinha, susto, não perca, incrível, chocante, você não vai acreditar, segredo, final inesperado, grátis, inscreva-se, curta, viral, tendência, oficial, o melhor, número 1, 100%, gênero, ideologia.

El origen de estas listas es [opinión mía], construida sobre las categorías oficiales de YouTube (Y6: engañoso, sensacionalista, «ruidoso»; Y17: clickbait malicioso; Y18: lo educativo engañoso y el relleno de palabras clave) y sobre la línea editorial del dueño (sin identidad de género; `series/granja/serie.md`). YouTube no publica una lista de palabras. «Gender» y «gênero» son línea editorial, no regla de la plataforma.

### 6.b Lo que revisa una persona (firma el comercial; la psicóloga puede vetar)

1. **El video cumple lo que el título promete**, mirando el video terminado, no el guion (Y5, Y8). Tin & Tan: si el título dice «How Many Turns?», el video calcula y responde. Tiky y Lumi: si el título dice «Saludar con la mano», el niño ve el gesto y tiene su pausa.
2. **No es engañoso** ni promete desarrollo («hablará», «aprenderá»), ni usa lenguaje médico, ni sugiere que el niño o el adulto «debe» algo (Y17, Y18).
3. **Pasa la línea editorial del dueño:** sin identidad de género ni ideología de género; Tiky es él y Lumi es ella; nada del contenido infantil se cruza con «M» ni con adultos.
4. **Es la palabra del mercado:** la frase de búsqueda es la que el adulto de ese mercado escribe (con su fuente). La palabra del gesto en cada idioma la confirma la pedagoga cuando cambia el objetivo (por ejemplo «hello» o «bye-bye»; en portugués, «oi» o «tchau», ver 3.b).
5. **Coincide con la miniatura y con los primeros segundos:** el fotograma elegido muestra lo que el título dice, sin texto que contradiga.
6. **Para niños:** ningún elemento del título presiona al niño o al adulto (nada de urgencia, culpa ni comparación), y nada que la psicóloga considere inadecuado. La psicóloga tiene veto.
7. **Para Tin & Tan:** la cifra del título, si la hay, coincide con la del video y con la descripción (`manual/12` §2.4), y no adelanta la respuesta.
8. **Dos pares de ojos:** el supervisor de continuidad vuelve a leer el título final (`manual/12` §1) y firma en `07_revision/controles.md`.

## 7. Qué va en la ficha

### 7.1 Bloque `titulo` en `publicacion.md` (uno por idioma)

```text
## Título (ficha)

- titulo_elegido: <texto exacto>
- caracteres: <número que calculó el filtro>
- idioma: <en | es | pt-BR>
- canal: <tin-y-tan | tiky-lumi>
- formato: <short | largo>
- publico: <quién elige el video, en una línea>
- frase_de_busqueda: <la frase escrita igual que en el título>
- fuente_de_la_frase: <enlace o «observación en YouTube, fecha»; volumen: sin dato>
- formula: <F1 | F2 | F3 de la sección 3 de titulos.md>
- alternativa_1: <texto> (<caracteres>)
- alternativa_2: <texto> (<caracteres>)
- uso_de_las_alternativas: reserva; no hay prueba A/B nativa en Shorts ni en «hecho para niños» (YouTube, https://support.google.com/youtube/answer/16391400?hl=en)
- filtro: version <n>, fecha <AAAA-MM-DD>, resultado <PASA | NO PASA>, errores <lista o ninguno>, avisos <lista y cómo se resolvió>
- revision_humana: video cumple el título <sí | no>; no engañoso <sí | no>; línea editorial <sí | no>; firma <nombre>, fecha <AAAA-MM-DD>
- medicion: <largo: CTR de impresiones y fuente de tráfico búsqueda | short: visto frente a deslizado y mostrado en el feed>, a 7 y 28 días; meta: establecer línea base
```

### 7.2 Bloque en `ficha.json` y `ficha_publicador.json`

**Aviso de compatibilidad:** en el `ficha.json` y en el `ficha_publicador.json` actuales (ejemplo: `TIN-EN-S-001`) la clave `titulo` ya existe y es **una cadena** con el título; el publicador la lee. Para no romperla, el bloque nuevo se llama **`titulo_ficha`** (objeto) y `titulo` sigue siendo la cadena, que debe ser igual a `titulo_ficha.elegido`. Si el dueño o el equipo prefieren que el objeto se llame `titulo`, hay que cambiar el publicador.

```json
"titulo_ficha": {
  "elegido": "",
  "caracteres": 0,
  "idioma": "",
  "canal": "",
  "formato": "",
  "publico": "",
  "frase_de_busqueda": "",
  "fuente_de_la_frase": "",
  "formula": "",
  "alternativas": [
    {"texto": "", "caracteres": 0},
    {"texto": "", "caracteres": 0}
  ],
  "uso_de_las_alternativas": "reserva; sin prueba A/B nativa en Shorts ni en hecho para niños",
  "filtro": {"version": 0, "fecha": "", "resultado": "", "errores": [], "avisos": []},
  "revision_humana": {"video_cumple_el_titulo": false, "no_enganoso": false, "linea_editorial": false, "firma": "", "fecha": ""},
  "medicion": {
    "formato_largo": ["ctr_de_impresiones", "impresiones", "fuente_de_trafico_busqueda", "terminos_de_busqueda"],
    "formato_short": ["visto_frente_a_deslizado", "mostrado_en_el_feed", "fuente_de_trafico_busqueda"],
    "plazos_dias": [7, 28],
    "meta": "establecer línea base"
  }
}
```

### 7.3 Cómo se mide si el título funcionó (para «Metas después de publicar»)

| Indicador | Formato | Meta | De dónde sale la meta | Dónde se lee |
|---|---|---|---|---|
| Porcentaje de clics de las impresiones (título y miniatura) | largo (capítulo de Tiky y Lumi) | establecer línea base | Canal nuevo, sin historial: sin dato. Referencia de YouTube, no meta: la mitad de los videos está entre 2 % y 10 % (Y12) | YouTube Studio, Analytics, pestaña Alcance (Reach). No se mira en las primeras horas |
| Visto frente a deslizado, y «Shown in feed» | Short | establecer línea base | Canal nuevo: sin dato | YouTube Studio, Analytics de Shorts; en esa página figura como «How many chose to view» (Y20) |
| Fuente de tráfico «búsqueda de YouTube» y términos de búsqueda | ambos | establecer línea base | Sin historial | YouTube Studio, Analytics, Alcance, «Tipos de fuente de tráfico» y el informe «Cómo encuentran tu video» (Y16) |
| Duración media de visualización | ambos | establecer línea base | Sin historial | Analytics, pestaña Interacción. Sirve para detectar si el título promete de más: CTR alto con duración baja es la señal de clickbait según YouTube (Y10) |

**Regla de lectura:** el título solo se juzga después de 28 días y con impresiones suficientes; YouTube pide no decidir con pocos datos ni por variaciones chicas de CTR (Y12) y recomienda no tocar lo que funciona (Y11). Un cambio de título en un video ya publicado se anota con su fecha y se lee como un nuevo punto de partida.

### 7.4 Fila nueva para la sección «Comercial e inteligencia digital» de cada `ficha_tecnica.md`

Formato estricto: 8 columnas, sin «|» ni corchetes dentro de las celdas. El número de criterio es el siguiente libre de cada ficha.

```text
| C7 | El título pasa el filtro de títulos | revisar_titulo.py termina con 0 errores, cada aviso está explicado, y el bloque titulo de la ficha está lleno con el recuento de caracteres que calculó el filtro; la revisión humana firmada dice que el video cumple lo que el título promete y que no es engañoso | Paquete, bloque titulo en publicacion.md y ficha.json | 3 | sí | | |
```

(El criterio C4 de `hola_granja`, «El título lleva la búsqueda principal al inicio y no promete de más», se sustituye por este o queda como su resumen humano.)

## 8. Aplicación a los títulos que ya tenemos

Conté los caracteres con Python (puntos de código Unicode). **Los recuentos que declaran hoy algunos paquetes no coinciden con el real** (regla M1): lo corrijo aquí; no toco esos archivos.

### 8.1 Hola, granja (capítulo 16:9, hecho para niños, `tiky-lumi`)

Perfil: capítulo, mínimo 20, máximo 60, frase termina antes del carácter 45.

| Idioma | Título | Declarado | Real | Veredicto del filtro |
|---|---|---|---|---|
| es (recomendado) | Saludar con la mano: Hola, granja con Tiky y Lumi | 49 | 49 | **PASA.** Frase «saludar con la mano» en los caracteres 1 a 19. Mayúscula de frase correcta; un «:» y una «,»; sin repeticiones ni palabras prohibidas |
| es (alt. 1) | Saluda con la mano (18 a 24 meses): Hola, granja | 48 | 48 | **NO PASA M4** si la frase de la ficha es «saludar con la mano» (aquí dice «saluda»). Se arregla declarando la variante como su propia frase; la edad coincide con la ficha pedagógica. |
| es (alt. 2) | Saludar con la mano: Tiky y Lumi en la granja | 45 | 45 | **PASA** |
| en (recomendado) | Wave Hello: Hello, Farm with Tiky and Lumi | 44 | **42** | **PASA con AVISO M9** («Hello» dos veces: la frase «Wave Hello» y el nombre del capítulo «Hello, Farm»). Mejor leerlo como relleno suave. **Qué cambiaría:** nada es obligatorio, pero una opción de reserva como «Wave Hello: Tiky and Lumi on the Farm» evita la repetición |
| en (alt. 1) | Wave Hello (Ages 18–24 Months): Hello, Farm | 43 | 43 | **PASA con AVISO M9** (misma repetición) |
| en (alt. 2) | Wave Hello: Tiky and Lumi on the Farm | 38 | **37** | **PASA.** Es la que menos repite; la sugiero como principal para inglés (opinión mía), a decidir por el equipo |
| pt-BR (recomendado) | Acenar com a mãozinha: Oi, fazenda com Tiky e Lumi | 53 | **50** | **PASA** mecánicamente. Pendiente de revisión humana: la palabra de búsqueda («acenar») frente a «dar tchau» y «oi e tchau» (3.b); no la cambio sin decisión y sin pedagoga |
| pt-BR (alt. 1) | Acenar e dizer oi (18 a 24 meses): Oi, fazenda | 46 | 46 | **PASA con AVISO M9** («oi» dos veces) |
| pt-BR (alt. 2) | Acenar com a mãozinha: Tiky e Lumi na fazenda | 51 | **45** | **PASA** |

**Cambios que propongo, todos dentro del paquete (no tocan el video):** (1) corregir los recuentos del paquete en inglés y portugués; (2) en inglés, considerar «Wave Hello: Tiky and Lumi on the Farm» como título principal por no repetir «Hello»; (3) en portugués, que la pedagoga confirme la palabra del gesto de llegada antes de publicar. No hay propuesta de cambio dentro del video.

**Shorts derivados** (títulos sugeridos en los paquetes en/pt-BR): «Wave Hello with Tiky» (20), «Wave Hello with Lumi» (20), «Tiky Waves to Lumi» (18) y «Acenar com o Tiky» (17), «Acenar com a Lumi», «Tiky acena para a Lumi». En español: «Saluda con la mano con Tiky» (27; la frase de la ficha no coincide, mismo arreglo que arriba). **Pasan el rango.** AVISO de observación (sin regla): «Wave Hello with [nombre]» es la misma forma que usan títulos ajenos (sección 4.b, 8), que no pasan M14 por el título entero pero sí comparten la estructura. No lo decido ahora: se revisa cuando exista el guion de cada Short.

### 8.2 Casete y lápiz (`tin-y-tan`, Short, ya entregado y cerrado por el dueño)

«Rewind a Cassette With a Pencil: How Many Turns?» (48 caracteres, coincide con lo declarado).

- **Veredicto: PASA.** Frase «rewind a cassette with a pencil» termina en el carácter 31 (antes del 40); Title Case correcto («With» se acepta de las dos formas); un «:» y un «?»; sin cifras, sin marcas, sin hashtags ni emoji; no repite palabras.
- **Solo anoto, no propongo rehacer:** (1) en la búsqueda pública del 2026-11-21 ya aparece un Short con exactamente ese título en el canal «Tin y Tan» (@TinandTan), con 3 vistas, es decir, **el Short parece estar ya publicado**; el nombre que muestra YouTube es «Tin y Tan», y el `README` del canal dice «Tin & Tan» (`manual/12` §1.4 acepta ambas escrituras como nombre propio). Confirmarlo es cosa del dueño. (2) Es la pregunta sin respuesta, que es lo que decidió el dueño; los estudios sobre las preguntas no son concluyentes (2.2).

### 8.3 GTA 6 (`tin-y-tan`, Short; título en `prompt.md` §8)

«How many days did we wait for GTA 6?» (36 caracteres).

- **Veredicto: NO PASA (un error de estilo).** M6: en inglés el canal usa Title Case y este título está en minúsculas de frase.
- **Cómo se arregla:** «How Many Days Did We Wait for GTA 6?» (36 caracteres). Con eso pasa M1 a M16: la frase de búsqueda «how many days did we wait for gta 6» es el título entero y termina en el carácter 36, antes del 40; «GTA» está en la lista de siglas; un «?»; sin la cifra (4.811 está en la descripción, no en el título, y `respuesta_del_video` la lista); sin repeticiones.
- **Marca de tercero:** «GTA 6» es el tema del video. La ficha debe listarla en `marcas_de_terceros` y la descripción ya trae «Not affiliated with Rockstar Games or Take-Two Interactive» (cumple M11).
- **Revisión humana pendiente:** que el video responda la pregunta (4.811 días) y que el dato del 19 de noviembre de 2026 se confirme antes de publicar (el propio prompt dice que la fecha de GTA 6 no se leyó en el sitio de la editora).
- **Observación:** otro canal pequeño publicó «I Waited 13 Years for GTA 6: 4,811 Days in One Room.» (sección 4.a, 8). No afecta al título nuestro, que no lleva la cifra. Es una señal más de que no conviene adelantarla.
- **Propuesta:** como el título está en `prompt.md` y no en una ficha de publicación, y yo no toco el prompt, el cambio de mayúsculas se lo propongo al director-de-prompts para que lo aplique cuando se abra la ficha de publicación.

## 9. Lo que no se pudo conseguir, y qué lo resolvería

| Qué faltó | Por qué | Qué lo resolvería |
|---|---|---|
| El texto completo de los estudios de terceros (Backlinko, Briggsby, AIR Media Tech, Returbe, OutlierKit, OverseerOS, ytgrowth, Creaticalc, vidIQ, Tunepocket, Pew) | **Hosts bloqueados o fuera de la lista permitida.** `backlinko.com`, `vidiq.com`, `www.tubebuddy.com` y `www.semrush.com` respondieron «CONNECT tunnel failed, response 403». No probé los demás (fuera de la lista) ni usé otra vía | Que la conversación principal pida permiso para: `backlinko.com`, `vidiq.com`, `air.io`, `returbe.com`, `outlierkit.com`, `www.overseeros.com`, `ytgrowth.io`, `creaticalc.com`, `www.briggsby.com`, `www.tunepocket.com`, `www.pewresearch.org`. Mientras tanto toda cifra de la sección 2 queda como «visto en resumen de buscador» |
| Longitud de título visible en el celular (Inicio, búsqueda, feed de Shorts) | YouTube no la publica; los terceros se contradicen (≈ 40, ≈ 50, 45 a 55 y hasta 80 con dos líneas) | Medirlo en un celular real con el título ya subido en privado (captura de pantalla de cada superficie), y guardarlo en `video-studio/estadisticas/datos/` |
| Si el título de un Short se ve en el feed de Shorts, y cuántos caracteres | Fuentes de terceros contradictorias | El mismo método: captura en un celular con un Short propio |
| Límite actual de caracteres de la descripción de TikTok y peso de las palabras en su búsqueda; texto de la ayuda de búsqueda de TikTok | `support.tiktok.com` devuelve solo la cáscara de la página (se arma con JavaScript) | Que el dueño abra la página y pegue el texto, o permiso para una herramienta de lectura que ejecute JavaScript |
| Longitud visible del pie de foto de Instagram, y si la búsqueda por palabras clave ya funciona en español y portugués | La página oficial de búsqueda es de 2021 y solo habla de inglés; `help.instagram.com` devuelve la cáscara vacía (comprobado en la base, 2026-11-20) | Mismo recurso: texto pegado por el dueño |
| Volúmenes de búsqueda de cada frase (saludar con la mano, wave hello, acenar, dar tchau…) | No hay herramienta de volumen en los sitios permitidos; `trends.google.com` respondió «429» (límite de peticiones) al probarlo una vez, y no insistí | Tendencias de Google con consultas espaciadas, o el informe «Búsqueda de YouTube» del propio canal cuando tenga historial, o una herramienta de palabras clave que elija el dueño |
| Cómo busca un adulto con un niño de 1 a 3 años (estudios de comportamiento) | No encontré ningún estudio específico; solo la regla de YouTube sobre contenido infantil | Los datos del propio canal («Cómo encuentran tu video», términos de búsqueda). En un canal «hecho para niños» no sé si la pestaña de investigación de Analytics está disponible: sin verificar |
| Datos del propio canal (impresiones, CTR, visto frente a deslizado, fuentes de tráfico) | El canal de Tiky y Lumi es nuevo y sin videos; el de Tin & Tan tiene un Short con 3 vistas visibles | La exportación de YouTube Studio a los 7 y 28 días en `video-studio/estadisticas/datos/` (las estadísticas no se suben al repositorio, el repo es público) |
| Si YouTube cambia el ajuste «hecho para niños» de un canal que muestra personajes animados, y qué hace eso con las funciones de Tin & Tan | Está en `base_conocimiento.md` §5: YouTube puede cambiar el ajuste por su cuenta | Se detecta si desaparecen los comentarios del Short; lo decide el dueño |
| Una regla de YouTube sobre nombrar productos de terceros en el título | La política de spam y la de suplantación no la tienen; la búsqueda del 2026-11-21 no encontró otra | Una consulta al soporte de YouTube, o la decisión del dueño con la prudencia de 3.a |

**Qué cambia cuando lleguen los datos:** las metas de la sección 7.3 pasan de «establecer línea base» a un valor, solo con datos del propio canal; los umbrales del filtro (longitud, frase en los primeros 40 caracteres) se ajustan con las capturas del celular; y la regla de cero emoji se reabre para Tin & Tan si una prueba con un Short lo justifica.
