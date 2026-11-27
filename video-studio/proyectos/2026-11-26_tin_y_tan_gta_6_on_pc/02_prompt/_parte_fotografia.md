<!--
Texto listo para pegar en direccion.md (secciones 3 y 3b), escrito por fotografia el 2026-11-27.
Reemplaza el pedido de las secciones 3 y 3b. No se editó direccion.md.
Sellos de manual/14 entre parentesis: (investigación), (oficio), (hipótesis del equipo). Toda cifra de cámara en unidades
del motor (u) es un VALOR DE PARTIDA para la vista previa, no una medida. Lo que se mide en el render va como «pendiente».
-->

## 3. Cámara y luz — director-de-fotografia

> Lee: `manual/13`, `canales/nostalgia-tin-y-tan/DESIGN.md` (control de color con profundidad), `PARAMETROS.md` sección 7,
> `estudios/2026-11-26_color_por_estadisticas_y_psicologia.md` (alternativa B) y, del short 4, su sección 3 y las
> revisiones v2 y v4 de fotografía. **Causa raíz de la v2 del short 4:** todas las cámaras miraban de frente, el
> televisor quedaba detrás del subtítulo y el rival tapaba la cara de Tin. Aquí se corrige desde el plano de partida:
> cámara baja y en diagonal, el motivo del centro fuera de la franja, y un carril por actor.

### 3.0 Reparto de la pantalla (zonas reservadas; coordenadas de la cámara de portada C0 y de los generales)

En planos con diagonal (`az` ≠ 0) las cosas se desplazan: **todas estas cifras se vuelven a medir en el render**
(pendiente del supervisor de continuidad). Despeje mínimo entre zonas: 30 px.

| Zona | Coordenadas (px) | Qué va y qué no |
|---|---|---|
| Útil | x 60–960, y 380–1440 | Caras, contactos, texto y objetos del tema. Los **pies** pueden bajar hasta y ≈ 1650 (valor de la portada del canal; la interfaz de Shorts puede tapar la parte baja: hipótesis de la revisión v4 del short 4, comprobar con plantilla) |
| Franja de subtítulos | y 885–1105 | **Prohibida** para caras, contactos, dato y rival. El panel es opaco (`#0B0F1F`, 100 %; lección A5 de la v2) |
| Dato, una línea o dos | x 60–960, y 670–855 | Tarjeta opaca. Despeje de 30 px con la pestaña (borde inferior 640) y con la franja (borde superior 885 − 30). Cabe: encabezado de 48 px + texto de 86 px (+ sello de 44 px **en el mismo renglón del encabezado**, a la derecha) |
| Tarjeta de medidas | y 855 hacia arriba: 1 renglón ≈ 635–855; 2 renglones ≈ 415–855 | Renglón = (título 48 px + cifra 86 px en la misma línea) + apoyo de 48 px en 2 líneas. **Es la única capa que puede tapar la pestaña** (la tapa por detrás, f374–f572); las demás tarjetas la dejan a la vista. Nunca pasa de y 380 |
| Pestaña (Z-AI) | x 80–330, y 400–640 | Cartón al fondo con marcas de asterisco en `#F3E9D2` (3,8:1 sobre el cartón `#9A6A45`, calculado). Texto de portada, dato y farol a 30 px o más (x ≥ 360) |
| Caída del objeto (Z-AD) | x 730–960, y 400–640 | Rasgadura en la parte alta (y 400–520, x ≥ 830). Libre de dato, subtítulo y farol desde f554 a f599 |
| Suelo de aterrizaje (Z-SU) | x 120–960, y 1125–1420 | El telescopio cae por x ≈ 850 y **queda quieto en x ≈ 640–720, y ≈ 1380–1420** (30 px por debajo del pasillo y a 30 px o más de la grieta y de la caja) |
| Pasillo de la firma | x 330–750, y 1100–1340, de c −30 a f30 | Solo el lápiz. Ni humo, ni gota, ni telescopio, ni caja registradora, ni resto del rival, ni la regla, ni el poste del farol |
| Grieta de entrada (Z-GR) | x 780–950, y 1350–1420, lado derecho | A 30 px del pasillo (750). Se abre en f30; no antes |
| Caja registradora rota | x 60–170, y 1340–1440, extremo izquierdo del suelo | Quieta desde f0; a 30 px o más del cuerpo de Tan en la portada (medir en f0) |
| Marca final (segundo asterisco) | dentro de Z-AI, junto al primero | Entra en f812–f815 (4 f); el dato 12 (tarjeta de y 670–855) entra en f816 y no la toca |

**Aviso de geometría (lo dejo a decidir antes del prompt):** con la franja prohibida en 885–1105, las caras de Tin, Tan y
el rival caben solo en y 1105–1440; con los pies en y ≈ 1650 eso da personajes de **≈ 340–360 px (18–19 %)** y un rival
de **≤ 545 px aparentes**. El rival «de 1,5 veces» se logra por **profundidad** (un carril más lejano), no por altura: si
se le pone la altura de 1,5 veces al lado de Tin (≈ 520 px) con los pies en el mismo carril, su cabeza cruza la franja
en f46–f87. Lo que lo hace grande: su ancho de madeja (1,35 R de radio contra 1 R de la cabeza de Tin) y la sombra.
Si el director creativo prefiere personajes más grandes, la salida es bajar el límite útil de 1440 a ≈ 1600 (hipótesis,
comprobar con plantilla de la interfaz) o aceptar los **dos tramos sin voz** (f554–f599 y f695–f727), donde no hay
subtítulo ni dato y la zona 380–1440 entera es de la acción.

### 3.1 Luz y paleta del escenario (uno solo: el patio de carga, de noche, exterior)

