# Motor de contenido — cómo se arma un universo que se ajusta con estadísticas

> **Origen:** ideas del dueño del 2026-11-26, trabajadas con Tin & Tan. Textual: «en la medida que vayamos generando
> videos todos los elementos los vayas almacenando, por si caben o se quieren reutilizar»; «todas las limitantes que se
> presenten se resuelvan con creatividad […] es parte de la naturaleza del motor: al trabajar con estadísticas debe saber
> ajustarse»; «si el universo es un cuaderno, podrían haber más cuadernos; lo que generamos en Shorts, ¿cómo se transforma
> en un video más largo? […] se vuelve parte de cómo definimos conceptualización, universo de los personajes y contexto
> para el motor […] dejando definido, en caso tomemos otro caso de otros personajes o marcas […], qué es lo que tendríamos
> que definir al principio con otra marca o personajes para aprovechar al máximo el motor».
>
> **Qué es este archivo:** el método, sin secretos de ningún universo. Sirve para Tin & Tan y para cualquier otro
> personaje o marca. El caso de Tin & Tan está en `canales/nostalgia-tin-y-tan/PARAMETROS.md`; la pieza técnica que dibuja
> la acción, en `motor_de_accion/`. El dueño tiene otra conversación llamada «Motor generador de contenido»: cuando
> explique lo que falte, se integra aquí.
>
> **Estado:** versión 0.4 (2026-11-27: añade la puntuación de nicho y subnicho, sección 7b, escrita por la conversación
> «Motor generador de contenido»). Antes: versión 0.3 (añade el filtro de políticas de YouTube, sección 5b; los tres métodos que siguen al motor,
> sección 9; y el mapa en forma de grafo, sección 10). Antes: versión 0.2 (2026-11-26: se añade el método de investigación completo, secciones 6 a 9, por pedido del
> dueño: «Todo lo que investigaste este día en las diferentes plataformas debe quedar en el método del motor para poder
> definir el tema y con ello el prompt que lleva todos los detalles y fichas técnicas, incluida la estrategia, y con ello
> el Short o el video, y todo lo anterior considerando el universo definido»). Lo que es método probado lo dice; lo demás es **[hipótesis del equipo]**: hay dos videos
> medidos.

## 1. Las siete capas

Cada capa se define una vez, se guarda y se ajusta con datos. Ninguna se da por cerrada.

| # | Capa | Qué decide | Dónde vive (Tin & Tan) | Qué la ajusta |
|---|---|---|---|---|
| 1 | **Estadísticas y demanda** | A quién se le habla, qué busca, cuándo y desde dónde | `estadisticas/datos/` (no se sube), `comercial/radar_de_tendencias.md`, calendario de temporadas por país | Cada lectura de Studio; autocompletado y Trends antes de fijar una pregunta |
| 2 | **Conceptualización** | La metáfora que contiene todo (el «contenedor») y sus reglas | Biblia del universo (privada) | Limitantes y hallazgos: se resuelven dentro de la metáfora |
| 3 | **Personajes** | Quiénes son, qué no cambia nunca, quién es el rival o conflicto | `personajes/` | Solo el dueño cambia identidad; lo demás, variaciones permitidas |
| 4 | **Forma** | Cómo se cuenta: acción, pelea, tiempos, cámara, sonido | `PARAMETROS.md` sección 7; estudios de referencia | Retención por segundo; se quedó a mirar |
| 5 | **Biblioteca** | Todo elemento hecho: paletas, entornos, utilería, efectos, sonidos, poses, guiones | `motor_de_accion/catalogo.json` | Se añade tras cada video; nada se borra, se retira |
| 6 | **Conexión y plan** | Qué une un video con otro; tandas de 15 días a un mes; formatos por duración | Registro de pistas y plan de tanda (privados) | Regresos, suscriptores, comentarios; el tema entra tarde desde el radar |
| 7 | **Adaptación** | Qué se hace cuando algo falla o cambia | `PARAMETROS.md` sección 9 | Es la capa que mueve a las demás |

## 2. El contenedor: una metáfora con escalas

Un universo aguanta cualquier tema si su metáfora tiene **escalas**: cada tamaño de contenido es una unidad de la
metáfora. En Tin & Tan la metáfora es el papel:

