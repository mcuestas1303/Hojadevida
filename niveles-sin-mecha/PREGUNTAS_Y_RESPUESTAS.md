# Velas marubozu: preguntas y respuestas

Recopilación de las preguntas que surgieron a partir de las velas sin mecha (marubozu) de XAUUSD en IC Markets y de las respuestas que se dieron, en el orden en que ocurrieron.

- Fechas en hora de El Salvador. Las conversaciones fueron el 6 de octubre de 2026.
- Las respuestas son las originales. Solo se quitaron los avisos de archivos enviados y los pasos de instalación.
- Donde un análisis posterior confirmó o corrigió algo, va una nota **«Lo que vimos después»**.
- Cada respuesta distingue lo **documentado** (con fuente) de lo que es **interpretación**.

**Contenido**

- Parte 1. Cómo se forma una marubozu
  1. ¿Por qué hay flechas de diferentes colores?
  2. ¿Por qué razón, en la formación de una vela, se dan esos casos?
  3. ¿Qué son los ticks?
  4. ¿El precio de la vela no es el precio al que compraron?
  5. ¿Me lo puedes explicar con velas, de forma interactiva?
- Parte 2. Los participantes y el desequilibrio
  6. ¿Qué persigue cada participante y por qué el precio vuelve a una marubozu?
  7. ¿Importa cuándo vuelve el precio?
  8. ¿Qué persigue cada participante en cada paso, y cómo encaja la idea de desequilibrio?
  9. Mi ejemplo: una marubozu no testeada y otra que sí se testeó
- Parte 3. Estadísticas con datos de IC Markets
  10. ¿Cuántas se forman, cuántas se testean, en cuánto tiempo, y hay jerarquía entre temporalidades?
  11. ¿Se confirma la jerarquía con más historial (H1)?
  12. ¿Qué pasó con las velas que no fueron testeadas?
  13. ¿Cómo se comportan por sesión?
  14. ¿Hay sesiones en las que se forman más marubozu?
  15. ¿En qué franjas horarias aparecen menos?
  16. ¿Cuáles son esas franjas en hora de El Salvador?
- Parte 4. De los datos a la operativa
  17. ¿Qué reglas establecerías en un fondo retail para scalping e intradía?
  18. ¿Cómo medimos el spread?
  19. ¿Qué salió al medir el spread?

---

# Parte 1. Cómo se forma una marubozu

## 1. ¿Por qué hay flechas de diferentes colores?

> *"Listo porque razón hay flechas con diferentes colores"* — 6 oct, 11:53

Cada color indica cuál de las cuatro condiciones cumple la vela. Así sabes, solo con mirar, si la que coincide con el extremo es la **apertura** o el **cierre**.

| Flecha | Dónde | Qué pasó en la vela | Lectura típica |
|---|---|---|---|
| ▼ **Roja** | Encima | **Apertura = Máximo**: abrió en el punto más alto y no subió nada | Vela bajista sin mecha arriba; los vendedores tomaron el control desde el inicio |
| ▼ **Naranja** | Encima, un poco más arriba | **Cierre = Máximo**: cerró en el punto más alto | Vela alcista que terminó con fuerza compradora |
| ▲ **Verde** | Debajo | **Apertura = Mínimo**: abrió en el punto más bajo y no bajó nada | Vela alcista sin mecha abajo; los compradores tomaron el control desde el inicio |
| ▲ **Azul** | Debajo, un poco más abajo | **Cierre = Mínimo**: cerró en el punto más bajo | Vela bajista que terminó con fuerza vendedora |

Una regla rápida para recordarlo:

- Las flechas **de arriba** (roja y naranja) significan que la vela no tiene mecha superior.
- Las flechas **de abajo** (verde y azul) significan que la vela no tiene mecha inferior.

A veces una vela tiene **dos flechas**. Por ejemplo, roja arriba y azul abajo: abrió en el máximo y cerró en el mínimo, así que es una vela bajista sin ninguna mecha (marubozu completa).

---

## 2. ¿Por qué razón, en la formación de una vela, se dan esos casos?

> *"Investiga no inventes nada porque razón sobre la formación de una vela se dan esos casos"* — 6 oct, 11:58

### 2.1 Cómo se forma una vela en MetaTrader (dato documentado)

Según la documentación oficial de MetaTrader 5:

- En símbolos OTC, como XAUUSD en IC Markets, **las velas de 1 minuto se construyen con el precio Bid**. Los instrumentos de bolsa usan el precio Last.
- La plataforma **solo guarda velas de 1 minuto**. Las de M5, H1, etc. se construyen a partir de ellas.
- Cada vela registra 4 precios: **Open** (el inicio), **High** y **Low** (el máximo y el mínimo de ese minuto) y **Close** (el final). También registra el volumen de ticks.

Además, en el foro oficial de MQL5 explican que **una vela nueva solo nace cuando llega el primer tick de ese minuto**. Ese primer tick es la apertura.

Por eso:

- **Apertura = Máximo:** el primer precio del minuto fue el más alto y ningún tick posterior lo superó.
- **Apertura = Mínimo:** el primer precio fue el más bajo y nadie lo perforó después.
- **Cierre = Máximo:** el último tick del minuto fue el más alto de todos.
- **Cierre = Mínimo:** el último tick fue el más bajo de todos.

### 2.2 Su nombre en el análisis de velas (dato documentado)

A estas velas se les llama **marubozu**, que en japonés significa "calvo" o "afeitado", porque no tienen mecha. Las referencias las dividen en tres tipos:

- **Marubozu completo:** sin mecha en ninguno de los dos extremos.
  - Alcista: Apertura = Mínimo y Cierre = Máximo.
  - Bajista: Apertura = Máximo y Cierre = Mínimo.
- **Marubozu de apertura:** sin mecha en el lado de la apertura. Es lo que marcan las flechas roja y verde.
- **Marubozu de cierre:** sin mecha en el lado del cierre. Es lo que marcan las flechas naranja y azul.

La interpretación habitual es que un lado (compradores o vendedores) dominó desde el primer precio hasta el último.

### 2.3 Por qué pasan tan seguido en M1 (matemática documentada + aplicación propia)

Hay un resultado matemático, el **teorema de Sparre Andersen**. En un movimiento aleatorio simétrico, la probabilidad de no volver nunca por encima del punto de partida durante *n* pasos es exactamente C(2n,n)/4ⁿ, que se aproxima a **1/√(π·n)**. El valor es universal: no depende de cómo se distribuyan los saltos.

