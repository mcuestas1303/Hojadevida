# Manual · Niveles sin mecha

Herramientas para estudiar las velas cuya **apertura o cierre coincide con el máximo o el mínimo** (velas sin mecha en un extremo) y los niveles que dejan atrás.

Probado con datos de **XAUUSD en IC Markets (MetaTrader 5)**. Funciona con cualquier activo.

---

## 1. Qué hay en esta carpeta

```
niveles-sin-mecha/
├── MANUAL.md                         ← este manual
├── REGLAMENTO.md                     ← reglas obligatorias de operativa (scalping e intradía)
├── MT5/
│   ├── Indicators/
│   │   └── OpenCloseExtremos.mq5     ← indicador v1.40: flechas, panel de % y líneas de niveles
│   └── Scripts/
│       ├── EstadisticasNiveles.mq5   ← estadísticas, reacción medida en M1
│       ├── EstadisticasNivelesH1.mq5 ← estadísticas, reacción medida en H1
│       └── ResumenSpread.mq5         ← resumen del spread por día y hora a partir de los ticks
├── MT4/
│   └── Indicators/
│       └── OpenCloseExtremos.mq4     ← el mismo indicador para MetaTrader 4
├── paginas/
│   ├── simulador-velas-ticks.html        ← simulador interactivo de ticks y velas
│   └── estadisticas-niveles-xauusd.html  ← resultados con gráficos (XAUUSD, M1 y H1)
└── resultados/
    ├── XAUUSD_M1_2026-10-06.txt      ← informe original del script M1
    ├── XAUUSD_H1_2026-10-06.txt      ← informe original del script H1
    └── XAUUSD_spread_2026-01-02_2026-10-05.csv ← resumen del spread por día y hora
```

Las carpetas `MT5/Indicators` y `MT5/Scripts` tienen el mismo nombre que las de MetaTrader, para que sepas dónde copiar cada archivo.

**Páginas publicadas** (se abren en el navegador):
- Simulador: https://claude.ai/artifact/RZ9BtMRSm2fdSZzfzgMMij
- Resultados XAUUSD: https://claude.ai/artifact/T23ng7WxJWqwXA7gFUbfrD

---

## 2. Instalación en MetaTrader 5

1. En MetaTrader ve a **Archivo → Abrir carpeta de datos**.
2. Copia los archivos:
   - `OpenCloseExtremos.mq5` → **MQL5 → Indicators**
   - `EstadisticasNiveles.mq5` y `EstadisticasNivelesH1.mq5` → **MQL5 → Scripts**
3. En el panel **Navegador** (Ctrl+N), haz clic derecho en «Indicadores» y en «Scripts» y elige **Actualizar**.
4. Haz doble clic en cada archivo para abrirlo en MetaEditor y pulsa **F7** para compilar.
5. Arrastra el indicador o el script desde el Navegador al gráfico.

**MetaTrader 4:** copia `OpenCloseExtremos.mq4` en **MQL4 → Indicators** y sigue los mismos pasos. Los scripts de estadísticas solo existen para MT5.

**La app del móvil** no admite indicadores propios. Para recibir avisos en el móvil, deja el indicador corriendo en el PC o en un VPS con la notificación push activada (ver 3.4).

---

## 3. Indicador OpenCloseExtremos (v1.40)

### 3.1 Las flechas

| Flecha | Dónde | Significado |
|---|---|---|
| ▼ roja | encima | **Apertura = Máximo**: abrió en el punto más alto |
| ▼ naranja | encima, más arriba | **Cierre = Máximo**: cerró en el punto más alto |
| ▲ verde | debajo | **Apertura = Mínimo**: abrió en el punto más bajo |
| ▲ azul | debajo, más abajo | **Cierre = Mínimo**: cerró en el punto más bajo |

Una vela puede tener dos flechas. Si tiene roja y azul, o verde y naranja, es una **marubozu completa**: sin mecha en ningún extremo.

