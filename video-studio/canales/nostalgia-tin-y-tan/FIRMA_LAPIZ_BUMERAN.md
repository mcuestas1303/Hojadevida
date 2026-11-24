# Firma del canal: el lápiz bumerán

> **Pedido del dueño (2026-11-24), textual:** «Lo otro que quiero es un efecto para todos los videos en el que el
> lápiz sirva como un bumerán: cuando comienza el video el bumerán está regresando a sus manos y cuando está
> terminando el video Tan tira el lápiz; definilo bien con el equipo».
>
> **Responsable:** director de animación (firma esta especificación). Las secciones 6 a 8 y 11 son **propuestas con
> valores concretos** para que el director de fotografía, el diseñador de sonido, el editor y el supervisor de
> continuidad las firmen o las corrijan. **Estado: borrador pendiente de firmas y de la prueba técnica (sección 9).**
> Sin códigos ni créditos: todo se dibuja con `palitos.py` 1.3 y `efectos.py` 1.0 (costo 0).
>
> **Sellos** (los de `manual/14_efectos_y_emocion.md`, sección 0): **[investigación]**, **[oficio]**,
> **[hipótesis del equipo]**. Los números de dosis (fotogramas, píxeles, grados) son norma de partida del estudio, o sea
> **[hipótesis del equipo]** aunque no lo repita cada vez; salen de la tabla de dosis del manual 14 cuando ahí hay una, y
> se ajustan con la prueba. Nadie ha escuchado los sonidos de la sección 7: Claude no oye; se comprueban con oído humano.
>
> Medidas a 30 fps, 1080×1920. «c» es el fotograma contado desde el empalme: `c = 0` es el fotograma 0 del video; `c = −1`
> es el último; `c = −24` es 24 fotogramas antes del final. «f» es lo mismo para `c ≥ 0`. Los 30 fotogramas de un
> segundo son `30 f`.

## 0. Resumen en diez líneas

1. **Tan lanza el lápiz al final y Tan lo atrapa al principio.** El lápiz sale de su mano, sube dando una vuelta y
   media, queda «colgado» en el aire justo en el empalme, y vuelve a su mano. Es un bumerán de verdad: regresa a quien
   lo lanzó.
2. **El bucle es el vuelo.** El último fotograma y el primero son dos instantes consecutivos del mismo vuelo; no hay corte.
3. **Dura 34 fotogramas en total (1,13 s):** cierre de 24 f (lanzamiento y vuelo de ida) y apertura de 10 f (vuelo de regreso y atrapada).
4. **En el fotograma 0 el lápiz está a la vista y nítido**, en el pasillo entre el objeto del tema y los personajes, sin tapar texto, objeto ni caras.
5. **La voz de Tan entra en f14** (0,47 s), después del golpe de la atrapada. Es el costo de la firma sobre el primer segundo y se mide (sección 10).
6. **Lo único que cambia de la portada:** Tan lleva el brazo en `saluda` (levantado, abierto) en el fotograma 0 y Tin va con `objeto=False`.
7. **Sin destellos, sin zoom, sin sacudida, cámara fija.** El movimiento es del lápiz y del brazo de Tan.
8. **Un sonido propio, siempre el mismo:** un whoosh continuo atado a la velocidad del lápiz y un golpe seco al atraparlo.
9. **Variantes:** `atrapa="tin"` (si el dueño quiso decir otra cosa) y «sin retorno» (cierre con pregunta de suspenso).
10. **No va** en infantil ni en videos cuya portada no deje pasillo libre.

## 0b. Corrección de medidas tras el primer uso (short 3, vuelta 2, 2026-11-24)

El supervisor de continuidad rechazó el primer render con la firma: con el brazo en `saluda` (100°, 155°) la mano queda a
1,07 R del eje de Tan, pegada a la mejilla, y **el lápiz cruzaba su cara al soltarlo (c = −15 a −13) y pisaba la mejilla al
atraparlo (f10)**. Lo que cambió en `herramientas/efectos.py` 1.1 (y manda sobre los valores de las secciones 2 a 4 y 9 de
este archivo, que se dejan como historia del diseño):

| Qué | Antes | Ahora |
|---|---|---|
| Brazo `bd` de Tan en el empalme, al soltar y al atrapar (`BD_FIRMA`) | `saluda` (100°, 155°) | **(95°, 108°)**: brazo abierto hacia delante, mano a la altura del hombro |
| Mano | (x + 1,07 R; suelo − 3,67 R) | **(x + 1,46 R; suelo − 3,17 R)** |
| Punto de mano H (centro del lápiz sujeto), plano de prueba | (358,0; 1306,1) = x + 1,12 R | **(392.1; 1349.8) = x + 1,51 R; suelo − 3,42 R** (el brazo mide 1,50 R: 1,6 R no se alcanza) |
| Bézier de ida B1 (plano de prueba) | H, (372; 1240), (570; 1165), S | **H, H + (110; −10), (570; 1165), S = (585; 1235)**: el lápiz sale hacia delante, lejos de la cara, y luego sube |
| Bézier de vuelta B2 | S, (597; 1290), (420; 1372), H | **S, (597; 1290), H + (95; 40), H** |
| `_despejes` | no medía los fotogramas junto a la mano («junto a la mano no se mide») y medía contra cajas | **mide TODOS los fotogramas (c = −30 a 30, en la mano y en vuelo) contra las cabezas como círculos** (`cabezas_firma`: centro con la inclinación de la cabeza, radio 1,04 R, más la visera de Tin) |
| Criterio de `geometria_firma` y `comprobar_firma` | «no toca las caras» | **8 px o más a cualquier cabeza en cualquier fotograma**; 30 px al texto y al objeto |
| Obturador | 1 a 6 subpasos (`1 + v/10`) | **1 a 16 subpasos (`1 + v/4`)**: con 6 se veía un abanico de copias en f4–f7 |
| Cara de la anticipación | `concentrado` | **la de la portada** (el prompt del short 3 no admite `concentrado`: se lee como enojo); lo decide cada render |

**Medido en el short 3 (render 2), con `comprobar_firma` sobre los 61 fotogramas de la firma:** distancia mínima del lápiz a la
cabeza de Tan **28,8 px** (en c = −14), a la de Tin (con visera) **46,2 px** (en c = 0), al objeto 61 px, al texto 461 px;
velocidad en el empalme 5,2 y 4,7 px/f; giro 4,4 y 4,0 °/f; máximos 58 px/f y 24,9 °/f; giro total 330°. Visto fotograma a
fotograma (f0–f14 y f900–f929): el lápiz no toca ninguna cabeza. El render del short 3 aplica además el desplazamiento del
cuerpo a la mitad (`dx_cuerpo = 0,5`: −4/+5 px) para que los pies no patinen, y baja el lazo 10 px (`subir = −10`).
La dirección en el empalme se mide por la tangente de las curvas (77,9° y 77,7°); por cuerdas de un fotograma la tuerce la curvatura.
Funciones programadas: `geometria_firma`, `lapiz_bumeran`, `pintar_lapiz_volador`, `golpes_firma`, `comprobar_firma`, `cabezas_firma`
(`efectos.py` 1.1) y `pose_entre`, `mano_de` y pose como dict (`palitos.py` 1.4). **Sin programar:** la variante «sin retorno» (§4.2) y `atrapa="tin"` (§4.3).

## 1. Idea y significado

### 1.1 Qué dice la frase del dueño y qué lecturas caben

«El bumerán está regresando a **sus** manos»: el sujeto de la frase es el bumerán, y la frase siguiente nombra a una
sola persona que lo lanza, Tan. «Sus manos» puede ser (A) las de Tin, dueño del lápiz; (B) las de Tan, la que lo lanzó;
(C) las de quien sea que lo tire. Se evalúan tres lecturas:

