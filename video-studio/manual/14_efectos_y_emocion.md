# 14 · Efectos y emoción (la gramática de efectos del estudio)

> Regla del dueño (2026-11-23), textual: *«No es lo que a mí me guste; cada efecto animado comunica y al mismo tiempo
> provoca una emoción, por eso debe ser basado en tu investigación»*.
>
> Este capítulo dice, para cada efecto de video, de animación y de profundidad: **qué comunica, qué emoción provoca,
> por qué (mecanismo), cuándo usarlo, cuándo no y cómo se mide**. Lo leen el director creativo, el director de
> fotografía, el director de animación, el editor, el diseñador de sonido y el supervisor de continuidad. En el canal
> infantil manda `infantil/guia_1_a_3.md` y decide la psicóloga.

**Quién:** el director creativo elige la emoción de cada segundo (`02_prompt/perfil_emocional.md`); fotografía,
animación, edición y sonido eligen el efecto en la tabla de este capítulo; el supervisor de continuidad comprueba la
dosis y la seguridad. Los efectos dibujados por código están en `herramientas/efectos.py` (gratis).

## 0. Cómo leer este capítulo: los tres sellos

Nada de aquí es gusto. Cada afirmación sobre percepción o emoción lleva uno de estos sellos:

- **[investigación]**: hallazgo o concepto establecido de psicología de la percepción, ciencia cognitiva del cine o
  comunicación, con autores, año y dónde se leyó.
- **[oficio]**: principio aceptado de la profesión, con su fuente. Es práctica, no ciencia.
- **[hipótesis del equipo]**: no se encontró respaldo. Se dice y se indica con qué métrica se va a comprobar.

Tres advertencias que valen para todo el capítulo:

1. **«Abierta» quiere decir que la página se descargó y se leyó el 2026-11-23.** Casi todo lo abierto es Wikipedia
   en inglés (fuente secundaria) y ayuda oficial de Google. De cada concepto se anotan los autores y la referencia
   primaria que Wikipedia cita; **el artículo primario no se abrió** (la red no deja). Lo que solo se vio en el
   resumen de un buscador dice «(resumen)». La lista completa está en la sección 9.
2. **Casi ningún estudio se hizo con Shorts verticales en un teléfono.** La investigación respalda el mecanismo (por
   ejemplo, que el paralaje se percibe como profundidad); que ese mecanismo mejore una métrica de YouTube es siempre
   **[hipótesis del equipo]** hasta medirlo.
3. **Las dosis (fotogramas, frecuencia máxima) son la norma de partida del estudio: [hipótesis del equipo]**, salvo
   las que citan una norma (destellos, duración de plano infantil). Se ajustan con los datos de cada video.

Sin cifras de «aumenta la retención un X %»: no se abrió ninguna fuente que las dé.

## 1. Cómo se elige un efecto (procedimiento en 5 pasos)

Se hace por cada tramo del video, antes de dibujar o generar, y queda escrito en `02_prompt/perfil_emocional.md`.

1. **Objetivo comercial.** El que fijó el dueño en el brief. Hoy, para todos los canales: entrar al Programa de
   socios. Se traduce a **una** métrica por tramo (sección 2, última columna): visto frente a deslizado, retención
   en ese segundo, repeticiones, compartidos o suscriptores.
2. **Qué debe sentir el espectador en ese segundo.** Una sola emoción dominante por plano (cap. 01, «Reglas de
   uso»), tomada del arco del video. Si no se puede nombrar la emoción, todavía no se elige efecto.
3. **Qué debe mirar.** Un solo punto del cuadro (la cifra, el objeto, la cara). Se escribe dónde está ese punto.
4. **Qué efecto lo consigue según la tabla.** Se busca por emoción (sección 3) y por momento (sección 4), se
   comprueba que el público lo admite (sección 5) y que pasa los límites de seguridad (sección 6). Se anota el
   efecto, su código de respaldo (R1, R2…) y su sello. Si el sello es **[hipótesis del equipo]**, se dice.
5. **Cómo se mide.** La métrica de la tabla, con el segundo exacto del video donde se va a mirar la curva. Después
   de publicar, el resultado va a `estadisticas/datos/` y a la ficha.

**La regla inversa: un efecto sin función se quita.** En la revisión, el supervisor de continuidad pregunta por
cada efecto: ¿qué emoción, qué punto del cuadro, qué métrica? Si falta una de las tres respuestas, el efecto sale.
Dos efectos sobre el mismo punto en el mismo segundo (por ejemplo golpe + destello + sacudida en la misma palabra)
cuentan como uno con función y dos sin ella: se dejan uno.

## 2. Tabla maestra

Primero el banco de respaldos (2.1) y después una fila por efecto (2.2 a 2.8). Las filas citan los códigos del
banco (R1, R2…).

### 2.1 Banco de respaldos

Cada código dice qué prueba **y qué no**.

#### Profundidad

- **R1 · Paralaje de movimiento. [investigación]** Es una clave monocular de profundidad: cuando el observador se
  mueve, lo cercano pasa rápido y lo lejano casi no se mueve (Ferris, 1972, *Journal of Experimental Psychology*
  95). Abierta: Wikipedia, «Depth perception». No prueba que la profundidad retenga más.
- **R2 · Oclusión (interposición). [investigación]** Las superficies cercanas tapan a las lejanas; es clave
  monocular de profundidad. Abierta: Wikipedia, «Depth perception» (sección «Occultation»).
- **R3 · Sombras. [investigación]** La luz y las sombras que arrojan los objetos son una clave eficaz de su forma y
  de su posición en el espacio (Lipton, 1982; Medina Puerta, 1989, *J. Opt. Soc. Am. A* 6, «shadow stereopsis»).
  Abierta: Wikipedia, «Depth perception».
- **R4 · Expansión óptica. [investigación]** Un objeto cuya imagen crece en la retina se percibe moviéndose hacia
  el observador; de ese ritmo de expansión se calcula el tiempo hasta el contacto (Swanston y Gogel, 1986,
  *Perception & Psychophysics* 39). Abierta: Wikipedia, «Depth perception».
- **R5 · Estímulos que se aproximan («looming»). [investigación]** Hay una respuesta fisiológica automática a
  percibir como «algo que se acerca» lo que crece en la retina; sirve para evitar choques y detectar depredadores.
  Schiff, Caviness y Gibson (1962, *Science* 136) describieron respuestas de miedo persistentes en monos rhesus; el
  sistema existe desde los primeros días de vida (van der Weel y van der Meer, 2009, *Naturwissenschaften* 96); hay
  «looming» también auditivo (Gray, 2011). Abierta: Wikipedia, «Looming». **No prueba** que un zoom en la pantalla
  de un teléfono suba la activación de un adulto: eso es **[hipótesis del equipo]**.
