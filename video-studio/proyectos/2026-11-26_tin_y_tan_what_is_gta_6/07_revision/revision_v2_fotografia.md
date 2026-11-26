# Revisión de fotografía · short 4 (TIN-EN-S-004) · versión 2

Revisor: director de fotografía. Fecha: 2026-11-26. Motivo: el dueño vio la v2 sin que ningún oficio la revisara y dijo que
«la animación pierde un poco de sentido cuando quieren interactuar en el espacio 3D» y que se trata de «producir algo de
alta calidad».

## 0. Qué se revisó y con qué límites

- **Visto:** las 9 hojas `hoja_v2_00.jpg` a `hoja_v2_08.jpg` (1 de cada 6 fotogramas; no vi los 5 intermedios de cada
  tramo, así que un defecto de 1 a 5 f puede quedar fuera), la dirección (secciones 3 y 3b), el guion
  `motor_de_accion/guiones/tin_en_s_004.js`, el entorno `tienda_de_videojuegos.js`, `codigo/tiempos.py` (tabla de
  cámaras) y `controles.md`. No oí el audio ni vi el video en movimiento.
- **Cómo calculé las posiciones en cuadro:** el motor usa `PerspectiveCamera(36, W/H)` (`motor_de_accion/escena.html`,
  línea 189): FOV vertical 36°, lo que da una focal ≈ 2954 px y un FOV horizontal de solo ≈ 21° (lente larga, «teleobjetivo»
  en vertical). Un objeto a distancia `d` mide `2954 / d` px por unidad (u). Con esto, el ancho visible a esa distancia es
  `0,366 · d` u y el **ancho útil de acción** (dejando 150 px a cada lado: cabeza ± 60 y margen) es **≈ 0,26 · d u**. Lo
  contrasté con f30 (coincide ±40 px) y con la altura del humo en f756 (coincide). En otros planos la hoja y el cálculo
  difieren más (hasta ≈ 200 px), así que **toda cifra de corrección de este documento es un valor de partida para
  probar en la vista previa, no un valor final**.
- **Zonas del cuadro de la dirección:** datos y 380–700; subtítulo 905–1085; piso de acción 1105–1700.
  Riesgo nuevo que la dirección no menciona: la interfaz de Shorts tapa en la práctica el borde derecho (≈ 120 px, botones)
  y la parte baja (título y canal) desde y ≈ 1600. Es hipótesis mía; hay que comprobarla con una plantilla de interfaz.

## 1. Diagnóstico de fondo (explica la queja del dueño)

Los tres defectos de profundidad vienen de la misma causa: **el mundo es 3D pero se mira como una pantalla plana**.

1. **Cámara siempre frontal.** `camaraDe` pone la cámara en `(cx, h, z + D)` y mira a `(cx, h, z)`: sin giro, sin
   diagonal. Sin ángulo no hay paralaje entre el estante, el mostrador, el televisor y los dibujos.
2. **Cámara a la altura de la cabeza (h ≈ 0,25·D) y lente larga.** Con la cámara a ≈ 2,6 u y personajes de 1,9 u, dos
   personajes separados 1,6 u en profundidad (z −2,6 y z −4,2 en P14) quedan **≈ 25 px de diferencia en la cabeza y ≈ 100 px
   en los pies**. Para el ojo, «detrás» y «al lado» son lo mismo: por eso los cruces se funden y los golpes no se sabe a
   qué distancia caen.
3. **Los dibujos son planos sin giro** (`PlaneGeometry` sin `rotation.y`, `escena.html` línea 101) y siempre de frente.
   Eso obliga a la cámara frontal (si gira, se ven de canto), y la cámara frontal quita la profundidad: es un círculo.
4. **El escenario de acción es una franja de ≈ 600 px** (y 1105–1700) entre el dato y el subtítulo. Todo el 3D se ve a
   través de esa ranura: personajes de 21 a 35 % del alto, tres actores (Tin, Tan, rival) en un ancho útil de ≈ 3 u.