| Lectura | Cierre | Apertura | A favor | En contra |
|---|---|---|---|---|
| **A. Relevo** (propuesta de partida de la coordinación) | Tan lanza | Tin atrapa | Calza con «Tan pregunta, Tin responde» (`PARAMETROS.md` §1); el lápiz ya es de Tin y sigue en su mano en el resto del video | No es un bumerán: nada regresa a quien lo lanzó, es un pase. El lápiz aterriza en Tin (derecha) y la voz sale de Tan (izquierda): dos focos en los primeros 0,4 s (R13: el movimiento lleva la mirada; aquí la lleva al personaje equivocado). En el empalme, Tan queda con el brazo extendido sin lápiz y Tin con la mano arriba: el fotograma 0 pide dos poses nuevas en vez de una |
| **B. Bumerán** (elegida) | Tan lanza | Tan atrapa | Es la palabra del dueño: lo que se tira vuelve a quien lo tiró. El ojo hace un solo recorrido: lápiz, mano de Tan, cara de Tan, voz de Tan (f14). El mismo brazo cierra y abre: la pose del empalme es una sola (`saluda`). Tin queda libre para reaccionar | El lápiz es de Tin: Tan lo toma prestado. Se resuelve con lo que el canal ya hace: cada toma declara qué objeto lleva cada mano (`control`, `calendario`, `lapiz`) y Tin va con `objeto=False` en el plano de firma |
| **C. Tin lanza y atrapa** | Tin lanza | Tin atrapa | Lápiz de Tin, sin préstamo | Contradice «Tan tira el lápiz» |

### 1.2 Decisión y razones

**Se elige B: Tan lanza y Tan atrapa.** Razones, por orden de peso:

1. **Es lo que dijo el dueño.** Un bumerán regresa a quien lo lanzó y él nombra un solo lanzador. Si lo que quiso
   decir fue «a las manos de Tin», el cambio cuesta una variante (`atrapa="tin"`, sección 4.3) y no obliga a rehacer nada.
2. **Un solo recorrido del ojo.** Lo primero que se oye es la voz de Tan; lo primero que se ve tiene que terminar en ella
   (R13, R14 [oficio] / [investigación, resumen]).
3. **Significado que sirve al objetivo.** El bumerán dice «lo que se lanza, vuelve». Lo que se quiere que vuelva es el
   **espectador** (espectadores que regresan, suscriptores por mil vistas). No repite el formato del video
   («Tin responde»), que ya se ve en el cuerpo de cada pieza: la firma marca el regreso, no la respuesta.
   Por qué esto es una lectura del equipo y no un dato: **[hipótesis del equipo]** (que el gesto se entienda así y que
   eso cambie algo se prueba en la sección 10).
4. **En el cierre, el lápiz lanzado es la pregunta abierta** que el manual 14 (§4b.4) recomienda dejar antes de la
   invitación: sale al aire; en el siguiente «play» vuelve.

**Lo que la lectura A conserva de bueno** (Tin con su lápiz) se guarda en la variante `atrapa="tin"`, que la prueba
técnica puede renderizar gratis para que el dueño compare sin explicaciones.

### 1.3 Qué comunica y qué emoción provoca cada parte (resumen; el detalle va en cada sección)

| Parte | Comunica | Emoción | Respaldo y sello | Métrica |
|---|---|---|---|---|
| Mismo gesto, mismo sonido, en todos los videos | «esto es Tin & Tan», reconocimiento | confianza, familiaridad | R26 mera exposición, R27 fluidez **[investigación]**; que una firma repetida convierta en suscriptores: **[hipótesis del equipo]** (manual 14, §7.1 fila 7) | espectadores que regresan; suscriptores por mil vistas |
| Anticipación (brazo atrás, 6 f) | «va a pasar algo» | expectativa | R22 **[oficio]**; dosis 4–8 f (tabla 2.5) | retención en el lanzamiento |
| Impulso y suelta (4 f) | energía, intención | determinación | R24 movimiento biológico **[investigación]**: la intención se lee en el brazo, no en la cara; manual 04, «Determinación» | — |
| Vuelo en arco con giro | juego, vida propia del objeto | curiosidad, alegría leve | arcos: uno de los doce principios (R22 **[oficio]**; el manual 14 no lo lista entre los que usa, sí la fuente que cita); R23 animacidad **[investigación, resumen]** | — |
| Crece de 1,0 a 1,7 (looming suave) | «vuelve hacia ti» | atención | R4, R5 **[investigación]**; en un adulto frente a un teléfono: **[hipótesis del equipo]**. Dosis 8–12 f con frenada, máx. ≈ 75 % del ancho (tabla 2.2): aquí 15 f y 20 % | visto frente a deslizado |
| Lápiz colgado en el empalme (velocidad mínima) | pausa, suspensión | expectación | pausa en el movimiento, R22 **[oficio]**; manual 04, «Pausa (hold)» | — |
| Atrapada con retroceso y oscilación | «llegó, tiene peso» | satisfacción, alivio leve | overshoot con muelle y seguimiento R22 **[oficio]**; dosis: se pasa 10–15 %, se asienta en 8–14 f | — |
| Final = lanzamiento | último golpe corto | curiosidad, activación alta | regla 2 de §4b.2: terminar en activación alta; R34/R48 pico y final **[investigación]** (con sus límites) | duración media vista; no sustituye el remate ni la invitación |
| Bucle | cierre redondo | ganas de repetir | manual 14, tabla 2.4: último fotograma = primero. **Aviso:** la repetición no es vista calificada (P3): el bucle es extra visual, no argumento | duración media vista > 100 % |

**Habituación (R10).** Una firma que se repite deja de provocar la respuesta de orientación. Aquí eso **es lo deseado**:
la firma es de reconocimiento, no de atención; por eso es pequeña (20 % del ancho), corta y siempre igual, y no
escala con el tiempo. La atención del gancho la siguen llevando el texto y el objeto del tema.

## 2. Cierre: el lanzamiento

**Quién:** Tan. **Una sola acción** (lanzar). Pose inicial: `saluda` (brazo `bd` en 100°/155°, abierto), con el lápiz en la
mano en el ángulo de siempre (−60°), cabeza inclinada 25° mirando el objeto, expresión de la portada del video.
Tin: `parado`, `objeto=False`, expresión de la portada, cabeza 25°.

### 2.1 Plano y medidas de partida

Se usan las medidas del plano de portada del canal (las de la toma 1 del video de GTA 6, que son las de
`ENTREGA_YOUTUBE.md`, «Portada de los Shorts»): texto en y 400–700; objeto del tema en y ≈ 744–1075; Tan en x = 259 px
(24 %), Tin en x = 821 px (76 %); pies en y = 1651 (86 %); `alto` = 487 px, o sea R = 88,07 px; los dos de perfil mirando
al centro; caras de Tan en x 121–303 e y 1201–1364 y de Tin en x 752–955 e y 1163–1364. **Cada video usa sus propias
medidas** (se miden en su fotograma 0); estas valen para la prueba técnica.

**Punto de mano H** (centro del lápiz sujeto, pose `saluda`, perfil `mira=1`):
`mano = (x_Tan + 1,072 R, suelo − 3,668 R)` = (353,6; 1328,1) y el lápiz va a `(+0,05 R; −0,25 R)` de la mano:
**H = (358,0; 1306,1)**.

### 2.2 Tabla por toma: cierre (plano de cierre de 30 f: c −30 a −1)

