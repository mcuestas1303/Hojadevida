## 4. Actuación y coreografía — director-de-animacion

> Escrita el 2026-11-27 por el director de animación sobre `02_prompt/direccion.md` (secciones 1, 2, 8, 9 y 10 del
> director creativo; pedido de la sección 4), `perfil_emocional.md` y el `00_brief.md`. Texto listo para pegar en lugar de
> la sección 4 abierta. Todo por código con el motor de acción: **no hay clip propio ni transferencia de movimiento.**
>
> **Convenciones.** 1080×1920, 30 f/s. «f» = fotograma desde el inicio; «c» = desde el final; «K» = fotograma de contacto.
> Los fotogramas siguen el plan con la **voz estimada** de 2.2 y se recalculan con la voz real; lo que no se mueve al
> recalcular: las reglas de 2.1, la gramática de 4.1 y la regla «el golpe cae 2 f antes de la voz de Tin» (la línea de
> Tin empieza en K +2). Sellos de `manual/14`: (investigación), (oficio), (hipótesis del equipo); **toda dosis sin sello
> es (hipótesis del equipo)**. Lo medido en el short 4 va con su fuente.
>
> **Lo medido y lo no medido.** Las distancias en «u» (unidad del motor) de este texto son **propuestas de coreografía**,
> no medidas del motor: el patio no existe todavía y no sé cuánto vale R (radio de cabeza) en u. Cada posición se fija al
> construir el entorno y se comprueba con `SECO=1 node render.js …` y `control_encuadre.py`. Lo que hay que medir está
> marcado **(pendiente)** y reunido en 4.16.

### 4.0 Lo que leí y lo que respeto

- **Fichas y bitácora.** `@tin` y `@tan`: Tin responde con datos, Tan pregunta y se asombra; no cambian colores, gorra,
  lentes, rodete ni bufanda; los gestos del canal son los de la ficha (el lápiz es de Tin; en la firma lo toma prestado
  Tan, y solo ahí). **La bitácora «No va»:** los nombres Tiky y Lumi y clonar a «Doodle Digest»; ninguno aparece. El banco
  de gestos de `manual/04` no trae a Tin ni a Tan: no hay gesto propio que respetar más allá de la ficha, y **no le pongo
  a nadie el gesto de otro**. `@duda`: sin nombre ni voz ni boca, sin dientes, garras, cuernos ni pupilas, **sin color
  propio** (el acento del video no la pinta; lo chamuscado es gris de ceniza, nunca rojo), sin sangre, nunca da miedo ni
  muere, se borra y por eso puede volver. Armas dibujadas con tinta: aprobadas (A12); **ninguna de fuego**. La ficha del
  rival dice «no lleva armas»: la corrigió el dueño el 2026-11-26; aquí el rival dibuja un paquete, no un arma.
- **Revisiones del short 4 (v2, v3, v4).** Sus defectos están convertidos en la lista de comprobación de 4.15.
- **Hojas.** Los paneles de expresión salen de `personajes/tin/referencias/expresiones.png` y de la hoja de Tan
  (`feliz, nostalgia, curiosidad, pensando, concentrado, sorpresa, risa, eureka`) y de `personajes/duda/referencias/
  hoja_v2_2026-11-26.png` (frente, perfil, espalda, guardia, crecida, golpe, patada, recibe, caído, borrándose).
  **Aviso:** `concentrado` de Tin lleva cejas bajas e inclinadas y se lee como enojo. Se usa solo en las pausas de 6 f,
  nunca en un dato; para la cara de póquer de los datos va `pensando` (boca recta, mirada al lado).
- **No narra nada del universo:** la grieta, la rasgadura, el telescopio, la marca y la salida no tienen mirada ni gesto
  de nadie salvo el de Tan de 6 f que pide el director creativo.

### 4.1 La gramática de cada golpe (tiempos medidos por Keter, a 30 f/s; se copian los tiempos, no los dibujos)

Fuente: `estudios/2026-11-26_referencias_de_pelea_estudio_de_keter.md`, secciones 3 y 7 (investigación, medido).

| Fase | Fotogramas | Qué se ve |
|---|---|---|
| Anticipación | K −12 a K −7 (6 f) | Movimiento contrario al golpe, con frenada (curva de salida suave, nunca lineal) |
| **Pausa** | K −6 a K −1 (6 f) | Pose de carga casi quieta; el trazo del rival «hierve», nada más; sin efectos de sonido |
| **Contacto = pausa de impacto** | K y K +1 (2 f) | Salto de posición y arco de borrón del color de quien golpea (Tin naranja, Tan verde azulado, rival tinta). Estrella ≤ 0,6 u que nace en el punto real (`contacto()`) y 5 a 7 gotas de tinta. Los dos cuerpos quedan quietos esos 2 f: solo se mueve el borrón |
| Lanzamiento | K +2 a K +5 (4 f) | El golpeado sale con 3 calcos translúcidos; el golpeador ya inicia su recuperación |
| Vuelo y desaceleración | 6 a 15 f | Flota o gira frenando; el reloj baja a 0,25–0,5 (cámara lenta del dibujo, no de la voz) |
| Choque | 2 f | Cuerpo contra el mundo; los choques grandes llevan un corte de 1 f a cuadro de impacto (nunca temblor) |
| Reacción y recuperación | 6 f (golpeador) y 10–16 f (golpeado) | El golpeador vuelve a la guardia; el golpeado se queda mirando lo que rompió, o se levanta solo |
| Sonido | K o K −1 | El golpe suena en el contacto o 1 f antes |
| Voz | K +2 | Tin empieza el dato 2 f después del contacto |

**Excepciones declaradas.** (1) **Golpe 1:** anticipación de 4 f y pausa de 4 f (8 f en vez de 12) y vuelo de 6 f: es «la
respuesta que no se hace esperar» (2.3). Las referencias miden 5 f casi quietos antes del golpe (PIERCE): 4 es el
mínimo que aún se lee. (2) **El bloqueo (f652) y el toque (f700)** no son golpes: no llevan estrella ni gotas ni arco de
borrón; llevan pausa, contacto de 2 f y vibración. (3) **Golpe 4:** el vuelo se comprime a 2 f y la flotación se mueve
**después** del choque (ver 4.3), porque las chispas y el fuego tienen que nacer en ≈ f344.

### 4.2 Mapa del patio: carriles, puntos fijos y quién va por dónde (propuesta; pendiente de medir)

Cámara alta y en diagonal (decisión D22/D23 del short 4, la confirma fotografía): C1 queda abajo en el cuadro y C3
arriba, así que quien va por C1 no tapa el vuelo del rival por C2/C3.

| Carril | Para qué | Regla |
|---|---|---|
| **C1 (frente)** | Tin y Tan cuando no golpean y cuando el rival cruza; Tan en la carrera previa al golpe 2 | Quien cruza por C1 pasa **por delante** del otro, a ≥ 0,4 u de profundidad |
| **C2 (de pelea)** | Todo contacto: **los dos en el mismo carril** (lección B7 del short 4); el rival corre y salta por aquí | Sin decorado que tape las piernas de nadie |
| **C3 (fondo)** | La pila de torres, la grieta, las cajas de la derecha, los monitores, el farol | La pila queda entre C2 y C3: se pasa por delante |
| Pared de fondo | Persiana metálica, pestaña de cartón | El choque contra la persiana es un vuelo **en profundidad** |

| Punto (x de −4,5 a +4,5 u; el ancho del patio es **pendiente**) | Posición propuesta | Qué le pasa |
|---|---|---|
| `pila` (torres + monitor de portada) | x 0, entre C2 y C3 | Golpe 1: pierde una torre (`torre_de_pc_rota`); el monitor se inclina y queda así |
| `grieta` (P-002) | x +1,3, C3, **a la derecha de la pila y a la izquierda de Tin**: el rival no cruza detrás de nadie al nacer | Se queda abierta hasta el final (daño que se queda) |
| `cajas_der` (pila de cartón) | x +2,9, C3 | Golpe 2: se aplastan |
| `monitores` (3 sobre un palé) | x −2,6, C3 | Golpe 3: uno se rompe (`monitor_roto`) |
| `farol` + `cajas_izq` a su pie | farol x −3,5, C3; cajas x −3,1, C2 | Golpe 4: el farol se tuerce 8°; las cajas arden |
| `persiana` | pared de fondo, de x +0,2 a +4,5 | Golpe 5: queda abollada con la silueta del rival |
| `pestana` (P-001/P-004) | pared de fondo, x −1,4 (la zona la fija fotografía; 30 px de despeje al texto) | No se toca; segunda marca en f812 |
| `caja_registradora_rota` (P-003) | extremo izquierdo del suelo, C1, x −4,1 | Quieta desde f0 |
| aterrizaje del telescopio (P-006) | suelo, extremo derecho, C1, x +3,4, **fuera del pasillo de la firma y de la zona de la pelea**; si cae fuera de la zona útil (x 60–960), acercarlo a x +2,6 | Quieto desde f595 |
| borde izquierdo de salida (P-005) | x −4,5, C2 | Sale el resto del rival |

**Vigilar:** E4 del short 4 (el rival sobre la cabeza de Tin o de Tan). En 2D no se resuelve con la distancia en el
mundo sino con la silueta: **ninguna cabeza del rival a menos de 1,2 R de la de Tin o la de Tan en pantalla** salvo en
los vuelos de 2 f. Se mide con `SECO=1` y `control_encuadre.py` (pendiente: el criterio exacto en px).

