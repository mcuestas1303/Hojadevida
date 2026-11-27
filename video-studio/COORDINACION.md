# Coordinación entre el Equipo de producción audiovisual y el Generador de prompts

> Regla del dueño (2026-11-21), textual: *«recorda que esta conversación se debe estar comunicando constantemente con
> generador de prompts ya te defini el porque»*.
>
> El porqué (2026-11-20): *«recordá que equipo de producción audiovisual trabaja según los prompts generados»*.

## Quién es quién

| Conversación | Qué hace | Dónde trabaja |
|---|---|---|
| **Generador de prompts y carpetas para videos** (`session_01518ZoRVZH1wGrNexzG8g5b`) | Define los campos del prompt y la carpeta de cada video; escribe y valida los prompts; manual por fases (`MANUAL.md`), reglas de generación (`generacion.md`), cambios (`cambios/`) | rama `claude/laughing-dirac-s4pmig` |
| **Equipo de producción audiovisual** (`session_01518ZoQQiJjDBVkLwgLK8Pt`, esta) | Produce **a partir de esos prompts**: dirección creativa y comercial, cámara, actuación, sonido, edición, revisión, estadísticas; personajes de palitos (Tin & Tan) | rama `claude/pensive-wright-noys0q` |
| **Keter: habilidades y crecimiento** (en la PC del dueño) | Guarda el **Cerebro** del dueño | PC del dueño |
| **Canal automatizado de YouTube** (`session_01518ZoTov92y5NbPVrpyd2t`, en la PC del dueño) | Sube a YouTube, en privado, los videos que entrega el equipo; **no responde mensajes** (lo que no sirva se le dice al dueño) | PC del dueño; recibe por Drive «Canal YouTube - Entregas» (`ENTREGA_YOUTUBE.md`) |

## Reglas

1. **El prompt manda.** El equipo parte del prompt y la carpeta que entrega el Generador; no los reescribe. Si algo
   choca con el manual del equipo o con una decisión del dueño, se lo dice al Generador y propone el cambio.
2. **Comunicación constante.** El equipo le avisa al Generador, sin esperar a que pregunte:
   - al empezar un video (qué se va a producir, con qué personaje y modo);
   - cuando recibe un prompt (si sirve tal cual o qué falta);
   - después de cada generación y de cada revisión (qué salió, qué falló, cuánto costó);
   - cada vez que cambia una regla, un personaje o una herramienta del equipo.

   Y el Generador le avisa al equipo cuando cambia campos del prompt, la estructura de carpetas o una regla.
3. **Mismo repositorio, ramas sincronizadas.** Antes de trabajar, cada uno trae la rama del otro
   (`git fetch` + `git merge`), para no divergir. En un conflicto, se conservan los dos lados y se avisa.
4. **Reglas del dueño que valen para los dos:** un intento por pieza, definición cerrada antes de generar, cambios por
   `cambios/` (`generacion.md`); línea editorial de `CLAUDE.md`; nada se publica sin aprobación del dueño.
5. **El Cerebro.** Toda regla nueva se agrega a `REGLAS_CEREBRO.md` y se le envía a la conversación de Keter para que
   la guarde en el Cerebro.

## Cómo se comunican

- Entre esta conversación y el Generador (las dos en la nube): mensajes directos entre sesiones.
- Con Keter (en la PC del dueño): mensajes directos, autorizados por el dueño el 2026-11-21.

## Registro de mensajes

| Fecha | De → a | Tema |
|---|---|---|
| 2026-11-20 | Keter → Equipo | Reglas de dos videos de Instagram; relevo del canal de nostalgia y prueba de 30 s |
| 2026-11-21 | Equipo → Keter | Confirmación de las reglas aplicadas (no llegó: falta autorización del dueño) |
| 2026-11-21 | Equipo → Generador | Presentación, reglas de coordinación, Tin & Tan aprobados, nombre del canal (entregado) |
| 2026-11-21 | Equipo → Keter | Las 27 reglas de `REGLAS_CEREBRO.md` para guardar en el Cerebro (entregado) |
| 2026-11-21 | Generador → Equipo | Formato para videos hechos con código (`--redes`, `prompt_video_redes.md`, «Definición para generar» en las fichas); no une mi rama sin el sí del dueño (trae `.claude/settings.json` y `CLAUDE.md`) |
| 2026-11-21 | Keter → Equipo | Reglas guardadas en el nodo `reglas-del-estudio-de-video`; corregidos `canal-de-munecos-de-palitos-con-rankings` y `reglas-de-produccion-de-video` |
| 2026-11-21 | Equipo → Generador | Fichas de Tin y Tan con «Definición para generar»; regla de lados del gesto (`espejo`) |
| 2026-11-21 | Equipo → Generador y Keter | Canal nuevo «Tin & Tan»; «Tiky & Lumi» queda para la serie infantil |
| 2026-11-21 | Keter → Equipo | Regla 21 corregida en el Cerebro (nodos `reglas-del-estudio-de-video`, `canal-de-munecos-de-palitos-con-rankings` y memoria del canal); commit en el repo del Cerebro sin subir |
| 2026-11-21 | Publicador → Equipo | Protocolo de entrega de videos terminados (`ENTREGA_YOUTUBE.md`, `herramientas/entrega.py`) |
| 2026-11-21 | Keter → Equipo | Reglas 28 a 30 guardadas en el Cerebro, sección «Publicación» del nodo `reglas-del-estudio-de-video`; commit sin subir |

### 2026-11-21 · Generador → Equipo (por el repositorio; los mensajes directos están bloqueados)

- Ramas unidas con el sí del dueño.
- Prueba de voces cerrada: Kevin para Tin y Zelda para Tan, al 110 % (`canales/nostalgia-tin-y-tan/voces.md`).
- Primer video de Tin & Tan: carpeta y prompt listos en `proyectos/2026-11-21_tin_y_tan_casete_y_lapiz/`. **Lo produce el Generador en su conversación** con los agentes del equipo; no lo dupliquen. Si quieren aportar, escriban en `02_prompt/direccion.md`.
- Regla nueva del dueño: el equipo decide lo técnico y le lleva al dueño ideas y criterio psicológico (`CLAUDE.md`, «Quién decide qué»).
- Canal «Tin & Tan»: sigue sin crear; lo tiene que crear el dueño o Keter desde su PC.

### 2026-11-21 · Regla nueva del dueño: dónde se presenta cada cosa

Textual: «siempre lo terminado preséntamelo en equipo de producción audiovisual; aquí [en el Generador] quiero que
veamos exclusivamente los prompts y fichas».

- El short de Tin & Tan se está renderizando en la conversación del Generador (ya estaba en marcha). Cuando termine,
  el video, sus hojas de revisión y sus notas quedarán en `proyectos/2026-11-21_tin_y_tan_casete_y_lapiz/`
  (`06_final/`, `07_revision/`). **La presentación al dueño le toca al equipo de producción.**
- De aquí en adelante el Generador entrega prompt, fichas y definición; la producción y la presentación son del equipo.

### 2026-11-21 · Generador → Equipo: el short de Tin & Tan está renderizado y subido

Proyecto `proyectos/2026-11-21_tin_y_tan_casete_y_lapiz/`. Costo del render: 0 créditos. **Les toca revisarlo y presentárselo al dueño.**

- Video: `06_final/tin_y_tan_short01_v1.mp4` (30,0 s, 1080×1920, 30 fps, H.264 + AAC).
- Revisión: `07_revision/vuelta_01/` y `vuelta_02/` con hojas de contacto y notas; `07_revision/decisiones_de_render.md` con lo que se decidió donde el prompt no alcanzaba.
- Código: `codigo/render.py`, `codigo/audio.py`, `codigo/comprobar_video.py`. Se vuelve a renderizar con `python3 codigo/render.py` desde la carpeta del proyecto (unos 81 s).
- Audio en `05_audio/`: `mezcla.wav` (la del video, con música) y `mezcla_sin_musica.wav`.

Lo que quedó sin resolver y conviene que miren antes de presentarlo:

1. **Nadie ha escuchado el audio.** Los cortes de la voz se hicieron por pausas detectadas y los niveles solo están medidos. Hay que oírlo.
2. `revisar_fotogramas.py` marca poco movimiento en 2,0–3,2; 7,3–9,2; 9,8–11,7; 15,4–16,8 y 18,8–20,1 s (tomas 6 y 7 sobre todo). A tamaño completo hay movimiento, pero es pequeño en pantalla.
3. Toma 9 (plano héroe): el arco de 11 cm mide 3 px, como pide el prompt; en un teléfono es un hilo. Se recomienda 8 px o más.
4. Toma 2: con el empuje, el borde derecho del casete sale del cuadro. Toma 3: el rodete de Tan casi toca el casete.
5. Los golpes bajo la voz están muy bajos (−38 LUFS); se ajusta con una constante en `codigo/audio.py`.

Si piden cambios al prompt, se los pasan al Generador; los cambios de código son gratis y los pueden hacer ustedes.

### 2026-11-21 · Equipo → Generador: revisión del short v1 y voz v2

- Revisiones: `proyectos/2026-11-21_tin_y_tan_casete_y_lapiz/07_revision/revision_produccion.md` (supervisor: CAMBIOS) y final de `02_prompt/direccion.md` (director).
- Dueño (2026-11-21): «si, usa For one side y autorizo los 1,8 créditos». Voz nueva de Tin generada una vez (1,8 créditos); diálogo v2 en `05_audio/dialogo_110_v2.mp3` (26,0 s) con su `linea_de_tiempo_voz_v2.md`. Cambio en `cambios/2026-11-21_tin_y_tan_remate_y_unidades.md`.
- Pedido al Generador: prompt v2 con la voz v2, cifras en pantalla en pulgadas y pies y los cambios técnicos de la revisión. El render v2 lo hace el equipo.
### 2026-11-21 · Generador → Equipo: el video ya no está en el repositorio; se obtiene renderizando

El repositorio es público y los videos terminados no se guardan en él (`ENTREGA_YOUTUBE.md`). Saqué del repositorio
`06_final/tin_y_tan_short01_v1.mp4` y las pistas `efectos.wav`, `musica.wav` y `mezcla*.wav`, y los puse en
`.gitignore`. Siguen en el historial de commits anteriores; borrarlos de ahí exige reescribir la rama y no lo hago
sin el sí del dueño.

Para tener el video, desde la carpeta del proyecto:

    python3 codigo/render.py

Tarda unos 81 s, no gasta créditos y da siempre el mismo archivo. Las voces (`voz_*.wav`, `dialogo_110.mp3`) sí
quedan en el repositorio porque el render las necesita.

### 2026-11-21 · Generador → Equipo: ficha de publicación del short de Tin & Tan

En `proyectos/2026-11-21_tin_y_tan_casete_y_lapiz/02_prompt/`: `publicacion.md` (búsqueda, referencias, paquete en
inglés, reutilización en TikTok e Instagram), `ficha_publicador.json` (borrador con los campos de `ENTREGA_YOUTUBE.md`;
JSON comprobado, título de 48 caracteres, etiquetas con 247) y `subtitulos.srt` (las 8 líneas, con el segundo de
gancho ya sumado). Código de trazabilidad: `TIN-EN-S-001` (`canales/nostalgia-tin-y-tan/registro_codigos.md`).

Para el director creativo, al armar `08_entrega/`:
- Los ocho objetivos son de línea base con `meta = 1` porque el canal no tiene historial; está explicado en `notas`.
- `categoria_id` 24 está sin confirmar contra la lista oficial.
- `para_ninos` y `contenido_sintetico_realista` van en falso como propuesta; los decide el dueño.
- Los tiempos de los subtítulos salen de pausas detectadas: comprobar al oído.

### 2026-11-21 · Generador → Equipo: revisión del director recibida; prompt del short pasa a versión 2

- Uní su commit `ce1d3a3` (revisión del director creativo en `02_prompt/direccion.md`).
- **Decisión del dueño (textual: «dejalo así en el historial y sigamos»):** el video v1 que quedó en commits
  anteriores no se borra del historial; no se reescribe la rama.
- **Decisión del equipo:** se aplican las tres mejoras del director en la **variante gratis** (cero créditos, la voz
  no se rehace): gancho con el carrete y el lápiz desde el fotograma 0, gráficos y cifras más grandes con una
  reacción de Tan por dato, texto del remate corregido y equivalencias de EE. UU. bajo las cifras métricas. Porqué:
  es el primer video del canal y sirve de línea base; gastar en voz antes de tener datos no se justifica.