**Paleta B (`motor_de_accion/paletas/b_noche_de_tinta.json`): CONFIRMADA, con cuatro correcciones de uso (no de hex).**

| Elemento | Hex | Para qué | Medido / calculado (WCAG, fórmula del estudio) |
|---|---|---|---|
| Fondo (mundo lejano) | `#141B33` | Cielo y muros lejanos | contra línea 14,1:1 |
| Suelo | `#27304F` | Piso del patio | contra línea 10,7:1 |
| Apoyos del fondo | `#3A4570` (bloque cerca), `#1C2444` (bloque lejos), `#5A6690` (polvo), `#0B0F1F` (sombra y panel de subtítulo) | Volumen por capas: lo lejano más azul y con menos contraste (perspectiva aérea, R7, investigación) | bloque lejos casi se funde con el fondo, por diseño |
| Línea y texto | `#F3E9D2` | Contorno de Tin, Tan y rival; texto; armas; marcas de la pestaña | sobre `#0B0F1F`: 15,8:1 |
| Rival | `#B79CFF` | Tinta de la madeja (ver 3.4) | contra fondo 7,5:1; contra suelo 5,7:1 |
| Acento | `#4FE3FF` | Solo detrás del dato (3b) | contra fondo 11,2:1; contra suelo 8,5:1 |
| Fuego | núcleo `#FFE45C`, borde `#B81414` | Plano, dos tonos con escalón duro | núcleo contra fondo 13,4:1; borde 2,6:1 |
| Humo | `#9A6A45` con contorno `#0B0F1F` | Humo y cajas de cartón | contra fondo 3,7:1 |

Correcciones de uso, cada una con su causa medida:

1. **Tan contra el suelo da 2,7:1** (estudio; no llega a 3:1): Tan **siempre lleva contorno `#F3E9D2`** y nunca se coloca en un
   pozo de luz más oscuro que el suelo. Tin da 4,3:1 contra el suelo y 5,7:1 contra el fondo.
2. **El humo y la cabeza de Tan tienen la misma luminosidad** (calculé 1,02:1 entre `#9A6A45` y `#2F7F7A`); los separa
   solo el tono (ΔE 52 / 37 / 27 en visión normal, deuteranopía y protanopía, del estudio; el umbral del equipo es 20,
   hipótesis). Por eso: el humo **va siempre detrás de Tan**, tiene contorno `#0B0F1F` y la cabeza de Tan, su contorno
   claro. Se mide el par en el render (pendiente).
3. **El borde rojo del fuego da 2,6:1 contra el fondo y 1,9:1 contra el suelo.** No se corrige el hex: el rojo oscuro es lo que
   mantiene seguro el destello (sin rojo saturado que parpadee). La figura del fuego se lee por el **núcleo** (13,4:1).
4. **El acento cian y el rival lila se acercan en deuteranopía** (ΔE ≈ 20, en el límite): nunca comparten zona (el dato es
   una tarjeta opaca y el rival nunca está detrás de ella) y se separan por forma.

**Esquema de luz (el mismo en todas las tomas del patio):**

- **Luz principal: el farol.** Cabeza de lámpara `#F3E9D2` con halo `#5A6690`, en x ≈ 700–860, y ≈ 560–640 (brazo desde un poste
  cercano en x ≈ 940, pie en y ≈ 1500). Su luz es un **pozo frío** sobre el suelo (el suelo sube de `#27304F` hacia `#3A4570`
  en un óvalo de ≈ 520 px de radio centrado hacia x ≈ 780, y ≈ 1450), con borde duro de dibujo, no degradado. Cae de arriba y
  un poco atrás: las sombras de contacto van hacia la cámara.
- **Los personajes no se tiñen:** la luz no cambia sus colores (regla: Tin y Tan conservan los suyos; `DESIGN.md`). La luz se
  lee en el suelo, en las cajas y en el contorno claro de los cuerpos.
- **Relleno: ninguno.** La noche es fría y plana; el mundo lejano no recibe luz.
- **El fuego es la única luz cálida del video** y llega con el peligro: pequeño en f344 (cajas junto al farol), grande en la
  explosión f702–f726. Es plano y no ilumina con degradado. Lo cálido aparece solo cuando sube la tensión (hipótesis del
  equipo; se mide en la retención de f344 y f700–f732).
- **Sombra de contacto:** `#0B0F1F` a 0,55 de opacidad (sobre el suelo apagado la sombra da solo 1,5:1, por eso más densa que la
  del short 4, que era 0,2–0,3 sobre papel); óvalo bajo cada pie. Dentro del pozo de luz sube a 0,6.
- **Fondo que no compite:** el mundo (`#141B33` a `#3A4570`) tiene menos saturación que los personajes y que el rival (regla del
  cap. 03). El único punto de máxima luminosidad de cada plano es el que se quiere mirar (R33, investigación).

### 3.2 Tabla de cámaras y planos (25 planos, 24 cortes)

Lente: «FOV» es el ángulo vertical del motor. Base 46° (la del short 4, normal-abierta); 30–36° tele para detalle;
52–56° abierta para generales fijos y el pico. `az` positivo = la cámara se corre al lado de Tin (derecha del eje);
negativo, al lado de Tan. `h` = altura de la cámara en u (Tin mide ≈ 1,9 u; ojos ≈ 1,7; cintura ≈ 1,0; ras de suelo ≈ 0,4).
**Todos los valores son de partida, a probar en la vista previa.** Velocidad máxima de cámara: ≈ 8 % del ancho por segundo
(`manual/14`, sección 6); calculé con ancho visible ≈ 0,48·D a FOV 46°.