### 4.3 La pelea golpe por golpe

#### A. Quién, con qué, hacia dónde, contra qué (cada golpe distinto del anterior en las cuatro cosas)

| Golpe · dato (línea) · K | Quién y con qué (cuerpo) | Hacia dónde | Contra qué | Por qué así |
|---|---|---|---|---|
| **1** · «Not announced.» (2) · **f88** | **Tin, empujón con las dos manos al pecho**, sin arma. Distinto del puño de Tin en el short 4 | A la izquierda, por C2, 1,0–1,4 u | `pila` de torres | El más corto y seco: una respuesta no necesita arma. Tin está a la derecha del rival, que nació a la izquierda de él |
| **2** · «Rockstar hasn't announced…» (3) · **f130** | **Tan, embestida de hombro** tras una carrera corta | A la derecha y al fondo | `cajas_der` | Los dos pelean desde el principio. Distinta de la patada giratoria de Tan del short 4 |
| (contraataque, no golpe) · f164–f197 | **El rival salta sobre Tin** con el brazo en zarpazo y falla | Cruza por encima de Tin agachado y aterriza a su izquierda | Nada: aterriza resbalando | «El rival contraataca una vez y falla» (2.3). Lo falla porque Tin lo lee en su pausa |
| **3** · «It's on PlayStation 5…» (4) · **f212** | **Tin, patada frontal con la planta del pie** | A la izquierda y al fondo (profundidad), 2,2 u | `monitores`: se rompe uno | Mete el choque con vidrio y chispas pequeñas; otra parte del cuerpo y otra dirección que el gancho ascendente del short 4 |
| (la torre que cede) · f262 | Nadie: la torre de encima de la rota resbala y cae | Hacia el vacío de la izquierda | Suelo, junto a Tin | La consecuencia llega tarde: causa del golpe 1 |
| **4** · «GTA 5 took…» (6) · **f336** | **Tin, regla de tinta, batazo diagonal ascendente** a dos manos | Arriba y a la izquierda, 1,6 u en horizontal y 1,3 u de altura | `farol` (caja de conexiones a 1,3 u): chispas y fuego en `cajas_izq` | El golpe más fuerte antes del pico; el fuego del fondo se abre aquí |
| **(se la pasan)** · f438–f444 y f532–f537 | Tin lanza la regla a Tan; Tan se la devuelve | Lanzamiento corto bajo la cintura, 1,0–1,4 u | — | «Regla de tinta, única arma dibujada de Tin y Tan (se la pasan)» |
| **5** · «Red Dead Redemption 2…» (8) · **f484** | **Tan, regla, estocada recta** (pierna adelantada, brazo y regla en línea) | **Hacia el fondo, en profundidad**, el vuelo se achica | `persiana`: abolladura con la silueta del rival | Es el único golpe en profundidad pura; Tan golpea con precisión, no con peso |
| **Bloqueo** · f652 (línea 9) | **Tin frena la mano de Tan con la regla** | — | — | El gesto central: se copia (no tocar el paquete) |
| **Toque** · f700 (línea 10) | **Tin, de lejos, con la punta de la regla** | El paquete revienta; el rival sale despedido a la izquierda | El paquete | No es un golpe contra el rival: la trampa le cae a él |
| **6** · «No official PC date…» (12) · **f812** | **Tin, regla, tajo vertical de arriba abajo** | Hacia abajo y adentro (implosión) | El propio rival | El remate no lo borra: lo repliega. Es el único golpe hacia abajo |

#### B. Los fotogramas de cada golpe (gramática de 4.1)

| Golpe | Anticipación | Pausa | Contacto (K, K+1) | Lanzamiento | Vuelo | Choque | Recuperación y reacción |
|---|---|---|---|---|---|---|---|
| **1** Tin | f80–f83 (4 f): peso atrás, manos al pecho | f84–f87 (4 f) | **f88–f89** | f90–f93, 3 calcos | f94–f99 (6 f, reloj 0,5, de frente a la pila) | f100–f101 contra `pila` | Tin: f90–f95 a la guardia. Rival: se encoge a 1,35 (f98–f106), se sienta y **mira la torre rota** f102–f117 |
| **2** Tan | Carrera f106–f123 (18 f); la frenada y el giro del hombro hacia atrás son la anticipación f118–f123 | f124–f129 (hombro adelante, 6 f; **espera a que el rival esté de pie**) | **f130–f131** | f132–f135, 3 calcos | f136–f145 (10 f, reloj 0,35, gira una vez) | f146–f147 contra `cajas_der` | Tan: f132–f137 a la guardia. Rival: a 1,2 (f132–f140); entre cartones f148–f157, de pie f158–f163 |
| *contraataque del rival* | f164–f169 (se echa atrás, 6 f) | f170–f173 (4 f; Tin lo lee y baja) | zarpazo en el aire **f182–f185, sin contacto** | — | salto f178–f189 sobre Tin agachado (f182–f189, hold 8 f) | — | Aterriza f190–f191, resbala f192–f197, se replanta f198–f207 |
| **3** Tin | f200–f205 (dos zancadas y el pie atrás) | f206–f211 | **f212–f213** | f214–f217 | f218–f225 (8 f, reloj 0,5) | f226–f227 contra `monitores` (corte de 1 f) | Tin: f214–f219. Rival: 1,1 (f214–f222); sentado entre el vidrio f228–f239; de pie f240–f251 |
| **4** Tin | f324–f329 (regla atrás y abajo, rodillas flexionadas) | f330–f335 | **f336–f337** | f338–f341, 3 calcos | **f342–f343 (2 f, rápido)**; **flota pegado al poste f346–f351 y cae despacio f352–f363 (12 f, reloj 0,25)** | **f344–f345** contra el farol (corte de 1 f) | Tin: f338–f343. Rival: 1,0 (f338–f346); trepa al farol f364–f395 y se queda abajo del todo agarrado f396–f437 |
| **5** Tan | f472–f477 (peso a la pierna de atrás, regla atrás) | f478–f483 | **f484–f485** | f486–f489 | f490–f499 (10 f, reloj 0,35, **en profundidad, se achica**) | f500–f501 contra `persiana` (corte de 1 f) | Tan: f486–f491. Rival: 0,9 (f486–f494); **resbala por la persiana** f502–f549 (48 f) y se despega f554–f565 |
| **Bloqueo** (Tin) | Carrera con regla f640–f651; frenada f646–f651 | — | **f652–f653** (regla sobre la muñeca de Tan) | — | — | — | Hold de silueta f654–f659; la regla vibra 4 f (±3°); suelta f660–f667 |
| **Toque** (Tin) | f688–f693 (retrocede el torso, brazo y regla al máximo) | **f694–f699** (6 f, voz y efectos en silencio) | **f700–f701** | blast: f704–f707, 3 calcos | rival f708–f719 (12 f, reloj 0,4) | rueda f720–f726; sin choque | Fases de la explosión en 4.5 |
| **6** Tin | f800–f805 (regla arriba, 6 f) | f806–f811 (regla vertical sobre la cabeza) | **f812–f813** (aplasta 1,0 → 0,6 de alto en 2 f) | — | — | — | Implosión f814–f831 (4.5); resto quieto f832–f855 |

**Estrella, gotas y arco.** Todas las estrellas ≤ 0,6 u y 5 a 7 gotas de tinta, excepto el golpe 1 (4 gotas, más seco) y el
golpe 4 (estrella 0,6 u y 7 gotas: es el más fuerte). **Ningún rojo sobre el cuerpo del rival.** Distancia de contacto
(mano o pie a pecho) ≤ 0,36 u, el máximo que midió el control del short 4 (0,23–0,36 u).

**Marcador de avance del rival (2.3) y «crece sin respuesta».** El tamaño baja un escalón con cada dato, **cuando el dato
entra**: 1,5 → 1,35 (f98) → 1,2 (f132–f140) → 1,1 (f214–f222) → 1,0 (f338–f346) → 0,9 (f486–f494) → 0,8 chamuscado (f726) →
resto ≈ 1,5 R (f830). Bajar el escalón se hace aplastando 3 f (permitido: es golpe) y asentando con muelle `POP`. Entre
un golpe y el siguiente **se infla 0,06–0,08** en los 24 f anteriores a la anticipación (ease-in-out, nunca lineal) y se
desinfla con el golpe: la pregunta crece mientras nadie la responde. Nunca pasa de 1,5. **Discrepancia con 2.3:** el
texto del tramo «Respiro 2» dice que el rival está «ya del tamaño de ellos» (1,0), y el marcador dice 0,9 tras la
línea 8: dejo 1,0 hasta f553 y 0,9 desde f554 (se despega ya encogido).

**Nunca da miedo.** Se infla como gato erizado, falla su contraataque, se sienta a mirar lo que rompió, se sacude, tose
humo por el rizo y se vuelve a plantar. Sin dientes, garras ni pupilas. **Nadie lo golpea mientras está caído o sentado:**
Tan frena su carrera (f118–f123) y espera con el hombro quieto hasta que está de pie (f127), y Tin espera a que se
replante (f207).

### 4.4 Lo que hacen los demás entre golpes: nadie clavado