| Escala | En el mundo real | En el universo de Tin & Tan | Formato |
|---|---|---|---|
| La unidad mínima | Un Short | **Una página** | 9:16, hasta ≈ 30 s |
| La unidad abierta | Un video largo | **El cuaderno abierto en doble página** (dos páginas lado a lado: por eso es horizontal) | 16:9, varios minutos |
| El universo alterno | Un tono o tipo de tema | **Una hoja** de otro papel (una por paleta) | cualquiera |
| La tanda | 15 días a un mes de producción | **Un cuadernillo** cosido: lo que se siembra y se cobra junto | — |
| La línea de contenido | Una serie, una temporada o un tema mayor | **Un cuaderno** | — |
| Todo lo del dueño o de la marca | Varios canales, personajes o marcas | **El estante**: cuadernos distintos que pueden prestarse hojas | — |

Reglas del contenedor:

1. **Lo corto y lo largo son la misma historia a otra escala.** El Short muestra una página; el video largo abre el
   cuaderno y deja ver lo que la página sola no muestra: cómo se tocan las páginas, qué quedó en los márgenes, por qué
   pasó lo que pasó. Un video largo nunca es un pegado de Shorts (política de contenido reutilizado): es la doble página.
2. **Para qué sirve el video largo:** (a) explicar el universo a quien ya vio varias páginas; (b) explicar con
   estadísticas un escenario actual de la realidad que no cabe en 30 segundos (varios asaltos, varias fuentes); (c) abrir
   el camino de horas del Programa de socios. Cuándo empieza lo decide el dato (regresos, comentarios), no el calendario.
3. **Más cuadernos:** cuando un tema mayor, una temporada u otro personaje no quepa en el cuaderno actual, se abre otro.
   Cada cuaderno tiene sus reglas; el estante dice cuáles pueden cruzarse. **Lo infantil está en otro estante y nunca se
   cruza** (regla del dueño).
4. **Toda limitante se traduce a la metáfora** (capa 7): un video sin distribución es una página arrancada; un orden
   roto, un cuaderno desencuadernado; un remake, pasar en limpio.

Otra marca u otros personajes no usan el papel: eligen **su** metáfora con el mismo criterio (sección 4, punto 5).

## 3. El ciclo de cada video

1. **Leer** estadísticas y demanda (capa 1). La pregunta del video se valida en datos de búsqueda, no en que existan
   videos parecidos.
2. **Recorrer el repertorio de ajustes** (capa 7): ¿algo cambió o falló desde el último video?
3. **Elegir** tema, paleta y entorno; decir qué conexión se cobra y cuál se siembra (capas 5 y 6).
4. **Brief** que abre con «Estadísticas en que se basa»; prompt validado; prueba completa (ninguna prueba a medias).
5. **Producir** con lo que haya en la biblioteca; lo nuevo entra al catálogo.
6. **Publicar** con el sí del dueño; **medir** a 48 horas, 7 días y 28 días.
7. **Ajustar** parámetros y universo con el dato, y anotarlo.

## 4. Qué hay que definir al principio con otra marca u otros personajes

La plantilla para llenar está en `plantillas/arranque_de_universo.md`. En resumen, antes del primer video:

| # | Qué | Por qué no se puede saltar |
|---|---|---|
| 1 | **Objetivo comercial** con métrica, meta y plazo | Todo se justifica contra él |
| 2 | **Accesos a los datos**: quién lee las estadísticas, cada cuánto y dónde se guardan | Sin dato no hay prompt |
| 3 | **Público y países reales** (o la hipótesis, marcada como hipótesis) y su calendario de temporadas | Tema, horario, idioma y color salen de aquí |
| 4 | **Lo que no se mueve**: identidad, manual de marca, tono, lo legal, lo que la marca no dice nunca, línea editorial | Es el borde de la creatividad |
| 5 | **La metáfora contenedora** y sus escalas (corto, largo, universo alterno, tanda, línea, estante) | Es lo que permite conectar y crecer |
| 6 | **Personajes**: quiénes, rasgos fijos, hoja de personaje, y **el conflicto o rival** (qué se enfrenta en cada pieza) | Sin conflicto no hay acción ni serie |
| 7 | **La firma**: lo que se repite en todos los videos y une uno con el siguiente | Reconocimiento y primera conexión |
| 8 | **La forma**: referencias medidas cuadro a cuadro, nivel de intensidad permitido, idioma, subtítulos | «Parecido a» sin medir es adivinar |
| 9 | **Paletas por tema**, con estudio de color sobre el público real | El color también se justifica |
| 10 | **Qué se promete y cómo se comprueba**: fuentes, qué se afirma y qué no | Confianza y políticas |
| 11 | **Canales y permisos**: cuentas, verificación, funciones disponibles, quién publica | Define qué conexiones existen |
| 12 | **Dinero y herramientas**: créditos, qué se puede instalar, en qué máquina se produce | Ruta de producción |
| 13 | **Quién decide qué** y qué necesita el sí del dueño o de la marca | Evita rehacer |
| 14 | **Dónde viven los secretos** del universo (nunca en un repositorio público) | Las teorías dependen de eso |
| 15 | **Qué se hereda del estante**: elementos de la biblioteca que sirven tal cual y cuáles nunca se cruzan | Aprovechar lo ya hecho |