**Cada flecha se configura por separado.** En la ventana de parámetros hay un bloque propio para la roja, la naranja, la verde y la azul, cada uno con:
- **Mostrar flecha** (sí/no).
- **Color**, **tamaño** (1–5) y **símbolo** (código Wingdings: 233 = flecha arriba, 234 = flecha abajo, 159 = punto, 108 = círculo).
- **Incluir en las alertas** al cerrar la vela. Los canales (emergente, push, sonido) se eligen en su propio bloque.
- **Dibujar su línea de nivel** y el **color** de esa línea mientras está pendiente. Por defecto, sí en la roja y la verde y no en la naranja y la azul.

### 3.2 Las líneas de niveles (desequilibrios)

Desde cada flecha **verde** o **roja** sale una línea punteada fina en el extremo sin mecha:

- **Pendiente** (no testeado): verde apagado si está en un mínimo, rojo apagado si está en un máximo. Se prolonga hacia la derecha.
- **Testeado**: cuando una vela posterior toca el nivel, la línea se corta en esa vela y pasa a gris.
- Al pasar el ratón por encima se ve el tipo, el precio, la hora y si está testeado.

Por defecto solo se dibujan los niveles de **apertura**. Los de cierre (naranja y azul) casi siempre quedan testeados en la vela siguiente, porque esta abre pegada al cierre anterior.

#### Quitar líneas que ya no quieres ver

- **Ocultar una línea a mano:** haz clic sobre ella para seleccionarla y pulsa **Supr**. También puedes borrarla desde la lista de objetos (**Ctrl+B**). El indicador lo registra en la vela siguiente y no la vuelve a dibujar, ni siquiera al reiniciar MetaTrader. Lo guarda en las variables globales del terminal (F3), con nombres que empiezan por `OCE_O_`. MetaTrader borra las variables que no se usan en 4 semanas, y el indicador las renueva cada vez que las consulta.
- **Restaurar:** si hay líneas ocultas del símbolo, aparece abajo a la izquierda el botón **«Restaurar niveles ocultos (N)»**. Al pulsarlo vuelven todas.
- **Cuidado:** si usas «Borrar todos los objetos» del gráfico, todas las líneas visibles quedan ocultas. Se recuperan con el botón.
- **Elegir qué flechas dibujan línea:** cada flecha tiene su propio «Dibujar su línea de nivel». Por ejemplo, solo verdes: desactívalo en la roja.
- **Filtrar por sesión** en la que nació la vela, en hora del servidor: Asia 01–10 h, Londres 10–15 h, Londres+NY 15–19 h y NY tarde 19–24 h. Por ejemplo, ver solo los niveles nacidos en NY, que son los que más quedan abiertos (sección 5.2).
- **Testeados temporales:** con «Ocultar testeados tras N velas» mayor que 0, las líneas testeadas desaparecen pasadas N velas del gráfico desde el test.
- **Niveles de otra temporalidad:** con «Temporalidad de los niveles» puedes ver, por ejemplo, en un gráfico M1 solo los niveles de H1 o H4. Las flechas siguen siendo las de la temporalidad del gráfico. En ese caso, «Velas a revisar para niveles» cuenta velas de la temporalidad elegida.

### 3.3 Panel de porcentajes

En la esquina superior izquierda muestra, sobre las últimas velas cerradas:
- qué % de velas cumple cada uno de los cuatro casos;
- los ticks promedio de las velas marcadas frente a las no marcadas;
- la referencia teórica de un movimiento aleatorio.

Se puede desactivar.

### 3.4 Parámetros

| Parámetro | Por defecto | Para qué sirve |
|---|---|---|
| Tolerancia en puntos | 0 | 0 = coincidencia exacta. En XAUUSD 1 punto = 0.01. Súbela a 1–5 para incluir velas con una mecha casi nula |
| Marcar vela en formación | No | Si lo activas, la flecha de la vela actual puede aparecer y desaparecer |
| Separación de la flecha | 12 px (MT5) / 0.3 ATR (MT4) | Distancia de la flecha a la vela |
| Alerta emergente / push / sonido | No | Aviso al cerrar una vela que cumple |
| Mostrar panel de porcentajes | Sí | Muestra u oculta el panel |
| Velas cerradas a analizar | 1000 | Velas que usa el panel (0 = todas) |
| Dibujar niveles sin mecha | Sí | Muestra u oculta las líneas |
| Mantener niveles testeados | Sí | Si lo desactivas, solo quedan los pendientes |
| Velas a revisar para niveles | 500 | Hasta cuántas velas atrás busca niveles |
| **Por cada flecha** (roja, naranja, verde, azul) | | Mostrar, color, tamaño, símbolo, alerta, dibujar su línea y color de la línea pendiente |
| Color nivel ya testeado | Gris | Color de todas las líneas testeadas |
| Temporalidad de los niveles | La del gráfico | De qué temporalidad salen los niveles (por ejemplo H1 en un gráfico M1) |
| Niveles nacidos en Asia / Londres / Londres+NY / NY tarde | Sí (las 4) | Filtro por la sesión en que nació la vela |
| Ocultar testeados tras N velas | 0 | 0 = nunca; N = las testeadas desaparecen pasadas N velas |
| Permitir ocultar líneas a mano | Sí | Hace las líneas seleccionables y recuerda las que borras |
| Botón para restaurar niveles ocultos | Sí | Muestra el botón «Restaurar niveles ocultos (N)» |