| Fase | Fotogramas (c) | Qué hace Tan | Qué hacen Tin y el lápiz | Curva / muelle | Respaldo |
|---|---|---|---|---|---|
| Reposo | −30 a −25 (6 f) | `saluda` con el lápiz (−60°); el plano entra por `borrón` desde la toma anterior; **el texto del gancho entra con `pop` en c = −30** y está asentado en c = −22 | Tin quieto; el lápiz en su mano | `pop` (rigidez 220, amortiguación 20, masa 1) para el texto | tabla 2.7: palabra clave 4–6 f de entrada |
| **1. Anticipación** | −24 a −19 (6 f; 5 intervalos) | El brazo `bd` baja de (100°, 155°) a (−25°, 20°): mano baja y atrás, a la altura de la cadera. El cuerpo se echa atrás −8 px. Cabeza 25° → 0° (baja la vista al lugar del lanzamiento). Cara `concentrado` | El lápiz gira con la mano de −60° a −100° (`giro_objeto` −40°). Tin quieto | ease-out cúbico (`eo`); nada lineal | R22 anticipación **[oficio]**; manual 04, «Anticipación» y «Determinación» (`plants feet, nods once`); dosis 4–8 f |
| **2. Acción: impulso** | −19 a −15 (4 intervalos) | El brazo barre de (−25°, 20°) a (100°, 155°) acelerando; el cuerpo pasa de −8 a +10 px; la mano llega al máximo de velocidad (≈ 31 °/f en cada articulación) | El lápiz gira de −100° a −30° (`giro_objeto` +30°) | ease-in cúbico (acelera) | R22 arcos: la mano describe un arco porque se interpola por ángulos, no por puntos |
| **Suelta** | **−15** | El brazo está en (100°, 155°). **La cara vuelve a la de la portada del video** | El lápiz sale de la mano en H, ángulo −30°, escala 1,0, y deja de ser parte del cuerpo | corte de estado (un fotograma) | — |
| **Vuelo de ida** | −15 a 0 (15 intervalos) | Mira el lápiz; cabeza 0° → 25° en el vuelo | Ver §2.3 | ver §2.3 | R4, R5, R22 |
| **3. Pose final y seguimiento** | −15 a −4 | **Sobrepaso del brazo:** +12° en el hombro y +13° en el codo a los 2–3 f de soltar (c ≈ −12,7), asentado (≤ 1°) en c = −4. El cuerpo vuelve de +10 px a 0. Las puntas de la bufanda se van hacia atrás al avanzar el cuerpo y oscilan | Tin: nada. **El lápiz sigue solo** | brazo: muelle `POP` (220, 20, 1) como respuesta al impulso; cuerpo: `SLIDE` (120, 16, 1); bufanda: `viento` = −0,06 × velocidad horizontal del cuerpo en px/f, recortado a ±0,8, con `SLIDE` | seguimiento y acción superpuesta, R22 **[oficio]**; acción secundaria, R24 |
| **Empalme** | c = 0 = f0 | Tan queda en `saluda` abierta, mirando arriba (25°), con la cara de la portada | El lápiz en el aire, a la mitad de su vuelo, nítido (§4) | — | manual 14, tabla 2.4 (bucle) |

**Frase de actuación en inglés** (para el registro; estas tomas se dibujan con código, no se envían a un modelo de video):
*Tan swings her arm back and down, snaps it forward and releases the pencil, then lifts her chin and watches it spin
up and hang in the air with her open hand still raised.*

**Panel de referencia** (`personajes/tan/referencias/expresiones.png`): `concentrado` para la anticipación; la de la
portada del video (`curiosidad`, `eureka` o `sorpresa`) para el resto. Poses de `poses.png`: `saluda`.

**Qué pasa con el texto y la invitación.**
- **La voz termina como máximo en c = −17** (0,57 s antes del empalme). La anticipación puede empezar durante la
  última sílaba; el lanzamiento no.
- La invitación a suscribirse y la pregunta abierta final (manual 14, §4b.4) se dicen **antes** de c = −17 y, si llevan
  texto, ese texto sale **antes de c = −30**. **La firma no lleva texto propio:** el único texto del plano es el del
  gancho, que ya está ahí por el bucle.
- La firma no se usa para pedir nada; es lo que queda después de la petición.

### 2.3 Trayectoria y giro del lápiz volando (cierre y apertura son el mismo vuelo)

**Qué se ve:** un lápiz de Tin, el de `palitos.lapiz` (mostaza con contorno de tinta, punta naranja claro, goma tomate),
dibujado **más grande porque pasa por delante de los personajes** (escala 1,0 en la mano, 1,7 en el punto más alto). No
se deforma (objeto rígido: manual 14, 2.5, «aplastar y estirar»: no).

**Profundidad:** el vuelo es hacia la cámara y de lado: crece de 1,0 a 1,7 y vuelve a 1,0. Es el único «looming» del video
y es suave. Equivale a z = 1000 / s − 1000: z = 0 en la mano; **z ≈ −412 en el punto alto** (`Camara.focal` = 1000, `Capa.z`
negativo = más cerca). Delante de los personajes, nunca detrás.

**Trayectoria (plano de prueba, en px; en R relativas a los pies de Tan va entre paréntesis):**

| Punto | Tramo de ida (cierre), Bézier cúbica B1 | Tramo de vuelta (apertura), Bézier cúbica B2 |
|---|---|---|
| P0 / Q0 | H = (358,0; 1306,1) (1,12 R; 3,92 R) | S = (585; 1235) (3,70 R; 4,73 R) |
| P1 / Q1 | (372; 1240) (1,28 R; 4,67 R) | (597; 1290) (3,84 R; 4,10 R) |
| P2 / Q2 | (570; 1165) (3,53 R; 5,52 R) | (420; 1372) (1,82 R; 3,17 R) |
| P3 / Q3 | S = (585; 1235) | H = (358,0; 1306,1) |

- **S es el punto del empalme.** La tangente de B1 en S es (15, 70) y la de B2 es (12, 55): misma dirección (0,21; 0,98),
  casi vertical hacia abajo. El punto más alto de la ida está en y ≈ 1207; el más bajo de la vuelta, en y ≈ 1330 (x ≈ 436).
  Forman un lazo aplastado: sube por fuera y vuelve por abajo, como un bumerán.
- **Pasillo libre:** x 330–750 e y 1100–1340, entre el objeto (abajo en y 1075), la cara de Tan (derecha en x 303) y la
  de Tin (izquierda en x 752).
- **Velocidad a lo largo del tramo** (u = avance de 0 a 1 en el tramo): `τ(u) = (1 − w)·(1 − (1 − u)²) + w·u` en la ida
  (sale rápido y frena) con **w = 0,35**; `τ(u) = (1 − w)·eio(u) + w·u` en la vuelta (arranca despacio, acelera y
  frena) con **w = 0,247**. Longitudes ≈ 290 px (ida, 15 intervalos) y ≈ 275 px (vuelta, 10 intervalos). Resultado:
  salida ≈ 32 px/f, velocidad en S ≈ 6,8 px/f **en los dos lados** (se comprueba, §4), máximo de la vuelta ≈ 69 px/f.
- **Escala:** ida `s = 1 + 0,7·(1 − (1 − u)²)`; vuelta `s = 1,7 − 0,7·eio(u)`. Pendiente 0 en S por los dos lados.

**Giro (siempre en sentido horario en pantalla, ángulo en grados como en `palitos.lapiz`; no hay inversión):**

| Tramo | Ángulo | Velocidad angular |
|---|---|---|
| Ida (15 f) | `θ = −30° + 220°·g₁(u)`, `g₁ = 0,75·(1 − (1 − u)²) + 0,25·u` | sale a ≈ 25,7 °/f y llega a S a **3,67 °/f** |
| Vuelta (10 f) | `θ = 190° + 110°·g₂(u)`, `g₂ = 0,666·eio(u) + 0,334·u` | sale de S a **3,67 °/f**, máximo ≈ 25 °/f, llega a la mano a ≈ 3,7 °/f |
| Total | −30° → 300° (= −60°, el ángulo de la mano) = **330°, poco menos de una vuelta** | **máximo de diseño 30 °/f (900 °/s); límite duro 40 °/f** |

En S el ángulo es **190°** (la punta apunta hacia Tan, casi horizontal, ≈ 216 px de largo): en el fotograma 0 se lee
«lápiz» y «viene hacia ella». La goma y la punta se distinguen por color (tomate / naranja claro), así que la vuelta se lee aunque
el palo sea simétrico.