Reglas (de la v3 y la v4 del short 4): **ninguna pose idéntica más de 12 f**; el reposo vivo (`respira`) con **el doble de
amplitud que en la v4** (pendiente: la amplitud de la v4 no la medí; hay que medirla en el código de `vivo`),
**cambio de apoyo cada 18–24 f** y **desfasado 9 f entre Tin y Tan**; la cabeza sigue al rival ±8°. Solo se quedan quietos
donde el guion lo pide: las pausas de 6 f, el hold del bloqueo (f654–f659) y el toque (f694–f699).

| f | Tin | Tan | Rival | Mundo |
|---|---|---|---|---|
| 0–29 | Firma: `parado`, sin lápiz, cabeza 25°, `curiosidad`; saltito en f10 | Firma: brazo (95°, 108°) de 9.1; atrapa en f10 | — | Pestaña y caja rota quietas |
| 30–45 | Gira la cabeza a la grieta (3 f) y da medio paso atrás, a la izquierda | Mirada a la grieta en f32; interrumpe la mano de `pregunta` | **Entrada por la grieta (4.4a)** | Polvo con contorno, 3 partículas |
| 46–69 | Se adelanta a su carril (2 pasos de 0,4 u, uno cada 8 f): `camina` | Retrocede hacia la izquierda 2 pasos de 0,4 u (f46–f62) con `sorpresa`; se recompone f62–f69 | Crece de 1,25 a 1,5 (24 f) | — |
| 70–79 | Planta los pies; `curiosidad` → `concentrado` (f80) | `sorpresa` → guardia | El rizo se inclina hacia Tan (8 f): acción secundaria | — |
| 88–117 | Golpe 1 | Hold de guardia con cambio de apoyo en f101 | Golpe 1; sentado f102–f117 | `torre_de_pc_rota` f100–f101 |
| 118–147 | Ya salió por C1 al flanco (f94–f111, 1,5 u) y no estorba la trayectoria del golpe 2; cambio de apoyo f120 | Golpe 2 (carrera f106–f123) | Se levanta f118–f127; vuelo y choque | `cajas_der` rotas |
| 148–207 | Pasa a C2 y se planta f158–f163; baja y esquiva f174–f189; dos zancadas f192–f205 | Recuperación f132–f137 y **camina a C1 izquierda** (3 pasos, f138–f160); sigue al rival con la cabeza | Se levanta f158–f163; contraataque; se replanta | — |
| 208–261 | Golpe 3 (f212); recupera f214–f219; **camina 0,8 u al frente del rival que se levanta** f226–f258 | **Esquiva el trozo de monitor** (f230–f237): salta atrás 0,3 u | Sentado f228–f239; de pie f240–f251; camina hacia Tan 1,0 u f254–f270 | `monitor_roto` f226–f227; trozo vuela f228–f236 |
| 262–295 | **Esquiva la torre que cae** (paso atrás de 0,4 u, f262–f270); `pensando`; cambio de apoyo f282 | **Camina a su sitio junto a Tin** (f270–f301, 2,0 u, `camina`); cambia la cara a `curiosidad` en f290 | Se planta; se infla 1,1 → 1,18 (f270–f294) | Torre cae f262–f270 |
| 296–329 | **Dibuja la regla** (f296–f321, plano de detalle; 4.6); anticipa f324 | Pregunta «How long last time?» (f302–f328): `pregunta`, cabeza ladeada 8° | Se acerca y se detiene a 1,1 u de Tin al ver la regla (f300–f323) | — |
| 330–437 | Golpe 4 (f336); recupera; **mira arriba al rival (cabeza +25° máx.)** f344–f400; gira la regla un cuarto de vuelta f380–f392; **a C1 en f436** | `sorpresa` y medio paso atrás (f344–f349); `curiosidad`; **camina 0,8 u hacia el centro** f364–f437 | Choque; pegado al poste; cae despacio; **trepa al farol** y se agarra con el rizo temblando | Chispas f344–f349; llama f346; humo f358 |
| 438–471 | **Lanza la regla a Tan** (f438–f441) y queda en guardia con el lápiz | **Recibe la regla en f444 mientras camina** (0,8 u) y dice la invitación con `invita` (la regla queda en la otra mano); **no mira a cámara** | **Baja del farol** (f438–f449, 1,3 u) y **corre por C2** hasta frente a Tan (f448–f471, 4,4 u, ≈ 5,5 u/s) | — |
| 472–553 | Dice la línea 8 caminando 0,3 u al centro; **recibe la regla** (f532–f537); la sostiene horizontal («mide», f538–f553) | Golpe 5; recupera; **devuelve la regla** a Tin (f532–f536) | Choque; resbala por la persiana; **se despega** f554–f565 | Persiana abollada; caja ardiendo cae y **la llama crece a 1,5** (f500–f511) |
| 554–599 | Reposo vivo; cabeza fija en el rival (**Tin no mira el telescopio**) | Reposo vivo; **mirada de 6 f al telescopio** (f588–f593) | **Camina a la izquierda** 3,3 u (f567–f595); sin gesto hacia el objeto | **Telescopio** f576–f595 (4.4b) |
| 596–651 | `susto` leve y corre en f640 (**regla en la mano**) | **Camina hacia la caja** f622–f641; se agacha con la mano extendida f642–f651 | **Dibuja la caja** (f596–f611) y **la empuja** (f612–f640); manos atrás, ladea el rizo | Caja de tinta desliza 3 f de ease-out al final |
| 652–699 | Bloqueo f652; hold f654–f659; retrocede 0,5 u extendiendo la regla f660–f687; anticipa f688 | Retira la mano f656; **retrocede 2 pasos de 0,4 u** (f664–f679) | **Se acerca a la caja** (f664–f699, 1,0 u, lento): mira y ladea | — |
| 700–732 | Toque; `susto`; retrocede 0,3 u (f704–f712) | `sorpresa`; retrocede 0,3 u (f704–f712) | Blast; rueda; **se sienta chamuscado** 0,8 | Explosión (4.5) |
| 733–799 | Dice el dato con `pensando`; cambio de apoyo f748 y f770; **camina hacia el rival** f786–f799 con la regla en guardia | `sorpresa` → `curiosidad` (f740); **consejo con la cabeza (dos negaciones de ±8°, sin dedo ni mano al mentón, que es gesto de Lumi)** | Mira el cráter f733–f748; **tose humo por el rizo**; de pie f750–f767; se planta en f768 con el rizo en alto | Humo despeja f727–f760 |
| 800–899 | Golpe 6 (f812); **mira su regla deshacerse** (f836–f847); **camina a su sitio** (3,9 u, f832–f893), lanza el lápiz a Tan al cruzarse (f858–f862) | Camina por C1 a su sitio (3,3 u, f832–f885), atrapa el lápiz (f862), vuelve a C2 y sube el brazo a `saluda` f886–f899 | Implosión; resto sentado f832–f855; **goteo f856–f869** | Humo y llama apagados en f831 |
| 900–929 | Firma de cierre: `parado`, sin lápiz, cabeza 25° (f895–f899) | Firma de cierre: anticipación c −24 a −19, suelta c −15 | — | Nada se mueve; el `respira` se apaga en f896–f899 |

#### 4.4a Entrada del rival por la grieta (P-002), f30–f45: 16 f, no más que la entrada de siempre

Es **la inversa de la salida del short 4** (que se escurría por una grieta del suelo en 16 f; usa `grieta()`, `trazoSuelo()` y
la gota de suelo del guion `tin_en_s_004.js`): misma grieta, mismo lado (derecho), mismas curvas con el tiempo al revés.
No existe como pieza: **construir `entra_por_grieta`** (README, «Piezas que faltan»).

| f | Qué pasa | Curva |
|---|---|---|
| f30–f33 (4 f) | La grieta se abre: dos trazos del suelo con 3 partículas de polvo con contorno | ease-out |
| f34–f39 (6 f) | Un hilo de tinta sube del suelo y se dibuja de un solo trazo (la madeja empieza en el rizo) | ease-in-out, el mismo `EASE.io` de la salida del short 4 |
| f40–f45 (6 f) | El trazo se enrolla en madeja y asoma el cuerpo de palitos; asienta a 1,25 | muelle `POP` (220, 20, 1) |
| f46–f69 (24 f) | Crece a 1,5 «como gato erizado» | ease-in-out |

La grieta se queda abierta hasta el final (daño que se queda). **Entre f46 y f575 no hay ningún evento activo del universo**
(9.4 punto 2); la grieta cuenta como sustitución de la entrada de siempre.

#### 4.4b El telescopio (P-006): 20 f activos, f576–f595

**Nada de lo que pasa alrededor cambia.** El rival camina a la izquierda y Tin y Tan siguen en su reposo vivo. Tan es la
única que mira, **6 f, solo cabeza, sin cambiar la cara**. Tin no mira; el rival no mira.