**Notificaciones push al móvil:** en la app ve a *Ajustes → Mensajes* y copia tu **MetaQuotes ID**. En el PC ve a *Herramientas → Opciones → Notificaciones*, actívalas, pega el ID y pulsa «Prueba». Después activa «Notificación push» en el indicador.

---

## 4. Scripts de estadísticas (solo MT5)

Los dos scripts analizan **el activo del gráfico donde los sueltes** y responden a lo mismo para las flechas **verde y roja**:
- cuántos niveles se formaron en cada temporalidad;
- cuántos se testearon y cuánto tardaron;
- cómo reaccionó el precio después del test;
- si los niveles de temporalidades mayores reaccionan mejor (tabla de jerarquía).

Cada resultado se compara con un **grupo de control**: aperturas normales, con mecha, medidas igual. Sin esa comparación no se puede saber si los niveles sin mecha son especiales.

### 4.1 Cuál usar

| | EstadisticasNiveles | EstadisticasNivelesH1 |
|---|---|---|
| Mide la reacción con velas | M1 | H1 |
| Temporalidades por defecto | M1, M5, M15, M30, H1, H4, D1 | H1, H4, D1, W1 |
| Ventana de reacción | 30 minutos | 4 velas H1 (4 horas) |
| ATR para normalizar | 60 velas M1 | 24 velas H1 |
| Mejor para | Temporalidades bajas | H4, D1 y W1 (mucho más historial) |
| Archivos | `OCE_Estadisticas_<activo>` | `OCE_EstadisticasH1_<activo>` |

### 4.2 Cómo ejecutarlos

1. Ve a **Herramientas → Opciones → Gráficos** y pon «Máx. barras en el gráfico» en **Ilimitado**. Reinicia MetaTrader.
2. Abre un gráfico del activo en **M1** (script M1) o en **H1** (script H1).
3. Haz clic en el gráfico y pulsa **Inicio** varias veces para descargar historial. En portátiles suele ser **Fn + flecha izquierda**.
4. Arrastra el script al gráfico. Los parámetros por defecto valen.
5. Al terminar aparece el aviso «Estadísticas listas». El informe también sale en la pestaña **Expertos** de la Caja de herramientas (Ctrl+T).
6. Los archivos quedan en **Archivo → Abrir carpeta de datos → MQL5 → Files**:
   - `.txt`: informe legible.
   - `.csv`: un nivel por fila, para analizarlo en detalle.

### 4.3 Cómo leer el informe

| Término | Significado |
|---|---|
| Testeado | Una vela posterior volvió a tocar el nivel |
| Pendiente | Ninguna vela lo ha tocado todavía |
| Mediana test | La mitad de los niveles se testea antes de este tiempo |
| Respetado | Al final de la ventana de reacción, el precio quedó del lado del rebote |
| Rebote | Lo máximo que se alejó a favor después del test |
| Penetración | Cuánto atravesó el nivel en contra |
| Rebote / penetración | Mayor que 1: rebota más de lo que atraviesa |
| ATR | Rebote y penetración divididos por la volatilidad reciente, para comparar entre activos y épocas |
| p | Probabilidad de ver esa diferencia frente al control solo por azar. Por debajo de 0.05 se considera real |
| (pocos casos) | Menos de 30 tests medidos: no sacar conclusiones |

