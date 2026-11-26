# Reglas del estudio para el Cerebro

> Pedido del dueño (2026-11-21), textual: *«Todas esas reglas deben quedar en el cerebro»*.
> Es la lista consolidada de reglas y decisiones del dueño sobre producción de video. Se le envía a la conversación
> de Keter para que la cargue en el Cerebro. Cada vez que se agrega una regla, se actualiza este archivo y se reenvía.
> Fuente de cada regla entre paréntesis. En el Cerebro está en el nodo `reglas-del-estudio-de-video` (guardado por Keter el
> 2026-11-21); si cambia esta lista, se le manda el cambio a Keter.

## Organización

1. **El equipo de producción audiovisual trabaja según los prompts generados** por la conversación «Generador de
   prompts y carpetas para videos» (2026-11-20).
2. **Las dos conversaciones se comunican constantemente**: al empezar cada video, al recibir un prompt, después de
   cada generación y revisión, y cada vez que cambia una regla (2026-11-21). Detalle: `video-studio/COORDINACION.md`.
3. **Todo queda como plantilla**: si cambia el proceso se actualiza el manual; si avanza un proyecto, su caso. Nada
   queda solo en la conversación (2026-11-21, `video-studio/MANUAL.md`).
4. **Todo lo que se cree de los personajes se guarda ordenado** en Google Drive, `Personajes/`, con `01 Diseño
   aprobado`, `02 Hojas de personaje`, `03 Pruebas descartadas` y la bitácora (2026-11-20).

## Créditos y generación

5. **Un intento por pieza**: cada imagen, clip o audio se genera una sola vez; si sale mal, se informa qué falló y
   cuánto cuesta rehacerlo, y solo el dueño autoriza otra generación (2026-11-20, `generacion.md`).
6. **No se genera sin definición cerrada** y sin autorización del dueño con el costo a la vista (2026-11-20).
7. **Cotizar siempre antes de generar** y decir el número (2026-11-07).
8. **Todo cambio que pide el dueño pasa primero por el equipo** (`video-studio/cambios/`) (2026-11-20).
9. **Lo editable no se genera**: texto, zooms, transiciones, cámara lenta y color se hacen gratis en edición.
10. Los clips se generan **sin audio**; la música la pone el dueño salvo que pida generarla (2026-11-07).

## Contenido

11. **El objetivo comercial lo fija el dueño en cada video** (monetizar, presencia, recordación, comunidad, conversión,
    viralidad u otra estrategia que nos ponga en la mente del público objetivo) (2026-11-20).
12. **El director es creativo y comercial**: diseña para una emoción y para un objetivo medible, y decide con las
    estadísticas de las cuentas (2026-11-20).
13. **Personajes originales**: no se recrean personajes ajenos ni personas reales (salvo el dueño, con sus fotos).
14. **No se calca metraje ajeno**: de un trend se copia la fórmula; si importa el movimiento, el dueño graba su versión
    y se transfiere (2026-11-07).
15. **Públicos separados**: el contenido infantil (Tiky y Lumi) nunca se cruza con contenido para adultos (Spike,
    «M», Tin y Tan).
16. **Línea editorial**: nada de identidad ni ideología de género en el contenido, en ningún idioma ni formato. Tiky
    es él y Lumi es ella (2026-11-20).
17. En el contenido infantil no se declara que está hecho con IA (2026-11-08); en el realista sí se etiqueta.
18. Nada se publica sin la aprobación del dueño.

## Personajes y canales

19. **Tiky y Lumi**: serie infantil `granja` (1–3 años), 3D de juguete de vinilo.
20. **Tin & Tan**: personajes nuevos de los videos de palitos del canal de nostalgia; Tan recuerda y pregunta, Tin
    hace la cuenta. Dibujados con código (`herramientas/palitos.py`). Aprobados el 2026-11-21 («si me gustan»).
21. **Tin & Tan tienen su propio canal nuevo, «Tin & Tan»** (lo crea el dueño). El canal «Tiky & Lumi» (@TikyAndLumi)
    **no se renombra**: queda para la serie infantil de Tiky y Lumi (2026-11-21).