| # | f | Dur. | Emoción | Plano | Ángulo (h; az) | Lente | Movimiento (velocidad; inicio → fin) | Luz | Frase de cámara (inglés) |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 0–29 | 30 f | Curiosidad | General frontal de portada (C0), monitor apagado al centro | Altura de ojos (C0 del canal); az 0 | La de C0 | **Fija** | Pozo del farol sobre el pasillo; pestaña y caja a la vista | `static locked-off shot, eye level, night loading yard, dark monitor on stacked towers at center` |
| 2 | 30–45 | 16 f | Curiosidad | **Subjetivo de Tan** (equivalente: cámara en su sitio, sin verse él), mirando a la grieta | h 1,7; az +24 | FOV 52 | **Empuje lento +3 %** (≈ 5,6 %/s); inicio abierto → fin sobre la grieta | Pozo del farol al fondo; la grieta se abre en `#0B0F1F` con filo `#F3E9D2` | `low POV from the smaller figure's eye level, slow push-in as a crack opens in the ground and ink rises out of it` |
| 3 | 46–75 | 30 f | Curiosidad | General bajo, ¾ desde la izquierda; Tan retrocede, Tin avanza, el rival crece | h 1,1; az −20 | FOV 46 | **Fija** | Pozo del farol: el rival crece dentro de la luz | `low three-quarter wide shot from the left, static, the ink figure grows as the two stick figures step apart` |
| 4 | 76–99 | 24 f | Determinación | **Golpe 1** (K = f88; Tin, puño, sin arma): medio-general lateral, ¾ desde la derecha | h 1,0; az +22 | FOV 46 | **Fija** | El contorno claro de Tin se lee contra la noche | `low three-quarter medium-wide shot from the right, static, a single straight punch` |
| 5 | 100–117 | 18 f | Impacto | El rival choca con la pila de torres; una cae rota (P-007) | h 0,7; az −18 | FOV 40 | **Fija** | Torres en `#3A4570`; polvo `#5A6690` con contorno | `low close three-quarter shot of a stack of computer towers, static, one tower splits and falls` |
| 6 | 118–143 | 26 f | Tensión | **Golpe 2** (K = f130; Tan, cuerpo): el rival se levanta y Tan golpea | h 0,9; az −20 | FOV 46 | **Fija** | Idem | `low three-quarter wide shot from the left, static, one figure rises and the other strikes it in the body` |
| 7 | 144–185 | 42 f | Tensión | General bajo: contraataque del rival que falla, esquive | h 1,3; az +12 | FOV 46 | **Paralaje lateral lento**: 0,4 u en 42 f (≈ 7 %/s), de izquierda a derecha | Cajas de cartón `#9A6A45` entre cámara y acción, fuera de las caras | `low wide shot, slow lateral drift past stacked cardboard boxes, a swing misses and the target dodges` |
| 8 | 186–229 | 44 f | Determinación | **Golpe 3** (K = f212; Tin, cuerpo): cajas y un monitor se rompen | h 0,8; az +26 | FOV 46 | **Fija** | Pozo del farol rompe en las cajas | `low three-quarter medium-wide shot from the right, static, boxes and a monitor burst apart` |
| 9 | 230–295 | 66 f | Tensión | General alto-medio, frontal casi (az pequeño): el rival se tambalea, Tan y Tin se acomodan | h 1,6; az −8 | FOV 46 | **Fija** | Estático | `medium-high wide shot, static, the figure staggers among broken boxes` |
| 10 | 296–329 | 34 f | Curiosidad | **Detalle (objeto):** el lápiz de Tin dibuja la regla de tinta; casi quieto | h 1,2; az +10 | FOV 30 (tele) | **Fija** (sin movimiento; la acción es la mano) | La línea clara nace sobre fondo oscuro; luces del farol desenfocadas al fondo | `macro close-up of a pencil tip drawing a long ink ruler, static, distant lamp lights softly out of focus` |
| 11 | 330–343 | 14 f | Determinación | **Medida 1** (K = f336; Tin, regla): golpe contra el poste del farol | h 0,6; az −16 | FOV 50 | **Fija** | La lámpara oscila | `low three-quarter wide shot from the left, static, a long ruler strikes a figure into a lamp post` |
| 12 | 344–373 | 30 f | Tensión | Chispas del farol y fuego pequeño en las cajas; el rival, contra el poste | h 0,5; az +8 | FOV 54 | **Fija** (el contrapicado deja la lámpara en la banda alta) | Fuego plano `#FFE45C`/`#B81414`; primera luz cálida | `worm's-eye wide shot, static, sparks fall from a swaying street lamp onto cardboard boxes catching a small flat fire` |
| 13 | 374–437 | 64 f | Tensión | General bajo con la tarjeta de medidas (renglón 1) | h 1,2; az −12 | FOV 46 | **Paralaje lateral lento**: 0,5 u en 64 f (≈ 5,8 %/s) | Fuego pequeño a la derecha; pozo del farol | `low wide shot, slow lateral drift, small flat fire at the back right, the dark monitor on the towers stays centered` |
| 14 | 438–471 | 34 f | Complicidad | **Héroe abierto de los dos (cerca de la mitad, 47–51 %):** Tan y Tin juntos, de cuerpo entero; Tan recibe la regla | h 0,9; az +10 | FOV 46 | **Fija** | Contorno claro; el rival baja del poste al fondo, fuera de las caras | `low three-quarter hero shot of the two figures side by side, static, the ruler passes from one to the other` |
| 15 | 472–497 | 26 f | Determinación | **Medida 2** (K = f484; Tan, regla): el rival choca con la persiana metálica | h 0,8; az +24 | FOV 46 | **Fija** | La persiana se abolla (daño que se queda) | `low three-quarter medium-wide shot from the right, static, a figure slams into a metal shutter and dents it` |
| 16 | 498–553 | 56 f | Tensión | General bajo con la tarjeta de medidas (renglón 2, desde f529) | h 1,4; az −8 | FOV 46 | **Fija** | Estático | `low wide shot, static, the large figure peels away from the shutter` |
| 17 | 554–599 | 46 f | Extrañeza leve | **General fijo del respiro 2, cielo libre.** Rasgadura (f573–f575), caída f576–f587, rebote f588–f595, Tan mira f588–f593 | h 1,3; az +6 | FOV 52 | **Fija** | El telescopio cae por x ≈ 850; sin subtítulo ni dato | `static wide shot, empty night sky above, a small cardboard object falls through a torn slit in the air and bounces once` |
| 18 | 600–651 | 52 f | Suspenso | El rival dibuja una caja lisa de tinta y la desliza hacia ellos | h 0,8; az +16 | FOV 44 | **Empuje lento +6 %** (≈ 3,5 %/s) hacia la caja | La caja `#3A4570` con borde lila, sin texto ni icono | `low three-quarter medium shot, slow push-in toward a plain ink box sliding across the ground` |
| 19 | 652–677 | 26 f | Contención | **Bloqueo** (f652): Tin frena la mano de Tan con la regla. **Se lee en silueta** | h 0,8; az ±35 (casi perfil) | FOV 42 | **Fija** | Contornos claros contra el pozo del farol | `low near-profile medium shot, static, one figure stops the other's reaching hand with a long ruler` |
| 20 | 678–699 | 22 f | Suspenso | **Detalle (objeto):** la caja y la punta de la regla que se acerca; sin voz | h 0,5; az +10 | FOV 34 (tele) | **Fija** | Misma luz de farol desenfocada al fondo | `close-up of a plain ink box on the ground, static, a ruler tip enters the frame from far away` |
| 21 | 700–732 | 33 f | Sorpresa | **Pico, general abierto (clímax):** toque en f700, explosión f702–f726; el rival queda chamuscado | h 0,4; az 0 | FOV 56 | **Fija** | Ver 3.3, destellos: máscara y tope | `static ultra-wide low-angle shot, the whole yard in view, a fireball blooms upward from the ground between the figures` |
| 22 | 733–799 | 67 f | Humor seco | **Revelado, plano fijo (respiro 3):** el humo despeja; el rival se vuelve a plantar a 0,8 | h 1,5; az −6 | FOV 50 | **Fija** | Humo con contorno, detrás de Tan | `static wide shot, thick outlined smoke clears slowly to reveal a singed figure standing up again` |
| 23 | 800–836 | 37 f | Alivio | **Golpe final** (K = f812; Tin, regla) e implosión f814–f831; segundo asterisco en la pestaña | h 1,0; az −20 | FOV 52 | **Fija** (la pestaña queda en cuadro) | La implosión se lleva humo y fuego | `low three-quarter wide shot from the left, static, everything collapses inward into one point and the smoke is pulled away` |
| 24 | 837–899 | 63 f | Alivio | **General fijo de remate:** el resto goteando por el borde izquierdo (f856–f869); Tin lanza el lápiz a Tan | h 1,3; az +8 | FOV 50 | **Fija** | Sin humo ni fuego; daños a la vista | `static wide shot, the last ink drips off the left edge, a pencil is tossed between the two figures` |
| 25 | 900–929 | 30 f | Curiosidad | **Portada de cierre** (C0, mismos pose, texto y cámara que el plano 1) | Altura de ojos; az 0 | La de C0 | **Fija** | Pozo del farol; daños conservados (excepción del fondo, la del short 4) | `static locked-off shot, same framing as the first frame, eye level, night loading yard` |

