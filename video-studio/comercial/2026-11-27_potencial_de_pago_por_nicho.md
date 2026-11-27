# Potencial de pago por nicho y calificación de los temas de diciembre · Tin & Tan

- **Autor:** experto en monetización de canales y redes.
- **Fecha:** 2026-11-27. Todas las páginas se leyeron el **2026-11-26** (hora de El Salvador), salvo que la fila diga otra cosa.
- **Encargo:** regla del dueño (`REGLAS_CEREBRO.md`, última sección), textual: «Considero que la selección de tema también debe estar basada en nichos con potencial de monetización de medio a mayor; definí eso en términos de potencial de pago con base a casos documentados de YouTube».
- **Qué es:** estimación con rangos. **No es promesa de ingreso ni asesoría fiscal o financiera.** Hoy el canal cobra US$0: no está en el Programa de socios.
- **Marcas de evidencia:** **[YT]** página oficial de YouTube o Google · **[creador]** cifra propia que el creador dio a un medio o publicó · **[agregado]** medición de un tercero sobre datos de Analytics de muchos canales, sin auditar · **[tercero]** estimación de un vendedor de herramientas (vidIQ, FluxNote, etc.): sirve de referencia, **no cuenta como caso documentado** · **[supuesto]** deducción mía.
- **Datos del canal:** se describen en palabras; las cifras exactas de Studio no van a este repositorio público.
- Las cuentas se hicieron con un script de Python el 2026-11-26 (no de cabeza).

---

## 1. Cómo se paga de verdad, por formato

### 1a. Shorts

| Hecho | Evidencia | Fuente y fecha |
|---|---|---|
| Los anuncios que corren **entre** Shorts en el feed se suman cada mes en un fondo: «revenue from ads running between videos in the Shorts Feed gets added together» | [YT] | https://support.google.com/youtube/answer/12504220?hl=en (2026-11-26) |
| Ese fondo se asigna al «Creator Pool» según vistas comprometidas y uso de música: «allocated into the Creator Pool based on engaged views and music usage». Con música, la parte de esas vistas se reparte con los sellos según el número de pistas | [YT] | misma |
| A cada creador le toca su parte de vistas **por país**: «based on their share of total engaged views from monetizing creators' Shorts in each country» | [YT] | misma |
| El creador se queda con el **45 %** de lo asignado, «regardless if music was used or not» | [YT] | misma |
| Solo cuentan vistas de contenido apto para anunciantes | [YT] | misma |
| Desde el 1-feb-2027, para cobrar del fondo cada mes hacen falta 10 millones de vistas calificadas de Shorts en 90 días; y los anuncios dirigidos a 5 canales o menos pagan 45 % directo | [YT] | https://support.google.com/youtube/answer/12504220?hl=en y https://support.google.com/youtube/answer/12843009?hl=en (base_conocimiento §7, 2026-11-20) |

**¿Cambia el nicho lo que cobra un Short? No, de forma directa.** La página oficial no menciona tema, categoría ni demanda del anunciante en el reparto (lo comprobé el 2026-11-26): el anuncio no va pegado a tu Short, va en el feed, y el dinero se reparte por tu parte de vistas dentro de cada país. Un Short de finanzas y uno de GTA 6, con las mismas vistas desde los mismos países y sin música de sellos, cobran lo mismo.

El nicho sí lo mueve por tres caminos indirectos:
1. **De qué países llegan las vistas.** Cada país tiene su fondo. Si un tema atrae más vistas de India o Filipinas que de EE. UU., cada vista vale menos. YouTube no publica el valor de cada fondo; el orden entre países sale de datos de todos los formatos (1c) [supuesto].
2. **Música de sellos.** Reduce la parte del fondo que te toca. Tin & Tan usa sonido propio: no aplica mientras siga así.
3. **Apto para anunciantes.** Un tema que no lo sea paga cero en esa vista.
4. **Desde el 1-feb-2027**, los anuncios dirigidos a pocos canales pagan directo. Ahí el nicho podría empezar a pesar. No hay dato de cuánto.

**Cuánto paga un Short por mil vistas (RPM), casos declarados:**