La prohibición «la cámara no persigue» (dirección, sección 3) se escribió para evitar el temblor, y sirve para eso. Pero
aplicada al pie de la letra impide acompañar los vuelos, que son justo donde el espacio se rompe (sección 2, B6 y A1).

## 2. Defectos por plano y fotograma

Gravedad: **B** bloquea presentar; **A** alta (se nota a la primera vista); **M** media; **b** baja. «Hoja» = fotograma
visto en la hoja. «Corrección» está en términos del motor (cámara `cx` = posición lateral, `D` = distancia, `h` = altura,
`z` = punto de mira; unidades del guion).

### Bloqueantes

| ID | Plano / fotogramas | Defecto | Corrección |
|---|---|---|---|
| B1 | Todo el video (causa en la sección 1) | Interacción en 3D ilegible: los golpes y cruces no dicen a qué distancia ocurren. Ejemplos: f156 el rival tapa la cabeza de Tan; f576–f584 Tan y Tin se funden; f600–f618 Tan, rival, mostrador y caja forman una mancha | Sección 3 (propuesta completa). Mínimo para la v3: B2 más reglas de carriles y cámara más alta con horizonte desplazado |
| B2 | P14, f564–f598 (K4 = 574) | **Tan cruza por detrás de Tin y se funden las cabezas** (f576–f582: dos cabezas superpuestas con la estrella encima). Además **Tin y Tan cambian de lado**: hasta f558 Tan va a la izquierda; desde f594 Tin va a la izquierda, y en la portada final (f956) vuelven a cambiar. Rompe el eje | Quitar el cruce del plano cercano. Hacerlo dentro de P12c (general, f512–f561) con 40 f de margen: Tan sube al carril z −3,8 (separación ≥ 1,6 u de Tin), pasa por detrás de Tin mientras Tin está agachado en el bloqueo y llega a x ≈ 1,6 antes del corte de impacto f562. En P14 Tan ya está a la derecha de Tin y no cruza. Si no se quiere el cruce: cambiar el reparto para que Tan reciba el mazo desde la izquierda y el mostrador pase a x = −2,6 (cambia continuidad: lo decide producción). La portada final cambia de lado en el borrón de 3 f: aceptable, pero anotarlo como excepción de eje |
| B3 | P2–P12c, f30–f561 (74 % del video) | **El televisor, el motivo central, queda detrás del subtítulo**: su pantalla cae en y ≈ 760–1040 y el panel (905–1085) lo tapa; solo asoma el marco. El control v2 lo dio por «a medias» y dijo que no se puede resolver con cámara recta. **Sí se puede, porque el televisor es utilería, no cámara** | En `tienda_de_videojuegos.js`: subir el televisor a centro y ≈ 3,9 u y achicarlo a 0,85 (2,0 × 1,2 u), alargar la columna de la isla a ≈ 3,3 u. Con h ≈ 2,9 y d ≈ 19 queda en y ≈ 710–880, entre el dato (≤ 700) y el subtítulo (≥ 905). Comprobar por plano con `y_px = 960 − 2954·(yTV − h)/d`: en P3, P6 y P14 (más cerca) hay que subir otros 0,2–0,3 u. Mover también `TV` del guion (`[0, 2,3, −7,44]`) a `[0, 3,9, −7,44]`, la llama (`fase`), las chispas, la punta y el humo del televisor. La llama no puede pasar de ≈ 1,0 u mientras haya dato (f552–f666): hasta f671 el dato ocupa la banda alta |
| B4 | P15, f599–f636 | **El gag central (mazazo, mostrador que se parte, caja que sale despedida) ocurre en el borde derecho**: Tan, el mostrador, las bolas grises y la caja salen pegados o cortados por la derecha (f612–f618, f624–f636). En el rail de botones de Shorts | P15: `cx` 0,8 → 1,5 con `D` 12,6 (ancho útil ≈ 3,3 u: de Tin x 0,1 a mostrador x 2,9 caben). Probar también 1,7 |
| B5 | f642–f666 y f750–f768 (el humo tapa el dato) | **Humo gris sobre los datos «from GTA 5 to GTA 6» y «GTA 5: Sep 17, 2013 / GTA 6: Nov 19, 2026»**. En f654–f666 una bola tapa el «5»; en f750–f768 las bolas pasan sobre las dos fechas. Tinta sobre humo `#666B76` ≈ 3,2:1 (calculado), contra 7:1 pedido. Causa: el guion (línea 309) suelta humo desde `TV[1] + 1,0 + fase·0,9` (≈ 4,8 u) con velocidad 1,0, y en `K.enfria` (línea 265) suelta 26 bocanadas con y hasta 3,6 u y sube 0,8 u/s: llegan a y ≈ 600–700 px | Limitar la altura del humo: nacer a `TV[1] + 0,3` y `vy` 0,5 en la línea 309; en `K.enfria` y ≤ 2,6 u y `vy` 0,35, y que se desvanezca al pasar de y = 3,3 u. Alternativa: un panel de papel `#DCE6EE` detrás del dato (como el disco que se hizo para la madeja). Revisar con la regla «ningún humo en y < 720 px mientras haya dato» |
| B6 | P8, f302–f335 (gancho) | **El rival sale por arriba del cuadro**: sube a y = 5,0 u (cabeza a ≈ 7 u) y la cámara fija no lo sigue; en f318–f330 se ve cortado en el borde alto, y la mitad superior queda vacía (no hay dato todavía: entra en f338). Se pierde el vuelo y la caída | Opción segura: bajar el ápice en el guion (línea 109: `[K3 + 11, [2.9, 4.9, −3.4]]` y vecinos) de 5,0 a 3,4 u (cabeza ≈ 5,5 u, entra en cuadro con `h` 2,96 y `D` 12). Opción mejor: acompañar el vuelo (sección 3, punto 5). En ambos casos el corte P9 debe verse como la caída desde arriba |