**Regla para leer la jerarquía:** si los niveles de una temporalidad tienen un *Respetado* y un *Rebote/Penetración* claramente mayores que su control, y esa ventaja crece con la temporalidad, hay jerarquía. Si se parecen al control, el regreso al nivel es el comportamiento normal del precio.

### 4.4 Otros activos

Funcionan con cualquier símbolo: EURUSD, índices, petróleo, cripto.
- Compara activos con las columnas en **ATR**, el **% respetado** y la relación **rebote/penetración**. Rebote y penetración en precio dependen de cada activo.
- En divisas con 5 decimales casi nunca coinciden exactamente apertura y extremo. Usa una tolerancia de 1–3 puntos.
- En activos con horario (índices, acciones), los huecos entre sesiones pueden testear o saltar niveles.

### 4.5 Cómo medir el spread

El spread (Ask − Bid) es el costo que se paga en cada entrada. El reglamento necesita conocerlo por hora para cerrar las reglas R6, R7 y R14. No hace falta ningún script: MetaTrader lo exporta.

**Método recomendado: script ResumenSpread (meses de ticks en un archivo pequeño).**
Exportar ticks crudos genera archivos enormes (5 semanas de oro ≈ 117 MB comprimidos). El script `MT5/Scripts/ResumenSpread.mq5` lee los ticks dentro de MetaTrader y guarda solo un resumen por día y hora.
1. Cópialo en **MQL5 → Scripts** y compílalo con **F7**.
2. Arrástralo a un gráfico de **XAUUSD** y pon las fechas **Desde** y **Hasta** (por ejemplo, de 2026.01.01 a 2026.10.06).
3. Espera: en la esquina del gráfico verás qué día está leyendo. La primera vez puede tardar, porque descarga los ticks del servidor.
4. Al terminar, el aviso indica cuántos días leyó. El archivo queda en **MQL5 → Files → `OCE_Spread_XAUUSD.csv`** y pesa pocos cientos de KB.
5. Adjúntalo en el chat.

Para cada día y hora trae: número de ticks, spread medio, percentiles 50, 75, 90 y 99, máximo, y el spread **ponderado por tiempo** (el que encontraría una orden enviada en un momento cualquiera de esa hora). Todo en puntos (1 punto = 0,01 en XAUUSD).

**Método manual: ticks crudos.** Cada tick trae su Bid y su Ask, así que el spread se calcula tick a tick. Sirve para revisar un día concreto.
1. Ve a **Ver → Símbolos** (Ctrl+U) y selecciona **XAUUSD**.
2. Abre la pestaña **Ticks**.
3. Elige un rango de **2 a 4 semanas** completas (de lunes a viernes) y pulsa **Solicitar**.
4. Pulsa **Exportar ticks** y guarda el CSV.
5. Envíamelo. Calculo el spread por hora del servidor y por día de la semana (mediana, percentil 90 y máximo).

La exportación de ticks puede no cubrir todo el historial disponible, y los archivos son grandes. Por eso conviene pedir pocas semanas cada vez.

**Método rápido: velas.**
1. En la misma ventana, pestaña **Barras**, elige **M1** y un rango de varios meses.
2. Pulsa **Solicitar** y luego **Exportar barras**.

El archivo trae una columna de spread por vela, en puntos (en XAUUSD, 1 punto = 0,01). MetaTrader guarda **un solo valor de spread por vela** y su documentación no aclara si es el mínimo o un promedio. Por eso sirve para ver el patrón por hora a lo largo de meses, pero los límites del reglamento se fijan con ticks.

**Comprobación en vivo.** En la **Observación de Mercado**, haz clic derecho, elige **Columnas → Spread** y verás el spread actual de cada símbolo. Así anota el trader el «spread al entrar» en el diario.

**Qué sale de la medición:**
- Las franjas definitivas de R6 (sin scalping) y R7 (horario de scalping).
- El tope de spread por hora de R14.
- La versión 1.1 del reglamento.

---

## 5. Resultados hasta ahora: XAUUSD, IC Markets, script M1 (2026-10-06)

Informe completo en `resultados/XAUUSD_M1_2026-10-06.txt`. Gráficos en la página de resultados.