| f | Qué pasa | Curva y medida |
|---|---|---|
| f576–f579 | La rasgadura se abre sobre el aterrizaje, en el cielo del fondo (4 f); **se cierra sola** en f584–f591 (no queda cicatriz: el cierre del bucle no suma otro elemento) | la abre en 4 f con ease-out; la cierra en 8 con ease-in-out |
| **f576–f587 (12 f)** | El telescopio de cartón asoma por la rasgadura y **cae** girando una vuelta | ease-in (acelera); sombra de suelo que crece de 0,2 a 0,7 u y de opacidad 0,1 a 0,3 |
| **f588** | Primer apoyo: cuadro de contacto (1 f), polvillo de cartón con contorno (3 partículas) | — |
| **f588–f595 (8 f)** | **Un solo rebote** de ≈ 0,4 u (sube f589–f591, baja f592–f594) y se **queda quieto a 20° de inclinación en f595**; con el tubo hacia arriba y la montura del lente visible | rebote parabólico (arco) con asiento sin segundo rebote |
| **f588–f593 (6 f)** | **Mirada de Tan, solo cabeza, `mira`:** giro de ida f588–f589 (2 f, ease-out), mantiene f590–f591 (2 f), vuelve f592–f593 (2 f, ease-in-out). **Cara sin cambio** | Si fotografía prefiere 6 f de mirada mantenida más los giros (f586–f596), el supervisor de continuidad decide si eso sigue siendo «6 f» y cuenta 20 f de evento |
| f596 en adelante | Queda quieto en el suelo hasta el final; sale en el plano de cierre fuera del pasillo de la firma (30 px) | — |

**Es difícil para el motor, y lo digo:** el telescopio es un objeto nuevo con rotación y rebote que no existe en el
motor (`objeto_caido`, prioridad 2 del plan de tanda). Versión simple si no llega: el mismo telescopio **sin giro** y
con la sombra y el rebote; la rasgadura va igual. No quito el rebote: es lo que lo distingue de un error de render.

### 4.5 El paquete, la explosión y la implosión

#### El paquete: «no tocar» se lee en silueta, sin texto (f596–f667)

| f | Qué pasa | Silueta o curva |
|---|---|---|
| f596–f611 (16 f) | El rival **dibuja una caja lisa de tinta** de un solo trazo con la mano; sonido `trazo_de_tinta` (16 f, existe) | Caja cúbica de tres caras, **sin texto, sin icono, sin flecha, sin lazo, sin ventana**, contorno de tinta y relleno plano de un solo tono (regla 2.1.4) |
| f612–f640 (29 f) | **La empuja con el pie y se aparta con las manos atrás**; la caja desliza ≈ 1,8 u por C2 hacia ellos y se detiene a ≈ 1,0 u de Tan | Sale rápida y frena (ease-out); sombra de contacto; **nada de rebote** (un rebote la haría ver viva) |
| f622–f641 | Tan **camina hacia la caja** (≈ 1,4 u, 30 f) | `camina` pareja |
| f642–f651 | Tan **se agacha y extiende la mano derecha** hacia la caja | Pose de curiosidad: torso inclinado, mano al frente |
| f640–f651 | Tin **corre con la regla** (12 f, 1,2 u) y frena en la frenada de 6 f (f646–f651) | `corre_arma`; arranque y frenada; sin giro instantáneo |
| **f652–f653 (2 f)** | **La regla de Tin cruza horizontal por delante de la muñeca de Tan**, a la altura de su mano; sin estrella, sin gotas | Silueta: Tan inclinada con el brazo extendido, la barra de la regla entre su mano y la caja, **Tin a su derecha** (cabeza a ≥ 1,2 R de la de Tan en pantalla). Se prueba en tira de 2 f **sin color** (negro sobre claro) |
| f654–f659 (6 f) | **Hold de póster:** nadie se mueve salvo la regla, que vibra 4 f (±3°, muelle de 4.12) | La tarjeta de «not from Rockstar» entra aquí (f654); no cubre el gesto |
| f660–f667 | Tin baja la regla 10°; Tan retira la mano a su pecho (f656–f663) | ease-in-out |

**Qué sé que es difícil para el modelo humano y lo es para el motor:** dos cuerpos que casi se tocan con un objeto entre
ambos. Si en la prueba la regla se lee como un golpe a Tan: separar a Tin 0,3 u y hacer que la regla cruce **a 0,2 u por
encima** de la muñeca sin contacto; el gesto sigue leyéndose como «frena».

#### Explosión (A6): toque f700, fases f702–f726

Silencio de efectos y de música desde f694 y voz callada f695–f727. **Regla de alcance (se mide):** la bola de fuego no
pasa del 75 % de la distancia entre la caja y Tin, y el rival se acerca a la caja hasta ≤ 50 % de ese alcance (lo hace f664–f699).
A Tin y a Tan **no los alcanza ni el fuego, ni los escombros, ni la onda del suelo** (la onda se disuelve antes); ellos se
cubren y retroceden 0,3 u por su cuenta.

| f | Fase | Qué se ve | Destello |
|---|---|---|---|
| f700–f701 | Toque | La punta de la regla toca la caja; una gota de tinta | no |
| f702–f703 | **Cuadros invertidos con máscara** (1 vez en todo el video) | Dos cuadros invertidos, solo sobre la caja y su entorno | 1 |
| f704–f708 | Líneas radiales | 8 líneas de tinta clara desde la caja, 5 f | no |
| f709–f712 | **Claro con máscara** | Mancha clara plana alrededor de la caja; **nunca a pantalla completa** | 2 |
| f713–f722 (10 f) | **Bola de fuego plana** | Fuego de pocos colores planos (naranja, amarillo, rojo de fuego, anillo amarillo) por fases de 2 f; escombros de tinta y tiras de papel | no |
| f723–f726 (4 f) | Enfriamiento | Rojo oscuro y marrón de fuego, después gris de ceniza | no |
| f727–f760 | Humo con contorno | Humo de tinta con contorno (no manchas borrosas); despeja y deja ver el dato (revelado de f735) | no |

`comprobar_destellos` debe dar 0 avisos: el máximo es de 3 destellos por segundo (regla 2.1.8) y aquí hay 2 en 11 f. A
la caja le sigue una **quemadura plana en el suelo** (daño que se queda); no hay agujero.
**El rival** sale despedido por el blast: calcos f704–f707, vuelo de 12 f hacia la izquierda (1,4 u), rueda f720–f726 y se
sienta en f727 chamuscado: **bordes de tinta tostados y puntos de ceniza, sin rojo**, a 0,8. Nada lo golpea mientras está
sentado.

#### Implosión (A6): golpe 6, f812; fases f814–f831 (18 f)

Tin en `mazoArriba` → `mazoAbajo` con la regla. Contacto sobre la cabeza del rival; se aplasta de 1,0 a 0,6 de alto en 2 f.

| f | Fase | Qué se ve | Reloj |
|---|---|---|---|
| f814–f815 | Succión | El rival se hunde; **la tarjeta de «no official date» y la voz de Tin ya entraron** (f814/f816); la marca de la pestaña se dibuja a la vez (f812–f815, 4.7) | 0,6 |
| f816–f823 | **Tres anillos de tinta** se cierran desde 1,6 u (escalonados 2 f) | acelera hacia adentro (ease-in) | de 0,6 a 1,4 |
| f824–f829 | **El humo y la llama se estiran en hilos hacia el centro** (las cajas de `cajas_izq` quedan ennegrecidas); la llama se apaga en f829 | ease-in | 1,4 |
| f830–f831 | Cierre seco; queda el resto: un trazo suelto de ≈ 1,5 R con el rizo | corte seco | 1,0 |

**La implosión ocurre en x −2,4, a 0,7 u del fuego**, para que se lea que se lo lleva. **En c −30 no se mueve nada salvo la
firma:** el fuego y el humo terminaron en f831 y el rival sale en f869.
**Resto y salida (P-005), f832–f869.** El resto queda sentado, con el reposo vivo, f832–f855 (24 f). **Goteo f856–f869 (14 f):** se
deshace en una gota alargada y se desliza por el suelo hacia el borde izquierdo (2,1 u en 14 f) con 3 gotas que caen
(`gota`); sale del cuadro en f869, **31 f antes de c −30**. Curva de ease-in-out (la misma de la salida del short 4) y deja un
trazo corto de tinta en el suelo (daño que se queda). **Si el supervisor lo lee como exceso, es lo primero que se encoge
(9.3 de la dirección: hasta su mínimo de 14 f).**

### 4.6 Armas dibujadas con tinta (A12; ninguna de fuego)

| Arma | Quién | Cuándo | Cómo se dibuja y se ve |
|---|---|---|---|
| **`regla_de_tinta`** | Tin la dibuja; Tan la usa y la devuelve | Dibujo f296–f321 (26 f, plano de detalle); en la mano hasta f812; se deshace f836–f847 | Un solo trazo de lápiz, 8 f para el cuerpo y 5 marcas de 3 f cada una; **sin números ni texto**: nada que se lea como fecha (2.1.3). Larga como la distancia entre las dos manos abiertas de Tin. No repite el bastón ni el mazo del short 4. Es una vara de medir, no una espada |
| **`paquete_de_tinta`** | El rival | f596–f611 | Caja lisa descrita arriba; **no es un arma**, nada que se parezca a un archivo (2.1.4) |

**Ninguna arma de fuego, ninguna silueta que lo parezca.** El lápiz de Tin **no es un arma** (firma) y no golpea nunca.

### 4.7 Marca final: asterisco, f812–f815 (P-004)

Seis trazos de 1 f del short 4 (`asterisco_tic`) se reparten aquí **en 3 trazos en f812, f813 y f814–f815** (4 f en total): es
la **segunda marca de la pestaña de cartón**, arriba al fondo, a la vez que el contacto de f812 y el inicio de la implosión.
**Interpretación mía:** la marca va en la pestaña (brief, P-004) y **no en el suelo donde se borra el rival**, como en el
short 4 (que dejaba un asterisco en el piso): así no se repite el cierre. Si el director creativo prefiere que esté junto
al resto, se mueve el golpe 6 bajo la pestaña (x −1,4) y cambia la dirección de la salida.

