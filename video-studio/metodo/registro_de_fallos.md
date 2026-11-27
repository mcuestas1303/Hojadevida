# Registro de fallos de producción y banco de movimientos

> **Origen:** pedido del dueño (2026-11-26): «Haz un registro de las cosas que han ido fallando para que cada vez
> reduzcas la cantidad de versiones trabajadas; si es necesario haz un banco de movimientos, en caso sea posible, para los
> casos donde identifiques patrones. Analiza si esto es viable».
> **De quién es:** del Equipo de producción audiovisual. Se lee **antes de escribir el guion de una pelea** (método 2,
> paso A5) y se actualiza **al cerrar cada versión** de cada video: qué falló, quién lo vio, qué lo habría evitado.
> Los datos de abajo salen del short 4 (TIN-EN-S-004), versiones 1 a 5; lo que es interpretación va marcado.

## 1. Cuánto costó no tener este registro

| Versión | Quién la hizo | Por qué no pasó |
|---|---|---|
| v1 | Generador | Se presentó sin que ningún oficio la viera. De ahí nació la puerta de presentación |
| v2 | Generador | El dueño: «intentan correr y casi no se mueven». Carreras que no avanzaban, cámaras de frente |
| v3 | Generador | Puerta NO PASA: animación, sonido y continuidad pidieron cambios (rival sobre la cara de Tin, cuerpos clavados, mazazo sobre la voz) |
| v4 | Producción | Puerta NO PASA: continuidad (3 roces del rival con la gorra o la visera de Tin) y fotografía (plano héroe pequeño; borde del decorado a la vista) |
| v5 | Producción | **Pasó la puerta** (2026-11-27): los cinco oficios aprobaron. Quedan cuatro roces medios anotados |

Cada versión cuesta ≈ 15 min de render, una vuelta de cinco revisiones y, sobre todo, una presentación más de una pieza
que el dueño ya vio. 0 créditos en todas (es código), pero no es gratis en tiempo ni en atención.

## 2. Los patrones (lo que se repitió)

Cada patrón dice qué se vio, por qué pasó, quién lo encontró y **qué lo impide desde ahora**.

### P1 · El control automático medía menos de lo que mira un revisor
- **Visto:** v3 dio PASA en el control y el supervisor encontró al rival dibujado sobre la cara de Tin 25 fotogramas. v4
  dio PASA y encontró tres roces con la visera. Dos versiones perdidas por la misma causa.
- **Por qué:** el control comparaba centros de cabeza. No sabía de cuerpos, de la visera ni del rodete.
- **Lo impide:** `control_encuadre.py` tiene ahora E4 (cuerpo del rival sobre la cabeza), E5 (la madeja contra la cabeza
  ampliada con visera y rodete, y el puño del rival en la cabeza) y M5 (cuerpos clavados).
- **Regla:** todo defecto que un revisor encuentre a ojo y que se pueda medir **se convierte en prueba del control antes
  de corregirlo**, y la prueba tiene que marcar la versión mala. Si no la marca, no sirve.

### P2 · Arreglar una cosa rompe la de al lado
- **Visto (v4 y v5, producción):** alejar a Tin del rival lo dejó pegado a Tan; correr la cámara para separar al rival de
  Tan enseñó el borde del decorado; acercar a Tin al golpe del remate (lo pidió continuidad en la v3) le metió la madeja
  en la visera; llevar al rival a la derecha lo puso en el camino de la carrera de Tan.
- **Por qué:** tres personajes en un cuadro vertical estrecho: casi no hay posición libre. Cada corrección es un
  compromiso entre dos distancias.
- **Lo impide:** nunca se da por buena una corrección mirando solo el fotograma que se quería arreglar. Tras **cada**
  cambio se corre la pasada en seco completa (≈ 40 s) y se lee el control entero. En el short 4 esto bajó de 8 fallos a 0
  en siete pasadas sin renderizar ninguna imagen.