| Caso | Nicho | Cifra declarada | RPM resultante (script) | Evidencia | Fuente |
|---|---|---|---|---|---|
| Brooke Monk, 1.ª semana del reparto (feb-2023) | sin dato | £768,41 por 64,5 M de vistas | £0,012 | [creador] vía Digiday, 2023-03-14 | https://digiday.com/marketing/youtube-shorts-ad-payouts-to-creators-highlights-deeper-monetization-woes/ |
| Riley Lemon, un mes | sin dato | US$383,13 por 7 M de vistas | US$0,055 | [creador] vía Business Insider (copia en Yahoo, actualizada 2023-09-14) | https://ca.news.yahoo.com/much-money-youtube-pays-1-120000576.html |
| Siete creadores sin nombre en el mismo artículo | varios | US$0,04-0,06 | — | [creador] vía BI | misma |
| Maddie Borge, Shorts con 10 M de vistas | estilo de vida | US$385 (US$373 del fondo de Shorts) | US$0,0385 | [creador] vía LADbible, 2024-09-19; no consta captura | https://www.ladbible.com/entertainment/youtube/influencer-maddie-borge-10-million-views-money-made-449665-20240919 |
| Maldhound | cartas «Magic: The Gathering» | US$0,18 | — | [creador] vía Digiday, 2025-02-25 | https://digiday.com/media/how-youtube-shorts-revenue-compares-to-long-form-video-revenue-for-creators/ |
| LordDraconical | sin dato | ≈ US$0,20 | — | [creador] vía Digiday | misma |
| Bennett Santora, varios canales de Shorts | malabares y finanzas personales | US$0,15-0,30 | — | [creador] vía Digiday | misma |
| Matt Steffanina | baile | ≈ US$0,18 | — | [creador] vía Digiday | misma |
| vidIQ: «US$0,03-0,10» en general | — | — | — | [tercero] | https://vidiq.com/blog/post/youtube-shorts-monetization/ (base del 2026-11-21) |

Lectura: los casos van de **US$0,01 a 0,30 por mil**. El rango sube con los años (2023: 0,01-0,06; 2025: 0,15-0,30), y dentro del mismo año **finanzas (0,15-0,30) y baile (0,18) quedan a la par**. Eso coincide con el mecanismo oficial: lo que manda es el país y el año, no el nicho. Con seis casos no se puede probar, pero tampoco hay ninguno que lo contradiga.

**Cuánto dejaría el umbral de 10 M de vistas** (después de entrar; antes, US$0):

| Escenario | RPM de Shorts | 10 M de vistas comprometidas |
|---|---|---|
| Cero (fuera del Programa, o vistas antes de aceptar el módulo de Shorts) | 0 | **US$0** |
| Bajo (Borge, 2024) | US$0,0385 | US$385 |
| Medio (Lemon, 2023) | US$0,055 | US$547 |
| Alto (Digiday, 2025) | US$0,18 | US$1.800 |
| Techo (Santora, 2025) | US$0,30 | US$3.000 |

### 1b. Video largo

