# Hojadevida

El sitio de la hoja de vida vive en `Evaluacion Fundamentos html/`.
`video-studio/` es un estudio de prompts para generación de video; su guía es `video-studio/README.md`.

## Equipo de producción de audio y video

- El flujo completo se coordina con `/producir` (`.claude/skills/producir/SKILL.md`). La conversación principal habla
  con el dueño, cotiza y genera; los agentes hacen cada oficio y escriben en `02_prompt/direccion.md`.
- Equipo: `director-creativo` (creativo y comercial), `jefe-de-produccion`, `director-de-fotografia`,
  `director-de-animacion`, `director-de-prompts`, `disenador-de-sonido`, `editor-de-video`,
  `supervisor-de-continuidad`, `analista-de-video`. Su formación está en `video-studio/manual/`.
- El **objetivo comercial** (monetizar, presencia, recordación, comunidad, conversión, viralidad…) lo fija el dueño
  en el brief de cada proyecto. Si falta, se pregunta.
- **Objetivo inicial fijado por el dueño (2026-11-23), para todos los canales que se trabajen: entrar al Programa
  de socios de YouTube lo antes posible.** «Rige para todos los canales que trabajemos».
  Textual: «Entonces el objetivo inicial es entrar al programa de socios; todo debe girar en torno a lograr el objetivo a la mayor brevedad posible». Cada decisión de tema, formato, título, gancho,
  ritmo y cadencia se justifica por cuánto acerca a los umbrales (suscriptores y vistas de Shorts u horas de video
  largo). Plan y cuentas de Tin & Tan: `video-studio/canales/nostalgia-tin-y-tan/plan_programa_de_socios.md`; de Tiky y
  Lumi: `video-studio/series/granja/estrategia_monetizacion.md`. En el canal infantil el objetivo nunca pasa por
  encima de `infantil/guia_1_a_3.md` ni del veto de la psicóloga.
- **Parámetros flexibles (regla del dueño, 2026-11-24):** «Cambia esas limitantes y define nuevos parámetros; podría
  ser que los parámetros sean flexibles». Cada canal tiene su `PARAMETROS.md`: lo poco que no se mueve (identidad,
  veracidad, seguridad, línea editorial, el sí del dueño) y lo demás como hipótesis con métrica, rango y revisión
  cada 5 videos. Tin & Tan: `video-studio/canales/nostalgia-tin-y-tan/PARAMETROS.md`; **la nostalgia quedó eliminada como
  criterio** (corrección del dueño: «me seguís colocando nostalgia aun cuando me dijiste que es una limitante»): Tin y
  Tan explican con hechos lo que la gente ya está mirando; el tema lo pone la demanda y la cuenta es opcional. Ese archivo manda sobre el diseño, los títulos y el radar.
- **Tin & Tan, en todos los videos (reglas del dueño, 2026-11-24):** la firma del **lápiz bumerán** («cuando comienza el
  video el bumerán está regresando a sus manos y cuando está terminando el video Tan tira el lápiz»; especificación en
  `video-studio/canales/nostalgia-tin-y-tan/FIRMA_LAPIZ_BUMERAN.md`) y **subtítulos en español dentro del video**
  (voz en inglés, traducción quemada en pantalla).
- **Nunca se suben subtítulos a YouTube (regla del dueño, 2026-11-26):** «esos no quiero que los pongas nunca porque el
  video ya lleva subtítulos». Fue un error de publicación en TIN-EN-S-003. Las pistas `.srt` no van en la entrega ni se
  cargan en Studio; quedan solo como archivo de trabajo en `02_prompt/`. Lo único que cuenta es que el subtítulo grabado
  en la imagen esté bien: se revisa en el control 1 sobre el video terminado.
- Solo actúan los personajes de `video-studio/personajes/REGISTRO.md` (Tiky, Lumi, Spike, Tin, Tan). Tin & Tan son
  los muñecos de palitos del canal Tin & Tan y se dibujan con `video-studio/herramientas/palitos.py`. Sus carpetas terminadas
  están en Google Drive, `Personajes/`.
- Antes de generar: cotizar con `estimate_video_cost` / `estimate_image_cost` / `estimate_audio_cost`, decir el número
  y esperar aprobación. Lo editable se hace gratis con `video-studio/herramientas/postpro.py`.
