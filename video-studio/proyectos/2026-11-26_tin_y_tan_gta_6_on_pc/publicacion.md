# Publicación — Is GTA 6 Coming to PC?

> Short 5 de Tin & Tan (`TIN-EN-S-005`), YouTube Shorts, 9:16, ≈ 31 s (plan: 930 fotogramas). Escrita el 2026-11-27 por el
> comercial con `00_brief.md`, `02_prompt/direccion.md` (secciones 1, 2, 8, 9 y 10), `comercial/2026-11-27_hechos_short5_gta_6_on_pc.md`,
> `comercial/titulos.md` y el método de metadatos del «Manager de redes sociales y YouTube» (fuera del repositorio, leído hoy).
> **Estado: borrador para el sí del dueño. No se publica ni se sube nada.** Calendario: viernes 2026-12-04, 16:00 (hora de
> El Salvador). El video no existe todavía (falta voz, render y revisión): todo lo que dice «el video» es el guion final.

## Antes de publicar: el hecho que caduca se relee ese día

«Not announced» y «No official PC date. As of today.» son una **ausencia** y caducan. El 2026-12-04, antes de subir (pasos
del archivo de hechos, sección 6):

1. `curl -sS -m 40 -A "Mozilla/5.0" https://www.rockstargames.com/VI` y contar «PC» y «Windows» (2026-11-27: 0 y 0). Leer el listado
   de `https://www.take2games.com/ir/press-releases` buscando «PC», «Windows» y «Steam» en los títulos nuevos, y el texto fuente de
   Wikipedia de `Grand_Theft_Auto_VI` buscando «Windows».
2. Si alguna fuente anuncia versión de PC, **no se publica**: el golpe 1 y el remate dejan de ser ciertos, la marca de la pestaña pasa
   a punto y se informa al dueño.
3. Si no la hay, se cambia la fecha por la de esa relectura en **tres lugares**: el sello de pantalla «as of» (código, no toca la
   voz), la primera línea de la descripción y la línea «Facts as of» del descargo. Las fechas «read on» de las fuentes se
   cambian solo de las páginas que se vuelvan a leer ese día (Rockstar, Take-Two, Wikipedia).
4. Al subir, en Studio: «No, it's not made for kids», sin restricción de edad, ningún aviso, y la respuesta de contenido alterado
   de la sección «Declaraciones al subir». Búsqueda del tema el día de publicar (autocompletado, Trends de YouTube a 7 días,
   Studio → Investigación) la hace el Manager, según su método; aquí quedan las de 2026-11-26.

## Búsqueda en que se apoya

Lecturas del Generador del 2026-11-26 (Google Trends «Explorar», Estados Unidos, valores relativos de 0 a 100 dentro de cada
comparación; ninguno es volumen absoluto: **volumen absoluto, sin dato**). Los archivos están en `estadisticas/datos/` y no se
suben; aquí van descritos en palabras.

- **Qué se escribe.** En la búsqueda de YouTube, a 7 días, «gta 6 pc» es el ángulo de GTA 6 más buscado de los cinco que se
  compararon y el único que no cae en la semana; «gta 6 map» cae a menos de la quinta parte y «what is gta 6» baja despacio. Entre
  las 25 consultas principales de «gta 6 pc», «gta 6 on pc» es la segunda (97 frente a 100 de la primera, «gta on pc»); las variantes
  «how to play gta 6 on pc», «how to get gta 6 pc» y «gta 6 pc release date» también están en la lista. Lectura de las 23:26.
- **Cómo lo completa la gente.** Autocompletado de YouTube (servicio público de sugerencias, sin sesión, inglés, EE. UU.,
  2026-11-26): al escribir «is gta 6 coming » la primera sugerencia es «is gta 6 coming to pc»; «when is gta 6 coming to pc» abre la
  lista del inicio «when is gta 6 coming»; «is gta 6 on pc» es la segunda de su inicio.
- **Frase elegida para el título:** «is gta 6 coming to pc» (la pregunta que contesta el video, tal como la completa YouTube).
  «gta 6 on pc» es la consulta con mejor puesto en Trends y va en la portada y en la primera etiqueta.
- **Qué se descarta.** Todo lo que sube en las consultas «en ascenso» es el port no oficial y una filtración (nombres propios del
  proyecto, «exe», «port race», «tracker», «leak»). No se nombra, no entra en título, descripción, etiquetas ni hashtags.
- **Mercados.** Studio mide EE. UU. primero, luego Filipinas e India. El autocompletado de Filipinas e India también trae «is gta 6
  coming to pc» (2026-11-26, anexo del archivo de puntuación del Motor). Este paquete es solo en inglés: el canal publica en
  inglés (brief). Paquetes en español y portugués: no se piden para este short.
- **Lo que la búsqueda no hace en este canal.** Casi todo el tráfico llega del feed de Shorts y la búsqueda es marginal (Studio,
  2026-11-26): el título se mide por «se quedó a mirar», no por tráfico de búsqueda (`PARAMETROS.md`, parámetro «Título»).
- **Referencias de otros canales:** no abrí videos de otros canales para este paquete. Sin dato; no se copia ningún título.
- **Derivados:** ninguno planeado. El video ya es un Short y no se parten Shorts de un Short.

## Título

**Is GTA 6 Coming to PC? Here's What's Announced**

