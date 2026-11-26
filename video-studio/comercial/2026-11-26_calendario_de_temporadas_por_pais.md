# Calendario de temporadas, feriados y fechas de alto interés por país (2026-12-01 a 2027-03-31, con esquema de 12 meses)

- **Autor:** comercial-inteligencia-digital
- **Fecha de elaboración y de lectura de todas las páginas:** 2026-11-26 (jueves; faltan 5 días para diciembre)
- **Canal:** Tin & Tan (`@TinandTan`), Shorts verticales en inglés. Formato de peleas de datos (`canales/nostalgia-tin-y-tan/PARAMETROS.md`, versión 2.1).
- **Pedido del dueño (2026-11-26), textual:** «Incluye a las consideraciones para contrastar con las estadísticas las temporadas; por ejemplo, estamos a 5 días de comenzar diciembre, y así sucesivamente cada temporada según los países que más estén viendo los videos; temporadas o feriados; revisa históricos para poder contrastar».
- **Para qué sirve:** que el equipo planee tandas de 15 días a un mes (requisito A13 de `PARAMETROS.md`) sabiendo qué fechas caen, de qué países son, con cuánta antelación se publicó lo que más vistas tuvo en temporadas pasadas y qué preguntas escribe hoy la gente.
- **Qué no es:** no es guion, ni prompt, ni título. Ningún título se propone aquí; cuando una fecha se convierta en video, el título sigue `comercial/titulos.md` sección 5 y pasa `revisar_titulo.py` con 0 errores.
- **Marcas de fiabilidad:** «leído» = abrí la página con `curl`; «resumen» = solo vi el resumen del buscador (la página no abrió); «sin confirmar» = una sola fuente o fuentes que se contradicen; «sin dato» = no lo conseguí; «derivado» = lo calculé y la cuenta está a la vista. Las cifras con «≈» son aproximadas o redondeadas por mí.
- **Propuestas para la pedagoga y la psicóloga:** ninguna. Es contenido de adultos y adolescentes; no entra Tiky y Lumi.

---

## Estadísticas en que se basa

Regla del dueño (2026-11-26): ningún prompt sin estadísticas. Este calendario no escribe prompts, pero decide qué fechas se miran, y por eso parte de dos tipos de dato. Las cifras del Studio no se copian aquí porque el archivo no se sube al repositorio público; van en palabras.

**1. Lo que el canal mide de verdad** (YouTube Studio, lectura de Keter del 2026-11-26 por la mañana, en `video-studio/estadisticas/datos/2026-11-26_studio_tin_y_tan.md`):

- **Países del público, por orden:** Estados Unidos (muy por delante), Filipinas, India, El Salvador, Indonesia y Canadá. Filipinas queda claramente segunda; del tercer lugar al sexto la diferencia es pequeña y el orden entre ellos puede cambiar con un solo video. Canadá se conoce por un video y por el orden que dio el dueño; no aparece en el total del canal.
- **Edad y género:** casi todo el público es menor de 45 años; hay mayoría de hombres; el tramo de 13 a 17 es de los más grandes. No hay público de 55 o más.
- **Cómo llegan:** casi todo el tráfico llega del feed de Shorts. La búsqueda de YouTube es marginal y los términos que dejó no guardan relación con los videos. Por eso una fecha no se elige por «lo que la gente busca» sino por lo que el feed reparte: el calendario es un indicio de qué temas tendrán atención en cada semana, no una promesa de tráfico.
- **Muestra:** solo dos videos con datos suficientes (el primero pasó de 500 vistas; el segundo, de 1.000 y poco). Ningún suscriptor. El peso de Estados Unidos cambió mucho entre los dos videos: en uno dominó y en el otro quedó al nivel de El Salvador y Filipinas. Eso significa que el país **no está estabilizado**: es una señal, no una prueba.
- **Sin dato en Studio:** hora del público, qué más mira, retención por país, impresiones y porcentaje de clics de Shorts. La gran mayoría de las vistas fue sin subtítulos activados.
- Lo que `PARAMETROS.md` v2.1 ya dice y este documento respeta: público a prueba de 13 a 44 años con Estados Unidos primero; tema por demanda verificable, sin cupos por tipo de tema; cadencia de partida de 3 por semana; títulos medidos solo por «se quedó a mirar».

**2. Lo que medí hoy en YouTube, con páginas abiertas** (2026-11-26; método de `estudios/2026-11-26_accion_stickman_y_tin_y_tan.md`, sección 2):

- **Históricos:** primera página de los listados `https://www.youtube.com/results?search_query=<texto>&hl=en&gl=<país>` (EE. UU., India, Filipinas, Indonesia) y fecha de cada Short en `https://www.youtube.com/shorts/<id>`. 38 eventos de temporadas pasadas con 2 a 4 consultas cada uno (sección 2 de este archivo).
- **Preguntas actuales:** autocompletado `https://www.youtube.com/complete/search?client=youtube&ds=yt&hl=en&gl=<país>&q=<texto>` en EE. UU., Filipinas, India, Indonesia, El Salvador (en inglés y en español) y Canadá.
- **Límite que se repite en cada fila:** el autocompletado **no da volumen**. Dice qué se escribe, no cuánta gente lo escribe. Además, cuando escribo una frase completa, YouTube la devuelve como primera sugerencia aunque nadie la busque; por eso solo cuento como «se escribe» lo que el autocompletado **añade** a un inicio parcial. La lección del 2026-11-26 sobre el short 4 (existir en el autocompletado no es pesar en Trends) sigue vigente: nada de este archivo prueba volumen.

**3. Fechas:** calendarios abiertos (timeanddate, Wikipedia en inglés) y resúmenes de buscador para fechas de 2027 que dependen de comunicados (sección «Fuentes»). Las fuentes oficiales que no abrieron están listadas al final.

**Lo que cambia en el radar.** El calendario de `radar_de_tendencias.md` (sección 3) se hizo para EE. UU., Brasil y México. El Studio dice otra cosa: Brasil y México no aparecen entre los primeros países del público. **Desde hoy los países del calendario son los del Studio:** Estados Unidos, Filipinas, India, El Salvador, Indonesia y Canadá. Las filas de Brasil y México del radar (Carnaval, Día de Reyes, Día del Niño, Día de las Madres, Copa Libertadores) quedan como registro y no se planean.

---

## 1. Cómo se leyó y qué límites tiene

1. **Muestra:** primera página del listado de YouTube por relevancia, no una muestra aleatoria. Los ceros reales no aparecen. Los Shorts que listo son los de más vistas **del propio listado**.
2. **Vistas acumuladas:** son las de hoy (2026-11-26). Un Short de hace once meses ha tenido once meses para sumar; eso favorece a los antiguos. La antelación que mido dice **cuándo se publicó lo que más vistas acumuló**, no cuándo rinde mejor un canal sin suscriptores (sin dato).
3. **Quiénes son:** casi todos son canales grandes y de tipo reacción, meme, estado de WhatsApp o clip; pocos son explicativos con datos. No sé cuántos eran explicativos; lo clasifico por título.
4. **Fecha del evento pasado:** tomada de Wikipedia o timeanddate cuando abrieron; si no, va marcada «sf» (sin fuente abierta) y coincide con la fecha de los Shorts del propio día.
5. **Convención:** antelación = fecha del Short menos fecha del evento, en días. **Negativo = antes; positivo = después.** Se mide mediana y rango del grupo de Shorts del tema con más vistas dentro de una ventana de 60 días antes a 30 días después (salvo que se diga otra).
6. No se vio el contenido de ningún video.

---

## 2. Históricos medidos: con cuánta antelación se publicó lo que más vistas tuvo

Todas las lecturas son del 2026-11-26. «n» es el número de Shorts del tema que pasaron el umbral de vistas indicado dentro de la ventana. Consultas exactas en la sección «Fuentes», F34.