22. Formato del canal de nostalgia: pregunta nostálgica con respuesta calculada de verdad; nada de clonar «Doodle
    Digest» (regla de contenido no auténtico de YouTube).

## Retención y revisión (de dos videos de Instagram, 2026-11-20; hipótesis a medir)

23. Movimiento y una afirmación de contraste o cifra en el segundo 0–1; dos ganchos para probar; cierre que empalma
    con el inicio; toda cifra con fuente; un solo llamado a la acción.
24. Nada genérico de IA; 1 o 2 motivos visuales que vuelven; subtítulos de 1 a 3 palabras con la palabra clave en
    color de acento.
25. Mapa de ritmo con picos y respiros; acelerar al final; cada corte con su golpe de sonido.
26. Revisión de cada render a 2 fotogramas por segundo, marcando fotogramas muertos; máximo 3 destellos por segundo.
27. Herramientas por instalar (HyperFrames, Remotion, Earshot, transcripción): solo con el sí del dueño.

## Publicación (2026-11-21)

28. **Todo se sube a YouTube en privado.** Para hacerlo público o programarlo, el publicador le presenta al dueño qué se
    publica, sus objetivos y el plan, y espera su sí a ese video (más adelante el dueño puede autorizar que sea solo).
29. **Entrega al publicador:** Drive «Canal YouTube - Entregas» / una subcarpeta por código de trazabilidad, con video,
    miniatura de menos de 2 MB (1280×720 si el video es horizontal; **1080×1920 si es un Short**), texto puesto en
    edición, subtítulos opcionales y `ficha.json`. Un código no se sube dos veces. Detalle:
    `video-studio/ENTREGA_YOUTUBE.md`.
    **Portada de cada Short** (dueño, 2026-11-21, traída por el Canal automatizado; cambia esta regla):
    1. Los primeros 0,5 a 1 s del video **son la portada**, y el video sigue desde ahí sin corte brusco; ese cuadro es
       el que se elige como miniatura (un canal fuera del Programa de Socios no puede subir imagen propia para un Short,
       y en el feed de Shorts no se ve miniatura: el video arranca solo).
    2. Además va `miniatura.png` **vertical de 1080×1920** (por si el canal entra al Programa o la API lo permite). Una
       horizontal se recorta y se pierden los personajes y el texto (pasó en TIN-EN-S-001). `entrega.py` la exige.
    3. **Zona útil x 60–960, y 380–1440**: fuera de ahí la tapan el título y los botones; solo fondo o cuerpos, nunca
       texto ni caras. (Zonas tomadas de vidIQ, no de YouTube: ajustarlas con una captura real del estante.)
    4. **Texto**: máximo 4 palabras en 2 líneas, entre y 400 y 700, letra de unos 120 px o más, **mayúscula inicial en
       cada palabra** y la palabra clave en el amarillo del canal. Sin la respuesta ni el número; no copia el título
       palabra por palabra.
    5. El objeto nostálgico en el centro (y 720–1100) y las caras de Tin y Tan dentro de la zona útil, con curiosidad o
       sorpresa y mirando el objeto.
    6. El video cumple lo que promete la portada (si no, YouTube lo trata como clickbait).
30. **Contenido no auténtico:** dos videos seguidos no repiten estructura, música ni estilo de miniatura; el video
    cumple lo que promete el título; nada de material ajeno sin licencia.

## Agregado por el Generador de prompts (2026-11-21)

- **Quién decide qué:** el equipo decide todo lo técnico y de producción y lo informa con su razón; al dueño se le llevan ideas, ajustes a las ideas y criterio psicológico. Gastar créditos, instalar, rehacer y publicar siguen necesitando su sí.
- **Consumo:** cada video anota créditos y uso de Claude en `video-studio/consumo.md`.
- **Voz del canal Tin & Tan:** Kevin (Tin) y Zelda (Tan), aceleradas un 10 % en edición.
- **Lados:** izquierda y derecha se escriben respecto al cuadro, no respecto al personaje.
- **Nombres propios con mayúscula, siempre (dueño, 2026-11-21):** «Tin & Tan» / «Tin y Tan», «Tiky», «Lumi»,
  «Spike» y los nombres de canal van con mayúscula inicial en todo texto (banner, perfil, miniaturas, títulos en
  pantalla, subtítulos, hojas, fichas, descripciones), aunque el estilo del canal pida minúsculas. El supervisor de
  continuidad lo revisa letra por letra; un nombre en minúscula no pasa.