**Cuenta:** 25 planos, 24 cortes en 31,0 s (rango de `PARAMETROS.md`: 8 a 25). **Cortes de impacto: uno solo** (el pico, con
las inversiones de 3.3); los demás cortes son «en el movimiento». Planos frontales (az 0 o casi): 1, 21, 25 y, con
poco ángulo, 9 y 17; **veinte de los 25 son en diagonal o a ras de suelo** (la causa de la v2 del short 4 era lo contrario).

**Qué se prueba primero en la vista previa:** (a) planos 2, 3 y 4: que el rival no tape la cara de Tan ni de Tin (la cara de
quien habla queda a la vista en cada plano); (b) plano 11: que el poste y la lámpara entren en cuadro sin que el rival suba
a la lámpara; (c) plano 17: que la caída entera (de y 400 a y 1400) quepa con el FOV de 52°.

**Ajustes que hice al plan del director creativo, porque la geometría lo pide:**

1. **Medida 1: el rival choca con el poste del farol, no sube a la lámpara.** Subir al farol cruzaría la franja de subtítulos
   (línea 6, f338–f432) con el cuerpo del rival. Las **chispas** son las que suben y bajan, y la lámpara oscila en la banda alta.
   Se mantiene «baja del poste» en f438–f471. Lo validan el director creativo y animación.
2. **El rival no mide 1,5 veces en altura aparente**, solo en el mundo (ver el aviso de 3.0).
3. **Ningún vuelo ni salto de nadie pasa por la franja de subtítulos con una cara dentro** (pedido a animación).

**Movimientos caros:** ninguno. No hay órbita, FPV ni dolly zoom. El subjetivo del plano 2 es barato (cámara en el sitio de Tan,
sin dibujarlo) y el `az` ya existe en el motor desde el short 4 (hasta 30°). **No hay versión «segura» que ofrecer:** si
el subjetivo del plano 2 no se ve claro en la vista previa, se cambia por un general bajo desde el lado de Tan (az −24),
fijo, y se pierde solo el «subjetivo» de la tabla de tipos de plano.

### 3.3 Qué se hace en edición y qué no