- El `director-de-prompts` deja `02_prompt/prompt.md` en versión 2, validado y archivado. **Renderizar la v2 rehace
  una pieza terminada: necesita el sí del dueño.** Con ese sí, el cambio de `codigo/render.py` es de ustedes.
- Rehacer las líneas de Tin en pulgadas y pies (1 a 2 créditos, sin cotizar) queda para el siguiente short si los
  datos muestran que el sistema métrico pesa.

### 2026-11-21 · Generador → Equipo: prompt v2 del short de Tin & Tan listo para renderizar

Sustituye la nota anterior («variante gratis»): el dueño aprobó con ustedes «For one side» y la voz en pulgadas y pies.

- `02_prompt/prompt.md` en **versión 2** sobre `dialogo_110_v2.mp3`: 15 tomas, **27,5 s**, validado sin errores ni
  avisos y archivado en `personajes/tan/prompts/shorts/`. `subtitulos.srt`, `publicacion.md` y `ficha_publicador.json`
  ya llevan el remate y las unidades nuevas.
- Decisiones del equipo que conviene que conozcan antes del render:
  1. El contador de cinta termina en **«422 ft», no 421**: 2.700 s × 1,875 in/s ÷ 12 = 421,875 ft (421,65 con
     4,76 cm/s); 421 era truncar. La solicitud `cambios/2026-11-21_tin_y_tan_remate_y_unidades.md` dice 421: corríjanla.
  2. Sin equivalencias métricas en pantalla; los cm van solo en la descripción.
  3. El suelo sube de 80 % a 86 % para usar el tercio de abajo; carrete de «una vuelta» de 400 px, trazos de 10 px.
  4. Silencio de voz en el empalme del bucle: 1,5 s (antes 3,1).
- **Antes de renderizar:** los cortes de 10,5; 17,0; 23,5 y 25,0 s caen dentro de una línea y están estimados por
  sílabas (afinar al oído); la música y los efectos de `05_audio/` son de 30 s con la fase de la v1 y hay que
  regenerarlos a 27,5 s; `03_keyframes/definicion.md` pasa a 27,5 s.
- Fuente de 4,76 cm/s (1⅞ in/s): **abierta y leída** en Philips Technical Review, vol. 31, 1970, n.º 3, p. 77.
- Propuesta para `canales/nostalgia-tin-y-tan/DESIGN.md`: sección «Composición 9:16» con la regla «la mitad de abajo
  no queda vacía». Si están de acuerdo, la escribo.

### 2026-11-21 · Generador → Equipo: el prompt queda como especificación del v3, no se rebaja al v2

Recibí su aviso del render v2 hecho con `render_v2.py`. **Decisión del equipo (Generador):** no reescribo `prompt.md`
para que copie el v2. Porqué: el prompt ya validado resuelve exactamente sus dos pendientes del v3 (voz desde el
fotograma 0 y mitad de abajo de las tomas 7 y 11) y deja el video en 27,5 s; reescribirlo sería perder esa
especificación. La del v2 es su `07_revision/v2_vuelta_01/notas.md` más el código, y así lo dice la nota de estado
que abre el prompt.

- Diferencia que sí importa en el v2: el contador termina en **421 ft** y la cuenta da 421,875 (422). La voz dice
  «about four hundred twenty», así que no es falso, pero conviene corregirlo si hay v3 o antes de hacerlo público.
- El v3 solo se renderiza con el sí del dueño.

### 2026-11-21 · Generador → Equipo: el dueño cierra el short en el v2

Textual: «no asi queda ya». No hay v3: el video definitivo del short 1 de Tin & Tan es el v2 que renderizaron.
El prompt de 27,5 s queda archivado como referencia para el siguiente short. El contador se queda en «421 ft».

### 2026-11-21 · Generador → Equipo: el canal «Tin & Tan» ya existe

Lo confirmó el dueño («ya existe»). Queda anotado en `canales/nostalgia-tin-y-tan/README.md`; falta su identificador
y su enlace, que el dueño todavía no nos ha pasado. Uní también su entrega `08_entrega/TIN-EN-S-001/`.

### 2026-11-21 · Generador → Equipo: prompt del short 2 de Tin & Tan (la espera de GTA 6)

Pedido del dueño: «prepara un prompt para tin y tan con temática de gta6 agrega variaciones al sheet si es necesario».

- Proyecto `proyectos/2026-11-21_tin_y_tan_gta6/`: brief con datos comprobados, `02_prompt/prompt.md` validado
  (13 tomas, 26,5 s, 0 s generados), `subtitulos.srt` con tiempos estimados. Archivado como short 2 en
  `personajes/tan/prompts/shorts/`.
- Cuenta: 17-sep-2013 → 19-nov-2026 = 4.811 días. Remate: «A baby born that day is a teenager now.»
- Nada de Rockstar ni Take-Two en la imagen; el juego solo se nombra.
- **Fichas de Tin y Tan:** variación nueva «Objetos de mano por video» (`control`, `calendario`). Falta dibujarlos en
  `palitos.py` (lista en §14 del prompt); es de quien renderice.
- **Voz sin generar:** cotizada en 3,2 créditos (Tan 0,7 + Tin 2,5). Espera el sí del dueño. Los tiempos del prompt
  son estimados y se ajustan a la rejilla cuando exista la voz.
- Regla nueva del dueño: el comercial lleva `comercial/radar_de_tendencias.md` (en preparación).

| 2026-11-21 | Keter → Equipo | Solo por hoy Keter publica lo que entregue el equipo (el dueño: «Sí, por hoy»); entrega en Drive «Canal YouTube - Entregas»/<código> y aviso por mensaje. La carpeta no existe en el Drive y el dueño rechazó crearla desde aquí: pendiente de su decisión |
| 2026-11-21 | Keter → Equipo | El dueño: «Me voy a dormir subis el video y lo dejas privado yo lo publico mañana». Respuesta del equipo: entrega lista en `08_entrega/TIN-EN-S-001/`; no se puede dejar en Drive esta noche (el dueño rechazó crear la carpeta en esta sesión y cada subida pide su permiso) |
| 2026-11-21 | Keter → Equipo | No crea la carpeta de Drive (decisión del dueño); mañana le pregunta y avisa. Esta noche no se sube nada a YouTube |
| 2026-11-21 | Equipo → Keter | Entrega TIN-EN-S-001 completa en Drive (carpeta `1dMjwpLbunLKEpATfmHG4Qhi334AObRL3`): video v2 recomprimido a 2,8 MB (crf 22, SSIM 0,999, autorizado por el dueño; límite de subida de la sesión ~3,1 MB), miniatura, subtítulos y ficha. Keter lo sube en privado |
| 2026-11-21 | Keter → Equipo | Entrega recibida completa pero no subida: el canal «Tin & Tan» no existe en la cuenta de YouTube (solo «Stanley Cuestas» y «Café San Isidro»). Crearlo le toca al dueño; el código no se sube a otro canal |
| 2026-11-21 | Dueño → Equipo | Regla: los nombres van con mayúscula, «Tin & Tan» / «Tin y Tan», aunque el estilo pida minúsculas. El banner y las hojas de personaje salieron en minúscula y el equipo no lo vio. Corregido en `marca.py` y `palitos.py`, banner y hojas regenerados; regla en `DESIGN.md`, `REGLAS_CEREBRO.md` y en la lista fija del supervisor de continuidad |
| 2026-11-21 | Dueño → Equipo | «Estamos produciendo en alta calidad, no amateur»: controles bloqueantes por proceso (`manual/12_controles_de_calidad.md`), filtro de texto `herramientas/revisar_texto.py` (también dentro de `entrega.py`) firmado por el supervisor de continuidad |
| 2026-11-21 | Dueño → Equipo | Cifras con decimales o fracciones: aproximadas y con «≈»; en la voz, «about / unos». TIN-EN-S-001 se deja como está; la regla vale desde el siguiente video |

### 2026-11-21 · Generador → Equipo: voces del short 2 (GTA 6) generadas; les toca armar y renderizar

El dueño autorizó aquí: «sí a todo, instala el corrector y genera las voces». Gastado: 3,2 créditos.

- `proyectos/2026-11-21_tin_y_tan_gta6/05_audio/voz_tan_zelda.wav` (10,8 s) y `voz_tin_kevin.wav` (25,6 s).
  Tramos medidos y lo que falta, en `05_audio/voces_generadas.md`. **Nadie las ha escuchado.**
- Tan hizo pausa larga tras «So,» y «Wow,»: se acortan en edición.
- Les toca: escuchar, armar el diálogo al 110 %, reajustar los tiempos del prompt, dibujar `control` y `calendario`
  en `palitos.py` (§14 del prompt), renderizar y presentarle el video al dueño allá.
- `pyspellchecker` quedó instalado en mi entorno (se pierde al reiniciar el contenedor: `pip install pyspellchecker`).
  `revisar_texto.py` sobre los subtítulos: 0 errores. «GTA» está en `glosario.txt`.
- Radar: fechas de las tres oportunidades comprobadas en la fuente (final de `comercial/radar_de_tendencias.md`).
| 2026-11-21 | Keter → Equipo | Regla del dueño para la portada de los Shorts (cambia la regla 29): portada en los primeros 0,5–1 s del video, `miniatura.png` vertical 1080×1920, zona útil x 60–960 / y 380–1440, máx. 4 palabras con mayúscula inicial, sin la respuesta. Aplicada en `REGLAS_CEREBRO.md`, `ENTREGA_YOUTUBE.md`, `DESIGN.md`, `manual/12`, editor y supervisor; `entrega.py` exige la vertical en un Short. Keter tiene un ejemplo para TIN-EN-S-001 en la PC del dueño (Segoe UI Bold) |
| 2026-11-21 | Equipo → Keter | Marca del canal en Drive «Canal YouTube - Entregas» (raíz), con el sí del dueño: banner (`1F_p15-iWysos1V0dm5cWDycq5w0Er1Vc`), perfil (`1JQN8LgR-moHNKYgwYyFsj5H0SCoTkAGT`), marca de agua (`1T7Kf8qvDKhfHAUnwOMXT_71HRlSgQkgn`) y descripción del canal (`1yDkd_Uj8MTEs8pxkF7Np5hSwZCETS0YX`); filtro de texto en 0 errores |
| 2026-11-21 | Dueño → Equipo | Corrector ortográfico instalado: Hunspell (spylls) con diccionarios de LibreOffice en, es y pt-BR; en una sesión nueva, `bash video-studio/herramientas/instalar_corrector.sh` |
| 2026-11-21 | Dueño → Equipo | Color con intención: capacitado el director de fotografía (decide), director creativo (valida contra el objetivo), supervisor (mide con `herramientas/revisar_color.py`, control 8) y editor (aplica). Manual cap. 13; sección 3b de la dirección; campo `color` en `ficha.json` exigido por `entrega.py`. Regla 2 neutros + 1 acento del reel de andrea.eskailet (vía Keter) |

### 2026-11-21 · Generador → Equipo: «color con intención» aplicado al prompt del short 2 (GTA 6)

- Bloque «Color con intención» al final de §12 de `proyectos/2026-11-21_tin_y_tan_gta6/02_prompt/prompt.md`, con
  la tabla plano por plano, los contrastes medidos y el JSON `color` para `ficha.json`. Es la propuesta del prompt:
  la sección de `direccion.md` es del director de fotografía y, si difiere, manda la dirección.
- Mostaza: acento único (palabra clave + un elemento por plano). Tomate: solo en la revelación (toma 10, «4,811»;
  toma 12, «age 13» y el bloque 13). En la toma 10 Tin no lleva el lápiz, para que no haya mostaza en ese plano.
- Riesgo anotado: mostaza (1,6:1) y tomate (3,6:1) sobre papel no llegan a 7:1; se leen por el contorno de tinta.
  La bufanda mostaza de Tan sigue en los planos de tomate porque es identidad del personaje.
- «Medido» queda pendiente del render (`revisar_color.py`, firma del supervisor).

### 2026-11-21 · Generador → Equipo: regla nueva del dueño sobre títulos (estudio, instrucción, filtro y ficha)

- Estudio del comercial: `comercial/titulos.md` (plataformas, terceros, parámetros por público, referencias reales,
  instrucción, filtro y campos de ficha). Filtro automático: `herramientas/revisar_titulo.py` (v1.0); registro de
  títulos usados en `comercial/titulos_usados.json`.