### Altas

| ID | Plano / fotogramas | Defecto | Corrección |
|---|---|---|---|
| A1 | P6, f114–f126 y f162–f180 | **Tan pegado y cortado por el borde izquierdo** (patada de Tan: pierna fuera de cuadro; el estante inclinado le cae encima en el borde) | P6 (`cx` 0,3, `D` 10,6): `cx` → −0,3. El rival aterriza a la derecha y sale del cuadro en vuelo, que es lo que se busca |
| A2 | P10 f338–f396 y P12 f442–f483 | **Tan cortado por el borde izquierdo** durante 90 f seguidas (la cabeza toca el borde); el trío no cabe: Tan en x −0,7 y el rival en la repisa del mostrador en x ≈ 2,9 son 3,6 u, ancho útil de `D` 11 = 2,9 u | Subir `D`, o juntar: mover a Tan a x = −0,1 y la cámara a `cx` 1,4 (de x −0,1 a 2,9 = 3,0 u, caben con `D` 11,5). Es más sencillo que cambiar el decorado y no toca ningún contacto |
| A3 | P7, f204–f276 | **Rival tendido y luego pegado al borde derecho**, con las bolas grises y los pies fuera (f234, f264–f276) | `cx` 0,95 → 1,5 durante todo P7 (empuje lento ya existente: que termine en 1,7). Mover la caída del rival (línea 108: `[K2 + 17, [2,3, 0, 0,15]]`) a x = 1,8 |
| A4 | P19, f750–f816; P20 f822–f900; P21 f906–f948 | **Tin pegado al borde izquierdo** (cabeza a ≈ 100–150 px, cuerpo inclinado fuera en f750–f816) y **Tan a ≈ 90 px del borde derecho** en f822–f858 con el martillo cruzando: la acción se aprieta en las esquinas y el centro lo ocupa la madeja o el humo | P19, P20 y P21: `D` 11–9,4 → 12,5–11 (el ancho útil sube de ≈ 2,6 u a ≈ 3,0 u) o acercar a Tin y Tan al centro (Tin x −1,05 → −0,85; Tan 1,5 → 1,25). Dejar a la madeja (rival) en x ≈ 0 para que el centro lo ocupe el actor principal |
| A5 | f618–f666 | **Subtítulo semitransparente sobre el fuego rojo**: «De GTA 5 a GTA 6:» se ve con velo rosa; el rojo atraviesa el panel (la llama está justo detrás de la franja por el defecto B3) | Panel de subtítulo opaco (100 %) en `codigo/componer.py` y llama más pequeña (B3). Pasa a 7:1 con tinta sobre `#F4F1EA` opaco |
| A6 | P18, f719–f749 («héroe abierto») | El héroe no se lee como héroe: personajes de ≈ 20 % del alto, pegados abajo a la izquierda, tapados por el estallido rojo (f732–f744), con techo y lámparas ocupando la banda alta. Y no es «de espaldas» (los dibujos no pueden) | Acercar: `D` 13,5 → 9,0 y `h` 0,7 → 1,3 con `sube` 3,1 → 1,6 para que la bola de fuego quede arriba sin comerse a los personajes. Personajes ≈ 32 % del alto, centrados, con la bola detrás de ellos (ya va a z −7 con `renderOrder` 5: bajar a 1). Hoy el estallido pinta encima de la cabeza de Tin en f738 |
| A7 | P11, f430–f441 («detalle») | No es detalle: es un medio de Tin con el bastón, la punta del lápiz no se ve dibujando. Falta el plano de objeto del manual (cap. 11, regla de diseño sobre tipos de plano) | `D` 5,6 → 3,2, `h` 1,45, `z` −2,6, `cx` 0,95 (mirar a la mano de Tin, x ≈ 0,9). 12 f, fija. Tin dibuja y el trazo se ve nacer. Mantener el fondo (estante) |
| A8 | f306–f336 (≈ 1 s) | **Cuadro vacío:** la mitad superior es pared lisa sin dato (el dato de «GTA 6» entra en f338) y el rival ya salió | Resuelto en parte por B6 (el rival se queda en cuadro). Además adelantar el dato «GTA 6» a f318 (es dato del subtítulo; lo decide el editor) o dejar la banda alta con el televisor ya subido (B3) para que haya algo |
| A9 | f30–f85 | Ya anotado en el control v2: Tin y Tan al 21 %, y la franja alta vacía de dato | Con B3 el televisor sube a esa franja y la rellena. P2: acercar a `D` 12,5 (rival 1,5× aún cabe: cabeza bajo y ≈ 1035). El «GTA 7?» de portada puede quedarse hasta f40 (editor) |