- **Capa de datos, subtítulos quemados, sello de fecha, ajuste a la voz real y mezcla:** edición, como pide el director creativo.
  El panel del subtítulo es **opaco** y la tarjeta del dato, también.
- **Sin subtítulo y sin dato en f554–f599 y f695–f727** (la voz calla); sin subtítulo en los planos 1 y 25.
- **Sin zooms, sin `whip pan`, sin cámara lenta, sin reencuadre en edición.** Cada uno comunica movimiento que aquí no hace falta:
  los tiempos de golpe son los medidos (anticipación 6 f, pausa 6 f, contacto 2 f); una cámara lenta los cambiaría y
  movería los fotogramas de la voz (R22, oficio). El formato es vertical nativo: no se reencuadra.
- **El pico f700–f732 y la implosión f812–f831 (lo único que puede dar luz fuerte):** (hipótesis del equipo; se mide con
  `comprobar_destellos` en esta paleta, que es el control crítico por ser oscura)
  - máximo **3 destellos por segundo** (R42 y R43, investigación); en f702–f712 una sola secuencia: dos cuadros invertidos y,
    a 3 cuadros de distancia, un claro de paleta `#F3E9D2` **con máscara circular de ≤ 30 % del cuadro y opacidad ≤ 0,45**
    (el short 4 usó 55 % y 0,6 sobre papel; sobre fondo oscuro el salto de luminosidad es mucho mayor);
  - **nunca blanco puro a pantalla completa**; el borde rojo del fuego no parpadea ni cubre más de un cuarto del cuadro en dos
    fotogramas seguidos; el cian del dato no se usa en destellos;
  - antes del toque, silencio de imagen: nada se mueve en f694–f699 salvo la regla que avanza.
- **Transición de cierre:** corte seco de f899 a f900. Si el editor conserva el borrón de 3 f de la firma, lo aplica **solo a la
  escena, nunca a la capa de texto** (lección M8 de la v4).

### 3.4 Color del rival en esta hoja (decisión)

**Tinta lila `#B79CFF` para la línea de la madeja, el cuerpo y el rizo.** Por qué:

- En un mundo `#141B33` la tinta oscura de su ficha no se vería (1,0:1): su «tinta» se ve en la hoja Noche como tinta clara, igual
  que la de Tin y Tan pasa de oscura a `#F3E9D2`. El lila fue el tono que más se separó de todos en la medición del estudio:
  de Tin ΔE ≈ 102, de Tan ≈ 73, del humo ≈ 79, de la línea ≈ 70, y se lee a 7,5:1 contra el fondo (investigación: el
  contraste de luminosidad es lo que no cambia con el daltonismo; H16).
- **No hay respaldo para una emoción del lila** (el estudio lo dice: elegido por distinguibilidad, no por emoción). Aquí
  solo se pide que no sea rojo, ni se acerque a «sangre», ni se confunda con el fuego, con Tin ni con Tan.
- **Los dos huecos de los ojos:** óvalos `#F3E9D2` con contorno `#0B0F1F` (el contorno separa el hueco del lila, 8,4:1; sin
  pupilas ni boca). Se conservan «de papel» para que no den miedo (perfil emocional).
- **Chamuscado tras el pico (f726 en adelante):** salpicaduras de hollín `#0B0F1F`; **el lila no cambia de hex y no hay rojo ni
  marrón sobre su cuerpo** (regla 2.1.7: ningún rojo sobre su cuerpo). Fuego y humo pasan por detrás o delante, nunca lo tiñen.
- **Paquete de tinta:** relleno `#3A4570` con contorno lila, liso, sin texto, icono ni flecha (regla 2.1.4).
- **Esto enmienda la ficha** (`personajes/duda/ficha.md`: «solo tinta», «pintarla de cualquier color» prohibido) **solo para la
  hoja Noche**, porque la tinta de la hoja es clara; la decisión de la línea de papel y del rival lila la cubre el sí del
  dueño del 2026-11-26 a la paleta B (`«me gustan los A, B y C»`). Si el dueño no la dio por cubierta, se le pide la
  confirmación antes de dibujar: es una decisión de identidad.
- **Marcador de avance:** el tamaño baja con cada dato (regla de su ficha), el color no cambia.

### 3.5 Motivos visuales que vuelven (2) y fondo que se mantiene

- **La regla de tinta, hecha con el lápiz** (`#F3E9D2`): nace en el plano 10, es el arma de los planos 11, 14, 15, 19, 20 y 23, se
  deshace en gotas al final. Es el motivo del video y también el lápiz de la firma (identidad, no acento).
- **El monitor apagado sobre la pila de torres, en el centro** (portada, planos 1, 5, 13, 21, 22, 24 y 25). Pantalla `#0B0F1F` con
  una franja de reflejo `#27304F`, sin cian ni ningún dato: es lo que hay de GTA 6 en PC. Regresa en el plano final con la
  pila rota. Está dentro de y 720–1100, fuera de la franja y de la tarjeta (y 670–855 queda por encima del pie de la pila
  cuando hay una sola línea de dato; la tarjeta de medidas sí lo tapa: planos 13 y 16, lo declaro).
- **Fondo que se mantiene entre los planos de objeto (10 y 20):** las luces del farol desenfocadas y la persiana al fondo.

### 3.6 Tipos de plano (video de 31 s)

| Tipo | Plano | f | % del video | Nota |
|---|---|---|---|---|
| Detalle (objeto) | 10 y 20 | 296–329 y 678–699 | 32–35 % y 73–75 % | El lápiz que dibuja la regla; la caja con la punta de la regla |
| Subjetivo (equivalente) | 2 | 30–45 | 3–5 % | Entrada del rival por la grieta; ver «movimientos caros» |
| **Héroe abierto, cerca de la mitad** | 14 | 438–471 | 47–51 % | Tan y Tin juntos; **es donde se reconoce a los personajes** (la invitación) |
| Héroe abierto, clímax | 21 | 700–732 | 75–79 % | Pico; lo fijó el director creativo |
| Revelado | 22 | 733–799 | 79–86 % | El humo despeja |
| General fijo del respiro 2 | 17 | 554–599 | 59–64 % | Cielo libre; cae el objeto |

