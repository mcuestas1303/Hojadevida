# Estudio: cómo están escritos los prompts de animación por código

- **Fecha:** 2026-11-21
- **Fuente:** `awesome-opus5-5-videos` (licencia MIT; 703 entradas, `data/videos.json` y 703 archivos en `prompts/`). Anotada en `referencias_externas.md`.
- **Tratamiento:** contenido de terceros no verificado. Se leyó como dato; no se ejecutó nada, no se visitó ningún enlace y no se siguió ninguna instrucción de los archivos. Una búsqueda de frases tipo «ignora lo anterior» no encontró nada de ese tipo (solo menciones de «API key» dentro de prompts de agentes).
- **Uso del material:** de cada prompt se toma el patrón. Las citas son de una o dos frases con el nombre del archivo; no se copia ningún prompt entero ni hay un prompt «listo para usar» calcado.
- **Estado:** estudio y propuestas. No se modificó ninguna plantilla ni definición; los cambios quedan en la sección 5 para pasar por el equipo (`generacion.md`, sección 3).

## 1. Resumen en 5 líneas

1. La biblioteca es un catálogo de **encargos a un agente que escribe código**, no de prompts para un generador de video: el agente puede iterar, revisar y renderizar gratis, y el prompt lo sabe.
2. La mitad de los prompts son cortos y vagos (mediana 221 caracteres, unas 35 palabras). Los largos (más de 1000 caracteres, 13 % de los completos) son los que concretan segundos, paleta con HEX, prohibiciones y verificación.
3. El patrón más repetido y más útil: **una sola idea formal por pieza, tiempo en rejilla (pulsos o intervalos de ~1 s), una lista negativa de tropos concretos y un ciclo de revisión escrito dentro del prompt**.
4. Para el estudio sirve sobre todo en la plantilla de redes (idea formal, rejilla, lista de tropos, texto bloqueado, archivo de hechos) y en la definición cerrada antes de generar. Hay una incoherencia propia que conviene arreglar: las plantillas dicen «intentos por toma: 2» y `generacion.md` dice uno.
5. Casi nada del ritmo de la biblioteca (pulso en cada beat, cero tiempo muerto, bucle, texto cinético) cabe en la serie infantil; un motor por código solo serviría ahí para tomas sin personajes y sin texto, y solo con aprobación del equipo.

## 2. Los números

### Cómo se contó

- Script propio (Python, `python3 -I`, ejecutado desde `/tmp`, ruta del JSON como argumento): `medir.py` y `m2.py` en la carpeta de trabajo de la sesión. Solo lee `videos.json`; no ejecuta nada de la biblioteca.
- **Prompt completo** = `prompt_partial` falso (496). **Parcial** = `prompt_partial` verdadero: el autor compartió solo una parte, y así lo marca cada archivo («The author shared only part of the prompt»).
- Las longitudes y las menciones se calcularon **solo sobre los 496 completos**, salvo que se diga otra cosa. Las menciones son búsquedas de palabras clave sin distinguir mayúsculas, en inglés: **cuentan presencia, no calidad**, y pueden sobrecontar («text» o «loop» en otro sentido) o subcontar (los prompts en chino, japonés y coreano, 67 entradas = 13,5 % de los completos, casi no coinciden con las palabras en inglés).
- Las etiquetas (`tech_tags`) las puso la biblioteca al hacer sus **remakes** en Skillry; describen el remake, no necesariamente lo que pidió el autor.

### Completos, parciales y duplicados

| Dato | Número |
|---|---|
| Entradas | 703 |
| Prompt completo | 496 (70,5 %) |
| Prompt parcial | 207 (29,4 %): fragmento del autor, de unas pocas palabras a un par de párrafos (mediana 222 caracteres) |
| Entradas sin texto (solo enlace) | 0 en el JSON. El README dice que sin prompt se enlaza el post, pero todas traen algún texto; una completa mide 11 caracteres |
| Entradas con remake | 418 (las 285 sin remake traen título y ninguna etiqueta de tecnología) |
| Prompts completos distintos | 476 de 496. Hay 12 grupos repetidos (32 entradas); una familia de plantilla («Ask me for: 8 to 12 UI states…») aparece 25 veces en 18 variantes. Repetir un prompt no lo hace 25 veces distinto |
| Autores distintos | 616 |
| Altas | 375 en 2026-09 y 328 en 2026-10 |
| Idioma | unas 67 entradas completas con chino/japonés/coreano (13,5 %); el resto, casi todo inglés |