### 4.8 Curvas de velocidad (A2)

El reloj de la escena baja o sube; **la voz nunca se frena ni se acelera** (siempre al 110 %). Nada lineal: toda curva es
ease-in, ease-out o ease-in-out, o un muelle declarado.

| Tramo (f) | Reloj | Qué se siente |
|---|---|---|
| Anticipaciones (6 f antes de cada pausa) | 1,0 con frenada | Carga |
| Pausas (K −6 a K −1) | La pose casi quieta; el mundo sigue (fuego, humo, polvo) | Aire contenido |
| Contactos (K, K +1) | 1,0, con salto de posición | Golpe seco |
| Lanzamientos | 1,3 con calcos | Violencia de dibujo |
| Vuelos: f94–f99 (0,5), f136–f145 (0,35), f218–f225 (0,5), f352–f363 (0,25), f490–f499 (0,35), f708–f719 (0,4) | 0,25 a 0,5 | El único cámara lenta es la del dibujo |
| Carreras de Tan (f106–f123) y del rival (f448–f471) | 1,3 con borrón | Urgencia; 4,5 a 6,2 u/s (rango medido en el short 4: 4,6–6,2 u/s) |
| Telescopio: caída f576–f587 (ease-in) y rebote f588–f595 (arco) | 1,0 | Peso |
| Explosión f702–f726 | Cada dibujo dura 2 f | Estallido legible |
| Respiro 3: f733–f799 | 1,0, casi nada se mueve | Cara de póquer |
| Implosión f814–f831 | 0,6 → 1,4 | Colapso hacia adentro |
| Firma: f0–f29 y f900–f929 | La de la firma | Reconocimiento |

El borrón de movimiento (arco del color de quien golpea) se pinta en los 2 f de contacto y en las carreras; **los vuelos del
short 4 no llevaban borrón** (README, límites): aquí se añade el calco, no un filtro.

### 4.9 Lo que se rompe, cuándo, y lo que queda (A5 y A8)

| f | Pieza | Qué le pasa | Nombre y estado final |
|---|---|---|---|
| f100–f101 | `pila` | Cede la torre de abajo: panel abierto, ventilador colgando, la pantalla del monitor inclinada 10° | **`torre_de_pc_rota`** (P-007); el monitor de portada se queda inclinado |
| f146–f147 | `cajas_der` | 5 cajas de cartón aplastadas, 2 abiertas y 8 tiras de cartón por el suelo | `cajas_de_carton_rotas` |
| f226–f227 | `monitores` | Un monitor revienta en estrella; trozo de marco vuela f228–f236; el soporte queda doblado | `monitor_roto` |
| f262–f270 | `pila` | La torre de encima de la rota resbala y cae junto a Tin | `torre_de_pc_caida` (tumbada, intacta) |
| f344–f345 | `farol` | Se tuerce 8° en la caja de conexiones; **la luz no parpadea** (no más de 3 destellos por segundo) | `farol_torcido` |
| f346 en adelante | `cajas_izq` | Chispas y llama fase 1; humo de f358; llama fase 2 (×1,5) con la caja que cae ardiendo en f500–f511 | Quedan **ennegrecidas** en f831 |
| f500–f501 | `persiana` | Abolladura con la silueta del rival (3 ondulaciones) | `persiana_abollada` |
| f702–f726 | Suelo | Quemadura plana bajo el paquete | `quemadura_del_paquete` |
| f30–f45 | Suelo | La grieta | `grieta_del_rival` |
| f576–f595 | Fondo | El telescopio queda quieto | `telescopio_de_carton` (ancla, short 6) |
| f856–f869 | Suelo | Trazo corto de tinta junto al borde izquierdo | marca del goteo |

**No se rompe:** el monitor de portada (solo se inclina), la pestaña, la caja registradora rota, el telescopio ni nada que se
parezca a un logotipo o una marca; ningún objeto del mundo lleva texto. Al final del video los daños quedan **acumulados
en el plano de cierre**: esta es la **excepción de fondo declarada, la misma del short 4 (D6): firmo la excepción**. Lo que sí
casa entre c −1 y f0: lápiz, brazo de Tan, cabeza, cuerpo, pose de Tin, caras, texto y cámara.

### 4.10 Tabla por toma (una acción por toma)

Emociones del cap. 01 y de `perfil_emocional.md`. Panel = la expresión de la hoja de Tin o Tan, o la pose de la hoja del rival.
«T» es la toma; el plan de cortes lo cierra fotografía, y **cada fila es una sola acción**.