Los planos medios o más cerca de Tin y Tan (reconocimiento) son 3, 4, 5, 8, 14, 15, 18, 19 y 23. Los generales sin cara legible
son cortos (1 y 25 con las caras de la portada; 17, 22 y 24 con la cara a ≈ 19 %).

### 3.7 Grabación propia

No aplica: todo se dibuja por código y nadie graba.

### 3.8 Continuidad y eje

- **Tomas encadenadas con el último fotograma:** ninguna (un solo render por código). El plano 25 repite el plano 1 (cámara,
  texto y poses) y el fotograma 0 es el paso siguiente del lanzamiento del lápiz; el fondo del cierre conserva los daños (la
  excepción declarada del short 4).
- **Eje de acción (regla de los 180°):** Tan a la izquierda y Tin a la derecha, mirando hacia el rival, que entra por la derecha.
  **La cámara siempre está del lado del público**: `az` alterna entre +26° y −20° pero nunca pasa a la espalda de los
  personajes. **Sin cambio de lado de Tan y Tin en todo el video** (defecto B2 de la v2 del short 4); el plano 19 (casi perfil)
  es el que más se acerca al eje y no lo cruza. Cada golpe ocurre con los dos en el mismo carril.
- **Que no se parezca al short 4 puesto uno tras otro (F6):** hoja, paleta, hora y lugar distintos (noche de tinta, patio exterior,
  acento cian y no amarillo, rival lila y no negro); la luz viene de un farol y no de una tienda pareja; cámara baja y
  en diagonal contra la general alta y frontal del short 4; el objeto del centro es un monitor apagado sobre torres y no un
  televisor; **un solo cuadro de impacto** (el short 4 llevaba cinco). **Lo que se parece y no se puede cambiar:** el plano de
  portada C0 (frontal, a la altura de ojos) por la firma. Si al ponerlos seguidos los dos primeros segundos se leen
  igual, se avisa al jefe de producción antes del prompt.

### 3.9 Lo que pido y queda pendiente

| A quién | Qué |
|---|---|
| Animación | Rasgadura no antes de f573 (la tarjeta de medidas sale en f570–f572); la caída por x ≈ 850; ningún vuelo con cara dentro de la franja; el golpe de f336 contra el poste, no la lámpara; el hollín del rival sin rojo; las máscaras del pico (≤ 30 % del cuadro) |
| Producción | Entorno `patio_tienda_de_computadoras`: pila de torres con monitor, poste y lámpara del farol (pozo de luz como óvalo 2D, no luz real: así los personajes no cambian de color), persiana, cajas, pestaña con marcas en `#F3E9D2`, grieta de entrada, caja registradora rota. Plantilla de la interfaz de Shorts para comprobar los pies (y ≈ 1650). `comprobar_destellos` sobre la paleta oscura; `geometria_firma` y `comprobar_firma` sobre el fotograma 0 |
| Editor | Panel de subtítulos y tarjeta opacos; sin subtítulo ni dato en f554–f599 y f695–f727; el texto de portada va en x 360–960, y 400–640, a la derecha de la pestaña (dos renglones de 80 a 86 px: **medir** que «GTA 6 on PC?» quepa en 600 px; si no, tres renglones de 92 px como permite `DESIGN.md`) |
| Supervisor de continuidad | Medir en el render: todas las coordenadas de 3.0; el par humo–Tan; `revisar_color.py`; destellos; la franja de subtítulos libre de caras |
| Director creativo | Aviso de geometría de 3.0 (personajes ≈ 18–19 %; rival por profundidad); el ajuste del poste del farol; la tarjeta de medidas tapando la pestaña |

---

## 3b. Color con intención — director-de-fotografia (valida director-creativo)

> `manual/13_color_con_intencion.md`, `DESIGN.md` y `estudios/2026-11-26_color_por_estadisticas_y_psicologia.md`
> (alternativa B). Regla: 2 neutros + 1 acento. **Tin y Tan conservan sus colores** (dueño, 2026-11-26: «Sí a los 3»).

- **Neutros (2):**
  - **Azul noche `#141B33`:** fondo y mundo lejano, con su escala de apoyo (suelo `#27304F`, bloque cerca `#3A4570`, bloque
    lejos `#1C2444`, polvo `#5A6690`, sombra y panel de subtítulo `#0B0F1F`). Fija el tono: noche, tecnología.
  - **Papel `#F3E9D2`:** línea de los cuerpos, texto, armas y marcas de la pestaña. Contra el fondo 14,1:1; contra `#0B0F1F`
    15,8:1; contra el suelo 10,7:1. Es el papel del canal: se reconoce entre Shorts aunque cambie la hoja.
- **Acento (1): cian `#4FE3FF`.** Va **solo detrás del dato**: placa llena detrás de la palabra o cifra clave (texto `#141B33`
  encima, 11,1:1) y, en los nombres de marca, **solo como subrayado** (el 40 % inferior de la altura de la letra, trazo de
  mano, inclinado ≈ 2°, sin placa llena). Placa llena en: **«not announced»** (f97), **«574 days»** (f379), **«≈ 1 year»**
  (f534), **«some carry malware»** (f735) y **«no official date»** (f821). Subrayado en: «GTA 6», «Rockstar», «PlayStation 5»,
  «Xbox Series X|S», «Red Dead Redemption 2», «Malwarebytes» y «Huntress». **También lleva el acento** el relleno de las dos
  barras de la tarjeta de medidas, porque son el dato: dos barras sueltas de largo proporcional a 574 y 375 días, sin eje
  común, sin tercera barra y con cada una sus dos fechas (regla 2.1.3).
  **No va en:** Tin, Tan, el rival, armas, entorno, farol, pestaña, fuego, humo, estrella de impacto (es `#FFE45C`),
  subtítulos ni destellos. Un acento por plano: nunca a la vez que el pico (el dato no comparte plano con él).