**Cómo se dibuja girando:**
- **Silueta:** el lápiz de `palitos.lapiz` con una `Pluma` de radio `R·s`; el contorno de tinta crece con la escala (≈ 6 px
  en S). Sin estela dibujada aparte: la estela es el borrón del obturador.
- **Desenfoque de movimiento por obturador, no por filtro:** se pinta el lápiz en `n` subpasos dentro de medio
  fotograma (obturador de 180°) y se promedian con alfa premultiplicado. `n = clamp(round(1 + v/10), 1, 6)` con `v` en px/f.
  En S (v ≈ 6,8) son 2 subpasos y el borrón es de ≈ 3 px: **nítido**. En el máximo de la vuelta (69 px/f) son 6 subpasos
  repartidos en ≈ 34 px. `efectos.borron` no sirve (solo horizontal o vertical y solo RGB).
- Se pinta en una capa RGBA propia con `Capa(z = 1000/s − 1000)`; se compone sobre el plano ya hecho.

**Sombras (profundidad, R3 [investigación]):**
- **Sombra proyectada** sobre el papel, vía `Capa.sombra`: `dx = 14·s`, `dy = 10·s`, `radio = 10·s`,
  `opacidad = 0,22 − 0,07·(s − 1)/0,7` (más lejos del plano, más suave y más clara: 0,22 en la mano, 0,15 en S).
- **Sombra de suelo** en y = 1651 bajo el lápiz (`capa_sombra_contacto`): `ancho = 90 + 50·(s − 1)/0,7` px,
  `opacidad = 0,26 − 0,12·(s − 1)/0,7`. No toca los pies de nadie (el vuelo queda entre x 358 y 600).

### 2.4 Reacción del otro personaje en el cierre

**Tin** (de partida): quieto y con la cabeza a 25° mirando el objeto; no reacciona en el cierre, para no llevarse la
mirada del lanzamiento. **Una acción por toma.** Variación permitida: ninguna reacción o, en videos con remate de
sorpresa, `sorpresa` ya fija desde la portada.

## 3. Apertura: el regreso y la atrapada

**Quién:** Tan atrapa (la misma que lanzó). **Una sola acción** (atrapar). Cuando el video empieza, el lápiz ya está en el
aire; no «entra» desde el borde (así el fotograma 0 lo tiene a la vista).

### 3.1 Tabla por toma: apertura (primer plano del video; dura **30 f como mínimo**)

| Fase | Fotogramas (f) | Qué hace Tan | Qué hace el lápiz / Tin | Curva / muelle | Respaldo |
|---|---|---|---|---|---|
| **Pose inicial = empalme** | **f0** | `saluda` abierta, cabeza 25°, cara de la portada, cuerpo en x. **Texto del gancho entero y quieto** (sin `pop`) | Lápiz en S: (585; 1235), 190°, escala 1,7, v ≈ 6,8 px/f. Tin `parado`, `objeto=False` | — | `ENTREGA_YOUTUBE.md`: el primer segundo es la portada; manual 14 §4, gancho: movimiento desde el fotograma 0 |
| **1. Anticipación (de la atrapada)** | f0 a f4 | Tan **no se mueve**: la mano abierta es la anticipación (ya está lista). La cabeza baja 25° → 0° entre f2 y f10 siguiendo al lápiz | El lápiz baja y vuelve, acelerando suave | `eio` | R22: la pose de espera ya es la anticipación; manual 04, «Mirada» (`looks at the box`) |
| **2. Acción: regreso** | f0 a f10 (10 intervalos) | Mano en H; la cabeza llega a 0° en f10 | Vuelo B2 con el giro de §2.3; sube a ≈ 69 px/f hacia f5 y frena hasta ≈ 6,8 px/f al llegar | §2.3 | R4, R5, R22 |
| **Contacto** | **f10** | El lápiz queda en la mano en −60° (ángulo de `saluda`). **Retroceso:** el brazo cede −10° en el hombro y −10° en el codo (pico a los 2–3 f), el cuerpo se echa −6 px y vuelve | Golpe de sonido (§7). Tin da un saltito de −5 px (arriba) y vuelve | brazo: `POP` (220, 20, 1) como impulso; cuerpo: `SLIDE` (120, 16, 1); Tin: `POP` | R22 overshoot, seguimiento; dosis 8–14 f |
| **3. Pose final y acción secundaria** | f10 a f24 | Sostiene el lápiz en `saluda`; la cabeza sube de 0° a 25° entre f14 y f22 (vuelve a mirar el objeto mientras habla) | El lápiz oscila en la mano: `giro_objeto` = 14°·(1 − muelle(t, k = 560, c = 10, m = 1)), residual < 2° a los 15 f (f25). Bufanda con `viento` como en el cierre | muelles declarados | acción secundaria, R22, R24 |
| **Voz de Tan** | **entra en f14** | Cara de la portada (no cambia con el habla) | — | — | §7 |
| Fin de la firma | f25 a f30 | Plano en reposo hasta el corte o el `borrón` hacia la toma 2 (el lápiz sale de la mano de Tan en esa transición y no se explica: es la convención del canal, §1) | — | — | — |

**Frase de actuación en inglés:** *The pencil spins back into frame, slowing as it comes home; Tan follows it with her
eyes, catches it with a small recoil of the arm and the body, and lifts her chin to the question.*

**Cómo cumple la regla de portada.**
1. **Fotograma 0:** texto del gancho entero y quieto (y 400–700, mayúscula inicial en cada palabra, palabra clave en el
   acento); objeto del tema nítido y completo (y 720–1100); las dos caras dentro de la zona útil (x 60–960, y 380–1440),
   con curiosidad o sorpresa, mirando el objeto; y **el lápiz, entero, nítido y a ≈ 20 % del ancho en el pasillo**
   (x 480–690, y 1130–1340), **dentro de la zona útil, sin tocar texto, objeto ni caras** (distancias mínimas en la sección 11).
2. **El lápiz se queda en el fotograma 0** porque (a) la firma tiene que registrarse en el primer segundo para que la
   mera exposición funcione (R26), (b) el movimiento desde el fotograma 0 es lo que pide el manual para el gancho, y (c) el
   lápiz horizontal con la punta hacia Tan es legible incluso como imagen fija. **Qué se arriesga:** un cuarto elemento en
   la portada. Se mantiene pequeño, bajo el objeto y lejos de las caras; si el dato de la sección 10 dice que baja el «se
   quedó a mirar», la primera medida es acortar la apertura, no quitar el lápiz del fotograma 0.
3. **El primer plano dura 30 f o más**, así que el gancho de varios cortes (2 o 3 planos en 30 f, con el primero de 12 f o
   más) se puede hacer: la firma ocupa el primer plano y no pisa el corte.

## 4. Empalme del bucle

### 4.1 Condiciones exactas (todas se miden; las comprueba `comprobar_firma`, §9)

El estado del cuadro `c = 0` (que es el fotograma 0) es **el mismo** que el que seguiría al último (`c = −1`) si el video
siguiera una vez más. Para que eso valga:

| Magnitud | Valor en el empalme | Tolerancia |
|---|---|---|
| Posición del lápiz | S = (585; 1235) en el plano de prueba (el `S` del video, `geo["S"]`) | ±0 px: el fotograma 0 se calcula con la **misma** función que el fotograma `N` |
| Ángulo del lápiz | 190° | ±0° |
| Escala del lápiz | 1,7 | ±0 |
| Velocidad del lápiz | 6,8 px/f en la dirección (0,21; 0,98) | diferencia entre el lado de ida y el de vuelta ≤ 1 px/f y ≤ 3° |
| Velocidad angular | 3,67 °/f | diferencia ≤ 0,5 °/f |
| Brazo `bd` de Tan | (100°, 155°) | ±2° (la cola del muelle en c = −1 es < 1°) |
| Cuerpo de Tan | x de la portada | ±1 px (la cola del `SLIDE` en c = −1 es ≈ 0,25 px) |
| Cabeza de Tan | 25° | ±0,5° |
| Expresiones | las de la portada del video, ambas | iguales |
| Texto del gancho | entero y quieto | sin diferencia |
| Cámara, fondo, grano (`papel`) | fijos | iguales |