Lo que el motor ya trae hecho y una marca nueva puede usar desde el primer día: el método de validación de preguntas, el
esqueleto de personajes 2D en mundo 3D, los efectos de acción, el sonido por código, la gramática de golpe medida, el
formato de biblia, registro de pistas y plan de tanda, el repertorio de ajustes y los controles de calidad.

## 5. De la investigación al video: la cadena completa

Cada eslabón sale del anterior. Si falta uno, no se pasa al siguiente (reglas «ningún prompt sin estadísticas» y
«ninguna prueba a medias»).

| Paso | Qué se hace | Con qué (sección 6) | Qué queda escrito |
|---|---|---|---|
| 1 | **Leer el canal** | Studio | Lectura con fecha y hora en `estadisticas/datos/` |
| 2 | **Leer el calendario** | Calendario de temporadas por país; radar | Qué fecha manda en la ventana y con cuánta antelación |
| 3 | **Medir el interés por tema** | Google Trends comparado | Qué tema domina y si sube o baja |
| 4 | **Sacar las preguntas reales** | Consultas relacionadas de Trends (las 25 + 25, web y YouTube) y autocompletado de YouTube y de Google | Lista de preguntas tal como se escriben |
| 5 | **Filtrar** | Lo que no se mueve del canal | Se quitan: lo que pide metraje ajeno, lo que no tiene fuente abierta, lo que choca con la línea editorial o con el tramo de 13 a 17 |
| 6 | **Mirar la oferta** | Listados de YouTube y pestaña «Investigación» de Studio | Qué hay ya hecho y cuánto rinde. Es oferta, **no** prueba de demanda |
| 7 | **Fijar tema y pregunta** | Pasos 3 a 6 | La pregunta del video, escrita como se busca, con su puesto en la lista |
| 7a | **Puntuar nicho y subnicho** | Sección 7b; estudio de potencial de pago | Tabla puntuada de candidatos, que es lo que recibe el Generador |
| 7b | **Filtro de políticas de YouTube** | Sección 5b | Cada renglón marcado «pasa», «pasa con condición» o «no pasa», con la cita |
| 8 | **Comprobar los hechos** | Fuente primaria o dos independientes | Cada dato con URL y fecha; qué se afirma y qué no |
| 9 | **Colocar el video en el universo** | Biblia, registro de pistas, plan de tanda, repertorio de ajustes | Hoja y paleta, entorno (nuevo o de la biblioteca), qué pista cobra y cuál siembra |
| 10 | **Brief** | Plantilla del proyecto | Abre con «Estadísticas en que se basa»; objetivo comercial; decisiones del equipo |
| 11 | **Dirección y fichas** (sección 8) | Equipo | Dirección, ficha técnica, perfil emocional, publicación, título, licencias |
| 12 | **Prompt** | `director-de-prompts`; `validar_prompt.py` | Prompt validado con todos los detalles; se archiva |
| 13 | **Prueba completa** | Motor de acción | Lleva todos los pedidos vigentes; se le presenta al dueño |
| 14 | **Producir, entregar, publicar** | Motor, `entrega.py`, publicador | Con el sí del dueño; en privado primero |
| 15 | **Medir y ajustar** | Studio a 48 h, 7 y 28 días | Bitácora de parámetros; biblioteca y registro de pistas al día |

## 5b. Filtro de políticas de YouTube (paso 7b; se repite sobre el guion final)

Un tema o un guion solo sigue si pasa todos los renglones. La cita exacta de cada política, con su enlace y fecha de
lectura, está en `estudios/2026-11-26_accion_stickman_y_tin_y_tan.md` (sección 1) y en
`estudios/2026-11-26_universo_conectado_investigacion.md`; se vuelven a leer cuando cambie una regla de la plataforma.