**El candidato del brief no pasa el filtro.** `Is GTA 6 Coming to PC? Here's What's Official` (45 caracteres) da **1 error** (regla
M8: «official» está en la lista de promesas engañosas evidentes; `titulos.md`, tabla de parámetros flexibles, fila M8, y `revisar_titulo.py`
v1.1). No hay forma de dejarlo: es un error, no un aviso. Se cambia una sola palabra: «Official» por «Announced», que además es
la palabra que usa el video («Not announced.»). «Official» sí puede ir en la voz y en la pantalla del final («No official PC
date»): el filtro es solo de títulos. Salida del candidato original, corrida hoy:

```text
Filtro de títulos v1.1 (flexible) · «Is GTA 6 Coming to PC? Here's What's Official» · 45 caracteres · tin-y-tan · en · short
  ERROR  M8 término bloqueado (línea editorial o promesa engañosa): «official»
NO PASA: 1 error(es), 0 aviso(s).
```

### Título (ficha)

Filtro: `revisar_titulo.py` versión 1.1 (modo flexible), corrido el 2026-11-27 con
`--canal tin-y-tan --idioma en --formato short --frase "is gta 6 coming to pc" --marca "GTA 6" --descripcion <la descripción de abajo>`.
No se usó `--registrar`: el título se anota en `titulos_usados.json` cuando el dueño apruebe el paquete.