| T | f | Personaje | Emoción | Pose inicial (keyframe) | Anticipación → acción → pose final | Secundaria | Mirada | Timing | Panel |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 0–29 | **Tan** | Curiosidad | `saluda` con arco de firma (95°, 108°), cabeza 25° | La mano abierta ya está lista → atrapa el lápiz en f10 con retroceso del brazo → sostiene | Bufanda con muelle; Tin da un saltito de −5 px | Sigue el lápiz y sube al objeto en f14 | Los de la firma (sin cambios) | Tan `curiosidad` |
| 2 | 30–69 | **Rival** | Curiosidad (la pregunta toma cuerpo) | Hilo de tinta en la grieta | Grieta (4 f) → hilo sube (6 f) → madeja y cuerpo (6 f) → crece a 1,5 (24 f) | El trazo hierve cada 3 f | Los dos huecos hacia Tan | 16 f (entrada normal) | Rival `crecida` |
| 3 | 30–69 | **Tan** | Sorpresa | `pregunta` | Interrumpe la mano → retrocede 2 pasos (f46–f62) → guardia (f62–f69) | La bufanda sigue | A la grieta (f32), luego al rival | Pasos de 0,4 u cada 8 f | Tan `sorpresa` |
| 4 | 30–87 | **Tin** | Determinación | `parado` sin lápiz | Gira la cabeza (3 f) → medio paso atrás → se adelanta 2 pasos → planta (f70–f79) | Cabeza ±8° | Al rival | 3 + 8 + 8 f | Tin `curiosidad` → `concentrado` (f80) |
| 5 | 70–117 | **Tin** | Determinación | Guardia: pies abiertos, manos al pecho | Peso atrás (4 f) → pausa (4 f) → empuja con las dos manos (2 f) → guardia (6 f) | La gorra se mueve 2 px en el contacto | Al pecho del rival | Golpe 1 (4.3.B) | Tin `concentrado` en la pausa; `pensando` al dato |
| 6 | 70–117 | **Rival** | Sorpresa | Rizo inclinado hacia Tan | Absorbe y se aplasta 3 f → sale volando de frente (6 f) → choca → se sienta y mira la torre rota (16 f) | Hierve | A la torre (f106) | 6 + 2 + 16 f | Rival `recibe`, `caído` (sentado, no tendido) |
| 7 | 104–147 | **Tan** | Determinación | `guardia` | Carrera 18 f con frenada → hombro atrás y quieto (12 f) → embiste (2 f) → guardia (6 f) | La bufanda hacia atrás | Al hombro del rival, luego al choque | Golpe 2 | Tan `curiosidad` → `sorpresa` al contacto |
| 8 | 118–163 | **Rival** | Terquedad | `sentado` | Se pone de pie (10 f) → se sacude (4 f) → pasa a C2 | Rizo que vuelve a subir | A Tin | 10 + 4 + 8 f | Rival `guardia` |
| 9 | 164–207 | **Rival** | Terquedad | `guardia` | Se echa atrás (6 f) → pausa (4 f) → salta sobre Tin (12 f) → aterriza resbalando (8 f) | Los brazos en aspas | Hacia Tin | 6 + 4 + 12 + 8 f | Rival `golpe` (falla) |
| 10 | 164–207 | **Tin** | Determinación | `guardia` | Lee la pausa → se agacha (8 f) → deja pasar (8 f) → se levanta y camina 2 zancadas | Cabeza que sigue al rival ±8° | Al rival de principio a fin | 8 + 8 + 14 f | Tin `curiosidad` |
| 11 | 200–251 | **Tin** | Determinación | Dos zancadas | Pie atrás (6 f) → pausa (6 f) → patada frontal con la planta (2 f) → guardia (6 f) | Los brazos equilibran | Al pecho | Golpe 3 | Tin `concentrado` / `pensando` |
| 12 | 226–251 | **Rival** | Sorpresa | Vuela de frente | Vuela (8 f) → choca (2 f) → sentado entre vidrio (12 f) → de pie (12 f) | Chispas | Al vidrio roto | 8 + 2 + 12 + 12 f | Rival `recibe` |
| 13 | 226–240 | **Tan** | Sorpresa | `guardia` | Ve el trozo de marco → salta atrás 0,3 u (8 f) → recompone (6 f) | Bufanda con muelle | Al trozo | 8 + 6 f | Tan `sorpresa` |
| 14 | 262–295 | **Tin** | Humor seco | `pensando` | Paso atrás de 0,4 u (8 f) → la torre cae → queda con la regla fuera | Cambio de apoyo f282 | A la torre | 8 + 8 f | Tin `pensando` |
| 15 | 296–329 | **Tin** | Concentración | `dibuja` | Marca el cuerpo (8 f) → cinco marcas de 3 f → empuña (2 f) | La lengua del lápiz no; el trazo hierve | A la regla | 26 f | Tin `curiosidad` mirando la regla |
| 16 | 302–328 | **Tan** | Curiosidad | `pregunta` | Ladea la cabeza 8° → la mano al frente → vuelve | Bufanda | A Tin | Voz f302–f328 | Tan `curiosidad` |
| 17 | 324–363 | **Tin** | Determinación | Regla atrás y abajo | Rodillas flexionadas (6 f) → pausa (6 f) → batazo diagonal (2 f) → sigue el golpe (6 f) | Arco naranja | Arriba, al rival | Golpe 4 | Tin `concentrado` → `eureka` al dato |
| 18 | 336–437 | **Rival** | Sorpresa → aferrado | Vuela de lado | Vuela (2 f) → choca (2 f) → pegado (6 f) → cae despacio (12 f) → trepa (32 f) → se agarra (42 f) | Rizo que tiembla | Hacia abajo | 2 + 2 + 6 + 12 + 32 + 42 f | Rival `recibe` |
| 19 | 438–471 | **Tan** | Complicidad | Mira a Tin | Recibe la regla (f444) → camina 0,8 u → dice la invitación con `invita` | Bufanda; la regla queda abajo | A Tin y al frente; **no mira a cámara más de lo que dura la frase** | 34 f | Tan `feliz` |
| 20 | 438–441 | **Tin** | Complicidad | `guardia` | Lanza la regla (4 f) → vuelve a la guardia | Lápiz en la otra mano | A Tan | 4 f | Tin `curiosidad` |
| 21 | 438–471 | **Rival** | Terquedad | Colgado | Baja del farol (12 f) → corre por C2 (24 f) → se planta | Hierve | A Tan | 12 + 24 f | Rival `guardia` |
| 22 | 472–553 | **Tan** | Determinación | `guardia` con la regla | Peso atrás (6 f) → pausa (6 f) → estocada recta (2 f) → guardia (6 f) | Bufanda hacia atrás | A la línea de la regla | Golpe 5 | Tan `concentrado` (verificar que no lea enojo) |
| 23 | 486–565 | **Rival** | Sorpresa | Planta | Vuela al fondo (10 f) → choca (2 f) → resbala por la persiana (48 f) → se despega (12 f) | Rastro de tinta | A Tan | 10 + 2 + 48 + 12 f | Rival `recibe` |
| 24 | 532–553 | **Tan y Tin** | Complicidad | Tan con la regla | Tan se la pasa (5 f) → Tin la recibe y la sostiene horizontal («mide») | Cambio de apoyo | Los dos al rival | 5 + 16 f | Tan `feliz`; Tin `pensando` |
| 25 | 554–599 | **Rival** | Terquedad → plan | Pegado | Se despega → camina a la izquierda (29 f) | Hierve | Al suelo | 12 + 29 f | Rival `guardia` |
| 26 | 576–595 | **Telescopio y Tan** | Extrañeza leve, sin comentar | Reposo vivo | La rasgadura (4 f) → cae (12 f) → rebota (8 f) → queda | Polvillo | **Tan: 6 f solo cabeza**; Tin no mira | 4.4b | Tan `curiosidad` **sin cambiar la cara** |
| 27 | 596–641 | **Rival** | Astucia (sin miedo) | `dibuja` | Dibuja la caja (16 f) → la empuja (29 f) → se aparta con las manos atrás | Rizo ladeado | A la caja | 16 + 29 f | Rival `guardia` |
| 28 | 622–651 | **Tan** | Curiosidad | `camina` | Va a la caja (20 f) → se agacha (6 f) → extiende la mano (4 f) | Bufanda | A la caja | 30 f | Tan `curiosidad` |
| 29 | 640–667 | **Tin** | Determinación | `corre_arma` | Corre (12 f) → frena (6 f) → cruza la regla (2 f) → hold (6 f) | Regla vibra 4 f | A la mano de Tan | 12 + 6 + 2 + 6 f | Tin `sorpresa` leve → `pensando` |
| 30 | 660–699 | **Tin** | Tensión | Con la regla | Retrocede y extiende (28 f) → anticipa (6 f) → pausa (6 f) | Respira | A la caja | f688–f699 | Tin `concentrado` |
| 31 | 664–699 | **Rival** | Curiosidad | Manos atrás | Se acerca a la caja (36 f) ladeando el rizo | Hierve | A la caja | 36 f | Rival `guardia` |
| 32 | 700–732 | **Tin y Tan** | Sorpresa | Tin en toque | Toque (2 f) → se cubren (10 f) → retroceden 0,3 u → bajan los brazos | Bufanda | A la bola de fuego | 4.5 | Tin `sorpresa`; Tan `sorpresa` |
| 33 | 700–760 | **Rival** | Sorpresa | Junto a la caja | Sale despedido (12 f) → rueda (7 f) → se sienta chamuscado → mira el cráter | Humo por el rizo | Al cráter | 12 + 7 f | Rival `caído` (sentado) |
| 34 | 733–799 | **Tin y Tan** | Humor seco | Reposo | Dato con `pensando`; Tan niega con la cabeza dos veces | Cambio de apoyo cada 18–24 f | Al rival | f733–f799 | Tin `pensando`; Tan `curiosidad` |
| 35 | 768–799 | **Rival** | Terquedad | Sentado | De pie (17 f) → rizo en alto | Tos de humo | A Tin | 17 f | Rival `guardia` |
| 36 | 800–831 | **Tin** | Determinación | Regla abajo | Regla arriba (6 f) → pausa (6 f) → tajo (2 f) → mira el resultado (18 f) | Arco naranja | A la cabeza del rival | Golpe 6 | Tin `concentrado` → `curiosidad` |
| 37 | 814–855 | **Rival** | Sorpresa | Aplastado | Succión (2 f) → anillos (8 f) → humo y llama hacia adentro (6 f) → cierre (2 f) → resto sentado (24 f) | Hierve | A Tin | 18 + 24 f | Rival `borrándose` |
| 38 | 836–847 | **Tin** | Humor seco | Regla en la mano | Mira cómo la regla se deshace en gotas (12 f) | Gotas que desaparecen | A la regla | 12 f | Tin `pensando` |
| 39 | 856–869 | **Rival (el resto)** | Alivio | Resto sentado | Se deshace en gota (4 f) → se desliza (10 f) → sale por el borde | 3 gotas caen | Al frente | 14 f | Rival `borrándose` |
| 40 | 832–899 | **Tin y Tan** | Alivio | Tin −1,4 u, Tan +0,9 u | Caminan a su sitio; Tin lanza el lápiz a Tan al cruzarse (f858); Tan sube a `saluda` (f886–f899) | Bufanda con muelle | Entre sí y luego a cámara a la firma | 61 f | Tin `curiosidad`; Tan `curiosidad` |
| 41 | 900–929 | **Tan** | Curiosidad | `saluda` | Anticipación c −24 → impulso → suelta c −15 | Sobrepaso del brazo | Al objeto | La firma | Tan `curiosidad` |

**Frases de actuación en inglés (para el registro: estas tomas se dibujan con código, no se envían a un modelo de video)**

1. *Tan catches the spinning pencil with a small recoil of the arm and lifts her chin to ask the question.*
2. *A thin ink thread climbs out of a crack in the floor, loops into a tangled ball, and swells until it towers over them.*
3. *Tan shrinks back two steps, eyes wide, scarf swinging.*
4. *Tin turns his head, takes a half step back, then steps forward and plants both feet.*
5. *Tin pulls both hands to his chest, holds still for a beat, then shoves the ink figure in a single frame.*
6. *The ink figure folds around the shove, flies across the yard into the stack of computer towers, and sits down to stare at the broken one.*
7. *Tan sprints, brakes, twists her shoulder back and holds it still until the figure is standing; then she charges with the shoulder.*
8. *The ink figure stands up, shakes off the cardboard, and steps into the lane.*
9. *The ink figure leans back, holds, then leaps over Tin with one arm swinging, lands on its knees and slides.*
10. *Tin watches the figure wind up, drops into a crouch and lets it sail over his head.*
11. *Tin takes two long strides, plants his back foot, holds, and pushes his sole into the ink figure's chest.*
12. *The ink figure crashes into a monitor, which bursts in a star of cracks; it sits among the glass.*
13. *Tan hops back as a piece of the frame spins past.*
14. *Tin steps back as the top tower tips and slides off the stack, then stands with his face blank.*
15. *Tin draws a ruler in one stroke of the pencil, then five short marks, one by one.*
16. *Tan tilts her head and asks the question with her hand out.*
17. *Tin swings the ruler back and low, holds, then swings it up on the diagonal in a single frame.*
18. *The ink figure slams into the lamp post, hangs flat against it, slides down slowly and climbs back up, clinging with its curl.*
19. *Tan catches the ruler while walking and invites with an open hand, never turning toward the camera longer than the sentence.*
20. *Tin tosses the ruler underhand and drops back into guard with the pencil.*
21. *The ink figure slips down the lamp post and runs along the yard, planting itself in front of Tan.*
22. *Tan shifts her weight back, holds, and lunges straight in with the ruler.*
23. *The ink figure flies backward into the shutter, leaves its own silhouette dented in it, and slides down slowly before peeling off.*
24. *Tan tosses the ruler underhand to Tin, who holds it level like a measuring stick.*
25. *The ink figure peels off the shutter and walks away to the left with its curl drooping.*
26. *Ink-colored cardboard telescope tumbles out of a tear in the sky, bounces once and lies still; Tan turns her head toward it for six frames without changing her face.*
27. *The ink figure draws a plain box in one stroke, nudges it with its foot and puts its hands behind its back.*
28. *Tan walks up to the box, crouches and reaches out one hand.*
29. *Tin sprints in with the ruler and stops it level across Tan's wrist; both freeze.*
30. *Tin backs away, stretching the ruler out at full length, and holds still before the tip.*
31. *The ink figure steps closer to its own box, tilting its curl.*
32. *Tin touches the box with the tip of the ruler; both cover their faces and step back.*
33. *The ink figure is thrown back, rolls, and sits scorched, coughing a puff of smoke through its curl.*
34. *Tin and Tan stand with blank faces; Tan shakes her head twice, slowly.*
35. *The ink figure stands up and plants itself, curl high.*
36. *Tin raises the ruler overhead, holds, and brings it straight down.*
37. *The ink figure collapses inward as three rings close, pulling the smoke and flame into itself.*
38. *Tin watches the ruler dissolve into drops.*
39. *The small ink scrap melts into a long drop and slides off the left edge of the page.*
40. *Tin and Tan walk back to their marks; Tin flips the pencil to her as they pass.*
41. *Tan swings her arm back and down, snaps it forward and releases the pencil.*