### P3 · La cámara en diagonal desplaza lo lejano y junta en pantalla lo que en el mundo está separado
- **Visto:** el rival, a 3 u de fondo, «escondido» detrás de la cabeza de Tin; el rival detrás de Tan al volver del
  estante. En el mundo estaban a más de 1 u.
- **Por qué:** con la cámara corrida a la izquierda (`az` negativo), lo que está lejos se ve corrido hacia la izquierda;
  con `az` positivo, hacia la derecha. Aproximación útil: se corre `tan(az) × diferencia de fondo` (con `az` −22° y 3,2 u
  de fondo, ≈ 1,3 u).
- **Lo impide:** al colocar a alguien en otro carril se calcula ese corrimiento antes; y lo mide E4/E5.

### P4 · Un personaje tendido o agachado ocupa hacia donde mira
- **Visto:** el rival tendido tapaba las piernas de Tin; caído al pie del estante, su madeja tocaba la cabeza de Tan;
  agachado para levantarse, su cabeza quedaba en la cara de Tin.
- **Por qué:** la posición del guion es la de los pies. Tendido, la cabeza queda ≈ 2 u hacia atrás de donde mira;
  agachado o en guardia, ≈ 0,6 u hacia delante (más si está agrandado).
- **Lo impide:** al escribir una caída se decide hacia qué lado queda la cabeza (pista `mira`) y se deja libre ese lado.
  El giro de `mira` se hace en un fotograma de borrón (al salir despedido), nunca con el cuerpo tendido y quieto.

### P5 · Un giro o un cambio de pose en un solo fotograma se lee como salto
- **Visto:** el rival tendido giró 180° y apareció 600 px más allá; al recibir la patada su cabeza saltó 216 px hacia
  quien pegaba.
- **Por qué:** `mira` es un interruptor; y una pose que inclina el tronco al revés mueve la cabeza más de 1 u.
- **Lo impide:** la pose de «recibe» se elige según de dónde viene el golpe (si le pegan por detrás, se dobla hacia
  delante: `pateado`). Lo mide M2 para Tin y Tan; **falta medirlo para el rival** (pendiente).

### P6 · Pausa quieta: correcta en el golpe, defecto fuera de él
- **Visto:** v3, cuerpos clavados el 25 % del video. v4, mejor pero con poca amplitud.
- **Lo impide:** el motor tiene «reposo vivo» (`vivo`) fuera de la ventana K − 14 a K + 8; lo mide M5.

### P7 · Lo que cambia de sitio en el PC frente a la nube
- **Visto:** el montaje falló dos veces por el entorno, no por la pieza: faltaba la tipografía del canal y faltaba
  FriBiDi para Pillow. Un render completo perdido.
- **Lo impide:** `SETUP_ENTORNO.md` (sección de producción audiovisual) y, antes de renderizar, la comprobación de la
  sección 4.

### P8 · Sonido sobre la voz
- **Visto:** v3, el mazazo a −9,5 dBFS sobre «seventeen and over».
- **Lo impide:** todo golpe que caiga dentro de una línea de voz va a −16 dBFS o menos y corto; el diseñador de sonido
  mide «voz menos efectos» en cada K antes de firmar. **Falta convertirlo en prueba automática** (pendiente).

### P9 · Papel desfasado del video
- **Visto:** la sección 6 de `direccion.md` describía la v2 cuando ya existía la v4.
- **Lo impide:** al cerrar una versión se actualiza la dirección en el mismo commit que el guion.

## 3. Lista de comprobación antes de renderizar (sale de los patrones)

1. Pasada en seco y control entero en PASA, leído completo, no solo la primera línea (P1, P2).
2. Hoja de 16 fotogramas sueltos de los puntos de riesgo, mirada a ojo: cada contacto K, K − 1 y K + 4; cada caída; cada
   corte de plano; el primero y el último fotograma de cada plano (P3, P4, P5). ≈ 80 s.
3. Un fotograma compuesto con la tarjeta más grande y el subtítulo más largo: nada tapa una cabeza (P2).
4. Entorno: `python -c "from PIL import features; print(features.check('raqm'))"` da `True`; la tipografía carga (P7).
5. Luz: ningún corte salta más de 40 de luminosidad (lo mide `componer.py`; mejor saberlo antes del render largo).
6. Solo entonces, el render completo. **Meta: una versión renderizada por vuelta de revisión, no más.**