- **Controles de calidad bloqueantes (dueño, 2026-11-21):** «estamos produciendo en alta calidad, no amateur».
  Texto, cifras, voz, imagen, video, entrega y marca tienen cada uno un control con responsable que lo firma
  (`video-studio/manual/12_controles_de_calidad.md`); lo que no pasa no sale. El texto pasa por
  `revisar_texto.py` con 0 errores más una lectura a mano; el supervisor de continuidad firma.
- **Cifras aproximadas con «≈» (dueño, 2026-11-21):** todo número con decimales o fracción (décimas, centésimas,
  milésimas, millonésimas) se aproxima y se escribe con «≈» («≈ 422 ft»); en la voz, «about», «unos», «cerca de».
  Solo una cita textual de una fuente se copia tal cual. Desde el video siguiente a TIN-EN-S-001.
- **Color con intención (dueño, 2026-11-21):** cada video lleva en su dirección (sección 3b) y en `ficha.json`
  (`color`) por qué se eligió cada color y cómo ayuda al objetivo. La paleta lleva 2 neutros y 1 acento, y el acento
  va solo en el título y en un elemento (reel de andrea.eskailet). La decide el director de fotografía, la valida el
  director creativo y el supervisor la mide con `revisar_color.py`. Texto ≥ 4,5:1, ≥ 7:1 para 45+. Manual: cap. 13.
- **Dónde se presenta cada cosa (2026-11-21):** en el Generador de prompts solo se ven prompts y fichas; todo lo terminado (videos, audios, imágenes) se le presenta al dueño en Equipo de producción audiovisual.

- **Títulos con estudio y filtro (dueño, 2026-11-21):** textual: «necesito que alguien del equipo estudie cuáles son
  los títulos que más penetran el algoritmo y el SEO para tener parámetros y referencias con base al público objetivo
  y eso volverlo instrucción y filtro; esto también debe quedar en la ficha». Estudio: `comercial/titulos.md` (del
  comercial). Filtro: `herramientas/revisar_titulo.py`, 0 errores. Ficha: bloque «Título (ficha)» en la publicación
  y objeto `titulo_ficha` en `ficha.json`.

- **Perfil emocional en la ficha (dueño, 2026-11-23):** textual: «Necesito que en la ficha del video o del contenido
  incorpores, bajo perfil de colores, animaciones, efectos de luz, velocidad del video, velocidad del audio, contenido
  del video y alguna otra cosa que consideres pertinente, qué emociones buscas provocar tanto con el contenido como
  con los elementos del contenido generado y cómo estas emociones nos van a acercar a los objetivos». Plantilla:
  `plantillas/proyecto/02_prompt/perfil_emocional.md` (15 elementos, cada uno con emoción, fundamento, objetivo,
  métrica y riesgo). Va también en `ficha.json`, campo `emociones`. `validar_prompt.py` no deja pasar uno sin llenar.
- **Oído del estudio (dueño, 2026-11-23):** «busca para que puedas auditar el tema de voz y audio».
  `herramientas/revisar_voz.py` transcribe y compara con el guion (Whisper sin conexión, `instalar_oido.sh`).

- **Objetivo inicial (dueño, 2026-11-23):** «Entonces el objetivo inicial es entrar al programa de socios; todo debe girar en torno a lograr el objetivo a la mayor brevedad posible». Vale para el canal Tin & Tan; todo
  brief, ficha técnica y perfil emocional lo lleva como objetivo comercial y mide contra los umbrales del Programa.