| # | Política | Qué se comprueba | No pasa si… |
|---|---|---|---|
| F1 | Contenido violento o gráfico | La violencia es de ficción animada, no gráfica | Hay tortura, desmembramiento, o intención de impactar o dar asco |
| F2 | Restricción por edad | Nada que la provoque: perdería a quien no inició sesión y a los menores de 18 | El foco es la violencia; un dibujo de aspecto familiar con temas adultos |
| F3 | Seguridad infantil y «creado para niños» | El canal y el video van «no creado para niños»; título y etiquetas no apuntan a niños | Aspecto infantil con violencia, muerte o armas realistas |
| F4 | Apto para anunciantes | Golpes sin herida visible, sin sangre como foco | Heridas graves a la vista; violencia contra personas reales con nombre |
| F5 | Armas de fuego | Solo armas dibujadas que no sean de fuego (decisión del canal) | Armas de fuego; instrucciones sobre armas |
| F6 | Contenido repetitivo o de plantilla | Cada video tiene tema, guion y desenlace propios; algo cambia y se queda | La misma situación con el mismo desenlace video tras video |
| F7 | Contenido reutilizado | Todo el dibujo, el sonido y la voz son propios o con licencia | Metraje, música o personajes ajenos; un video largo hecho pegando Shorts |
| F8 | Desinformación y teorías conspirativas dañinas | Una teoría como tema se explica y se contrasta con fuentes, con el contexto dentro del video | Se promueve; es de salud, elecciones, tragedias o señala a grupos (decisión del dueño) |
| F9 | Engañoso o clickbait | El video cumple lo que prometen el título y la portada; un adelanto no promete lo que no se va a cumplir | Promesa que el video no paga |
| F10 | Personas reales y marcas | Solo hechos públicos verificables; marcas solo nombradas | Cara, voz o frases inventadas de una persona real; logotipos o colores de marca |
| F11 | Contenido alterado o generado | Se declara lo que la plataforma pida declarar | Realismo generado sin declarar |
| F12 | Derechos de autor | Licencia de cada recurso en `licencias.md` | Un recurso sin origen |
| F13 | Requisitos del Programa de socios | Sin avisos activos; nada de vistas o suscriptores comprados | Cualquier atajo que cueste la admisión |

Si un renglón no pasa, se aplica la regla de adaptación: se cambia el ángulo, no se fuerza el tema.

## 6. Las fuentes: qué da cada una, cómo se lee y qué no da

Probado el 2026-11-26. «Nube» = la sesión de Claude en la nube; «PC» = una sesión en la computadora del dueño (Keter),
que tiene Chrome con su sesión iniciada.

| Fuente | Qué da | Qué **no** da | Cómo se lee | Quién puede |
|---|---|---|---|---|
| **YouTube Studio → Estadísticas** (modo avanzado, 28 días y «desde que se publicó») | Por video: vistas, vistas interesadas, usuarios únicos, horas, duración media, % medio visto, se quedó a mirar frente a descartado, suscriptores, me gusta, compartidos, comentarios. Curva de retención punto por punto (al pasar el cursor). Audiencia: edad, sexo, países, nuevos frente a recurrentes, dispositivos, uso de subtítulos. Tráfico por fuente y términos de búsqueda | Impresiones y CTR de Shorts; hora del público con poco volumen; muchos cortes dicen «No hay suficientes datos» en videos pequeños | A mano en el navegador; las páginas pueden no cargar: se reintenta y se dice | Solo PC |
| **Studio → Contenido y página del video** | Visibilidad, columna «Avisos», público («no creado para niños»), derechos de autor, uso de IA declarado | Por qué el feed no repartió un video | A mano | Solo PC |
| **Studio → Alcance del video** | Cómo encontraron el video (si falta la fila «Feed de Shorts», el feed no lo repartió) | Cifra de «mostrado en el feed» | A mano | Solo PC |
| **Studio → «Investigación»** | Cuadrícula de videos por tema, con filtros y multiplicador de éxito | **Ya no da** volumen de búsqueda, «búsquedas de tu público» ni «brecha de contenido» (comprobado el 2026-11-26) | A mano | Solo PC |
| **Google Trends, Explorar** | Interés relativo de hasta 5 términos (0 a 100) por país y periodo; curva por día; **consultas relacionadas** principales y en ascenso (25 + 25), con filtro «Búsqueda web» o «Búsqueda de YouTube»; 5 años para estacionalidad | Volumen absoluto. Recalcula entre lecturas: vale la última | A mano o CSV. Desde la nube devuelve error 429 | Solo PC |
| **Google Trends, RSS diario** | Lo más buscado en las últimas horas por país | Nada histórico ni por tema | `https://trends.google.com/trending/rss?geo=US` (cambiar país) | Nube y PC |
| **Autocompletado de YouTube** | Qué se escribe a partir de un inicio, en su orden, por país e idioma | Volumen. Una frase completa se devuelve a sí misma: solo cuentan las extensiones de un inicio parcial | `https://www.youtube.com/complete/search?client=youtube&ds=yt&hl=en&gl=US&q=<inicio>` | Nube y PC |
| **Autocompletado de Google** | Igual, para la búsqueda web | Volumen | `suggestqueries.google.com/complete/search?client=firefox&hl=en&gl=us&q=<inicio>` (no abre desde la nube) | Solo PC |
| **Listados de búsqueda de YouTube** | Título, canal, vistas y antigüedad de lo ya publicado; la fecha exacta de un Short en `youtube.com/shorts/<id>` | Demanda: es oferta. Ordena por relevancia; los ceros no salen | `https://www.youtube.com/results?search_query=<consulta>&hl=en&gl=US` | Nube y PC |
| **Página «Gaming» de YouTube** | Qué juegos encabezan | — | `https://www.youtube.com/gaming` | Nube y PC |
| **Videos de referencia** (YouTube, Instagram) | La forma, medida cuadro a cuadro: tiempos del golpe, cámara, mundo, efectos, color, sonido | El audio no se «escucha»: se miden picos y silencios | Se bajan en la PC con autorización del dueño, se sacan hojas de contacto a 2 f/s y cuadro a cuadro; informe y hojas van al Drive, nunca al repositorio | Solo PC |
| **Ayuda oficial de YouTube** | Políticas (violencia, edad, niños, anunciantes, monetización, desinformación), umbrales del Programa, funciones | Cómo se aplican en la práctica | `support.google.com/youtube/answer/<n>?hl=en`, citando textual | Nube y PC |
| **Fuentes de hechos** | El dato del video | — | Primaria, o dos independientes. Abren desde la nube: Wikipedia en inglés, Box Office Mojo, timeanddate. **No abren** (hay que pedir permiso de red o leerlas en la PC): `sec.gov`, sitios de empresas y de prensa, sitios académicos | Según el sitio |
| **Estudios propios** | Color por estadísticas y psicología; universo conectado; calendario de temporadas | Artículos académicos completos (bloqueados): van como resumen o Wikipedia | `estudios/` y `comercial/` | Nube |