- **Placa de más contraste del video:** «not announced» al principio y «no official date» al final llevan la placa llena de
  cian más grande y quieta más tiempo (108 y 70 f); son la promesa del título. Pasan 11,1:1.
- **Color del rival:** lila `#B79CFF` (ver 3.4). **Colores de efecto (declarados aparte):** fuego núcleo `#FFE45C` y borde
  `#B81414`; estrella `#FFE45C`; humo `#9A6A45` con contorno `#0B0F1F`; cajas y utilería `#9A6A45`.
  **Identidad (no cuenta como acento):** naranja de Tin `#E07A2E`, verde azulado de Tan `#2F7F7A`, mostaza de bufanda y lápiz
  `#E8B33B`, goma tomate `#C8553D`.
- **Contrastes de texto (calculados con la fórmula de WCAG; los medidos en el render van como pendiente):**

| Texto | Fondo | Contraste | Mínimo |
|---|---|---|---|
| Subtítulo `#F3E9D2` | panel opaco `#0B0F1F` | 15,8:1 | 4,5:1 |
| Dato `#F3E9D2` | tarjeta opaca `#0B0F1F` | 15,8:1 | 4,5:1 |
| Dato `#141B33` | placa cian `#4FE3FF` | 11,1:1 | 4,5:1 |
| Sello «as of …» `#F3E9D2` (44 px) | tarjeta opaca | 15,8:1 | 4,5:1 |
| Texto de portada `#F3E9D2` | cielo `#141B33` | 14,1:1 | 4,5:1 |

- **Tamaños:** dato de 86 px o más de alto de letra; apoyo y renglones de tarjeta, 48 px o más; sello, 44 px o más; 3 renglones a
  la vista como máximo. Públicos de 45 años o más: son casi nulos en Studio (estudio, tabla 1), así que vale 4,5:1 y no 7:1;
  los pares de arriba pasan además de 7:1 salvo el del sello contra el cian, que no existe.
- **Por qué cada color** (para este público; hipótesis, no significado fijo):

| Color | Qué comunica y qué emoción busca | Respaldo | Métrica |
|---|---|---|---|
| Azul noche | Cambia de golpe el aspecto del canal en el feed (el short 4 era claro) y pide concentración. Emoción: tensión baja y sostenida | Luminosidad baja da tensión (`manual/13`, 4) (oficio). **En contra:** más luminosidad da más activación (H6) y el celular a pleno sol se ve peor oscuro (hipótesis); lo saturado se ve más luminoso en lo oscuro (H19) (investigación) | «Se quedó a mirar»; reparto por dispositivo |
| Papel (línea y texto) | Siluetas legibles y la respuesta que se lee sin sonido. Emoción: claridad | Contraste ≈ 14:1 (H17, oficio); lo que se lee fácil se cree más (R27, investigación) | Porcentaje medio visto; retención en cada dato |
| Cian detrás del dato | «Esto es lo comprobado»: el punto más luminoso y frío del plano; el ojo va solo ahí. Emoción: certeza tras el golpe | Un solo elemento distinto se mira primero (R33, investigación); máxima saturación y luminosidad atraen la atención (H7); azul como familia preferida (H1, H4). **Que señale «certeza»: hipótesis del equipo** | Retención en f97, f221, f379, f534, f659, f735 y f821 |
| Lila del rival | Solo se separa de todo y se ve sobre noche. Sin emoción propia | Elegido por medición, no por emoción (estudio, B) (hipótesis del equipo) | Retención en f30 a f69 (cuando entra) |
| Fuego plano amarillo y rojo oscuro, única luz cálida | Peligro de dibujo; sube la tensión. Emoción: sobresalto breve | Rojo y amarillo como señal de peligro (H11, H12); activación (H6) (investigación) | Retención en f344 y en f700–f732 |
| Humo pardo con contorno | «Esto se quemó»; despeja para el dato | Humo pardo oscuro: el único que se separa de Tan, Tin y el rival a la vez (nota del humo del estudio) (oficio) | Ninguna propia (es condición de lectura) |

- **Cómo ayuda al objetivo:** Programa de socios → vistas calificadas del feed → el primer cuadro se distingue del del short 4
  (hoja clara y amarillo) y se lee en menos de un segundo: noche, siluetas claras y un monitor apagado → **«se quedó a mirar»**
  (KPI, no más de 5 puntos bajo el short 4). Después el cian aparece solo donde hay un dato: quien lo aprende en el primer
  golpe sabe dónde mirar en los siguientes → **retención en f97, f221, f379, f534, f659, f735 y f821**. La placa
  de «not announced» (al inicio) y la de «no official date» (al final) son la promesa del título y los puntos de más
  contraste: que la respuesta honesta no pase inadvertida es lo que separa este video del clickbait → **ningún aviso;
  ningún comentario del tipo «no respondió»**. La luz cálida del fuego, solo en f344 y en el pico, ayuda a que el pico se
  sienta distinto (retención en f700–f732). Que el color mueva una métrica: **hipótesis del equipo** (H8 y H9: hay dos
  resultados nulos; el color es condición para que se lea la acción, no una palanca probada de retención).