### Medias

| ID | Plano / fotogramas | Defecto | Corrección |
|---|---|---|---|
| M1 | P9 (f336–f337) y P4 (f100–f101) | Cuadros de impacto de 2 f que **no informan**: un bloque beige y madeja negra, sin saber qué es. Las líneas radiales cruzan el dato («GTA = Grand Theft Auto», «rated M» en f562) | En el motor se ve bien solo si lleva un solo elemento reconocible: P4, un estante inclinado con 3 cajas en el aire; P9, el mostrador con la grieta en diagonal. Líneas radiales bajo la capa del dato (en `componer.py`, la capa de dato por encima de los efectos). Si se quiere ahorrar, pueden ser P5/P10 con la cámara más cerca (versión segura) |
| M2 | f576–f598 | Los destellos rojos del televisor suben detrás del subtítulo (el panel corta la llama por la mitad) | B3 |
| M3 | f300–f480 y f600–f670 | **Utilería de primer plano abajo a la derecha** (cartel caído beige, mostrador gris): rectángulos grandes sin dibujo que tapan suelo y piernas y que parecen planos vacíos. Ya anotado (defecto 5 del control) | Primero de todo, como paralaje, es bueno (sección 3); pero que no pase de ≈ 12 % del cuadro ni de y 1500: reducir el cartel caído a 70 % y girarlo para que se vea la banda de tinta |
| M4 | f822–f948 | Una pieza negra rectangular en primer término abajo a la izquierda (cabeza del mazo caída) parece un maletín y distrae | Poner el mazo de tinta con su mango tirado (silueta de mazo) o desaparecer al caer |
| M5 | f717–f718 y f724–f727 | **Color fuera de paleta:** la máscara circular (`#FFF4B8` al 0,6 sobre `#DCE6EE`) sale como un disco verdoso/sucio; en f717 otro disco gris-azulado con puntos amarillos. No son ni la tinta ni el claro declarado | Cambiar a claro sólido `#FFF4B8` con borde de tinta y escalón duro (como el fuego), sin transparencia; o hacerlo en negativo (invertir a tinta/papel) 4 f. Medir con `revisar_color.py` por fotograma |
| M6 | f732–f740 | **El anillo amarillo contradice la sección 3b** («el acento no va en el fuego ni el humo»). El control v2 lo marca como «hecho», pero la dirección no cambió | Decidir: o se quita, o se anota en 3b la excepción con su porqué y su métrica. No lo decido yo solo (valida el director creativo) |
| M7 | Datos pequeños | Líneas de apoyo ≈ 40–44 px de letra («GTA 5: Sep 17, 2013», «a game series · since 1997») y el sello «as of Nov 26, 2026» ≈ 30–34 px; la sección 3b pide 48 px o más | En `componer.py`: apoyo a 48 px, sello a 44 px como mínimo. Hay espacio: el dato queda en y 380–700. (Estimado de las hojas a escala 4:1, ± 4 px) |
| M8 | f948–f954 | El **borrón de 3 f afecta también al subtítulo** (se ve borroso) | Que el borrón solo afecte a la escena, no a la capa de texto. Pero el subtítulo ya debe haber salido: quitarlo en f948 |
| M9 | f486–f510 (Tan invita) | Plano al 35 %, bien para reconocer, pero **el 40 % superior queda vacío** (no hay dato) y el televisor se ve cortado detrás del panel | B3 lo rellena. Acercar apenas: `D` 8,3 → 7,6 |
| M10 | Zona segura | Pies de los personajes en y ≈ 1700 (P16–P21): dentro de la zona baja que la interfaz de Shorts suele tapar | Subir los pies a y ≈ 1600 (`h` 2,45 → 2,3 en P16–P21) y probar con la plantilla de interfaz. **Hipótesis mía a comprobar** |