| ID | Evento pasado (fecha) | Listado | n y umbral | Mediana y rango (días) | Qué muestran los de más vistas |
|---|---|---|---|---|---|
| H1 | The Game Awards 2025 (2025-12-11; Wikipedia, leída) | EE. UU. | 11 de ≥ 430.000 | 0; de −24 a +24 | **Dos oleadas.** Antes: a −24, −23 y −16 días (nominados y predicciones: ≈ 610.000, ≈ 954.000 y ≈ 11 millones; los Shorts de nominados llevan fecha 2025-11-17, 24 días antes; sin fuente abierta de ese anuncio) y a −2 («quién gana»: ≈ 430.000). Día del evento y después: 0 a +2 (memes y resultados: ≈ 4,8 millones, ≈ 2,4 millones, ≈ 2,2 millones) |
| H2 | Final de *Stranger Things* 5 (2025-12-31, sf) | EE. UU. | 11 de ≥ 1 millón | +1; de 0 a +33 | Casi todo en 0 a +2; el más visto (≈ 32 millones) llegó a +13 con una teoría del final |
| H3 | Super Bowl LX (2026-02-08; Wikipedia, leída) | EE. UU. | 8 de ≥ 500.000 | 0; de −2 a +8 | Medio tiempo y resultado el mismo día. Aparte, el anuncio del artista del medio tiempo (2025-09-28) dio dos Shorts de ≈ 1 millón y ≈ 516.000 a unos −132 días |
| H4 | Óscar 98.ª (2026-03-15; Wikipedia, leída) | EE. UU. | 3 de ≥ 500.000 | +1; de 0 a +1 | Resultados y momentos de la gala |
| H5 | Golden Globes 2026 (2026-01-11, sf) | EE. UU. | 4 de ≥ 800.000 | +1; de 0 a +3 | Alfombra y presentadores |
| H6 | Grammys 2026 (2026-02-01, sf) | EE. UU. | 5 de ≥ 800.000 | 0; de −2 a +1 | Ganadores y discursos |
| H7 | Juegos Olímpicos de Invierno 2026 (inicio 2026-02-06, sf) | EE. UU. | 8 de ≥ ≈ 2,8 millones | +10; de −1 a +19 | Evento largo: lo más visto salió **durante** (+6 a +13). El único previo («cómo prepararse», ≈ 15 millones, a −1) fue un encargo de YouTube |
| H8 | Año Nuevo 2026 (2026-01-01) | EE. UU. | 7 de ≥ 5 millones, de −60 a +30 | −2; de −30 a 0 | Cuenta atrás, meme y «adiós a 2025»: la mayoría en la última semana, uno a −30 |
| H9 | Halloween 2026 (2026-10-31) | EE. UU. | 5 de ≥ 700.000, de −60 a 0 | −5; de −26 a −2 | Disfraces y bromas; ola de 1 a 4 semanas antes |
| H10 | Acción de Gracias 2026 (2026-11-26) | EE. UU. | 4 de ≥ 300.000 | −2; de −3 a −2 | Humor familiar; todos a 2 o 3 días |
| H11 | Lanzamiento de GTA VI (2026-11-19; radar) | EE. UU. | 12 de ≥ ≈ 1,9 millones | +2; de −1 a +5 | Reacciones de streamers y escenas; mayoría después del lanzamiento |
| H12 | Ramadán 2026 (inicio 2026-02-18; Wikipedia «Ramadan», leída) | EE. UU. e Indonesia | 7 de ≥ 1,8 millones | −4; de −20 a +2 | Cuentas atrás y «primer día». Además, Shorts de «cuántos días faltan» publicados de 114 a 252 días antes con ≈ 1 a 5 millones (un meme de ≈ 102 millones a −337 días no es de cuenta atrás y no cuenta) |
| H13 | Lebaran/Idul Fitri 2026 (fecha usada 2026-03-20, inicio de vacaciones; feriado 2026-03-21; timeanddate) | Indonesia | 5 de ≥ 800.000 | −2; de −9 a +16 | Mudik y saludos. Además tres Shorts de ≈ 0,8 a 1,7 millones publicados de 113 a 335 días antes sobre «cuándo cae» |
| H14 | Año Nuevo Lunar 2026 (2026-02-17) | EE. UU. e Indonesia | 1 de ≥ 30 millones | −2 | Un solo Short enorme (consejo de «guardar»); el resto de EE. UU. ≤ ≈ 71.000 y el de Indonesia ≈ 1 millón como máximo |
| H15 | Diwali 2026 (2026-11-08; timeanddate) | India | 8 de ≥ 3 millones | −14; de −33 a −1 | Petardos y tendencias: la ola empieza 1 a 5 semanas antes |
| H16 | Makar Sankranti y Pongal 2026 (2026-01-14) | India | 4 de ≥ 1,7 millones | −1,5; de −6 a +3 | Cometas y celebraciones |
| H17 | Día de la República 2026 (2026-01-26) | India | 5 de ≥ 300.000 | −1; de −6 a 0 | Ensayo del desfile y estados de WhatsApp |
| H18 | IPL 2026 (inicio 2026-03-28; Wikipedia, leída) | India | 10 de ≥ 600.000, de 0 a +94 | +45; de 0 a +94 | **Durante la temporada** (mejor momento: +12 a +71). Aparte, contenido de subasta y traspasos publicado de 175 a 282 días antes: ≈ 0,5 a 1,4 millones |
| H19 | Mundial T20 2026 (inicio 2026-02-07, sf) | India | 4 de ≥ 1,6 millones | +27,5; de +15 a +35 | Semifinal y final. Dos Shorts de calendario y sedes publicados a −130 y −111: ≈ 2,3 y ≈ 1,2 millones |
| H20 | Simbang Gabi 2025 (inicio 2025-12-16; Wikipedia, leída) | Filipinas | Shorts del tema | todos ≤ ≈ 25.000 | «Christmas in the Philippines» de viajeros: ≈ 450.000 (+5) y ≈ 243.000 (+9); ninguno explicativo |
| H21 | Traslación del Nazareno 2026 (2026-01-09; Wikipedia, leída) | Filipinas | 1 de ≥ 1 millón | +1 | Un Short de un famoso (≈ 1,6 millones); el resto ≤ ≈ 68.000 |
| H22 | Sinulog 2026 (2026-01-18) | Filipinas | máximo ≈ 135.000 | de −9 a +6 | Desfiles y contingentes |
| H23 | March Madness 2026 (primera ronda 2026-03-19, sf) | EE. UU. | 3 de ≥ 500.000 | +11; de +3 a +13 | Durante el torneo |
| H24 | Pascua 2026 (2026-04-05) | EE. UU. | lo más visto en la ventana ≈ 286.000 | −17 | Demanda baja; los de más vistas son de años anteriores |
| H25 | MLK Day 2026 (2026-01-19; timeanddate) | EE. UU. | 1 de ≈ 5,2 millones | −1 | Un saludo; el resto es de años anteriores y llega a ≈ 155.000 |
| H26 | *Avatar: Fire and Ash* (estreno 2025-12-19, sf) | EE. UU. | 4 de ≥ 700.000, de 0 a +30 | +15,5; de +3 a +26 | Reparto y detrás de cámaras después del estreno; antes, ≈ 2 millones (a −67) y ≈ 1,8 millones (a −143) |
| H27 | Navidad 2025 (EE. UU.) | EE. UU. | — | sin dato | Dos consultas no devolvieron Shorts. No se mide |
| H28 | Día de Pokémon 2026 (2026-02-27) | EE. UU. | — | sin dato | Tres consultas no devolvieron Shorts. No se mide |
| H29 | Black Friday 2026 (2026-11-27) | EE. UU. | máximo ≈ 148.000 | −2 | Ofertas; es compra y rinde poco |

### 2.1 Cuatro patrones que se repiten

1. **Eventos con resultado y día fijo** (premios, finales, el Super Bowl, el lanzamiento de un juego): lo más visto sale **el día y los tres días siguientes** (mediana 0 a +2 en H1 a H6 y H11). Antes del evento hay una oleada menor de predicciones y nominaciones (H1: de −24 a −16 días) y otra a −2.
2. **Fiestas y cuentas atrás** (Año Nuevo, Halloween, Acción de Gracias, Diwali, Ramadán, Lebaran): lo más visto sale entre **−14 y −1 días**, con mediana de −2 a −5 en casi todas y −14 en Diwali, que es una fiesta que exige comprar y preparar.
3. **Eventos largos** (Juegos Olímpicos, IPL, Mundial T20, March Madness): lo más visto sale **durante**, de +3 a +71 días después del inicio (H7, H18, H19, H23).
4. **«¿Cuándo cae?» con meses de antelación:** para Ramadán y Lebaran existen Shorts de ≈ 0,8 a 5 millones publicados de 113 a 335 días antes (H12, H13). Es una pregunta de calendario que no caduca, pero no es una prueba de que un canal pequeño la gane.

### 2.2 Regla de antelación que propongo (opinión mía, con los datos de arriba)

| Tipo de fecha | Cuándo publicar | Por qué | Límite |
|---|---|---|---|
| A. Resultado con día fijo (premios, finales, estrenos grandes, Super Bowl) | **Una pieza de datos que no depende del resultado, de −7 a −2 días; y, si el equipo puede, una del resultado en las 72 horas posteriores (día 0 a +3)** | H1: la oleada previa existe y el pico es 0 a +2; la regla de «lo que ya pasó se hace ya» del radar | Producir el resultado en 72 horas es lo que el radar llama «ya»; no sé si el estudio llega. Si no llega, solo la pieza previa |
| B. Fiesta o cuenta atrás | **De −7 a −3 días** como punto de partida; última oportunidad −2 | Las medianas de H8 a H17 están entre −1 y −5; el −7 deja margen de revisión | Los datos miden cuándo publicaron los canales grandes. Si un canal de cero suscriptores rinde mejor antes o después: sin dato |
| C. Evento largo | **Una pieza a −30 a −7 sobre el calendario o el formato del torneo, y piezas durante (+3 a +35)** | H7, H18, H19, H23 | Requiere producir durante el torneo, no solo antes |
| D. Fecha que la gente pregunta con meses de antelación (Ramadán, Lebaran, Año Nuevo Lunar) | **Se puede publicar de −120 a −14 días** si la pieza es «cuándo cae y por qué cambia cada año» | H12, H13 | Puede morir en una semana si el feed no la reparte; lo decide la medición, no esta regla |

**Producción:** la regla del radar es empezar un Short **10 días antes** de la fecha de publicación (estimación del radar, no medida). Para publicar el 2026-12-14 hay que empezar el 2026-12-04.

---

## 3. Tabla maestra por fecha (2026-12-01 a 2027-03-31)