**Reglas de lectura que salieron de los errores del 2026-11-26:**

1. **Que existan videos sobre algo no prueba que se busque.** La pregunta del video sale de las consultas relacionadas de
   Trends y del autocompletado. Dos preguntas redactadas por el equipo se cayeron así en un día.
2. **Se pide la lista completa** (las 25 + 25), no las cinco primeras.
3. **Ninguna fuente da volumen absoluto.** Se dice siempre. Lo que hay es orden, peso relativo y tendencia.
4. **Un video sin la fila «Feed de Shorts» en Alcance no sirve para juzgar nada** de su tema ni de su forma.
5. **Toda lectura lleva fecha, hora y quién la hizo**, y se guarda tal cual donde no se sube. La copia que dura es la del
   Drive privado: la carpeta de datos de una sesión en la nube se pierde al cerrarla.
6. **Lo que una sesión no puede abrir se le pide a la otra** y se anota qué no abrió; no se rellena.
7. **Se cita el número que corresponde al tema**: no se presta la cifra de un video parecido.
8. **El mismo término pesa distinto en la web y en YouTube.** Se comparan los dos; para un Short manda la búsqueda de
   YouTube (caso del 2026-11-26: «gta 7» por encima de «what is gta 6» en YouTube y muy por debajo en la web).

## 7. Qué lleva la definición del tema

Un tema está definido cuando se puede escribir, con su fuente, cada renglón:

| Renglón | Ejemplo de la forma (no del contenido) |
|---|---|
| Tema y por qué ahora | Interés relativo frente a los otros candidatos y su curva; fecha del calendario que lo empuja |
| La pregunta, como se escribe | Texto exacto, fuente (Trends o autocompletado), puesto y valor relativo |
| Las preguntas secundarias | Otras de la misma lista que el video responde de paso (cada una puede ser un golpe) |
| Lo que se descartó y por qué | Consultas más altas que no se pueden usar |
| Los hechos | 3 a 5 datos con URL y fecha; qué se afirma y qué no |
| Fecha límite para publicar | Con la regla de antelación del calendario |
| Riesgos | Marca, persona real, dato que cambia, política de la plataforma |
| Lugar en el universo | Hoja, paleta, entorno, pista que cobra y pista que siembra |

## 7b. Puntuación de nicho y subnicho (lo que el Motor le entrega al Generador)