- **Riesgos de lectura:**
  1. **Cian junto a nombres de marca:** el cian `#4FE3FF` no es el color de ninguna de las marcas nombradas que conozco, pero
     **no tengo cargada su fuente** (regla 6 del cap. 11). Pendiente: compararlo con el color oficial de PlayStation, Xbox,
     Rockstar, Malwarebytes y Huntress tomado de una fuente abierta; si queda a ΔE < 25 de alguno, cambia el acento. Por eso
     en las marcas el acento va como subrayado.
  2. **Humo pardo y cabeza verde azulada de Tan:** misma luminosidad (1,02:1); los separa el tono, que con daltonismo baja
     (ΔE 37 y 27, protanopía en el límite). Mitigación: el humo va detrás de Tan, con contorno oscuro, y Tan con contorno claro.
  3. **Cian y lila en deuteranopía** (ΔE ≈ 20): nunca comparten zona.
  4. **Tan contra el suelo, 2,7:1:** siempre con contorno claro.
  5. **Fondo oscuro en un celular con brillo bajo o a pleno sol** (hipótesis del equipo): el dato va en tarjeta opaca y se mide
     el contraste; el panel del subtítulo es opaco.
  6. **Destellos sobre fondo oscuro:** el salto de luminosidad es mayor que sobre papel. Tope de 3.3 (máscara ≤ 30 %,
     ≤ 3 por segundo, nada de blanco a pantalla completa); `comprobar_destellos` es el control crítico.
  7. **Rojo:** el borde del fuego no parpadea, nunca cubre más de un cuarto del cuadro en dos fotogramas seguidos y **nunca
     toca el cuerpo del rival**.
  8. **Daltonismo rojo–verde (≈ 8 % de los hombres):** ninguna información se separa solo por rojo contra verde; el fuego y Tin
     se separan por luminosidad (núcleo 13,4:1 contra 5,7:1 de Tin) y por contorno.
  9. **Esquina izquierda del cuadro:** la caja registradora y la pestaña están a la izquierda; el pozo del farol está a la
     derecha. Si el cuadro se ve cargado a la izquierda, se mueve la caja, no la pestaña.
- **Control de color con profundidad (criterio para esta hoja; sigue `DESIGN.md`, «Control de color en videos con
  profundidad», firmado en parte el 2026-11-24):**
  1. **Fotograma nítido de control** de cada plano con profundidad (mismas capas, sin desenfoque, sombras ni grano):
     **≥ 85 %** dentro de la paleta declarada (neutros, apoyos, acento, rival, efectos e identidad).
  2. **Fotograma final: ≥ 75 %**, y lo que quede fuera tiene que ser mezcla de colores de la paleta: ningún color dominante
     (k-medias de `revisar_color.py`) con más del 3 % del cuadro a ΔE76 ≥ 12 de la recta entre dos colores de la paleta.
     Aviso, no bloqueo, hasta medirlo (igual que `DESIGN.md`).
  3. **Si falla el 1**, hay un color nuevo de verdad: se corrige. **Si pasa el 1 y falla el 2**, el efecto es demasiado fuerte:
     se baja (el pozo del farol y el desenfoque del plano 10 son los primeros sospechosos).
  4. **Saltos de luminosidad entre segundos ≤ 15 %** (`manual/13`), con dos excepciones que son el giro del video y quedan
     escritas aquí: el pico f700–f732 y la implosión f812–f831. Se miden aparte, con `comprobar_destellos`.
  5. **Mostaza y tomate** (bufanda, lápiz, goma) no cuentan como acento y no comparten plano con el cian **como acento**.
  6. La caja registradora, la pestaña y el telescopio entran en la paleta por sus hex del entorno; si el render los mezcla
     con un hex fuera, se corrige el entorno, no se amplía la paleta.
- **Medido (lo llena el supervisor):** pendiente. `revisar_color.py` con la paleta declarada (neutros, apoyos, acento, rival,
  efectos e identidad); `revisar_color.py --contraste` sobre los cinco pares de arriba; saltos entre segundos, con f700–f732
  y f812–f831 aparte; `comprobar_destellos` en esta paleta; par humo–Tan en el render. **Ninguna cifra de la lista de medidas
  es mía:** son cálculos con la fórmula de WCAG y valores de la tabla del estudio; lo que dé el render manda.

### Bloque `color` para `ficha.json`

```json
"color": {
  "neutros": ["#141B33", "#F3E9D2"],
  "acento": "#4FE3FF",
  "por_que": "Hoja Noche, paleta B. Azul noche y papel fijan el tono (noche, tecnología) y se distinguen del short 4 (hoja clara y acento amarillo). El cian solo va detrás del dato (placa llena; subrayado en nombres de marca) y en las dos barras de la tarjeta de medidas, para que el ojo aprenda dónde mirar. El rival es lila porque la tinta oscura no se ve en la noche; Tin y Tan conservan sus colores; el fuego es la única luz cálida. Hipótesis para público menor de 45, mayoría hombres, 13 a 17 el tramo mayor; no hay estudio que lo pruebe (H8 y H9 son resultados nulos).",
  "objetivo": "Entrar al Programa de socios: el primer cuadro se distingue en el feed y el color lleva la mirada al dato; se verá en «se quedó a mirar» (no más de 5 puntos bajo el short 4), en la retención en f97, f221, f379, f534, f659, f735 y f821, y en que ningún comentario diga que no se respondió.",
  "medido": "pendiente: revisar_color.py (≥ 85 % de control, ≥ 75 % final), contrastes de texto ≥ 4,5:1 (calculados 11,1 a 15,8:1), par humo-Tan, comprobar_destellos en paleta oscura, comparar el cian con el color de las marcas nombradas; firma del supervisor de continuidad"
}
```