| TF | Niveles | Testeados | Mediana test | Respetado (30 min) | Control |
|---|---|---|---|---|---|
| M1 | 5.219 | 99,1% | 3 velas (3 min) | 49,5% | 49,6% |
| M5 | 2.342 | 99,0% | 3 velas (15 min) | 50,1% | 50,1% |
| M15 | 2.010 | 98,8% | 3 velas (45 min) | 47,4% | 50,1% |
| M30 | 2.101 | 98,3% | 3 velas (1,5 h) | 49,4% | 49,9% |
| H1 | 1.661 | 98,3% | 3 velas (3 h) | 52,6% | 50,7% |
| H4 | 511 | 97,7% | 2 velas (8 h) | 64,0% (25 casos) | 50,7% |
| D1 | 189 | 95,8% | 2 velas (2 días) | 1 caso | 53,5% |

**Conclusiones:**
1. Casi todos los niveles acaban testeados (~99%), igual que los normales. Que el precio vuelva es lo esperable.
2. Los niveles sin mecha tardan **más** en testearse: ~30% en la vela siguiente, frente a ~50% de los normales. La mediana es 3 velas en todas las temporalidades.
3. De M1 a H1 la reacción tras el test ronda el 50%, igual que el control. Ninguna diferencia supera lo que podría ser azar.
4. El tiempo que el nivel estuvo pendiente no mejora la reacción.
5. H4 parecía mostrar jerarquía (64%), pero con solo 25 casos. El script H1 no lo confirma (ver 5.1).

### 5.1 Script H1: XAUUSD, IC Markets (2026-10-06)

Informe completo en `resultados/XAUUSD_H1_2026-10-06.txt`. Reacción medida en 4 velas H1, con historial H1 desde 1998.
Cada flecha se compara con el control de **su misma dirección**: la tendencia alcista del oro hace que todo lo que queda por debajo del precio se respete algo más.

| TF | Verde (casos) | Control alcista | p | Roja (casos) | Control bajista | p |
|---|---|---|---|---|---|---|
| H1 | 52,7% (807) | 52,8% | 0,94 | 47,1% (826) | 49,1% | 0,26 |
| H4 | 57,7% (319) | 52,9% | 0,09 | 46,7% (180) | 48,5% | 0,63 |
| D1 | 60,9% (133) | 55,3% | 0,21 | 39,6% (48) | 47,1% | 0,30 |
| W1 | 41,7% (12) | 54,8% | 0,36 | 33,3% (6) | 48,9% | 0,45 |

**Conclusiones:**
1. El 64% de H4 no se confirma: H4 da 53,7% frente a 50,8% del control.
2. Ninguna fila se separa de su control con claridad (todas con p > 0,05).
3. Las verdes de H4 y D1 juntas dan 58,6% frente a 53,6% (452 casos, p 0,03). Es un **indicio débil**: el grupo se eligió después de ver los datos y el efecto viene sobre todo de antes de 2018 (2018–2026: H4 55,1% frente a 52,6%, p 0,56; D1 solo 14 casos).
4. Las rojas no superan a su control en ninguna temporalidad.
5. El tiempo que el nivel estuvo pendiente no mejora la reacción.
6. Para confirmar o descartar el indicio de las verdes en H4 y D1 hace falta probarlo en otro activo o con datos futuros.

### 5.2 Por sesión (datos del script M1, temporalidades M1 a H1)

Sesiones en hora del servidor de IC Markets, que es siempre la hora de Nueva York + 7 (GMT+2 en invierno, GMT+3 en verano): **Asia** 01–10 h, **Londres** 10–15 h, **Londres+NY** (solapamiento) 15–19 h y **NY tarde** 19–24 h.

| Nace en | M5: se cierra en la misma sesión | H1: misma sesión | H1: siguiente sesión | Siguen sin testear (flechas / control) |
|---|---|---|---|---|
| Asia | 83,2% (control 87,2%) | 57,2% | 17,3% | 0,75% / 0,87% |
| Londres | 75,8% (85,4%) | 35,2% | 34,9% | 0,96% / 0,91% |
| Londres+NY | 71,3% (81,1%) | 22,2% | 21,4% | **2,11% / 1,29%** |
| NY tarde | 69,0% (82,3%) | 23,3% | 50,1% | **1,61% / 0,71%** |