### Bajas y observaciones

- **b1 Sombras de contacto:** ≈ 0,2–0,3 de opacidad, bien en f30–f100; en P19–P21 (f684–f955) se pierden entre los escombros y
  no distingo el contacto de los pies (los dibujos «flotan» sobre el suelo roto). Subir a 0,35 y añadir un óvalo de tinta al
  30 % bajo cada pie cuando el suelo lleve escombros.
- **b2 Rejilla del suelo (`rgba(27,27,34,0,20)`):** es casi lo único que da perspectiva real y está tenue. Subir a 0,28
  cerca de cámara y bajar a 0,12 lejos (gradiente por distancia) refuerza la profundidad sin tocar la paleta.
- **b3 Portada final (f960–f984):** Tan y Tin cambian de lado frente a P21 (ver B2). La firma manda: se queda, con el eje
  anotado como excepción.
- **b4 Salto de tamaño entre la firma (487 px) y la pelea (≈ 400–600 px):** igual que v1; aceptable con el borrón.

### Eje y continuidad (regla de los 180°)

- Eje de la pelea: Tan a la izquierda, Tin a la derecha, rival entre y detrás (f30–f558). Se mantiene en los 12 cortes de
  P2–P12c. **Se rompe en f570–f588 (B2)** y no vuelve hasta la portada. Anoto el cruce como el único giro de eje permitido y
  que ocurra dentro de un plano general.
- Cortes que confunden: f100 y f336 (M1: no se entiende qué se ve), f719 (de P16 cercano a P18 lejano en 1 f: el espectador
  pierde a los personajes durante 30 f). Con A6 el salto de tamaño baja de ≈ 35 % a ≈ 32 %.
- Cortes que funcionan: P2→P3 (misma dirección de mirada), P12→P12b, y los cuadros de impacto cuando el golpe cae en el
  borde del cuadro.

## 3. Cómo usar la profundidad de verdad en este formato

El formato (vertical, dibujos planos de palitos, datos arriba y subtítulo en el medio) deja poco espacio, así que la
profundidad tiene que venir de lo que **sí** puede ser tridimensional: la cámara, los carriles, el primer término y el decorado.
Los dibujos siguen planos pero **siempre de frente a la cámara**, no de canto: un «billboard» que gira con ella.