Aplicado a una vela (interpretación, suponiendo que los ticks se mueven al azar):

- Con **25 ticks** en el minuto, la probabilidad de que la apertura sea el máximo es de ≈ 11 %.
- Con **100 ticks** baja a ≈ 5,6 %.
- La probabilidad es la misma para cada uno de los 4 casos, así que en M1 es normal ver flechas en una parte importante de las velas. **No hace falta que haya una "causa" especial para que ocurra.**
- **Cuantos menos ticks tenga la vela, más frecuente es el caso.** Por eso deberían verse más flechas en horas tranquilas (sesión asiática, cambio de día) que en horas de mucho movimiento.
- En temporalidades altas (H1, H4) hay miles de ticks por vela y estos casos se vuelven raros.

Otros dos efectos (deducción, no comprobada con datos):

- El oro cotiza en saltos de 0,01. Que dos ticks repitan exactamente el mismo precio cuenta como "igual", y eso sube aún más la frecuencia.
- Como la vela se arma con el **Bid del bróker**, la misma vela de las 11:01 puede salir con flecha en IC Markets y sin flecha en otro bróker. Cada uno tiene su propio flujo de precios.

**Conclusión.** En M1, que la apertura o el cierre coincidan con un extremo es en buena parte **una consecuencia estadística normal** de cómo se arma la vela con pocos ticks. Por sí solo no es una señal fuerte.

> **Lo que vimos después.**
> - La predicción sobre las horas se confirmó con los datos de IC Markets: hay más marubozu a las 01–02 h y a las 23 h del servidor, las horas de poca liquidez, y menos a las 16–17 h, las de más liquidez (preguntas 14 y 15).
> - En cambio, que en temporalidades altas "tengan más significado" no se confirmó para la reacción del precio. Después del test, reaccionan igual que una vela normal (preguntas 10 y 11).

**Fuentes:**