- **Radar de tendencias (regla del dueño, 2026-11-21):** el `comercial-inteligencia-digital` mantiene
  `video-studio/comercial/radar_de_tendencias.md` (temporadas, lanzamientos, aniversarios y tendencias en curso, con
  fuente, fecha y fecha límite para producir) y lo actualiza cada semana. Antes de proponer el siguiente video se mira el radar.
- Las estadísticas de las cuentas van en `video-studio/estadisticas/datos/` y no se suben (el repo es público).
- **Coordinación (regla del dueño, 2026-11-21):** el equipo trabaja según los prompts del «Generador de prompts y
  carpetas para videos» y se comunica con esa conversación constantemente; toda regla nueva va a
  `video-studio/REGLAS_CEREBRO.md` para el Cerebro. Detalle: `video-studio/COORDINACION.md`.

## Todo queda como plantilla (regla del dueño, 2026-11-21)

- El procedimiento completo para montar un personaje está en `video-studio/MANUAL.md`; el caso real, en
  `video-studio/casos/`. Un personaje nuevo se monta siguiendo ese manual, fase por fase.
- Cada decisión, paso, costo y error se documenta: si cambia el proceso, se actualiza el manual; si
  avanza un proyecto, se actualiza su caso. Nada se deja solo en la conversación.
- `python3 video-studio/herramientas/estado.py` dice en qué fase está cada personaje, serie y proyecto.
- El consumo de cada video se anota en `video-studio/consumo.md` al terminar cada fase: créditos de Higgsfield y
  tokens de cada agente. Sirve para estimar el costo del siguiente video.

## Quién decide qué (regla del dueño, 2026-11-21)

Textual: «Esto no lo puedo decidir yo, por eso te he estado dando elementos para que te capacites técnicamente; ya
cuando entremos en calor, en lo que voy a acompañar al equipo creativo es con ideas y ajustes a ideas o los
elementos psicológicos».

- **Decide el equipo, sin preguntarle al dueño:** todo lo técnico y de producción: gancho, ritmo, formato de cada
  pieza, objetivo de medición, público estimado, herramienta, orden de trabajo, quién produce. Cada decisión se
  anota con su porqué en el brief del proyecto («Decisiones del equipo») y se le informa después.
- **Se le lleva al dueño:** ideas y temas, ajustes a las ideas, lo psicológico y emocional del contenido, la línea
  editorial, y lo que solo él puede hacer (crear cuentas y canales, exportar estadísticas, publicar).
- **Sigue necesitando su sí:** gastar créditos o dinero, instalar herramientas, rehacer una pieza ya generada y
  publicar. Eso no cambia.
- Al informar se le presenta la decisión tomada y su razón, no una lista de opciones.
- **Canal automatizado (regla del dueño, 2026-11-24):** «Filtra todo vos con base a tu investigación; ya te dije que
  estamos afinando un canal automatizado». Cuando el dueño da un tema, el equipo investiga, filtra y decide solo el
  ángulo, el tono, lo que se dice y lo que no, el título y los efectos, lo deja escrito con su porqué y sigue hasta
  tener la pieza lista. No se le devuelven listas de decisiones ni preguntas de gusto o de tono. Solo se le detiene
  para lo que sigue necesitando su sí (créditos o dinero, instalar, rehacer una pieza, publicar) y para lo que solo él
  puede hacer.

- **Ningún prompt sin estadísticas (regla del dueño, 2026-11-26):** «No quiero que vuelvas a generar un prompt sin
  haberte basado en estadísticas; en este caso solo seguiste la línea del video anterior». Antes de escribir un prompt
  se leen las estadísticas del canal (Studio: vistas, se quedó a mirar, retención, suscriptores, tráfico, **edad** y
  país; las pasa el dueño o Keter y van en `video-studio/estadisticas/datos/`) y la demanda medida de la investigación;
  el brief abre con una sección «Estadísticas en que se basa» con cifras, fecha y fuente. Si no hay dato, se pide; no
  se sigue «la línea del video anterior» ni la promesa de un cierre. «Hay que irnos ajustando a las estadísticas
  resultantes y a tu investigación»: público, tema y forma se corrigen con lo que arrojen (por ejemplo, la edad real).
  Esto rige hasta que exista el motor generador de contenido, que el dueño explicará.

- **Ninguna prueba a medias (regla del dueño, 2026-11-26):** «No quiero que las pruebas me las vaya[s] a sacar sin todos los
  cambios solicitados, incluidos los colores». Antes de presentar una prueba o de generar una pieza se repasa la lista de
  pedidos del canal (`PARAMETROS.md`, secciones 7 y 8) y la prueba los lleva **todos**; si falta uno, no se presenta ni
  se genera: se dice qué falta y de quién depende.