### 4.11 Transferencia de movimiento

**No hace falta.** Ninguna toma depende de un movimiento exacto que el motor no pueda hacer (no hay baile, trend ni gesto de
una persona real). **No se graba nada ni se usa `motion_control` ni `hf_mult_motion_control`.** Las tomas difíciles son
difíciles para el motor, no para un modelo de video: 4.5 (el bloqueo, dos cuerpos con un objeto entre ellos) y 4.4b (el
telescopio con giro y rebote). Para cada una dejé una versión más simple.

### 4.12 Gráficos con código (rigidez, amortiguación y masa; fotograma de entrada y de salida)

HyperFrames y Remotion **no figuran como aprobados por el dueño** en los documentos que leí: **no se usan**. La capa de datos la
monta el editor (sección 6) con el `componer.py` del proyecto (código 2D, como en el short 4) o con `postpro.py`/CapCut.
Esto es lo que le pido a esa capa, con las curvas de la casa del short 4 y de la firma: `POP` es (220, 20, 1) y `SLIDE`
es (120, 16, 1) (firma, 9.3); las demás dosis son (hipótesis del equipo). **Nada lineal; ningún elemento entra sin muelle o curva.**

| Elemento | Entrada (f) | Salida (f) | Muelle o curva |
|---|---|---|---|
| Tarjeta de datos 2 («not announced») | f92 | f205–f207 | `POP` (220, 20, 1) |
| Tarjeta de datos 4 | f216 | f297–f299 | `POP` |
| **Tarjeta de medidas**, renglón 1 («574 days») | f374 | f570–f572 | `POP` y la tarjeta crece al renglón 2 en f529 con `SLIDE` (120, 16, 1) |
| **Barra de «574 days»** | se dibuja f374–f397 (24 f) con el golpe de f336 ya dado | — | ease-out, **sin sobrepaso** (que no se lea como pronóstico) |
| Barra del renglón 2 («≈ 1 year») | f529–f552 (24 f) | f570–f572 | ease-out, **más corta que la primera, sin eje común ni tercera barra** |
| Tarjeta 9 («not from Rockstar») | f654 | ≈ f699 | `POP` |
| Tarjeta 10 («some carry malware») | f730 | ≈ f801 | `POP` |
| Tarjeta 12 («no official date») y sello | f816 | f891–f893 | `POP`; el sello «as of (fecha)» entra con la tarjeta 2 y con la 12 |
| Portada | c −30 | — | `POP` (firma, 2.2) |

Los datos quedan quietos los fotogramas de 2.2 (30 f o más). **Ninguna tarjeta comparte plano con el pico (f700–f732)** y ninguna
cubre una cara, el bloqueo ni la caja.

### 4.13 Lo que existe en el motor y lo que hay que construir

Fuente: `motor_de_accion/README.md` y `catalogo.json` (actualizado el 2026-11-27). **Existe, hecho para el short 4:**

| Qué | Dónde | Lo uso para |
|---|---|---|
| Poses: `quieto`, `guardia`, `carga`, `golpe`, `embiste`, `patada`, `recibe`, `vuela`, `caido`, `agachado`, `sentado`, `susto`, `esquiva`, `bloqueo`, `dibuja`, `pregunta`, `invita`, `explica`, `atrapa`, `mazoArriba`, `mazoAbajo`, `festeja` | `escena.html` y `guiones/tin_en_s_004.js` | Casi todas las tomas de 4.10 |
| Locomoción por distancia: `corre`, `corre_arma`, `camina`; `trayecto(quién, f0, f1, puntos, modo)` | `escena.html` (CICLOS, `poseCiclo`) | Todos los desplazamientos |
| `contacto()`, `estrella`, calcos, `respira`, `humoC`, `polvoC`, `chispaC`, `gota`, llama plana por fases, bola de fuego plana, `onda`, `grieta`, `quemadura`, `mancha`, `trazoSuelo`, `romperCajones`, `mira`, `velocidad(S)` | motor y guion del short 4 | Impactos, fuego, humo, explosión, daños |
| Implosión de 3 anillos y el goteo con `escurre` | guion del short 4 | Golpe 6 y la salida |
| Cámara por planos (`PLANOS`, `encara`), pistas (`SECO=1`), `control_encuadre.py` | motor | Verificación |
| Sonidos del catálogo (`trazo_de_tinta`, `golpe`, `choque_madera`, `vidrio_grieta`, `chispas`, `cajas_caen`, `roce_suelo`, `fuego_enciende`, `explosion`, `implosion`, `escurre`, `gotas`, `asterisco_tic`) | `sonidos/sonido.py` y `codigo/audio.py` | Ver 4.14 |
| Paleta B | `paletas/b_noche_de_tinta.json` (nunca usada en un video) | Todo |

**Hay que construir** (no bloquea el paquete; viaja como pedido a producción, sección 7). **Pendiente de verificar en el
código** si la pose existente cubre la forma pedida antes de construir otra:

| # | Qué | Para qué toma | Nota |
|---|---|---|---|
| 1 | Entorno `patio_tienda_de_computadoras` con `pila`, `cajas_der`, `monitores`, `farol`, `persiana`, `pestana(marcas)`, `cajas_izq` y **sus versiones rotas** | Todo | Entra al catálogo (temas: tecnología, hardware, compras) |
| 2 | **`entra_por_grieta`** (inversa de la salida del short 4) | T2 | 16 f; mismas curvas al revés |
| 3 | **`sale_goteando`** (borde izquierdo, 14 f, con 3 gotas y trazo) | T39 | Variante del `escurre` del short 4 |
| 4 | **`objeto_caido`** con rasgadura, giro, rebote, sombra y mirada de Tan (`mira` ya existe) | T26 | Prioridad 2 del plan de tanda |
| 5 | **`telescopio_de_carton`** y su versión rota | T26 | Ancla del short 6; la versión rota es de ese video |
| 6 | **`regla_de_tinta`**: arma con 5 marcas, lanzable y que se deshace en gotas | T15–T38 | Reemplaza bastón y mazo |
| 7 | **`paquete_de_tinta`**: caja que se dibuja, desliza con frenada y revienta | T27–T32 | Sin texto, icono, ni flecha |
| 8 | Poses nuevas: `empuja` (dos brazos al frente), `hombro` (si `embiste` no se lee de hombro), `patada_frontal` (si `patada` es solo la giratoria), `batazo` (diagonal ascendente a dos manos), `estocada`, `trepa`, `se_aferra`, `manos_atras` (rival), `cruza_regla` (bloqueo) | T5–T36 | Verificar cuáles ya existen con otro nombre |
| 9 | `torre_de_pc_rota`, `torre_de_pc_caida`, `monitor_roto`, `persiana_abollada` (abolladura con la silueta del rival), `farol_torcido`, `cajas_carbonizadas` | 4.9 | Piezas con nombre propio |
| 10 | Marca de asterisco y de punto en la pestaña | 4.7 | Prioridad 2 del plan |
| 11 | Rasgadura (abre y se cierra) | T26 | Parte del objeto caído |
| 12 | Corte a cuadro de impacto de 1 f en los choques (f226, f344, f500) | Choques grandes | Se hace en `componer.py`, 2D |

### 4.14 Lo que pido a fotografía, sonido, edición, producción y continuidad

**Fotografía (sección 3).**
1. Cámara alta y en diagonal; **corta, no tiembla**. Plano **detalle** en f296–f321 (el lápiz dibuja la regla); **subjetivo
   o equivalente** para la entrada por la grieta (f30–f45); **héroe abierto en f700–f732** que deje ver a Tin, Tan, el
   rival y la caja a la vez (es la prueba de que no los alcanza); **plano general fijo f554–f599 con el cielo libre sobre
   x +3,4** (ahí cae el telescopio); revelado en f733–f760.
2. El bloqueo de f652–f659 en un plano abierto de **perfil casi sin diagonal**, para que Tan, la regla y la caja no se
   solapen. Es el gesto central.
