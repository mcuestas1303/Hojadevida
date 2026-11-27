# Ficha técnica — Is GTA 6 Coming to PC?

Resumen del video y rúbrica con la que se puntúa. El detalle está en `direccion.md` (guion por fotogramas, coreografía,
cámara, color, sonido, universo y reconciliación entre oficios) y en `perfil_emocional.md`. Escrita el 2026-11-27 por el
comercial sobre el brief cerrado el 2026-11-27 y la dirección de ese día. Los fotogramas son un plan con la voz estimada: se
recalculan con la voz real. **Los puntajes quedan vacíos: se llenan con el video hecho.**

- **Estado:** SIN EVALUAR (falta prompt validado, voz, render y revisión)

## 1. Objetivos comerciales

**Fijado por el dueño el 2026-11-23, para todos los canales.** Textual: «Entonces el objetivo inicial es entrar al programa de
socios; todo debe girar en torno a lograr el objetivo a la mayor brevedad posible».

| Qué | Valor (`canales/nostalgia-tin-y-tan/plan_programa_de_socios.md`, secciones 1, 3.4 y 3.5; páginas oficiales de YouTube leídas el 2026-11-23) |
|---|---|
| Objetivo | Entrar al Programa de socios de YouTube lo antes posible |
| Primer hito (métrica y meta) | Nivel intermedio: 500 suscriptores, 3 subidas públicas válidas en 90 días y 3 millones de vistas calificadas de Shorts en 90 días (o 3.000 horas en 12 meses). No cambia el 2027-02-01 |
| Segundo hito | Nivel alto: 1.000 suscriptores y 10 millones de vistas calificadas de Shorts en 90 días hasta el 2027-01-31; 20 millones desde el 2027-02-01 (o 4.000 u 8.000 horas) |
| Plazo | «A la mayor brevedad»; el plan dice que se planea contra los umbrales nuevos y que el 2027-01-31 es un caso afortunado; se solicita el mismo día en que Studio avise que se alcanzó un nivel. Revisión del plan: 2026-12-07 |
| Qué aporta este video | Vistas calificadas del feed de Shorts y los primeros suscriptores. No tiene una meta de vistas propia: el canal no tiene base (dos videos con datos, ningún suscriptor); se mide contra otro video |

**Nicho y potencial de pago** (`comercial/2026-11-27_potencial_de_pago_por_nicho.md`): videojuegos es **nivel BAJO**; este tema
(«Is GTA 6 coming to PC?») queda **BAJO, y MEDIO solo si el video habla de requisitos o piezas** (lado del hardware: PC, espacio
en disco). **Observación del comercial:** la dirección sacó de la voz los 212 GB de PS5 (decisión C9) y los dejó en la descripción;
en la voz el video no toca hardware, así que el video, tal como está, **no sube a nivel medio**. Es decisión del director creativo;
cambiarla puede costar tiempo en un guion ya apretado. En Shorts el nicho casi no cambia el ingreso (la página oficial no
menciona tema ni categoría en el reparto); el criterio pesa para el video largo y para el tipo de suscriptor que se junta.

**Puntuación del Motor** (`comercial/2026-11-27_puntuacion_de_nichos_tanda_01.md`, fila H02): demanda 3, pago 2, hechos «sin
comprobar» con techo 2, políticas 1, encaje 3; **73 hoy y 83 de techo en Short** (68 y 78 en video largo); veredicto: «se propone
hoy; se propone si se comprueban los hechos». Los hechos se comprobaron el 2026-11-27
(`comercial/2026-11-27_hechos_short5_gta_6_on_pc.md`) con primarias, salvo los puntos que ese archivo marca; la puntuación no se
volvió a calcular.

| Qué aporta este video (brief, «Estrategia») | Métrica de Studio | Meta | Plazo |
|---|---|---|---|
| Vistas calificadas del feed: la respuesta delante tiene que detener el dedo | «Se quedó a mirar» (visto frente a deslizado) | No más de 5 puntos por debajo del short 4 a la misma edad; si no está público, del short 2 | 48 a 72 horas |
| Que el feed lo reparta | Fila «Feed de Shorts» en Alcance | Presente | 48 a 72 horas |
| Que nada cueste la admisión | Columna «Avisos» | Ninguno | Al subir, 48 horas, 7 y 28 días |
| Que el objeto que cae no frene a quien mira | Retención en el segundo de la caída (≈ 19,2 s) | Sin escalón | 48 a 72 horas |
| Primeros suscriptores | Suscriptores por mil vistas | Establecer línea base (hoy: cero) | 7 y 28 días |