- **Las limitantes se resuelven con creatividad; el motor se ajusta (regla del dueño, 2026-11-26):** «todas las limitantes
  que se presenten se resuelvan con creatividad; por ejemplo, si se quedó un video no publicado, se trata de hacer un
  remake o se rompe la línea de tiempo. Necesito que el equipo tenga la habilidad de generar e irse ajustando dependiendo
  del contexto dado por las estadísticas […] y limitantes dadas por el tema o la plataforma, incluso las circunstancias
  […] es parte de la naturaleza del motor: al trabajar con estadísticas debe saber ajustarse». Ante una limitante (de
  las estadísticas, del tema, de la plataforma o de las circunstancias) el equipo no responde «no se puede»: propone cómo
  se convierte en parte del universo o del plan, lo anota con el dato que lo motivó y sigue. No toca lo que no se mueve
  (fuentes, seguridad, línea editorial, el sí del dueño). Para Tin & Tan: `PARAMETROS.md`, sección 9.

- **Motor de contenido replicable (regla del dueño, 2026-11-26):** lo que se define con Tin & Tan (conceptualización,
  universo, formatos corto y largo, biblioteca de elementos, conexiones, adaptación) «se vuelve parte de cómo definimos
  conceptualización, universo de los personajes y contexto para el motor» y debe poder replicarse «con otros personajes o
  marcas comerciales». Método: `video-studio/MOTOR_DE_CONTENIDO.md`. Con cada personaje o marca nuevos se llena primero
  `video-studio/plantillas/arranque_de_universo.md`. Los secretos de un universo no van al repositorio público.
  El mismo archivo fija la cadena de trabajo de cada video (dueño: «Todo lo que investigaste este día en las diferentes
  plataformas debe quedar en el método del motor para poder definir el tema y con ello el prompt […] y fichas técnicas,
  incluida la estrategia […] considerando el universo definido»): estadísticas → calendario → interés por tema →
  preguntas reales → hechos → lugar en el universo → brief → fichas → prompt → prueba completa → medición (secciones 5 a 8).

- **Tres métodos después del motor y mapa del estudio (regla del dueño, 2026-11-26):** el resultado del motor pasa por
  `video-studio/metodo/1_generador_de_prompts.md` (paquete de prompt con sus fichas, estrategia y lugar en el universo),
  `video-studio/metodo/2_produccion_audiovisual.md` (del paquete al video publicado y medido) y, cuando el prompt pide un
  personaje que no existe, `video-studio/metodo/3_creador_de_personajes.md` (pedido en
  `plantillas/pedido_de_personaje.md`). Cada método trae su tabla de bifurcaciones: qué se hace cuando falta algo, a quién
  se le pide y si bloquea. El tema y el guion pasan el filtro de políticas de YouTube (motor, sección 5b). Antes de buscar
  en archivos se lee `video-studio/mapa/MAPA.md` (el estudio como grafo; se regenera con `herramientas/mapa.py` al cerrar
  cada video y cuando cambia una regla).

- **Cada conversación, su oficio (regla del dueño, 2026-11-26):** «Bajo mi lógica vos solo generás el prompt y se lo
  pasás a producción audiovisual; producción debe tener los métodos para generar el video, así que por tu parte solo te
  quedás de ahora en adelante con generar el prompt, no tenés que generar el video; y mi lógica me dice que el video va
  primero y después va el audio: que eso lo defina el equipo audiovisual». El **Generador de prompts** entrega el
  paquete de prompt (método 1) y ahí termina: no construye, no renderiza, no genera voz ni video, no presenta piezas.
  El **Equipo de producción audiovisual** produce con el método 2, que es suyo: decide el orden (el dueño propone
  imagen primero y audio después) y lo deja escrito en `video-studio/metodo/2_produccion_audiovisual.md`.

- **El método no se salta: puerta de presentación (regla del dueño, 2026-11-26):** «La idea de definir un método es que
  no te lo saltes, que no vuelva a pasar». Ninguna pieza terminada se le presenta al dueño, ni se le dice «listo para
  revisar», sin que `python3 video-studio/herramientas/puerta_de_presentacion.py <proyecto> <pieza>` diga PASA: animación,
  fotografía, sonido, edición y continuidad firman en `07_revision/firmas.md` sobre el sha256 de esa pieza (método 2,
  paso A9b). Si no pasa, se dice qué falta y de quién depende; no se presenta «con reservas».