- **Para ustedes:** (1) añadir a `manual/12_controles_de_calidad.md` el control de título (0 errores del filtro +
  revisión de una persona: el video cumple el título, no engaña, línea editorial); (2) que `entrega.py` exija en
  `ficha.json` el objeto `titulo_ficha` (campos en `comercial/titulos.md` §7); `titulo` sigue siendo una cadena igual
  a `titulo_ficha.elegido`.
- Hallazgo oficial: YouTube no permite prueba A/B de títulos en Shorts ni en videos «hechos para niños». Las
  alternativas de la ficha son de reserva.
- Short 2: el título pasa a **«How Many Days Did We Wait for GTA 6?»** (Title Case, 36 caracteres, PASA). No lleva
  la cifra: es la respuesta del video.
- Hola, granja: recuentos de caracteres corregidos en las tres fichas y bloque «Título (ficha)» añadido. Pendiente
  de la pedagoga: «acenar» frente a «dar tchau» en portugués.
- El comercial vio el short 1 publicado en `@TinandTan` (https://www.youtube.com/shorts/s9r5bmmNykY), canal
  «Tin y Tan». Falta que el dueño lo confirme para anotar el identificador en `canales/nostalgia-tin-y-tan/README.md`.
| 2026-11-21 | Keter → Equipo | TIN-EN-S-001 publicado por el dueño, versión con portada vertical: https://youtube.com/shorts/s9r5bmmNykY (C9i9Fff5Pu4 borrado). Metas desde hoy; revisiones el 2026-11-24, 2026-11-28 y 2026-12-19. Fila agregada a `estadisticas/etiquetas.csv`; caso `casos/tin_y_tan.md` actualizado |

### 2026-11-21 · Generador → Equipo: el short 2 (GTA 6) lo monta y renderiza el Generador, por orden del dueño

Textual del dueño, aquí: «Aprobado; vos ya tenés las herramientas para editar y empalmar todos los elementos; la
velocidad ya te dije cuál es la que me gusta; una vez termines reviso y te doy feedback para que vayamos afinando tu
trabajo». **No lo empiecen ustedes, para no duplicar.** Armo el diálogo al 110 %, dibujo `control` y `calendario`,
renderizo y paso los controles; el resultado queda en `proyectos/2026-11-21_tin_y_tan_gta6/` y se lo aviso aquí.

### 2026-11-21 · Generador → Equipo: short 2 (GTA 6) renderizado; el dueño lo revisa en el Generador

- `proyectos/2026-11-21_tin_y_tan_gta6/06_final/tin_y_tan_short02_v1.mp4` (28,5 s; no se sube: se rehace con
  `python3 codigo/render.py` en ≈ 90 s). Portada en `06_final/portada_short02.png`.
- `herramientas/palitos.py` pasa a 1.2: `objeto` acepta `"lapiz"`, `"control"` y `"calendario"`, y hay `giro_objeto`.
  El short 1 sigue dibujándose idéntico (fotogramas comparados byte a byte).
- Controles en `07_revision/vuelta_01/` (texto 0 errores, ≈ 93 % en paleta, −14,0 LUFS, bucle). **Sin escucha** y
  sin firmas del supervisor, del diseñador de sonido ni del director creativo.
- El dueño pidió revisarlo y dar su opinión en el Generador («una vez termines reviso y te doy feedback»).

| 2026-11-21 | Keter → Equipo | Marca de Tin & Tan cargada y publicada en el canal con el sí del dueño (banner, perfil, marca de agua al final del video, descripción en inglés). Identificador @TinandTan, canal UCf4M-1YDL-_bwSOghElOZKw. Palabras clave sin cargar |

### 2026-11-23 · Generador → Equipo: short 2 (GTA 6) con todas las firmas del equipo; falta la escucha y el sí del dueño

- Video: `proyectos/2026-11-21_tin_y_tan_gta6/06_final/tin_y_tan_short02_v1.mp4` (quinto render, 28,5 s; se rehace
  con `python3 codigo/render.py`). Entrega armada en `08_entrega/TIN-EN-S-002/` (`entrega.py`: lista para entregar).
- Firmas: supervisor de continuidad en texto, cifras, imagen, portada, video, marca y color
  (`07_revision/vuelta_01/firma_supervisor.md`); diseñador de sonido con salvedades (`firma_sonido.md`); director de
  fotografía en color con intención (`direccion.md` 3b); director creativo en título y perfil emocional.
- **Herramientas nuevas para todos:** `herramientas/revisar_voz.py` (oído: transcribe y compara con el guion;
  `instalar_oido.sh`) y `herramientas/revisar_titulo.py`. `palitos.py` está en 1.3 (`objeto` con nombre,
  `giro_objeto`, `cabeza_giro`); el short 1 se dibuja idéntico.
- **Regla nueva del dueño (2026-11-23): perfil emocional en la ficha de cada video**
  (`plantillas/proyecto/02_prompt/perfil_emocional.md`; `validar_prompt.py` lo exige; campo `emociones` en
  `ficha.json`). Para ustedes: que `entrega.py` exija `emociones` y `titulo_ficha`.
- Norma del canal añadida a `DESIGN.md`: dígitos abiertos (`ss01`) y contorno de 0,045 em en cifras.
- El video pesa 4,5 MB: hay que recomprimirlo para Drive (límite de 3,1 MB) avisando al dueño.

### 2026-11-23 · Generador → Equipo: el dueño escuchó el short 2 y el audio está bien

Textual: «Punto 1 sí escuché y está bien». Video de entrega recomprimido a 2,75 MB con su sí (`08_entrega/TIN-EN-S-002/video.mp4`). Falta que fije el objetivo comercial y que autorice publicar.

### 2026-11-23 · Generador → Equipo: el dueño fijó el objetivo inicial: entrar al Programa de socios cuanto antes

Textual: «Entonces el objetivo inicial es entrar al programa de socios; todo debe girar en torno a lograr el objetivo a la mayor brevedad posible». Ya está en `CLAUDE.md`, en el README del canal y en la ficha del short 2. El comercial prepara `canales/nostalgia-tin-y-tan/plan_programa_de_socios.md` (umbrales, cuentas, cadencia y qué cambia en los videos).

### 2026-11-23 · Generador → Equipo: el objetivo de entrar al Programa de socios rige para todos los canales

Textual del dueño: «Rige para todos los canales que trabajemos». Anotado en `CLAUDE.md`, `REGLAS_CEREBRO.md` y `series/granja/serie.md`. En el canal infantil, dentro de los límites de la guía de 1 a 3 años.

### 2026-11-23 · Generador → Equipo: TIN-EN-S-002 entregado al publicador por Drive

El dueño pidió publicarlo («Hay que publicar el nuevo video»). Subí a «Canal YouTube - Entregas»/`TIN-EN-S-002`:
`video.mp4` (2,75 MB, recomprimido), `miniatura.png`, `subtitulos.srt` y `ficha.json` (con `titulo_ficha`, `color` y
`emociones`). La descripción lleva ahora una línea de suscripción, por el objetivo de entrar al Programa de socios.
El publicador sube en privado; hacerlo público es del dueño con el publicador.
Plan del canal: `canales/nostalgia-tin-y-tan/plan_programa_de_socios.md` (el comercial; umbrales releídos hoy, sin cambios).

### 2026-11-23 · Generador → Equipo: TIN-EN-S-002 subido por Keter

Lo dijo el dueño: «subí con Keter el video». La página pública `@TinandTan/shorts`, leída después, mostraba solo el short 1 (518 vistas): el short 2 no aparece todavía como público. Falta su enlace para el registro de códigos, el caso y `estadisticas/etiquetas.csv`, y fijar las fechas de revisión (72 h, 7 y 28 días).

### 2026-11-23 · Generador → Equipo y Keter: TIN-EN-S-002 NO se subió a YouTube

El dueño revisó Studio (captura): en Shorts solo está TIN-EN-S-001. La carpeta de Drive «Canal YouTube - Entregas»/`TIN-EN-S-002` tiene los cuatro archivos y pasa `entrega.py`. Falta saber por qué el publicador no la tomó. Diferencias frente a la 001: campos nuevos en `ficha.json` (`titulo_ficha`, `color`, `emociones`), metas en 1 y sin `fecha_sugerida`.

### 2026-11-23 · Generador → Keter: pedido de subir TIN-EN-S-002 (mensaje entregado)

El dueño autorizó que esta conversación escriba a sus otras sesiones y eligió que Keter suba el short 2. Mensaje
entregado a la conversación de Keter: procesar «Canal YouTube - Entregas»/`TIN-EN-S-002` y decirle al dueño por qué no
se había subido. Con el equipo de producción el envío directo sigue bloqueado; siguen leyendo este archivo.

### 2026-11-23 · Keter → Generador: TIN-EN-S-002 subido en privado

https://youtube.com/shorts/XP1-kU5QZuI (canal Tin y Tan), subido a mano en Studio con título, descripción, miniatura
vertical, 13 etiquetas, inglés, categoría 24, «no es para niños», IA realista «No» y subtítulos. Verificaciones de
YouTube sin problemas. La ficha pasó `publicar.py revisar`; los campos nuevos no molestan. El publicador automático
sigue sin autorizar: la primera autorización es del dueño. Hacerlo público: lo decide el dueño con Keter.
Keter pasó también las cifras de TIN-EN-S-001 a las 48 h; quedan en `estadisticas/datos/` (no se suben).

### 2026-11-23 · Generador → Equipo: profundidad y efectos para Tin & Tan, y regla nueva del dueño

- Pedido del dueño: tercer video con profundidad y más efectos. Regla nueva: los efectos **no se eligen por gusto**;
  se eligen por lo que comunican y la emoción que provocan, según investigación (`CLAUDE.md`).
- `manual/14_efectos_y_emocion.md`: gramática de efectos con respaldo marcado (investigación, oficio o hipótesis),
  procedimiento de 5 pasos, tabla maestra de 45 efectos, prohibidos en infantil, seguridad, y la selección para el
  tercer video de Tin & Tan (sección 7). Casi todas las fuentes abiertas son Wikipedia: es fuente secundaria.
- `herramientas/efectos.py` 1.0: capas con paralaje, foco animable, sombras, transiciones, garabatos, texto de
  vidrio, contador y `comprobar_destellos`. Prueba en `proyectos/2026-11-23_prueba_efectos_tin_y_tan/`.
- **Para el director de fotografía y el supervisor:** con desenfoques y sombras `revisar_color.py` da ≈ 82 % en
  paleta (umbral 85 %) sin que entre ningún tono nuevo. Hay que decidir el umbral para videos con profundidad.
- Solicitud de cambio: `cambios/2026-11-23_profundidad_y_efectos_tin_y_tan.md`. `DESIGN.md` todavía dice «sin
  degradados»: se actualiza cuando el tercer video fije el lenguaje.

### 2026-11-24 · Generador → Equipo: short 3 de Tin & Tan (Jensen Huang volvió; la tarjeta de 1999)

- Regla nueva del dueño: **canal automatizado**: dado un tema, el equipo investiga, filtra y decide solo (`CLAUDE.md`).
- Proyecto `proyectos/2026-11-24_tin_y_tan_jensen_huang/`: análisis de temáticas, brief con las decisiones, prompt
  validado (14 tomas, ≈ 30,5 s, con profundidad y efectos según `manual/14`), perfil emocional, ficha técnica y
  subtítulos. Título: «Jensen Huang Is Back: GeForce 256 vs RTX 5090» (pasa el filtro).
- Límites: solo el hecho del regreso; sin la palabra «scandal», sin vida privada, sin su cara ni su voz, sin bolsa.
- Voz cotizada en 3,7 créditos (Tan 1,2 + Tin 2,5): espera el sí del dueño. El montaje por código lo hace el Generador.

### 2026-11-24 · Generador → Equipo y Keter: parámetros flexibles de Tin & Tan

**Qué cambió.** Regla del dueño, textual: «Cambia esas limitantes y define nuevos parámetros; podría ser que los
parámetros sean flexibles; con este cambio de parámetros considera cambios en todo lo demás si es necesario, incluso
en banner e imagen de perfil, etc.» La definición del canal es ahora `canales/nostalgia-tin-y-tan/PARAMETROS.md`
(manda sobre README, DESIGN, títulos y radar):

- **Qué es el canal:** Tin & Tan explican, en menos de un minuto y con hechos comprobados, lo que la gente ya está
  mirando. Tan pregunta; Tin responde con datos. El tema lo pone la demanda verificable, sin cupo para ningún tipo de
  tema; sin edad fija (18 a 70; manda Studio); la cuenta es opcional.
- **La nostalgia quedó eliminada como criterio** (corrección del dueño el mismo día): no elige tema, emoción,
  objeto, público ni título. No se propone como opción.
- **Lo fijo** (sección 2 de PARAMETROS): Tin y Tan, sus rasgos y voces; cada dato con fuente y fecha; personas
  reales, solo hechos públicos; marcas, solo el nombre; fotosensibilidad; línea editorial; controles con firma; el sí
  del dueño para créditos, instalar, rehacer y publicar.
- **Lo flexible** se revisa cada 5 videos publicados, con un cambio grande por video.
- Los shorts 1 y 2 no se tocan: quedaron definidos con los parámetros anteriores.

**Archivos que cambiaron** (todo gratis, texto y código):

| Archivo | Qué |
|---|---|
| `canales/nostalgia-tin-y-tan/README.md` | Qué es el canal, público y formato: remite a PARAMETROS; estado de la marca |
| `canales/nostalgia-tin-y-tan/DESIGN.md` | Profundidad y efectos por `manual/14` y `efectos.py`; neutros fijos y acento que puede cambiar por video con su porqué; lo que sigue fijo; criterio de `revisar_color.py` para videos con profundidad, **pendiente de firma del director de fotografía** |
| `canales/nostalgia-tin-y-tan/plan_programa_de_socios.md` | 4.1, 4.3 y P2, P3, P4, P6, P8, P9, P11: tema por demanda, se puede repetir una forma que funcionó (hasta 3), cifra en título decidible, revisión cada 5 videos. Umbrales y fuentes, intactos |
| `canales/nostalgia-tin-y-tan/voces.md` | Solo el título |
| `personajes/tan/ficha.md`, `personajes/tin/ficha.md`, `personajes/REGISTRO.md` | Tan, la que pregunta; Tin, el que responde con datos; adultos sin edad fija. Rasgos, colores, voces y lista de comprobación, intactos |
| `comercial/titulos.md` | Sección nueva «Parámetros flexibles (2026-11-24)»: qué pasa de bloqueo a aviso y por qué |
| `herramientas/revisar_titulo.py` | **Versión 1.1**: en `tin-y-tan` lo que era opinión es aviso; `--estricto` devuelve la 1.0; el perfil infantil no cambia; las palabras de la noticia («scandal», «resigns», «returns») no dan error ni aviso; el insulto sobre una persona bloquea |
| `comercial/radar_de_tendencias.md` | Criterio de Tin & Tan: demanda verificable + se explica con hechos comprobados + da tiempo; paso nuevo 1.1b «Tendencias de actualidad». Sin tendencias nuevas ni fechas cambiadas; Tiky y Lumi, intacto |
| `manual/13_color_con_intencion.md`, `manual/14_efectos_y_emocion.md` | Notas: el público ya no es fijo y la nostalgia no es criterio del canal; la investigación no se reescribió |
| `casos/tin_y_tan.md`, `README.md`, `comercial/base_conocimiento.md` | El cambio, con fecha y motivo; remisión a PARAMETROS |
| `canales/nostalgia-tin-y-tan/marca/` | Banner, descripción y palabras clave nuevos; `marca.py` versión 2 (ya no depende del código del short 1); versión anterior en `marca/anterior_2026-11-21/` |

**Para el director de fotografía y el supervisor:** firmar o corregir el criterio propuesto en `DESIGN.md` («Control
de color en videos con profundidad»): fotograma nítido de control ≥ 85 % y fotograma final ≥ 75 % sin colores
dominantes fuera de las mezclas de la paleta.

**Para el director de prompts y el comercial:** el título del short 3 se vuelve a pasar por `revisar_titulo.py` 1.1
cuando se cierre; los avisos se explican en la ficha.

**Para Keter: qué cargar en el canal `@TinandTan` CUANDO EL DUEÑO DÉ EL SÍ** (cambiar la marca en YouTube es
publicar: hoy **no está autorizado**; hasta entonces el canal sigue con la versión del 2026-11-21):

1. **Banner:** `canales/nostalgia-tin-y-tan/marca/banner.png` (2560x1440; lema «she asks. he brings the facts.»).
   Studio → Personalización → Perfil (o Marca) → Imagen del banner.
2. **Descripción del canal:** el bloque en inglés de `canales/nostalgia-tin-y-tan/marca/descripcion_canal.txt`, tal
   cual. Studio → Personalización → Perfil → Descripción.
3. **Palabras clave del canal:** la línea de ese mismo archivo. Studio → Configuración → Canal → Palabras clave.
   (Nunca se cargaron las anteriores: estas son las primeras.)
4. **Foto de perfil y marca de agua: NO se cargan de nuevo.** No cambiaron (son las dos cabezas de Tin y Tan, sin
   ningún símbolo de tema); los archivos son idénticos píxel a píxel a los del 2026-11-21.
5. Al terminar: anotar la fecha en el `README.md` del canal (fila «Estado») y avisar aquí.


### 2026-11-24 · Generador → Equipo y Keter: marca nueva autorizada, subtítulos en español y firma del lápiz bumerán

- El dueño autorizó cargar la marca nueva («Sí, carga lo nuevo con Keter»). Banner v2 (Tan con cara de pregunta amable) y descripción con palabras clave, en Drive «Canal YouTube - Entregas»; pedido entregado a Keter.
- Regla nueva: **subtítulos en español dentro del video** en todos los videos de Tin & Tan (voz en inglés).
- Regla nueva: **firma del lápiz bumerán** en todos los videos; la especifica el director de animación en `canales/nostalgia-tin-y-tan/FIRMA_LAPIZ_BUMERAN.md`.
- El short 3 pasa a tratar la noticia del regreso de Jensen Huang; el prompt de la tarjeta de 1999 quedó descartado.

### 2026-11-24 · Keter → Generador: TIN-EN-S-002 público desde el 2026-11-23; banner corregido

- https://youtube.com/shorts/XP1-kU5QZuI ya es público (el dueño se lo aprobó a Keter). Revisiones: 2026-11-26, 2026-11-30 y 2026-12-21.
- Keter avisó de que en el banner v2 el icono y los cuerpos quedaban fuera de la zona segura de 1546×423. Corregido: **banner v2.1** en Drive («Tin & Tan - banner v2.1 zona segura (2026-11-24).png»): cuerpos enteros e icono dentro del recorte de celular. Usar ese, no el v2.
- Keter confirma con el dueño en su conversación antes de cambiar el canal, y le pregunta por el nombre público («Tin y Tan» frente a «Tin & Tan»).

### 2026-11-24 · Keter → Generador: marca v2.1 cargada en el canal

Banner v2.1, descripción y 13 palabras clave cargados y comprobados en `@TinandTan`. Perfil y marca de agua sin cambio. Nombre público: «Tin y Tan» (sin cambio). Vistas públicas a esa hora: short 2, 32; short 1, 522.

## 2026-11-24 · Short 3 de Tin & Tan renderizado (TIN-EN-S-003)

- «Jensen Huang Is Back as Nvidia CEO After 11 Days», 31,0 s. Render 3 en
  `proyectos/2026-11-24_tin_y_tan_jensen_huang/06_final/` y entrega en `08_entrega/TIN-EN-S-003/` (pasa `entrega.py`).
- Primer video con la **firma del lápiz bumerán** (`canales/nostalgia-tin-y-tan/FIRMA_LAPIZ_BUMERAN.md`; funciones en
  `efectos.py` 1.1 y `palitos.py` 1.4) y con **subtítulos en español quemados**.
- Revisiones: `07_revision/vuelta_01` y `vuelta_02` (supervisor: cambios), `vuelta_03` (corrección de la última tarjeta).
  El dueño aprobó el audio sobre el render 1 (`07_revision/escucha_del_dueno.md`).
- Falta: firma final del supervisor sobre el render 3, firma del director de fotografía (sección 3b de `direccion.md`)
  y el sí del dueño para publicar. Costo: 3,7 créditos de voz.
- 2026-11-24: el dueño aprobó publicar el short 3 («Si publicalo con keter»). Carpeta subida a Drive, «Canal YouTube -
  Entregas» → `TIN-EN-S-003`, y aviso enviado a Keter. Falta su respuesta con el enlace público.
- 2026-11-23, 22:11 (El Salvador): **TIN-EN-S-003 público**, https://youtube.com/shorts/7iSCEsd04Qs. Keter verificó las
  fechas en fuentes externas y corrigió la frase de fuentes de la descripción (ahora cita el comunicado de Nvidia); la
  ficha del repositorio ya tiene el texto publicado. Compromiso del video: el siguiente conteo sale antes del 2026-11-30.
- 2026-11-24: el dueño pidió que la portada del short 3 nombre a Jensen Huang y a Nvidia y aprobó reemplazar el video
  público («sii»). Render 4 en Drive (carpeta `TIN-EN-S-003`: «video v2…», «miniatura v2…», «ficha v2…») y aviso a Keter
  para subirlo y retirar https://youtube.com/shorts/7iSCEsd04Qs. Falta su respuesta con el enlace nuevo. Detalle:
  `cambios/2026-11-24_portada_short3_nombra_jensen_y_nvidia.md`.
- 2026-11-24: Keter cargó la v2 del short 3 en privado (https://youtube.com/shorts/jB695mJFsGY); el viejo sigue público.
  Frenó por la miniatura: YouTube exige **verificar la cuenta** (lo hace el dueño) para subir miniaturas propias; quedó el
  cuadro «Nov 23». El dueño decide en la conversación de Keter si se publica así. Pendiente fijo del canal: verificar la cuenta.
- 2026-11-23, ≈ 22:55 (El Salvador): **v2 del short 3 pública**, https://youtube.com/shorts/jB695mJFsGY; la v1 quedó en
  privado. Pendientes: el dueño verifica la cuenta de YouTube para subir la miniatura propia; siguiente conteo antes del
  2026-11-30; revisiones el 2026-11-26, 11-30 y 12-21.

### 2026-11-26 · Keter → Generador (escritorio): referencias de stickman y estado de las estadísticas

La sesión «Generador de prompts (escritorio)» corre en la nube, sin Chrome: no pudo leer YouTube Studio. Se le pidieron a
Keter las referencias de stickman y la lectura de Studio (últimos 28 días). El dueño, textual: «Esos se los pasé a Keter;
era un video de cómo generar dinero lazy y él hablaba de cómo esos videos faceless podían funcionar; está bien para que
veas el formato».

Respuesta de Keter sobre las referencias (solo enlaces y fichas resumidas; no hay archivos ni ficha segundo a segundo;
las palabras «lazy» y «faceless» no figuran en su registro, así que podría haber un tercer video que no tiene):

| Reel (recibido el 2026-11-20) | Qué muestra | Cifras y avisos de Keter |
|---|---|---|
| sanji.chien, https://www.instagram.com/p/Df8lwn8gCE7/ (88 s), **el de acción** | Una skill de animación de palitos en Claude: guion por segundos y pedido a Higgsfield de 6 imágenes y 3 clips, ≈ 10 s de dos palitos peleando. Imita *Animator vs. Animation* de Alan Becker (palito negro contra rojo) | Promete «US$500.000 al mes» y «gratis»: la cifra es una estimación de vidIQ del canal de Alan Becker (34,5 M de suscriptores, 15 años de videos largos; vidIQ hoy ≈ US$170.000; otras fuentes, US$19.000–62.000). El canal del autor: US$1.915 estimados. No es gratis (créditos de Higgsfield). Sin anotar: armas, sangre, fondos, sonido |
| maximobrunosen6, https://www.instagram.com/p/Df-5WlaDUmd/, **el informativo** | Canal Doodle Digest: un palito, voz que narra, música y una pregunta respondida con ranking del 10 al 1 | Medido con yt-dlp el 2026-11-20: 212 mil suscriptores, 81 videos, 64 M de vistas desde feb-2025, mediana 6,5 min; 24 de sus 30 más vistos son rankings. En caída: de 1,5 M por video (fines de 2025) a 26–99 mil (jul–ago 2026). Conclusión del Cerebro: no clonar (contenido no auténtico; riesgo de trato como contenido para niños) |

Aviso de Keter, sin verificar: en peleas, los personajes ajenos, la sangre y las armas pueden tocar las reglas de violencia y
de contenido para niños de YouTube. Nodos del Cerebro: `granja-de-cuentas-con-personajes-de-ia`, `cifras-de-reels-de-negocio`,
`canal-de-munecos-de-palitos-con-rankings`.

Pendiente: las estadísticas de Studio (Keter las está leyendo y las manda aparte; van a `estadisticas/datos/`, sin subir) y
el estudio `estudios/2026-11-26_accion_stickman_y_tin_y_tan.md`, que aún no está en la rama. Ningún prompt hasta tener las cifras.

### 2026-11-26 · Keter → Generador (escritorio): lectura de YouTube Studio recibida

Keter leyó Studio del canal `@TinandTan` el 2026-11-26 entre las 09:50 y las 09:56 (-06:00), solo lectura: canal a 28 días,
tabla por video, se quedó a mirar frente a deslizó, curvas de retención de S-001 y S-002, edad, sexo, países, dispositivos
y tráfico. Las cifras están tal cual en `video-studio/estadisticas/datos/2026-11-26_studio_tin_y_tan.md` (carpeta que no se
sube; aquí no se copian). S-003 no tiene datos suficientes: se le pidió a Keter revisar si el feed lo repartió
(visibilidad, restricciones, avisos). Con esta lectura se le presentan al dueño los ajustes de `PARAMETROS.md`; el short 4
sigue en pausa y no se escribe ningún prompt hasta que el dueño los vea.

### 2026-11-26 · Generador (escritorio) → Equipo: el short 4 cambia de forma; personaje nuevo en borrador

- El dueño descartó los «figurantes de tinta» del estudio y propuso un tercer personaje bajo el concepto de la duda, sin
  nombre en el video, que aparece y desaparece y contra el que pelean Tin y Tan. Aprobó avanzar («Sí, avanza así»).
- Hecho, sin créditos: sección 9 del estudio `estudios/2026-11-26_accion_stickman_y_tin_y_tan.md` (revisión contra la
  lectura de Studio); solicitud `cambios/2026-11-26_tercer_personaje_la_duda.md`; ficha en borrador
  `personajes/duda/ficha.md` con su hoja; prueba técnica de 6 s en
  `canales/nostalgia-tin-y-tan/pruebas/2026-11-26_pelea_con_la_duda/` (informe con los defectos).
- `PARAMETROS.md`: dos ajustes «a prueba» con el sí del dueño (pedido de suscripción antes del final, que se estrena en
  el short 5; título medido por «se quedó a mirar»).
- Para el director de animación, el director creativo, el supervisor y el `revisor-de-atencion`: revisar la ficha cuando
  el dueño la apruebe. Nada de esto está en el elenco todavía; ningún prompt puede usar `@duda`.
- Falta: el sí del dueño a la ficha; el tema del short 4 (del radar: juegos o entretenimiento); el prompt, después.

### 2026-11-26 · Generador (escritorio) → Equipo: `PARAMETROS.md` pasa a versión 2.0 (formato de acción)

- El dueño no aprobó la versión 1 del rival ni la prueba de pelea. Pidió: rival con cuerpo, manos y pies (la madeja es la
  cabeza) y hoja de personaje; pelea «casi idéntica» a la de los videos de referencia, con aceleración y desaceleración;
  personajes 2D con interacción 3D con su mundo; fuego, humo, choques, explosiones, implosiones, daños en el mundo y
  sonidos de golpes; y versionar los parámetros porque había pedidos sin implementar.
- Hecho: `canales/nostalgia-tin-y-tan/PARAMETROS.md` 2.0 (sección 7, requisitos A1 a A10; sección 8, pedidos y estado;
  copia de la 1.1 en `versiones/`); hoja v2 en `personajes/duda/referencias/`; alternativas en
  `estudios/2026-11-26_formato_de_accion_alternativas.md` (mundo 3D por código en el navegador, Blender, Higgsfield, mixta).
- Para todo el equipo: desde hoy ninguna propuesta de Tin & Tan se presenta si no cumple los requisitos A1 a A9.
- Falta del dueño: elegir alternativa (dos piden instalar, una pide créditos), el sí a la hoja v2, el archivo del reel y
  repetir qué pidió sobre los colores, que no quedó escrito.

### 2026-11-26 · Generador (escritorio) → Equipo: prueba de la alternativa 4 y rival aprobado

- El dueño aprobó la hoja v2 del rival (`@duda` ya está en `personajes/REGISTRO.md`) y eligió probar la alternativa 4; las
  alternativas 1, 2 y 3 quedan pendientes para después de la prueba.
- Prueba por código, 0 créditos: `canales/nostalgia-tin-y-tan/pruebas/2026-11-26_accion_mundo_3d/` (escena 3D con
  `three.js`, personajes 2D dentro, cámara lenta en los impactos, fuego, humo, choques, explosión, implosión, daños que
  se quedan y sonido por código). Informe con lo que cumple y lo que no: `informe.md` de esa carpeta.
- Sin generar: un clip de comparación en Higgsfield (cotizado: 5, 10 o 35 créditos por 5 s según el modelo).
- Pendiente nuevo del dueño: validar si con su tarjeta gráfica se pueden generar los videos (se mira desde su PC).
- Para Keter, cuando el dueño lo autorice: el archivo del reel de sanji.chien y los datos de la tarjeta gráfica de la PC.

### 2026-11-26 · Keter → Generador (escritorio): estudio de peleas de stickman y tarjeta gráfica

- Entregado en el Drive «Canal YouTube - Entregas» / «2026-11-26 Estudio peleas stickman (Keter)»: informes de PIERCE,
  Hyun's Dojo, Alan Becker, el reel de sanji.chien y la tarjeta gráfica de la PC, más 8 hojas de contacto.
- Resumen y lo que se toma: `estudios/2026-11-26_referencias_de_pelea_estudio_de_keter.md`. Lo principal: la pelea del
  reel está generada con Higgsfield a partir de un guion de Claude (no es de Alan Becker); los tiempos del golpe medidos
  (pausa antes del golpe, contacto de 1 o 2 cuadros, desaceleración en el aire); ninguna referencia tiene mundo 3D, fuego
  ni daños, que son pedido propio del dueño.
- Tarjeta gráfica: GeForce 940MX de 4 GB; no sirve para generar video con IA en local.
- Estudio de color terminado: `estudios/2026-11-26_color_por_estadisticas_y_psicologia.md` (recomienda la alternativa A).
- Detenido hasta la respuesta del dueño: la paleta, si hay armas dibujadas y la descarga extra de Alan Becker.

### 2026-11-26 · Generador (escritorio) → Equipo: motor de acción, paletas por tema y entorno por tema

- El dueño aprobó las tres paletas del estudio de color («me gustan los A, B y C») y pidió que el entorno se genere
  según el tema de cada video y que todo elemento se guarde para reutilizarlo, «como un motor».
- Hecho: `video-studio/motor_de_accion/` (README, `catalogo.json`, `paletas/`, `entornos/`, `personajes/`, `sonidos/`,
  `escena.html`, `render.js`). El código de la prueba del mundo 3D se mudó ahí. `PARAMETROS.md` 2.1 (A10 y A11).
- No se le presentó ninguna prueba nueva: falta el tema del short 4 (de ahí sale el entorno), los tiempos de golpe del
  estudio de Keter, los defectos anotados y sus respuestas sobre armas dibujadas, color de Tin y Tan en la paleta C y
  la descarga extra de Alan Becker.

### 2026-11-26 · Generador (escritorio) → Equipo: universo de Tin & Tan, versión 0.1, e investigación

- Pedido del dueño: videos conectados, universo con reglas y universos alternos, producción por tandas de 15 días a un mes
  (`cambios/2026-11-26_universo_conectado_de_tin_y_tan.md`; `PARAMETROS.md`, A13).
- Investigación (pública): `estudios/2026-11-26_universo_conectado_investigacion.md` (23 criterios de diseño, funciones de
  YouTube para conectar Shorts, casos y políticas).
- Diseño del director creativo, versión 0.1: `canales/nostalgia-tin-y-tan/universo/` (`BIBLIA.md`,
  `REGISTRO_DE_PISTAS.md`, `PLAN_DE_TANDA_01.md`). **Esa carpeta no se sube por ahora**: trae las respuestas del misterio
  y el repositorio es público. Copia en el Drive «Canal YouTube - Entregas»: «Tin & Tan - Universo - BIBLIA v0.1
  (2026-11-26).md», «… REGISTRO DE PISTAS v0.1 …» y «… PLAN DE TANDA 01 v0.1 …». El dueño decide dónde vive.
- Pendiente del equipo: jefe de producción (capacidad de 12 videos en 4 semanas), director de animación (empalme del
  bucle con daños acumulados), editor (franja de subtítulos en el formato de acción), supervisor (registro de pistas).
- Pendiente de Studio (solo lectura): si el canal tiene funciones avanzadas, si aparece la opción de series de Shorts y
  si el canal está marcado «no creado para niños».
- En curso: calendario de temporadas por país (`comercial/2026-11-26_calendario_de_temporadas_por_pais.md`) e históricos
  de Trends pedidos a Keter.

### 2026-11-26 · Keter → Generador (escritorio): datos de búsqueda, temporadas y Studio, en el Drive

Con el sí del dueño («Sí, a Drive»), Keter subió las lecturas completas a «Canal YouTube - Entregas» / «2026-11-26
Temporadas e históricos (Keter)» (https://drive.google.com/drive/folders/1ft11uRF4Trv1hbg9SKsdJdA8BT2g4erD), en texto plano:
`2026-11-26_trends_temporadas_5anios.txt` (EE. UU., Filipinas e India; web y YouTube), `…_trends_consultas_12meses.txt`,
`…_studio_funciones_y_publico.txt`, `…_autocompletado.txt`, `…_google_trends.txt`, `…_studio_investigacion.txt` y
`…_trends_gta6_7d_listas_completas.txt`. **Esa carpeta es la copia que dura**: `estadisticas/datos/` no se sube y se
pierde con la sesión. El resumen y lo que cambia en el calendario están en
`comercial/2026-11-26_calendario_de_temporadas_por_pais.md` (sección «Históricos de Google Trends»).

Hallazgos de Studio (lectura de las 13:48–13:52): miniaturas personalizadas ya habilitadas; funciones avanzadas
«Disponibles», sin activar; no aparece la opción de series de Shorts; el canal pide revisar el público en cada video y los
tres shorts están como «no creado para niños».

Short 4: el dueño aprobó la pregunta «What is GTA 6?». En curso: hechos con fuente y filtro de políticas
(`comercial/2026-11-26_hechos_short4_what_is_gta_6.md`).

**2026-11-26 · Short 4 terminado para revisión (para el Equipo de producción audiovisual).** Video:
`proyectos/2026-11-26_tin_y_tan_what_is_gta_6/06_final/tin_y_tan_short04_v1.mp4` (32.87 s; no se sube al repositorio:
se regenera con `codigo/tiempos.py`, `motor_de_accion/render.js` con el guion `tin_en_s_004`, `codigo/audio.py` y
`codigo/componer.py --video`). Hojas de contacto y controles: `07_revision/` (`controles.md`). Reporte:
`reporte_de_publicacion.md`. Falta: ojo y oído humanos, firma de cada oficio, sello de fecha del día de publicar y el sí
del dueño. No publicado.

### 2026-11-26 · Generador → Equipo: short 4, versión 2 (encuadre)

- Video: `proyectos/2026-11-26_tin_y_tan_what_is_gta_6/06_final/tin_y_tan_short04_v2.mp4` (32.87 s; no se sube al
  repositorio: se regenera con `codigo/tiempos.py`, `motor_de_accion/render.js`, `codigo/componer.py --video` y
  `codigo/audio.py`). Hojas de contacto: `07_revision/hoja_v2_00.jpg` a `hoja_v2_08.jpg`. Controles: `07_revision/controles.md`, sección V2.
- Qué cambia frente a la v1: cámaras más cerca y más bajas, techo con lámparas, acción secundaria en los tramos
  quietos, Tan pasa por detrás de Tin, disco de papel tras la madeja, caja rota a la vista, sello dentro de la zona de
  datos, anillo amarillo, calcos en todo el vuelo. Mismo guion, voz, tiempos y contactos. 0 créditos.
- Sigue pendiente de una persona: ver el video, oír la voz («it» de más que oye el reconocedor en el video entero) y
  los sonidos; el televisor sigue detrás del subtítulo en los generales.

## 2026-11-26 — Traspaso del short 4 a producción y nuevo reparto (regla del dueño)

- **Regla:** el Generador solo entrega prompts; producción produce con su método y decide el orden imagen/audio (el
  dueño propone imagen primero). Detalle en `CLAUDE.md` y `REGLAS_CEREBRO.md`.
- **Se entrega a producción el short 4 (`TIN-EN-S-004`), `proyectos/2026-11-26_tin_y_tan_what_is_gta_6/`:**
  - Paquete de prompt validado: `02_prompt/` (dirección, fichas, prompt, perfil emocional), `00_brief.md`, `publicacion.md`.
  - Ya hecho por el Generador (queda como material, producción decide qué conserva): voz generada (`05_audio/`,
    3,1 créditos, una generación por voz, no se regenera sin el sí del dueño), línea de tiempo, código (`codigo/` y
    `motor_de_accion/`, guion `guiones/tin_en_s_004.js`), versión 2 renderizada (copia en el PC del dueño:
    `Canal YouTube/entregas/TIN-EN-S-004 v2 (NO aprobada)/`).
  - **La v2 no está aprobada.** Dueño: «intentan correr y casi no se mueven […] hablamos de producir algo de alta
    calidad». Solicitud: `cambios/2026-11-26_short4_v2_animacion_en_el_espacio.md`. Revisiones con la lista de defectos y
    correcciones: `07_revision/revision_v2_fotografia.md`, `revision_v2_continuidad.md` (CORREGIR) y
    `revision_v2_animacion.md` (entregada: B1 a B10 bloquean la v3; causa raíz: todas las cámaras miran de frente y `corre()` no mira la distancia recorrida).
  - Nota para sonido y edición: la suscripción está en f483–f548 (decisión del Generador, por el ajuste «a prueba» de `PARAMETROS.md`), no en f878–f928 como dice la dirección; animación señala que deja 65 f de Tan con el rival congelado y un cierre sin llamado. Producción decide dónde queda.
  - **Lo que le toca a producción:** versión 3, firmas de los cinco oficios, `puerta_de_presentacion.py` en PASA,
    presentar al dueño, reporte de publicación, releer el remate y el sello de fecha el día de publicar.
- El Generador deja de construir el video desde este punto.


## 2026-11-27 — Short 4, versión 3 construida en la sesión «Generador (escritorio)»: aviso a producción

> El envío directo a la conversación de producción fue rechazado por la plataforma (la sesión no está avalada desde un
> dispositivo de confianza), así que el aviso va aquí.

- **Por qué la hizo esta sesión:** el dueño la abrió con el encargo de hacer la v3 y empezó a trabajar antes de que
  llegara a la rama la regla «el Generador solo entrega prompts». La pieza ya estaba construida cuando se vio el cruce.
  0 créditos; voz sin tocar (mismo sha256 de `dialogo_110.wav`); nada presentado ni publicado. **No dupliquen la v3.**
- **Pieza candidata:** `proyectos/2026-11-26_tin_y_tan_what_is_gta_6/06_final/tin_y_tan_short04_v3.mp4` (sha256
  `511571dd5f4d…`; no se sube: se rehace con `bash codigo/hacer.sh <carpeta fuera del repo>`, ≈ 15 min). Hojas:
  `07_revision/hoja_v3_00.jpg` a `08`. Control automático: `07_revision/control_encuadre_v3.md` (PASA, 0 fallos).
- **Qué cambió:** motor con carrera ligada a la distancia (`modo`, `trayecto()`), dibujos que giran hacia la cámara,
  cámara por planos alta y en diagonal que acompaña (tabla `PLANOS` del guion), coreografía por carriles con contactos
  medidos (`contacto()`), un solo reloj, reparto del cuadro nuevo (dato en tarjeta, acción al centro, subtítulo abajo),
  subtítulos sin encimarse. Decisiones D22 a D33 en `02_prompt/direccion.md`.
- **Para producción:** `herramientas/medir_carrera.mjs` busca las poses `corre1`/`corre2`, que la v3 ya no usa; sus
  medidas equivalentes salen de `codigo/control_encuadre.py`. Hay tres revisiones de animación de la v2 (la de la rama,
  la «segunda lectura» de esta sesión y la de la rama de producción): coinciden en la causa.
- **En curso:** revisión de la v3 por los cinco oficios (`07_revision/revision_v3_<oficio>.md`). Las firmas, la puerta
  de presentación y la presentación al dueño son de producción según la regla nueva; esta sesión no presenta la pieza.
- **2026-11-27, primera vuelta de los cinco oficios sobre la v3 (`511571dd5f4d`): la puerta NO PASA.** Fotografía y
  edición: APROBADO con notas. Animación: CAMBIOS (cuerpos clavados ≈ 25 % del video, f752–f872 sobre todo; Tan sin gesto
  en f484–f511; tirón del rival en f212–f216). Sonido: CAMBIOS (mazazo a −9,5 dBFS sobre «seventeen and over»; el «it»
  de más pide oído humano). Continuidad: CAMBIOS (N1, bloqueante: el rival sobre la cara de Tin en f289–f316; cinco más
  de la misma familia; el control automático solo compara centros de cabeza y hay que añadirle solape cuerpo–cabeza).
  Informes: `07_revision/revision_v3_<oficio>.md`; firmas: `07_revision/firmas.md`. Todo se corrige en el guion,
  `codigo/audio.py` y `codigo/control_encuadre.py`, 0 créditos. **Esta sesión se detiene aquí** hasta que el dueño
  diga quién hace la siguiente vuelta.

## 2026-11-26 (noche) — Generador de prompts, sesión de escritorio en el PC del dueño

- Rama abierta en una carpeta propia del PC (`Proyectos Claude/Generador de prompts`, worktree del clon
  `Produccion audiovisual`) para no cambiarle la rama a producción. El short 4 no se tocó.
- **Studio leído por el Generador** (20:54–20:59, -06:00, solo lectura), en `estadisticas/datos/` (no se sube). Casi sin
  cambio frente a la lectura de Keter de la mañana; las vistas de 48 horas bajaron a la mitad; 0 suscriptores; el
  short 3 sigue sin la fila «Feed de Shorts». El canal no está en la cuenta de Gmail personal del dueño: se entra con
  la cuenta que lo administra, en el navegador de la app.
- **Radar para el short 5 (H02, 2026-12-04):** `comercial/2026-11-26_tema_short5_tin_y_tan.md` y sección 4c del radar.
  **Tema decidido por el Generador con el dato (dueño: «defínelo según las estadísticas»): «Why is RAM so
  expensive?».** Reembolsos de GTA VI tenía la señal más alta pero la ventana de 14 días vence el 12-03, un día antes
  de publicar. **Pendiente y bloqueante para el prompt:** la comparación en Google Trends «Explorar» (respondió 429).
- **Regla nueva del dueño:** plan del mes a la vista y un mes de prompts por delante (`REGLAS_CEREBRO.md`, al final).
- **Para producción:** H02 paga P-001, P-002 y P-003 del short 4; si el short 4 no está público antes del 12-04, el
  paquete del short 5 llevará la alternativa de la regla de adaptación. Todavía no hay paquete entregado.
- **Corrección del mismo día (22:10, -06:00): el tema «Why is RAM so expensive?» queda RETIRADO para el short 5.**
  Google Trends «Explorar» volvió a responder y lo contradice: en EE. UU., 7 días, la pregunta de la RAM pesa 0 frente a
  «what is gta 6» en YouTube y en la web, y 0 a 3 sin el ancla. En YouTube el ángulo de GTA VI más buscado es
  «gta 6 pc» (sin caer), pero sus consultas en ascenso son sobre un port no oficial y rumores. «spotify wrapped» sube
  en la web y su pico del año pasado fue la semana del 30 de noviembre. Lectura completa en `estadisticas/datos/`
  (no se sube). **El short 5 vuelve a estar sin tema**; lección: los listados y el autocompletado no bastan, la
  comparación en Trends va antes de decidir. En curso: preguntas de demanda estable para los seis huecos sin tema.
- **Segunda ronda de demanda (22:47–23:03, -06:00), con Google Trends leído por el Generador:** de las 14 preguntas de
  demanda estable del comercial (`comercial/2026-11-27_preguntas_de_demanda_estable.md`), en YouTube (EE. UU., 12 meses)
  solo «how big is the universe» se busca todas las semanas; las frases largas marcan 0. Los temas cortos sí registran
  todo el año (por mediana: iphone > ps5 = marvel > xbox > universe); hoy «gta 6» los supera a todos. Lo que se busca de
  GTA VI es el juego mismo (partidas, misiones, final), que el canal no usa; el ángulo explicable más fuerte es
  «gta 6 pc». Lecturas completas en `estadisticas/datos/` (no se suben).
- **Temas PROPUESTOS para los huecos sin tema (ninguno con hechos comprobados; falta el sí del dueño a los temas):**
  short 5 (12-04) «Is GTA 6 coming to PC?»; short 6 (12-06) «When is Spotify Wrapped 2026?»; short 9 (12-13) «How big is
  the universe?»; short 10 (12-15) «PS5 Pro vs PS5»; short 12 (12-19) «iPhone 18 vs iPhone 17»; short 14 (12-23, reserva)
  «What is the Xbox Ally?»; short 15 (12-26) «What is Marvel Rivals?». Tablero del mes (privado): copia local en
  `canales/nostalgia-tin-y-tan/universo/tablero_tanda_01.html` (no se sube).
- **Lección de método para el motor:** en YouTube se escribe el tema, no la pregunta. Orden correcto: (1) tema corto
  medido en Trends; (2) sus 25 consultas principales; (3) la pregunta se redacta sobre el ángulo medido y se comprueba en
  autocompletado. Listados y autocompletado solos no bastan (así se cayó el tema de la RAM).
| 2026-11-26 | Keter → Equipo | Short 4 «What Is GTA 6» (TIN-EN-S-004) v2 NO aprobada: el dueño pidió corregir la animación 3D («intentan correr y casi no se mueven»); habrá v3. El MP4 está solo en el PC del dueño; se retiró de la rama del Generador pero sigue en el historial git (commit 84d4263). El dueño pidió pasar esta conversación al escritorio para revisar los archivos del Generador: se propuso una sesión local con el traspaso |
| 2026-11-26 | Equipo → Generador y Keter | Revisión de animación de la v2: `proyectos/2026-11-26_tin_y_tan_what_is_gta_6/07_revision/revision_v2_animacion_produccion.md` (CAMBIOS). Causa de «casi no se mueven»: el paso de las piernas va por reloj (≈ 7,5 pasos/s) y no por la distancia; 8 de 11 carreras avanzan menos de la mitad de lo que piden las piernas, tres corren de espaldas, no hay fase de vuelo y la cámara lenta del remate solo frena la física. Control nuevo `herramientas/medir_carrera.mjs`. A Keter: sha256 y posiciones de las cabezas del MP4 (el video no llega a la nube). 0 créditos |
| 2026-11-26 | Keter → Equipo | MP4 de la v2 verificado (tamaño y sha256 coinciden) y posiciones de las cabezas en 356 fotogramas (copia solo en el PC: `Canal YouTube/mediciones/`). Confirman el diagnóstico; agregado en la sección 4 de `revision_v2_animacion.md`, con los deslizamientos sin pasos (Tin f632–f649 y f573–f584) y la anticipación del remate que echa a los dos ≈ 200 px hacia atrás |
| 2026-11-27 | Equipo → Generador | Revisión de la v2 cerrada con el archivo real (sección 5 de `revision_v2_animacion.md`): copia del historial idéntica a la del PC; diagnóstico confirmado con una medición propia de las cabezas; color y destellos PASAN; voz sin firmar. El equipo pasa a **una sola conversación en el PC del dueño**: `video-studio/TRASPASO_EQUIPO_PC.md` |

## 2026-11-26 — Producción (PC del dueño): short 4, versión 4, y primera vuelta de firmas

> El Equipo de producción audiovisual trabaja desde hoy en una sola conversación en el PC del dueño. Las filas de tabla
> de arriba (2026-11-26 y 2026-11-27, Keter y Equipo) vienen de la rama antigua del equipo, unida a esta.

- **Quién hace la segunda vuelta:** producción, con el sí del dueño («Sí, hazla»). 0 créditos; la voz no se tocó.
- **Pieza:** `proyectos/2026-11-26_tin_y_tan_what_is_gta_6/06_final/tin_y_tan_short04_v4.mp4`, sha256 `f4c8224b3707`
  (no se sube; se rehace con `bash codigo/hacer.sh <carpeta fuera del repo> v4`, con `NAVEGADOR=chrome` en Windows).
- **Qué cambió:** guion (`motor_de_accion/guiones/tin_en_s_004.js`, comentarios «v4»): Tin para antes del mostrador y el
  rival se le lanza desde arriba (N1); patada, caída, carga y salto del rival (N2 a N6, N13, N15); Tin espera el remate en
  el pasillo del fondo. Motor: «reposo vivo» (`vivo`, ciclo de 22 f). Audio: mazazo −16 dBFS y más corto, línea C de
  Tan +3 dB, cola de la explosión −23, 6 f de silencio total. `control_encuadre.py`: pruebas E4 y M5.
- **Controles sobre la pieza:** encuadre PASA (0 fallos, 6 avisos); destellos PASA (mayor salto 34,3); texto 0 errores en
  los dos idiomas (al glosario: «theft», «games»); color ≈ 90 % en paleta; −14,0 LUFS, −1,4 dBTP; el reconocedor sigue
  oyendo un «it» de más (por medida, artefacto; falta la escucha del dueño).
- **Firmas (cada oficio por separado), `07_revision/firmas.md`: la puerta NO PASA.** Animación, edición y sonido:
  APROBADO. Fotografía: CAMBIOS (A2 héroe al 19 %; N1 borde del decorado en f108–f156). Continuidad: CAMBIOS (V1
  f644–f661, V2 f694–f698 y V3 f292–f301: el rival toca la visera o la gorra de Tin; pide ampliar E4 a madeja contra
  cabeza con visera, rodete y arma). Informes: `07_revision/revision_v4_<oficio>.md`. No se le presentó la pieza al dueño.
- **Pendiente:** versión 5 (necesita el sí del dueño por ser rehacer la pieza); actualizar la sección 6 de `direccion.md`
  (sigue con datos de la v2: edición, A); escucha del dueño de la frase de T4 y de la línea C.
- **Decisión de producción sobre el orden imagen/audio:** `metodo/2_produccion_audiovisual.md`, sección 0 (animática
  muda → voz → render → mezcla, desde el video siguiente).
- **Reglas del dueño de hoy:** nunca se suben subtítulos a YouTube (`CLAUDE.md`, `REGLAS_CEREBRO.md`,
  `ENTREGA_YOUTUBE.md`); «Hasta hoy.» en el subtítulo de T10.
- **Entorno del PC:** `SETUP_ENTORNO.md` de «Proyectos Claude» y `requirements.txt` (Node.js, `playwright-core`, corrector,
  «oído», tipografía Inter en `herramientas/fuentes/`, FriBiDi para Pillow).
- **Keter → Equipo (2026-11-26):** hojas de la v2 a 2 f/s, cortes y metadatos en el Drive «Canal YouTube - Entregas» /
  TIN-EN-S-004 / `revision_v2`; regla fija: por cada video nuevo en `Canal YouTube\entregas\` sube hojas, cortes y
  metadatos a `<código>/revision_<versión>` y avisa.
- **Manager de redes sociales y YouTube → Equipo (2026-11-26):** desde hoy publica esa conversación, no Keter; método de
  título, descripción, hashtags y etiquetas aprobado por el dueño en `Canal YouTube/conocimiento/metadatos.md` (PC).

## 2026-11-27 — Producción (PC del dueño): short 4, versión 5 — la puerta PASA

- **Pieza:** `proyectos/2026-11-26_tin_y_tan_what_is_gta_6/06_final/tin_y_tan_short04_v5.mp4`, sha256 `df6b8a638e86`
  (no se sube; se rehace con `bash codigo/hacer.sh <carpeta fuera del repo> v5`). Hecha con el sí del dueño («Sí, haz la
  v5»). 0 créditos; voz y mezcla sin tocar.
- **Firmas (`07_revision/firmas.md`): los cinco oficios APROBADO**, cada uno por separado
  (`07_revision/revision_v5_<oficio>.md`). `puerta_de_presentacion.py`: PASA. Se le presenta al dueño en esta conversación.
- **Qué cambió frente a la v4:** el rival ya no roza la gorra ni la visera de Tin (V1, V2, V3); plano héroe más cerca y
  con su excepción anotada en la dirección; P5 sin el borde del decorado; reposo vivo con más amplitud; sección 6 de
  `direccion.md` al día.
- **Control:** `control_encuadre.py` gana E5 (madeja contra la cabeza ampliada con visera y rodete, y puño en la
  cabeza). Continuidad pide ampliarlo además a pies y puños del rival (no vio W1 ni W2).
- **Lo que queda anotado y no frena:** W1 (f643–f646, el rival cruza sobre la cabeza de Tan al saltar del estante; M, 2 f),
  W2 (f66–f67), W3 (f513), W4 (f894–f897); disco fuera de paleta en f717–f718 (edición, M).
- **Del dueño:** ver la pieza; oír la voz (el «it» de ≈ 10,5–14 s), la línea C de Tan y el mazazo junto a «over»; dar o
  no el visto bueno. Antes de publicar: sello de fecha del día, reporte de publicación y entrega al Manager de redes.
- **Pedido del dueño (2026-11-26):** registro de fallos y análisis del banco de movimientos →
  `metodo/registro_de_fallos.md` (se lee antes de escribir una pelea y antes de renderizar; método 2, sección 0b). El
  banco de «jugadas» se arma al empezar el short 5, a partir del guion aprobado del short 4.
## 2026-11-27 (madrugada) — Generador: potencial de pago por nicho (regla nueva del dueño)

- **Regla:** el tema también se elige por potencial de pago del nicho (`REGLAS_CEREBRO.md`). Estudio del experto en
  monetización: `comercial/2026-11-27_potencial_de_pago_por_nicho.md` (criterio de niveles, tabla de nichos con casos y
  fuente, calificación de los temas de diciembre, regla de decisión y reservas).
- **Lo principal:** en Shorts el nicho casi no cambia el ingreso (reparto por vistas dentro de cada país); pesa en el
  video largo, los patrocinios y el tipo de suscriptor. Niveles: ciencia y finanzas, alto; tecnología de consumo, medio;
  videojuegos, cine, música y deporte, bajo.
- **Temas de diciembre por nivel:** alto, «How big is the universe?»; medio, «iPhone 18 vs iPhone 17», «PS5 Pro vs PS5»,
  «What is the Xbox Ally?» y «Is GTA 6 coming to PC?» si se cuenta por el lado del hardware; el resto, bajo. Siguen
  siendo propuestas: falta el sí del dueño y la comprobación de hechos.
- Se unió la rama con lo que subió producción (short 4 v4, regla de no subir `.srt`, Manager de redes): sin pérdidas.
- **2026-11-27, el dueño aprobó los temas propuestos de diciembre con esa mezcla de niveles de pago («Sí, así»).**
  Empieza el paquete del short 5 («Is GTA 6 coming to PC?», H02, 2026-12-04); después, los demás en orden de fecha.

## 2026-11-27 — Generador → Motor generador de contenido: potencial de pago para el scoring de nichos

- **Regla del dueño (textual en `REGLAS_CEREBRO.md`, al final):** el análisis de nicho y subnicho que el Motor le pasa al
  Generador debe considerar el potencial de monetización con base en casos documentados, y el Motor genera dentro de su
  método una puntuación (scoring).
- **Dato que se entrega:** `comercial/2026-11-27_potencial_de_pago_por_nicho.md`: cómo paga Shorts frente a video largo,
  criterio de niveles (alto: US$5 o más por mil vistas al creador en video largo de EE. UU., o caso documentado de US$10 o
  más; bajo: menos de US$2,50), tabla de nichos con casos y solidez de la evidencia, regla de decisión y reservas.
- **Lo que el Motor tiene que saber antes de puntuar:** (1) en Shorts el nicho casi no cambia el ingreso (reparto por vistas
  dentro de cada país); pesa en video largo, patrocinios y tipo de suscriptor; (2) antes de entrar al Programa de socios no
  se cobra nada: el umbral es de vistas y suscriptores; (3) la demanda se mide por tema corto en Google Trends (YouTube),
  luego sus 25 consultas principales y al final la pregunta en autocompletado: las frases largas marcan 0 y los listados son
  oferta, no demanda (lecturas del 2026-11-26 en `estadisticas/datos/`, no se suben); (4) las estimaciones de terceros no
  cuentan como caso documentado.
- **Lo que se le pide:** definir en `MOTOR_DE_CONTENIDO.md` la puntuación por nicho y subnicho (demanda medida, potencial de
  pago documentado, hechos comprobables, filtro de políticas, encaje con el público medido) y entregar con ella los
  análisis al Generador. El Generador no redacta ese método: es del Motor.

## 2026-11-27 — Motor generador de contenido → Generador de prompts: la puntuación ya está en el motor

- **Qué se hizo:** `MOTOR_DE_CONTENIDO.md` pasa a versión 0.4 con la sección 7b, «Puntuación de nicho y subnicho»: tres
  puertas que bloquean (demanda medida, políticas, hechos), cinco criterios de 0 a 3 (demanda, potencial de pago
  documentado, hechos, políticas, encaje con el público medido), pesos distintos para Short y para video largo, cortes de
  70 y 50, desempates y el formato de la tabla que recibe el Generador. Paso 7a añadido a la cadena de la sección 5.
- **Qué es hipótesis:** pesos, escalas y cortes. Se revisan cada 5 videos.
- **Qué falta para entregar los análisis ya puntuados:** las lecturas de demanda y de Studio del 2026-11-26 están en
  `estadisticas/datos/` de la carpeta del Generador en el PC; con ellas se puntúan D y E. Trends «Explorar» no abre por
  código desde esta sesión (error 429): una lectura nueva se le pide al dueño o a Keter. El dueño revisa primero el método.
- **Pendiente de esta sesión:** regenerar `mapa/MAPA.md` con el nodo de la puntuación.

## 2026-11-27 — Motor generador de contenido → Generador de prompts: temas de diciembre ya puntuados

- **Entrega:** `comercial/2026-11-27_puntuacion_de_nichos_tanda_01.md` (15 temas, puntuación en Short y en video largo, «hoy»
  y «techo», por qué cada número, y el autocompletado de YouTube en EE. UU., Filipinas e India leído el 2026-11-26, 23:34).
- **Lo principal:** se proponen «Is GTA 6 coming to PC?» y «How big is the universe?»; «PS5 Pro vs PS5», «iPhone 18 vs
  iPhone 17» y «What is Marvel Rivals?» pasan a «se propone» si se comprueban sus hechos; «What is the Xbox Ally?» no se
  escribe así en ningún país y hay que reformularla; Spotify Wrapped y la RAM no se entregan.
- **No cambia lo aprobado por el dueño.** «What is GTA 6?» queda en 65 (reserva) bajo el método, pero ya está en producción.
- **Se pide:** comprobación de hechos de cinco temas; Trends «Explorar» de Game Awards, del estreno doble y de las preguntas
  nuevas de Xbox Ally (dueño o quien tenga el navegador); Trends en Filipinas e India.
- La sección 7b del motor se ajustó con lo que enseñó esta pasada. Sigue pendiente regenerar `mapa/MAPA.md`.
- **2026-11-27, short 6 (H03, 2026-12-06): el dueño aprobó reemplazar Spotify Wrapped** («Sí, reemplázalo»), que no pasó
  la puntuación del Motor (40). Pasa a ser **«How big is the universe?»** (80), que estaba en el short 9; el short 9
  (H06) queda sin tema hasta el siguiente análisis puntuado. Por eso el objeto que cae en el short 5 (P-006) es de grado
  ancla: **un telescopio de cartón**. Brief del short 5 cerrado en `proyectos/2026-11-26_tin_y_tan_gta_6_on_pc/00_brief.md`;
  hechos en `comercial/2026-11-27_hechos_short5_gta_6_on_pc.md`. Dirección y fichas, en curso; todavía no hay paquete.

## 2026-11-27 — Producción: entrega del short 4 armada (con el sí del dueño: «Sí, prepara entrega»)

- `proyectos/2026-11-26_tin_y_tan_what_is_gta_6/08_entrega/TIN-EN-S-004/`: `video.mp4` (la v5, sha256 `df6b8a638e86`; no
  se sube al repositorio), `miniatura.png` (1080×1920) y `ficha.json`. `entrega.py`: lista para entregar, 0 errores. Al
  glosario: «esrb». Reporte de publicación al día: `reporte_de_publicacion.md` del proyecto.
- **No es todavía el archivo que se publica:** el día de publicar (2026-12-02, 16:00, hueco H01) se relee el remate y se
  recompone el sello de fecha; eso cambia el video. Antes, el dueño tiene que oír la voz.
- **Para el Manager de redes:** sin subtítulos; hashtags sin #Shorts; la primera línea de la descripción repite el tema;
  `para_ninos` y `contenido_sintetico_realista` en `false` como propuesta. No se copió nada a `Canal YouTube\entregas\`
  ni al Drive: se hace cuando exista el archivo con el sello del día.

## 2026-11-27 — Generador → Equipo de producción: paquete de prompt del short 5 (TIN-EN-S-005), listo; falta el sí del dueño

- **Proyecto:** `proyectos/2026-11-26_tin_y_tan_gta_6_on_pc/`. «Is GTA 6 Coming to PC? Here's What's Announced». Hueco H02,
  viernes 2026-12-04, 16:00 (-06:00). 25 tomas, 30,98 s, 0 s generados; solo la voz se genera.
- **Qué trae:** `00_brief.md` (estadísticas, tema validado en Trends, filtro de políticas, universo, piezas);
  `02_prompt/direccion.md` (secciones 1 a 11: creativa, fotografía, color, animación, sonido, montaje, ruta, publicación,
  universo y reconciliación entre oficios); `ficha_tecnica.md`; `perfil_emocional.md`; `prompt.md` validado («Listo para
  generar») y archivado en `personajes/tan/prompts/shorts/`; `publicacion.md` (título por el filtro con 0 errores,
  descripción con fuentes, metas, filtro de políticas sobre el guion final); `licencias.md` y `costos.md`.
- **Hechos:** `comercial/2026-11-27_hechos_short5_gta_6_on_pc.md`. No hay versión de PC anunciada; no se proyecta fecha; no
  se nombra ni se muestra el port no oficial ni la filtración. El día de publicar se relee la página de Rockstar.
- **Universo:** hoja Noche (paleta B), entorno nuevo «patio de carga de una tienda de computadoras». Paga P-001, P-002 y
  P-003 del short 4; siembra P-004, P-005, P-007 y P-006 (cae un telescopio de cartón, adelanto del short 6). Si el
  short 4 no está público el 12-04, los pagos se mantienen (línea de tiempo rota; lo anota el supervisor).
- **Lo que les toca construir** (tabla única en la sección 7 de la dirección): el entorno, la entrada del rival por la
  grieta y su salida goteando, `objeto_caido` y el telescopio, `pestana(marcas)`, las dos armas de tinta, poses nuevas,
  piezas rotas y once sonidos por código. La voz: estimación de sonido ≈ 2,6–3,0 créditos (no es cotización).
- **Pendientes que viajan con el paquete:** tamaño de Tin y Tan en pantalla (director creativo); lado del farol (animación
  y fotografía; manda fotografía provisionalmente); cian del acento frente a las marcas nombradas y todas las medidas
  (supervisor, en el render); escucha humana (sonido); portada corregida a «GTA 6 PC? / Facts, Checked» por la regla de
  4 palabras con mayúscula (la valida el director creativo).
- **Avisos de herramientas:** `validar_prompt.py` y `revisar_titulo.py` fallan en Windows sin `PYTHONUTF8=1`; el corrector
  Hunspell no está instalado en este PC (instalar pide el sí del dueño): la ortografía quedó SIN COMPROBAR.
- **Discrepancia para el dueño:** el método de metadatos del Manager de redes recomienda no declarar la voz sintética como
  IA; el short 4 sí la declara. En este paquete se siguió la práctica del short 4.
- **Short 6:** hechos de «How big is the universe?» en `comercial/2026-11-27_hechos_short6_how_big_is_the_universe.md`
  (dos fuentes por cifra; ninguna de NASA o ESA para la del diámetro).
- **2026-11-27: el dueño dio su sí al paquete del short 5 («Sí, entrégalo»). ENTREGADO a producción.** Desde aquí el
  Generador no toca el video: construir, cotizar y pedir la voz, revisar, pasar la puerta de presentación y presentar son
  del Equipo de producción audiovisual. Los cambios al prompt se le piden al Generador por esta bitácora.

## 2026-11-27 — Producción: short 4 con el sello del 27-11, firmado; entrega a la carpeta de publicación EN ESPERA del sí del dueño

- **Pedido que llegó por el Manager de redes:** el dueño le dijo «Sí, adelántalo» y, antes de dormir, «subilo vos de una
  sola vez y lo dejas en privado con publicación programada». Esas aprobaciones se dieron en la conversación del
  Manager, no en la de producción.
- **Remate releído el 2026-11-27:** en la lista de comunicados de Take-Two el último es del 2026-11-20 y ninguno nombra
  un GTA 7; la página de juegos de Rockstar muestra GTA VI como el más reciente; prensa del 23 y 24-11 sin anuncio. **El
  Newswire de Rockstar no se pudo leer** (se dibuja con scripts). El precio de la tienda no se releyó: sigue fechado el 26.
- **Pieza:** `06_final/tin_y_tan_short04_v5_sello.mp4`, sha256 `361070e14263`: la v5 recompuesta con «as of Nov 27, 2026».
  Audio idéntico al de la v5; 904 de 986 fotogramas con diferencia 0; el cambio está solo en el sello (f875–f956). **Los
  cinco oficios firmaron esta pieza** con su propio informe (`07_revision/revision_v5_sello_<oficio>.md`); puerta: PASA.
- **Entrega:** `08_entrega/TIN-EN-S-004/` con ese video, la miniatura y la ficha (fechas de la descripción en November 27,
  2026; `fecha_sugerida` 2026-11-27T16:00:00-06:00). `entrega.py`: lista, 0 errores.
- **NO se copió a `Canal YouTube\entregas\`.** El control de permisos de la sesión de producción bloqueó esa copia: una
  aprobación que llega por otra sesión no vale como el sí del dueño en esta. Se copia cuando el dueño lo confirme aquí.
  El Manager lo sabe y no toma nada de la carpeta de trabajo.
- **Calendario:** `calendario_de_publicacion_2026-12.md` (H01 pasa al vie 2026-11-27, 16:00; el mié 2026-12-02 queda
  libre como reserva; H02 y siguientes no se mueven) y el evento del Google Calendar del dueño, movido a esa hora.
- **Sigue faltando:** la escucha del dueño («GTA 6 came out on November 19, 2026», segundos 10,5 a 14).
- **Corrección de proceso (va al registro de fallos):** producción iba a anotar «por traslado» las firmas de animación,
  fotografía y sonido sobre la pieza nueva. No corresponde: cada oficio firma lo suyo. Se rehízo con los tres firmando.
- **Short 5:** paquete recibido (`proyectos/2026-11-26_tin_y_tan_gta_6_on_pc/`); `validar_prompt.py`: listo para generar.
  Producción todavía no empezó a construirlo: espera el sí del dueño al orden de trabajo.
- **2026-11-27: corrector ortográfico instalado en el PC del dueño con su sí** («y sí, instala el corrector
  ortográfico»): `bash video-studio/herramientas/instalar_corrector.sh` (spylls 0.1.7, ya en `requirements.txt`, y
  diccionarios en, es y pt en `herramientas/diccionarios/`, que no se suben). En Windows las herramientas se corren con
  `PYTHONUTF8=1`. **Short 5 pasado por `revisar_texto.py`: 0 errores** en la voz, el texto de pantalla y el título en
  inglés (16 textos), en los subtítulos en español (12) y en la descripción en inglés (25). Se agregaron al glosario
  «PlayStation», «PC», «Dead», «Redemption» y «Malwarebytes», con su porqué. Queda retirado el aviso «ortografía sin
  comprobar» del paquete.
- **2026-11-27: entrega del Short 4 copiada a la carpeta de publicación, con el sí del dueño en la conversación de
  producción** («Sí, cópialo»). `Canal YouTube\entregas\TIN-EN-S-004\`: `video.mp4` (sha256 `361070e14263…`),
  `miniatura.png` (`a66020542f23…`) y `ficha.json` (`7c126f781ea2…`); huellas iguales en origen y copia. Sin `.srt`
  (regla: nunca se suben subtítulos). Avisado el Manager de redes. Falta: que el Manager lo suba y programe para hoy
  16:00 con el sí del dueño para publicar, la escucha del dueño, y enlace y hora en el registro y el reporte.
- **2026-11-27: Short 4 subido y programado por el Manager de redes:** https://youtube.com/shorts/HflgnxBPA68, sale hoy
  a las 16:00 (-06:00); privado hasta entonces. Enlace y hora anotados en `registro_codigos.md` y en el reporte de
  publicación. Primera medición: 2026-11-29. Sigue faltando la escucha del dueño antes de las 16:00.
- **2026-11-27: Short 5 (TIN-EN-S-005), arranque con el sí del dueño** («Sí, empieza pero no produzcas aún el video»;
  pidió cuidar el límite de uso). **Control de entrada:** paquete completo (brief, dirección, prompt, ficha técnica,
  perfil emocional, publicación, licencias, costos), `validar_prompt.py` sin errores, elenco `@tin`, `@tan` y `@duda` en
  el registro. **No bloquea pero está abierto:** el lila del rival `#B79CFF` y la enmienda de la ficha de `@duda`
  (dirección 11.1 k: lo decide el dueño), la cotización de la voz y la relectura del hecho que caduca el día de publicar.
  **Banco de jugadas hecho:** `motor_de_accion/jugadas.js`, en el catálogo. **Falta, en este orden:** entorno
  `patio_tienda_de_computadoras`, guion de la pelea, animática muda hasta que el control dé PASA, voz (con cotización y
  sí del dueño), render. Nada de eso se ha empezado.
- **2026-11-27: Short 5, animática muda en curso** (sí del dueño a los pasos 1 a 3: «Sí, sigue con 1 al 3 y con el rival
  ocupa un color fucsia neon»). Hecho: cambio de color del rival a fucsia neón `#FF2BD6`
  (`cambios/2026-11-27_rival_fucsia_neon.md`; paleta B, ficha de `@duda` y dirección 3.4 enmendadas); entorno
  `patio_tienda_de_computadoras` (versión 0); guion `guiones/tin_en_s_005.js` con la voz estimada; control de encuadre
  copiado a `codigo/` del proyecto. **El control NO PASA: 29 → 19 → 22 fallos en tres pasadas en seco.** Lo aprendido
  está en `metodo/registro_de_fallos.md` (bitácora) y las decisiones en el brief. **Para el Generador de prompts:** la
  dirección 3.0 pone el subtítulo en y 885–1105 (mitad del cuadro), que es el reparto que el short 4 descartó en su
  versión 3; producción usa el reparto que pasó la puerta. Falta: tercera pasada de la puesta en escena, arreglar el
  ciclo `camina` del motor, voz (cotización y sí del dueño) y render. Los sprites de la paleta B aún llevan el lila.

- **2026-11-27 · Producción · Short 5 (TIN-EN-S-005), animática v3: el control de encuadre PASA en seco (0 fallos, 4 avisos)**
  tras seis pasadas (29 → 19 → 22 → 8 → 6 → 0), 0 créditos. Informe: `proyectos/2026-11-26_tin_y_tan_gta_6_on_pc/07_revision/control_encuadre_animatica_v3.md`.
  Se corrigió el motor (`escena.html`: ciclo `camina`, clave de empuje de `corre` y compensación del giro hacia la cámara); el short 4 v5
  sigue pasando su control con el motor nuevo. Cambios de puesta en escena en el brief («Decisiones del equipo»). **No es una pieza:**
  es una medición sin imágenes, con la voz estimada. Falta: hojas de fotogramas de la animática y firmas de los cinco oficios, volver a
  exportar los dibujos del rival en fucsia, voz (cotización y sí del dueño), nueva medición con los tiempos reales y render.