3. Choques grandes f226, f344 y f500: corte de 1 f a cuadro de impacto; **sin temblor**.
4. **El rival nunca tapa la cara de Tin ni la de Tan** (≥ 1,2 R en pantalla); **Tan sale en cuadro y activa toda la pelea**
   (M7 del short 4, donde estuvo fuera de cuadro ≈ 10 s).
5. **El farol no parpadea** más de 3 veces por segundo; el fuego y el humo se leen sobre azul noche (el contraste lo mide
   la sección 3b). El rival **no lleva color** (ficha): decidir si la paleta B se lo da y qué gris tiene el chamuscado.
6. La grieta de la derecha, la caja registradora rota a la izquierda y la pestaña: sus coordenadas, con **30 px de despeje**,
   fuera del pasillo de la firma. Para el telescopio hay que medir si x +3,4 cae dentro de la zona útil.

**Sonido (sección 5).** Nadie los ha oído; los valida una persona.
- Sonidos que existen: `trazo_de_tinta`, `golpe`, `choque_madera`, `vidrio_grieta` (monitor), `chispas`, `cajas_caen`,
  `roce_suelo` (caja que desliza), `fuego_enciende`, `explosion`, `implosion`, `escurre` y `gotas` (goteo), `asterisco_tic`.
- **Nuevos que pide esta coreografía:** `grieta_se_abre` (f30–f45); `regla_golpe` (madera hueca, más aguda que el bastón,
  en f336, f484 y f812; los golpes 1 a 3 usan `golpe`, que existe) y `regla_vibra` (f652–f659); `torre_pc_cae` (chasis metálico, f100 y f262); `farol_metal`
  (f344); `persiana_golpe` (metal que vibra, f500); `papel_rasga` (f576–f579) y `caida_objeto` (f588–f595), ambos bajos;
  `caja_desliza` (f612–f640); `regla_se_deshace` (f836–f847).
- **Cada contacto en K o K −1:** f87/f88, f129/f130, f211/f212, f335/f336, f483/f484, f651/f652 (el bloqueo, más suave) y f811/f812.
- **Silencio de efectos y de música** de f694 a f699 antes del toque y voz callada f695–f727; la explosión cae en la expansión
  (f713). **Nada por encima de la voz** en la invitación (f438–f471) y el consejo (f768–f794).
- **Música:** solo percusión sin melodía y **otro pulso que el del short 4** (F6).

**Editor (sección 6).** Los datos quietos de 2.2 y sus entradas de 4.12; ninguno sobre el bloqueo ni sobre el pico;
subtítulos en su franja.
**Producción (sección 7).** Lo de 4.13, con prioridad en: entorno, `regla_de_tinta`, `paquete_de_tinta`, `entra_por_grieta`,
`objeto_caido` y `pestana(marcas)`.
**Continuidad.** La excepción de fondo de 4.9; las eventos activos suman **38 f** (telescopio 20, marca 4, goteo 14), por
debajo del tope de 45; **nada activo entre f46 y f575**.

### 4.15 Lista de comprobación: que no se repitan los defectos del short 4

Cada punto se mide en el render antes de presentar (`SECO=1` + `control_encuadre.py` + una tira de 1 de cada 2 fotogramas).

| # | Defecto del short 4 (revisión) | Qué se comprueba aquí |
|---|---|---|
| 1 | Carreras que no avanzan, marcha atrás (v2 B1, B2) | Toda carrera usa `trayecto()`; recorre ≥ 2,1 u a 4,5–6,2 u/s; el pie de apoyo no resbala; **nadie corre en el sitio** |
| 2 | Cuerpos clavados (v3 A1, v4 M1 y M2) | **Ninguna pose idéntica más de 12 f** salvo las pausas de 6 f y los holds declarados; cambio de apoyo cada 18–24 f, desfase de 9 f; reposo vivo con el **doble de amplitud**; en cada hold de 40 f o más, algo cambia |
| 3 | Invitación sin gesto ni cara (v3 A2) | Tan **camina, recibe la regla y usa `invita`** (f438–f471); la cara cambia al menos una vez |
| 4 | Rival que patina fuera de cuadro (v3 A3, v4 b4) | El rival **nunca sale del cuadro salvo en su salida del goteo** (f856–f869); el cuerpo sentado lleva contorno claro y un pie a la vista; **sentado, no tendido** |
| 5 | Estrella sobre la cara (v3 M2) | La estrella nace en el punto real del contacto; ninguna estrella a menos de 0,5 u de la cabeza de Tin ni de Tan; el bloqueo **no lleva estrella** |
| 6 | Armas que se cruzan, remate «de sándwich» (v3 M3, v4 M3) | Nunca más de un arma en contacto con el rival a la vez; **Tin y Tan jamás golpean al mismo tiempo**; el bloqueo y el toque son de Tin solo |
| 7 | Rebote nervioso al retroceder (v3 M1) | Amplitud de paso ≤ 0,06 u en vertical; pasos de 0,4 u cada 8 f |
| 8 | Rival pegado al hombro (v3 M6, v4 b2) | Ninguna cabeza del rival a menos de 1,2 R de la de Tin o la de Tan salvo en vuelos de 2 f |
| 9 | Rival sobre la cabeza (E4) | El control no avisa E4; si avisa, separar 0,2 u en z |
| 10 | Onda con los dos agachados e iguales (v3 M4) | Tin y Tan **reaccionan distinto** (Tin se cubre, Tan se asombra) y retroceden con pasos |
| 11 | Decorado que tapa el contacto (v2 B10, v3 M5) | Ninguna pieza del patio tapa las piernas del golpeador ni la pausa; la regla se ve entera en su dibujo |
| 12 | Lápiz que cae pequeño (v4 b3) | El telescopio es de ≥ 2 R de largo y se lee en teléfono (se mide en el render) |
| 13 | Tan fuera de cuadro (v3 M7) | Tan en cuadro en **todos** los fotogramas de pelea y activa: golpes 2 y 5, invitación, esquives, mirada, consejo |
| 14 | Polvo en círculos que parecen ruedas (v4 b5) | El polvo es de partículas con contorno irregular, no círculos |
| 15 | Cámara lenta falsa de los personajes (v2 B6) | El reloj baja solo en vuelos, calcos y fuego; los personajes no «flotan» salvo el golpeado |
| 16 | Empalme del bucle con fondo distinto (D6) | Lo que debe casar casa (4.9); el fondo cambia, firmado |
| 17 | Cuerpos que cruzan con la cabeza detrás del torso (v3 M8) | Quien cruza por C1 lo hace 0,4 u por delante |
| 18 | Giros instantáneos (v2 B9) | Los giros de `mira` y de cuerpo duran ≥ 3 f; solo la mirada de Tan es de 2 f por tramo |
| 19 | **Nuevos** | (a) la regla no lleva números; (b) el paquete no lleva texto ni icono; (c) a Tin y Tan no los alcanza fuego, escombro ni onda; (d) ningún rojo sobre el cuerpo del rival; (e) ninguna arma ni silueta de fuego; (f) `comprobar_destellos` 0 avisos; (g) en c −30 no se mueve nada salvo la firma; (h) Tin sin lápiz en los dos planos de la firma; (i) nadie mira el telescopio salvo Tan, 6 f |

### 4.16 Pendientes de medir y decisiones que paso al director creativo

**Pendiente de medir (no los invento):**
1. R en u del motor y las medidas del patio (ancho, profundidad, alturas del farol y de la pila): fijan las posiciones de 4.2.
2. Alcance de Tin con la regla (para la regla de 75 %/50 % de la explosión).
3. Amplitud del `respira` de la v4 (para duplicarla).
4. Si `embiste`, `patada`, `golpe` y `bloqueo` cubren hombro, patada frontal, batazo y cruce de regla.
5. Criterio de 1,2 R en píxeles y distancia mínima entre el rival y Tin al cruzarse.
6. Si x +3,4 cae dentro de la zona útil; si no, x +2,6.
7. Que `comprobar_destellos` dé 0 con paleta B (fondo oscuro: un claro deslumbra más que sobre papel).
8. Todos los fotogramas, con la **voz real**; la distancia del objeto que cae a la última cifra (20 f o más).

**Cambios o lecturas mías que el director creativo puede revertir:**
1. **Golpe 1 con 4 f de anticipación y 4 de pausa.** Cumple «el más corto y seco»; si se prefiere la gramática completa, se mueven f80 a f76 y el vuelo a 4 f.
2. **Golpe 4: choque en f344, no al final del vuelo.** La flotación va después, pegado al poste, para que el fuego nazca en ≈ f344 y el golpe más fuerte conserve su suspenso.
3. **Rival en 1,0 hasta f553 y 0,9 desde f554** (el texto de 2.3 y el marcador discrepan).
4. **La mirada de Tan de 6 f incluye los giros.** Si el director creativo la quiere mantenida 6 f, el evento activo pasa de 20 f a ≈ 25 f y la suma a ≈ 43 f (tope 45).
5. **La marca de f812 va en la pestaña, no en el suelo.** Es mi lectura de «marca final donde se borra el rival».
6. **Las rasgaduras se cierran** (f584–f591): no queda cicatriz en el plano de cierre.
7. **La torre que cae en f262** (consecuencia del golpe 1) es mía: da una acción real entre f240 y f295 sin añadir ataques del rival.
8. **Tan no hace ningún gesto de dibujar** (es de Tin) y el consejo lo dice con dos negaciones de cabeza: así no le pongo el gesto de otro.