- **Reporte de publicación y calendario con avisos (regla del dueño, 2026-11-26):** «Cada vez que se publique un video
  necesito ver el detalle, a manera de reporte, de lo que se consideró para subir ese video, incluidos los objetivos y las
  generales de cómo se conecta al siguiente video. El calendario que generemos […] necesito verlo en Calendar y necesito
  recibir alertas para que no se nos vaya a pasar por alto que hay que publicar». Cada video lleva su reporte
  (`video-studio/plantillas/reporte_de_publicacion.md`) antes de pedir el sí para publicar. El calendario de publicación
  del canal (`video-studio/canales/nostalgia-tin-y-tan/calendario_de_publicacion_2026-12.md`) se copia al Google Calendar
  del dueño con aviso un día antes y dos horas antes; si cambia una fecha, se cambia en los dos lados.

## Qué se ve en cada conversación (regla del dueño, 2026-11-21)

Textual: «siempre lo terminado preséntamelo en equipo de producción audiovisual; aquí quiero que veamos
exclusivamente los prompts y fichas».

- **Generador de prompts y carpetas:** solo prompts y fichas (de personaje, pedagógica, técnica, de publicación) y
  sus definiciones. Aquí no se presentan videos, audios ni imágenes terminados.
- **Equipo de producción audiovisual:** todo lo terminado se presenta allí: videos, audios, imágenes, revisiones.
- Lo que el Generador produzca o reciba ya terminado se deja en el repositorio, se anota en
  `video-studio/COORDINACION.md` con su ruta y se le avisa al equipo; al dueño, aquí, solo se le dice que ya está
  y dónde verlo.

## Controles de calidad (regla del dueño, 2026-11-21)

- «Estamos produciendo en alta calidad, no amateur»: texto, cifras, voz, imagen, video, entrega y marca pasan
  controles bloqueantes con responsable que firma (`video-studio/manual/12_controles_de_calidad.md`). Un error
  ortográfico o un nombre en minúscula no sale. El texto pasa por `video-studio/herramientas/revisar_texto.py`.
- Nombres propios siempre con mayúscula («Tin & Tan»). Cifras con decimales o fracciones: aproximadas y con «≈».
- Títulos (regla del dueño, 2026-11-21): se escriben con la instrucción de `video-studio/comercial/titulos.md`
  (estudio por público, con fuentes) y pasan `video-studio/herramientas/revisar_titulo.py` con 0 errores; el bloque
  «Título (ficha)» va en la ficha de publicación y en `ficha.json`. El comercial mantiene el estudio.
- Ficha técnica de cada video (`02_prompt/ficha_tecnica.md`): abre con los **objetivos comerciales** que fijó el dueño
  (con su métrica, meta y plazo); si el dueño no los ha fijado, se le pregunta y no se pone uno por defecto.
- Perfil emocional (regla del dueño, 2026-11-23): la ficha de cada video lleva `02_prompt/perfil_emocional.md`: por
  cada elemento (contenido, colores, animaciones, efectos de luz, velocidad del video y del audio, voces, música,
  efectos, texto, cierre, título) qué emoción se busca, con qué fundamento, cómo acerca al objetivo y con qué métrica
  se verá. Lo escribe el director creativo (en infantil decide la psicóloga); `validar_prompt.py` lo exige lleno.
- Efectos y animación (regla del dueño, 2026-11-23): «cada efecto animado comunica y al mismo tiempo provoca una
  emoción, por eso debe ser basado en tu investigación». Ningún efecto se elige por gusto ni se le pregunta al dueño
  cuál prefiere: se elige con `video-studio/manual/14_efectos_y_emocion.md` (qué comunica, qué emoción provoca, con
  fuente) y se justifica en el perfil emocional del video.
- Color con intención: 2 neutros + 1 acento; por qué cada color y cómo ayuda al objetivo va en la dirección
  (sección 3b) y en `ficha.json`; se mide con `video-studio/herramientas/revisar_color.py` (`manual/13`).

## Línea editorial

- Decisión del dueño (2026-11-20), para todo lo que se produzca aquí: nada de identidad de género ni
  ideología de género en el contenido, en ningún idioma ni formato. Tiky es él y Lumi es ella.

## Créditos y cambios (regla del dueño, 2026-11-20)