1. **Dos carriles y una regla** (cuesta cero). Tin y Tan en el carril cercano (z ≈ −2,0 a −2,6) y el rival en el lejano
   (z ≈ −4,0 a −5,5) durante los golpes. Separación mínima de 1,6 u. Nadie cruza de un carril a otro en un plano cercano
   (solo en un general, con empuje o desplazamiento). Los golpes ocurren siempre **en el mismo carril**, con la víctima
   saliendo en **diagonal hacia el fondo o hacia cámara**, nunca en línea recta lateral: la diagonal es la que se lee como 3D.
2. **Cámara más alta con horizonte desplazado** (versión segura, requiere tocar `escena.html`: `camara.setViewOffset`
   o `filmOffset`). Subir `h` de ≈ 0,25·D a ≈ 0,40·D y desplazar la imagen para que los pies sigan en y ≈ 1600–1700 y las
   verticales sigan rectas. Efecto estimado: la separación entre carriles pasa de ≈ 100 px a ≈ 230 px en los pies. El
   suelo con cuadrícula se ve más y las líneas del piso empiezan a fugar. Esto sustituye al `sube` de P18 (que inclina).
3. **Lente más abierta, cámara más cerca.** FOV 36° → 48° (horizontal ≈ 28°) con `D` ×0,75 para conservar el tamaño: los
   estantes (x = ±2,8) fugan con ángulo claro hacia el televisor, que es lo que el entorno ya dice que quiere («se vean fugar»).
   La pared del fondo mide 9 u y la cámara está dentro de la tienda, así que no hay borde que se vea (comprobar P2: ±4,5 u
   a z = −10). Cambia todas las cámaras de la tabla de `tiempos.py` y las cifras de arriba: hacerlo **antes** de corregir
   plano por plano, no después.
4. **Paralaje lateral en los generales largos** (los planos que ya existen y duran): P7 (107 f), P10 (92 f), P19 (124 f) y
   P21 (50 f). Un desplazamiento de la cámara de 0,9 u en 90 f, a 8 % del ancho por segundo (el límite de `manual/14`,
   sección 6). Con el estante en primer término y el televisor al fondo, se cruzan a distinta velocidad. Es **un movimiento
   por toma**, sin temblor. Sustituye al «empuje +5 %», que es plano.
5. **Cámara que acompaña tres vuelos** (excepción a la regla «no persigue», que aplica a temblor; pide aprobación de
   fotografía y animación, y del jefe de producción): el rival en el gancho (K3+5 a K3+21), la caja registradora hacia cámara (K5+2
   a K5+18) y el mazo (K.mazo+12 a +17). Giro/inclinación suave de 12 a 16 f, sin salir del eje. Cuesta una animación de
   `lookAt` por plano, no más. Versión segura: sin movimiento, solo con los ápices bajados (B6) y la cámara más lejos.
6. **Primer término con intención.** Un elemento a distancia 0,5–1 u de la cámara (poste de fila, esquina del estante) en
   una esquina inferior, ≤ 12 % del cuadro, nunca sobre acción ni dato. Con el desplazamiento del punto 4 se mueve más rápido
   que el fondo y da lectura inmediata de volumen. Ya existe el poste de fila (x 1,9–3,3, z 0,5): usarlo en P2 y P7, y mover el
   cartel caído (M3) a esa función.
7. **Billboard cilíndrico:** al tener la cámara una diagonal (azimut de ±12° a ±20° en P7, P10, P19), cada dibujo gira
   con `rotation.y` igual al azimut de la cámara para no verse de canto. Con ±20° la deformación de un dibujo plano es
   imperceptible (el ancho aparente cambia ≈ 6 %). Si no se acepta tocar el motor, **no usar azimut** y quedarse con 1–4.
8. **Contactos legibles:** el punto de contacto (puño, bastón, mazo) siempre entre ambos cuerpos y en el mismo carril. Un
   solo trazo de «línea de acción» (3 f) y la estrella a z + 0,05 por delante de los dos. No hay objeto grande entre cámara y contacto.