Entre el último fotograma y el primero, **el movimiento del lápiz es de un solo paso** (≈ 6,8 px y 3,7°): no hay salto.
Con el sonido igual (§7): la cola del whoosh de ida y el inicio del de vuelta están al mismo nivel.

### 4.2 Si el video no puede ir en bucle (cierre con pregunta de suspenso, u otro cierre que pida otro último cuadro)

La apertura **no cambia** (el lápiz ya está en S en el fotograma 0; el espectador que ve el video de nuevo desde el
principio ve un salto, y eso es aceptable porque el bucle no es lo que decide el cierre: manual 14, §4b.2 punto 6).
Cambia el cierre: **lanzamiento sin retorno**.

| Fase | Fotogramas (c) | Qué cambia |
|---|---|---|
| Anticipación, impulso | −27 a −22 y −22 a −18 | Igual que §2.2, 3 f antes |
| Suelta | −18 | Igual |
| Vuelo | −18 a −1 (17 intervalos) | Bézier B3: P0 = H, P1 = (420; 1180), P2 = (700; 980), P3 = (1180; 820), con aceleración de salida (`eo` invertido), escala de 1,0 a ≈ 3,4 y giro de 330° (el mismo tope de 30 °/f). El lápiz sale por el borde derecho por encima de la cabeza de Tin (despeje ≥ 50 px) y pasa por delante del objeto 4 o 5 f: se acepta porque este final no es portada |
| Fin | −5 a −1 | El lápiz ya salió; Tan y Tin con la cabeza a 25° mirando hacia donde se fue; **silencio 9–15 f** (manual 14, 2.8: silencio antes del dato / expectación). El último plano lleva la pregunta abierta como texto en la zona de texto, no encima del lápiz |
| Sonido | — | El whoosh de ida cae a silencio en c ≈ −5, sin golpe de cierre |

Esto da el cierre «Tan lanza la pregunta al aire y no vuelve». Solo se usa si la pregunta abierta cumple las condiciones del
manual 14, §4b.3 (hecho público, con fecha, que el canal se compromete a responder).

### 4.3 Variante `atrapa="tin"` (si el dueño quiso decir «las manos de Tin»)

Tin con pose `saluda` espejada hacia el centro (mano en x = 821 − 1,122 R = 722 px), lápiz en su mano al final del vuelo; el
vuelo B1/B2 se refleja respecto del eje x = 540. Cambios que trae, para decidir con el dueño: (1) el lápiz aterriza en
Tin y la voz sigue siendo de Tan (dos focos: pérdida de la lectura A); (2) en el empalme Tan queda con el brazo
extendido sin lápiz y Tin con la mano arriba (dos poses nuevas en la portada); (3) la voz puede entrar antes (f4) porque
el golpe no cae en el personaje que habla. Se renderiza en la prueba técnica solo si el dueño lo pide.

## 5. Variaciones permitidas y límites

### 5.1 Lo que puede cambiar por video sin dejar de ser la firma

| Qué | Rango | Por qué se permite |
|---|---|---|
| Anticipación | 4 a 8 f | dosis de la tabla 2.5 |
| Vuelo de ida / de vuelta | 12 a 16 f / 8 a 12 f | tiempo de gancho; la vuelta nunca más de 12 f |
| Altura del punto alto (S y arco) | ±40 px según el pasillo del video | cada portada deja un pasillo distinto |
| Vueltas | 330° (de partida). El total tiene que ser 330° o 690° para que el lápiz llegue a la mano en −60°; 690° solo si se alargan los tramos y no se pasa de 30 °/f | que el ángulo de llegada a la mano sea −60° |
| Quién reacciona | Tin (saltito en la atrapada, de partida), nadie o, en videos de remate de sorpresa, `sorpresa` | una sola reacción |
| Cara de Tan y de Tin | las de la portada del video | la portada ya las fija |
| Cierre | bucle (de partida) o sin retorno (§4.2) | el cierre lo decide el director creativo |
| Que el lápiz «traiga» el objeto del tema | **No en v1.** En el cierre, el objeto del tema no se mueve; en la apertura, no entra con el lápiz. Razón: el fotograma 0 tiene que mostrar el objeto completo y quieto (portada) | proponerlo solo si la prueba técnica y los datos dicen que la firma funciona |

### 5.2 Lo que nunca cambia

- Lanza y atrapa **Tan**, con la mano del brazo `bd`. Tin no lo toca.
- El lápiz: el de `palitos.lapiz`, mostaza con contorno de tinta, goma tomate, punta naranja claro. No se deforma, no cambia de
  color, no deja estela dibujada, no se divide.
- Sentido horario del giro; arco por el pasillo; escala 1,0 a 1,7 a 1,0; sin salir del cuadro en el bucle.
- Empalme exacto (§4.1). El texto del gancho está entero en el fotograma 0.
- Cámara fija, sin destello, sin zoom, sin sacudida (§8).
- El mismo sonido (§7). Voz de Tan en f14 como mínimo.
- Duración: **la firma completa no pasa de 34 f (1,13 s)**; la apertura de acción, **no más de 12 f**.
- Una acción por plano (lanzar / atrapar); un solo lápiz en pantalla.

### 5.3 Duración máxima y por qué

El primer segundo decide si se quedan: en el primer Short, 20,7 % se quedó a mirar (533 vistas; una sola muestra). La
apertura de acción es de 10 f; con la entrada de la voz en f14 el costo sobre el gancho es **0,47 s de voz tardía**.
Esa es la apuesta de la firma. Reglas para no robar más: tope de 12 f de acción (§5.2); la primera frase se mantiene
entera; si la firma se alarga, el editor la recorta antes de recortar el gancho.

### 5.4 Cuándo no se usa

- **Serie infantil (Tiky y Lumi): nunca.** Es solo de Tin & Tan. En infantil no hay bucle como gancho, ni escala rápida hacia cámara,
  ni golpes de sonido (manual 14, §5.3).
- Videos sin Tan en la portada.
- Portadas donde no haya pasillo libre (sección 11, punto 2): se rediseña la portada, no se aprieta la firma.
- Si se mide daño al «se quedó a mirar» (§10): se recorta o se pausa.
- No se aplica a videos ya renderizados. **Pendiente del jefe de producción y del dueño:** si el video en curso del canal
  (Jensen Huang) lleva la firma o espera al siguiente. Este archivo no toca ese proyecto.

## 6. Profundidad y cámara (para el director de fotografía)

| Elemento | Valor | Comunica / emoción | Respaldo |
|---|---|---|---|
| Cámara | fija, escala 100 %, sin `avance`, sin `temblor` | las medidas de la portada valen todo el plano; calma | cap. 14, §6 (paralaje ≤ 8 %/s: aquí 0) |
| Foco | todo nítido (`apertura = 0`); el lápiz solo se desenfoca por obturador | legibilidad desde el fotograma 0 | R27 fluidez |
| Capas | papel (z fondo) · objeto y personajes (z = 0) · **lápiz volador (z = 1000/s − 1000, de 0 a ≈ −412)**; sombras como en §2.3 | el lápiz pasa por delante, por oclusión (R2) y por sombra (R3) | R2, R3 **[investigación]** |
| Pasillo | x 330–750, y 1100–1340 (plano de prueba) | lugar del vuelo | — |
| Sombra proyectada | `dx = 14 s`, `dy = 10 s`, `radio = 10 s`, `opacidad` 0,22 → 0,15 | altura | R3 |
| Sombra de suelo | `capa_sombra_contacto(x, 1651, ancho 90 → 140, opacidad 0,26 → 0,14)` | altura sobre el suelo | R3 |
| Niebla / viñeta / grano | los del video; el grano fijo (`papel()`) | — | R42: sin parpadeo |
| Color | lo de §8 | acento | cap. 13 |