- **Lo confirma «a prueba»:** la fila «Feed de Shorts» presente, ningún aviso, «se quedó a mirar» no más de 5 puntos por debajo del
  video de comparación y sin escalón en ≈ 19,2 s. **Lo descarta:** un escalón en ese segundo, o cualquier aviso.
- **Límite:** un video no decide; este estrena a la vez el objeto que cae, la invitación a mitad del video, la respuesta delante y
  la hoja Noche. Las metas completas, con fechas y dónde se lee cada dato, están en `publicacion.md`, «Objetivos y metas medibles».

## 2. Identificación y formato

| Campo | Valor |
|---|---|
| Código | `TIN-EN-S-005` (previsto) |
| Canal | Tin & Tan, inglés, EE. UU.; subtítulos en español quemados en la imagen; **ninguna pista `.srt` se sube a YouTube** (dueño, 2026-11-26) |
| Tipo | Short n.º 5. Segundo video del formato de acción; primer pago del universo (hueco H02 de la tanda 01) |
| Título | Is GTA 6 Coming to PC? Here's What's Announced (46 caracteres; `revisar_titulo.py` 1.1: PASA, 0 errores y 0 avisos). El candidato del brief («…What's Official») da 1 error (M8, «official»). Reservas en `publicacion.md` |
| Aspecto y tamaño | 9:16, 1080×1920, 30 f/s |
| Duración | ≈ 31 s (plan: 930 fotogramas); tolerancia 29 a 32 s; pico en ≈ 23,3 a ≈ 24,4 s (75 a 79 %) |
| Cómo se hace | Modo C, por código, con el motor de acción (`video-studio/motor_de_accion/`). 0 créditos de imagen y de video. Solo la voz se genera |
| Portada | El fotograma 0: «GTA 6 PC?» / «Facts, Checked» (propuesta del director creativo; no cumple la regla de portada en dos puntos, ver `publicacion.md`), monitor apagado sobre torres al centro, Tan y Tin de perfil, el lápiz en el aire |
| Público | El que mide Studio: casi todo menor de 45, mayoría hombres, tramo de 13 a 17 el mayor en el short de juegos; EE. UU., Filipinas e India |
| Fecha | Calendario: viernes 2026-12-04, 16:00 (El Salvador); el interés por GTA 6 baja semana a semana |

## 3. Elenco

| Personaje | Papel | Voz | Lleva |
|---|---|---|---|
| `@tan` | Pregunta («Is GTA 6 coming to PC?», «How long last time?»), invita a suscribirse a mitad del video, da el consejo («Don't download them.»); atrapa y lanza el lápiz | Zelda, al 110 % | Lápiz en los planos de firma; la regla de tinta cuando se la pasan |
| `@tin` | Responde con los hechos (8 líneas); golpea con puño y con la regla de tinta; frena la mano de Tan en el bloqueo; sin lápiz en los planos de firma | Kevin, al 110 % | Regla de tinta que dibuja con el lápiz |
| `@duda` (el rival) | La pregunta hecha cuerpo: sale de una grieta del suelo, crece a vez y media, baja un escalón de tamaño por dato, dibuja un paquete liso de tinta que revienta, y no se borra del todo | Ninguna | Paquete de tinta (no es un arma). Sin nombre en pantalla |

Ninguna persona real aparece, se nombra ni se cita. Marcas solo nombradas: GTA, Rockstar, Take-Two, PlayStation, Xbox, Red Dead
Redemption, Malwarebytes y Huntress (texto en la capa de datos, nunca objetos del mundo).

## 4. Contenido: frases, estado y fuente

Las doce líneas de voz de `direccion.md`, sección 2.2, sin cambiar ninguna palabra. Detalle y citas:
`comercial/2026-11-27_hechos_short5_gta_6_on_pc.md`.

| # | Quién | Frase (inglés) | Estado | Golpe |
|---|---|---|---|---|
| 1 | Tan | Is GTA 6 coming to PC? | Pregunta medida (autocompletado, Trends) | El rival sale de la grieta |
| 2 | Tin | Not announced. | Ausencia comprobada con primaria; **caduca**; relectura el 2026-12-04 | Golpe 1, puño, sin arma |
| 3 | Tin | Rockstar hasn't announced a PC version. | Misma ausencia | Golpe 2 (Tan, cuerpo) |
| 4 | Tin | It's on PlayStation 5 and Xbox Series X and S. | Tres primarias | Golpe 3 (Tin, cuerpo) |
| 5 | Tan | How long last time? | Pregunta | Respiro: la regla de tinta |
| 6 | Tin | GTA 5 took about a year and a half to reach PC. | 574 días (cuenta con script); Steam da 573 | Golpe 4 (regla contra el poste del farol) |
| 7 | Tan | Subscribe for facts, checked. | Invitación única, sin promesa de tema | Dicha en movimiento |
| 8 | Tin | Red Dead Redemption 2: about a year. | 375 días (Wikipedia) o 405 (Steam): «cerca de un año» | Golpe 5 (regla contra la persiana) |
| 9 | Tin | Files that say 'GTA 6 for PC' are not from Rockstar. | Ausencia de versión oficial; primaria más dos avisos | Bloqueo: Tin frena la mano de Tan |
| 10 | Tin | Some carry malware. | Malwarebytes (2026-08-24) y Huntress (2026-09-09), leídos | Pico: el paquete revienta |
| 11 | Tan | Don't download them. | No es un hecho: es el consejo del canal | — |
| 12 | Tin | No official PC date. As of today. | Misma ausencia, con sello de fecha | Remate: implosión |

**No se afirma:** que GTA 6 vaya o no a salir en PC; ninguna fecha, año, ventana ni proyección para GTA 6 en PC, ni en voz ni en
dibujo (ninguna barra, eje ni hueco); el port no oficial ni la filtración (ni nombre, ni imagen, ni cómo conseguirlos); que todo lo
que circula sea falso o malicioso; requisitos de PC; el rumor del primer trimestre de 2027; a ninguna persona. «Rated M» y los 212
GB van en la descripción, no en la voz.

## 5. Entorno, paleta y efectos

| Campo | Valor |
|---|---|
| Hoja y paleta | Noche · paleta B (`motor_de_accion/paletas/b_noche_de_tinta.json`), confirmada por fotografía; primera vez que se usa en un video. Fondo `#141B33`, suelo `#27304F`, línea y texto `#F3E9D2`, sombra y panel de subtítulo `#0B0F1F`. Acento cian `#4FE3FF`, solo detrás del dato y como subrayado en nombres de marca. Fuego: núcleo `#FFE45C`, borde `#B81414`. Humo `#9A6A45` con contorno. Tin y Tan conservan sus colores |
| Rival | Tinta lila `#B79CFF` con hollín `#0B0F1F`: **pendiente del dueño** (enmienda la ficha de `@duda`, «solo tinta»; dirección 11.1 k). Ningún rojo sobre su cuerpo |
| Entorno | Nuevo: `patio_tienda_de_computadoras`, exterior, de noche, sin logotipos: pila de torres genéricas con un monitor apagado, cajas de cartón, monitores sobre un palé, persiana metálica, farol. Entra al catálogo (temas: tecnología, hardware, compras) |
| Qué se rompe y se queda | `torre_de_pc_rota` (P-007), torre caída, cajas de cartón rotas, monitor roto, farol torcido, cajas carbonizadas, persiana abollada, quemadura del paquete, grieta del rival, marca del goteo; la `caja_registradora_rota` del short 4 está quieta desde el primer cuadro |
| Armas | Regla de tinta (de Tin y Tan) y paquete de tinta (del rival: caja lisa, sin texto ni icono). Sin armas de fuego ni sangre |
| Fuego, humo y explosiones | Chispas y fuego pequeño desde ≈ f344; explosión por fases f702–f726 (dos cuadros invertidos f702–f703 y un claro con máscara f709–f712); implosión f814–f831 que apaga el fuego y se lleva el humo |
| Cámara | 25 planos y 24 cortes (dirección 11.1 l); un solo cuadro de impacto, el del pico; sin temblor |
| Sonido | Voz de Kevin y Zelda, golpes y efectos por código pegados al contacto, percusión por código en otro patrón que el del short 4; silencio de f692 a f699. Nadie los ha oído |
| Universo | Pasivos al abrir: pestaña de cartón con un asterisco (P-001) y caja registradora rota (P-003). Activos: el rival sale de la grieta por la derecha (P-002, sustituye a la entrada de siempre), el telescopio de cartón cae en ≈ 19,2 s (P-006, grado ancla; anuncia el short 6), segunda marca de la pestaña (P-004) y el resto del rival gotea por el borde izquierdo (P-005). 38 fotogramas activos (tope 45) |

## 6. Requisitos del formato y lo fijo: cómo se cumplen y cómo se comprueban

Requisitos A1 a A14 de `canales/nostalgia-tin-y-tan/PARAMETROS.md`, sección 7, uno por uno. **Ninguno está puntuado**: se
puntúan con el video hecho.

| # | Requisito | Cómo lo cumple este video | Cómo se comprobará |
|---|---|---|---|
| A1 | Pelea con los tiempos medidos | Seis golpes (K = f88, f130, f212, f336, f484 y f812), un bloqueo (f652) y un toque (f700) con la gramática del short 4: anticipación de 6 f, pausa de 6 f antes del contacto, contacto de 2 f, lanzamiento de 4 f, vuelo, choque y recuperación; ninguna espera de más de 45 f sin contacto o esquive entre f150 y f300 | Lectura fotograma a fotograma de cada golpe en el render, contra la tabla de animación |
| A2 | Aceleración y desaceleración | Cámara lenta en los vuelos y en la anticipación del pico; velocidades distintas por golpe; borrón de movimiento en lo rápido; la voz no cambia | Curva de velocidad exportada por el motor; hoja de contactos a 2 por segundo y todos los fotogramas de los vuelos |
| A3 | Mundo con profundidad e interacción | Patio en 3D con suelo, pared y piezas a distintas distancias; el rival crece por profundidad (carril lejano); cada plano de acción tiene una interacción con una pieza | Lista de planos de la dirección: en cada uno, una interacción y un movimiento en profundidad a la vista |
| A4 | Fuego y humo | Chispas y fuego pequeño desde ≈ f344 en las cajas del pie del farol; humo con contorno desde la explosión; se apagan con la implosión | Fotogramas del fuego, del humo y de f700 legibles en una pantalla de teléfono; ningún fuego de partículas borrosas |
| A5 | Choques | Cinco choques de cuerpo contra el mundo: torre (f100), cajas (f146), monitor (f226), poste del farol (f344) y persiana (f500) | Cada choque deja su daño (A8) |
| A6 | Explosión e implosión | Explosión en f702–f726 con cuadros invertidos, radiales, claro con máscara, bola plana y enfriamiento; implosión en f814–f831 | `comprobar_destellos` sin avisos (máximo 3 destellos por segundo, máscara de 30 % o menos); ambas en la hoja de contactos |
| A7 | Sonidos de golpes | Un sonido por contacto con el pico en K −1 y otro por choque contra el mundo en el fotograma anterior al choque, por debajo de la voz; silencio de efectos y música de f692 a f699 | `eventos.json` contra la tabla de sonido; `revisar_voz.py` sin palabras perdidas; escucha de una persona |
| A8 | Daños que se quedan | Diez daños listados en la sección 5 de esta ficha, todos visibles en el plano de cierre | Fotograma f900 contra la lista |
| A9 | Rival con cuerpo | `@duda` versión 2: cuerpo de palitos, madeja por cabeza, rizo sin punto; color lila pendiente del dueño | Contra la hoja v2 aprobada |
| A10 | Paleta por tema | Paleta B, noche de tinta, porque el tema es de tecnología y no repite la hoja del short 4 | `revisar_color.py` con la paleta declarada: 85 % o más |
| A11 | Entorno por tema y catálogo al día | `patio_tienda_de_computadoras`, nuevo, con sus piezas y versiones rotas nombradas | Entradas nuevas en `catalogo.json`: entorno, piezas rotas, armas, efectos y sonidos, con «usada_en» |
| A12 | Armas dibujadas, sin armas de fuego ni sangre | Regla de tinta y paquete de tinta, dibujados en pantalla; la regla se deshace en gotas al final; ningún rojo sobre el rival | Revisión de fotogramas: ninguna arma de fuego ni su silueta; ninguna mancha roja fuera del borde del fuego |
| A13 | Conexión del universo | Cobra P-001, P-002 y P-003; siembra P-004, P-005, P-006 y P-007; control «se entiende solo» (dirección 9.4); 38 fotogramas activos | Registro de pistas (privado) con fotograma y zona medidos en el render; firma del supervisor |
| A14 | Escala: una página vertical | Un Short, 9:16, una sola página | Formato del archivo |
| Fijo | Firma del lápiz bumerán | Apertura f0–f29 y cierre f900–f929 sin cambios en la animación; excepción declarada: el fondo del cierre lleva los daños | `comprobar_firma`; la excepción de fondo, con la firma del director de animación |
| Fijo | Subtítulos en español | Quemados en la franja (y 885–1105), sin subtítulo en los planos de portada, con panel opaco | Medición de la franja; `revisar_texto.py` sobre los textos |
| Fijo | Cada dato con su fuente | Sección 4 de esta ficha; fuentes en la descripción y en pantalla (línea 10) | Comparación de voz, pantalla, subtítulo y descripción con el archivo de hechos |
| Fijo | Ninguna persona real ni marca golpeada | Los nombres de marca son texto de la capa de datos | Revisión de fotogramas |
| Fijo | Fotosensibilidad | Máximo 3 destellos por segundo; nunca blanco puro a pantalla completa | `comprobar_destellos`; `postpro.py destellos` |
| Fijo | Apto para 13 a 17 | Golpes, fuego y explosión de dibujo; el rival no da miedo ni muere | Revisión de una persona; columna «Avisos» |

## 7. Filtro de políticas: condiciones que aplican

El filtro F1 a F13 se repitió el 2026-11-27 sobre el guion final (líneas 1 a 12 de la dirección, 2.2) con las páginas de YouTube
abiertas ese día; el detalle, las citas y las condiciones están en `publicacion.md`, sección «Filtro de políticas sobre el guion
final». **Resumen:** las líneas 9, 10 y 11 (archivos falsos y malware) pasan sin cambiar ninguna palabra; F6 (tercer short de GTA
6), F8 (hecho que caduca), F9 (el video debe cumplir el título), F11 (voz generada) y F13 (sin avisos) pasan con condición; E2 («Rated
M» fuera de la voz) queda como punto abierto. **Se repite sobre el video terminado.**

## 8. Rúbrica

Puntaje: 0 no se cumple · 1 se cumple a medias · 2 se cumple. Cumplimiento = suma de puntaje por peso, sobre el doble de la suma
de pesos. «CUMPLE» con 80 % o más y todos los críticos en 2; un crítico por debajo de 2 es «NO PUBLICAR». Es el formato de fila y
la fórmula de `herramientas/puntuar_ficha.py`; la herramienta hoy solo acepta las disciplinas de la serie infantil, así que hasta
que admita estas secciones el cálculo se hace con la misma fórmula. Los fotogramas de la columna «Dónde» son del plan.

## Comercial e inteligencia digital

Responsable: `director-creativo` y `comercial-inteligencia-digital`

| # | Objetivo | Cómo se comprueba en el video | Dónde | Peso | Crítico | Puntaje | Evidencia |
|---|---|---|---|---|---|---|---|
| C1 | El gancho se entiende en el primer segundo y el fotograma 0 sirve de miniatura | En el fotograma 0 se ven el tema (monitor apagado, texto de portada), las dos caras y el lápiz en el aire; los primeros 3 s muestran a Tan, a Tin y el patio | f0 a f29 | 3 | sí | | |
| C2 | La respuesta oficial llega antes del segundo 5 | Se oye «Not announced.» entre ≈ 3,0 y ≈ 3,9 s y se lee quieta desde ≈ 3,2 s | f90 a f117 | 3 | sí | | |
| C3 | El video cumple lo que prometen título y portada | Responde «no está anunciado» y da los dos precedentes con fecha; la portada no da la respuesta ni insinúa fecha o descarga; firma una persona | Todo el video | 3 | sí | | |
| C4 | Entre los segundos 5 y 10 hay solo pelea y dato | Al menos cuatro acciones entre f150 y f300, ninguna espera de más de 45 f sin contacto o esquive, y ningún evento del universo | f150 a f300 | 2 | no | | |
| C5 | Una sola invitación, con voz, a mitad del video | Tan la dice una vez antes de los 15,5 s, sin promesa de tema, y no hay otro pedido en voz ni en pantalla | f438 a f471 | 2 | no | | |
| C6 | Título, descripción y portada pasan sus filtros | `revisar_titulo.py` con 0 errores y el bloque de título lleno en `publicacion.md`; descripción con descargo, fuentes y fecha de la relectura; portada según la regla del canal o decisión escrita del director creativo | Paquete de publicación | 3 | sí | | |

## Veracidad y políticas

Responsable: `comercial-inteligencia-digital` y `supervisor-de-continuidad`

| # | Objetivo | Cómo se comprueba en el video | Dónde | Peso | Crítico | Puntaje | Evidencia |
|---|---|---|---|---|---|---|---|
| V1 | Cada frase es la comprobada | Voz, pantalla, subtítulo y descripción coinciden con el archivo de hechos, sin una afirmación de más | Todo el video | 3 | sí | | |
| V2 | La respuesta no predice | Se oye not announced y no hay fecha, año, ventana, barra, eje ni hueco para GTA 6 en PC, ni en voz ni en dibujo; el sello de fecha es el de la relectura del día de publicar | f90 a f117 y f814 a f893 | 3 | sí | | |
| V3 | Nada del juego ni del port en pantalla | Ninguna imagen, logotipo, tipografía, nombre de personaje, nombre de proyecto o archivo; el paquete es una caja lisa sin texto, icono ni flecha | Todo el video | 3 | sí | | |
| V4 | El aviso de seguridad no enseña ni nombra | Las líneas 9 a 11 dicen que los archivos no son de Rockstar, que algunos traen programas maliciosos y que no se descarguen; sin nombres, enlaces ni cómo; las dos fuentes con fecha están en pantalla | f600 a f800 | 3 | sí | | |
| V5 | La relectura del 2026-12-04 se hizo | Rockstar, Take-Two y Wikipedia releídos ese día, sin anuncio de PC, y la fecha cambiada en los tres lugares | Antes de publicar | 3 | sí | | |
| V6 | Ninguna persona real ni marca recibe golpes | Los nombres de marca solo son texto de la capa de datos; nadie nombrado | Todo el video | 3 | sí | | |
| V7 | Apto para 13 a 17 | Sin sangre, sin armas de fuego, el rival no da miedo ni muere | Todo el video | 3 | sí | | |
| V8 | Clasificación M en la descripción | La descripción y el descargo dicen Mature 17+ (la voz no la dice, decisión C8) | Paquete de publicación | 2 | no | | |

## Formato de acción

Responsable: `director-de-animacion`, `director-de-fotografia` y `disenador-de-sonido`

| # | Objetivo | Cómo se comprueba en el video | Dónde | Peso | Crítico | Puntaje | Evidencia |
|---|---|---|---|---|---|---|---|
| A1 | Tiempos de golpe medidos | En cada golpe hay 6 fotogramas de pausa antes del contacto y el contacto dura 1 o 2 | Seis golpes y el bloqueo | 3 | sí | | |
| A2 | Aceleración y desaceleración | Cámara lenta en los vuelos y antes del pico, no después del contacto | Vuelos y f694 a f699 | 2 | no | | |
| A3 | Mundo con profundidad e interacción | Cada plano de acción tiene una interacción con el entorno y un movimiento hacia el fondo o hacia cámara | 25 planos | 3 | sí | | |
| A4 | Fuego y humo | Fuego plano por fases y humo con contorno, legibles en teléfono | f344 a f831 | 2 | no | | |
| A5 | Choques | Cada choque de cuerpo contra el mundo deja un daño | Cinco choques | 2 | no | | |
| A6 | Explosión e implosión | Las dos presentes y dentro del límite de destellos | f702 a f726 y f814 a f831 | 3 | sí | | |
| A7 | Sonidos de golpes | Cada contacto suena en su fotograma o uno antes, la voz se entiende entera y ningún efecto tapa un nombre o una cifra dichos | Tabla de sonidos | 2 | no | | |
| A8 | Daños que se quedan | Los diez daños se ven en el plano final | f900 | 3 | sí | | |
| A9 | Rival con cuerpo | Coincide con la hoja aprobada y lleva el rizo sin punto; ningún rojo sobre su cuerpo | Siempre que aparece | 2 | no | | |
| A10 | Paleta por tema | Medición de color dentro de la paleta B declarada | Video completo y fotograma 0 | 2 | no | | |
| A11 | Entorno y catálogo | El entorno es el de la dirección y el catálogo tiene las entradas nuevas | Catálogo del motor | 2 | no | | |
| A12 | Armas dibujadas | Solo regla y paquete de tinta dibujados en pantalla; ninguna arma de fuego; nada rojo sobre el rival | f296 a f893 | 3 | sí | | |
| A13 | Universo | Pagos y siembras donde dice la dirección, medidos; pasa el control se entiende solo; eventos activos de 45 fotogramas o menos | f0 y f576 a f869 | 2 | no | | |
| A14 | Escala | Una página vertical | Formato | 1 | no | | |

## Lo fijo del canal

Responsable: `supervisor-de-continuidad`

| # | Objetivo | Cómo se comprueba en el video | Dónde | Peso | Crítico | Puntaje | Evidencia |
|---|---|---|---|---|---|---|---|
| F1 | Firma del lápiz bumerán | Pasa la comprobación de la firma; la única diferencia en el empalme es el fondo, firmada | f0 a f29 y f900 a f929 | 3 | sí | | |
| F2 | Subtítulos en español | Quemados dentro de su franja, sin tapar un contacto ni la portada, y ninguna pista aparte subida a YouTube | Todo el video | 3 | sí | | |
| F3 | Dato quieto mientras se lee | Cada dato sin moverse 30 fotogramas o más, un dato a la vez | Siete datos | 2 | no | | |
| F4 | Fotosensibilidad | Tres destellos por segundo como máximo y nunca blanco puro a pantalla completa | Todo el video | 3 | sí | | |
| F5 | Texto sin errores | Ortografía y nombres propios correctos en pantalla, subtítulos y descripción | Todo el texto | 3 | sí | | |
| F6 | Control «se entiende solo» | Quien no ha visto otro video cuenta qué preguntó Tan, qué se respondió y qué hay que hacer con los archivos | Todo el video | 2 | no | | |

## Producción

Responsable: `jefe-de-produccion` y `editor-de-video`

| # | Objetivo | Cómo se comprueba en el video | Dónde | Peso | Crítico | Puntaje | Evidencia |
|---|---|---|---|---|---|---|---|
| P1 | Sin fotogramas muertos | Hoja de contactos sin cuadros vacíos, congelados ni texto cortado | Todo el video | 2 | no | | |
| P2 | Una sola generación de voz | Registro de costos con una generación por voz, cotizada y autorizada con el número a la vista | Costos | 3 | sí | | |
| P3 | Duración y formato del máster | Entre 29 y 32 segundos, 1080×1920, 30 f/s | Archivo final | 2 | no | | |
| P4 | Prueba completa | La prueba lleva todos los pedidos del canal antes de presentarse | Lista de pedidos | 3 | sí | | |
| P5 | Licencias y catálogo al día | Cada recurso con su origen | Licencias | 2 | no | | |

## Emoción

Responsable: `director-creativo`

| # | Objetivo | Cómo se comprueba en el video | Dónde | Peso | Crítico | Puntaje | Evidencia |
|---|---|---|---|---|---|---|---|
| E1 | La tensión sube golpe a golpe | Cada golpe cambia de quién, de dirección y de contra qué choca el rival; el más fuerte antes del pico es el de la cifra grande | f88 a f700 | 2 | no | | |
| E2 | El pico es el paquete que revienta | La explosión cae entre el 70 y el 90 por ciento del video y es el único evento que no es un golpe contra el rival | f700 a f732 | 2 | no | | |
| E3 | El rival no da miedo ni hay ensañamiento | Falla su contraataque, mira su paquete reventado y nadie golpea a un caído | Todo el video | 3 | sí | | |
| E4 | El final se entiende como respuesta honesta | Una persona que no conoce el canal cuenta que no hay fecha oficial para PC y que no se descarguen archivos falsos | f800 a f893 | 3 | sí | | |
| E5 | El cierre deja el plano de portada | Último plano igual al primero salvo los daños | f900 a f929 | 1 | no | | |

## Metas después de publicar

Fechas contadas desde la publicación prevista (viernes 2026-12-04, 16:00, El Salvador); se mueven con la hora real. Comparación
con el short 4 a la misma edad si está público (hoy no lo está: sale el 2026-12-02) y, si no, con el short 2. Las cifras de
comparación están en `estadisticas/datos/` y no se suben. Detalle, lectura del escalón y método en `publicacion.md`.

| Cuándo | Indicador | Meta | De dónde sale la meta | Dónde se lee |
|---|---|---|---|---|
| 48 a 72 horas (2026-12-06 y 12-07) | «Se quedó a mirar» | No más de 5 puntos por debajo del video de comparación | Brief y dirección, sección 1 | Studio, Interacción (visto frente a deslizado) |
| 48 a 72 horas | Fila «Feed de Shorts» | Presente | Brief, «Estrategia» | Studio, Alcance, fuentes de tráfico |
| 48 a 72 horas, 7 y 28 días | Avisos | Ninguno | Brief; un aviso cuesta la admisión | Studio, contenido, columna «Avisos» |
| 48 a 72 horas | Retención al segundo 3 y en los segundos 5 a 10 | Establecer línea base | Sin base propia para fijar un número | Studio, retención de audiencia |
| 48 a 72 horas | Escalón de retención en ≈ 19,2 s | Ningún escalón (umbral de lectura de partida: el doble de la pérdida de los tramos vecinos, hipótesis del equipo) | Brief, «Lo confirma» y «Lo descarta» | Misma curva |
| 48 a 72 horas y 7 días | Retención entre ≈ 13 y ≈ 17 s (invitación) | Establecer línea base | Estreno del pedido a mitad del video | Misma curva |
| 7 días (2026-12-11) | Suscriptores por mil vistas | Establecer línea base | Hoy: cero suscriptores | Studio, suscriptores por contenido |
| 7 días | Pico (≈ 23,3 a ≈ 24,4 s) y caída al oír «No official PC date» | Establecer línea base | Sin dato propio | Misma curva |
| 7 y 28 días | Porcentaje medio visto y duración media | Establecer línea base; no más de 5 puntos por debajo del video de comparación | Brief | Studio, Interacción |
| 7 y 28 días | Búsqueda de YouTube y términos de búsqueda | Establecer línea base | La búsqueda es marginal en el canal | Studio, «Cómo encuentran tu video» |
| 7 y 28 días | Comentarios, compartidos, público que regresa | Establecer línea base | Hoy en cero | Studio |
| 28 días (2027-01-01) | Decisión sobre el patrón de gancho «la pregunta tal cual, con la respuesta delante» | Anotar «a prueba» con la cifra | Un video no decide | Todo lo anterior |

## Resultado

Sin evaluar. Se llena después del render con el puntaje y la evidencia de cada fila, y los resultados de las metas se llenan con
los datos que el dueño exporte de Studio.

## 9. Costo y pendientes

| Concepto | Costo |
|---|---|
| Voz de Tan y de Tin | Estimación del diseñador de sonido: ≈ 2,6 a 3,0 créditos (Tin ≈ 2,0 a 2,3; Tan ≈ 0,6 a 0,7; ≈ 26 a 30 s de voz a 0,1 créditos por segundo). **Es estimación, no cotización**; producción cotiza con `estimate_audio_cost` y el dueño autoriza con el número a la vista. Nada gastado. Referencia: los shorts 3 y 4 costaron ≈ 3,7 y ≈ 3,1 |
| Imagen, video, música y efectos | 0 (por código) |

Pendientes: tabla «Sin resolver» de `direccion.md` (sección 10) y pendientes de la sección 11.3; portada que cumpla la regla (decisión
del director creativo); color lila del rival (dueño); cotización de la voz; relectura del 2026-12-04.