9. **El decorado también es de profundidad:** el televisor (B3) y los banderines sobre el nivel del dato son la banda alta; el
   mando mostaza (z = −9,78) da el fondo extremo. Cada plano general debe tener tres capas visibles: primer término, carril de
   acción y fondo. Hoy muchos tienen solo la segunda.

**Qué cuesta cada cosa (para que elija el jefe de producción):**

| Opción | Qué es | Toca | Riesgo |
|---|---|---|---|
| Segura | B2–B6, A1–A9 + carriles + TV elevada + lente más abierta (puntos 1 y 3) | Guion, `tiempos.py`, entorno | Bajo. Todo se mira en la vista previa |
| Media | La segura + horizonte desplazado + paralaje lateral (puntos 2 y 4) | `escena.html` (una llamada de cámara) + `camaraDe` | Medio: hay que reajustar el reparto del cuadro |
| Ambiciosa | La media + vuelo acompañado + billboard cilíndrico (puntos 5 y 7) | `escena.html` (rotación por personaje) | Alto: los dibujos y su sombra cambian; revisar firma y comprobar_firma |

Recomiendo la **media**: es lo mínimo que responde a lo que dijo el dueño sin reescribir el motor. La ambiciosa solo si
la media no basta tras la vista previa.

## 4. Veredicto

**No se presenta la v3 hasta cumplir lo siguiente.**

Bloquea presentar:
1. B2 (cruce de Tan y Tin con cambio de lado) resuelto y el eje anotado.
2. B3 (televisor fuera de la franja de subtítulos) resuelto en el decorado y en las cifras de la llama.
3. B4 (el gag del mostrador en el borde) y B6 (el vuelo del rival fuera de cuadro).
4. B5 (humo sobre los datos) con medida: en la hoja de contacto ningún dato con humo detrás.
5. B1: elegir una de las tres opciones de la sección 3 y aplicarla antes de corregir plano por plano.

No bloquea pero debe ir en la v3: A1–A5 (personajes cortados, subtítulo con velo), A6 y A7 (héroe y detalle, que son tipos de
plano que la dirección prometió), M5 (color fuera de paleta) y M7 (tamaño de letra).

Antes de enseñarla al dueño:
- **Un control automático nuevo** (lo escribiría el jefe de producción, no yo): con las posiciones de cada personaje por
  fotograma, que ningún personaje tenga el centro a menos de 150 px del borde, ni solape con otro más del 30 % de su ancho, y
  que ningún dato quede detrás de un objeto del mundo. Los controles de hoy miden la firma, el color y los destellos, pero no
  el encuadre: por eso los defectos de arriba pasaron.
- **Revisión visible de fotografía y de animación** del video v3 en movimiento (no solo hojas) y firma del supervisor de
  continuidad. Lo que digan las hojas no basta: el dueño habló de cómo se siente al verla.
- **Comparar el resultado con la hoja de referencia** de las peleas (cap. 11, regla 6) con planos reales cargados. No lo hice aquí.
- Anotar en `controles.md` que la sección «V2 · Defectos que siguen» omitió B1–B6 y A1–A9.

## 5. Para el jefe de producción: orden sugerido

1. Decidir la opción de la sección 3 (segura, media o ambiciosa).
2. Entorno: televisor y columna (B3), cartel caído (M3), cuadrícula del suelo (b2), sombras (b1).
3. Guion: ápices del rival (B6), humo (B5), recorrido de Tan (B2), posiciones (A2, A3, A4).
4. `tiempos.py`: nueva tabla de cámaras con lente más abierta y `cx`/`D`/`h` por plano (A1–A9).
5. `componer.py`: panel opaco (A5), tamaño de letra (M7), capa del dato sobre los efectos (M1), borrón sin texto (M8), color (M5).
6. Vista previa por plano con una rejilla de zonas (datos 380–700, subtítulo 905–1085, márgenes laterales de 150 px y la
   interfaz de Shorts); recién después, render.

No toqué código ni otros archivos.