| Campo | Valor |
|---|---|
| `titulo_elegido` | Is GTA 6 Coming to PC? Here's What's Announced |
| `caracteres` | 46 (los cuenta el filtro) |
| `idioma` | en |
| `canal` | tin-y-tan |
| `formato` | short |
| `publico` | EE. UU. primero, luego Filipinas e India; casi todo menor de 45 años, mayoría hombres, tramo de 13 a 17 el mayor en el short de juegos (Studio, 2026-11-26) |
| `frase_de_busqueda` | is gta 6 coming to pc |
| `fuente_de_la_frase` | Autocompletado de YouTube (suggestqueries, ds=yt, hl=en, gl=us), leído 2026-11-26: primera sugerencia de «is gta 6 coming ». Trends: «gta 6 on pc», puesto 2 de las 25 consultas de «gta 6 pc», YouTube, 7 días, EE. UU., 2026-11-26 23:26. Volumen absoluto: sin dato |
| `formula` | F2 (pregunta con el nombre propio del tema, dentro de los primeros 40 caracteres) + cierre que dice qué entrega el video |
| `alternativa_1` | Is GTA 6 Coming to PC? How Long Past Games Took (47) |
| `alternativa_2` | Is GTA 6 Coming to PC? Here Are the Facts (41) |
| `uso_de_las_alternativas` | Reserva. YouTube no ofrece prueba A/B en Shorts (https://support.google.com/youtube/answer/16391400?hl=en, `titulos.md` Y13); no se cambia un título publicado antes de los 28 días y sin datos del canal |
| `filtro` | versión 1.1, fecha 2026-11-27, resultado **PASA** (las tres opciones), errores: ninguno, avisos: ninguno (la salida de las tres está abajo) |
| `revision_humana` | **Pendiente.** Riesgo que firma una persona: «Here's What's Announced» no promete fecha ni descarga, pero el lector puede esperar un anuncio; el video responde «Not announced.» en ≈ 3,0 s (antes del segundo 5) y entrega dos precedentes con fecha. Firma el director creativo con el video terminado. Alternativa 1 promete «cuánto tardaron»: el video lo cumple con 574 días y cerca de un año |
| `medicion` | Short: «se quedó a mirar» (visto frente a deslizado) y «mostrado en el feed» a 48–72 horas, 7 y 28 días; meta: no más de 5 puntos por debajo del video de comparación (sección «Objetivos y metas»); búsqueda de YouTube como fuente: establecer línea base |

Por qué esta forma (`titulos.md`): la frase de búsqueda empieza en el carácter 1 y termina en el 21 (antes del 40); Title Case
con las palabras menores en minúscula; una sola «?» y ningún «:»; sin cifras, sin emoji, sin hashtags; «GTA 6» es el tema del
video y va como marca autorizada con el descargo «Not affiliated with…» en la descripción (M11). No lleva «confirmed», «release
date», «leaked», «download», «PC version is here» (F9 del archivo de hechos). La cifra de la respuesta (574, 375) no va en el título.

**Salida del filtro de las tres opciones** (con la descripción de abajo; recuentos de caracteres del propio filtro):

```text
Filtro de títulos v1.1 (flexible) · «Is GTA 6 Coming to PC? Here's What's Announced» · 46 caracteres · tin-y-tan · en · short
PASA: 0 error(es), 0 aviso(s). Falta la revisión de una persona (el video cumple el título, no engaña, línea editorial).
  filtro: {"version": "1.1", "modo": "flexible", "fecha": "2026-11-27", "resultado": "PASA", "errores": [], "avisos": []}

Filtro de títulos v1.1 (flexible) · «Is GTA 6 Coming to PC? How Long Past Games Took» · 47 caracteres · tin-y-tan · en · short
PASA: 0 error(es), 0 aviso(s). Falta la revisión de una persona (el video cumple el título, no engaña, línea editorial).
  filtro: {"version": "1.1", "modo": "flexible", "fecha": "2026-11-27", "resultado": "PASA", "errores": [], "avisos": []}

Filtro de títulos v1.1 (flexible) · «Is GTA 6 Coming to PC? Here Are the Facts» · 41 caracteres · tin-y-tan · en · short
PASA: 0 error(es), 0 aviso(s). Falta la revisión de una persona (el video cumple el título, no engaña, línea editorial).
  filtro: {"version": "1.1", "modo": "flexible", "fecha": "2026-11-27", "resultado": "PASA", "errores": [], "avisos": []}
```

(Los tres bloques de `filtro` son los que imprime el script en «Bloque para la ficha»; aquí van en una línea.) Descartada
una cuarta opción, «…What We Know So Far»: pasa con 1 aviso (M6, «So» en minúscula en Title Case) y se prefirió una sin aviso.

## Descripción (inglés)

La fecha «as of November 27, 2026» es la de la última lectura y se cambia por la de la relectura del 2026-12-04 (primera línea y
descargo). Primera línea: la respuesta fechada (lo pide la dirección, sección 8). Segunda: qué entrega el video. 3.664 bytes
(el límite de YouTube es 5.000); 3 hashtags.

```text
Is GTA 6 coming to PC? Not announced: Rockstar and Take-Two have not announced a PC version, a date or system requirements, as of November 27, 2026.
Tin and Tan check it, add how long the last two Rockstar games took to reach PC, and say why files that claim to be "GTA 6 for PC" are not from Rockstar.

What the video says:
- Not announced. Rockstar's page for the game lists PlayStation 5 and Xbox Series X|S and does not mention PC or Windows. That is an absence, not a prediction: it does not mean there will never be a PC version, and it does not mean there will be one.
- GTA 6 came out on November 19, 2026, on PlayStation 5 and Xbox Series X|S.
- GTA 5 reached PC 574 days after its console release: September 17, 2013 to April 14, 2015. About a year and a half.
- Red Dead Redemption 2 took about a year: October 26, 2018 on consoles, November 5, 2019 on Windows. The count starts from its first Windows release.
- Files that say "GTA 6 for PC" are not from Rockstar. Security companies have documented fake GTA 6 downloads that carry malware. Don't download them.

Also good to know, not said in the video:
- GTA 6 is rated M (Mature 17+) by the ESRB: seventeen and over.
- PlayStation asks for at least 212 GB of free space on PS5. There are no official PC requirements. Steam lists 125 GB of storage for GTA 5 and 150 GB for Red Dead Redemption 2. These measure different things (free space asked on a console, storage asked on PC), so they are not a forecast.
- Steam shows April 13, 2015 for GTA 5 on PC (573 days) and December 5, 2019 for Red Dead Redemption 2 (405 days). The video uses the dates from Wikipedia and says "about a year" for the second game because of this difference.

Sources, all read on November 27, 2026 unless noted:
- Platforms and no mention of PC or Windows (Rockstar Games): https://www.rockstargames.com/VI
- Release on November 19, 2026 (Take-Two, list of press releases; PlayStation): https://www.take2games.com/ir/press-releases and https://www.playstation.com/en-us/games/grand-theft-auto-vi/
- 212 GB of free space on PS5 (PlayStation): same PlayStation page
- Release dates of GTA 5 and Red Dead Redemption 2 (Wikipedia): https://en.wikipedia.org/wiki/Grand_Theft_Auto_V and https://en.wikipedia.org/wiki/Red_Dead_Redemption_2
- Steam dates and storage (Steam store data): https://store.steampowered.com/api/appdetails?appids=271590 and https://store.steampowered.com/api/appdetails?appids=1174180
- Fake GTA 6 downloads with malware (Malwarebytes, August 24, 2026): https://www.malwarebytes.com/blog/news/2026/08/fake-gta-6-extended-look-and-demo-sites-deliver-an-infostealer
- Fake GTA 6 downloads with malware (Huntress, September 9, 2026): https://www.huntress.com/blog/fake-gta6-download-malware-analysis
- Rating, Mature 17+ (ESRB, read November 26, 2026): https://www.esrb.org/search/?searchKeyword=grand+theft+auto+vi
- The count: September 17, 2013 to April 14, 2015 is 574 days; October 26, 2018 to November 5, 2019 is 375 days (date difference).

Subscribe to Tin & Tan. We check the facts.

Tin & Tan is an independent channel. Not affiliated with, endorsed by, or sponsored by Rockstar Games, Take-Two Interactive, Sony Interactive Entertainment (PlayStation) or Microsoft (Xbox). Grand Theft Auto, GTA, Rockstar Games, Take-Two Interactive, PlayStation and Xbox are trademarks of their respective owners and are named only to say what this video is about. No footage, images, music or characters from the game are used. This channel does not link to, host or support unofficial or pirated versions of any game. Rated M (Mature 17+) by the ESRB. Facts as of November 27, 2026.

#GTA6 #GTA6PC #TinAndTan
```

**Estado de cada dato de la descripción** (del archivo de hechos; nada se afirma de más):

| Dato | Fuente y estado |
|---|---|
| Ni Rockstar ni Take-Two han anunciado versión, fecha ni requisitos de PC | Página de Rockstar leída el 2026-11-27 (0 menciones de «PC» y de «Windows»), listado de comunicados de Take-Two (solo el listado; el cuerpo de cada comunicado no abrió) y tres fuentes independientes (Wikipedia, ZDNet, Malwarebytes). Comprobado; **caduca** |
| Salió el 2026-11-19 en PlayStation 5 y Xbox Series X\|S | Rockstar, PlayStation y el listado de Take-Two: tres primarias |
| GTA 5: 574 días | Fechas de Wikipedia (2013-09-17 y 2015-04-14) y cuenta con script (archivo de hechos, sección 3). Steam da 2015-04-13 (573 días): se dice en la descripción |
| RDR2: cerca de un año | 375 días con la fecha de Wikipedia (2019-11-05) y 405 con la de Steam (2019-12-05): por eso la voz dice «about a year» y no un número de días |
| Archivos falsos con programas maliciosos | Malwarebytes (2026-08-24) y Huntress (2026-09-09), leídos. Se dice «no son de Rockstar», nunca «todo lo que circula es falso» (parte de lo filtrado se reporta como real) |
| M (Mature 17+) | ESRB, PlayStation y distintivo de Rockstar, leídos para el short 4 (2026-11-26). Va solo en la descripción (decisión C8 de la dirección) |
| 212 GB; 125 GB y 150 GB | PlayStation (leído 2026-11-27) y fichas de Steam por API (leídas 2026-11-27). Mide cosas distintas: la descripción lo dice. Va solo en la descripción (decisión C9 de la dirección) |

**Lo que no entra** (regla del dueño de no promover piratería; F7, F8, F9, F10): ningún nombre de proyecto, archivo, cuenta o
persona del port no oficial ni de la filtración; ningún enlace a descargas o repositorios; el rumor del «primer trimestre de
2027»; ninguna estimación de requisitos de la prensa; ninguna cifra de Kaspersky (no se leyó en su sitio); ninguna fecha
proyectada para GTA 6; nada del director ejecutivo de Take-Two ni de otras personas.

**Línea de suscripción:** una sola en la descripción, la que pide la dirección (sección 8) además de la voz. No hay otro pedido.

## Etiquetas, hashtags y otros campos

- **Etiquetas** (8; 128 caracteres con comillas y comas, el límite es 500): `is gta 6 coming to pc`, `gta 6 on pc`, `gta 6 pc`,
  `will gta 6 come to pc`, `gta vi pc`, `grand theft auto 6 pc`, `gta 6`, `Tin & Tan`. Sin «exe», «download», «leak», «free» ni
  «release date» (dirección, sección 8); sin palabras de público infantil; sin el nombre de ningún proyecto o port.
- **Hashtags** (3, al final de la descripción, los que YouTube muestra junto al título): `#GTA6 #GTA6PC #TinAndTan`. Verdaderos y
  del tema; `#Shorts` no hace falta (método de metadatos del Manager, y `titulos.md` Y15). Ninguno en el título.
- **Categoría:** 24, Entretenimiento. **Idioma del video:** inglés (`en`).
- **Lista de reproducción:** sin dato (no encontré una definida para el canal en el repositorio); decide el Manager.
- **Subtítulos:** **no se sube ninguna pista `.srt` a YouTube** (regla del dueño, 2026-11-26). Los subtítulos en español van quemados
  en la imagen. No se sube pista en inglés ni en español.

## Portada y miniatura

- **Miniatura:** el fotograma 0 (1080×1920). No se sube una miniatura aparte (no hay prueba A/B en Shorts). El fotograma 0 trae:
  monitor apagado sobre una pila de torres genéricas al centro, Tan a la izquierda y Tin a la derecha, de perfil, con caras de
  curiosidad, el lápiz en el pasillo, la pestaña de cartón al fondo y la caja registradora rota en un extremo del suelo. Personajes
  grandes, una sola idea (la pregunta sobre PC), se entiende sin leer el título. Ninguna imagen, logotipo, tipografía ni color del
  juego; el monitor está apagado: es lo que hay de GTA 6 en PC.
- **Texto propuesto por el director creativo:** «GTA 6 on PC?» / «Facts, Checked» (`direccion.md`, 9.2).
- **Comprobación contra la regla de portada** (`DESIGN.md`, «Portada de los Shorts»: mayúscula inicial en cada palabra, de partida
  4 palabras en 2 líneas, nombra al sujeto, no da la respuesta ni insinúa fecha o descarga):

| Regla | ¿Cumple? | Lectura |
|---|---|---|
| Nombra al sujeto con la consulta medida | Sí | «GTA 6» y «PC» son la consulta; «gta 6 on pc» es el puesto 2 de Trends |
| No da la respuesta ni insinúa fecha o descarga | Sí | Termina en «?»; «Facts, Checked» es el lema del canal, no promete nada |
| Dos renglones | Sí | |
| Mayúscula inicial en cada palabra | **No** | «on» va en minúscula |
| Máximo 4 palabras | **No** | Son 5 palabras y una cifra (GTA, on, PC, Facts, Checked, y el 6). La regla es «de partida», o sea flexible, pero el short 4 usó «GTA 7?» / «Facts, Checked» (3 palabras y una cifra) |

  **No la cumple en dos puntos.** Cambio mínimo que sí la cumple: **«GTA 6 PC?» / «Facts, Checked»** (4 palabras y una cifra,
  todas con mayúscula, y «gta 6 pc» es el ángulo más buscado de la semana). Si el director creativo prefiere conservar
  «on PC», la salida es «GTA 6 On PC?», que cumple la mayúscula y sigue en 5 palabras. **La decide el director creativo**; la portada
  forma parte del fotograma 0 y de la firma (empalma con el cierre), así que yo no la cambio.

## Declaraciones al subir

| Campo de Studio | Respuesta | Por qué |
|---|---|---|
| ¿Es contenido para niños? | **No, it's not made for kids** | Tema de un juego clasificado M (17+), tramo mayor de 13 a 17, lenguaje y formato de acción; título y etiquetas sin palabras de público infantil. **Es decisión legal del dueño** y está anotada en el método del Manager |
| Restricción de edad | Ninguna | El video no muestra el juego, ni sangre ni armas de fuego; la violencia es de dibujo |
| Contenido alterado o sintético | **Sí, se declara: la voz de los personajes es generada con IA (Higgsfield); el dibujo y los sonidos son código** | La respuesta prudente que ya usa el canal (short 4: «se declara en Studio»; `plan_programa_de_socios.md`, sección de IA). La página de YouTube dice que declarar no limita al público ni a la monetización (https://support.google.com/youtube/answer/14328491?hl=en, leída por el plan el 2026-11-23). **Contradicción con el método del Manager:** `metodo de metadatos` recomienda `containsSyntheticMedia=false` mientras no haya escenas realistas y deja la decisión al dueño. Aplico la práctica del short 4 y se lo señalo al dueño; la línea «Voices are AI-generated» **no se agrega** a la descripción (dueño, 2026-11-26: «No por ahora») |
| Promoción pagada | No | Sin patrocinio ni colocación de productos |
| Visibilidad al subir | Privado, hasta el sí del dueño | Regla del método del Manager |
| Comentarios | Los de un canal «no creado para niños» (activos) | Si un comentario dice que el video no respondió la pregunta, es señal de F9; si nombra el telescopio, la pestaña, la grieta o la caja, se copia al registro de pistas (privado) |
| Licencia | Estándar de YouTube | Todo es propio (`licencias.md`) |

## Límites de la plataforma que aplican

- **No hay prueba A/B de títulos ni miniaturas en Shorts** («You are not able to A/B test Shorts», https://support.google.com/youtube/answer/16391400?hl=en,
  `titulos.md` Y13). Las dos alternativas son reserva.
- **En la descripción de un Short los enlaces no se pueden tocar** (método del Manager, regla 9). Las fuentes van como texto; se
  citan solo páginas de las empresas, de los dos avisos de seguridad y de Wikipedia, ninguna de descargas.
- **Pantalla final y tarjetas en Shorts:** sin verificar; no se planea con ellas.
- **Hechos que caducan:** el anuncio de PC (relectura del 2026-12-04, arriba). Un aviso de Normas de la Comunidad impide solicitar
  el Programa de socios: se confirma «sin avisos» en Studio al subir (F13).
- **Un Short ya público no se reemplaza por otro casi igual** (`PARAMETROS.md`, bitácora 2026-11-26): si el video se corrige, es en
  el siguiente.

## Objetivos y metas medibles

**Objetivo comercial (dueño, 2026-11-23):** entrar al Programa de socios de YouTube lo antes posible. **Metas del plan**
(`canales/nostalgia-tin-y-tan/plan_programa_de_socios.md`, secciones 1, 3.4 y 3.5; páginas oficiales leídas el 2026-11-23):
primer hito, el nivel intermedio: 500 suscriptores, 3 subidas públicas válidas en 90 días y 3 millones de vistas calificadas de
Shorts en 90 días (o 3.000 horas en 12 meses), que no cambia el 2027-02-01; segundo hito, el nivel alto: 1.000 suscriptores y 10
millones de vistas calificadas de Shorts en 90 días hasta el 2027-01-31 (20 millones desde el 2027-02-01; 4.000 u 8.000 horas por el
otro camino). El plan dice que se planea contra los umbrales nuevos y que el 31-ene es un caso afortunado. **Plazo:** «lo antes
posible»; fecha de revisión del plan, 2026-12-07. Este video aporta vistas calificadas; **no tiene una meta de vistas propia
porque el canal no tiene base** (dos videos con datos, ningún suscriptor): se mide contra otro video.

**Video de comparación, a la misma edad:** el **short 4** (`TIN-EN-S-004`) si ya está público; **hoy no lo está** (calendario:
2026-12-02, 16:00). Si el 12-04 no ha salido o aún no tiene la edad, el **short 2**. Las cifras de comparación están en
`estadisticas/datos/` (no se suben) y aquí no se copian.

| Cuándo | Indicador | Meta | De dónde sale la meta | Dónde se lee |
|---|---|---|---|---|
| **48–72 horas** (2026-12-06 y 12-07, 16:00) | «Se quedó a mirar» (visto frente a deslizado) | No más de 5 puntos por debajo del video de comparación a la misma edad. **Es el KPI principal** | Brief y dirección, sección 1 («a prueba») | Studio → Analytics del Short → Interacción (visto frente a deslizado; en la página de ayuda figura como «How many chose to view», `titulos.md` Y20) |
| 48–72 h | Fila «Feed de Shorts» en las fuentes de tráfico | Presente | Brief, «Estrategia»: el feed es lo que reparte | Studio → Alcance → fuentes de tráfico |
| 48–72 h, 7 días y 28 días | Avisos de Normas de la Comunidad o de monetización | Ninguno | Brief: un aviso cuesta la admisión (F13) | Studio → contenido, columna «Avisos» |
| 48–72 h | Retención en el segundo 3 y en los segundos 5 a 10 | **Establecer línea base**; leerla contra el video de comparación | En los dos videos medidos la caída fuerte estuvo entre los segundos 5 y 10 (Studio, 2026-11-26); aquí «Not announced.» entra a ≈ 3,0 s. Sin cifra propia ni base para fijar una meta numérica | Studio → Interacción → retención de audiencia, por segundo |
| 48–72 h | **Escalón de retención en ≈ 19,2 s** (cae el telescopio; plan f576) | **Ningún escalón** (lo descarta: un escalón en ese segundo) | Brief, «Lo confirma / lo descarta» | Misma curva; lectura abajo |
| 48–72 h y 7 días | Retención entre ≈ 13 y ≈ 17 s (invitación a suscribirse, ≈ 14,6 a ≈ 15,7 s) | Establecer línea base | Estreno del pedido a mitad del video (`PARAMETROS.md`, «Pedir la suscripción», a prueba) | Misma curva; separada del telescopio por ≈ 3,5 s |
| 7 días (2026-12-11) | Suscriptores por mil vistas | Establecer línea base | Hoy: 0 suscriptores y 0 comentarios en todo el canal (Studio, 2026-11-26) | Studio → Audiencia / suscriptores por contenido |
| 7 días | Pico en ≈ 23,3 a ≈ 24,4 s (el paquete revienta) y caída o no al oír «No official PC date» (≈ 27,1 s en adelante) | Establecer línea base | Sin dato propio | Misma curva |
| 7 días y 28 días | Porcentaje medio visto y duración media | Establecer línea base; no más de 5 puntos por debajo del video de comparación | Brief (retención) | Studio → Interacción |
| 7 días y 28 días | Fuente «búsqueda de YouTube» y términos de búsqueda que trajeron gente | Establecer línea base; mirar si aparece «gta 6 on pc» o «is gta 6 coming to pc» | La búsqueda es marginal en este canal; sus términos no tenían relación con los videos (Studio, 2026-11-26) | Studio → Alcance → «Cómo encuentran tu video» |
| 7 días y 28 días | Comentarios, compartidos, público que regresa | Establecer línea base | Hoy en cero | Studio |
| 28 días (2027-01-01) | Lectura final del paquete: título, portada y descripción frente al video de comparación | Decisión sobre el patrón de gancho «la pregunta tal cual, con la respuesta delante» (`metodo/ganchos.md`) | Un video no decide (`PARAMETROS.md`, sección 4): se anota «a prueba» | Todo lo anterior |

**Lectura del escalón de retención en ≈ 19,2 s.** El telescopio cae en el plano 17, f576–f587 (rebote f588–f595), sin voz y 23
fotogramas después de «about a year» (f553). Cómo se lee, con la voz real y el render final (el segundo exacto se recalcula
cuando el editor entrega la línea de tiempo):
1. Marcar en la curva los segundos s − 2, s y s + 2, con s = el segundo de la caída del telescopio en el render final (hoy ≈ 19,2 s
   → 17,2 s, 19,2 s y 21,2 s). La resolución por segundo de la curva de Studio en un Short: **sin dato**; se lee a lo que dé la gráfica.
2. Calcular la pérdida por segundo en el tramo anterior (17,2 → 19,2) y en el posterior (19,2 → 21,2), y la pérdida en el segundo
   que sigue a la caída.
3. **Hay escalón** si la pérdida en el segundo de la caída es claramente mayor que la de los dos tramos vecinos. Umbral de partida:
   **el doble** de la media por segundo de los dos tramos vecinos (**hipótesis del equipo**, sin base propia: es el primer video con
   un objeto que cae; se afina con los datos). No hay escalón si la curva sigue la pendiente de los vecinos.
4. Antes de atribuirlo al telescopio, descartar los otros dos eventos cercanos: la invitación (≈ 14,6–15,7 s, más de 3 s antes) y
   la tarjeta «Red Dead Redemption 2» que sale en f570–f572 (≈ 19,0–19,1 s, justo antes). Si hay caída en ≈ 19 s y la curva de esa
   tarjeta explica el cambio, se anota «no atribuible al telescopio».
5. **Resultado:** sin escalón confirma el mecanismo M1 (un objeto ajeno que cae sin frenar a quien mira); con escalón lo
   descarta (brief). Un video no decide: se repite en el short 6, donde el telescopio vuelve.

Para las fechas, si el video se publica otro día, las lecturas se mueven con él: 48 h, 72 h, 7 días y 28 días contados desde la hora
real de publicación (si sale el 2026-12-04 a las 16:00: 12-06, 12-07, 12-11 y 2027-01-01).

## Filtro de políticas sobre el guion final

**Qué se revisó.** Las líneas 1 a 12 de la sección 2.2 de `direccion.md` (voz en inglés, exacta), la sección «Estado de cada
frase», el título elegido y las dos alternativas, la descripción y la portada propuesta. **Qué no se revisó:** el video terminado
(no existe), la sección 11 de la dirección salvo para confirmar que no cambia ninguna frase de voz (no cambia: dice que ninguna
decisión cambia una frase), y la voz real.

**Páginas de YouTube abiertas hoy (2026-11-27, ≈ 06:28 UTC, `curl -sS -m 40 -A "Mozilla/5.0"`, texto completo leído).** Ninguna
de las tres muestra fecha de última modificación en el texto que se descarga; las citas son literales.

| Política | URL | Cita textual (inglés) | Qué aplica a este guion |
|---|---|---|---|
| Spam, prácticas engañosas y estafas | https://support.google.com/youtube/answer/2801973?hl=en | «Malicious clickbait: Using maliciously misleading titles, thumbnails, descriptions, or imagery to trick users into clicking on a video that does not deliver what was promised.» | El título pregunta y el video contesta «Not announced.» en ≈ 3,0 s y entrega dos precedentes con fecha: cumple lo que promete. Lo firma una persona con el video hecho |
| (misma) | (misma) | «Off-platform diversion: Content created solely to drive users off of YouTube to external sites, especially those hosting prohibited material like malware, adult content, or illegal goods/services.» | Ninguna línea ni la descripción lleva a un sitio de descargas; los únicos enlaces son páginas de las empresas, dos avisos de seguridad y Wikipedia. El video hace lo contrario: avisa |
| (misma) | (misma) | «It's okay to ask viewers to like, comment, or subscribe.» | La línea 7 («Subscribe for facts, checked.») es una invitación permitida: no ofrece recompensa ni pide «sub por sub» |
| (misma) | (misma) | «Detection evasion: Technical manipulation (such as speeding up audio, heavy filters, cropping) designed to bypass abuse detection.» | La voz se acelera un 10 % en edición. **Es para el ritmo, no para evadir ninguna detección** (voz propia y generada, sin material de terceros). Se anota porque la política nombra «speeding up audio» como ejemplo; el criterio es el propósito |
| (misma) | (misma) | «Creators should disclose when content is generated or meaningfully altered with AI, but this disclosure is not a free pass to violate our policies.» | Se declara la voz generada al subir (sección «Declaraciones al subir») |
| Contenido dañino o peligroso | https://support.google.com/youtube/answer/2801964?hl=en | «Bypassing payment for digital content or services: Content that shows viewers how to get unauthorized access to content, software, or services that usually require payment.» (bajo «Digital security content») | **Es la línea más cercana a «piratería» que dice YouTube hoy.** El guion no muestra cómo, dónde ni con qué nombre se consigue nada no autorizado: dice que esos archivos no son de Rockstar, que algunos traen programas maliciosos y que no se descarguen. Es lo contrario de enseñar a acceder |
| (misma) | (misma) | «These policies also apply to external links in your content. This can include clickable URLs, verbally directing users to other sites in video, as well as other forms.» | La voz no dirige a ningún sitio; la descripción solo enlaza fuentes. Ningún enlace a descargas ni a repositorios |
| Desinformación | https://support.google.com/youtube/answer/10834785?hl=en | «Certain types of misleading or deceptive content with serious risk of egregious harm are not allowed on YouTube.» Lista: «Suppression of census participation», «Manipulated content», «Misattributed content» | **La política no cubre este tipo de afirmación** (un hecho de producto con fecha). El riesgo de decir algo falso es nuestro control F8: fuente y fecha de cada frase, sello «as of» y relectura el día de publicar. No hay en el guion contenido manipulado ni filmaciones de otro suceso |
| Derechos de autor | https://support.google.com/youtube/answer/2797466?hl=en | Sin mención de piratería ni de acceso no autorizado en el texto (búsqueda de «pirac», «circumvent», «unauthorized», «infring»: 0) | No aplica a este guion: todo es propio |
| Monetización: contenido inauténtico | https://support.google.com/youtube/answer/1311392?hl=en | «Generic or repetitive content includes content that looks like it's made with a template, or that may feel repetitive to viewers after watching several videos in a row from the same channel.» / «Videos where characters are put in the same situation over and over again with the same outcome» | Es el tercer short de GTA 6 (F6). Cambian la pregunta, la forma de explicar (medir dos precedentes), la hoja, la paleta, el entorno y la estructura (respuesta primero). Condición: si al ponerlo seguido del short 4 se parece, se avisa antes de publicar |

**No abrí** la política «Illegal or regulated goods or services» ni la de seguridad infantil; no aplican al guion (no se vende
nada, no aparece ningún menor) pero la primera es la que cita la página de contenido dañino para bienes ilegales: queda anotado.

### Línea por línea

| # | Voz (exacta) | Resultado | Por qué y condición |
|---|---|---|---|
| 1 | «Is GTA 6 coming to PC?» | **Pasa** | Es la pregunta medida. F9: se contesta en la línea 2, ≈ 3,0 s |
| 2 | «Not announced.» | **Pasa con condición** | Verdad hoy (página de Rockstar sin PC ni Windows; Take-Two sin comunicado de PC). **Caduca:** relectura el 12-04. Dice «not announced», nunca «won't» ni «will» |
| 3 | «Rockstar hasn't announced a PC version.» | **Pasa con condición** | Misma ausencia. Con el sello «as of» en pantalla. Solo nombra a Rockstar; la descripción dice «Rockstar and Take-Two» (ambos comprobados) |
| 4 | «It's on PlayStation 5 and Xbox Series X and S.» | **Pasa** | Tres primarias (Rockstar, PlayStation, Take-Two). No dice «solo»: no afirma que sea solo en consolas para siempre |
| 5 | «How long last time?» | **Pasa** | Pregunta sin dato |
| 6 | «GTA 5 took about a year and a half to reach PC.» | **Pasa** | 574 días ≈ 1,57 años: «año y medio» es exacto; «casi dos años» (ZDNet) se descartó. Pantalla: «574 days» con las dos fechas. Steam da 573: la descripción lo dice. No proyecta nada para GTA 6 |
| 7 | «Subscribe for facts, checked.» | **Pasa** | Invitación permitida («It's okay to ask viewers to… subscribe»). Una sola; sin promesa de tema ni recompensa |
| 8 | «Red Dead Redemption 2: about a year.» | **Pasa** | 375 días (Wikipedia) o 405 (Steam): «cerca de un año» sirve a las dos. La pantalla dice «≈ 1 year» y las fechas de Wikipedia |
| 9 | «Files that say 'GTA 6 for PC' are not from Rockstar.» | **Pasa con condición** | No enseña a conseguir nada: no nombra proyecto, archivo, cuenta ni lugar; no dice qué tal corre. Su cita («GTA 6 for PC») es el nombre con que circulan las estafas, y aquí va como advertencia. **Condición:** en pantalla y en subtítulo, ningún icono, ventana, nombre de archivo ni «.exe» (el paquete de tinta es una caja lisa); la descripción no repite la frase como etiqueta ni hashtag |
| 10 | «Some carry malware.» | **Pasa con condición** | Respaldada por dos avisos de empresas de seguridad (Malwarebytes, 2026-08-24, un ladrón de contraseñas; Huntress, 2026-09-09, una imagen ISO con instalador falso, programas de control remoto, ladrón de datos y un programa de secuestro). «Some» es exacto: no dice «todos» ni «todo lo que circula» (parte de lo filtrado se reporta como real) y no dice que otros sean seguros. **Condición:** la pantalla trae las dos fuentes con fecha, tal como está en 2.2 |
| 11 | «Don't download them.» | **Pasa** | Es un consejo, no un hecho (lo dice Tan, no Tin). «Them» remite a los archivos de la línea 9 |
| 12 | «No official PC date. As of today.» | **Pasa con condición** | Repite la ausencia con fecha; «as of today» una sola vez; el sello de pantalla lleva la fecha de la relectura. **«Official» está bien en la voz y en pantalla** (cita de lo que no existe); solo está bloqueada en el título (M8) |

**Veredicto sobre las líneas de malware (9, 10 y 11): pasan; no hace falta cambiar ninguna palabra.** Ninguna enseña ni dirige a
material no autorizado; las tres juntas dicen «no son oficiales, algunos traen malware, no los descargues». Dos cambios mínimos
**opcionales**, solo si el director creativo o la psicóloga lo piden, y yo no los pido:
- Línea 10: cambiar «Some carry malware.» por «Fake ones carry malware.» **empeora** el hecho (llama falso a todo lo que circula,
  y no está comprobado): se desaconseja.
- Línea 9: si alguien teme que «'GTA 6 for PC'» entre como búsqueda, el cambio mínimo es quitar las comillas del texto de
  pantalla; el hecho no cambia. No lo pido: la cita es la que reconoce quien busca ese archivo.

### F1 a F13 (y E1 a E3) sobre el guion final

| # | Resultado | Nota |
|---|---|---|
| F1, F2, F4 | Pasa | Violencia de dibujo, sin heridas ni sangre; ninguna persona real recibe golpes; nada del juego. F2: sin restricción de edad |
| F3 | Pasa con condición | «No creado para niños»; título, descripción y etiquetas sin palabras de público infantil; «malware» y «descargas» atraen a menores: el video no enseña nada |
| F5 | Pasa | Solo armas de tinta (regla); ninguna de fuego |
| F6 | Pasa con condición, riesgo medio-alto | Tercer short de GTA 6. Condición arriba (inauténtico) |
| F7, F12 | Pasa | Todo propio; nada del juego, de la filtración ni del port; `licencias.md` al día |
| F8 | Pasa con condición | Solo lo de la lista «se afirma»; todo hecho que caduca lleva el sello de fecha; sin rumores, sin estimaciones, sin cifra de Kaspersky |
| F9 | Pasa con condición | Respuesta en ≈ 3,0 s; título y portada sin fecha ni descarga; revisión humana del video terminado pendiente |
| F10 | Pasa | Marcas solo nombradas; ninguna persona nombrada (ni del port, ni de Take-Two, ni la persona menor del proyecto); descargo «Not affiliated with…» |
| F11 | Pasa con condición | Se declara la voz generada al subir |
| F13 | Pasa con condición | Sin avisos al subir; el aviso es lo que impide solicitar el Programa |
| E1 | Pasa | Sin identidad ni política; no entra en los motivos de quien filtró ni en la polémica de ediciones |
| E2 | **Punto abierto** | «Rated M» salió de la voz (decisión C8) y va en la descripción y en el descargo. El brief lo dejaba «si cabe sin frenar». El tramo de 13 a 17 es el mayor del canal: lo señalo, no lo bloqueo |
| E3 | Pasa | No promueve piratería ni ports: ningún nombre, enlace, cómo ni estado de avance |

## Controles de texto de este archivo

- `revisar_titulo.py` sobre las tres opciones: 0 errores y 0 avisos (con `--marca "GTA 6"` y la descripción de arriba).
- `revisar_texto.py --idioma en` sobre la descripción: el único error es el de siempre, ortografía sin comprobar por falta de
  Hunspell (no se instala sin el sí del dueño); el supervisor lee cada palabra y lo deja escrito en `07_revision/`. Sobre los
  títulos sueltos no corre (el script lee archivos, no cadenas).
- Pendiente antes de publicar: relectura del hecho que caduca (arriba), cambio de fecha, firma del director creativo sobre el título,
  decisión de la portada, `ficha.json` con el bloque de título, y que el Manager corra su `publicar.py revisar`.