- **El objetivo de entrar al Programa de socios rige para todos los canales (dueño, 2026-11-23):** «Rige para todos
  los canales que trabajemos». Incluye Tin & Tan y Tiky & Lumi. En el canal infantil se persigue dentro de los
  límites de `infantil/guia_1_a_3.md` (sin ganchos, sin pedir suscripción al niño) y del veto de la psicóloga.

- **Los efectos se eligen por investigación, no por gusto (dueño, 2026-11-23):** «No es lo que a mí me guste; cada
  efecto animado comunica y al mismo tiempo provoca una emoción, por eso debe ser basado en tu investigación».
  Gramática de efectos: `manual/14_efectos_y_emocion.md`. No se le pregunta al dueño qué efecto prefiere.

- **Canal automatizado: el equipo filtra y decide (dueño, 2026-11-24):** «Filtra todo vos con base a tu investigación;
  ya te dije que estamos afinando un canal automatizado». Dado un tema, el equipo decide ángulo, tono, límites,
  título y efectos con su investigación y lo deja escrito; al dueño solo se le pide el sí para créditos, instalar,
  rehacer y publicar.

- **Parámetros flexibles (dueño, 2026-11-24):** «Cambia esas limitantes y define nuevos parámetros; podría ser que los
  parámetros sean flexibles; con este cambio considera cambios en todo lo demás si es necesario, incluso en banner e
  imagen de perfil». Tin & Tan deja de ser «canal de nostalgia»: hacen la cuenta de lo que la gente está mirando.
  `canales/nostalgia-tin-y-tan/PARAMETROS.md` separa lo fijo de lo flexible (cada parámetro con métrica y rango).

- **La nostalgia se elimina como criterio (dueño, 2026-11-24):** «Esto es lo que manda para mí porque lo sacaste de una
  investigación… me seguís colocando nostalgia aun cuando me dijiste que es una limitante; no es lógico. Haz los
  cambios con respecto a la investigación». Las seis limitantes halladas (nostalgia, cuenta obligatoria, público de
  45 a 70, evitar toda palabra de la polémica, filtro de títulos por opinión, no repetir forma) quedan sin efecto.

- **Firma del lápiz bumerán (dueño, 2026-11-24):** «quiero un efecto para todos los videos en el que el lápiz sirva
  como un bumerán: cuando comienza el video el bumerán está regresando a sus manos y cuando está terminando el video
  Tan tira el lápiz; definilo bien con el equipo». Especificación: `canales/nostalgia-tin-y-tan/FIRMA_LAPIZ_BUMERAN.md`.
- **Subtítulos en español en el video (dueño, 2026-11-24):** «te pido colocar subtítulos en español… en el video».
  Voz en inglés y traducción al español quemada en pantalla, en todos los videos de Tin & Tan.
- **Marca nueva autorizada (dueño, 2026-11-24):** «Sí, carga lo nuevo con Keter»: banner y descripción v2.

- **Portada de los Shorts nombra al sujeto (dueño, 2026-11-24):** «back in 11 days no hace referencia a nada… deja algo
  que nombre jensen y nvidia». El texto de la portada dice de quién o de qué trata el video (persona, marca u objeto),
  con las palabras que la gente busca; la cifra o la pregunta sola no basta.

- **Ningún prompt sin estadísticas (dueño, 2026-11-26):** «No quiero que vuelvas a generar un prompt sin haberte basado
  en estadísticas». El brief abre con «Estadísticas en que se basa» (Studio del canal, con edad y país, más la demanda
  medida), con cifras, fecha y fuente. Sin dato no hay prompt: se pide. No vale seguir la línea del video anterior.

- **Formato de acción de Tin & Tan y parámetros versionados (dueño, 2026-11-26):** «la animación de pelea debe ser casi
  idéntica [a] los videos; es un formato de acción donde hay aceleración, desaceleración […] personajes 2D con interacción
  3D con su mundo […] fuego, humo, choques, sonidos de golpes, explosiones, implosiones, daños en el mundo 3D […] necesito
  que las alternativas sean rigurosas con lo que te estoy pidiendo». Y: «Mejor versiona los parámetros porque hay cosas que
  ya te había pedido que no están implementadas». `PARAMETROS.md` lleva número de versión, copia de cada versión anterior
  y una lista de pedidos con su estado; una alternativa que no cumple un requisito no se presenta como válida. Tin y Tan
  pelean juntos contra un tercer personaje sin nombre en pantalla (concepto: la duda), con cuerpo, manos y pies.