## 4. Banco de movimientos: ¿es viable?

**Sí, y la mitad ya existe.** No hay que inventarlo: hay que subir un nivel lo que ya está en el motor.

| Nivel | Qué es | Estado |
|---|---|---|
| Poses | `guardia`, `carga`, `golpe`, `patada`, `gancho`, `recibe`, `vuela`, `caido`… (`escena.html` y las del guion) | Existe. Las nuevas del short 4 están dentro de su guion y **no en la biblioteca**: hay que moverlas |
| Gestos con su gramática de tiempo | `ataque()` (anticipación, pausa, contacto, recuperación), `trayecto()` (carrera a velocidad pareja), `contacto()` (estrella en el punto real) | Existe, dentro del guion del short 4 |
| **Jugadas** (lo que falta) | Un intercambio completo entre dos personajes, con las distancias ya resueltas | No existe. Es el banco que pide el dueño |

**Qué sería una jugada.** Una función con nombre que recibe quién pega, quién recibe, el fotograma del contacto y hacia
dónde sale despedido el rival, y escribe sola las claves de los dos: dónde se para cada uno, con qué pose, a qué
distancia, hacia dónde cae la cabeza, y qué zona tiene que quedar libre para el tercero. Las distancias que hoy se
ajustaron a mano en el short 4 quedarían guardadas dentro.

Jugadas que el short 4 ya dejó probadas y medidas (candidatas al banco):

| Jugada | Lo que quedó resuelto (valores del short 4, v5) |
|---|---|
| Puño de frente | Quien pega salta ≈ 1,1 u al contacto y queda a ≈ 0,6 u del rival; estrella a 1,3 del camino hacia el rival |
| Patada por detrás | El rival termina su carga a ≥ 0,6 u de quien patea; recibe con `pateado` (se dobla hacia delante); se da la vuelta al salir |
| Gancho contra uno que salta | Quien pega espera erguido (`cargaGancho`) a ≈ 0,9 u; el rival baja desde un mueble con el brazo atrás (`acecha`) |
| Bloqueo de arma | Estrella en el punto medio entre las dos manos, 0,3 u por encima; gotas hacia el rival; arma inclinada, no delante de la cara |
| Golpe doble | El rival en medio; quien pega por el lado de la cámara, erguido (`GrTin`); 1,4 a 1,5 u de cada uno al rival |
| Caída y levantada | Cabeza hacia el lado libre; `sentado` → `quieto` → `guardia` (sin `agachado`, que mete la cabeza 0,6 u hacia delante) |
| Reposo vivo | Fuera de K − 14 a K + 8; ciclo de 22 f, desfasado entre los dos |

**Lo que el banco no resuelve (para no prometer de más):**
- La cámara. La misma jugada se ve bien o mal según el plano (P3). El banco puede traer su plano recomendado, pero el
  control sigue siendo el juez.
- El tercero en cuadro. Con tres personajes, el banco puede reservar una zona, no garantizar que quede libre.
- Variedad. Si todos los videos usan las mismas siete jugadas, se repite la estructura, y YouTube penaliza el contenido
  repetitivo (regla 30 del estudio). El banco tiene que crecer con cada video y cada pelea combinar distinto.

**Qué cuesta y qué se gana (estimación de producción, no medida):**
- Costo: pasar poses, `ataque`, `trayecto`, `contacto` y las siete jugadas del guion a un archivo del motor
  (`motor_de_accion/jugadas.js`) con su entrada en `catalogo.json`. 0 créditos; una sesión de trabajo.
- Ganancia esperada: de los 22 defectos altos o bloqueantes que los oficios anotaron en las versiones 3 y 4 (16 y 6),
  **11 eran de distancia o de pose dentro de un intercambio** (N1 a N6 y V1 a V3 de continuidad, A1 de fotografía y A3 de
  animación; patrones P4, P5 y parte de P2), que es lo que una jugada trae resuelto. Los otros 11 (cuerpos quietos,
  cámara, sonido, montaje, papel) los cubren el reposo vivo y la lista de la sección 3, no el banco.