> **Regla del dueño (2026-11-27), textual:** «Pásale ese dato al motor generador de contenido, porque para pasarte a ti los
> análisis de nicho o subnicho debe considerar el potencial de monetización con base a casos documentados; así va
> generando dentro de su método un scoring». Insumo de pago: `comercial/2026-11-27_potencial_de_pago_por_nicho.md`.
>
> **Qué es probado y qué no:** las tres puertas y las reglas de lectura salen de reglas del dueño y de errores ya
> ocurridos. Los pesos, las escalas de 0 a 3 y los cortes de 70 y 50 son **[hipótesis del equipo]**: ningún video se ha
> elegido todavía con esta puntuación. Se revisan cada 5 videos contra el resultado (se quedó a mirar y suscriptores por
> mil vistas).

**Dos niveles.** El **nicho** es el tema corto que se mide en Trends («gta 6», «iphone»); el **subnicho** es la pregunta
tal como se escribe («is gta 6 coming to pc»). El nicho aporta el potencial de pago y el encaje con el público; el
subnicho aporta la demanda de la pregunta, los hechos y las políticas. Un subnicho hereda el nivel de pago de su nicho,
salvo que tenga un puente escrito a otro nicho (una pregunta de videojuegos que se responde con piezas de PC toma el
nivel de tecnología de consumo, y se dice).

**Primero, tres puertas. No puntúan: si una no pasa, el candidato no se entrega.**

| Puerta | No pasa si… | Excepción |
|---|---|---|
| P1 · Demanda medida | No hay lectura con fecha del tema corto en Trends (búsqueda de YouTube) ni de la pregunta en autocompletado. Un listado de videos no cuenta: es oferta | Fecha conocida del calendario: entra marcada «por revalidar» y se mide la semana de publicar |
| P2 · Políticas | Algún renglón de la sección 5b queda en «no pasa» | Ninguna: se cambia el ángulo y se vuelve a puntuar |
| P3 · Hechos y lo que no se mueve | No hay fuente primaria ni dos independientes, o choca con la línea editorial o con lo fijo del canal | Ninguna |

**Después, cinco criterios, cada uno de 0 a 3.** «Sin dato» vale 0 y se escribe «sin dato»: nunca se rellena con un valor
intermedio ni con la cifra de un tema parecido.

| Criterio | 3 | 2 | 1 | 0 |
|---|---|---|---|---|
| **D · Demanda medida** | El tema corto lidera su tablero de Trends (YouTube, país principal) o está dentro del doble del líder, y la pregunta sale en las 25 consultas y en autocompletado | Tema líder, o estable a 12 meses con al menos una décima parte del líder hoy, y la pregunta sale en autocompletado | Tema por debajo de eso, solo autocompletado, o solo fecha conocida por revalidar | La pregunta marca cero o no hay lectura |
| **M · Potencial de pago documentado** | Nicho ALTO | Nicho MEDIO | Nicho BAJO | Nicho sin clasificar por el experto en monetización |
| **H · Hechos comprobables** | Fuente primaria abierta y dato que no cambia | Dos fuentes independientes | El dato cambia antes de publicar, o la fuente solo abre en la PC | (lo saca la puerta P3) |
| **P · Políticas** | Los 13 renglones en «pasa» | Una condición | Dos o más condiciones, o riesgo de marca o de persona real | (lo saca la puerta P2) |
| **E · Encaje con el público medido** | El autocompletado lo confirma en los tres países principales del canal, sirve para el tramo de 13 a 17 y el nicho ya se midió en el canal con buen «se quedó a mirar» | El autocompletado lo confirma en los tres países, pero el canal no ha medido ese nicho | Solo el país principal, o es una hipótesis sin dato del canal | Choca con el público medido |

Regla de H: si nadie ha comprobado los hechos, H vale 0 «sin comprobar» y la puntuación se da dos veces: «hoy» y «techo»
(lo que alcanzaría con los hechos comprobados). La puerta P3 queda «pendiente», no «no pasa».

Primera aplicación, con las tres correcciones a la escala que salieron de ella (corte de tamaño en D, nicho medido en E,
par «hoy» y «techo» en H): `comercial/2026-11-27_puntuacion_de_nichos_tanda_01.md`.

Reglas de M: el nivel sale de la tabla del experto, con su fila citada y su marca de solidez copiada tal cual
(«provisional», «evidencia débil»). Las estimaciones de terceros no suben un nivel. Si el nivel es provisional, se
entrega con esa palabra al lado del número.

**Los pesos cambian con el formato**, porque el pago no funciona igual: en Shorts YouTube reparte por vistas dentro de
cada país y el nicho casi no cambia el ingreso; en video largo el anuncio se vende contra el tema. Antes de entrar al
Programa de socios no se cobra nada, así que lo que acerca al umbral es la demanda.