**Para firmar o corregir:** (a) que el pasillo (y 1100–1340) sea aceptable como lugar del lápiz en la portada; (b) que el
lápiz grande (216 px) en el fotograma 0 no estropee la lectura de la miniatura; (c) las distancias mínimas de la §11 punto 2
(≥ 30 px al texto y al objeto, 0 a las caras).

## 7. Sonido (para el diseñador de sonido)

**Principio:** el sonido es la mitad del efecto (manual 14, 2.8) y la firma lleva **siempre el mismo sonido** (R26, R27;
manual 14, §7.1 fila 7). **Referencia de nivel:** la voz está a −14 LUFS integrado, con picos cerca de −1 dBFS. Los
niveles de abajo son picos en dBFS; ninguno pasa de −12 dBFS.

| # | Fotograma | Evento | Duración | Contenido (propuesta) | Pico |
|---|---|---|---|---|---|
| S1 | c = −17 a −15 | Chasquido de brazo y suelta | 3 f (100 ms) | ruido de banda corta que sube, 1 a 4 kHz, seco | −20 dBFS |
| S2 | c = −15 a 0 | Whoosh de ida | 15 f (500 ms) | ruido filtrado 600–2.500 Hz; **la envolvente sigue la velocidad del lápiz** (32 → 6,8 px/f); tono que baja de 1.800 a 900 Hz; **dos pulsos** de modulación de ±3 dB cuando el lápiz cruza la horizontal: **c ≈ −14 y c ≈ −2** | −20 dBFS al inicio, cae a −34 dBFS al final |
| S3 | f0 a f10 | Whoosh de regreso | 10 f (333 ms) | **empieza a −34 dBFS, igual que la cola de S2** (sin hueco en el empalme); tono que sube de 900 a 1.700 Hz; envolvente = velocidad (6,8 → 69 → 6,8 px/f), máximo hacia f5; **sin pulsos** (en la vuelta el lápiz no cruza la horizontal) | −18 dBFS en f5, cae a −30 dBFS en f10 |
| S4 | f10 | **Golpe de atrapada** | 3 f (90 ms) + cola de 1 f | golpe de madera seco + «pop» corto, centro ≈ 1,2 kHz, caída de 30 dB en 90 ms. **Es el único golpe de la firma y el mismo archivo en todos los videos** | **−12 dBFS** (≈ 11 dB bajo el pico de la voz) |
| — | f10 a f13 | Silencio de efectos | 4 f | nada por encima de −45 dBFS | — |
| Voz | **f14** | Primera sílaba de Tan | — | — | — |

**Cómo no pisa la primera sílaba de Tan:**
1. La voz de Tan **entra en f14**, 4 f después del pico del golpe (f10) y 1 f después de que termine su cola (f13).
   Sin escucha no se sabe dónde cae la sílaba exacta de la voz generada; se mide con `silencedetect` sobre el audio ya
   armado y se corrige el desfase, no el efecto.
2. Ningún sonido de la firma se programa después de f10 por encima de −45 dBFS.
3. **En el cierre la voz termina en c ≤ −17** y S1 empieza en c = −17: no hay solapamiento con la última palabra.
4. Empalme de audio: fundido de 2 f (66 ms) entre el final del video y el inicio, con S2 y S3 al mismo nivel (−34 dBFS):
   el whoosh es **uno solo** que atraviesa el empalme.
5. Música: la firma no lleva música propia; si el video tiene música, se baja 6 dB desde c = −24 hasta f14 (pedido al
   editor, no a esta firma).

**Para firmar o corregir:** los cinco niveles, la frecuencia del golpe, los dos pulsos de S2 (los pulsos se atan al
paso por la horizontal porque en 330° de giro el lápiz no completa una vuelta entera: atar el ritmo a «vueltas
completas» daría cero o un pulso), y el origen de los sonidos (Mirelo en Higgsfield cuesta créditos y pide el sí del
dueño; el estudio puede sintetizarlos por código gratis con Web Audio o `postpro.py mezclar --efectos archivo@segundo`).

## 8. Color y seguridad

### 8.1 Color

- **El lápiz es identidad, no acento.** Es parte de «lo que nunca cambia» de Tin (mostaza `#E8B33B`, contorno de tinta
  `#2B2420`, goma tomate `#C8553D`, punta naranja claro `#F2A35E`) y `DESIGN.md` ya lo asigna a la mostaza. En los
  planos de firma cuenta como elemento de acento cuando el acento del video es mostaza, y como identidad (como las
  cabezas y la bufanda) cuando no lo es.
- **Contorno de tinta siempre:** sobre papel la mostaza da 1,6:1 (`DESIGN.md`); sin contorno no se lee.
- **Conflicto posible, a decidir por el director de fotografía:** si el objeto del tema es mostaza (el mando del video de GTA 6),
  hay dos mostazas en el plano (la palabra clave y el lápiz, más el objeto). Propuesta: el lápiz no cede; el objeto del tema
  usa tinta o el acento del video si no es mostaza.
- **Goma tomate:** ≈ 0,2 % del cuadro; excepción a «tomate nunca con mostaza en el mismo plano» porque es parte del lápiz.
- `revisar_color.py`: se mide el fotograma 0 y el fotograma de S; en la prueba, ≥ 85 % en el fotograma nítido de
  control (criterio de `DESIGN.md`, pendiente de firma).

### 8.2 Seguridad (manual 14, §6; todo se comprueba antes de entregar)

| Límite | Valor de la firma | Cómo se comprueba |
|---|---|---|
| Destellos | ninguno: **sin destello de impacto en la atrapada, sin zoom de golpe, sin sacudida**; el impacto es sonido más retroceso del cuerpo | `efectos.comprobar_destellos` sobre toda la prueba: 0 cambios bruscos |
| Un efecto por punto | la atrapada es un solo evento: golpe + retroceso + oscilación (no se suma ningún efecto de cámara) | revisión de fotogramas |
| Mareo (R44) | cámara fija; objeto en movimiento de ≤ 20 % del ancho; **velocidad angular de diseño 30 °/f (900 °/s), límite duro 40 °/f (1.200 °/s)**; **velocidad lineal máxima 69 px/f, límite duro 90 px/f (≈ 8 % del ancho por fotograma)**; menos de una vuelta por tramo | `comprobar_firma` y revisión; **los números son [hipótesis del equipo]** (ninguna fuente abierta da umbral) |
| Parpadeo por giro | ω ≪ 90 °/f: sin efecto de «rueda de carreta» (aliasing a ≈ 180 °/f para un palo) | cálculo |
| Patrones | un solo objeto, sin rayas ni cuadrículas | revisión |
| Rojo | la goma es tomate; no hay parpadeo hacia o desde rojo saturado | revisión |
| «Reducir movimiento» del teléfono | no se puede leer: los límites se aplican a todos | — |

## 9. Implementación

### 9.1 Qué hay que programar y dónde (no se toca código en este encargo)

| # | Dónde | Qué | Por qué |
|---|---|---|---|
| 1 | `palitos.py` 1.4 | `dibujar(..., pose=...)` acepta **un dict** `{"bi": (a1, a2), "bd": (a1, a2), "pi": ..., "pd": ...}` además del nombre de pose; ayudante `pose_entre(a, b, p)`; el resto igual. Con un nombre se dibuja exactamente como siempre | el cierre necesita poses intermedias (empuje atrás, barrido) que no existen en las 9 poses |
| 2 | `efectos.py` 1.1 | `geometria_firma(portada, atrapa="tan")` | calcula H, S y los puntos de Bézier a partir de las medidas de la portada del video (R, posiciones, cajas de texto, objeto y caras); comprueba el pasillo (§11 punto 2) y falla con `FirmaError` si no hay |
| 3 | `efectos.py` 1.1 | `lapiz_bumeran(c, geo, variante="bucle")` | función pura: devuelve el estado de la firma en el fotograma `c`, sin dibujar |
| 4 | `efectos.py` 1.1 | `pintar_lapiz_volador(est, geo)` | devuelve las `Capa` del lápiz (con obturador de subpasos) y de sus dos sombras |
| 5 | `efectos.py` 1.1 | `golpes_firma(N, voz_entra=14)` | lista `(fotograma, nombre, pico_dBFS)` para el diseñador de sonido y `postpro.py mezclar` |
| 6 | `efectos.py` 1.1 | `comprobar_firma(geo, N)` | verifica las condiciones de §4.1, las velocidades de §8.2 y las distancias de §11 punto 2; devuelve un dict como `comprobar_destellos` |