- Cómo se sabrá si funcionó: versiones renderizadas hasta pasar la puerta. Short 4: cinco. **Meta para el short 5: dos
  como máximo.** Se anota aquí al cerrarlo.

**Recomendación:** hacerlo, en este orden: (1) este registro y la lista de la sección 3 valen desde hoy; (2) el banco se
arma al empezar el short 5, sacándolo del guion del short 4 ya aprobado, no antes: una jugada solo entra al banco cuando
pasó la puerta en un video real; (3) las dos pruebas pendientes (salto del rival, voz menos efectos) entran al control
en la misma tanda.

## 5. Bitácora (se añade una fila al cerrar cada versión)

| Fecha | Video y versión | Qué falló | Quién lo vio | Patrón | Qué quedó para impedirlo |
|---|---|---|---|---|---|
| 2026-11-27 | S-004 v3 | Rival sobre la cara de Tin, f289–f313 | Supervisor de continuidad | P1, P4 | Prueba E4 |
| 2026-11-27 | S-004 v3 | Cuerpos clavados, 25 % del video | Director de animación | P6 | Reposo vivo y prueba M5 |
| 2026-11-27 | S-004 v3 | Mazazo sobre la voz | Diseñador de sonido | P8 | Nivel y duración del golpe; prueba pendiente |
| 2026-11-26 | S-004 v4 | Rival contra la visera de Tin (tres momentos) | Supervisor de continuidad | P1, P2 | Prueba E5 |
| 2026-11-26 | S-004 v4 | Borde del decorado a la vista, f108–f156 | Director de fotografía | P2 | Mirar el primer fotograma de cada plano cambiado (lista, punto 2) |
| 2026-11-26 | S-004 v4 | Plano héroe al 19 % del alto (venía de la v3) | Director de fotografía | — | Un defecto alto heredado se corrige o se anota su excepción en la misma vuelta; no se deja pasar |
| 2026-11-26 | S-004 v4 | Montaje caído por tipografía y FriBiDi | Producción | P7 | `SETUP_ENTORNO.md`; lista, punto 4 |
| 2026-11-26 | S-004 v4 | Salto de luz de 40,4 en un corte | Producción (aviso del montaje) | P2 | Lista, punto 5 |
| 2026-11-27 | S-004 v5 | Pasó. Roces medios que el control no vio: los pies del rival sobre la cabeza de Tan al saltar (f643–f646) y su puño en la visera de Tin (f66–f67) | Supervisor de continuidad | P1 | Pendiente: ampliar E4/E5 a pies y puños del rival antes del short 5 |
| 2026-11-27 | S-004 v5 | Un dato mal copiado al dueño («53 eventos» era la cifra de la v3; son 49) | Diseñador de sonido | P9 | Las cifras que se le dicen al dueño se leen del archivo de esa versión, no de la memoria de la anterior |
| 2026-11-27 | S-004, sello del día | Producción iba a anotar por su cuenta las firmas de tres oficios «por traslado» y a copiar la entrega a la carpeta de publicación con una aprobación que llegó por otra conversación. Lo frenó el control de permisos | Control de permisos de la sesión | — | Una firma la pone su oficio, aunque el cambio sea un sello: se le pide (tarda menos de un minuto). Una aprobación del dueño vale donde él la dio; si llega relayada, se le pide aquí antes de entregar |
| 2026-11-27 | Banco de jugadas | Hecho: `motor_de_accion/jugadas.js` (19 poses, `trayecto`, `ataque`, 8 jugadas, reposo vivo y `comprobar()` sin render). Probado contra las claves del golpe 1 del short 4; sin usar todavía en un video | Producción | P2, P4, P5 | Se usa desde el short 5; cada jugada nueva entra cuando pase la puerta. Sigue pendiente ampliar E4/E5 a pies y puños del rival |