| Criterio | Peso en Short | Peso en video largo |
|---|---|---|
| D · Demanda | 40 | 30 |
| E · Público | 20 | 15 |
| M · Pago | 15 | 30 |
| H · Hechos | 15 | 15 |
| P · Políticas | 10 | 10 |

Puntuación = suma de (peso × puntos ÷ 3); va de 0 a 100 y se calcula dos veces, una por formato. En Short, M no se lee
como ingreso del video: se lee como el tipo de suscriptor que se junta para el video largo.

| Puntuación | Veredicto |
|---|---|
| 70 o más | Se propone para ese formato |
| 50 a 69 | Reserva: entra si falta un hueco o si una lectura nueva lo sube |
| Menos de 50 | No se entrega, salvo fecha conocida, y se dice por qué |

**Desempates y cupos** (del experto en monetización, sección 4 de su estudio; el cupo es propuesta suya, sin medir):

1. Con demanda parecida (una dentro del doble de la otra en el mismo tablero), gana el nicho de mayor nivel de pago.
2. Demanda alta y pago bajo: va como Short y se escribe «demanda X; pago bajo; se elige por vistas hacia el umbral». No
   pasa a video largo sin un puente a un nicho medio o alto.
3. Demanda baja y pago alto: no ocupa un Short de crecimiento; se guarda para el video largo o se busca dentro del nicho
   la pregunta que sí tenga demanda.
4. De cada tres Shorts de la tanda, al menos uno de nivel medio o alto cuando haya uno con demanda comparable.

**Qué se le entrega al Generador de prompts.** Una tabla por tanda, con un renglón por candidato; cada celda con su
fuente y su fecha:

| Columna | Qué lleva |
|---|---|
| Nicho y subnicho | El tema corto y la pregunta exacta, con el puente si lo hay |
| Puertas | P1, P2 y P3: «pasa» o qué falta |
| D, M, H, P, E | Los puntos y, al lado, el dato que los respalda (lectura, fila del estudio de pago, URL del hecho, renglones del filtro, corte de Studio) |
| Puntuación en Short y en video largo | Los dos números |
| Veredicto | Se propone, reserva o no se entrega; y el desempate aplicado |
| Qué falta y quién lo consigue | Lecturas que esta sesión no pudo abrir (Trends «Explorar», Studio) y a quién se le piden |

El Motor no redacta el brief ni el prompt: entrega esta tabla y ahí termina. Los datos de Studio se describen en
palabras; las cifras exactas se quedan en `estadisticas/datos/`.

## 8. Qué lleva el prompt y sus fichas

El prompt de un video es una carpeta, no un texto suelto. Mínimo, y todo con su porqué:

| Pieza | Archivo del proyecto | Qué contiene |
|---|---|---|
| **Brief** | `00_brief.md` | «Estadísticas en que se basa» (cifras descritas, fecha y fuente); objetivo comercial con métrica, meta y plazo; tema y pregunta (sección 7); decisiones del equipo |
| **Estrategia** | dentro del brief y de la ficha técnica | A qué umbral acerca; qué se prueba en este video (un solo cambio grande) y contra qué se compara; qué resultado lo confirma y cuál lo descarta; lugar en la tanda |
| **Dirección** | `02_prompt/direccion.md` | Público, emoción y arco; guion por segundos con el dato fuerte antes del segundo 5; coreografía con los tiempos de golpe medidos; cámara; color (3b); sonido |
| **Ficha técnica** | `02_prompt/ficha_tecnica.md` | Objetivos por disciplina; formato y duración; elenco; entorno y paleta; efectos; requisitos del formato (A1 en adelante) marcados uno por uno; es la rúbrica con que se puntúa |
| **Perfil emocional** | `02_prompt/perfil_emocional.md` | Por cada elemento: emoción, fundamento, cómo acerca al objetivo y métrica |
| **Universo** | sección del brief | Hoja, conexión que cobra, conexión que siembra (segundo y zona de pantalla), control «se entiende solo» |
| **Prompt** | `02_prompt/prompt.md` | El texto para producir, validado con `validar_prompt.py` |
| **Publicación** | `publicacion.md`, `ficha.json` | Título con su bloque de ficha (pasa `revisar_titulo.py`), descripción con fuentes, portada, etiquetas, subtítulos |
| **Licencias y costos** | `licencias.md`, `costos.md` | Origen de cada recurso; créditos cotizados y aprobados |