**Conclusiones:**
1. La mayoría se cierra en la **misma sesión** en que nace (M5: 69–83%). Las flechas siempre algo menos que las velas normales, porque nacen en el extremo.
2. Si no se cierra en su sesión, casi siempre lo hace en la **siguiente**: Asia → Londres, Londres → Londres+NY, Londres+NY → NY tarde, NY tarde → Asia del día siguiente (85% en M15).
3. Asia tiene la tasa de «misma sesión» más alta en parte porque es la sesión más larga (9 h). Midiendo a 60 minutos, que no depende de la duración, Asia y Londres se parecen (≈74% en M5) y NY tarde es la más lenta (63%), en parte porque su última hora termina en el corte diario del mercado.
4. Una flecha que nace en la **última hora** de su sesión casi nunca se cierra en ella (M15: 30%, frente a 72% del resto).
5. Hallazgo más interesante: las flechas que nacen **durante la sesión de Nueva York** quedan sin testear unas **2 veces más** que las velas normales de esa misma sesión (Londres+NY 2,1% frente a 1,3%; NY tarde 1,6% frente a 0,7%). En Asia y Londres no hay diferencia. Encaja con la idea de impacto permanente: en NY salen los datos económicos de EE. UU. y los movimientos con información nueva no se deshacen. Es una interpretación; los números absolutos son pequeños (41 y 48 niveles).
6. Se forman más flechas en las horas de poca liquidez (01–02 h y 23 h: ~10–12% de las velas M1/M5) que en el solapamiento Londres+NY (16–18 h: ~5–6%), como predice la teoría de los ticks.
7. La reacción tras el test no cambia por sesión: ronda el 49–52% en todas, igual que el control.

### 5.3 ¿A qué hora se forman más y menos marubozus?

% de velas que son flecha verde o roja (sin mecha en la apertura), por hora. Las marubozus completas no se pueden contar con los archivos de los scripts.

**Conversión de horas.** El servidor de IC Markets es la hora de Nueva York + 7 y cambia con el horario de verano de EE. UU. El Salvador está en UTC-6 todo el año:
- De mediados de marzo al primer domingo de noviembre: **El Salvador = servidor − 9 h**.
- De noviembre a mediados de marzo: **El Salvador = servidor − 8 h**.

**Franjas con menos marubozus:**

| Sesión | Servidor | Nueva York | El Salvador (mar–nov) | El Salvador (nov–mar) | Qué tan claro es |
|---|---|---|---|---|---|
| Asia | 04:00–06:00 | 21:00–23:00 | **19:00–21:00** (noche anterior) | 20:00–22:00 | Claro |
| Asia (secundaria) | 08:00–10:00 | 01:00–03:00 | 23:00–01:00 | 00:00–02:00 | Moderado |
| Londres | 11:00–14:00 | 04:00–07:00 | **02:00–05:00** | 03:00–06:00 | Débil, Londres es plana |
| Londres+NY | 16:00–19:00 | 09:00–12:00 | **07:00–10:00** | 08:00–11:00 | Muy claro |
| ↳ Mínimo del día | 16:00–17:00 | 09:00–10:00 | **07:00–08:00** | 08:00–09:00 | M1 7%, H1 1,9% |
| ↳ Excepción vela H1 | 17:00–18:00 | 10:00–11:00 | 08:00–09:00 | 09:00–10:00 | H1 sube a 5,2% |
| NY tarde | 19:00–21:00 | 12:00–14:00 | **10:00–12:00** | 11:00–13:00 | Claro |

**Franjas con más marubozus:**

| Momento | Servidor | El Salvador (mar–nov) | El Salvador (nov–mar) |
|---|---|---|---|
| Reapertura tras el corte diario | 01:00–03:00 | 16:00–18:00 | 17:00–19:00 |
| Antes del corte diario | 23:00–24:00 | 14:00–15:00 | 15:00–16:00 |

**Por qué.** Con menos liquidez hay menos ticks en la vela, y es más probable que la apertura quede en un extremo. En la reapertura, el primer tick tras el corte diario puede llegar con hueco. La excepción de la vela H1 de las 17:00 h coincide con la apertura de la bolsa de Nueva York y con datos económicos de EE. UU.: es una interpretación, no comprobada con datos de noticias.