### Longitud de los 496 completos

| Medida | Caracteres | Palabras |
|---|---|---|
| Mínimo / máximo | 11 / 12 497 | 1 / 1 787 |
| Percentil 10 | 80 | 9 |
| Percentil 25 | 127 | 18 |
| **Mediana** | **221** | **35** |
| Media | 658 | 104 |
| Percentil 75 | 473 | 73 |
| Percentil 90 | 1 624 | 230 |
| Percentil 99 | 8 142 | 1 389 |

Sin repetidos la mediana es 218,5. Por tramos: menos de 100 caracteres, 87 (17,5 %); 100 a 250, 187 (37,7 %); 250 a 500, 105 (21,2 %); 500 a 1000, 51 (10,3 %); 1000 a 2500, 27 (5,4 %); más de 2500, 39 (7,9 %). Medianas por categoría: motion 200, explainer 226, 3d 258, interactive 267.

### Categorías (las pone la biblioteca)

motion 369 (52,5 %), 3d 117, explainer 116, interactive 101.

### Tecnologías

| Medida | Resultado |
|---|---|
| Etiquetas de los remakes (de 703; 418 llevan alguna, 285 ninguna) | canvas 267, svg 183, threejs 131, shader 92, gsap 86, css 57, audio 39, playable 22, particles 17, pixel 15, webgl 9, physics 9, ai-image 6 |
| Tecnología nombrada en el texto del prompt (completos) | 195 de 496 (39 %) nombran alguna; **61 % deja la elección al agente** |
| Detalle en el texto | Three.js 57, Canvas 47, CSS 37 (casi siempre «no CSS transitions»), SVG 15, WebGL 15, Remotion 15, Blender 10, GSAP 8, Web Audio 8, shaders/GLSL 8, HyperFrames 4 |
| «Un solo HTML autocontenido / index.html» | 70 (14 %) |
| Render determinista «cada fotograma es función del tiempo» / fotograma a fotograma | 63 (13 %); Playwright o Puppeteer 33 (7 %) |

### Duración y formato

- **Duración en segundos explícita:** 184 de 496 (37 %). Más frecuentes: 15 s (52), 30 s (36), 20 s (17), 60 s (12), 10 s (11). Hasta 20 s: 106; de 21 a 60 s: 70; más de 60 s: 8.
- **Relación de aspecto o resolución** (16:9, 9:16, 1920x1080, 1080p, 4K): 44 (9 %). `16:9` literal 16 veces, `9:16` literal 8, `1:1` 1.
- **fps:** 60 fps en 56 (11 %), 30 fps en 10, 24 fps en 3.
- **Rangos de tiempo escritos («0.0–0.6 seconds»):** solo 10 (2 %). Es raro y está en los prompts largos.

### Menciones (496 completos)