**Cómo se lee.** «Fuente» usa los códigos F1 a F39 de la sección 10, con cuántas fuentes sostienen la fecha. «Antelación medida» remite a la sección 2. «Preguntas que se escriben» son las que el autocompletado **añade** a un inicio parcial (país entre paréntesis); no dan volumen. «Encaje» responde al filtro del radar (sección 2): demanda, hechos comprobables, apto para 13 a 17, sin personas reales golpeadas, marcas solo nombradas, línea editorial del dueño (sin identidad ni ideología de género, sin política partidista, violencia, armas ni salud). Religión y política: respeto y hechos, o se descarta.

| Fecha | País | Qué es | Fuente | Antelación medida | Preguntas que se escriben | Encaje | Riesgo |
|---|---|---|---|---|---|---|---|
| 2026-12-07 (lun) | EE. UU. | Golden Globes: anuncio de nominaciones; ceremonia 2027-01-10 (84.ª). Votos finales cierran 2027-01-02 | F25 (resumen; 2 páginas) | H5: ceremonia 0 a +3; nominaciones sin dato | «golden globes 2027 predictions» (EE. UU.) | Bajo: farándula y personas reales; sin hecho propio que comprobar | Personas reales |
| 2026-12-10 (jue) | Mundial, EE. UU. primero | The Game Awards 2026 (Peacock Theater, Los Ángeles). Nominados 2026-11-17; votación pública cierra 2026-12-09 | F19 (Wikipedia leída por el radar) + F-radar (dos fuentes de prensa de juegos) | H1: previa de −24 a −16 (ya pasó la de las nominaciones) y −2; resultado 0 a +2 (mediana 0) | «game awards 2026 predictions», «nominees», «winners», «goty», «gta 6», «live» (EE. UU., Filipinas, Indonesia, El Salvador y Canadá; India no probada); «who will win game of the year 2026» (EE. UU.) | **Medio a alto en demanda;** es el terreno que el canal ya mostró (juegos). Pasa el filtro solo si se abre una fuente primaria del reparto de votos | Personas reales (presentador, jurado); polémica «nominado antes de jugarse»; reparto 90 % jurado y 10 % público en una sola fuente (Wikipedia); `thegameawards.com` no abre |
| 2026-12-16 (mié) | India (y global de críticos) | Subasta de la IPL 2027 en Goa (reportada; el BCCI no emitió comunicado formal en lo que vi). Ver nota de choque con India–Sri Lanka | F21 (resumen; 2 medios, oficial sin abrir) | H18: contenido de subasta y traspasos de 175 a 282 días antes llegó a ≈ 0,5 a 1,4 millones | «ipl 2027 auction date», «players list», «retained players», «mega auction»; «when is the ipl auction 2027» (India; también aparece en Filipinas e Indonesia) | Medio a bajo: tercer país; hechos de precios públicos; fecha sin confirmar | Fecha sin confirmar formalmente; personas reales (jugadores): solo cifras públicas, nadie recibe golpes |
| 2026-12-16 a 12-24 | Filipinas | Simbang Gabi: nueve misas antes de Navidad (inicio 12-16; «anticipada» 12-15). Además: 12-08 Inmaculada Concepción (no laborable especial), 12-24 y 12-31 (no laborables especiales), 12-25 Navidad (feriado regular), 12-30 Día de Rizal (feriado regular) | F15 (Wikipedia) + F2 (timeanddate); la Proclamación 1427 de 2027 no afecta a 2026 | H20: Shorts del tema ≤ ≈ 25.000; «Christmas in the Philippines» de viajeros ≈ 450.000 (+5) y ≈ 243.000 (+9) | «simbang gabi song», «live today», «karaoke», «manila cathedral», «sa roblox»; «what is simbang gabi»; «why do filipinos celebrate christmas early» (Filipinas) | **Bajo:** lo que se escribe en inglés son canciones y misas en vivo, no preguntas con respuesta de datos | Religión: solo hechos o descartar. Se descarta como núcleo |
| 2026-12-18 (vie) | EE. UU. y mundial | **Dunesday:** *Avengers: Doomsday* y *Dune: Part Three* el mismo día (la segunda con tres semanas de IMAX exclusivo en EE. UU.) | F18 (Box Office Mojo, leído) + F-radar (Wikipedia de cada película, leída): 2 fuentes | Medido hoy: Shorts de ≈ 205.000 en 7 días y ≈ 54.000 en 12 horas (radar 4b); sin análogo pasado idéntico. H26 (*Avatar*): reparto y datos de la película a +3 y +26 días | «will avengers doomsday flop / make money / be in imax / be rated r», «dune part three vs avengers doomsday», «avengers doomsday vs avengers endgame / vs gta 6», «how long is avengers doomsday» (EE. UU.); «avengers doomsday trailer / reaction / tv spot» también en Filipinas, Indonesia, El Salvador y Canadá | **Alto:** demanda medida, apto para 13 a 17, hechos abiertos (fechas y duración) | Marcas (Disney, Marvel, Warner, Legendary): solo nombradas. Preventas y proyecciones cambian; quién gana no se sabe antes del 12-18 |
| 2026-12-21 (lun) | Todos | Solsticio de diciembre | F1 a F6 (los seis calendarios) | sin dato | «winter solstice» devuelve música, no preguntas | Bajo | — |
| 2026-12-25 (vie) | Los seis | **Navidad** (feriado en los seis países; en Indonesia 12-24 es día de cuti bersama) | F1 a F6 (6 calendarios, timeanddate) | EE. UU.: sin dato (H27). Análogos: Halloween −5, Acción de Gracias −2, Año Nuevo −2 (H8 a H10) | «how many days until christmas» y «2026», «2027», «countdown» (EE. UU., Filipinas, India, Indonesia); «why is christmas on december 25» (EE. UU., Filipinas, India, Indonesia, El Salvador); «christmas 2026 decor / wishlist / gifts / countdown / philippines / abs cbn» | Medio: una cuenta atrás de datos es universal. La pregunta «por qué el 25» toca religión | Religión: calendario e historia comprobada o descartar; ningún juicio |
| 2026-12-25 (vie) | EE. UU. | *Jumanji: Open World* (estreno; el radar anota que se movió del 12-11) | F18 (leído) + F-radar (resumen) | sin dato | «jumanji open world trailer / full movie / reaction» | Bajo a medio | Marca; fecha movida |
| 2026-12-26 a 2027-01-05 | Canadá (y EE. UU.) | Mundial Juvenil de Hockey (Edmonton y Red Deer) | F28 (resumen; 2 medios) | sin dato | «world juniors 2027 canada» (Canadá) | Bajo: sexto país; jugadores menores de edad (personas reales menores) | **Descartar:** menores de edad |
| 2026-12-26 | Canadá | Boxing Day (feriado federal) | F6 | sin dato | «boxing day» devuelve el tsunami de 2004 | Descartar | Tragedia mezclada en la consulta |
| 2026-12-31 y 2027-01-01 | Los seis | **Año Nuevo.** Filipinas: 12-31 no laborable especial; India, Indonesia, El Salvador, EE. UU., Canadá: 01-01 feriado | F1 a F6 (6 calendarios) | **H8: mediana −2; de −30 a 0.** Otros países: sin dato propio | «new year 2027 countdown / times square / london», «how many days until 2027» (EE. UU., Filipinas, India, Indonesia), «why do we celebrate new year on january 1st» (EE. UU.); en español: «año nuevo 2027 cuenta regresiva» (El Salvador) | **Medio a alto:** cuenta atrás universal; sirve a los seis países; hechos de calendario | Ya hay millones de Shorts de meme y estado de WhatsApp (H8); la competencia es de otra clase |
| 2027-01-06 a 01-09 | EE. UU. y mundial | CES 2027, Las Vegas (tecnología) | F26 (resumen; 2 páginas, oficial sin abrir) | sin dato | «ces 2027 tv / las vegas», «sony ces 2027», «lg ces 2027» (los cuatro países de habla inglesa) | Medio: tecnología es terreno posible; no medido | Marcas (Sony, LG): solo nombradas |
| 2027-01-09 (sáb) | Filipinas | Traslación del Nazareno Negro (fiesta del 9 de enero) | F17 (Wikipedia) | H21: un Short de famoso ≈ 1,6 millones; el resto ≤ ≈ 68.000 | «traslacion 2027», «paghahanda sa traslacion 2027» (Filipinas) | **Bajo** | Religión y multitudes: se descarta |
| 2027-01-10 (dom) | EE. UU. | Golden Globes (84.ª), CBS | F25 (resumen) | H5: 0 a +3 | «golden globes 2027 predictions» | Bajo | Personas reales |
| 2027-01-14 y 01-15 | India | Makar Sankranti (01-14); Pongal (01-15) | F3 (timeanddate) | H16: mediana −1,5; de −6 a +3 | «makar sankranti 2027 date / kab hai», «pongal 2027 date» (consultas en hindi y tamil, no en inglés) | Bajo | Religión y consultas en otros idiomas: descartar |
| 2027-01-17 (dom) | Filipinas | Sinulog de Cebú (tercer domingo de enero; derivado) | F16 (Wikipedia) | H22: máximo ≈ 135.000 | «sinulog 2027 song / update» | Bajo | Religión: descartar |
| 2027-01-18 (lun) | EE. UU. | Día de Martin Luther King Jr. (feriado federal) | F1 (timeanddate; sin segunda fuente) | H25: un saludo de ≈ 5,2 millones a −1; el resto de años anteriores | «mlk day for kids»; «martin luther king vs gandhi» (EE. UU.) | **Descartar** salvo el hecho de calendario | Política y raza: línea editorial y respeto; una comparación con otra persona real se convierte en juicio |
| 2027-01-21 (jue) | EE. UU. | Anuncio de nominaciones de los Óscar (99.ª; ceremonia 2027-03-14). Votación preliminar 12-07 a 12-11 y listas cortas 12-15 | F7 (Wikipedia, leída) | H4 (ceremonia): 0 a +1 | «oscars 2027 predictions / nominations / host / best picture» (EE. UU.) | Bajo a medio | Personas reales |
| 2027-01-26 (mar) | India | Día de la República | F3 (timeanddate) | H17: mediana −1 | «why is republic day celebrated» (India) | **Descartar** | Política y nacionalismo |
| 2027-02-06 (sáb) | Los seis (Filipinas e Indonesia lo marcan feriado) | **Año Nuevo Lunar** (Año de la Cabra, según el autocompletado). Filipinas: no laborable especial según una fuente, sin confirmar; Indonesia: feriado (SKB) | F1 a F4 y F6 (timeanddate) + F22 (resumen, Indonesia) + F23 (resumen, Filipinas; las fuentes discrepan en la clasificación) | H14: un Short de ≈ 30 millones a −2; el resto pequeño | «chinese new year 2027 date / calendar» (EE. UU., Filipinas, India, Indonesia); «when is chinese new year in 2027» (Indonesia, con inicio parcial); «year of the goat 2027» (EE. UU.) | **Medio:** hechos de calendario lunar; cuatro de los seis países lo marcan | Respeto cultural; «Cabra», «Oveja» o «Carnero» varía según la fuente: verificar el nombre antes de afirmarlo |
| 2027-02-07 (dom) | EE. UU. | Grammys (69.ª) | F9 (Wikipedia, leída; antes también en WTOP, radar): 2 fuentes | H6: 0 a +1 | «grammys 2027 predictions / nominations / nominees / best new artist» | Bajo | Personas reales; política en discursos |
| 2027-02-08 (lun) al 03-08 | Indonesia, India, Filipinas, EE. UU. y global | **Ramadán 2027** (fecha astronómica; el inicio real depende de la observación de la luna; timeanddate lo da «tentativo»: 02-09 en Indonesia) | F11 (Wikipedia, tabla leída) + F3 y F4 (timeanddate): 2 fuentes | **H12: mediana −4; de −20 a +2.** Cuentas atrás de 114 a 337 días antes con ≈ 1 a 5 millones | «ramadan 2027 date / start date / countdown» (Filipinas); «when is ramadan 2027», «when will ramadan start in 2027» (Indonesia); «how many days until ramadan 2027» (Filipinas e Indonesia); «why is ramadan celebrated» (EE. UU., Filipinas, India, Indonesia, El Salvador); en indonesio: «ramadan 2027 kapan» | **Medio, con cautela:** muchos países del público lo escriben; la pieza sería de calendario lunar | Religión: hechos astronómicos y de calendario con respeto; sin doctrina; la fecha puede variar un día: se dice |
| 2027-02-14 (dom) | EE. UU. y global | **Super Bowl LXI** (SoFi Stadium, Inglewood; medio tiempo: Jay-Z, según Wikipedia con Puck y Deadline) y San Valentín | F8 (Wikipedia, leída) + F1 (timeanddate): 2 fuentes | **H3: mediana 0; de −2 a +8**; el anuncio del medio tiempo, a −132 días con ≈ 1 millón | «super bowl 2027 predictions / halftime show / location / commercial / logo / jay z / performer», «why is super bowl called ...», «how much does the super bowl cost», «how many people watch...» (EE. UU.; la primera también en Canadá y El Salvador) | **Medio a alto:** hechos medibles (costo, audiencia, números romanos); apto 13 a 17 | «Super Bowl» es marca de la NFL: solo nombrada, con descargo; personas reales (Jay-Z, jugadores) no se tocan; nada de apuestas |
| 2027-02-15 (lun) | EE. UU. y Canadá | Día de los Presidentes (EE. UU.); Día de la Familia (AB, BC, NB, ON, SK) | F1 y F6 | sin dato | «presidents day for kids» (EE. UU.) | Bajo | — |
| 2027-02-16 (mar) | India | Inicio de exámenes de la CBSE (clase 10 hasta 03-09; clase 12 hasta 04-09); hoja de fechas publicada el 2026-11-06 | F20 (resumen; 2 medios y una nota de la radio pública All India Radio; oficial sin abrir) | Medido en el listado de India (2026-11-26) para los exámenes de 2026: un Short de «predicción» de ≈ 4 millones a −29 y otro de resultados de ≈ 17 millones a +36; sin serie limpia | «cbse board exam 2027 date / date sheet / time table / class 10 / class 12» (India) | Bajo a medio para 13 a 17 de India | Estrés y salud mental (línea editorial: sin salud); rumores de filtración: no |
| 2027-02-19 a 02-21 | EE. UU. | NBA All-Star, Phoenix | F27 (resumen; 2 páginas, oficial sin abrir) | sin dato | «nba all star 2027 predictions» (EE. UU., Filipinas, India, Indonesia) | Bajo a medio | Personas reales |
| 2027-02-27 (sáb) | Mundial | Día de Pokémon (anual) y *Pokémon Winds* y *Pokémon Waves* (2027, sin fecha); el Pokémon Presents de 2027: sin anunciar | F29 (resumen; la edición 2026 en dos medios) | H28: sin dato | «pokemon winds and waves trailer / leaks / starters / gameplay» (EE. UU., Filipinas, India, Indonesia); «pokemon day 2027», «pokemon presents» | **Medio a alto** para 13 a 17: juegos | Marca (The Pokémon Company, Nintendo): solo nombrada; fecha 2027 del evento y del juego: sin dato |
| 2027-03-08 a 03-15 | Indonesia | Nyepi (03-08); Idul Fitri (03-10 y 03-11, «tentativo» en timeanddate; el SKB lo fija según resumen); cuti bersama 03-09, 03-12 y 03-15 | F22 (resumen; 2 medios, oficial sin abrir) + F4 | **H13: mediana −2; de −9 a +16** | «when is eid 2027», «how many days until eid» (Indonesia); «lebaran 2027 tanggal / kapan», «mudik 2027» (indonesio); «what is nyepi» | Medio a bajo en inglés | Religión: hechos de calendario y logística (mudik) o descartar |
| 2027-03-10 (mié) al 05-15 | India y global | **IPL 2027** (74 partidos; 10 equipos) | F10 (Wikipedia, leída; cita a Cricinfo) | **H18: mediana +45; de 0 a +94**; previa de 175 a 282 días | «when will ipl 2027 start», «how many matches in ipl», «how many teams in ipl», «who has won the most ipl» (India; «when is ipl 2027» también en Filipinas e Indonesia) | **Medio:** hechos de formato; tercer país | Apuestas y personas reales: fuera; fecha puede cambiar |
| 2027-03-14 (dom) | EE. UU. | **Óscar 99.ª** (Conan O'Brien presenta por tercer año; ceremonia 2027-03-14) y **comienzo del horario de verano** en EE. UU. | F7 (Wikipedia, leída) y F1 (timeanddate; el 03-14) | H4: 0 a +1 (Óscar) | «oscars 2027 predictions / host» (EE. UU.); «daylight saving time explained / bill / permanent», «why do we change the clocks twice a year» (EE. UU.) | **Medio:** el horario de verano es un hecho puro; la gala trae personas reales | Óscar: personas reales; horario de verano: ninguno relevante. Canadá: no verifiqué su fecha |
| 2027-03-16 (mar) al 04-05 | EE. UU. | March Madness (torneo masculino de la NCAA: 76 equipos por primera vez; final en Ford Field, Detroit) | F12 (Wikipedia, leída; cita a la NCAA) | H23: mediana +11; de +3 a +13 | «march madness 2027 predictions», «how does march madness work», «how many teams in march madness» (EE. UU.) | **Medio:** «de 68 a 76 equipos» es un hecho nuevo | Marcas (NCAA, «March Madness»): solo nombradas; quinielas y apuestas: fuera |
| 2027-03-19 (vie) | EE. UU. y global | *Sonic the Hedgehog 4* (película, Paramount) | F14 (Wikipedia, leída) | sin dato | «sonic the hedgehog 4 trailer / toys / 2027» | Medio a bajo | Marcas (Sega, Paramount) |
| 2027-03-22 (lun) | India | Holi | F3 | Medido en el listado de India para Holi 2026 (2026-03-04): dos Shorts de ≈ 19 millones a −3 y +1; el resto del listado no es del tema | «holi 2027 kab hai / date» (hindi) | Bajo | Religión: descartar |
| 2027-03-25 a 03-28 | Filipinas, Indonesia, El Salvador, EE. UU., Canadá, India | Semana Santa: jueves y viernes santos (03-25 y 03-26) feriados regulares en Filipinas; viernes santo en Indonesia, Canadá e India; jueves a sábado feriados en El Salvador; **Pascua 03-28** | F1 a F6 (timeanddate) + F23 (resumen, Filipinas) | H24: demanda baja (lo más visto ≈ 286.000 a −17) | «why does easter change every year», «why is easter different every year», «easter 2027 date» (EE. UU.); «date of holy week 2027» (Filipinas) | Bajo a medio: «por qué Pascua cambia» es un hecho de calendario | Religión: solo el cálculo del calendario o descartar |

**Fechas vistas y descartadas sin análisis** (por línea editorial o por ser compra): Janucá (2026-12-05 a 12-12; religión), Kwanzaa (12-26; religión), Pearl Harbor (12-07; guerra), GivingTuesday (12-01; caridad y marca), Black Friday y Cyber Monday (2026-11-27 y 11-30; compra; H29 muestra poco rendimiento), Isra Miraj (2027-01-05, Indonesia; religión), Maha Shivaratri (2027-03-06, India; religión), Ram Navami (2027-04-15, fuera de la ventana; religión).

**Nota sobre el choque de la subasta de la IPL (12-16):** el resumen del buscador dice que la fecha llegó por un mensaje interno del BCCI a las franquicias y que coincide con un partido India–Sri Lanka en Bengaluru; no hay confirmación formal. Se trata como «sin confirmar».

---

## 4. Temporadas escolares y de vacaciones (importan por el tramo de 13 a 17)

| País | Qué sé | Fuente | Marca |
|---|---|---|---|
| EE. UU. | Los calendarios los fijan los distritos escolares; no tengo una fuente nacional abierta. **Sin dato verificado** de la pausa de invierno y de las vacaciones de primavera | — | sin dato |
| Canadá | Igual: calendarios por provincia y distrito. **Sin dato verificado** | — | sin dato |
| Filipinas | Año escolar 2026–2027 del DepEd bajo calendario de tres periodos: clases del 2026-06-08 al 2027-04-08. El tercer periodo empieza el **2027-01-04**. Las fechas de la pausa navideña: **sin dato** (en 2025 fueron dos semanas desde el 12-20, con regreso el 2026-01-05) | F24 (resumen; GMA y depedclub, oficial sin abrir) | resumen |
| India | Exámenes de la CBSE: clase 10 del 2027-02-16 al 03-09; clase 12 hasta el 04-09 | F20 (resumen) | resumen |
| Indonesia | No hay calendario nacional: lo fijan las provincias. Patrón de 2025–2026: la mayoría empezó el 12-22 y volvió hacia el 01-03 o 01-04, Java Occidental más tarde. Para 2026–2027 los blogs dicen del 12-21 al 12-31 (con regreso el 2027-01-04) y Java Occidental del 12-28 al 01-08; **se contradicen**: tomarlo como «alrededor del 21 de diciembre al 4 de enero» | F30 (resumen) | resumen, sin confirmar |
| El Salvador | El 2026 escolar público termina el **2026-11-13**; el 2026 empezó el 02-02. El inicio del 2027: **sin dato** | F31 (resumen) | resumen |

**Lectura:** los adolescentes del público están de vacaciones largas entre el 20 de diciembre y el 4 de enero en Filipinas e Indonesia, y probablemente en EE. UU. y Canadá (sin dato verificado). En India no hay vacaciones largas en esa fecha (los exámenes empiezan el 02-16). Eso no se tradujo todavía en nada medido en el canal: **sin dato** de si la vista aumenta en vacaciones.

---

## 5. Calendario de diciembre de 2026, día por día

**Cadencia de partida:** 3 Shorts por semana (`PARAMETROS.md`, sección 3). Las filas con «publicar» son propuestas de ventana; el equipo decide qué entra por demanda y por filtro. **No se reserva cupo para ningún tema:** las ventanas de abajo son plazos, no cupos. La regla del radar es empezar a producir 10 días antes (estimación del radar).

| Fecha | Día | Qué cae (país) | Qué conviene |
|---|---|---|---|
| 2026-12-01 | mar | GivingTuesday (EE. UU.; descartado). **Fecha límite del short 4** (radar) | Short 4 publicado hoy o antes |
| 2026-12-02 | mié | — | Hueco libre por demanda |
| 2026-12-03 | jue | — | Con la regla de 10 días, una pieza empezada hoy ya no llega a la previa de los Game Awards antes del 12-13: **la pieza previa solo cabe si se empieza a más tardar el 11-29 o 11-30 (radar) y se publica el 12-08 o 12-09** |
| 2026-12-04 | vie | — | Empezar el Short de Dunesday si se quiere publicarlo el 12-14 |
| 2026-12-05 | sáb | Janucá empieza (descartado) | — |
| 2026-12-06 | dom | San Nicolás (observancia; sin encaje) | — |
| 2026-12-07 | lun | Golden Globes: nominaciones (EE. UU.); Pearl Harbor (descartado); votación preliminar de los Óscar empieza | Nada propio |
| 2026-12-08 | mar | Inmaculada Concepción (Filipinas); **fecha límite del radar para empezar Dunesday** | Dunesday ya en producción |
| 2026-12-09 | mié | **Cierra la votación pública de The Game Awards**; último día de la pieza previa | Último día de la pieza previa (si se empezó a tiempo); H1 mide una oleada previa a −2 días |
| 2026-12-10 | jue | **The Game Awards 2026** (Los Ángeles) | **Ventana de 72 horas para el resultado (12-10 a 12-13), solo si el estudio llega** |
| 2026-12-11 | vie | Termina la votación preliminar de los Óscar | — |
| 2026-12-12 | sáb | Termina Janucá | — |
| 2026-12-13 | dom | — | Cierre de la ventana de resultado de los Game Awards |
| 2026-12-14 | lun | — | **Primera ventana de publicación de Dunesday** (de 12-14 a 12-17; el radar pedía de 12-10 a 12-17) |
| 2026-12-15 | mar | Listas cortas de los Óscar | — |
| 2026-12-16 | mié | **Simbang Gabi empieza** (Filipinas); **subasta de la IPL** en Goa (reportada) | Opcional: pieza de la IPL solo si pasa el filtro; la fecha no está confirmada |
| 2026-12-17 | jue | — | Último día cómodo de Dunesday antes del estreno |
| 2026-12-18 | vie | **Dunesday** (EE. UU.); votos finales de los Golden Globes se envían | Nada nuevo publicado hoy: la pieza ya salió |
| 2026-12-19 | sáb | — | — |
| 2026-12-20 | dom | Primeras cifras de taquilla del fin de semana | **Ventana de 72 horas para la taquilla** (12-20 a 12-23), solo si pasa el filtro de hechos |
| 2026-12-21 | lun | Solsticio de diciembre | — |
| 2026-12-22 | mar | — | **Ventana de la cuenta atrás de Navidad** (12-18 a 12-23), si se hace; empezar a producir el 12-08 |
| 2026-12-23 | mié | — | — |
| 2026-12-24 | jue | Nochebuena; Filipinas e Indonesia: no laborable/cuti bersama | — |
| 2026-12-25 | vie | **Navidad** (los seis países); estreno de *Jumanji: Open World* | Nada publicado hoy (los datos dicen que la ola de fiestas es antes) |
| 2026-12-26 | sáb | Boxing Day (Canadá; descartado); inicio del Mundial Juvenil de hockey (descartado: menores de edad) | — |
| 2026-12-27 | dom | — | — |
| 2026-12-28 | lun | Canadá: día feriado trasladado | **Abrir la ventana de la cuenta atrás de Año Nuevo** (de 12-26 a 12-30) |
| 2026-12-29 | mar | — | — |
| 2026-12-30 | mié | Día de Rizal (Filipinas) | **Último día cómodo** de la cuenta atrás de Año Nuevo (mediana de los de más vistas: −2) |
| 2026-12-31 | jue | **Año Nuevo** (Filipinas: no laborable especial); víspera | Nada propio |

### Lo que conviene tener publicado cada semana

| Semana | Publicado en la semana | En producción en la semana | Qué dato lo apoya |
|---|---|---|---|
| 11-30 a 12-06 | Short 4 (GTA VI, límite 12-01) | Pieza previa de The Game Awards (empezar el 11-29 o 11-30 para publicar el 12-08 o 12-09); Dunesday (empezar 12-04) | H1 (oleada previa de nominaciones); radar |
| 12-07 a 12-13 | Pieza previa de The Game Awards (12-08 o 12-09, límite 12-09); resultado de los Game Awards en 72 horas (12-10 a 12-13) si el estudio llega | Dunesday terminado; cuenta atrás de Navidad (empezar 12-08) | H1: previa −24 a −16 y −2; resultado 0 a +2 |
| 12-14 a 12-20 | **Dunesday (12-14 a 12-17)**; taquilla del primer fin de semana desde el 12-20 | Cuenta atrás de Navidad; cuenta atrás de Año Nuevo (empezar 12-16 a 12-20) | Radar 4b: demanda de Dunesday sube hasta el 12-18; H26 |
| 12-21 a 12-27 | Cuenta atrás de Navidad (12-18 a 12-23) | Año Nuevo; Enero (ver 6) | H8 a H10: fiestas con mediana −2 a −5 |
| 12-28 a 01-03 | Cuenta atrás de Año Nuevo (12-26 a 12-30) | Enero: CES, Golden Globes, Óscar, Año Nuevo Lunar | H8 |

**Resumen del mes:** en diciembre mandan **tres fechas** (Game Awards 12-10, Dunesday 12-18 y Año Nuevo 12-31/01-01) y una cuarta de segundo orden (Navidad 12-25). La IPL (12-16) y Simbang Gabi (12-16 a 12-24) son de países 2.º y 3.º pero la primera no está confirmada y la segunda no tiene demanda en inglés de preguntas. Con 3 por semana, diciembre trae ≈ 13 espacios; de ellos **cinco a seis** quedan atados a una fecha de este calendario (Short 4, Game Awards previo y resultado, Dunesday previo y taquilla, Navidad, Año Nuevo, según lo que el estudio alcance) y el resto lo llena el radar semanal por demanda. Es una propuesta de plazos, no un cupo.

---

## 6. Esquema de 12 meses (diciembre de 2026 a noviembre de 2027)

Fechas tomadas de timeanddate (F1 a F6) salvo que se indique. Las marcadas «tent.» son tentativas (feriados religiosos que dependen de la luna o de proclamas que faltan). Todo lo que no tiene fuente abierta va marcado.

| Mes | EE. UU. y Canadá | Filipinas | India | Indonesia | El Salvador | Global (cine, juegos, deportes) | Nota de antelación |
|---|---|---|---|---|---|---|---|
| Dic 2026 | Navidad 12-25; Boxing Day (CA); Mundial Juvenil 12-26 a 01-05 (CA) | Simbang Gabi 12-16 a 12-24; Navidad; Rizal 12-30 | IPL: subasta 12-16 (reportada); Navidad | Navidad 12-25 (cuti bersama 12-24); vacaciones escolares ≈ 12-21 a 01-04 (resumen) | Navidad | Game Awards 12-10; Dunesday 12-18; *Jumanji* 12-25 | A (resultado), B (Navidad y Año Nuevo) |
| Ene 2027 | Año Nuevo 01-01; CES 01-06 a 01-09; Golden Globes 01-10; MLK 01-18; nominaciones Óscar 01-21 | Año Nuevo; DepEd retoma 01-04; Nazareno 01-09; Sinulog 01-17 | Makar Sankranti 01-14; Pongal 01-15; República 01-26 | Año Nuevo; Isra Miraj 01-05 | Año Nuevo | Año Nuevo | A y B; la Copa Asiática ya no cae aquí (se movió a 2027-12-23, F13) |
| Feb 2027 | Grammys 02-07; Super Bowl y San Valentín 02-14; Presidentes 02-15; NBA All-Star 02-19 a 02-21; Familia (CA) 02-15 | Año Nuevo Lunar 02-06 (clasificación en disputa) | CBSE 02-16; IPL se acerca | Imlek 02-06; **Ramadán empieza ≈ 02-08 o 02-09** | — | Ramadán; Día de Pokémon 02-27 | D (Ramadán, Año Nuevo Lunar), A (premios y Super Bowl) |
| Mar 2027 | Óscar y horario de verano 03-14; March Madness 03-16 a 04-05; San Patricio 03-17; *Sonic 4* 03-19; Pascua 03-28 | Eid'l Fitr ≈ 03-10 (tent.; se proclama aparte); Semana Santa 03-25 a 03-28 | **IPL empieza 03-10**; Ramzan Id ≈ 03-10 (tent.); Holi 03-22; Viernes Santo 03-26 | Nyepi 03-08; **Idul Fitri 03-10 y 03-11**; Viernes Santo 03-26 | Semana Santa 03-25 a 03-27 | Eid; equinoccio 03-21 | A, C (torneos largos) |
| Abr 2027 | Final de March Madness 04-05 | Día del Valor 04-09; DepEd cierra 04-08 | Ram Navami 04-15; Mahavir 04-19; IPL sigue | — | — | Película de *Zelda* 04-30 (F14); Apple II 04-16 y *Los Simpson* 04-19 (radar sección 3.3; marcas de fiabilidad allí) | C |
| May 2027 | Día de las Madres 05-09; Memorial Day 05-31 | Eid'l Adha ≈ 05-17 (tent.) | IPL termina 05-15; Bakrid ≈ 05-17 (tent.); Buddha Purnima 05-20 | Idul Adha ≈ 05-17 (tent.); Waisak 05-20 | Día de la Madre 05-10 | *Star Wars* 50.º 05-25 y *Starfighter* 05-28 (radar, resumen) | A |
| Jun 2027 | Juneteenth 06-18/19; Padre 06-20 | Independencia 06-12 | — | Muharram ≈ 06-06 (tent.); Pancasila 06-01 | Padre 06-17 | *Spider-Man: Beyond the Spider-Verse* 06-18 y *Shrek 5* 06-30 (radar, resumen). Summer Game Fest y Mundial Femenino de FIFA: **sin dato** | A |
| Jul 2027 | Día de Canadá 07-01; Independencia EE. UU. 07-04 (observado 07-05) | — | — | — | — | *A Minecraft Movie Squared* 07-23 (F14) | A |
| Ago 2027 | — | Ninoy 08-21; Héroes 08-30 | Independencia 08-15; Janmashtami 08-25 | Independencia 08-17; Maulid ≈ 08-15 (tent.) | Fiestas agostinas 08-03 a 08-06 | — | B |
| Sep 2027 | Día del Trabajo 09-06 | «Ber months»: la gente escribe «ber months song» (autocompletado; el inicio de la temporada navideña como costumbre: **sin fuente abierta**) | Ganesh Chaturthi 09-04; Onam 09-12 | — | Independencia 09-15 | Atari VCS 50.º (radar, sin confirmar el día) | B |
| Oct 2027 | Halloween 10-31; Columbus 10-11 | — | Dussehra 10-09; Diwali 10-29 | — | — | Mundial de Cricket 10-04 a 11-21 (F10, vía Cricinfo en resumen) | B, C |
| Nov 2027 | Acción de Gracias 11-25; Black Friday 11-26; Cyber Monday 11-29; Veteranos 11-11 | Todos los Santos 11-01; Bonifacio 11-30 | Guru Nanak 11-14 | — | Difuntos 11-02 | Game Awards 2027: **sin dato**; final del Mundial de Cricket 11-21 | A, B |

**Qué se mide para ajustar esta tabla:** a los 7 y 28 días de cada video atado a una fecha, país por país en Studio («Países» de cada video). Después de 5 videos con fecha, se compara el reparto de países de los atados al calendario de EE. UU. con los atados a una fecha de otro país (sección 7).

---

## 7. Qué implica que el 2.º y el 3.º país no sean de habla inglesa nativa mayoritaria

**Hechos que sostienen el análisis**

1. **Filipinas** tiene el inglés como idioma oficial junto al filipino (Wikipedia «Languages of the Philippines», leída; F32). **India** tiene el hindi como idioma oficial de la Unión y el inglés como idioma oficial adicional, y el inglés funciona como lengua franca en gran parte del país (F32, leída). **Indonesia** no tiene el inglés como idioma oficial: su idioma oficial es el indonesio (F32, leída). **El Salvador** es hispanohablante (sin fuente abierta; es de dominio común y lo marco así).
2. **El autocompletado en inglés dice lo mismo en varios países cuando el tema es global** (juegos, cine, deporte): «avengers doomsday», «game awards 2026» y «gta 6» devuelven sugerencias equivalentes en EE. UU., Filipinas, Indonesia, El Salvador y Canadá (India: probé «gta 6 india» y no las dos primeras); «how much did gta 6 make» y «pokemon winds and waves» en Filipinas, India e Indonesia (la segunda también en EE. UU.); «nba all star 2027» y «ces 2027» en EE. UU., Filipinas, India e Indonesia. **Cuando el tema es local, las sugerencias son canciones, misas en vivo, y consultas en hindi, tamil o indonesio** («simbang gabi» → canciones y misas; «makar sankranti 2027» → «kab hai»; «lebaran 2027» → «tanggal»).
3. **Algunos temas compartidos sí se escriben en inglés en varios países:** «chinese new year 2027 date» (EE. UU., Filipinas, India, Indonesia), «when is ramadan 2027» y «how many days until ramadan 2027» (Filipinas e Indonesia), «how many days until christmas» y «until 2027» (EE. UU., Filipinas, India, Indonesia), «when is ipl 2027 auction» (India, Filipinas e Indonesia).
4. **El Studio dice que el peso de cada país cambia mucho de un video a otro** (sección «Estadísticas»): el país no está estabilizado.

**Recomendación (opinión mía): programar por el calendario de Estados Unidos y de los eventos globales de entretenimiento como columna vertebral, y sumar una capa pequeña de fechas compartidas por varios países. No abrir tandas por país.**

**Por qué**

- El primer país tiene una ventaja grande y se repite en el listado de todos los temas globales. El feed de Shorts reparte por comportamiento del espectador, no por la fecha local: una pieza sobre Dunesday o el Super Bowl llega a Filipinas e India en inglés sin necesitar una fecha local.
- Las fechas locales de Filipinas, India e Indonesia (Simbang Gabi, Traslación, Sinulog, Makar Sankranti, Holi, Nyepi) piden consultas en otros idiomas, son religiosas o culturales (riesgo: tratar con respeto y hechos, o descartar), y en los históricos medidos rinden poco en inglés (H20, H21, H22).
- Las fechas que sí valen la pena de esa capa son las que pasan tres pruebas a la vez: (a) se escriben en inglés en más de un país (Año Nuevo Lunar, Ramadán, cuentas atrás de Navidad y Año Nuevo, IPL); (b) hay un hecho comprobable con fuente abierta (calendario lunar, duración, número de partidos); (c) pasan el filtro editorial.
- Los otros países no necesitan tandas propias porque el contenido va en inglés con subtítulos en español quemados (regla del dueño): eso sirve de inmediato a El Salvador y no ayuda a Indonesia, donde el inglés no es idioma oficial. Filipinas e India tienen el inglés como idioma oficial o adicional (F32), pero **no sé** qué parte de su público lo entiende bien (sin dato medido aquí).

**Límites**

- **Hay dos videos medidos.** Del tercer al sexto país la diferencia es pequeña y el orden entre ellos puede cambiar con un solo video. Si dentro de cinco videos el reparto cambia, la recomendación se revisa.
- No hay datos de retención por país ni de hora del público: no sé si un país mira más tiempo o a otras horas. Una pieza programada «para la mañana de Estados Unidos» llega a Filipinas, Indonesia e India en la noche; **sin dato** de si importa.
- No sé si Filipinas, India e Indonesia ven el canal por el tema global (juegos, cine) o por el formato. Los Shorts de Studio no dicen el tema por país.
- «Capa pequeña» no significa un número: no fijo cuántas piezas son de fecha compartida. La métrica es país × fecha en cada video y la regla de revisión de `PARAMETROS.md` (cada 5 videos).

**Propuesta para el equipo (técnica; la decide el equipo, no hace falta aprobación del dueño):** añadir una pista de subtítulos en inglés (`subtitulos_en.srt`, 0 créditos) además de la de español. Hoy casi todo el público ve sin subtítulos; el efecto es **sin dato**, pero cuesta nada y se mide con la tabla de subtítulos de Studio. **Propuesta de cambio dentro del video para la pedagoga y la psicóloga:** ninguna.

---

## 8. Pendiente de los históricos de Trends que traerá Keter

Google Trends devuelve error 429 desde esta sesión. Keter lo lee aparte. **Lista exacta de lo que conviene leer**, con rango de cinco años (de 2021-11 a 2026-11) y granularidad semanal para ver en qué semana empieza a subir cada término antes de su fecha, y con «Búsqueda web» y «YouTube» por separado. El objetivo es medir la antelación del **volumen**, que este archivo no tiene.

| # | Términos (en inglés salvo que se diga) | País | Para qué |
|---|---|---|---|
| 1 | «game awards», «the game awards winners», «game of the year» | EE. UU., Filipinas, India, Indonesia | Cuándo sube la búsqueda antes del 12-10 y cuánto dura después |
| 2 | «avengers doomsday», «dune part three», «dunesday» | EE. UU., Filipinas, India, Indonesia | Semana de arranque y de pico antes del 12-18; contraste con *Avatar: Fire and Ash* (2025-12-19) |
| 3 | «how many days until christmas», «christmas», «pasko» (Filipinas), «natal» (Indonesia) | EE. UU., Filipinas, India, Indonesia, El Salvador (con «navidad»), Canadá | Semana en que sube la cuenta atrás; contraste con Simbang Gabi |
| 4 | «new year 2027», «how many days until 2027», «new year countdown» | los seis | Mediana de antelación del volumen del Año Nuevo |
| 5 | «simbang gabi», «traslacion», «sinulog», «ber months» | Filipinas | Si hay volumen en inglés o solo en filipino |
| 6 | «ipl auction», «ipl 2027», «ipl schedule» | India, Filipinas, Indonesia | Subasta 12-16 y arranque 03-10 |
| 7 | «ramadan 2027», «when is ramadan», «lebaran 2027», «idul fitri 2027», «puasa 2027» | Indonesia, India, Filipinas, EE. UU., Canadá | Cuántos meses antes sube «cuándo cae» |
| 8 | «super bowl», «super bowl halftime show», «super bowl 61» y «super bowl lxi» | EE. UU., Canadá, El Salvador | Antelación del anuncio del medio tiempo y del partido |
| 9 | «oscars», «oscars nominations», «golden globes», «grammys» | EE. UU., Canadá | Antelación de nominaciones y ceremonia |
| 10 | «chinese new year», «lunar new year», «year of the goat», «year of the sheep» | EE. UU., Filipinas, India, Indonesia, Canadá | Qué nombre del animal domina antes de afirmarlo |
| 11 | «march madness», «march madness bracket», «how many teams in march madness» | EE. UU. | Semana del pico |
| 12 | «daylight saving time», «why do we change the clocks» | EE. UU. | Pico en marzo y noviembre |
| 13 | «pokemon winds and waves», «pokemon day», «pokemon presents» | EE. UU., Filipinas, India, Indonesia | Si el tema global se comparte entre los países |
| 14 | «cbse board exam 2027», «cbse date sheet» | India | Si hay volumen en inglés entre 13 y 17 años |
| 15 | «gta 6», «how much did gta 6 make», «gta 6 sales» | EE. UU., Filipinas, India, Indonesia | Referencia: lo ya medido en EE. UU. dice que las consultas de dinero **no** entran en las 100 de la lista; confirmar en los otros tres países |
| 16 | «winter break», «spring break» | EE. UU., Canadá | Si la temporada escolar mueve el interés |

**Cómo leerlo:** para cada término, anotar la semana en que el interés relativo sube por encima de la mitad del valor del pico y compararla con la fecha del evento: **eso es la antelación del volumen**, que se contrasta con la antelación de publicación de la sección 2. También sirve la categoría «Juegos» y «Películas» en cada país. Lo que Trends devuelva se archiva en `video-studio/estadisticas/datos/` y no se sube.

---

## 9. Lo que no sé

| Qué falta | Por qué | Qué lo resolvería |
|---|---|---|
| Volumen de búsqueda de cualquier pregunta | El autocompletado no da volumen; Trends da 429 | Lecturas de Keter (sección 8) |
| Si una pieza publicada antes o después rinde más en un canal de cero suscriptores | Los históricos miden canales grandes y vistas acumuladas | Medir el propio canal: fecha de publicación contra vistas a 7 días, con 5 videos atados a fecha |
| Qué países ven qué temas | Studio solo da país por video | Cruzar país × tema de cada video |
| La hora a la que mira el público | Studio dice «no hay suficientes datos» | Más de 5 videos con hora de publicación anotada |
| Calendario escolar de EE. UU. y Canadá; de El Salvador para 2027; pausa navideña de Filipinas | Sin fuente nacional abierta | Fuentes del DepEd, el MINED y los distritos |
| Las fechas de eventos pasados marcadas «sf» (final de *Stranger Things* 5, Golden Globes 2026, Grammys 2026, Juegos de Invierno 2026, Mundial T20 2026, March Madness 2026, estreno de *Avatar*) | No abrí una fuente de cada una; las fechas de los propios Shorts del día coinciden | Abrir cada una |
| Las clasificaciones de feriados de Filipinas 2027 (cuáles son «regulares», cuáles «especiales», si el Año Nuevo Lunar es feriado) | Las fuentes discrepan; la Proclamación 1427 oficial no abrió | `officialgazette.gov.ph` |
| Cuándo cae Idul Fitri en Filipinas, India e Indonesia con certeza | Depende de la observación lunar; en Filipinas se proclama aparte; el SKB de Indonesia lo fija en resumen | Comunicados de cada gobierno |
| Fecha de la subasta de la IPL | Solo reportes; el BCCI no emitió comunicado formal en lo que vi | `iplt20.com` |
| Fecha del Pokémon Presents 2027 y del lanzamiento de *Winds* y *Waves* | No anunciados | Comunicados de Nintendo y The Pokémon Company |
| Fecha de Spotify Wrapped 2026, Google «Year in Search», Summer Game Fest 2027, Game Awards 2027, Mundial Femenino de FIFA 2027 | No las verifiqué | Fuentes oficiales |
| Qué hay en Navidad 2025 y en Día de Pokémon 2026 | El listado no devolvió Shorts (H27 y H28) | Otra consulta o Trends |
| Si el horario de verano de 2027 también cambia el 03-14 en Canadá | No lo verifiqué | Fuente oficial de Canadá |
| Cuántos de los Shorts de los históricos son explicativos con datos | Clasifiqué por título | Revisar uno a uno si el equipo lo pide |
| Hechos para cada pieza candidata (preventas, duración, reglas de votos) | No es objeto de este archivo; cada pieza se verifica en su semana | Paso 5 del filtro del radar |

---

## 10. Fuentes

Todas leídas o consultadas el 2026-11-26. «Leído» = abierto con `curl -sS -m 40 -A "Mozilla/5.0"`; «resumen» = resumen del buscador de la sesión.

| Código | Qué | Dirección | Marca |
|---|---|---|---|
| F1 | Feriados de EE. UU. 2026 y 2027 | https://www.timeanddate.com/holidays/us/2026 y https://www.timeanddate.com/holidays/us/2027 | leído |
| F2 | Feriados de Filipinas | https://www.timeanddate.com/holidays/philippines/2026 y .../2027 | leído |
| F3 | Feriados de India | https://www.timeanddate.com/holidays/india/2026 y .../2027 | leído |
| F4 | Feriados de Indonesia | https://www.timeanddate.com/holidays/indonesia/2026 y .../2027 | leído |
| F5 | Feriados de El Salvador | https://www.timeanddate.com/holidays/el-salvador/2026 y .../2027 | leído |
| F6 | Feriados de Canadá | https://www.timeanddate.com/holidays/canada/2026 y .../2027 | leído |
| F7 | 99.ª entrega de los Óscar | https://en.wikipedia.org/wiki/99th_Academy_Awards | leído (texto fuente) |
| F8 | Super Bowl LXI | https://en.wikipedia.org/wiki/Super_Bowl_LXI | leído |
| F9 | 69.ª entrega de los Grammy | https://en.wikipedia.org/wiki/69th_Annual_Grammy_Awards | leído |
| F10 | IPL 2027 (10 de marzo a 15 de mayo; cita a Cricinfo, NDTV Sports; Mundial de cricket 4 de octubre a 21 de noviembre de 2027) | https://en.wikipedia.org/wiki/2027_Indian_Premier_League | leído |
| F11 | Ramadán (tabla de fechas: 2026-02-18 a 03-19; 2027-02-08 a 03-08) | https://en.wikipedia.org/wiki/Ramadan | leído |
| F12 | Torneo masculino de la NCAA 2027 | https://en.wikipedia.org/wiki/2027_NCAA_Division_I_men%27s_basketball_tournament | leído |
| F13 | Copa Asiática 2027 (movida a 2027-12-23 a 2028-01-21) | https://en.wikipedia.org/wiki/2027_AFC_Asian_Cup | leído |
| F14 | Videojuegos 2027 y adaptaciones (*Sonic 4* 03-19, *Zelda* 04-30, *Minecraft* 07-23) | https://en.wikipedia.org/wiki/2027_in_video_games | leído |
| F15 | Simbang Gabi | https://en.wikipedia.org/wiki/Simbang_Gabi | leído |
| F16 | Sinulog | https://en.wikipedia.org/wiki/Sinulog | leído |
| F17 | Fiesta del Nazareno Negro | https://en.wikipedia.org/wiki/Feast_of_the_Black_Nazarene | leído |
| F18 | Calendario de estrenos | https://www.boxofficemojo.com/calendar/ | leído |
| F19 | The Game Awards 2026 | https://en.wikipedia.org/wiki/The_Game_Awards_2026 (leída por el radar el 2026-11-26; yo no la releí) | leído (radar) |
| F20 | Exámenes CBSE 2027 | https://newsonair.gov.in/cbse-releases-2027-board-exam-date-sheet-exams-begin-16th-february/ y https://www.businesstoday.in/education/exams/story/cbse-class-10-12-board-exam-2027-dates-announced-exams-to-begin-on-february-16-566282-2026-11-06 | resumen |
| F21 | Subasta de la IPL 2027 | https://www.crictracker.com/cricket-news/ipl-2027-auction-to-be-held-on-december-16-in-goa-7060/ y https://www.businesstoday.in/sports/ipl/story/ipl-2027-goa-likely-to-host-auction-on-december-16-as-bcci-informs-franchises-562272-2026-10-17 | resumen |
| F22 | Feriados de Indonesia 2027 (SKB firmado el 2026-09-15) | https://kemenkopmk.go.id/pemerintah-tetapkan-18-hari-libur-nasional-dan-8-cuti-bersama-tahun-2027 y https://setneg.go.id/baca/index/inilah_skb_3_menteri_libur_nasional_dan_cuti_bersama_2027 | resumen |
| F23 | Feriados de Filipinas 2027 (Proclamación 1427, firmada el 2026-09-08) | https://newsinfo.inquirer.net/2303491/list-holidays-special-non-working-days-for-2027 y https://www.gmanetwork.com/news/topstories/nation/1001999/malaca-ang-bares-holidays-for-2027/story | resumen |
| F24 | Calendario del DepEd 2026–2027 | https://www.gmanetwork.com/news/topstories/nation/984622/explainer-deped-school-calendar-sy/story/ y https://depedclub.com/deped-three-term-school-calendar-for-sy-2026-2027/ | resumen |
| F25 | Golden Globes 2027 (84.ª) | https://goldenglobes.com/articles/nikki-glaser-to-host-jan-10-2027-golden-globes/ y https://nextbestpicture.com/the-84th-golden-globes-have-a-date-a-host-new-ai-rules/ | resumen |
| F26 | CES 2027 | https://www.ces.tech/About-CES/Dates-and-Hours.aspx y https://audioxpress.com/news/ces-returns-january-with-ai-connected-mobility-and-new-opportunities-for-audio | resumen |
| F27 | NBA All-Star 2027 | https://nbaevents.nba.com/nba-all-star-2027 y https://www.nba.com/suns/news/phoenix-suns-up-next-to-host-nba-all-star-2027 | resumen |
| F28 | Mundial Juvenil de Hockey 2027 | https://www.iihf.com/en/news/70834/edmonton_and_red_deer_to_host_2027_iihf_world_juni y https://www.nhl.com/news/2027-world-junior-championship-schedule-announced | resumen |
| F29 | Pokémon Presents 2026 y *Winds* y *Waves* | https://nintendosoup.com/pokemon-presents-announced-for-february-27th-2026 y https://gigazine.net/gsc_news/en/20260227-pokemon-presents-30th-anniversary/ | resumen |
| F30 | Vacaciones escolares de Indonesia | https://www.detik.com/edu/sekolah/d-8284422/jadwal-masuk-sekolah-usai-libur-nataru-2026-siap-siap-kembali-belajar y https://www.brainacademy.id/blog/kalender-pendidikan-sd-smp-sma | resumen, se contradicen |
| F31 | Año escolar de El Salvador 2026 | https://diario.elmundo.sv/nacionales/las-clases-en-las-escuelas-publicas-terminaran-el-13-de-noviembre y https://diario.elmundo.sv/nacionales/ano-escolar-2026-iniciara-el-2-de-febrero | resumen |
| F32 | Idiomas oficiales | https://en.wikipedia.org/wiki/Languages_of_the_Philippines, https://en.wikipedia.org/wiki/Languages_of_India y https://en.wikipedia.org/wiki/Languages_of_Indonesia | leído |
| F33 | Autocompletado de YouTube (no da volumen) | `https://www.youtube.com/complete/search?client=youtube&ds=yt&hl=en&gl=<US, PH, IN, ID, SV, CA>&q=<texto>`; en español `hl=es` para El Salvador | leído |
| F34 | Listados y Shorts de YouTube | `https://www.youtube.com/results?search_query=<texto>&hl=en&gl=<US, IN, PH, ID, SV>` y `https://www.youtube.com/shorts/<id>`. Consultas por evento: «game awards 2025 shorts / winners / nominees / predictions»; «stranger things 5 finale shorts»; «super bowl 2026 shorts / halftime / facts»; «oscars 2026 shorts / winners / nominations»; «golden globes 2026 shorts / winners»; «grammys 2026 shorts / winners»; «winter olympics 2026 shorts»; «new year 2026 shorts / facts / countdown»; «halloween 2026 shorts»; «thanksgiving 2026 shorts»; «black friday 2026 shorts»; «gta 6 launch shorts»; «ramadan 2026 shorts»; «lebaran 2026 shorts»; «idul fitri 2026 shorts»; «puasa 2026 shorts»; «lunar new year 2026 shorts»; «diwali 2026 shorts»; «makar sankranti 2026 shorts»; «republic day 2026 shorts»; «ipl 2026 shorts / facts»; «t20 world cup 2026 shorts / facts»; «holi 2026 shorts»; «simbang gabi shorts / 2025»; «christmas philippines shorts»; «traslacion 2026 shorts»; «sinulog 2026 shorts»; «march madness 2026 shorts / bracket»; «easter 2026 shorts»; «mlk day 2026 shorts»; «avatar fire and ash shorts / runtime» | leído |
| F35 | Datos del canal (no se sube) | `video-studio/estadisticas/datos/2026-11-26_studio_tin_y_tan.md` | leído |
| F-radar | Radar de tendencias | `video-studio/comercial/radar_de_tendencias.md` (secciones 3, 4b, 5b) y `comercial/2026-11-26_tema_short4_tin_y_tan.md` | leído |

**Fuentes que intenté abrir y no abrieron** (host exacto, para que la conversación principal pida permiso si hace falta): `www.opm.gov` (feriados federales de EE. UU.), `www.officialgazette.gov.ph` (Proclamación 1427), `setneg.go.id` y `kemenkopmk.go.id` (SKB de Indonesia 2027), `www.cbse.gov.in` y `newsonair.gov.in` (exámenes CBSE), `goldenglobes.com` (Golden Globes), `www.iihf.com` (Mundial Juvenil), `www.nba.com` (All-Star), `www.ces.tech` (CES), `www.canada.ca` (feriados de Canadá), `www.iplt20.com` (IPL). Además: `trends.google.com` (429 desde esta sesión, lo lee Keter), `thegameawards.com`, `www.sec.gov` y los de la lista de 7b del radar.