- **Ninguna prueba a medias (dueño, 2026-11-26):** «No quiero que las pruebas me las vaya[s] a sacar sin todos los cambios
  solicitados, incluidos los colores». Una prueba o una pieza solo se presenta o se genera cuando lleva todos los pedidos
  vigentes del canal (`PARAMETROS.md`, secciones 7 y 8). Si falta uno, se dice cuál y de quién depende.
- **Colores (dueño, 2026-11-26):** «Replantear los colores con base a estadísticas y análisis psicológico».

- **Entorno por tema y motor de elementos (dueño, 2026-11-26):** «El entorno idealmente se debe generar con base al
  prompt, es decir, el contexto y temática […] como un motor […] donde en la medida que vayamos generando videos todos los
  elementos los vayas almacenando, por si caben o se quieren reutilizar en algún otro video; pero el entorno debe cambiar
  dependiendo del contexto y temática del video». Biblioteca: `video-studio/motor_de_accion/` con `catalogo.json`.
- **Paletas (dueño, 2026-11-26):** «me gustan los A, B y C» (estudio de color del 2026-11-26). Se eligen por tema.

- **Universo conectado de Tin & Tan (dueño, 2026-11-26):** «necesito que los videos vayan conectados de alguna manera; por
  ejemplo, que aparezca algo que no tenga nada que ver con el video y en realidad es un adelanto del siguiente video, que
  alguna animación se conecte con la del siguiente video, algo que permita después lanzar videos conspirativos del mismo
  canal […] hay que generar un universo más pensado y universos alternos para Tin y Tan […] contrástalo con estadísticas;
  bajo esta lógica debe haber por lo menos una producción de 15 días a un mes para que podamos conectar todo». El canal es
  informativo con el atractivo de las peleas y admite casi cualquier temática. Solicitud:
  `video-studio/cambios/2026-11-26_universo_conectado_de_tin_y_tan.md`.

- **Temporadas por país, con históricos (dueño, 2026-11-26):** «Incluye a las consideraciones para contrastar con las
  estadísticas las temporadas; por ejemplo, estamos a 5 días de comenzar diciembre, y así sucesivamente cada temporada
  según los países que más estén viendo los videos; temporadas o feriados; revisa históricos para poder contrastar». El
  calendario del radar se hace con los países que muestra Studio, no con los supuestos.
- **Una pregunta solo vale si aparece en datos de búsqueda (lección del 2026-11-26):** el dueño preguntó si la pregunta
  del short 4 estaba validada; no lo estaba. Que existan videos sobre algo es oferta, no demanda. Antes de fijar la
  pregunta de un video se comprueba en autocompletado y en las consultas relacionadas de Google Trends.

- **Las limitantes se resuelven con creatividad; el motor se ajusta (dueño, 2026-11-26):** «todas las limitantes que se
  presenten se resuelvan con creatividad; por ejemplo, si se quedó un video no publicado, se trata de hacer un remake o se
  rompe la línea de tiempo […] el equipo [debe tener] la habilidad de generar e irse ajustando dependiendo del contexto
  dado por las estadísticas, circunstancias […] y limitantes dadas por el tema o la plataforma […] es parte de la
  naturaleza del motor: al trabajar con estadísticas debe saber ajustarse». Y aprobó («Sí a las 5»): el mundo de Tin & Tan
  es un cuaderno con tres hojas (una por paleta); el rival es una pregunta que se responde y nunca muere ni da miedo; las
  respuestas del misterio no van al repositorio público; de las teorías conspirativas como tema quedan fuera salud,
  elecciones, tragedias y las que señalan a grupos; la primera tanda dura cuatro semanas y empieza con el short 4.