| Elemento | Prompts | % |
|---|---|---|
| Sonido (sound, audio, music, sfx, voz) | 124 | 25 % |
| Música | 67 | 14 % |
| Voz en off / TTS / narración | 31 | 6 % |
| Beat o BPM | 60 | 12 % |
| Texto en pantalla (palabra «text», caption, subtitle, label, tipografía; criterio amplio) | 75 | 15 % |
| Tipografía o fuente concreta | 45 | 9 % |
| Paleta o color con nombre; HEX | 30; 14 | 6 %; 3 % |
| Física (physics, gravity, collision, bounce, spring, particle) | 57 | 11 % |
| Cámara (camera, zoom, pan, orbit, dolly) | 73 | 15 % |
| Bucle (loop, seamless) | 44 | 9 % |
| Restricciones (no X, must, never, do not, don't, avoid, without) | 126 | 25 % |
| De ellas, fuertes (must, never, do not, don't) | 71 | 14 % |
| Lista «Banned / forbidden / prohibited / avoid» | 35 | 7 % |
| Referencias de estilo (inspired by, style of, similar to…) | 80 | 16 % |
| Revisión propia (criterio amplio: verify, inspect, screenshot, test…) | 50 | 10 % |
| Revisión propia (criterio estricto: inspect, contact sheet, verify, critic, review) | 30 | 6 % |
| Hoja de contacto o extracción de fotogramas | 6 | 1 % |
| Estructura con encabezados, listas o etiquetas XML | 59; 34 (XML) | 12 %; 7 % |
| «Go all out» o equivalente | 46 | 9 % |
| «No me hagas preguntas / decide tú» | 9 | 2 % |

### Qué cambia con la longitud

Porcentaje de prompts que mencionan cada cosa, según su longitud (criterio amplio):

| Elemento | Menos de 250 car. (274) | 250 a 1000 (156) | 1000 o más (66) |
|---|---|---|---|
| Duración en segundos | 32 % | 32 % | 70 % |
| Sonido | 14 % | 29 % | 67 % |
| Restricciones | 7 % | 28 % | 82 % |
| Paleta o color | 1 % | 11 % | 65 % |
| Verificación o revisión | 1 % | 10 % | 52 % |
| Cámara | 4 % | 16 % | 64 % |

Lectura: la duración está tan presente en un prompt corto como en uno medio; lo que **solo** aparece al detallar son las restricciones, la paleta, la revisión y la cámara.

## 3. Patrones de escritura

Se leyeron 64 prompts completos con atención (los 8 más largos, unos 25 de longitud media repartidos entre las cuatro categorías y 12 cortos de menos de 130 caracteres) más fragmentos dirigidos a rasgos concretos. Los nombres de archivo son los de `prompts/`, sin la extensión.

### 3.1 Cómo abren

- **Verbo + entregable + duración + estilo, en una frase.** «Make a dynamic 15-second motion graphics video that shows off everything you can do as a motion designer» (`aichrislee-961335`). Es la apertura más común en los cortos.
- **Reto abierto sin forma** («show me what an incredible motion designer you are», `zheke-622583`; «Go ALL OUT» en `robvjourney-237474`). Son pruebas de capacidad del modelo; el prompt casi no define la pieza.
- **Entregable y reglas técnicas desde la primera línea:** «Create a single self-contained index.html: a ~2-minute animated piano performance…» (`0xcodez-474136`), con lugar, música, sincronía y reglas en líneas cortas con etiqueta.
- **Bloques con etiqueta** (`<inputs>`, `<direction>`, `<structure>`, `<build>`, `<gotchas>`, `<start>`, o `<deliverables>`, `<art_direction>`, `<timeline>`), propios de los prompts largos y de las plantillas parametrizadas (`twoclipping-402193`, `brainextends-606193`).
- **Rol primero** (`<role>` en `everestchris6-399895`) o **encargo con placeholders entre corchetes** (`humzaakhalid-011081`), para reutilizarlo con cualquier marca.
- Algunas «entradas» no son prompts sino el texto del post que lo presenta (`cagrimbakirci-842869`, `deedydas-407965`, `jamee-now-583635`). Hay que descartarlas al estudiar el estilo.

### 3.2 Orden de las secciones en los prompts largos

El orden es casi siempre el mismo y es el que vale la pena imitar:

1. Entradas que debe pedir o decidir (`<inputs>`), o el tema en una línea.
2. **Dirección**: idea formal, estilo, paleta, tipografía, cámara, lista de prohibidos.
3. **Estructura temporal**: rejilla de pulsos o línea de tiempo por intervalos.
4. **Elementos con ficha** (mascota, portada, panel fijo que reaparece), con medidas.
5. **Cómo construirlo**: formato de archivo, motor, fps, cómo se mide la música.
6. **Trampas conocidas** (`<gotchas>`).
7. **Arranque**: «pídeme las entradas y enséñame la lista de estados sobre la rejilla antes de escribir código».

### 3.3 Cómo especifican el tiempo

- **Rejilla musical:** «120 BPM, 7 bars, something happens on every beat» y la cuenta explícita 28 pulsos = 14 s (`twoclipping-402193`, `yankis0x-174321`). `heyiamnick-119558` añade que cada movimiento «empieza 0,05 s antes de su pulso para aterrizar en él» y divide 30 s en 15 compases de 2 s con nombre cada uno.
- **Intervalos de ~1 s con una acción cada uno:** `brainextends-606193` escribe 18 tramos («0.0–0.6 seconds», «0.6–1.5 seconds»…), cada uno con qué entra, qué se ve y cómo se mueve.
- **Cuenta de planos en el guion:** `okazaky-084783` usa «una línea de letra = una escena» y `nft-chen-068069` fija «cada tramo dura ~1,6 s con corte seco».
- Los cortos dan solo la duración total y dejan el ritmo al agente.

### 3.4 Cómo especifican movimiento y cámara

- **Mecánica en vez de adjetivos:** resortes críticamente amortiguados con una fórmula y un rango de parámetros (`heyiamnick-119558`); «un resorte por cada cambio de objetivo» para que el movimiento siga siendo función del tiempo (`twoclipping-402193`).
- **Regla de entrada y salida:** el contenido entra después de que su contenedor empieza a transformarse y sale antes de la siguiente transformación, para que el texto no se solape (`verbove-268381`).
- **Truco de detalle:** los dos bordes de un indicador estiran con resortes distintos; un solo gesto bien dicho vale más que un párrafo de «fluido y moderno».
- **Cámara en una frase:** «bloqueada y frontal, como una mesa de dibujo; los objetos giran, la cámara no» (`heyiamnick-119558`); «la cámara reencuadra cada estado para que la interfaz llene el cuadro» (`thegrootdev-966114`).
- **Física verdadera cuando importa:** «la caminata aleatoria debe ser una caminata aleatoria, no un dibujo de una» (`astrothewizard-618782`).

### 3.5 Cómo especifican estilo

- **Paleta con HEX y rol de cada color** (`heyiamnick-119558`, `gdgtify-393073`, `brainextends-606193`): «el acento de cada etapa es el color de base de la siguiente».
- **Una sola familia tipográfica** con pesos y tamaños (Geist 900 para palabras grandes, 600–800 para rótulos de 24–28 px).
- **Geometría con medidas relativas:** el «escenario» ocupa el 80 % del ancho y el 75 % del alto; nada en reposo a menos de 150 px de los lados (`brainextends-606193`, `heyiamnick-119558`).
- **Referencias por nombre de estilo:** «Dribbble-level», «3Blue1Brown», «Kurzgesagt», crayón, riso, plano, pixel art (`nft-chen-068069`, `rneayan-441493`). Nombrar el estilo ahorra párrafos; nombrar un autor vivo es otra cosa y aquí no se imita.
- **Una idea formal única por pieza:** «un lápiz que se asciende tres veces y nunca sale de la pantalla» (`heyiamnick-119558`); «una forma, nunca se corta» (`twoclipping-402193`); «un mecanismo que demuestra la prueba, no una decoración» (`gdgtify-393073`). Esta frase organiza todo lo demás.
- **El último fotograma igual al primero** como instrucción de bucle (`twoclipping-402193`, `thegrootdev-966114`), con la nota de que incluye la posición y velocidad del cursor.

### 3.6 Cómo especifican restricciones

- **Lista «Banned:» de tropos concretos**, no genérica: explosiones de partículas, resplandores, destellos de lente, sacudida de cámara, división RGB, fundidos cruzados, rebote exagerado, «cualquier cosa que parezca plantilla» (`heyiamnick-119558`, `twoclipping-000267`). Son los fallos típicos del modelo.
- **Texto bloqueado** («LOCKED COPY») con la frase exacta, más una **lógica prohibida** («no afirmes que multiplicar primos y sumar uno siempre da un primo») que protege la exactitud (`gdgtify-393073`).
- **Fuente única de hechos:** «archivo de hechos: la única fuente de cualquier número, nombre o afirmación en pantalla» (`everestchris6-399895`), y «datos reales, no marcadores» (`verbove-268381`).
- **Reglas de motor** como lista corta: sin CSS transitions, sin temporizadores, sin estado entre fotogramas; «Canvas 2D, sin librerías, sin recursos externos, con `?t=90` para saltar a un momento» (`0xcodez-474136`).
- **Márgenes y texto sin puntos finales** («No full stops in on-screen text», `twoclipping-000267`): una restricción pequeña y comprobable.

### 3.7 Revisión y verificación dentro del prompt

- «Renderiza una prueba de 5 segundos primero y confirma que funciona» (`everestchris6-399895`).
- «Renderiza un fotograma por pulso antes del render completo; corrige lo que se salga de la rejilla, esté apretado o difícil de leer» (`twoclipping-402193`).
- «Hoja de contacto de 16 fotogramas para verificación visual» (`okazaky-084783`); «revisa imágenes fijas de cada escena con ojo crítico, comprueba transiciones fotograma a fotograma, mide la mezcla de audio con números» (`astrothewizard-618782`).
- **Pasada numérica:** «cuánto cambia cada fotograma respecto del anterior, brillo y detalle de bordes» para encontrar tiempos muertos (`everestchris6-399895`). Es la misma idea que `revisar_fotogramas.py`.
- **Punto de control con la persona:** «pídeme las entradas y enséñame la lista de estados sobre la rejilla antes de escribir código» (`twoclipping-402193`).
- Contra-ejemplo: «No me hagas preguntas, decide tú» (9 prompts, p. ej. `aichrislee-961335`). Es útil para el agente que itera gratis, pero **choca** con la regla del estudio de preguntar lo que falte.

### 3.8 Qué diferencia un prompt detallado de uno vago

| | Vago (`zheke-622583`, `robvjourney-237474`) | Detallado (`brainextends-606193`, `gdgtify-393073`) |
|---|---|---|
| Qué se ve | «Impresióname» | Qué aparece en cada intervalo de ~1 s |
| Texto | Lo inventa el modelo | Copia exacta y tamaño relativo |
| Color y tipo | Libre | HEX con rol, una familia, medidas |
| Qué no | Nada | Lista de tropos prohibidos y afirmaciones prohibidas |
| Final | Libre | Último plano definido; bucle o fundido |
| Cómo se comprueba | «Dame el MP4» | Prueba corta, un fotograma por pulso, hoja de contacto |
| Quién decide | El modelo | La persona |

Lo vago funciona cuando lo que se mide es **el modelo** («mira lo que hace»), y los resultados vistos como virales dependen de eso. Para una pieza de marca que debe repetirse, el encargo detallado es lo que la hace reproducible. Un tercer tipo útil es el **corto parametrizable**: `nft-chen-068069` repite una fórmula (duración + nombre de estilo + tema entre corchetes + tres o cuatro hitos visuales + una línea de texto) para una docena de piezas distintas.

### 3.9 Los 8 patrones más útiles para el estudio

1. **Idea formal única** en una frase que gobierna la pieza.
2. **Rejilla de tiempo** (pulsos o intervalos de ~1 s), con una acción por intervalo y las salidas antes de las entradas.
3. **Dirección con números**: HEX con rol, una familia tipográfica, márgenes en px o %, proporciones del escenario.
4. **Lista negativa de tropos concretos** del propio generador, no frases genéricas.
5. **Texto bloqueado y afirmaciones prohibidas** más un archivo de hechos como única fuente de cifras.
6. **Movimiento descrito como mecánica** (qué parte se mueve, con qué curva, en qué orden de entrada y salida), no con adjetivos.
7. **Ciclo de revisión escrito en el prompt**: prueba corta, un fotograma por pulso, hoja de contacto, pasada numérica.
8. **Punto de control antes de producir**: la lista de estados o tomas sobre la rejilla se enseña a la persona antes de gastar nada.

## 4. Qué tiene ya el estudio (para no proponer lo que existe)

- `plantillas/prompt_video_redes.md` ya trae: restricciones críticas al inicio (sección 10), gancho y mapa de ritmo en décimas de segundo (11), tipografías, paleta con HEX, «Prohibido» y tabla de texto con posición y tamaño (12), golpes de sonido atados a cortes (13), motor y revisión con `revisar_fotogramas.py` (14), y límite de 3 destellos por segundo.
- `generacion.md` ya trae: un intento por pieza, definición cerrada (personaje, lugar, `definicion.md` con autorización y costo), cambios por solicitud, registro de costos.
- `referencias_externas.md` pide estudiar esta biblioteca «cuando el dueño decida el motor».
- Falta, según el estudio: idea formal única, rejilla musical, lista de tropos propia por generador, texto bloqueado con afirmaciones prohibidas, archivo de hechos, prueba corta previa, y qué cambia cuando el motor es por código (iterar es gratis).

**Incoherencia detectada (no es de la biblioteca):** ambas plantillas (`prompt_video.md` y `prompt_video_redes.md`) dicen «Intentos estimados por toma: 2» y el presupuesto multiplica «tomas × intentos», mientras `generacion.md` fija un solo intento. El presupuesto debería partir de 1.

## 5. Qué aplicar en el estudio

Todos son **propuestas** que pasan por el equipo (solicitud en `cambios/`); ninguna se aplicó.

| Patrón | Dónde encaja | Cambio concreto propuesto |
|---|---|---|
| Idea formal única | Plantilla de redes, sección 3 | Añadir la etiqueta **Regla formal de la pieza:** (una frase; p. ej. «todo se transforma en lo siguiente, sin cortes»). El validador solo comprobaría que no esté vacía |
| Rejilla de tiempo | Plantilla de redes, sección 11 | Añadir a la tabla de ritmo una columna **Pulso / intervalo** y una línea **Rejilla:** [BPM y compases, o «intervalos de ~1 s»]. Regla: cada intervalo dice qué entra, qué sale y qué se mueve; lo que sale se va antes de que entre lo siguiente |
| Lista negativa de tropos propios | Plantilla de redes, sección 12, «Prohibido» | Pasar de frase genérica a **lista de 5 a 10 tropos concretos** del generador usado (resplandores, partículas, rebote exagerado, división RGB, «cualquier cosa que parezca plantilla»). Anotarla además en «Fallos conocidos» de la ficha del personaje o del lugar cuando el fallo venga de una generación real |
| Texto bloqueado + afirmaciones prohibidas | Plantilla de redes, sección 12 | Añadir **Texto exacto:** (copia literal, sin traducir) y **No afirmar:** (lo que la pieza no puede decir, p. ej. promesas de resultado). Encaja con «toda cifra lleva fuente y fecha» |
| Archivo de hechos | Plantilla de redes, sección 10 | Añadir a las restricciones críticas: «CRITICAL: toda cifra, nombre o afirmación en pantalla sale de `datos/hechos.md` del proyecto, con fuente y fecha». Crear ese archivo en `nuevo_proyecto.py --redes` |
| Márgenes y proporciones numéricas | Plantilla de redes, sección 12 | Añadir **Márgenes seguros** (en % o px) y **Escenario** (proporción de la pieza que ocupa el contenido), además de la zona segura de `formatos.md` para 9:16 |
| Movimiento descrito como mecánica | Plantilla de redes, tabla de tomas | En **Acción**, pedir «qué parte se mueve, curva (lineal prohibida), orden de entrada y salida». Para el motor por código, añadir la fórmula de la curva |
| Ciclo de revisión escrito | Plantilla de redes, sección 14 | Escribir el ciclo: prueba corta de 5 s, un fotograma por pulso, hoja de contacto, pasada numérica de cambio entre fotogramas (la herramienta ya existe). Documentar que en motor por código las vueltas son gratis, pero se cuentan en `costos.md` si usan APIs de pago |
| Punto de control antes de producir | `generacion.md`, sección 2 | Añadir: «antes de renderizar, se enseña al dueño la lista de tomas sobre la rejilla». Es lo que ya hace `definicion.md`; se hace explícito para piezas por código |
| Definición cerrada de una pieza por código | `generacion.md`, sección 2 y `03_keyframes/definicion.md` | Añadir una fila **Pieza por código** con: archivo de hechos, paleta con HEX, tipografía y licencia, texto exacto, duración y fps, rejilla, lista de prohibidos, motor y versión, costo de APIs externas (voz, música, imágenes), autorización |
| Un solo intento, también en código | `generacion.md`, sección 1 | Aclarar: el límite de un intento es para lo que **cuesta créditos** (generador de video, imagen, voz o música de pago). Las iteraciones de código local no cuestan créditos, pero el render final con servicios de pago sí se autoriza pieza por pieza |
| Autonomía («decide tú», «no me preguntes») | No aplicar | Va en contra de «lo que falte se pregunta, no se supone». Solo valdría para elegir detalles de composición dentro de una definición ya cerrada |
| Presupuesto con intentos | Ambas plantillas, sección 1 y 9 | Cambiar «Intentos estimados por toma: 2» por 1 (generador) o «0 créditos» (código local); es una incoherencia con `generacion.md` |
| Plantilla parametrizable con corchetes | `nuevo_proyecto.py` | Opción de proyecto «corto por código» con campos de marca, duración, estilo, tema, tres hitos y una línea de texto; es la fórmula de los cortos de `nft-chen-068069`, escrita con material propio |
| Validador | `herramientas/validar_prompt.py` | Reconocer los campos nuevos de la plantilla de redes y comprobar que la rejilla suma la duración total |

## 6. Qué no aplica a la serie infantil, y por qué

Referencia: `infantil/guia_1_a_3.md`, sección 7 (planos de 6 s o más, cámara fija o lenta, un foco, sin texto, sin efectos, sin destellos), y los vetos de la psicóloga.

| Patrón de la biblioteca | Por qué no entra |
|---|---|
| Algo pasa en cada pulso, «sin tiempo muerto», sin sostener más de medio segundo | Contradice planos de 6 s o más y un solo foco |
| Cortes y morfismos continuos a 120 BPM, fundidos de color, latigazos de cámara | La guía pide corte directo o fundido lento; sin barridos ni zooms bruscos |
| Texto cinético, subtítulos, rótulos, texto bloqueado en pantalla | Ningún texto en pantalla: el público no lee, y el mismo video sirve para tres idiomas |
| Bucle (último fotograma igual al primero) | Veto de la psicóloga a lo que se repite sin fin; la despedida debe cerrar |
| Gancho en el primer segundo, «go all out», saturar | «Sin ganchos para seguir mirando» |
| Destellos, desenfoque de movimiento, división RGB, partículas | Sin efectos; luz pareja, sin parpadeos |
| Música marcada al beat y golpes de sonido por corte | Música suave solo en saludo y cierre; sin golpes ni sustos |
| Voz en off con subtítulos incrustados | La voz es otra pista por idioma; no se pide hablar al generador |
| Autonomía total («no preguntes, decide tú») | El estudio pregunta lo que falta |
| Cursor, interfaz que se transforma, cartas de producto | Es lenguaje de adultos y de aplicaciones |
| Llamado a la acción | «Hecho para niños»: no se pide suscribir ni comentar |

**Lo que sí podría pasar, previa revisión de pedagoga y psicóloga:** la lista negativa de tropos concretos (ya existe en espíritu en la guía), el texto fijo en forma de **frases fijas** de la voz, el archivo de hechos para lo que se le diga al adulto en `publicacion.md`, la prueba corta y la hoja de contacto, y el punto de control antes de gastar créditos. Nada de lo que cambia lo que ve el niño se toca sin el equipo.

## 7. Qué dice esto de un motor de gráficos por código

### Qué sale bien así (según lo que pide la gente en la biblioteca)

- **Títulos, cortinillas, intros de logotipo y rótulos animados:** el texto exacto y la tipografía son controlables al píxel.
- **Explicaciones con datos y mecanismos:** una prueba matemática, un recorrido «del teléfono al transistor», un explicador de una base de datos (`deedydas-407965`), gráficos que se dibujan, escalas de comparación, diagramas explotados.
- **Piezas de producto y de marca para adultos:** transformaciones de interfaz, promos, reels. Aquí encaja el reel de adultos de Instagram del que partió la solicitud de cambio.
- **Estilos con textura controlable:** papel, crayón, plano, blueprint, pixel art, riso.
- **Bucles geométricos y visualizaciones:** movimiento definido por fórmulas que se repiten exactamente.
- **Sincronía exacta:** al calcular todo desde una sola línea de tiempo, el sonido sigue al movimiento (rejilla de pulsos, `0xcodez-474136`, «one timeline drives both»).

### Qué no sale bien (o no hay evidencia de que salga)

- **Personajes con identidad estable como Tiky y Lumi** si lo que se busca es la fidelidad de su ficha y la actuación natural: en la biblioteca los personajes son siluetas, cajas, pixel art o dibujos de crayón muy esquemáticos, no personajes con ficha de proporciones.
- **Fotorrealismo, rostros, ropa, pelo, agua o animales actuando**: las piezas que lo intentan combinan imágenes generadas con modelos de pago, mezcla 2.5D y mucho trabajo propio (`zhu185178-255661`), y eso ya no es «gratis».
- **Voz natural y música original:** casi siempre se apoyan en TTS, bibliotecas de sonidos o síntesis; es un costo y una licencia aparte.
- **Aprender de lo que funciona sin ver el resultado:** no hay forma de saber en este estudio si el MP4 final cumplió lo que el prompt pedía.

### Condiciones si se aprueba (decisión del dueño, ver `cambios/2026-11-20_videos_instagram.md`)

- Es un motor para **adultos y redes** primero; en la serie infantil solo tomas sin personajes, sin texto y con planos largos, y siempre con aprobación de pedagoga y psicóloga.
- La unidad de trabajo es **una plantilla de proyecto «por código»** con los campos de la sección 5, no un prompt suelto.
- Hay que decidir y escribir qué costos entran: render local (tiempo de cómputo, por ejemplo 3 360 renders de navegador para 14 s a 60 fps con 4 subfotogramas, según `yankis0x-174321`), y servicios externos (voz, música, imágenes), que **sí** son créditos y siguen la regla de un intento.
- Instalar nada requiere el permiso del dueño; este estudio no instaló nada.

## 8. Límites del estudio

- **No se vieron los videos.** Todo se dedujo del texto de los prompts. Un prompt largo y claro no garantiza un resultado bueno, ni uno vago un resultado malo.
- **Popularidad no es calidad.** La colección reúne lo que se hizo viral y lo que los autores quisieron compartir; muchos prompts son retos de capacidad del modelo, no encargos reales.
- **No hay datos de resultados:** ni intentos, ni fallos, ni correcciones posteriores, ni cuántas veces tuvo que repetirse un encargo. Hay **sesgo de supervivencia**: solo se ven los que salieron bien.
- **Los prompts son para un agente que escribe código** (con herramientas, iteración y acceso a internet), no para un generador de video como el que usa el estudio; el paso de uno a otro no está probado.
- **Duplicados y no-prompts:** 20 prompts completos están repetidos (una familia de plantilla pesa 25 entradas) y algunas entradas son textos de post, no instrucciones.
- **207 prompts son parciales** y no sirven para medir estructura.
- **Las menciones son búsquedas de palabras** en inglés: sobrecuentan algunas (texto, bucle) y subcuentan los 67 prompts en chino y japonés. Los porcentajes son órdenes de magnitud, no cifras exactas.
- **Las etiquetas de tecnología vienen de los remakes de la biblioteca**, no del autor original.
- **Licencia:** la MIT cubre la recopilación, no los videos ni los prompts de cada creador. Aquí solo se aprovechan los patrones y no se republica nada.
