# Manual · Niveles sin mecha

Herramientas para estudiar las velas cuya **apertura o cierre coincide con el máximo o el mínimo** (velas sin mecha en un extremo) y los niveles que dejan atrás.

Probado con datos de **XAUUSD en IC Markets (MetaTrader 5)**. Funciona con cualquier activo.

---

## 1. Qué hay en esta carpeta

```
niveles-sin-mecha/
├── MANUAL.md                         ← este manual
├── MT5/
│   ├── Indicators/
│   │   └── OpenCloseExtremos.mq5     ← indicador: flechas, panel de % y líneas de niveles
│   └── Scripts/
│       ├── EstadisticasNiveles.mq5   ← estadísticas, reacción medida en M1
│       └── EstadisticasNivelesH1.mq5 ← estadísticas, reacción medida en H1
├── MT4/
│   └── Indicators/
│       └── OpenCloseExtremos.mq4     ← el mismo indicador para MetaTrader 4
├── paginas/
│   ├── simulador-velas-ticks.html        ← simulador interactivo de ticks y velas
│   └── estadisticas-niveles-xauusd.html  ← resultados con gráficos (XAUUSD, M1)
└── resultados/
    └── XAUUSD_M1_2026-10-06.txt      ← informe original del script M1
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

## 3. Indicador OpenCloseExtremos (v1.20)

### 3.1 Las flechas

| Flecha | Dónde | Significado |
|---|---|---|
| ▼ roja | encima | **Apertura = Máximo**: abrió en el punto más alto |
| ▼ naranja | encima, más arriba | **Cierre = Máximo**: cerró en el punto más alto |
| ▲ verde | debajo | **Apertura = Mínimo**: abrió en el punto más bajo |
| ▲ azul | debajo, más abajo | **Cierre = Mínimo**: cerró en el punto más bajo |

Una vela puede tener dos flechas. Si tiene roja y azul, o verde y naranja, es una **marubozu completa**: sin mecha en ningún extremo.

### 3.2 Las líneas de niveles (desequilibrios)

Desde cada flecha **verde** o **roja** sale una línea punteada fina en el extremo sin mecha:

- **Pendiente** (no testeado): verde apagado si está en un mínimo, rojo apagado si está en un máximo. Se prolonga hacia la derecha.
- **Testeado**: cuando una vela posterior toca el nivel, la línea se corta en esa vela y pasa a gris.
- Al pasar el ratón por encima se ve el tipo, el precio, la hora y si está testeado.

Por defecto solo se dibujan los niveles de **apertura**. Los de cierre (naranja y azul) casi siempre quedan testeados en la vela siguiente, porque esta abre pegada al cierre anterior.

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
| Marcar Apertura / Cierre | Sí / Sí | Activar cada condición por separado |
| Marcar vela en formación | No | Si lo activas, la flecha de la vela actual puede aparecer y desaparecer |
| Separación de la flecha | 12 px (MT5) / 0.3 ATR (MT4) | Distancia de la flecha a la vela |
| Alerta emergente / push / sonido | No | Aviso al cerrar una vela que cumple |
| Mostrar panel de porcentajes | Sí | Muestra u oculta el panel |
| Velas cerradas a analizar | 1000 | Velas que usa el panel (0 = todas) |
| Dibujar niveles sin mecha | Sí | Muestra u oculta las líneas |
| Incluir niveles de cierre | No | Añade líneas para las flechas naranja y azul |
| Mantener niveles testeados | Sí | Si lo desactivas, solo quedan los pendientes |
| Velas a revisar para niveles | 500 | Hasta cuántas velas atrás busca niveles |
| Colores de niveles (3) | Verde, rojo y gris apagados | Pendiente en mínimo / pendiente en máximo / testeado |

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
5. H4 muestra la única pista de jerarquía (64%), pero con solo 25 casos. **Pendiente:** confirmarlo con el script H1.

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
| 2026-10-06 | Script EstadisticasNiveles (M1) y primera página de resultados de XAUUSD |
| 2026-10-06 | Script EstadisticasNivelesH1 |