### 9.2 Firma de las funciones

```python
class FirmaError(ValueError): ...

def geometria_firma(portada: dict, atrapa: str = "tan") -> dict:
    """portada: {"R", "x_tan", "x_tin", "suelo", "texto": bbox, "objeto": bbox, "cara_tan": bbox, "cara_tin": bbox}
    -> {"H", "S", "B1", "B2", "R", "s_max": 1.7, "zona_util": (60, 380, 960, 1440), "paso_libre": bbox}"""

def lapiz_bumeran(c: int, geo: dict, variante: str = "bucle") -> dict:
    """c < 0: cierre (c = -24 .. -1); c >= 0: apertura (c = 0 .. 30). Devuelve:
      {"fase": str,
       "lapiz": {"visible", "en_mano", "x", "y", "esc", "angulo", "v", "omega"},
       "tan": {"pose": dict, "dx": px, "expresion": str|None (None = la de la portada), "cabeza_giro": grados,
               "giro_objeto": grados, "objeto": "lapiz" | False, "viento": -1..1},
       "tin": {"dy": px, "objeto": False, "cabeza_giro": 25.0}}"""

def pintar_lapiz_volador(est: dict, geo: dict, fps: int = 30, obturador: float = 0.5) -> list: ...
def golpes_firma(N: int, voz_entra: int = 14) -> list: ...
def comprobar_firma(geo: dict, N: int) -> dict: ...
```

El render llama a `lapiz_bumeran(c)` con `c = f` en la apertura y `c = f − N` en el cierre; dibuja a Tan y a Tin con
`palitos.dibujar(... pose=est["tan"]["pose"], giro_objeto=..., cabeza_giro=..., objeto=...)` y compone encima las `Capa` del
lápiz con `efectos.componer`.

### 9.3 Fórmulas (pseudocódigo; todo depende del número de fotograma)

```python
def bezier(P, t):                       # cúbica
    u = 1 - t
    return (u**3*P[0][0] + 3*u*u*t*P[1][0] + 3*u*t*t*P[2][0] + t**3*P[3][0],
            u**3*P[0][1] + 3*u*u*t*P[1][1] + 3*u*t*t*P[2][1] + t**3*P[3][1])

def tau_ida(u, w=0.35):   return (1 - w) * (1 - (1 - u)**2) + w * u           # sale rápido, frena (no a 0)
def tau_vuelta(u, w=0.247): return (1 - w) * eio(u) + w * u                    # arranca suave, acelera, frena
def g_ida(u):             return 0.75 * (1 - (1 - u)**2) + 0.25 * u
def g_vuelta(u):          return 0.666 * eio(u) + 0.334 * u

# vuelo de ida: c = -15 .. 0   ->  u = (c + 15) / 15
x, y = bezier(geo["B1"], tau_ida(u));  esc = 1 + 0.7 * (1 - (1 - u)**2);  ang = -30 + 220 * g_ida(u)
# vuelo de vuelta: f = 0 .. 10 ->  u = f / 10
x, y = bezier(geo["B2"], tau_vuelta(u)); esc = 1.7 - 0.7 * eio(u);          ang = 190 + 110 * g_vuelta(u)
# velocidad: v = |pos(c+1) - pos(c)| ; omega = ang(c+1) - ang(c)

# brazo de Tan  (a1, a2) = (hombro-codo, codo-mano), en grados, como POSES
c in [-24, -19]:  p = eo((c + 24) / 5);   bd = lerp((100, 155), (-25, 20), p)    # anticipación
c in [-19, -15]:  p = ((c + 19) / 4)**3;  bd = lerp((-25, 20), (100, 155), p)    # impulso
c >= -15:         bd = (100, 155) + (12, 13) * impulso_muelle(t = (c + 15) / 30, k=220, c=20, m=1)   # +12° pico a ~2,3 f
f >= 10:          bd = (100, 155) - (10, 10) * impulso_muelle(t = (f - 10) / 30, k=220, c=20, m=1)   # retroceso al atrapar
# impulso_muelle(t) = e^(-z*w0*t) * sin(wd*t) / valor_en_el_pico   (respuesta a un impulso, normalizada a 1 en el pico)

# cuerpo de Tan (dx en px)
c in [-24, -19]: dx = -8 * eo((c + 24) / 5);  c in [-19, -15]: dx = lerp(-8, 10, ((c + 19) / 4)**3)
c >= -15:        dx = 10 * (1 - muelle((c + 15) / 30, SLIDE))               # ≈ 0,25 px en c = -1
f >= 10:         dx = -6 * (1 - muelle((f - 10) / 30, SLIDE))

# lápiz en la mano: giro_objeto
c in [-24, -19]: -40 * eo(...);   c in [-19, -15]: lerp(-40, +30, ...);   f >= 10: 14 * (1 - muelle((f - 10) / 30, (560, 10)))
# cabeza de Tan: 25 -> 0 (c -24..-19) -> 0 (-19..-15) -> 25 (c -15..0, eio) ; apertura: 25 (f0..2) -> 0 (f10, eio) -> 25 (f14..22, eio)
# cara: 'concentrado' en c = -24 .. -16; cara de la portada en el resto
# Tin: dy = -5 * impulso_muelle(t = (f - 10) / 30, POP) desde f10; nada más
```

**Obturador:** `n = clamp(round(1 + v/10), 1, 6)`; el lápiz se pinta en `n` posiciones entre `c − 0,25` y `c + 0,25`
(medio fotograma centrado en `c`) y se promedia con alfa premultiplicado.

**Declaración de muelles por elemento** (regla 11 del manual 11): texto del gancho: `POP` (220, 20, 1); brazo de Tan al
soltar y al atrapar: `POP` (220, 20, 1); cuerpo de Tan y puntas de la bufanda: `SLIDE` (120, 16, 1); oscilación del lápiz en
la mano: (560, 10, 1); saltito de Tin: `POP`. Posición, escala y giro del lápiz volando: **curvas con frenada, sin muelle**
(un muelle con rebote no corresponde a un vuelo libre). Nada es lineal; la mezcla `w·u` de las curvas es para que el
lápiz nunca se detenga del todo en S.

### 9.4 Plan de prueba técnica (6 s; 0 créditos; antes de usarla en un video real)

1. **Qué se renderiza:** 180 f (6 s) a 1080×1920: dos pasadas del bucle de 90 f. Cada pasada = plano de cierre de 30 f
   (c −30 a −1) + apertura de 60 f (f0 a f59, sin voz; el marcador «voz» en f14 se pinta como una marca de 3 f en el borde).
   Plano de prueba: texto «TEST ?» en y 400–700, un rectángulo de tinta de 600×330 px como objeto (y 744–1075), Tan y Tin de
   perfil con las medidas de §2.1.
2. **Qué se comprueba (todo medible):**
   - empalme: `comprobar_firma` verifica §4.1 entre el fotograma 89 y el 90, y entre el 179 y el 0;
   - tira de 24 fotogramas (c −12 a +11) en una hoja de contactos de 6 × 4 para mirar a ojo el giro, la atrapada y el retroceso;
   - `efectos.comprobar_destellos` sobre los 180 f: 0 cambios bruscos;
   - velocidades: máx. angular ≤ 30 °/f; máx. lineal ≤ 69 px/f (límites duros 40 y 90);
   - despejes (§11 punto 2) en los 34 f de la firma;
   - `revisar_color.py` sobre el fotograma 0 y el de S;
   - tamaño y borrón del lápiz en el fotograma 0 (borrón ≤ 4 px);
   - patinaje de pies de Tan por el desplazamiento de −8 y +10 px: si se nota, se baja a ±5 px;
   - **lectura del bumerán:** si la tira no se lee como «sale y vuelve» (en vez de «rebota»), se prueba la variante de más
     recorrido (el lazo sube hasta y ≈ 1130 y la vuelta baja hasta y ≈ 1380) antes de tocar nada más.