**Límites.** Los datos de M1 cubren solo 7 semanas; M15 (desde 2024) y H1 (desde 2018) confirman el patrón. En las semanas de marzo y octubre-noviembre en que Londres y Nueva York cambian de horario en fechas distintas, las franjas de Londres se desplazan una hora.

### 5.4 Niveles que no se testean

Muy pocos niveles quedan sin testear (M1 0,9%, H1 1,7%, H4 2,3%, D1 4,2%, W1 14%), y casi todos son antiguos y están lejos del precio: en H1 a ~52% del precio actual y en D1 a ~88% (mínimos de 2005–2008). En H4, D1 y W1 todos los pendientes son verdes (mínimos que la subida del oro dejó atrás), y las velas normales muestran el mismo reparto: es la tendencia, no la flecha.

El % que sigue sin testear después de N velas sigue la ley del camino aleatorio, 1/√(π·N):

| Velas | Flechas sin testear | Control | Azar puro |
|---|---|---|---|
| 1 | 69,7% | 49,8% | 56,4% |
| 5 | 39,7% | 26,1% | 25,2% |
| 20 | 20,8% | 13,6% | 12,6% |
| 100 | 9,2% | 6,1% | 5,6% |
| 1000 | 2,9% | 2,0% | 1,8% |

Las flechas siguen la misma curva que el azar, ~1,5 veces más arriba porque nacen en el extremo de la vela. Consecuencia: si un nivel lleva N velas pendiente, la probabilidad de que se testee en las N siguientes es siempre ~29%. **El tiempo no crea más presión por volver** (base de la regla R3 del reglamento).

### 5.5 Spread por hora (XAUUSD, IC Markets, 196 días)

Medido con el script `ResumenSpread` sobre los ticks del 2026-01-02 al 2026-10-05. Datos en `resultados/XAUUSD_spread_2026-01-02_2026-10-05.csv`. Valores en puntos (1 punto = 0,01 USD); «ponderado por tiempo» es el spread que encontraría una orden enviada en un momento cualquiera de esa hora. Cada cifra es la mediana de los 196 días.

| Hora servidor | El Salvador (mar–nov / nov–mar) | Ticks por hora | Spread típico | Percentil 90 | Días con P90 > 20 | Máximo típico del día |
|---|---|---|---|---|---|---|
| 01 | 16 / 17 | 10.600 | 9 | 12 | 7,7% | 99 |
| 02 | 17 / 18 | 11.000 | 9 | 12 | 2,6% | 86 |
| 03–08 | 18–23 / 19–00 | 12.000–29.000 | 9 | 12 | 0–0,5% | 67–93 |
| 09–14 | 00–05 / 01–06 | 15.000–22.000 | 8–8,5 | 10–11 | 0–1,5% | 72–83 |
| 15 | 06 / 07 | 27.000 | 8,6 | 10 | **7,1%** | 112 (hasta 700) |
| 16 | 07 / 08 | **46.400** | 8,6 | 10 | **5,1%** | 109 |
| 17 | 08 / 09 | **49.100** | 8 | 10 | 1,5% | 115 |
| 18 | 09 / 10 | 34.100 | 7,8 | 10 | 0,5% | 84 |
| 19–22 | 10–13 / 11–14 | 19.000–24.000 | 8–8,2 | 11 | 0–1% | 61–75 |
| **23** | 14 / 15 | 8.500 | **17,8** | **40** | **100%** | 82 |

**Conclusiones:**
1. El spread típico es **casi constante, 8–9 puntos (0,08–0,09 USD), de 02 a 22 h**. No hay diferencias entre días de la semana, y por meses solo febrero fue algo más alto (9,7).
2. **La hora de las 23 es la única claramente cara:** el spread se duplica todos los días, por la cercanía del corte diario.
3. **La 01 h (reapertura) y las 15–16 h (datos de EE. UU. a las 15:30 y apertura de la bolsa a las 16:30)** tienen picos ocasionales, con máximos de hasta 700 puntos (7 USD).
4. **La liquidez sí cambia mucho:** 16–17 h tiene unos 47.000 ticks por hora, frente a ~10.000 en la reapertura y a las 23 h.
5. Costo por operación: con 9 puntos de spread y, si aplica a la cuenta, 7 USD de comisión por lote ida y vuelta (0,07 USD por onza), cada entrada cuesta ~0,16 USD por onza. Con un stop de 1 USD, el costo ya es el 16% del riesgo.