- **Nada de segundos intentos.** Cada imagen, clip o audio se genera una sola vez. Si sale mal, se informa
  qué falló y cuánto costaría rehacerlo; no se regenera sin que el dueño lo autorice para esa pieza.
- **No se genera sin definición cerrada**: ficha del personaje con «Definición para generar», lugar definido
  en `entorno.md` con su imagen de referencia, y `03_keyframes/definicion.md` revisada por el equipo y
  autorizada por el dueño con el costo a la vista. Lo que falte se pregunta, no se supone.
- **Todo cambio que pida el dueño pasa primero por el equipo**: se abre una solicitud en `video-studio/cambios/`,
  se revisa qué toca de lo ya definido y qué habría que rehacer, y se le presenta con el costo y las dudas
  antes de aplicar o generar nada. Detalle en `video-studio/generacion.md`.

## Trabajo con videos

- Para ver un video: `python3 video-studio/herramientas/analizar_video.py <video> <salida>` y luego
  lee las hojas de contacto (`hoja_NN.jpg`). No se puede reproducir video directamente.
- Un video nuevo empieza con `python3 video-studio/herramientas/nuevo_proyecto.py <nombre> [referencia]`.
- El análisis de una referencia lo hace el agente `analista-de-video`; el prompt lo escribe
  `director-de-prompts`. La conversación principal coordina y habla con el usuario.
- Todo prompt define su elenco con personajes de `video-studio/personajes/`. Si el usuario no ha
  dicho quién sale, se le pregunta; no se inventan personajes ni se elige por él.
- No se da por bueno un prompt hasta que `validar_prompt.py` termina sin errores.
- Todo clip generado se revisa con `revisar_fotogramas.py` (gratis) antes de puntuar su rúbrica; el resultado va en `07_revision/`.
- El ritmo de redes (gancho, ráfagas de cortes, bucle, texto en pantalla) es solo para contenido de adultos:
  plantilla `prompt_video_redes.md`, proyecto con `--redes`. Nunca en series infantiles.
- Cada proyecto lleva `licencias.md` con el origen y la licencia de cada recurso.
- Los prompts son archivos `.md`. Una vez validado, cada prompt se archiva con `archivar_prompt.py` en
  `video-studio/personajes/<protagonista>/prompts/` dentro de `intro/`, `capitulos/`, `shorts/` u `otros/`.
  Ahí es donde el usuario los busca; `proyectos/` es solo la mesa de trabajo.

## Contenido infantil (series)

- Las series viven en `video-studio/series/<serie>/`. La primera es `granja`: Tiky y Lumi, 1 a 3 años.
- Un episodio se crea con `nuevo_proyecto.py <nombre> --serie granja` y pasa por el equipo en este orden:
  `pedagoga-montessori` (ficha pedagógica) → `guionista-interactivo` (guion) → `psicologa-infantil`
  (revisión) → `director-de-prompts` (prompt). Si la psicóloga pide cambios, vuelve al guionista.
- El `comercial-inteligencia-digital` trabaja después de la ficha pedagógica: entrega `publicacion.md` y su
  sección de la ficha técnica. Le habla al adulto que elige el video; no cambia el guion, y lo que proponga
  para dentro del video lo deciden la pedagoga y la psicóloga. Toda cifra lleva fuente y fecha.
- Idiomas: español (maestro), inglés y portugués de Brasil. El video es el mismo; cambian la voz
  (`voz_idiomas.md`) y el paquete de publicación (uno por idioma). Se adapta, no se traduce literal.
- Formatos en `video-studio/formatos.md`: capítulo e intro en 16:9 (1920x1080); short en 9:16 (1080x1920), 60 s o menos.
- Todos trabajan contra `video-studio/infantil/guia_1_a_3.md`.
- Cada prompt de serie lleva su `ficha_tecnica.md`: los objetivos de cada disciplina (pedagogía, Montessori,
  psicología infantil, aprendizaje interactivo, producción, comercial e inteligencia digital), escritos por su responsable antes de generar.
  Es la rúbrica del video: una vez generado se puntúa cada criterio y se calcula con `puntuar_ficha.py`.
- En la serie `granja` solo actúan `@tiky` y `@lumi` hasta que el dueño cargue los secundarios.
- El contenido infantil nunca se cruza con «M» ni con personajes para adultos.
- El resto de los personajes del dueño está en la rama `claude/focused-thompson-wojzu6` (`creador-personajes/`).