3. **Audio de prueba:** los cuatro sonidos de §7 sintetizados por código, mezclados con `postpro.py mezclar --efectos
   archivo@segundo` con una pista de voz de relleno que entra en f14; se verifica la sincronía a ±1 f. **Falta el oído humano.**
4. **Quién firma la prueba:** el supervisor de continuidad (sección 11), el director de fotografía (§6 y §8) y el diseñador de sonido (§7); la
   aprobación para usarla en un video real es del jefe de producción.
5. **Opcional, 3 s:** la variante `atrapa="tin"` para que el dueño elija por lo que ve.

## 10. Cómo se mide

**Qué dirá si la firma ayuda:**

| Pregunta | Métrica | Dónde | Señal |
|---|---|---|---|
| ¿La reconocen? | **espectadores que regresan** frente a nuevos; **suscriptores por cada 1.000 vistas**; comentarios que nombran el lápiz o a Tan | Studio, `estadisticas/datos/` | sube frente a los videos sin firma |
| ¿Daña el primer segundo? | **«se quedó a mirar» frente a deslizó**; caída de la curva de retención entre 0,3 y 1,0 s (la ventana del lápiz y de la voz tardía); porcentaje medio visto | Studio | referencia: el 20,7 % del primer Short (533 vistas: una sola muestra, **no es una vara de medir**) |
| ¿Sirve el bucle? | duración media vista sobre 100 % | Studio | solo como dato; la repetición no es vista calificada (P3) |

**Honestidad de la comparación.** La firma es para **todos** los videos: no hay un grupo de control limpio y «un video
solo no decide nada» (`PARAMETROS.md` §4). Plan: los **5 primeros videos con firma** se comparan contra los **videos
anteriores sin ella** y entre sí; la comparación queda confundida con el tema de cada video y se dice. **Una cosa por
video:** el primer video con firma no cambia otra cosa del gancho.

**Qué se cambia si la daña** (en este orden, un cambio por paso, con 5 videos por paso):
1. Se acorta la apertura: 10 f → 6 f de acción y la voz entra en f8.
2. Se saca el lápiz del fotograma 0 (la apertura entra a los 6 f por el borde del pasillo) si el problema es la portada.
3. Se deja **solo el cierre** (el fotograma 0 queda limpio).
4. Se retira la firma. Se anota en la bitácora de `PARAMETROS.md`.

Si no daña pero tampoco sube nada en 5 videos, se deja como está y se dice: lo que el dato no distingue no se cambia.

## 11. Lista de comprobación para el supervisor de continuidad (10 puntos; todos se miden en fotogramas)

1. **Empalme:** el fotograma 0 y el último distan un solo paso de vuelo: lápiz a ≤ 8 px y ≤ 4,5° del paso previsto; brazo
   de Tan a ≤ 2°; cabeza a ≤ 0,5°; mismas caras, mismo texto, mismo fondo.
2. **Despejes:** en cada fotograma de la firma, el polígono del lápiz (no el círculo que lo rodea) está a ≥ 30 px del texto y del
   objeto, **a 0 px de las caras (no las toca)**, y el centro está dentro de la zona útil (x 60–960, y 380–1440).
3. **Fotograma 0:** lápiz entero y nítido (borrón ≤ 4 px), texto del gancho entero y quieto, objeto completo, las dos caras
   visibles; el lápiz mide ≈ 20 % del ancho.
4. **Anticipación visible:** el brazo de Tan se mueve en sentido contrario durante 6 f (c −24 a −19) antes del impulso.
5. **Suelta:** en c = −15 el lápiz deja la mano exactamente en el punto de la mano; no hay dos lápices en ningún fotograma
   (salvo los subpasos del obturador); Tin no lleva lápiz.
6. **Giro:** siempre horario; ≤ 30 °/f de diseño (≤ 40 °/f duro); ≤ 330° por vuelo completo; el ángulo en la mano es −60°
   cuando se asienta (f25).
7. **Velocidad y escala:** ≤ 69 px/f (≤ 90 duro); escala máxima 1,7; el lápiz no sale del cuadro en la versión con bucle.
8. **Atrapada:** contacto en f10; retroceso del brazo (−10°) y del cuerpo (−6 px); la oscilación del lápiz baja a < 2° en f25; la
   mano no atraviesa el lápiz.
9. **Cámara y seguridad:** cámara fija; ni destello ni zoom ni sacudida; `comprobar_destellos` en 0; sin cuadrículas.
10. **Sonido:** la voz de Tan entra en f14 o después; el golpe cae en f10 ±1; el whoosh no tiene hueco en el empalme; la
    última palabra de la voz termina en c ≤ −17; en los 34 f de la firma no suena nada que no esté en §7.

## 12. Dudas reales que quedan

1. **«Sus manos»: ¿las de Tan o las de Tin?** Se eligió Tan por la palabra «bumerán», pero lo puede aclarar solo el dueño
   (es una idea, no un dato técnico). Costo de cambiar: una variante, sin rehacer lo ya hecho (§4.3).
2. **¿Un lazo de 210 × 110 px se lee como «bumerán»?** El pasillo es corto porque el objeto y las caras ocupan la
   portada. Solo la prueba técnica lo dirá; si no, se prueba el lazo más largo o un recorrido que salga por encima de la cabeza de
   Tin (§4.2) y se rediseña la portada si hace falta.
3. **Costo de la voz en f14 (0,47 s).** Nadie sabe cuánto pesa sobre el «se quedó a mirar»; es la apuesta de la firma.
4. **El lápiz en el fotograma 0** añade un elemento a la portada. Se defiende por la mera exposición, pero la miniatura se
   decide con datos.
5. **Mostaza doble** cuando el objeto del tema es mostaza (§8.1): lo resuelve el director de fotografía.
6. **Los sonidos** no se han oído: los niveles y el golpe son propuestas. Si se quiere un sonido real hay que pedir un archivo o gastar créditos.
7. **El lápiz «de Tin» en la mano de Tan.** Se apoya en que el canal declara los objetos por toma; si el dueño o el supervisor lo ven
   como falta de continuidad, la alternativa es la lectura A, con las pérdidas de la sección 1.1.
8. **Video en curso (Jensen Huang):** no se toca; el jefe de producción decide si lleva la firma. **Los videos ya renderizados no se
   rehacen** sin el sí del dueño.
9. **El banco de gestos de `manual/04` no trae gestos propios de Tin ni de Tan;** esta firma sería el primero. Falta añadir la
   fila al banco (no se hizo en este encargo).
10. **Patinaje de pies** por el desplazamiento del cuerpo (−8 / +10 px): se verá en la prueba.

## 13. Firmas pendientes

| Rol | Qué firma | Estado |
|---|---|---|
| Director de animación | Idea, fases, curvas, muelles, variaciones (§1 a §5, §9) | firmado en este borrador (2026-11-24) |
| Director de fotografía | §6 y §8 (pasillo, capas, sombras, color, mostaza) | pendiente |
| Diseñador de sonido | §7 (niveles, golpe, pulsos, empalme de audio) | pendiente |
| Editor de video | §5.3 y §7 punto 5 (duración, voz en f14, primer plano de 30 f, música) | pendiente |
| Supervisor de continuidad | §11 | pendiente |
| Director creativo | Perfil emocional fijo de la firma (tabla de §1.3 en cada `perfil_emocional.md`) | pendiente |
| Dueño | Lectura B (Tan–Tan) o A | pendiente |