- **R6 · Efecto de profundidad cinética. [investigación]** Una figura plana que rota deja ver su forma en tres
  dimensiones (Wallach y O'Connell, 1953, *Journal of Experimental Psychology* 45). Abierta: Wikipedia, «Depth
  perception».
- **R7 · Desenfoque, perspectiva aérea y textura. [investigación]** Figuran como claves monoculares: lo lejano
  pierde contraste y saturación, y el detalle fino solo se ve de cerca. Abierta: Wikipedia, «Depth perception».
- **R8 · Cámara multiplano. [oficio]** Capas de dibujo a distintas distancias que se mueven a distintas velocidades:
  cuanto más lejos, más lento. De ahí viene el «parallax scrolling». Abierta: Wikipedia, «Multiplane camera» y
  «Parallax scrolling».
- **R9 · Cambio de foco. [oficio]** «Rack focus»: pasar el foco de un sujeto a otro dentro del plano (Bordwell,
  Thompson y Smith, *Film Art*, 11.ª ed., citado en Wikipedia, «Focus puller», abierta). Que el ojo siga al foco es
  práctica de oficio (cap. 02: «dirigir la mirada sin cortar»); **no se abrió ningún estudio con seguimiento ocular
  que lo mida** (sección 8).

#### Atención y montaje

- **R10 · Respuesta de orientación y habituación. [investigación]** Reacción a un estímulo nuevo o significativo
  (el reflejo «¿qué es?» de Pavlov); con la repetición la respuesta baja (Sokolov, 1960). Abierta: Wikipedia,
  «Orienting response» y «Habituation». Consecuencia: **un efecto que se repite deja de funcionar**.
- **R11 · Los cortes provocan orientación. [investigación]** (resumen) Lang, Geiger, Strickwerda y Sumner (1993,
  *Communication Research* 20) encontraron que los cortes producen los signos fisiológicos de una respuesta de
  orientación. Solo visto en resumen de buscador, citado por un estudio de 2016.
- **R12 · Duración de los planos en el cine. [investigación]** Cutting, DeLong y Nothelfer (2010, *Psychological
  Science*) midieron 150 películas de 1935 a 2005: los planos se acortaron con los años y su secuencia se acerca a
  un patrón 1/f. El trabajo posterior añade más movimiento, más primeros planos y menos desorden en el cuadro.
  Abierta: Wikipedia, «James E. Cutting»; detalle del artículo, en resumen. **Ojo:** que ese patrón siga la
  atención es una propuesta de los autores, no un resultado, y el artículo no dice que esas películas gusten más.
- **R13 · Teoría atencional de la continuidad. [investigación]** (resumen) Smith (2012, *Projections* 6): el montaje
  de continuidad funciona porque usa señales naturales de atención (movimiento, miradas, gestos, sonidos fuera de
  cuadro) para llevar la mirada a través del corte. Solo visto en resumen de buscador.
- **R14 · Corte en el movimiento. [oficio]** La acción empieza en un plano y termina en el siguiente; ese puente
  distrae del corte y de los pequeños errores de continuidad. Abierta: Wikipedia, «Cutting on action».
- **R15 · Efecto Kuleshov. [investigación], con fuentes que se contradicen.** Prince y Hensley (1992, *Cinema
  Journal* 31; 137 participantes, una sola prueba por persona) **no** encontraron el efecto. Mobbs y otros (2006,
  *Social Cognitive and Affective Neuroscience* 1) y Barratt y otros (2016, *Perception* 45; 36 participantes, 24
  secuencias) **sí**: una cara neutra se juzga según el plano que la acompaña. Abierta: Wikipedia, «Kuleshov
  effect». Se usa con cautela: el plano de al lado tiñe la cara, pero no la sustituye.
- **R16 · Murch y la emoción primero. [oficio]** *In the Blink of an Eye* (Murch, 1992; 2.ª ed. 2001) pide al
  montador poner la emoción por encima de lo técnico; ahí formula su «regla de seis». Abierta: Wikipedia, «Walter
  Murch» e «In the Blink of an Eye (Murch book)». El orden de los seis criterios (emoción, historia, ritmo, línea
  de mirada, plano bidimensional, espacio tridimensional) se cita de memoria del oficio; **no se abrió** el libro.
- **R17 · Montaje como choque. [oficio]** Eisenstein: el sentido nace del choque de planos independientes, cada
  uno percibido «encima» del anterior. Abierta: Wikipedia, «Soviet montage theory».
- **R18 · Ritmo de corte. [oficio]** Planos cortos dan urgencia; planos largos, calma. El corte rápido (planos de
  3 s o menos) transmite mucha información, energía o caos (Nelmes, 2003). Abierta: Wikipedia, «Fast cutting» y
  «Shot (filmmaking)»; la frase sobre urgencia está en una sección **sin referencias**.
- **R19 · Corte que se nota. [oficio]** El «jump cut» rompe la continuidad y llama la atención sobre el montaje
  (Bordwell y Thompson, *Film Art*); el «smash cut» corta de golpe con fin cómico, narrativo o emocional. Abierta:
  Wikipedia, «Jump cut» y «Smash cut».
- **R20 · Congelado. [oficio]** Viene del cuadro vivo del teatro, que servía para subrayar la importancia de una
  escena. Abierta: Wikipedia, «Freeze-frame shot».
- **R21 · Plano subjetivo. [oficio]** Muestra lo que ve un personaje; da un punto de vista subjetivo frente al
  objetivo de los demás planos. Abierta: Wikipedia, «Point-of-view shot».

#### Animación

- **R22 · Los 12 principios. [oficio]** Thomas y Johnston, *The Illusion of Life* (1981). Los que se usan aquí:
  aplastar y estirar (peso y flexibilidad, sin cambiar el volumen); anticipación (prepara al público para la
  acción); puesta en escena (dirige la atención a lo más importante); entrada y salida lentas (más dibujos al
  principio y al final: lo real acelera y frena); seguimiento y acción superpuesta (lo suelto sigue moviéndose y
  vuelve con oscilación amortiguada); acción secundaria (da vida y apoya, sin tapar la principal); ritmo («timing»,
  crítico para el ánimo, la emoción y la reacción del personaje); exageración (la imitación perfecta se ve estática
  y sosa), y la pausa en movimiento, que evita lo «sin vida». Abierta: Wikipedia, «Twelve basic principles of
  animation».
- **R23 · Animacidad. [investigación]** (resumen) Tremoulet y Feldman (2000, *Perception* 29): un solo objeto
  rígido parece vivo según la magnitud de su cambio de velocidad y de dirección. Solo visto el resumen del
  artículo. Heider y Simmel (1944, *American Journal of Psychology* 57) quedó localizado en Wikipedia («Fritz
  Heider», abierta), sin leer su contenido.
- **R24 · Movimiento biológico. [investigación]** Johansson (1973): con unos pocos puntos de luz en las
  articulaciones se reconoce la acción cuando se mueven, no cuando están quietos; también se reconocen ira,
  tristeza y alegría. Abierta: Wikipedia, «Biological motion». Es el fundamento de que un muñeco de palitos
  transmita emoción **por cómo se mueve**, no por su cara.
- **R25 · Movimiento con aceleración. [oficio]** (resumen) Material Design de Google: en el mundo real nada arranca
  ni se detiene al instante; la velocidad se ajusta con duración y curva de aceleración. Solo visto en resumen
  (páginas antiguas de la guía); el sitio actual no se pudo abrir.

#### Emoción, memoria y compartir

- **R26 · Mera exposición. [investigación]** Zajonc (1968): lo que ya se ha visto gusta más que lo nuevo parecido;
  demostrado con palabras, figuras, caras y sonidos. Abierta: Wikipedia, «Mere-exposure effect».
- **R27 · Fluidez de procesamiento. [investigación]** Lo que se procesa con facilidad (claridad visual, contraste,
  repetición) se juzga más verdadero, más agradable y da más confianza (Alter y Oppenheimer, 2009). Abierta:
  Wikipedia, «Processing fluency».
- **R28 · Curiosidad. [investigación]** Berlyne (1960): la despiertan la novedad, la complejidad, la incertidumbre
  y el conflicto, además de la sorpresa y la incongruencia. Loewenstein (1994, *Psychological Bulletin* 116) la
  trata como deseo motivado de información (la «brecha de información»). Abierta: Wikipedia, «Curiosity»; el
  artículo de Loewenstein no se abrió.
- **R29 · Nostalgia. [investigación]** Emoción agridulce; mejora el ánimo, **aumenta la conexión social**, la
  autoestima y el sentido (Wildschut, Sedikides, Arndt y Routledge, 2006; Sedikides y otros, 2008). La dispara la
  soledad, y también la música, el cine y la televisión. Abierta: Wikipedia, «Nostalgia».
- **R30 · Pico de reminiscencia. [investigación]** Los mayores de 40 recuerdan más y mejor lo vivido en la
  adolescencia y la primera juventud (Jansari y Parkin, 1996; Rubin, Rahhal y Poon). Abierta: Wikipedia,
  «Reminiscence bump». Dice **qué** objetos mostrar a cada edad.
- **R31 · Autorreferencia. [investigación]** Lo que se relaciona con uno mismo se recuerda mejor (Rogers, Kuiper y
  Kirker, 1977). Abierta: Wikipedia, «Self-reference effect».
- **R32 · Qué se comparte. [investigación]** Berger y Milkman (2012, *Journal of Marketing Research* 49): cuanto
  más activa una emoción, sobre todo las de alta activación, más se pasa el contenido. Abierta: Wikipedia, «Viral
  phenomenon». **Ojo:** el estudio es sobre artículos de prensa, no sobre videos cortos.
- **R33 · Efecto de aislamiento (von Restorff, 1933). [investigación]** Entre elementos parecidos, el que se
  distingue se recuerda más. Abierta: Wikipedia, «Von Restorff effect». Es el fundamento del acento único (cap. 13).
- **R34 · Regla del pico y el final. [investigación]** Una experiencia se juzga sobre todo por su momento más
  intenso y por su final, no por el promedio (Kahneman). Abierta: Wikipedia, «Peak–end rule».
- **R35 · Sorpresa y sobresalto. [investigación]** La sorpresa es breve, nace de la diferencia entre lo esperado y
  lo que ocurre, y puede ser agradable, desagradable o neutra. El sobresalto es una respuesta defensiva, en gran
  parte inconsciente, a un ruido o movimiento súbito. Abierta: Wikipedia, «Surprise (emotion)» y «Startle response».
- **R36 · Humor. [investigación]** Dos teorías: incongruencia y resolución; y violación benigna (McGraw y Warren):
  algo amenaza cómo «debería ser» el mundo, parece inofensivo y se ven las dos lecturas a la vez. Abierta:
  Wikipedia, «Theories of humor». Son teorías, no recetas.
- **R37 · Asombro. [investigación]** Keltner y Haidt (2003, *Cognition and Emotion* 17): «en lo más alto del placer
  y en el límite del miedo», ante algo más grande o poderoso que uno. Abierta: Wikipedia, «Awe».
- **R38 · Ternura (esquema del bebé). [investigación]** Lorenz: ciertos rasgos infantiles hacen que algo se vea
  tierno y despiertan el impulso de cuidarlo (Glocker y otros, 2009, *PNAS* 106). Abierta: Wikipedia, «Cuteness».
- **R39 · Sonido pegado a la imagen. [oficio]** «Mickey Mousing»: sincronizar la música con la acción. Chion,
  *L'audio-vision* (1990), es el libro de referencia sobre la relación entre sonido e imagen. Abierta: Wikipedia,
  «Mickey Mousing» y «Michel Chion»; el libro no se abrió.
- **R40 · Viñeta y grano. [oficio]** La viñeta se añade para llevar el interés al centro y enmarcarlo; el grano se
  añade como efecto artístico. Abierta: Wikipedia, «Vignetting» y «Film grain». Que el grano «suene a pasado» no
  tiene cita: **[hipótesis del equipo]**.
- **R41 · Animación de pizarra. [investigación]** Un estudio de 2016 (Türkay) concluye que, pese a su popularidad,
  hay poca o ninguna prueba experimental sólida de que enseñe, motive o convenza más que otros formatos. Abierta:
  Wikipedia, «Whiteboard animation». Por eso los garabatos son **[hipótesis del equipo]**.

#### Seguridad y público

- **R42 · Epilepsia fotosensible. [investigación]** ≈ 1 de cada 4.000 personas. Disparan crisis las luces que
  parpadean, las imágenes que se alternan rápido y los patrones regulares de rayas o cuadros; casi siempre con
  contraste de luminosidad alto; **más si llenan todo el campo visual**; el cambio solo de color, sin cambio de
  luminosidad, rara vez. La frecuencia sensible varía por persona. Las pautas de televisión británicas nacen de un
  anuncio de 1993 y de los trabajos de Graham Harding (prueba de Harding, regulador Ofcom); en 1997 un episodio de
  Pokémon con destellos a pantalla completa llevó a más de 600 personas al hospital. Abierta: Wikipedia,
  «Photosensitive epilepsy», «Harding test», «Graham Harding», «Dennō Senshi Porygon».
- **R43 · WCAG 2.3.1, «Tres destellos o por debajo del umbral» (nivel A). [investigación]** (norma; texto en
  resumen) Nada parpadea más de tres veces en un segundo, o el destello queda por debajo de los umbrales. Destello
  general: un par de cambios opuestos de luminancia relativa de 10 % o más con la imagen oscura por debajo de 0,80.
  Hay umbral aparte para el rojo saturado. Wikipedia («Web Content Accessibility Guidelines», abierta) confirma el
  criterio y su nivel; **el texto de la norma solo se vio en resumen** (w3.org bloqueado). El propio resumen avisa
  de que cumplir el umbral no garantiza seguridad.
- **R44 · Movimiento y mareo. [investigación]** La cinetosis se produce con movimiento real **o percibido**;
  ≈ un tercio de la población es muy susceptible y las mujeres algo más (Wikipedia, «Motion sickness», abierta). En
  pantallas basta la sensación visual de moverse uno mismo (LaViola, 2000; Wikipedia, «Virtual reality sickness»,
  abierta). WCAG 2.3.3 (nivel AAA) pide poder desactivar la animación no esencial porque provoca distracción,
  mareo, dolor de cabeza y náusea, y nombra el paralaje como ejemplo (resumen). Android ofrece «Quitar
  animaciones» (support.google.com, abierta; la página dice que es para «ayudar a concentrarse»).
- **R45 · Vista y atención con la edad. [investigación]** La sensibilidad al contraste baja desde los 40 a 50 años
  en detalle fino (Owsley, Sekuler y Siemsen, 1983; resumen). El campo visual útil se reduce con la edad, por menor
  velocidad de procesamiento visual y más dificultad para ignorar distracciones (Sekuler, Bennett y Mamelak, 2000;
  Wikipedia, «Useful field of view», abierta). La presbicia avanza desde los 40 (Wikipedia, «Presbyopia», abierta).
  El capítulo 13 ya fija 7:1 de contraste para 45 o más.
- **R46 · Ritmo rápido en primera infancia. [investigación]** Lillard y Peterson (2011, *Pediatrics* 128): niños de
  4 años que vieron 9 minutos de un dibujo animado de ritmo rápido rindieron peor, justo después, en tareas de
  función ejecutiva que los que vieron uno lento o dibujaron. Abierta: Wikipedia, «SpongeBob SquarePants»; detalle
  en resumen. **Límites:** son niños de 4 años, no de 1 a 3; el efecto medido es inmediato; la cadena criticó el
  método; una revisión sistemática de 2024 encuentra resultados mixtos, y el estudio no separa el ritmo de lo
  fantástico del contenido. Concuerda con la guía infantil (§5), que ya decía «muy rápido y fantástico».
- **R47 · Televisión infantil diseñada con investigación. [oficio]** *Blue's Clues* usó repetición, la misma
  estructura en cada episodio e invitación a participar, con investigación dentro del proceso (Anderson, 2004).
  Abierta: Wikipedia, «Blue's Clues».

#### Datos de plataforma (no llevan sello: son definiciones de YouTube, leídas el 2026-11-23)

- **P1 · Curva de retención.** Línea plana: se ve ese tramo entero. Bajada gradual: se pierde interés. **Picos:
  ese tramo se volvió a ver o se compartió** (o no se entendió y hubo que repetirlo). **Caídas: ahí se saltó o se
  abandonó.** Los «momentos clave» solo aparecen en videos de 60 s o más con 100 vistas o más.
  https://support.google.com/youtube/answer/9314415?hl=en
- **P2 · Métricas.** «Engaged views»: vistas que pasan del primer fotograma. `shares`: veces que se usó el botón
  Compartir. `subscribersGained`: suscripciones. `averageViewPercentage`: porcentaje medio visto.
  https://developers.google.com/youtube/analytics/metrics
- **P3 · Umbral del Programa de socios.** 1.000 suscriptores y 4.000 horas calificadas en 12 meses, o 1.000
  suscriptores y 10 millones de vistas calificadas de Shorts en 90 días; la página avisa de cambios desde el
  1-feb-2027. https://support.google.com/youtube/answer/72851?hl=en. El detalle está en
  `canales/nostalgia-tin-y-tan/plan_programa_de_socios.md`, que además recoge que **las repeticiones en bucle no
  cuentan como vistas calificadas**.
- **P4 · «Visto frente a deslizado».** Es el dato que da Studio para Shorts (cap. 10). **No se encontró la página
  de ayuda que lo define** (sección 8).

**Cómo leer las tablas:** la columna «Mecanismo y respaldo» separa lo que está respaldado de lo que es apuesta del equipo. Las
dosis son a **30 fotogramas por segundo** (f = fotogramas; 30 f = 1 s) y son norma de partida (sección 0, punto 3).
Entre paréntesis, la función de `herramientas/efectos.py` cuando existe.

### 2.2 Profundidad

| Efecto | Qué comunica | Emoción o estado | Mecanismo y respaldo | Úsalo cuando | No lo uses cuando | Dosis | Métrica que lo delata |
|---|---|---|---|---|---|---|---|
| **Capas con paralaje** (`Capa`, `Camara`, `componer`) | «esto es un lugar, no una lámina»; qué está cerca y qué lejos | presencia, atención tranquila | Profundidad: R1, R8 **[investigación]**. Que un plano con profundidad se perciba como «más cuidado» y se deslice menos: **[hipótesis del equipo]** | planteamiento, plano héroe, recorrido lento por un objeto | hay texto que leer y el texto se mueve; amplitud grande (R44); infantil salvo muy lento | 2 o 3 capas; la cámara recorre como máximo ≈ 8 % del ancho por segundo | retención sin caída en ese tramo; si va en 0–1 s, visto frente a deslizado |
| **Cambio de foco** (`Camara.foco`) | «ahora mira esto», sin cortar | curiosidad que se resuelve | R9 **[oficio]**; el desenfoque como clave de distancia, R7 **[investigación]**. Que la mirada siga al foco en un Short: **[hipótesis del equipo]** | pasar del objeto al personaje, o de la pregunta a la respuesta | el plano que se desenfoca lleva texto que aún se está leyendo | 8–12 f; máximo 1 cada 5 s | retención en ese segundo |
| **Revelado desde desenfoque** (`revelar_desde_desenfoque`) | «algo aparece», «un recuerdo que vuelve» | anticipación breve | La incertidumbre despierta curiosidad, R28 **[investigación]**. Que lo borroso se lea como «recuerdo»: **[hipótesis del equipo]** | presentar el objeto nostálgico después del gancho | en el fotograma 0: el primer fotograma tiene que leerse nítido | 6–10 f; 1 o 2 por video | retención del segundo donde se revela |
| **Sombras de contacto y proyectadas** (`sombra_contacto`, `sombra_proyectada`, `sombra_de_suelo`) | «pisa el suelo, pesa, está ahí» | solidez, credibilidad | R3 **[investigación]** | siempre que un personaje u objeto toca una superficie | la sombra tapa texto o ensucia el papel | permanente; opacidad ≈ 0,2 a 0,3 | no tiene métrica propia: control de calidad (cap. 12) |
| **Algo cruza por delante** (`cruce_por_delante`) | «hay algo más cerca que tú»; esconde un corte | sorpresa leve, fluidez | Profundidad: R2 **[investigación]**. El movimiento como puente del corte: R14 **[oficio]**, R13 **[investigación]** (resumen) | cambiar de escena o de idea | tapa la cifra en su momento de lectura; infantil | 4–8 f en total, tapado completo 3 f como máximo; 1 cada 6–8 s | que no haya caída de retención en el corte |
| **Escala o acercamiento hacia cámara** (`acercar`, `Camara.avance`) | «esto viene hacia ti», «esto importa» | alerta, sobresalto leve | R4 y R5 **[investigación]** (respuesta defensiva documentada en monos y bebés). En un adulto frente al teléfono: **[hipótesis del equipo]** | el gancho: el objeto llega a cámara; el remate | infantil (nada que asuste); junto con destello; más de 2 veces (R10) | 8–12 f con frenada al final; el objeto ocupa como máximo ≈ 75 % del ancho; 1 o 2 por video | visto frente a deslizado |
| **Atravesar la escena** (`atravesar`) | «entramos en otro tiempo o en otro nivel» | asombro, sensación de viaje | Riesgo de mareo: R44 **[investigación]**. La emoción de «viaje»: **[hipótesis del equipo]** | el paso del presente al pasado, una sola vez | más de una vez; público sensible al movimiento; infantil | 10–14 f; 1 por video | retención en la transición; picos (se vuelve a ver) |
| **Órbita** | «objeto valioso, míralo entero» | admiración | La rotación revela volumen, R6 **[investigación]**; «momento clave, héroe, producto» (cap. 02) **[oficio]** | plano héroe de un objeto con volumen | personajes planos de palitos (delata que no tienen volumen): ahí, giro de 15° como máximo; infantil | 30–60 f, lenta; 1 por video | retención del plano héroe |

### 2.3 Cámara

| Efecto | Qué comunica | Emoción o estado | Mecanismo y respaldo | Úsalo cuando | No lo uses cuando | Dosis | Métrica que lo delata |
|---|---|---|---|---|---|---|---|
| **Empuje lento** | «esto importa cada vez más» | intimidad, tensión que crece, ternura | cap. 01 y 02 **[oficio]**; percepción de acercamiento, R4 **[investigación]** | antes de la revelación; momentos de ternura | mientras se lee texto pequeño | 45–90 f; la escala sube 5–10 % | retención del tramo anterior a la revelación |
| **Zoom de golpe** (`golpe_de_zoom`, `transicion_zoom`) | «¡esto!» | sorpresa cómica | cap. 01 y 02 **[oficio]**; R5 y R35 **[investigación]** | en la cifra o en el remate | infantil (prohibido); más de 2 por video (R10); 45–70 años: 1 | 4–6 f de ida y 6–8 f de asiento; escala ≤ +35 % | picos de retención en ese segundo |
| **Sacudida** (`sacudida`) | «impacto» | sobresalto leve, energía | movimiento súbito y sobresalto, R35 **[investigación]**; su uso para «peso» **[oficio]** | un golpe físico, una cifra que cae | hay texto fino en pantalla; infantil; más de 1 cada 5 s | ≤ 8 f, amplitud ≤ 16 px y decreciente | retención en ese segundo |
| **Barrido** (`barrido_obturador`, `salida_del_cuadro`) | «cambio de tema, rápido» | energía | cap. 02 **[oficio]**; riesgo, R44 **[investigación]** | entre dos bloques del video | infantil (prohibido en la guía §7); 45–70 años: más de 2 | 5–8 f | que no haya caída en el corte |
| **Plano fijo de respiro** | «míralo con calma» | calma; seriedad del humor *deadpan*; tiempo para entender | cap. 01 **[oficio]**; con la edad baja la velocidad de procesamiento visual, R45 **[investigación]** | después de una ráfaga; antes del remate; por defecto en infantil | en 0–1 s si dentro del plano no se mueve nada | adultos 45–90 f; infantil 180 f o más (guía §7) | línea plana en la curva de retención (P1) |
| **Subjetivo** | «lo ves con sus ojos», «son tus manos» | inmersión, recuerdo en primera persona | R21 **[oficio]**; autorreferencia, R31 **[investigación]** | las manos usando el objeto de época | junto con sacudida; infantil solo lento | 45–75 f | compartidos y comentarios («yo también») |
| **Macro** | «el detalle que recuerdas» | nostalgia sensorial, ternura | cap. 02 **[oficio]**; recuerdo de juventud, R30 **[investigación]** | la textura o la pieza del objeto que todos tocaron | el detalle no es exacto: ese público lo conoció y lo nota | 30–60 f | retención; comentarios que corrigen = alerta |

### 2.4 Montaje

| Efecto | Qué comunica | Emoción o estado | Mecanismo y respaldo | Úsalo cuando | No lo uses cuando | Dosis | Métrica que lo delata |
|---|---|---|---|---|---|---|---|
| **Corte seco** | «y ahora esto» | reorienta; sorpresa si hay contraste | R10 **[investigación]**; R11 **[investigación]** (resumen); choque de planos, R17 **[oficio]** | por defecto | infantil: solo con la imagen en reposo | 0 f | — |
| **Corte en el movimiento** | «sigue siendo la misma acción» | fluidez; el corte no se nota | R14 **[oficio]**; R13 **[investigación]** (resumen) | unir dos planos de una acción; tapar un defecto | se quiere que el corte se note (remate) | cortar 2–4 f después de que arranca el movimiento | que no haya caída en el corte |
| **Ráfaga de cortes** | «muchas cosas, muy rápido» | activación, urgencia | R18 **[oficio]**; R11 **[investigación]** (resumen); R12 no prueba que guste más | enumerar; un montaje de época | infantil (prohibido); texto distinto en cada plano; saltos fuertes de luminosidad entre planos (cuentan como destellos, R43) | 3–6 planos de 8–15 f; 45–70 años: 12 f o más por plano; máximo 2 ráfagas en 30 s | retención durante la ráfaga y justo después |
| **Plano de respiro tras ráfaga** | «ya; aquí está» | alivio | el estímulo repetido pierde efecto, R10 **[investigación]**; «picos y respiros» (cap. 11, regla 14) **[hipótesis del equipo]** | siempre después de una ráfaga | — | 60–90 f | línea plana después de la ráfaga |
| **Congelado** (`congelado_con_marco`) | «este instante»; «esto ya es una foto» | énfasis, humor, recuerdo | R20 **[oficio]**; pausa antes del remate (cap. 07) **[oficio]** | el remate; convertir el momento en foto de álbum | a mitad de una frase de la voz | 9–15 f (0,3–0,5 s) | picos en ese segundo |
| **Bucle** | «vuelve a empezar» | cierre redondo | el final pesa en el juicio, R34 **[investigación]**; que el empalme haga volver a ver: **[hipótesis del equipo]** (cap. 11, regla 3) | el cierre de los Shorts de adultos | infantil (sin ganchos para seguir mirando; solo saludo y despedida iguales) | último fotograma = primero; empalme de 6 f o menos | duración media vista por encima del 100 %. **Aviso:** la repetición no cuenta como vista calificada (P3) |
| **Gancho de varios cortes en el primer segundo** | «aquí está pasando algo» | orientación, curiosidad | R10 **[investigación]**; R11 **[investigación]** (resumen). Que más cortes bajen los deslizados: **[hipótesis del equipo]** (cap. 11 lo trata igual) | Shorts de adultos | infantil; si impide leer la promesa | 2 o 3 planos en 30 f; el primero, con la promesa legible, 12 f o más | visto frente a deslizado |

### 2.5 Animación

| Efecto | Qué comunica | Emoción o estado | Mecanismo y respaldo | Úsalo cuando | No lo uses cuando | Dosis | Métrica que lo delata |
|---|---|---|---|---|---|---|---|
| **Anticipación** | «va a pasar algo» | expectativa | R22 **[oficio]** | antes de toda acción importante | se busca sorpresa total | 4–8 f de movimiento contrario | retención en la acción |
| **Aplastar y estirar** | peso, elasticidad, vida | simpatía, humor | R22 **[oficio]** | saltos, caídas, cosas blandas | objetos rígidos de verdad (un casete, una tecla): deformarlos les quita verdad; infantil, muy suave | extremos de 2–4 f; volumen constante | — |
| **Overshoot con muelle** (`muelle`, `muelle_exacto`) | «llegó con energía» | viveza, agrado | seguimiento con oscilación amortiguada, R22 **[oficio]**; cambios de velocidad y sensación de vida, R23 **[investigación]** (resumen). Que agrade más que una entrada suave: **[hipótesis del equipo]** (cap. 11, regla 11) | entradas de texto y de objetos | infantil (sin rebote); todo rebota a la vez (R10) | se pasa 10–15 % como máximo y se asienta en 8–14 f | — |
| **Ease in/out frente a lineal** (`eo`, `eio`) | curva: natural, con peso. Lineal: máquina | curva: confianza, naturalidad. Lineal: frialdad | R22 **[oficio]**; R25 **[oficio]** (resumen); R23 **[investigación]** (resumen) | curva en todo lo vivo; lineal solo en lo mecánico (cinta que gira, segundero) | lineal en personajes o en texto (cap. 11, regla 7) | — | — |
| **Acción secundaria** | «está vivo aunque no hable» | calidez, ternura | R22 **[oficio]**; R24 **[investigación]** | bufanda, lápiz, copete: siempre | compite con la cifra en el mismo segundo | amplitud pequeña, continua | — |
| **Rebote al pulso** | «va con la música» | alegría, energía | R39 **[oficio]** | hay música con pulso claro y no hay voz diciendo un dato | infantil; encima de la cifra | 1 por pulso; escala ≤ 6 % | — |
| **Contador que acelera y frena** (`contador`) | «es muchísimo… y es exactamente esto» | anticipación y luego satisfacción | incertidumbre y curiosidad, R28 **[investigación]**; ritmo, R22 **[oficio]**. La forma de la curva: **[hipótesis del equipo]** | la cifra central del video | el contador retrocede (`DESIGN.md`); más de 1 por video | 36–72 f; frena en los últimos 10–15 f; cifra final quieta 30 f o más (45 f para 45–70 años) | retención y picos en el segundo de la cifra |
| **Entrada escalonada** | orden, jerarquía, «una lista» | claridad | puesta en escena, R22 **[oficio]**; menor velocidad de procesamiento con la edad, R45 **[investigación]** | listas, titulares, varias piezas de un objeto | más de 5 elementos; frases largas | desfase de 3–5 f; cada elemento entra en 8–10 f | retención del tramo |

### 2.6 Luz y color

| Efecto | Qué comunica | Emoción o estado | Mecanismo y respaldo | Úsalo cuando | No lo uses cuando | Dosis | Métrica que lo delata |
|---|---|---|---|---|---|---|---|
| **Destello corto** (`destello`) | «golpe», «cambio» | sobresalto | R35, R42 y R43 **[investigación]** | un solo corte clave | infantil (prohibido); a pantalla completa en blanco puro; junto con zoom de golpe | 2–4 f; nunca más de 3 por segundo; 45–70 años: 1 cada 5 s como máximo | `postpro.py destellos` y `comprobar_destellos` en 0; retención en ese segundo |
| **Inversión o negativo** (`negativo_paleta`, `mascara_circulo`) | «lo contrario», «ruptura» | extrañeza, impacto | cuenta como destello, R42 y R43 **[investigación]**. La emoción: **[hipótesis del equipo]** | un giro de idea, una vez, en una zona limitada | a pantalla completa; repetido; infantil; encima de texto | 4–6 f; 1 por video | igual que el destello |
| **Viñeta** (`papel`) | «mira al centro»; aire de foto vieja | recogimiento | R40 **[oficio]** | permanente y suave | es tan fuerte que baja el contraste del texto en los bordes | permanente | contraste medido con `revisar_color.py` |
| **Paso de neutro a acento** | «esto es lo importante» | foco, recordación | R33 **[investigación]**; cap. 13 (2 neutros + 1 acento) | la palabra clave, la cifra | hay dos acentos en el mismo plano | el acento en un solo elemento y en el título | retención del segundo 1 al 3; recordación |
| **Desaturar antes del color** | «antes y ahora»; «vuelve a la vida» | de melancolía a alegría | el contraste con lo anterior destaca, R33 **[investigación]**; el significado del color depende del contexto (Elliot y Maier, 2014, cap. 13): **[hipótesis del equipo]** | revelar el objeto | la paleta ya es de saturación baja (Tin & Tan, ≈ 17 %): queda poco margen | transición de 20–30 f | retención en la revelación |
| **Textura de papel o grano** (`papel`) | «hecho a mano, de otra época» | calidez | R40 **[oficio]**; que suene a pasado: **[hipótesis del equipo]** | permanente | el grano cambia en cada fotograma (parpadeo); `papel()` lo deja fijo | fijo | — |

### 2.7 Texto y gráficos

| Efecto | Qué comunica | Emoción o estado | Mecanismo y respaldo | Úsalo cuando | No lo uses cuando | Dosis | Métrica que lo delata |
|---|---|---|---|---|---|---|---|
| **Palabra clave que entra con golpe** (`palabra_clave`, `K`) | «esta palabra» | énfasis | R33 y R10 **[investigación]** | una por frase | varias a la vez; infantil (sin texto) | entra en 4–6 f, se asienta en 6–8 f; en pantalla 20 f o más (30 f o más para 45–70 años) | retención en ese segundo |
| **Texto de vidrio** (`panel_vidrio`, `texto_vidrio`) | «léelo aunque el fondo se mueva» | claridad | el contraste facilita la lectura, R27 **[investigación]**. Que el vidrio se perciba como «moderno»: **[hipótesis del equipo]** | texto sobre un fondo con detalle o con movimiento | el fondo liso ya da contraste de sobra | contraste 7:1 o más (cap. 13) | `revisar_color.py --contraste` |
| **Titulares en cascada** (`titulares_en_cascada`) | «pasaron muchas cosas» | acumulación, prisa | R18 **[oficio]**. La emoción: **[hipótesis del equipo]** | un montaje de época, una lista de hechos | más de 4; 45–70 años: cada titular legible menos de 24 f | desfase de 6–10 f | retención del tramo |
| **Garabatos que se dibujan** (`garabato`, `trazo_*`) | «te lo señalo a mano» | cercanía, curiosidad por el trazo sin terminar | no hay prueba sólida de que este formato convenza más, R41 **[investigación]**; incertidumbre, R28. El efecto: **[hipótesis del equipo]** | rodear, subrayar, una flecha | encima de texto; más de 2 a la vez | 8–15 f por trazo | retención en ese segundo |
| **Gráfico que crece** | «cuánto», comparado con algo | comprensión, asombro | asombro ante lo que es mucho mayor, R37 **[investigación]**. Su uso en gráficos: **[hipótesis del equipo]** | comparar dos magnitudes | la escala engaña (cap. 12: cifras con fuente) | 20–40 f con frenada | retención; compartidos |
| **Subrayado** (`trazo_subrayado`) | «esto» | énfasis suave | R33 **[investigación]** | una palabra clave en un plano tranquilo | ya lleva golpe y color (énfasis triple) | 6–10 f | — |

### 2.8 Sonido atado a la imagen

Cada corte y cada efecto llevan su sonido (cap. 11, regla 17). El sonido no es un añadido: es la mitad del efecto.

| Efecto | Qué comunica | Emoción o estado | Mecanismo y respaldo | Úsalo cuando | No lo uses cuando | Dosis | Métrica que lo delata |
|---|---|---|---|---|---|---|---|
| **Golpe en el corte** | «aquí pasó algo» | impacto | R39 **[oficio]**; ruido súbito y sobresalto, R35 **[investigación]** | cortes y entradas clave | infantil («sin golpes ni sustos», guía §7); todos los golpes iguales y en todos los cortes (R10) | a ±1 f de la imagen; mezcla a −14 LUFS (cap. 07) | retención en el corte |
| **Subida antes de la revelación** | «viene algo» | anticipación | «build-up» (cap. 01) **[oficio]**; hay «looming» auditivo, R5 **[investigación]** | 0,5 a 1,5 s antes de la cifra | infantil; no hay revelación que la pague | 15–45 f | retención del tramo anterior |
| **Silencio antes del dato** | «atento» | expectación | pausa antes del remate (cap. 01 y 07) **[oficio]**; el cambio brusco es novedad, R10 **[investigación]** | justo antes de la cifra o del remate | más de 2 por video | 9–15 f (0,3–0,5 s) | retención y picos en la cifra |

## 3. Por emoción (índice inverso)

| Emoción | La producen | Combinados cómo | La arruinan |
|---|---|---|---|
| **Nostalgia** | macro y subjetivo del objeto; textura de papel y viñeta; revelado desde desenfoque; congelado con marco; desaturar antes del color | primero el objeto exacto de la juventud de ese público (R30), en primera persona (R31) y despacio; después el dato. La nostalgia es una emoción **social** (R29): el plano con los dos personajes juntos pesa más que el objeto solo **[hipótesis del equipo]** | ráfaga de cortes sobre el objeto; destellos; negativo; un detalle inexacto; estética de aplicación actual |
| **Curiosidad** | gancho con pregunta visual; cambio de foco; garabato a medio dibujar; contador que arranca; algo que cruza por delante | abrir una sola incógnita y dejarla abierta (R28); cada efecto señala hacia la respuesta, ninguno la da | resolver en el primer segundo; abrir tres incógnitas; texto que no da tiempo a leer |
| **Anticipación** | anticipación del personaje; empuje lento; subida de sonido; contador que acelera; silencio antes del dato | en este orden: anticipación → empuje y subida → silencio de 9–15 f → revelación (R22) | que no haya revelación; una subida de más de 1,5 s en un Short; dos subidas seguidas |
| **Sorpresa** | corte seco con contraste; zoom de golpe; escala hacia cámara; destello único; sacudida | **uno solo** por sorpresa, después de un tramo tranquilo: la sorpresa es la diferencia con lo esperado (R35) | repetirlos (R10); anunciarlos; juntar tres en el mismo fotograma |
| **Alivio** | plano fijo de respiro; la cifra quieta; el silencio que termina en nota mayor; frenada del contador | después del pico, 60–90 f sin efectos | cortar el respiro con otro gancho; música que sigue subiendo |
| **Ternura** | acción secundaria; empuje lento; macro; curvas suaves; plano a la altura de los ojos | movimientos lentos y completos (cap. 01); rasgos redondos y cabeza grande (R38) | sacudida, zoom de golpe, destello, cortes rápidos |
| **Asombro** | gráfico que crece; plano general con capas; atravesar la escena; la cifra enorme quieta | la magnitud comparada con algo conocido (R37), y luego silencio | escala falsa; texto encima de la cifra; cortar antes de que se entienda |
| **Confianza** | curvas con frenada; sombras de contacto; contraste alto; la misma paleta y los mismos gestos en todos los videos | lo fácil de procesar se cree más (R27) y lo ya visto gusta más (R26) | movimiento lineal; texto que salta; un tipo de efecto nuevo en cada video; cifras sin fuente |
| **Humor** | plano fijo; pausa; corte seco en el remate; congelado; aplastar y estirar | seriedad total, pausa de 9–15 f y un solo efecto exacto en el remate (cap. 01, *deadpan*; R36) | subrayar el chiste con zoom, sacudida y sonido a la vez; explicar el remate |

## 4. Por momento del video

| Momento | Tocan | No tocan |
|---|---|---|
| **Gancho (0–1 s)** | objeto o cifra legible **desde el fotograma 0**; escala hacia cámara; palabra clave con golpe en el acento; 1 o 2 cortes con su sonido; movimiento dentro del plano desde el primer fotograma (cap. 11, regla 1) | revelado desde desenfoque (retrasa la lectura), logo, plano vacío, destello a pantalla completa, texto de más de 4 palabras |
| **Planteamiento (1–5 s)** | capas con paralaje, sombras, subjetivo o macro del objeto, cambio de foco, entrada escalonada | ráfagas, zoom de golpe (se gasta antes del remate), bucles de texto |
| **Desarrollo** | corte en el movimiento, garabatos, titulares en cascada, **una** ráfaga con su respiro, acción secundaria continua | el mismo efecto tres veces seguidas (R10); texto de vidrio sin necesidad |
| **Revelación** | subida de sonido → silencio → contador que acelera y frena → cifra quieta; empuje lento antes; un zoom de golpe **o** un destello, no los dos | cortar durante la cifra; mover la cámara mientras se lee |
| **Remate** | corte seco, congelado, pausa; plano fijo | añadir información nueva; música que tapa |
| **Cierre y bucle** | plano fijo de los personajes (firma del canal), mismo gesto y mismo sonido siempre; último fotograma igual al primero | despedida larga; lista de peticiones; cualquier efecto nuevo |

Infantil (1 a 3 años): estos momentos **no aplican**. La estructura es saludo → presentación → práctica → cierre →
invitación (`infantil/guia_1_a_3.md` §3) y no hay gancho ni bucle.

## 5. Por público

### 5.1 Adultos de 30 a 50 años en Shorts

- Admiten el ritmo de redes del capítulo 11. Las dosis de la tabla son para ellos.
- Texto: 1 a 3 palabras por golpe, contraste 4,5:1 como mínimo (cap. 13).
- Destellos: los de la tabla, nunca más de 3 por segundo (R43).

### 5.2 Adultos de 45 a 70 años en Shorts

Lo respaldado: baja la sensibilidad al contraste en el detalle fino, baja la velocidad de procesamiento visual,
cuesta más ignorar distracciones y la vista cercana empeora (R45). Lo que el estudio deduce de ahí es norma de
partida, **[hipótesis del equipo]**, y se mide con la retención en los tramos con texto:

| Aspecto | Norma para 45–70 |
|---|---|
| Legibilidad | contraste 7:1 (cap. 13); texto grande; el acento claro siempre con contorno oscuro; separar por claro contra oscuro, no solo por tono |
| Tiempo de lectura | cada palabra clave quieta 30 f o más; la cifra final, 45 f o más |
| Velocidad | planos de 12 f o más también dentro de las ráfagas; máximo 2 ráfagas en 30 s; un respiro de 60–90 f después de cada una |
| Un solo foco | nada se mueve en el fondo mientras hay texto que leer |
| Destellos | 1 cada 5 s como máximo, 2–4 f, nunca a pantalla completa en blanco puro |
| Movimiento | paralaje y zoom pequeños (sección 6); sin barridos encadenados |

### 5.3 Niños de 1 a 3 años (serie `granja`)

Manda `infantil/guia_1_a_3.md` y decide la psicóloga. La investigación (R46, con sus límites) va en el mismo
sentido que la guía: ritmo lento, un solo foco, tiempo para mirar. Aquí no se busca enganchar.

**PROHIBIDOS** (por la guía §1, §5 y §7, y por los capítulos 01, 02 y 11):

- Zoom de golpe, barrido (*whip pan*), cámara en mano, sacudida, ángulo holandés.
- Ráfaga de cortes, gancho de varios cortes, corte brusco, bucle como gancho, cualquier suspenso al final.
- Destello, inversión o negativo, parpadeos, neón añadido al escenario.
- Escala o acercamiento rápido hacia cámara, atravesar la escena, cualquier cosa que se abalance (R5: la
  respuesta a lo que se acerca existe desde los primeros días de vida).
- Todo texto en pantalla: palabra clave, texto de vidrio, titulares, contadores, subrayados.
- Golpes de sonido, subidas, sustos; música debajo de la palabra clave.
- Rebote al pulso y overshoot marcado; objetos que aparecen solos o por arte de magia.
- Transiciones con efecto (barridos, zooms, cruces).

**PERMITIDOS:**

- Plano fijo, o movimiento de cámara lento y suave a la altura de los ojos de los personajes.
- Corte directo con la imagen en reposo, o fundido lento. Cada plano que ve el niño dura 6 s o más (180 f).
- Empuje muy lento hacia el objeto que se nombra; cambio de foco lento para guiar la mirada.
- Sombras de contacto suaves; profundidad sin movimiento de capas, o con movimiento muy lento.
- Anticipación, acción secundaria suave (el copete de Tiky), curvas con frenada, movimientos lentos y completos.
- La mirada del personaje como guía: objeto → cámara → objeto (guía §6).
- La pausa de 3 a 5 s después de cada pregunta, como plano propio.
- Sonidos reales a volumen parejo; música suave solo en el saludo y el cierre.

## 6. Seguridad: límites duros del estudio

Se comprueban antes de entregar; si uno falla, el video no sale. Firma el supervisor de continuidad.

| Límite | Valor | Fuente | Cómo se comprueba |
|---|---|---|---|
| Destellos | nunca más de 3 en un segundo; nunca blanco puro ni negro puro a pantalla completa | R43 (WCAG 2.3.1) y R42; ya estaba en el cap. 11, regla 20 | `postpro.py destellos`; `efectos.comprobar_destellos` |
| Tamaño del destello | limitado a una zona (máscara) siempre que se pueda; opacidad máxima 0,6 | R42: lo que llena el campo visual es más peligroso | código (`efectos.destello`) |
| Rojo | ningún parpadeo hacia o desde un rojo saturado | R43 (umbral aparte para el rojo; resumen) | revisión de fotogramas |
| Patrones | sin rayas ni cuadrículas regulares de alto contraste que ocupen mucho cuadro, quietas o en movimiento | R42 | revisión de fotogramas |
| Cortes como destellos | una ráfaga con saltos de luminosidad entre planos cuenta como destellos; entre planos de una ráfaga, saltos de luminosidad pequeños | R42 («imágenes que se alternan rápido»); cap. 13, punto 3 de colorimetría | `revisar_color.py` (saltos) |
| Grano y ruido | la textura no cambia de un fotograma a otro | R42 (parpadeo) | código (`efectos.papel`) |
| Paralaje y zoom grandes | la cámara no recorre más de ≈ 8 % del ancho por segundo; zoom de golpe ≤ +35 %; sacudida ≤ 16 px y ≤ 8 f; un solo «atravesar» por video; sin dos movimientos de cámara encadenados | R44 (WCAG 2.3.3 nombra el paralaje; cinetosis por movimiento percibido). **Los números son [hipótesis del equipo]**: ninguna fuente abierta da un umbral | revisión de fotogramas |
| «Reducir movimiento» | un video no puede leer esa preferencia del teléfono: el espectador que la tiene activada verá el movimiento igual. Por eso los límites anteriores se aplican **a todos** los videos | R44 | — |
| Infantil | lista de prohibidos de la sección 5.3 | guía infantil; R46 | psicóloga |

## 7. Aplicación a Tin & Tan (para el tercer video)

**Dato real** del primer Short (`TIN-EN-S-001`, 48 h, `estadisticas/datos/2026-11-23_TIN-EN-S-001_48h.md`): 533
vistas, 92 % desde el feed de Shorts; **20,7 % se quedó a mirar**; duración media vista 0:19 de 0:31 (**63 %**);
**0 compartidos; 0 suscriptores**.

**Lectura.** De cada cinco personas a las que se les mostró, cuatro deslizaron antes de quedarse: el problema
mayor es el primer segundo. Quien se queda ve casi dos tercios: el desarrollo aguanta. Nadie lo pasó ni se
suscribió: el video no deja un pico que pida ser enviado ni una razón para volver. Dos cautelas: son 533 vistas
(muestra pequeña) y **no se abrió ninguna fuente oficial que diga qué porcentaje de «se quedó a mirar» es bueno**;
se compara contra los propios videos del canal.

**Objetivo:** Programa de socios (1.000 suscriptores y vistas calificadas de Shorts, P3). Las repeticiones en
bucle no cuentan para el umbral; los suscriptores sí.

### 7.1 Los efectos que atacan esos tres problemas

Tiempos para un Short de ≈ 30 s a 30 fps. El segundo exacto se ajusta al guion.

| # | Problema | Efecto | En qué segundo | Por qué (respaldo) | Cómo se mide |
|---|---|---|---|---|---|
| 1 | Primer segundo | **El objeto de época, nítido y con la cifra o la pregunta ya legible en el fotograma 0** (el fotograma 0 es la portada), con **escala hacia cámara** | 0,0–0,4 s (12 f, frenando; el objeto llega a ≈ 75 % del ancho) | Lo que crece se percibe como algo que se acerca y pide atención: R4, R5 **[investigación]**. El objeto es de la juventud de ese público: R30 **[investigación]**. Que eso baje los deslizados: **[hipótesis del equipo]** | visto frente a deslizado, contra el 20,7 % |
| 2 | Primer segundo | **Palabra clave con golpe en mostaza con contorno** sobre papel, una sola, más su golpe de sonido | 0,2–0,6 s (entra en 5 f, se asienta en 7 f, queda quieta 30 f o más) | El único elemento distinto se recuerda y atrae: R33; lo nuevo orienta: R10 **[investigación]**; sonido pegado a la imagen: R39 **[oficio]** | visto frente a deslizado; retención al segundo 1 |
| 3 | Primer segundo | **Un corte dentro del primer segundo** (dos planos, no más), hecho como **corte en el movimiento**: el objeto sigue moviéndose a través del corte | ≈ 0,7 s; el primer plano dura 20 f o más para que se lea | Los cortes provocan orientación: R11 **[investigación]** (resumen); el movimiento tiende el puente: R14 **[oficio]**. Solo uno, por el público de 45 a 70 (R45) | visto frente a deslizado; que no haya caída en 0,7–1,5 s |
| 4 | Primer segundo y retención temprana | **Capas con paralaje y sombras de contacto** en el plano de Tin & Tan con el objeto | 1–4 s, cámara lenta (≈ 8 % del ancho por segundo como máximo) | Profundidad real: R1, R3 **[investigación]**. Que se perciba como producción cuidada y sostenga la mirada: **[hipótesis del equipo]** | retención del segundo 1 al 4 |
| 5 | No se comparte | **Subjetivo o macro de las manos usando el objeto** (el gesto que todos hicieron), con Tin y Tan juntos en el plano siguiente | 4–8 s, 45–75 f, sin cortes | Lo que habla de uno mismo se recuerda: R31; la nostalgia aumenta la conexión social: R29 **[investigación]**. Que eso lleve a enviarlo a quien lo vivió con uno: **[hipótesis del equipo]** | compartidos por cada 1.000 vistas; comentarios «yo también» |
| 6 | No se comparte | **El pico: subida de sonido → silencio de 10–12 f → contador que acelera y frena → cifra quieta 45 f**, con **un** zoom de golpe suave (≤ +20 %) al caer la cifra | entre el 60 % y el 75 % del video (≈ 18–23 s) | Se comparte más lo que activa: R32; el juicio se forma con el pico y el final: R34; la sorpresa es la diferencia con lo esperado: R35 **[investigación]**; anticipación y ritmo: R22 **[oficio]** | pico en la curva de retención en ese segundo (P1); compartidos |
| 7 | No se suscribe | **Cierre de firma: plano fijo de respiro con Tin y Tan, congelado con marco de foto**, el mismo gesto, la misma paleta y el mismo sonido corto en **todos** los videos, con una sola invitación | últimos 2–3 s; 60–90 f; el último fotograma empalma con el primero | Lo ya visto gusta más: R26; el final pesa: R34; lo fácil de reconocer da confianza: R27 **[investigación]**. Que una firma repetida convierta en suscriptores: **[hipótesis del equipo]** | suscriptores por cada 1.000 vistas; espectadores que regresan |
| 8 | No se suscribe | **Acción secundaria continua** (las puntas de la bufanda de Tan, el lápiz de Tin) y **curvas con frenada** en todo movimiento de los personajes | todo el video | Con solo el movimiento se leen la acción y la emoción: R24 **[investigación]**; da vida: R22 **[oficio]**. Que el apego al personaje lleve a suscribirse: **[hipótesis del equipo]** | suscriptores; comentarios que nombran a Tin o a Tan |

Reglas de uso para este canal: una sola incógnita abierta en el gancho; el acento mostaza solo en la palabra clave
y en el lápiz (cap. 13); 12 f o más por plano; un destello como máximo, y mejor ninguno; nada se mueve detrás de la
cifra mientras se lee. Y se cambia **una cosa por video** respecto del anterior en el primer segundo, para saber a
qué se debe el cambio en el dato.

### 7.2 Tres efectos de moda que NO convienen a este canal

| Efecto de moda | Por qué no aquí |
|---|---|
| **Estrobo: destellos, negativos a pantalla completa y cortes de menos de 8 f al pulso de la música** | El público es de 45 a 70: procesa más despacio y le cuesta más ignorar distracciones (R45). Los destellos y la alternancia rápida de imágenes son el disparador clásico de crisis fotosensibles y lo que llena el campo visual es peor (R42, R43). Arruina la nostalgia (sección 3). Y lo repetido deja de sorprender (R10). **[investigación]** en el riesgo; que además ahuyente a este público: **[hipótesis del equipo]** |
| **Subtítulos que saltan, tiemblan y cambian de color en cada palabra, con zoom y sacudida constantes** | Un énfasis en todo no destaca nada: el efecto de aislamiento necesita un fondo homogéneo (R33). Texto en movimiento con contraste variable es lo contrario de lo que pide la vista de ese público (R45, cap. 13). El zoom y la sacudida continuos suman movimiento percibido (R44). **[investigación]** en el mecanismo |
| **Estética de aplicación actual: texto de vidrio en todo, degradados, neón y transiciones 3D con órbitas** | Contradice lo que el canal promete: papel, tinta y años 70 (`DESIGN.md` prohíbe degradados; cap. 11, regla 7). El papel con tinta ya da 12,6:1: el vidrio no añade lectura. Los muñecos de palitos son planos: una órbita delata que no tienen volumen. Cambiar de estética de un video a otro pierde la familiaridad (R26). Que rompa la nostalgia: **[hipótesis del equipo]**; el texto de vidrio queda para cuando haya un fondo con detalle |

Sobre el **bucle**: se mantiene porque redondea el cierre, pero no es la palanca del objetivo: la repetición no
cuenta como vista calificada (P3). No se sacrifica el cierre de firma por un empalme invisible.

## 8. Lo que no se pudo confirmar y hosts bloqueados

**Hosts que la red bloqueó (un intento, sin insistir):**

- `www.w3.org`: texto de WCAG 2.3.1 y 2.3.3. Lo citado viene del resumen de un buscador.
- `m3.material.io`: guía de movimiento de Material Design 3.
- `web.dev`: adonde redirige la página de Google sobre «prefers-reduced-motion».
- La interfaz `api.php` de `en.wikipedia.org` respondió «demasiadas solicitudes»; las páginas se leyeron por
  `index.php?action=raw`.

**Sin confirmar (no se usa como dato hasta abrirlo):**

1. **Profundidad de campo y guía de la mirada:** no se abrió ningún estudio con seguimiento ocular. Queda como
   oficio (R9).
2. **«Looming» y activación en adultos frente a una pantalla pequeña:** lo abierto habla de monos, bebés y
   evitación de choques (R5).
3. **Ritmo de corte y atención:** el artículo de Cutting (2010) y el de Lang (1993) solo se vieron en resumen; la
   relación entre el patrón 1/f y la atención es una propuesta de los autores (R11, R12).
4. **Smith, teoría atencional de la continuidad (2012)**, y **Smith y Henderson (2008)** sobre cortes que no se
   notan: el primero, solo en resumen; el segundo no apareció.
5. **Murch, regla de seis:** el orden y los pesos de los seis criterios no se leyeron en fuente abierta (R16).
6. **Curvas de aceleración y animacidad:** Tremoulet y Feldman (2000), solo el resumen; Heider y Simmel (1944),
   solo la referencia. No se encontró nada sobre curvas de aceleración y emoción en gráficos animados.
7. **Loewenstein (1994):** no se abrió el artículo; la «brecha de información» se cita por su referencia.
8. **Contraste y legibilidad con la edad:** Owsley (1983), solo en resumen. No se encontró fuente sobre tamaño de
   letra o tiempo de lectura de mayores en video; los números de la sección 5.2 son del equipo.
9. **Lillard y Peterson (2011):** no se confirmó el tamaño de la muestra; el estudio no es con niños de 1 a 3 años.
10. **Material Design:** solo páginas antiguas en resumen; ninguna dice nada del movimiento lineal.
11. **«Visto frente a deslizado»:** no se encontró la página de ayuda de YouTube que lo define, ni un valor de
    referencia oficial.
12. **Mareo por paralaje o zoom en video:** ninguna fuente da un umbral numérico; los límites de la sección 6 son
    del equipo.
13. **Grano, viñeta, desenfoque y nostalgia; garabatos; texto de vidrio; rebote; cascada:** sin respaldo
    encontrado; son hipótesis.
14. **Efecto Zeigarnik** (lo inacabado se recuerda más): se abrió la página, pero no se comprobó si se ha
    replicado; no se usa.

Lo que el capítulo 11 trae de videos de Instagram sigue siendo hipótesis, como allí se dice; este capítulo no lo
convierte en dato.

## 9. Fuentes

**Abiertas de verdad el 2026-11-23** (descargadas y leídas):

- Wikipedia en inglés, `https://en.wikipedia.org/wiki/<título>`: Depth perception · Looming · Parallax scrolling ·
  Multiplane camera · Focus puller · Orienting response · Habituation · James E. Cutting · Cutting on action ·
  Kuleshov effect · Walter Murch · In the Blink of an Eye (Murch book) · Soviet montage theory · Fast cutting · Shot
  (filmmaking) · Jump cut · Smash cut · Freeze-frame shot · Point-of-view shot · Twelve basic principles of
  animation · Fritz Heider · Biological motion · Mere-exposure effect · Processing fluency · Curiosity · Nostalgia ·
  Reminiscence bump · Self-reference effect · Viral phenomenon · Von Restorff effect · Peak–end rule · Surprise
  (emotion) · Startle response · Theories of humor · Awe · Cuteness · Mickey Mousing · Michel Chion · Vignetting ·
  Film grain · Whiteboard animation · Photosensitive epilepsy · Harding test · Graham Harding · Dennō Senshi
  Porygon · Web Content Accessibility Guidelines · Motion sickness · Virtual reality sickness · Useful field of
  view · Presbyopia · SpongeBob SquarePants · Blue's Clues · Psychocinematics · Zeigarnik effect.
- Ayuda de YouTube: https://support.google.com/youtube/answer/72851?hl=en (Programa de socios) ·
  https://support.google.com/youtube/answer/9314415?hl=en (retención) ·
  https://support.google.com/youtube/answer/12942217?hl=en (consejos de la pestaña Contenido).
- Google para desarrolladores: https://developers.google.com/youtube/analytics/metrics (métricas).
- Ayuda de accesibilidad de Android: https://support.google.com/accessibility/android/answer/11183305?hl=en
  («Remove animations»).
- Del propio estudio: `manual/01`, `02`, `03`, `04`, `07`, `11`, `13`; `infantil/guia_1_a_3.md`;
  `canales/nostalgia-tin-y-tan/DESIGN.md` y `plan_programa_de_socios.md`; `herramientas/efectos.py`;
  `estadisticas/datos/2026-11-23_TIN-EN-S-001_48h.md`.

**Vistas solo en resumen de buscador el 2026-11-23** (no abiertas):

- Smith (2012), *Projections* 6(1): https://ualresearchonline.arts.ac.uk/id/eprint/21187/
- Lillard y Peterson (2011), *Pediatrics* 128(4): https://pmc.ncbi.nlm.nih.gov/articles/PMC9923845 · revisión de
  2024: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11044375/
- WCAG 2.3.1: https://www.w3.org/WAI/WCAG21/Understanding/three-flashes-or-below-threshold · WCAG 2.3.3:
  https://w3.org/WAI/WCAG21/Understanding/animation-from-interactions
- Cutting, DeLong y Nothelfer (2010): https://www.psychologicalscience.org/journals/psychological-science/0956797610361679/
- Lang, Geiger, Strickwerda y Sumner (1993), citado en https://sas-space.sas.ac.uk/6561/1/Heimann%20et%20al%202016.pdf
- Tremoulet y Feldman (2000): https://journals.sagepub.com/doi/10.1068/p3101
- Owsley y otros (1983), citado en https://pmc.ncbi.nlm.nih.gov/articles/PMC3049199
- Material Design (guías antiguas): https://m1.material.io/motion/duration-easing.html ·
  https://m2.material.io/go/design-easing