- [MetaTrader 5 – Price Data](https://www.metatrader5.com/en/terminal/help/trading_advanced/price_data)
- [MetaTrader 5 – Tick generation](https://www.metatrader5.com/en/terminal/help/algotrading/tick_generation)
- [Foro MQL5 – detección de nueva vela con el primer tick](https://www.mql5.com/en/forum/39816/1310279)
- [What tick volume actually is in MetaTrader 5](https://www.mql5.com/en/blogs/post/774938)
- [LuxAlgo – Marubozu](https://www.luxalgo.com/library/concept/marubozu/)
- [Capital.com – Marubozu candle](https://capital.com/en-gb/learn/technical-analysis/marubozu-candle)
- [Majumdar – Universal first-passage properties of discrete-time random walks (Sparre Andersen)](https://arxiv.org/pdf/0912.2586)

---

## 3. ¿Qué son los ticks?

> *"…explícame más qué son los ticks"* — 6 oct, 12:03

Un **tick** es **cada actualización de precio que envía el bróker**. Cada vez que cambia el precio de compra (Bid) o el de venta (Ask), llega un tick nuevo a MetaTrader.

**Lo que dicen las fuentes:**

- Cada tick lleva marcas que indican qué cambió: el Bid, el Ask, el último precio negociado o el volumen.
- En forex y CFDs (como XAUUSD en IC Markets), el **"volumen" que se ve en MetaTrader es volumen de ticks**: cuántas actualizaciones llegaron mientras se formaba la vela.
- El volumen de ticks **no es volumen real**. No cuenta lotes ni dinero negociado, solo cuántas veces cambió la cotización. El volumen real (operaciones ejecutadas) solo existe en instrumentos de bolsa.
- **No mide cuánto se movió el precio:** 10 cambios de 1 punto cada uno dan 10 ticks, y 1 solo salto de 10 puntos da 1 tick.

**Ejemplo.** La vela de las 11:01 recibe estos ticks (Bid):

```
11:01:00.2  →  2650.40   ← primer tick = Apertura
11:01:03.8  →  2650.35
11:01:15.1  →  2650.20   ← el más bajo = Mínimo
11:01:41.6  →  2650.28
11:01:59.7  →  2650.31   ← último tick = Cierre
```

Ningún tick posterior superó 2650.40, así que **Apertura = Máximo**: flecha roja. El volumen de ticks de esa vela sería 5.

**Detalle técnico (deducción a partir de la documentación).** Las velas se dibujan solo con el **Bid**, pero el volumen de ticks también cuenta los cambios que fueron solo del **Ask**. Por eso el número de movimientos reales del Bid puede ser menor que el volumen de ticks que se ve.

**Fuentes:**

- [MetaTrader 5 – Price Data](https://www.metatrader5.com/en/terminal/help/trading_advanced/price_data)
- [MetaTrader 5 – Volume indicators](https://www.metatrader5.com/en/terminal/help/indicators/volume_indicators)
- [MetaTrader 5 Build 1200 – Tick history (marcas de cada tick)](https://www.metatrader5.com/en/releasenotes/terminal/1200)
- [What tick volume actually is in MetaTrader 5](https://www.mql5.com/en/blogs/post/774938)

---

## 4. ¿El precio de la vela no es el precio al que compraron?

> *"No termino de entender cuando dices cuántas veces cambió la cotización. Eso me interesa entender para comprender la formación de la vela por medio de ticks, porque yo asumía que ese precio es el que habían comprado y razón por la que la vela sube"* — 6 oct, 12:15 aprox.

Es la confusión más común, y en forex y CFDs como XAUUSD **no funciona así**. El precio que se ve en la vela **no es el precio al que alguien compró**. Es el precio al que **te ofrecen** comprar o vender en ese momento.

### 4.1 Cotización (oferta) vs. operación (transacción)

Piensa en una **casa de cambio** con su pizarra:

```
         COMPRAMOS (Bid)   VENDEMOS (Ask)
Dólar        3.70              3.75
```

- Esa pizarra es una **cotización**: el precio que ellos **ofrecen**. Que diga 3.70 no significa que alguien acabe de cambiar dólares a 3.70.
- Si el cajero borra 3.70 y escribe 3.71, eso es **un tick**: la cotización **cambió**, aunque quizá nadie haya cambiado un solo dólar en ese momento.
- Si cambian 10 veces la pizarra en un minuto, son **10 ticks**, haya habido 0 clientes o 50.

**Eso es lo que significa "cuántas veces cambió la cotización".**

### 4.2 Cómo aplica a XAUUSD en IC Markets (dato documentado)

- IC Markets dice que **obtiene sus precios de proveedores de liquidez externos** (bancos y otras entidades) conectados en una red ECN. Esos proveedores **ponen los precios de compra y de venta** (Bid y Ask), e IC Markets los pasa al cliente.
- Cada vez que esos precios cambian, a MetaTrader llega **un tick**. Cada tick lleva marcas de **qué cambió**: el Bid, el Ask, el último precio negociado o el volumen.
- En símbolos OTC, **la vela se dibuja con el Bid**, es decir, con el precio de la pizarra, no con precios de operaciones.
- En forex y CFDs, MetaTrader solo da **volumen de ticks**. El volumen real **solo existe en instrumentos de bolsa**, donde las velas se construyen con el precio "Last", el de la última operación ejecutada.

| | En bolsa (acciones, futuros) | En XAUUSD de IC Markets |
|---|---|---|
| Con qué se dibuja la vela | Precio de la **última operación** (Last) | **Bid**: precio ofrecido |
| Qué es el "volumen" | Operaciones / contratos reales | **Número de cambios de cotización** |
| ¿El precio = alguien compró ahí? | Sí | **No necesariamente** |

### 4.3 Entonces, ¿por qué sube la vela?

Esta parte es la explicación general de cómo funcionan estos mercados, no algo que diga la documentación de IC Markets.

La vela sube porque **los proveedores de liquidez suben sus precios**, en reacción a lo que pasa en el mercado:

- Cuando hay **muchas órdenes de compra**, se "comen" las ofertas de venta más baratas y las siguientes son más caras. Los proveedores ajustan su Bid y su Ask hacia arriba.
- También ajustan sus precios por lo que ocurre en **otros mercados** (por ejemplo, el oro en otros centros de negociación), por noticias, etc.

Así que **la compra sí está detrás de la subida**, pero de forma **indirecta**. No se ven las operaciones, solo **cómo se mueve la pizarra** como consecuencia de ellas. Tampoco se ve cuánto se compró, porque el volumen de ticks no lo mide.

### 4.4 El ejemplo de la vela con esta idea

```
11:01:00.2  Bid 2650.40   ← primer cambio de pizarra del minuto = Apertura
11:01:03.8  Bid 2650.35   ← la pizarra bajó
11:01:15.1  Bid 2650.20   ← punto más bajo de la pizarra = Mínimo
11:01:41.6  Bid 2650.28
11:01:59.7  Bid 2650.31   ← último cambio de pizarra del minuto = Cierre
```

"Apertura = Máximo" **no** significa "el primero que compró pagó lo más caro". Significa **"el primer precio ofrecido del minuto fue el más alto, y en ningún cambio posterior la pizarra volvió a subir por encima de él"**.

**Fuentes:**

- [IC Markets – Centro de ayuda / FAQ (precios de proveedores de liquidez, modelo ECN)](https://icmarkets.com/client-area/faq)
- [IC Markets – Help centre](https://www.icmarkets.com/global/ko/help-resources/help-centre)
- [Compare Forex Brokers – IC Markets Raw Spread vs Standard](https://www.compareforexbrokers.com/reviews/ic-markets-review/raw-spread-vs-standard-account/)
- [MetaTrader 5 – Price Data (OTC con Bid, bolsa con Last)](https://www.metatrader5.com/en/terminal/help/trading_advanced/price_data)
- [MetaTrader 5 – Volume indicators (volumen de ticks vs real)](https://www.metatrader5.com/en/terminal/help/indicators/volume_indicators)
- [MetaTrader 5 Build 1200 – marcas de cada tick](https://www.metatrader5.com/en/releasenotes/terminal/1200)

---

## 5. ¿Me lo puedes explicar con velas, de forma interactiva?

> *"Podrías explicármelo con velas porfa y si es posible de forma interactiva"* — 6 oct, mediodía

Se creó un **simulador interactivo**: https://claude.ai/artifact/RZ9BtMRSm2fdSZzfzgMMij (también en `paginas/simulador-velas-ticks.html`).

**Qué tiene:**

- **La pizarra del proveedor:** precios de venta (Ask) y de compra (Bid), con cuántos lotes ofrece en cada precio.
- **La vela de 1 minuto:** se dibuja **solo con el Bid**, igual que en MetaTrader, con las mismas flechas de colores que el indicador.
- **Tres contadores:** ticks totales, ticks que movieron el Bid (los que dibujan la vela) y operaciones ejecutadas. Este último es justo lo que MetaTrader no muestra.
- **Registro tick por tick:** la hora, el Bid, el Ask, qué cambió y por qué.

**La idea principal que se ve:**

- Una **compra** no mueve la vela directamente. Primero se agotan las ofertas del **Ask**, y esos ticks no mueven la vela. Después el proveedor sube su **Bid**, y solo entonces se mueve la vela.
- Una **venta** sí la mueve en el acto, porque golpea directamente el Bid, que es el lado con el que se dibuja la vela.
- Puede haber **operación sin tick** (alguien compra y la vela no se mueve) y **tick sin operación** (la vela salta sin que nadie opere, por ejemplo por una noticia).

Es un **modelo simplificado con números inventados**, no datos reales de IC Markets. Lo documentado es que la vela se dibuja con el Bid, que el volumen es volumen de ticks y que IC Markets toma sus precios de proveedores de liquidez. La forma exacta en que el proveedor cambia sus precios está simplificada para ilustrar el mecanismo.

---

# Parte 2. Los participantes y el desequilibrio

## 6. ¿Qué persigue cada participante y por qué el precio vuelve a una marubozu?

> *"Podrías agregar estos 4 escenarios al simulador y explicar un poco más qué está pensando cada quien, qué están persiguiendo los proveedores de liquidez, qué están persiguiendo los fondos, qué deberían perseguir los retailers, y con base a eso explicar mi observación: el precio tiende a regresar donde hay una vela marubozu. Quiero entender a nivel de formación de velas y a nivel técnico el porqué."*
> *"Complementando mi observación, el precio tiende a regresar donde hay una vela marubozu que no fue testeada nuevamente."* — 6 oct, mediodía

### 6.1 Las 4 flechas, tick a tick (en el simulador)

- 🔴 **Apertura = Máximo:** las ventas dominan desde el primer tick y el rebote no llega a la apertura.
- 🟠 **Cierre = Máximo:** el minuto empieza bajando y al final las compras llevan el Bid a su punto más alto.
- 🟢 **Apertura = Mínimo:** las compras dominan desde el primer tick y el retroceso no perfora la apertura.
- 🔵 **Cierre = Mínimo:** al final del minuto las ventas llevan el Bid a su punto más bajo.

**Escenario «Un fondo compra con prisa».** Un fondo compra 24 lotes en un minuto y se forma una marubozu. El **inventario del proveedor** queda en −24 lotes. En el minuto siguiente el proveedor baja sus precios para recomprar, y el precio vuelve a entrar en el cuerpo de la marubozu.

### 6.2 Qué persigue cada participante

- **Proveedor de liquidez:** quiere ganar el spread sin quedarse con una posición. Si el flujo lo deja vendido o comprado, mueve sus precios para equilibrarse. Si sospecha que le operan con información, amplía el spread.
- **Fondos e institucionales:** quieren ejecutar órdenes grandes al menor costo. Con prisa, aceptan pagar el impacto, y eso produce velas de cuerpo grande.
- **Retail:** paga el spread y no ve la pizarra ni las operaciones. Lo razonable es controlar costos, no entrar cuando el impacto temporal está en su máximo y comprobar con datos antes de arriesgar. Es orientación general, no una recomendación de inversión.

### 6.3 La observación: el precio vuelve a la marubozu **no testeada**

Lo que está respaldado por investigación:

1. **Parte del impacto es temporal.** Cuando una orden grande termina, el precio se relaja desde su pico y una parte del movimiento se deshace.
2. **El proveedor ajusta sus precios según su inventario.** Tras una marubozu alcista quedó vendido, así que baja sus precios para recomprar, y eso empuja el Bid de vuelta hacia la vela.

Por qué podría importar que **no esté testeada** (interpretación): ese «trabajo pendiente» se resuelve **la primera vez** que el precio vuelve. El proveedor recompra y la parte temporal se deshace. Después de ese primer test queda menos motivo para volver.

Las advertencias:

- Matemáticamente, el precio **vuelve casi siempre** a cualquier nivel cercano (teorema de Pólya). Además, «no testeada» deja de serlo justo cuando el precio vuelve, así que con el tiempo casi todas acaban testeadas. Volver, por sí solo, no prueba nada.
- La teoría de «desequilibrio» o «hueco de valor justo» que usan muchos traders no se encontró validada en estudios.
- El rebote entre Bid y Ask (Roll) **no aplica**, porque la vela se dibuja solo con el Bid.

**La forma de saberlo es medirlo:** cuántas velas tarda el precio en testear una marubozu, comparado con velas normales.

> **Lo que vimos después:** al medirlo (preguntas 10 a 12), los niveles sin mecha **tardan más** en testearse que los normales. Pero **después del test** el precio reacciona igual que en un nivel normal (~50 %).

Las fuentes de esta parte están al final de la página del simulador.

---

## 7. ¿Importa cuándo vuelve el precio?

> *"No la considero relevante porque son de las cosas que no podemos controlar del mercado, lo cual sería el cuándo; solo quedaría como una zona de precio a observar."* — 6 oct, mediodía

Tiene sentido. Cuándo vuelve el precio no se controla, así que la marubozu no testeada sirve como **zona de precio a vigilar**, no como un aviso de cuándo va a pasar algo.

De ahí salieron las líneas del indicador. Cada nivel no testeado se dibuja hacia la derecha mientras el precio no lo toque, y se marca como testeado cuando vuelve.

---

## 8. ¿Qué persigue cada participante en cada paso, y cómo encaja la idea de desequilibrio?

> *"Cada vez que presione un botón del simulador es donde quiero que me agregues la explicación de qué persigue cada uno de los interesados; agrega otros si no los he incluido, y de igual manera las observaciones que te comento."* — 6 oct, 12:48
> *"Estos son ejemplos que han sido testeadas, porque hay otras velas que llegaron a esa zona, y sí lo interpreto como una especie de imbalance; por lo mismo el precio lo vuelve a buscar y testeando balancea el precio."*

**En el simulador.** Cada botón y cada paso de los escenarios actualizan el panel **«Qué persigue cada participante en este paso»**. Por ejemplo:

- Al comprar, el proveedor dice cuántos lotes lleva vendidos y por qué sube el precio.
- En la noticia, el arbitrajista explica por qué el salto es instantáneo.
- Al ampliarse el spread, el retail lee que es un mal momento para entrar.

**Participantes añadidos:**

- **Bróker (IC Markets):** cobra comisión o margen por cada operación, así que le interesa el volumen y no la dirección (dato de IC Markets).
- **Arbitrajistas y alta frecuencia:** igualan el precio entre mercados.
- **Coberturistas:** mineras o empresas que operan para cubrir un riesgo de su negocio, no por la vela del minuto.

**La interpretación como desequilibrio encaja con el modelo:**

- La marubozu deja un **desequilibrio**: el proveedor quedó con una posición que no quería y una parte del impacto fue temporal.
- Cuando el precio vuelve a la zona, el proveedor recompra y la parte temporal se deshace. Eso es el **balanceo**.
- Una vez testeada, ese motivo ya se resolvió en gran parte. Por eso tiene sentido fijarse solo en las no testeadas.

---

## 9. Mi ejemplo: una marubozu no testeada y otra que sí se testeó

> *"Aquí te dejo el ejemplo completo. La que está marcada por la flecha verde dentro del rectángulo no fue testeada; el mercado siguió subiendo y formó otra, que es la que está en el círculo, y ahí te muestro cómo fue testeada más adelante. Es decir, todavía hay una con desequilibrio más abajo, pero no sabemos cuándo se va a cerrar."* — 6 oct, 12:53

**Cómo se interpretó:**

- **El nivel:** cada vela con flecha deja como nivel su **extremo sin mecha**. En la flecha verde, ese nivel es su apertura, que también es su mínimo.
- **Testeado:** el nivel pasa a testeado cuando una vela posterior vuelve a tocarlo. Mientras eso no ocurra, queda como **desequilibrio pendiente**, sin hora.

**El ejemplo, paso a paso** (escenario «Tu ejemplo: dos desequilibrios» del simulador):

1. **Vela A (rectángulo):** Apertura = Mínimo. Su apertura queda como nivel.
2. El mercado sigue subiendo sin volver a A.
3. **Vela B (círculo):** otra Apertura = Mínimo, más arriba.
4. Las compras se agotan y el precio baja hasta tocar B, que queda **testeado**.
5. **A sigue pendiente** más abajo, y no sabemos cuándo se cerrará.

**Algo que salió de la formación de las velas:**

- **Los niveles de cierre** (flechas naranja y azul) quedan testeados **casi siempre en el acto**. La vela siguiente abre con el primer tick después del cierre, y ese tick está pegado al cierre anterior.
- **Los niveles de apertura** (flechas verde y roja) **quedan atrás** cuando el precio se aleja. Esos sí pueden pasar mucho tiempo sin que otra vela los toque.

Por eso los desequilibrios que se marcan son de **apertura**, y por eso el análisis siguiente usa solo las flechas verde y roja.

---

# Parte 3. Estadísticas con datos de IC Markets

## 10. ¿Cuántas se forman, cuántas se testean, en cuánto tiempo, y hay jerarquía entre temporalidades?

> *"Tomando en cuenta solo escenarios de flecha verde y roja, ¿podrías con la data disponible de IC Markets sacar estadísticas respecto a cuántas se formaron, cuántas fueron testeadas, en cuánto tiempo fueron testeadas, y si hay con base a estadísticas alguna especie de jerarquía, por ejemplo el nivel de reacción cuando son de temporalidades más altas a 1 minuto?"* — 6 oct, 13:08

Se midió con el script `EstadisticasNiveles.mq5` en el MetaTrader del usuario, con datos reales de IC Markets.

- **«Respetado»:** 30 minutos después del test, el precio quedó del lado del rebote.
- **Control:** aperturas normales, con mecha, medidas con la misma regla.

| TF | Niveles formados | Testeados | Mediana hasta el test | Respetado 30 min después | Control (con mecha) |
|---|---|---|---|---|---|
| M1 | 5.219 | 99,1% | 3 velas (3 min) | 49,5% | 49,6% |
| M5 | 2.342 | 99,0% | 3 velas (15 min) | 50,1% | 50,1% |
| M15 | 2.010 | 98,8% | 3 velas (45 min) | 47,4% | 50,1% |
| M30 | 2.101 | 98,3% | 3 velas (1,5 h) | 49,4% | 49,9% |
| H1 | 1.661 | 98,3% | 3 velas (3 h) | 52,6% | 50,7% |
| H4 | 511 | 97,7% | 2 velas (8 h) | 64,0% (25 casos) | 50,7% |
| D1 | 189 | 95,8% | 2 velas (2 días) | 1 caso, no evaluable | 53,5% |

**Qué significa:**

1. **Casi todas acaban testeadas (~99%), pero los niveles normales también.** Que el precio vuelva a un nivel cercano es lo esperable. Por sí solo no demuestra un desequilibrio.
2. **Los niveles sin mecha sí tienen algo distinto: tardan más en testearse.** Solo ~30% se testea en la vela siguiente, frente a ~50% de los normales. Es por cómo se forma la vela: el nivel queda en el extremo, más lejos del cierre.
3. **De M1 a H1, la reacción tras el test es como lanzar una moneda (~50%),** igual que en los niveles normales.
4. **Que el nivel tarde más en testearse no mejora la reacción.** El respetado sigue rondando el 50 % se agrupe como se agrupe.
5. **En H4 apareció una pista de jerarquía:** 64% respetado. Pero eran solo 25 casos, y con tan pocos el valor real podría estar entre el 44% y el 80%.

> **Lo que vimos después:** el 64 % de H4 **no se confirmó** al medir con más historial (pregunta 11).

---

## 11. ¿Se confirma la jerarquía con más historial (H1)?

> *"Te comparto las de H1"* — 6 oct, 13:55

Se midió la reacción con velas H1, que tienen historial desde 2018 (y antes), en lugar de M1.

**El 64% de H4 no se confirma.** Con 499 tests, H4 da 53,7% de respetado frente a 50,8% de un nivel normal, una diferencia que puede ser azar.

Para que la tendencia alcista del oro no distorsione la comparación, cada flecha se comparó con el control de su misma dirección:

| TF | Verde (casos) | Control alcista | Roja (casos) | Control bajista |
|---|---|---|---|---|
| H1 | 52,7% (807) | 52,8% | 47,1% (826) | 49,1% |
| H4 | 57,7% (319) | 52,9% | 46,7% (180) | 48,5% |
| D1 | 60,9% (133) | 55,3% | 39,6% (48) | 47,1% |
| W1 | 41,7% (12) | 54,8% | 33,3% (6) | 48,9% |

- **Ninguna temporalidad, por separado, supera con claridad a su control.**
- **Las rojas no superan a su control en ninguna temporalidad.**
- **Las verdes de H4 y D1 son el único indicio de jerarquía:** juntas dan 58,6% frente a 53,6% (452 casos). Es débil por dos motivos:
  - Esa combinación se eligió después de ver los datos.
  - La ventaja viene sobre todo de antes de 2018. De 2018 a 2026, H4 da 55% frente a 53%, y en D1 solo hay 14 casos.
- **El tiempo que el nivel estuvo pendiente no mejora la reacción.**

**En resumen.** Los niveles sin mecha **sí se distinguen en cuándo se testean**: tardan más que un nivel normal. Pero **no en cómo reacciona el precio** después del test. La pista de las verdes de H4 y D1 solo se puede comprobar limpiamente en otro activo o con datos futuros.

---

## 12. ¿Qué pasó con las velas que no fueron testeadas?

> *"¿Podrías estadísticamente explicar qué pasó con las velas que no fueron testeadas?"* — 6 oct, 14:00

### 12.1 Son muy pocas

| TF | Flechas sin testear | % del total | Control (con mecha) |
|---|---|---|---|
| M1 | 46 de 5.219 | 0,9% | 0,6% |
| H1 | 28 de 1.661 | 1,7% | 1,1% |
| H4 | 12 de 511 | 2,3% | 1,9% |
| D1 | 8 de 189 | 4,2% | 3,3% |
| W1 | 3 de 21 | 14% | 7,6% |

Cuanto mayor es la temporalidad, más niveles quedan pendientes: una vela de D1 o W1 cubre mucho más precio y hay menos velas posteriores para tocarla.

### 12.2 No son recientes: el precio se fue lejos y no volvió

| TF | Distancia típica al precio actual (≈4.176) |
|---|---|
| M1 | 3,9% |
| M15 | 24% |
| H1 | 52% |
| H4 | 83% |
| D1 | 88% (niveles de 2005–2008, cuando el oro estaba en 500–750) |

### 12.3 Su dirección la decide la tendencia, no la flecha

- **En H4, D1 y W1 todos los pendientes son verdes:** mínimos que quedaron por debajo, porque el oro lleva más de 20 años subiendo.
- **En M1 y M5 la mayoría son rojos:** máximos que quedaron por encima, porque en ese periodo (agosto a octubre de 2026) el oro bajó de ~4.390 a ~4.176.
- **Las velas normales muestran exactamente el mismo reparto.** Es la tendencia dejando niveles atrás.

### 12.4 Siguen la ley del camino aleatorio

| Velas transcurridas | Flechas sin testear | Control | Azar puro 1/√(πN) |
|---|---|---|---|
| 1 | 69,7% | 49,8% | 56,4% |
| 5 | 39,7% | 26,1% | 25,2% |
| 20 | 20,8% | 13,6% | 12,6% |
| 100 | 9,2% | 6,1% | 5,6% |
| 500 | 4,0% | 2,8% | 2,5% |
| 1000 | 2,9% | 2,0% | 1,8% |

- **Las velas normales siguen casi exactamente la fórmula del azar.** Es la misma ley de Sparre Andersen de la pregunta 2.
- **Las flechas siguen la misma curva, pero ~1,5 veces más arriba,** porque su nivel nace en el extremo de la vela, más lejos del cierre.
- **Si un nivel lleva N velas sin testear, la probabilidad de que lo testeen en las siguientes N velas es siempre de ~29%.** Pasa igual de 100 a 200 velas que de 500 a 1000.
- **Por tanto, el tiempo no crea más "presión" por volver.** Cuanto más tiempo lleva pendiente, más tiempo se espera que siga así. Un desequilibrio antiguo no atrae más al precio que uno reciente.

**Conclusión.** Las velas no testeadas son la **cola normal de un movimiento aleatorio con tendencia**. Encaja con la idea de tratarlas como **zonas a observar sin hora**, con un matiz: cuanto más antigua es la zona, menos probable es que el precio vuelva pronto.

---

## 13. ¿Cómo se comportan por sesión?

> *"Ampliemos un poco más el análisis y analiza su comportamiento por sesión, por ejemplo si el desequilibrio se generó en NY, si se cerró en la misma sesión, si no en qué sesión se cerró si es que se cerró, cuántas veces sucede eso, etc."* — 6 oct, 14:05

Sesiones en hora del servidor de IC Markets (hora de Nueva York + 7). Datos de las flechas verde y roja de M1 a H1.

| Sesión | Hora del servidor |
|---|---|
| Asia | 01–10 h |
| Londres | 10–15 h |
| Londres+NY (solapamiento) | 15–19 h |
| NY tarde | 19–24 h |

### 13.1 ¿Se cierra en la misma sesión?

| Nace en | M5 | H1 | H1: se cierra en la sesión siguiente |
|---|---|---|---|
| Asia | 83% (control 87%) | 57% | 17% |
| Londres | 76% (85%) | 35% | 35% |
| Londres+NY | 71% (81%) | 22% | 21% |
| NY tarde | 69% (82%) | 23% | 50% |

- **En temporalidades bajas, la mayoría se cierra en la misma sesión.** Las flechas siempre un poco menos que las velas normales.
- **Asia sale más alta en parte porque dura 9 horas.** Midiendo cuánto se cierra en los 60 minutos siguientes, Asia y Londres quedan iguales (≈74% en M5). NY tarde es la más lenta (63%), porque su última hora choca con el corte diario.
- **Si la flecha nace en la última hora de su sesión, casi nunca se cierra en ella:** 30% en M15, frente a 72% del resto.

### 13.2 Si no se cerró en su sesión, ¿en cuál se cerró?

Casi siempre en **la siguiente**:

- Asia → Londres (47%) o Londres+NY (32%)
- Londres → Londres+NY (74%)
- Londres+NY → NY tarde (43%) o la Asia siguiente (31%)
- **NY tarde → Asia del día siguiente (85%)**

### 13.3 ¿Cuáles se quedan sin cerrar?

| Nace en | Flechas sin testear | Velas normales sin testear |
|---|---|---|
| Asia | 0,75% | 0,87% |
| Londres | 0,96% | 0,91% |
| **Londres+NY** | **2,11%** | 1,29% |
| **NY tarde** | **1,61%** | 0,71% |

En Asia y Londres las flechas se comportan igual que las velas normales. En las sesiones de **Nueva York** quedan pendientes **unas 2 veces más**, una diferencia demasiado grande para ser azar.

Interpretación: en NY salen los datos económicos de EE. UU. Un movimiento que trae información nueva tiene impacto permanente y no se deshace. Los números absolutos son pequeños (41 y 48 niveles), así que es una pista, no una regla.

### 13.4 Otros datos

- **La reacción tras el test no cambia por sesión:** ronda el 49–52% en todas, igual que en las velas normales.

**Limitaciones:**

- Las horas de las sesiones son aproximadas: Londres cambia de horario de verano en fechas distintas a EE. UU.
- Solo se analizó de M1 a H1.
- Los datos de M1 cubren 7 semanas; M15 desde 2024 y H1 desde 2018.

---

## 14. ¿Hay sesiones en las que se forman más marubozu?

> *"¿Hay sesiones en las que se forman más velas tipo marubozu?"* — 6 oct, 14:11

Sí. **Se forman más en Asia y al final de NY, y menos durante el solapamiento Londres+NY.** Solo se midieron las flechas verde y roja (sin mecha en la apertura).

| Sesión (hora del servidor) | M1 | M5 | M15 | H1 |
|---|---|---|---|---|
| **Asia** (01–10 h) | **11,8%** | 4,9% | 4,2% | **4,0%** |
| Londres (10–15 h) | 10,3% | 4,5% | 3,7% | 2,7% |
| **Londres+NY** (15–19 h) | **8,1%** | **4,0%** | **3,5%** | 2,8% |
| **NY tarde** (19–24 h) | 10,4% | **5,2%** | **4,4%** | 3,2% |

| Hora del servidor | M1 | H1 | Qué pasa a esa hora |
|---|---|---|---|
| **01–02 h** | **15–17%** | **6–7%** | Reapertura tras el corte diario, poca liquidez |
| 16–18 h | 7–8% | ~2% | Solapamiento Londres+NY, máxima liquidez |
| 17 h (solo H1) | — | **5,2%** | Pico dentro de NY |
| **23 h** | **14%** | **5%** | Última hora antes del corte diario |

**Por qué:**

1. **Liquidez (ticks).** Con menos ticks en la vela es más probable que la apertura quede en un extremo: es la ley de Sparre Andersen de la pregunta 2. Este es el efecto principal.
2. **Reapertura de las 01 h.** El primer tick después del corte diario puede llegar con hueco. Si el precio sigue en esa dirección, la vela abre en su mínimo o su máximo.
3. **Pico de las 17 h en H1** (interpretación, no comprobada con datos de noticias). Esa vela empieza poco después de la apertura de la bolsa de Nueva York (16:30 h servidor) y coincide con varios datos económicos de EE. UU.

**Conclusión.** Las marubozu aparecen más cuando **hay poca liquidez**, no por un mayor interés del mercado. Las de Asia se comportan como velas normales; las que dejan desequilibrios más duraderos son las que **nacen en NY**, aunque se formen menos.

---

## 15. ¿En qué franjas horarias aparecen menos?

> *"¿Cuáles son los rangos horarios por sesión en las que menos aparecen las marubozu?"* — 6 oct, 14:13

En hora del servidor (entre paréntesis, hora de Nueva York = servidor − 7):

| Sesión | Franja con menos marubozu | Hora NY | % de velas que son flecha (M1 / M5 / M15 / H1) | Qué tan claro es |
|---|---|---|---|---|
| **Asia** (01–10 h) | **04:00–06:00** | 21:00–23:00 | 8,6–11,7 / 4,1–4,3 / 2,9–3,6 / 2,8–3,7 | Claro |
| | 08:00–10:00 (secundaria) | 01:00–03:00 | 9,9–11,6 / 4,1–5,4 / 3,3–3,4 / 2,2–3,6 | Moderado |
| **Londres** (10–15 h) | **11:00–14:00** | 04:00–07:00 | 9,8–10,6 / 4,5–4,6 / 3,1–4,2 / 1,8–2,8 | Débil |
| **Londres+NY** (15–19 h) | **16:00–19:00** | 09:00–12:00 | 7,0–8,3 / 3,3–4,0 / 2,9–3,8 / 1,9–2,1 | **Muy claro: mínimo del día** |
| **NY tarde** (19–24 h) | **19:00–21:00** | 12:00–14:00 | 8,4–10,5 / 4,0–4,6 / 3,4–4,6 / 2,5–2,8 | Claro |

- **El mínimo del día está entre las 16:00 y las 17:00 h del servidor.** En M1 solo el 7% de las velas son flecha, y en H1 el 1,9%, frente al 15–17% y el 6–7% de las 01–02 h.
- **La excepción es la vela H1 de las 17:00 h,** que sube al 5,2%.
- **El patrón general:** las marubozu escasean cuando **más liquidez hay** y abundan en la **reapertura (01–02 h)** y **antes del corte diario (23 h)**.

---

## 16. ¿Cuáles son esas franjas en hora de El Salvador?

> *"Entonces hora El Salvador, ¿cuáles serían esos rangos?"* — 6 oct, 14:14

El Salvador está en UTC-6 todo el año, sin horario de verano. El servidor de IC Markets sí cambia de hora con Estados Unidos:

- **De mediados de marzo a principios de noviembre:** hora de El Salvador = hora del servidor − **9 h**.
- **De noviembre a marzo:** hora de El Salvador = hora del servidor − **8 h**.

**Franjas con menos marubozu:**

| Sesión | Hora del servidor | El Salvador: marzo a noviembre | El Salvador: noviembre a marzo |
|---|---|---|---|
| **Asia** | 04:00–06:00 | **19:00–21:00** (noche anterior) | 20:00–22:00 |
| Asia (secundaria) | 08:00–10:00 | 23:00–01:00 | 00:00–02:00 |
| **Londres** (diferencia débil) | 11:00–14:00 | **02:00–05:00** | 03:00–06:00 |
| **Londres+NY** | 16:00–19:00 | **07:00–10:00** | 08:00–11:00 |
| ↳ **Mínimo del día** | 16:00–17:00 | **07:00–08:00** | 08:00–09:00 |
| ↳ Excepción (vela H1) | 17:00–18:00 | 08:00–09:00 | 09:00–10:00 |
| **NY tarde** | 19:00–21:00 | **10:00–12:00** | 11:00–13:00 |

**Franjas con más marubozu:**

| Momento | Hora del servidor | El Salvador: marzo a noviembre | El Salvador: noviembre a marzo |
|---|---|---|---|
| Reapertura tras el corte diario | 01:00–03:00 | 16:00–18:00 | 17:00–19:00 |
| Antes del corte diario | 23:00–24:00 | 14:00–15:00 | 15:00–16:00 |

El cambio de horario de EE. UU. de 2026 es el **1 de noviembre**. A partir de esa fecha se usa la última columna.

---

# Parte 4. De los datos a la operativa

## 17. ¿Qué reglas establecerías en un fondo retail para scalping e intradía?

> *"Con lo que tenemos hasta ahorita, ¿cuáles serían las reglas que establecerías en un fondo retail para operativa scalping e intraday?"* — 6 oct, 14:17
> *"No solo como sugerencia…"* — 6 oct, 14:26

Lo más importante: **con lo medido no hay una ventaja demostrada para operar estos niveles.** El precio vuelve casi siempre, pero después del test reacciona como una moneda al aire (~50%). Por eso las reglas sirven sobre todo para **no perder dinero por suposiciones falsas** y para **comprobar con método** las pocas pistas que aparecieron. Es un marco general basado en los datos, no asesoría de inversión.

**Lo que los datos permiten afirmar:**

| Hallazgo | Fiabilidad |
|---|---|
| ~99% de los niveles se testean, en una mediana de 3 velas | Alta, pero igual que en velas normales |
| Después del test, el precio queda del lado del rebote ~50% de las veces | Alta: **no hay ventaja** |
| Los niveles que llevan más tiempo pendientes no reaccionan mejor | Alta |
| Las flechas que nacen en NY quedan sin testear el doble de veces | Media (41–48 casos) |
| Las verdes de H4 y D1 se respetan un poco más (58,6% frente a 53,6%) | **Baja**: no confirmado y peor desde 2018 |
| Más marubozu en horas de poca liquidez (01–03 y 23 h servidor) | Alta |

**Las reglas, en resumen:**

- **Lo que los datos prohíben:**
  - operar un nivel sin mecha solo por ser nivel;
  - apostar a que «el precio tiene que volver»;
  - aumentar el tamaño porque un nivel lleve mucho tiempo pendiente;
  - dar por hecho que un nivel nacido en NY se va a cerrar.
- **Ejecución y horario:** evitar las horas de poca liquidez y el corte diario, concentrar el scalping en las horas de más liquidez y tener cuidado con la apertura de NY y los datos de EE. UU.
- **Gestión de riesgo:**
  - 0,25 % por operación en scalping y 0,5 % en intradía;
  - 2 % de pérdida máxima diaria y 6 % mensual;
  - stop definido antes de entrar y que nunca se mueve en contra;
  - costos incluidos en cada cálculo.
- **Método:** toda hipótesis se prueba en datos que no se usaron para descubrirla, y pasa al menos 100 operaciones con tamaño mínimo antes del tamaño normal. Diario de operaciones obligatorio.

Las reglas quedaron como **obligatorias** en `REGLAMENTO.md`, redactadas con «debe / no debe». Incluyen roles del equipo, consecuencias por incumplir, revisiones y plantilla de diario.

> **Lo que vimos después:** al medir el spread (pregunta 19), el reglamento pasó a la **versión 1.1** y se ajustaron los horarios.

---

## 18. ¿Cómo medimos el spread?

> *"…y dime cómo medimos el spread"* — 6 oct, 14:26

- **Método exacto, con ticks.** Cada tick trae su Bid y su Ask.
  - Desde la ventana **Símbolos** (Ctrl+U), pestaña **Ticks**: se exporta un periodo y se calcula el spread por hora y por día. Para periodos largos el archivo es enorme, así que se usó el script `ResumenSpread.mq5`, que lee los ticks dentro de MetaTrader y guarda solo el resumen por día y por hora.
  - Se calcula la mediana, el valor que solo se supera el 10 % de las veces y el máximo.
- **Método rápido, con velas.** La pestaña **Barras** trae un valor de spread por vela, en puntos (1 punto = 0,01 en XAUUSD). La documentación no aclara si es el mínimo o un promedio de la vela, así que sirve para ver el patrón, pero los límites se fijan con los ticks.
- **En vivo:** en la **Observación de Mercado**, clic derecho → **Columnas → Spread**. Es el «spread al entrar» que se anota en el diario.

---

## 19. ¿Qué salió al medir el spread?

> Resultados de `OCE_Spread_XAUUSD.csv` — 6 oct, 15:02

Con 196 días de ticks, el spread típico del oro es **casi el mismo todo el día, 8–9 puntos (0,08–0,09 USD), de 02 a 22 h**. Solo la hora de las **23 h** es claramente cara.

| Hora servidor | El Salvador (mar–nov) | Spread típico | Percentil 90 | Días con picos (> 20 puntos) | Ticks por hora |
|---|---|---|---|---|---|
| 01 h (reapertura) | 16 h | 9 | 12 | 7,7% | ~10.600 |
| 02–14 h | 17–05 h | 8–9 | 10–12 | 0–2,6% | 11.000–29.000 |
| 15–16 h (datos y apertura de NY) | 06–07 h | 8,6 | 10 | **5–7%**, hasta 700 puntos | 27.000–46.000 |
| 17–22 h | 08–13 h | 8 | 10–11 | 0–1,5% | 19.000–49.000 |
| **23 h (antes del corte)** | **14 h** | **18** | **40** | **100%** | ~8.500 |

El percentil 90 es el valor que solo se supera el 10 % del tiempo. No hay diferencias entre días de la semana, y por meses solo febrero fue algo más alto.

**Cómo quedó el reglamento (v1.1):**

| Regla | Ahora |
|---|---|
| R6: sin scalping | **23:00–02:00** servidor (El Salvador 14:00–17:00) |
| R7: horario de scalping | **02:00–23:00**, con franja preferente **16:00–19:00** (El Salvador 07:00–10:00) |
| R8: noticias | Ventana de los **datos de EE. UU.: 15:25–15:45** y apertura de NY **16:25–16:35** servidor |
| R14: tope de spread | **18 puntos (0,18 USD)**, el doble del spread típico |
| R18 (nueva) | El costo total (spread + comisión) **no puede superar el 10 % del riesgo** |

**Sobre R18.** Supone 0,09 USD de spread y 7 USD de comisión por lote ida y vuelta (0,07 USD por onza). Así, cada entrada cuesta ~0,16 USD por onza, y para que ese costo no pase del 10 % del riesgo, **el stop tiene que estar al menos a 1,60 USD de la entrada**. **Pendiente:** confirmar la comisión real del oro en la cuenta.

---

## Resumen en una página

- **Qué es una marubozu en MT5:** una vela cuyo primer o último tick (Bid) fue el extremo del periodo. En M1 es muy frecuente por pura estadística (Sparre Andersen), sobre todo con pocos ticks.
- **El precio de la vela no es un precio de compra:** es la cotización Bid del proveedor de liquidez. Las compras mueven la vela de forma indirecta, a través de cómo el proveedor ajusta su pizarra.
- **La idea del desequilibrio** encaja con el impacto temporal y el inventario del proveedor. Los niveles útiles son los de **apertura** (verde y roja); los de cierre se testean casi en el acto.
- **Lo que confirman los datos:**
  - ~99 % de los niveles se testean;
  - tardan más que un nivel normal (mediana 3 velas);
  - los no testeados siguen la ley del azar con tendencia;
  - los nacidos en NY quedan pendientes el doble de veces;
  - hay más marubozu con poca liquidez.
- **Lo que no confirman:** que después del test el precio rebote más que en un nivel normal (~50 %), ni una jerarquía clara por temporalidad. La única pista, las verdes de H4/D1, es débil.
- **Uso práctico:** zonas a observar sin hora, con reglas de riesgo y costos obligatorias.
- **Pendiente:**
  - confirmar la comisión del oro;
  - probar la pista de las verdes de H4/D1 en otro activo;
  - definir una entrada y salida concretas y medirlas después de costos.