**Aplicado en la plantilla del brief** (`plantillas/proyecto/00_brief.md`): tema y pregunta validada, estrategia, universo y
requisitos del formato. **Pendiente:** que `validar_prompt.py` y la plantilla de la ficha técnica exijan esas secciones;
hasta entonces el director de prompts las revisa a mano y el supervisor de continuidad las firma.

## 9. Los tres métodos que siguen al motor

| Método | Recibe | Entrega | Archivo |
|---|---|---|---|
| **Generador de prompts** | El resultado del motor (tema validado, filtro de políticas, lugar en el universo) | El paquete de prompt: brief, dirección, fichas, prompt validado, publicación, lista de piezas y pedidos | `metodo/1_generador_de_prompts.md` |
| **Equipo de producción audiovisual** | El paquete de prompt | El video revisado, la entrega, la biblioteca y los registros al día, y la medición | `metodo/2_produccion_audiovisual.md` |
| **Creador de personajes** | Un pedido de personaje, cuando el prompt necesita uno que no existe | Ficha, hoja aprobada, fila en el elenco y dibujo en el motor | `metodo/3_creador_de_personajes.md` |

Para los primeros tres segundos hay un método aparte, con su banco de ganchos medidos: `metodo/ganchos.md`.

Cada método tiene su tabla de **bifurcaciones**: qué se hace cuando falta algo, a quién se le pide, qué se le entrega,
qué devuelve y si bloquea. Regla común: lo que toca identidad, hechos o reglas del universo bloquea; lo que es
construcción viaja como pedido.

## 10. El mapa: el estudio como grafo

Idea tomada de Graphify (herramienta que convierte una carpeta en un grafo de conocimiento con un informe que se lee
primero; el dueño vio cómo funciona y le gustó como método de organización). Se adopta **el método**, sin instalar la
herramienta:

1. **Todo lo del motor es un nodo con tipo** (regla, método, personaje, paleta, entorno, efecto, estudio, video, fuente,
   conversación) y **toda relación es una arista con verbo** (usa, sale de, entrega a, bloquea, aprueba, se mide en).
2. **Hay un informe que se lee primero:** `mapa/MAPA.md`. Dice cuáles son los nodos centrales, qué depende de qué, qué
   está pendiente y qué quedó suelto. Una sesión nueva lo lee antes de buscar en archivos.
3. **El grafo se guarda en un archivo** (`mapa/grafo.json`, en formato de nodos y enlaces, el mismo que usa Graphify) y
   el informe se genera con `herramientas/mapa.py`. Se actualiza al cerrar cada video y cuando cambia una regla.
4. **Cada arista dice si es un hecho o una hipótesis**, igual que los sellos del estudio.

**Graphify instalado el 2026-11-26** (el dueño: «Sí, instala Graphify»; paquete `graphifyy` 0.9.121; queda en el guion de
inicio del entorno de la nube, sin probar todavía en una sesión nueva). Hay dos mapas y se usan juntos:

| Mapa | Cómo se hace | Qué da | Qué no da |
|---|---|---|---|
| **Estructural** (`graphify-out/GRAPH_REPORT.md`) | `graphify update video-studio`, ≈ 9 s, sin modelo externo ni costo | Todos los archivos, funciones y encabezados y cómo se enlazan (3.455 nodos y 5.713 relaciones en la primera pasada); consultas con `graphify query`, `explain`, `path`, `affected` | El significado: no sabe que un estudio respalda una regla. Respeta `.gitignore`, así que no ve estadísticas ni el universo |
| **De significado** (`mapa/MAPA.md`) | A mano en `mapa/grafo.json`, se genera con `herramientas/mapa.py` | Las relaciones que importan para decidir: quién entrega a quién, qué bloquea, qué está pendiente | No cubre todo el repositorio |

La pasada de significado de Graphify (leer los documentos con un modelo) pide una clave de API o correrlo como habilidad
dentro de una sesión; no se ha hecho. Solo se sube el informe; el grafo pesa ≈ 14 MB y se regenera.

## 11. Lo que no sé todavía


- Si las conexiones entre videos convierten en regresos y suscriptores: no hay ningún video conectado publicado.
- Cuánto del método sirve para una marca comercial con productos reales (logotipos, precios, promesas de venta): el caso
  de Tin & Tan no tiene nada de eso.
- Si los pesos y los cortes de la puntuación (sección 7b) eligen mejor que la regla anterior: ningún video se ha elegido
  con ella.
- Cuánto baja la puntuación de pago un público de 13 a 17 y cuánto vale el fondo de Shorts por país: el estudio de pago
  lo deja «sin dato».
- Cómo se une esto con lo que el dueño llama «Motor generador de contenido» en su otra conversación.