- El creador recibe el **55 %** de los anuncios de la página de reproducción [YT] (https://support.google.com/youtube/answer/72902?hl=en, base del 2026-11-20). **Aquí el nicho sí pesa:** el anuncio se vende contra ese video y su público, y los anunciantes pagan distinto por cada tema.
- **Ojo, RPM no es CPM.** El CPM es lo que paga el anunciante por mil impresiones de anuncio, antes del reparto. El RPM es lo que recibe el creador por mil vistas, después del reparto y contando las vistas que no llevan anuncio. No se convierte uno en el otro multiplicando por 0,55: no todas las vistas muestran anuncio.
- Casos declarados de RPM de video largo:

| Caso | Nicho | RPM de video largo | Evidencia | Fuente |
|---|---|---|---|---|
| Josh Mayo | finanzas personales | US$29,30 (oct-2022). Un año antes, con menos finanzas, ≈ US$6 | [creador] vía BI (Yahoo, 2023-09-14) | https://ca.news.yahoo.com/much-money-youtube-pays-1-120000576.html |
| Ocho creadores del mismo artículo | varios | US$1,61-29,30 | [creador] vía BI | misma |
| Maldhound | cartas «Magic» (videos de 20-30 min) | ≈ US$5,50 | [creador] vía Digiday, 2025-02-25 | https://digiday.com/media/how-youtube-shorts-revenue-compares-to-long-form-video-revenue-for-creators/ |
| LordDraconical | sin dato | ≈ US$3,33 | [creador] vía Digiday | misma |
| Seis creadores de Digiday | varios | US$3-6 en video largo y menos de US$0,20 en Shorts | [creador] vía Digiday | misma |

- **Medición agregada por nicho:** AIR Media-Tech, 300 canales, 3.595 meses-canal monetizados, may-2025 a may-2026, datos de YouTube Analytics. Publica medianas. No dice si incluye Shorts ni da países [agregado]. Página actualizada el 2026-07-01: https://air.io/en/air-data-findings/how-much-does-youtube-really-pay-in-2026-real-rpm-data-from-300-channels (leída el 2026-11-26).

| Nicho (AIR) | RPM mediana | Cuartiles P25-P75 | CPM mediana en Studio |
|---|---|---|---|
| Educación y ciencia | US$10,22 | 2,31-19,50 | US$5,91 |
| Transporte (menos de 10 canales) | 5,69 | 3,17-9,81 | 5,88 |
| Estilo de vida | 2,98 | 1,77-5,24 | 5,32 |
| Noticias y política (menos de 10) | 2,60 | 1,79-3,62 | 4,51 |
| Entretenimiento | 2,43 | 0,88-5,02 | 3,98 |
| Manualidades | 2,39 | 1,00-3,90 | 3,42 |
| Gadgets y tecnología | 2,33 | 0,70-3,71 | 5,73 |
| Música | 2,28 | 1,35-4,16 | 4,05 |
| Comida (menos de 10) | 2,25 | 1,50-3,11 | 4,04 |
| Videojuegos | 2,05 | 0,70-3,62 | 4,05 |
| Negocios y finanzas (menos de 10) | 2,01 | 0,73-5,17 | 4,84 |
| Salud y deporte | 1,23 | 0,72-1,53 | sin dato |
| Niños y adolescentes | 0,33 | 0,16-0,88 | sin dato |

  Dos lecturas de AIR que importan: (1) **dentro de un nicho la diferencia es mayor que entre nichos** (en negocios y finanzas, el cuartil alto gana 7,1 veces lo que el bajo); (2) **finanzas aparece abajo**, en contra de lo que dicen casi todas las guías, aunque con una muestra chica. Por eso aquí no se toma una sola cifra: se combina el CPM, que mide lo que paga el anunciante, con el RPM y los casos de creadores.
- **Estacionalidad** [agregado, AIR, misma página]: la mediana mensual sube hasta noviembre (US$2,35) y cae en enero (US$1,56): **34 % menos que noviembre y 26 % menos que diciembre**. La prima del cuarto trimestre cambia por nicho: finanzas +60 %, comida +39 %, música +21 %, tecnología +13 %, educación +11 %, videojuegos +9 %, entretenimiento +4 %. Para Shorts no hay dato estacional.
- **Referencia de tercero, no caso:** vidIQ (2026-04-20, revisada 2026-05-29) da CPM de finanzas US$15-50 y RPM de US$5-17; tecnología de consumo US$5-12 de CPM; software B2B US$10-30; IA US$10-25; videojuegos US$4-15; entretenimiento y vlogs US$2-8; educación US$8-20; música ≈ US$1-3. Dice que sus rangos son «directional». https://www.vidiq.com/blog/post/most-profitable-youtube-niches

### 1c. País y edad del público

| Factor | Dato | Evidencia | Fuente |
|---|---|---|---|
| EE. UU. | RPM US$4,70 | [agregado] Dynamoi, cuentas conectadas, 2025-11-24 a 2026-11-23. No dice qué parte es Shorts, largo o música | https://dynamoi.com/data/youtube-adsense-rpm (2026-11-26) |
| Filipinas | US$0,62 | [agregado] misma | misma |
| India | **sin dato medido**: no está entre los 83 mercados publicados | — | misma |
| Promedio global | US$1,05 | [agregado] misma | misma |
| Shorts por país | YouTube reparte por país, pero **no publica cuánto vale cada fondo**: sin dato | [YT] | 12504220 |
| Menores de 18 | En cuentas de menores de 18 Google no permite anuncios personalizados y restringe las categorías sensibles; vale para YouTube | [YT] | https://support.google.com/adspolicy/answer/12205906?hl=en (2026-11-26) |

- **Mezcla supuesta para un futuro video largo:** 50 % EE. UU., 15 % Filipinas, 15 % India y 20 % otros al promedio global. Los porcentajes son supuestos: el dueño dijo «cerca de la mitad» para EE. UU. y que siguen Filipinas e India. Con India entre 0 y 0,62, el RPM da **US$2,65-2,75**, antes de descontar edad y nicho.
- **Efecto de la edad:** Google lo dice en lo cualitativo, pero no publica cuánto baja el pago. **Sin dato.** Como el canal tiene un tramo grande de 13 a 17, el escenario bajo se ancla por debajo del promedio global (≤ US$1,05) [supuesto, regla propia]. En Shorts la página oficial solo nombra país y música; no dice si la edad cambia el reparto. Sin dato.

**Escenarios de RPM de video largo para Tin & Tan** (supuestos, no pronóstico):

| Escenario | RPM | Por 100 mil vistas de video largo |
|---|---|---|
| Cero (fuera del Programa) | 0 | US$0 |
| Bajo (público joven, nicho bajo) | US$1,05 | US$105 |
| Medio (mezcla de países, nicho medio) | US$2,70 | US$270 |
| Alto (nicho alto: mediana de educación y ciencia en AIR, con público de EE. UU. en la mitad) | hasta US$10,22 | hasta US$1.022 |

### 1d. Lo que no depende del anuncio

| Vía | ¿Aplica a Tin & Tan hoy? | Fuente |
|---|---|---|
| **YouTube Creator Partnerships** (antes BrandConnect): pide 18 años o más, estar en el Programa, vivir en un país de la lista y no tener avisos | **No.** El Salvador no está en la lista (sí EE. UU., Filipinas, India y México) | [YT] https://support.google.com/youtube/answer/9385307?hl=en (2026-11-26) |
| Afiliado de YouTube Shopping | **No.** Pide estar en el Programa y El Salvador no está en la lista | [YT] base del 2026-11-21, https://support.google.com/youtube/answer/13376398?hl=en |
| Amazon Associates | **Sin verificar.** La página de programas internacionales no tiene uno de El Salvador; falta ver si un residente salvadoreño puede inscribirse en el de EE. UU. | https://affiliate-program.amazon.com/help/node/topic/GCE3F2NCVZLDFM6A (visto en resumen del buscador, sin abrir) |
| Patrocinio directo con una marca, fuera de YouTube | Posible en teoría. **No encontré ningún caso documentado de tarifas para un canal nuevo**: sin dato. Aquí sí pesa el nicho: las marcas de tecnología, software y finanzas compran público de su tema, y las guías que lo afirman son de terceros | — |
| Membresías y Super Thanks (nivel intermedio: 500 suscriptores y 3 M de vistas de Shorts) | Sí, cuando se llegue. No dependen del nicho del anuncio | [YT] https://support.google.com/youtube/answer/13429240?hl=en (base del 2026-11-20) |

Conclusión: para un canal de este tamaño y país, patrocinios y afiliados valen **cero hoy**. El nicho importa para ellos más adelante, cuando haya suscriptores de un tema que una marca quiera comprar.

---

## 2. Tabla de nichos

**Criterio de niveles (definido aquí, con números):** se usan dos indicadores de AIR (mediana de video largo) y los casos de creadores.

- **CPM en Studio:** alto si es de US$5,50 o más; medio entre US$4,50 y 5,49; bajo por debajo de US$4,50.
- **RPM:** alto si es de US$5 o más; medio entre US$2,50 y 4,99; bajo por debajo de US$2,50.
- **ALTO:** al menos un indicador alto y ninguno bajo, **o** un caso de creador documentado con RPM de US$10 o más.
- **MEDIO:** indicadores mezclados (uno alto y otro bajo), o los dos medios.
- **BAJO:** los dos indicadores bajos y ningún caso que lo contradiga.

Este criterio vale para el **video largo y los patrocinios**. Para el pago de un Short no cambia nada (1a).

| Nicho | Nivel | Respaldo | Solidez |
|---|---|---|---|
| Finanzas y dinero | **ALTO** | Josh Mayo, US$29,30 (BI, 2023); vidIQ, RPM de US$5-17 [tercero]; prima de fin de año +60 % (AIR). **En contra:** la mediana de AIR (US$2,01) sale de menos de 10 canales | Media: un solo caso de creador con nombre. **Riesgo propio:** YouTube no monetiza personajes de IA que se presenten como expertos en finanzas (1311392, base §3). Tin y Tan son dibujos, no un experto humano, pero hay que cuidarlo |
| Ciencia y educación | **ALTO** | AIR: RPM US$10,22 y CPM US$5,91. vidIQ: educación US$8-20 de CPM [tercero] | Media: dato agregado, sin caso de creador con nombre |
| Software e IA | **MEDIO (provisional)** | AIR no tiene esta categoría. vidIQ: IA US$10-25 y software B2B US$10-30 de CPM [tercero] | Baja: no hay caso. Si el tema es software para trabajo o empresas tiende a alto; la IA explicada al público general, sin dato |
| Tecnología de consumo (teléfonos, consolas, hardware) | **MEDIO** | AIR: CPM US$5,73 (alto) y RPM US$2,33 (bajo); prima +13 %. vidIQ: US$5-12 [tercero] | Media |
| Estilo de vida | **MEDIO** | AIR: CPM US$5,32 y RPM US$2,98 | Media |
| Noticias y actualidad | **MEDIO** (en el borde) | AIR: CPM US$4,51 y RPM US$2,60, con menos de 10 canales | Baja |
| Cine y entretenimiento | **BAJO** | AIR: CPM US$3,98 y RPM US$2,43; prima +4 %. vidIQ: US$2-8 [tercero] | Media |
| Videojuegos | **BAJO** (MEDIO si el tema es hardware para jugar) | AIR: CPM US$4,05 y RPM US$2,05. Maldhound, cartas: US$5,50 (Digiday 2025). vidIQ: «esports and hardware pay better than let's plays» [tercero] | Media |
| Música | **BAJO** | AIR: CPM US$4,05 y RPM US$2,28. vidIQ: ≈ US$1-3 [tercero] | Media |
| Deporte | **BAJO** | AIR (salud y deporte): RPM US$1,23; CPM sin dato | Baja |
| Estacional (Navidad, Año Nuevo) | **No es un nicho:** toma el nivel de su tema (una cuenta regresiva es entretenimiento: BAJO) | Pesa la fecha: noviembre es el pico y enero cae 34 % (AIR) | Media |
| Contenido para niños y adolescentes | **BAJO** | AIR: RPM US$0,33 | Media. Aviso para el tramo de 13 a 17 |

---

## 3. Calificación de los temas propuestos

La columna «demanda medida» repite solo lo que el equipo ya midió. Donde no hay dato, dice «sin dato».

| Tema | Nicho (corregido) | Nivel | Por qué | Demanda medida |
|---|---|---|---|---|
| What is GTA 6? | Videojuegos | BAJO | Videojuego, no hardware | **Alta:** hoy domina la búsqueda de YouTube en EE. UU. |
| Is GTA 6 coming to PC? | Videojuegos con puente a hardware de PC | BAJO, MEDIO si se habla de requisitos o piezas | Puede pasar a tecnología | Sin dato propio; arrastra la de GTA 6, falta medir esta pregunta |
| When is Spotify Wrapped 2026? | Música y apps | BAJO | Es música, aunque la app sea tecnología | Sin dato |
| The Game Awards, previa y resultado | Videojuegos y entretenimiento | BAJO | — | Sin dato |
| How big is the universe? | Ciencia y educación | **ALTO** | El nicho con mejor mediana en AIR | Estable, pero la más baja de las cinco (iphone > ps5 = marvel > xbox > universe) |
| PS5 Pro vs PS5 | Tecnología de consumo (consolas) | MEDIO | Compra de hardware | Estable: ps5, segundo puesto |
| Avengers: Doomsday y Dune: Part Three el mismo día | Cine | BAJO | — | Sin dato de esta pregunta. «marvel» está estable, pero es otro término |
| iPhone 18 vs iPhone 17 | Tecnología de consumo (teléfonos) | MEDIO | — | **La mayor de las estables:** iphone |
| Navidad, cuenta regresiva | Estacional y entretenimiento | BAJO | Sale en el pico de fin de año, pero el nicho es bajo | Sin dato |
| What is the Xbox Ally? | Hardware de juegos | MEDIO | Es hardware, no un juego | Estable: xbox, cuarto puesto |
| What is Marvel Rivals? | Videojuegos | BAJO | — | Sin dato propio; «marvel» es otro término |
| Año Nuevo, cuenta regresiva | Estacional y entretenimiento | BAJO | Además sale cuando el RPM de enero es el más bajo del año | Sin dato |
| *Reserva:* precios de la RAM y hardware de PC | Tecnología de consumo | MEDIO | — | **Cero:** las preguntas de RAM pesan cero |
| *Reserva:* finanzas personales y dinero cotidiano | Finanzas | ALTO | Hay que cuidar la regla de personajes de IA que hablan de finanzas | Sin dato |
| *Reserva:* inteligencia artificial explicada | Software e IA | MEDIO (provisional) | — | Sin dato |
| *Reserva:* cómo paga YouTube | Negocios y dinero en línea | ALTO (evidencia débil: AIR negocios y finanzas con muestra chica, OutlierKit [tercero]) | Atrae a creadores, no a gamers | Sin dato |

---

## 4. Regla de decisión

**Dicho sin adornos:** mientras el canal sea solo de Shorts, el nicho **casi no cambia el ingreso**. Hoy el ingreso es US$0, y después de entrar un Short paga según sus vistas y el país de quien mira, no según su tema (12504220). La entrada se gana con vistas calificadas y suscriptores, y eso lo pone la demanda. **El criterio de pago importa para el video largo, para los patrocinios y para el tipo de suscriptor que se junta:** quien se suscribe por un Short de iPhone es el público de un futuro video de tecnología; quien llega por GTA es el de uno de videojuegos. Esto último es un supuesto razonado, sin medir.

Regla en cinco pasos:

1. **Primero la demanda.** Sin demanda medida, el tema no entra. La excepción es una fecha conocida, que se revalida la semana de publicar.
2. **Con demanda parecida** (dentro del doble una de otra en el mismo tablero), **gana el nicho de mayor nivel**.
3. **Demanda alta y pago bajo** (GTA 6, Game Awards): **se hace como Short y se dice por qué**: «demanda X; pago bajo; se elige por vistas hacia el umbral». No pasa a video largo salvo que tenga puente a un nicho medio o alto (GTA 6 en PC: requisitos y piezas).
4. **Demanda baja y pago alto** (universo, finanzas sin dato): **no ocupa el lugar de un Short de crecimiento**. Se guarda para el video largo, que es la doble página, o se busca dentro del nicho la pregunta que sí tenga demanda.
5. **Cupo de siembra** [supuesto, propuesta mía]: de cada tres Shorts de la tanda, al menos uno de nivel medio o alto cuando haya uno con demanda comparable. Así, cuando se abra el video largo, ya habrá suscriptores de un nicho que paga. Se ajusta con suscriptores por mil vistas en Studio.

Con esta regla, diciembre queda así: iPhone 18 vs 17, PS5 Pro y Xbox Ally (demanda medida y nivel medio) suben de prioridad. GTA 6 se queda por demanda. El universo pasa a candidato del primer video largo. Spotify Wrapped, Marvel Rivals, Game Awards, cine y las cuentas regresivas solo entran si una lectura nueva de demanda lo justifica.

---

## 5. Lo que no pude confirmar y qué lo resolvería

| Pendiente | Qué lo resuelve |
|---|---|
| Cuánto vale el fondo de Shorts por país (EE. UU., Filipinas, India) | YouTube no lo publica. Lo resuelve el RPM de Shorts por país en Studio, cuando el canal cobre |
| Cuánto baja el pago el público de 13 a 17 | Google no da la cifra. Studio, por video, cuando haya video largo monetizado |
| RPM de India | Dynamoi no la publica. Studio |
| Casos de creadores con nombre para tecnología, ciencia, cine, música y deporte | Business Insider está bloqueado para mi lector y su copia en India no respondió. Hay que abrir a mano las series «how much YouTube pays» de BI o buscar videos de ingresos de creadores de cada nicho con captura de Studio |
| Si AIR incluye Shorts y qué países tiene | AIR no lo dice; hay que preguntarles o encontrar su método completo |
| Por qué finanzas sale baja en AIR (menos de 10 canales) frente al caso de US$29,30 | Una muestra más grande o casos de 2025-2026 con captura |
| Ali Abdaal (educación y productividad): «US$4-10» por mil en su blog | Solo lo vi en el resumen del buscador; su página dio 403. Sin verificar |
| Si un residente salvadoreño puede usar Amazon Associates de EE. UU. | Página de inscripción oficial de Amazon |
| Tarifas de patrocinio para un canal nuevo | No hay caso documentado: sin dato |
| Cuánto pesará el nicho en Shorts con los anuncios directos de febrero de 2027 | Sin dato hasta que YouTube publique detalles o haya casos |
| Demanda de Spotify Wrapped, Game Awards, Marvel Rivals, el cine y las cuentas regresivas | Una lectura de Trends o del autocompletado del equipo de demanda |