Estos datos fijaron las reglas R6, R7, R8, R14 y R18 de la versión 1.1 del reglamento.

---

## 6. Simulador de ticks y velas

`paginas/simulador-velas-ticks.html` (o el enlace publicado). Explica de forma interactiva:
- qué es un tick y por qué la vela se dibuja solo con el **Bid**;
- cómo una compra mueve primero el Ask y después el Bid;
- las cuatro flechas, cada una con su escenario guiado;
- qué persigue cada participante en cada paso: proveedor de liquidez, fondo, retail, bróker, arbitrajistas y coberturistas;
- la marubozu, el inventario del proveedor y el regreso al nivel;
- el escenario de tus dos desequilibrios (uno testeado y otro pendiente).

Es un **modelo simplificado con números inventados**, no datos reales.

---

## 7. Glosario

- **Tick:** cada actualización de precio que envía el bróker (cambio de Bid o de Ask). No es una operación.
- **Bid / Ask:** precio al que te compran / precio al que te venden. En forex y CFDs la vela se dibuja con el Bid.
- **Volumen de ticks:** cuántas actualizaciones llegaron en la vela. No es volumen negociado.
- **Marubozu:** vela sin mecha en uno o en los dos extremos.
- **Nivel sin mecha:** el precio del extremo sin mecha de una vela con flecha verde o roja.
- **Testeado / pendiente:** si una vela posterior ha vuelto a tocar el nivel o no.
- **Desequilibrio:** tu interpretación del nivel pendiente: una zona que el precio dejó atrás y podría volver a buscar.
- **Grupo de control:** niveles normales (aperturas con mecha) medidos igual, para comparar.

---

## 8. Problemas frecuentes

| Problema | Solución |
|---|---|
| No encuentro la carpeta | *Archivo → Abrir carpeta de datos*. Los indicadores van en `MQL5/Indicators`, los scripts en `MQL5/Scripts` y los resultados aparecen en `MQL5/Files` |
| El indicador no aparece en el Navegador | Clic derecho en «Indicadores» → Actualizar. Comprueba que compiló sin errores (F7) |
| El script dice «sin datos» o hay pocos casos | Pon Máx. barras en Ilimitado y pulsa Inicio en el gráfico para descargar más historial |
| No salen flechas en un activo | Sube la tolerancia a 1–3 puntos |
| Error al compilar | Copia el mensaje de la pestaña «Errores» de MetaEditor |

---

## 9. Historial de versiones

| Fecha | Cambio |
|---|---|
| 2026-10-06 | Indicador v1.00: cuatro flechas y alertas |
| 2026-10-06 | Indicador v1.10: panel de porcentajes |
| 2026-10-06 | Indicador v1.20: líneas punteadas de niveles sin mecha |
| 2026-10-07 | Indicador v1.40: configuración separada para cada una de las 4 flechas (mostrar, color, tamaño, símbolo, alerta y línea de nivel) |
| 2026-10-07 | Indicador v1.30: ocultar líneas a mano (persistente) con botón de restaurar, filtros por dirección y sesión, testeados temporales y niveles de otra temporalidad |
| 2026-10-06 | Script EstadisticasNiveles (M1) y primera página de resultados de XAUUSD |
| 2026-10-06 | Script EstadisticasNivelesH1 |
| 2026-10-06 | Resultados H1 de XAUUSD añadidos a la página y al manual |
| 2026-10-06 | Análisis por sesión añadido a la página y al manual |
| 2026-10-06 | Franjas horarias con más y menos marubozus, con hora de El Salvador |
| 2026-10-06 | Reglamento operativo v1.0, sección 4.5 (cómo medir el spread) y 5.4 (niveles que no se testean) |
| 2026-10-06 | Script ResumenSpread |
| 2026-10-07 | Spread por hora medido (sección 5.5) y reglamento v1.1 |
