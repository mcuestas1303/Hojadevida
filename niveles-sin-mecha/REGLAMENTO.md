# Reglamento operativo · Scalping e intradía

**Versión 1.1 · vigente desde el 2026-10-07**

Este reglamento es **obligatorio** para todo el equipo. Las reglas se basan en las estadísticas de `MANUAL.md` (secciones 5 a 5.3) y en prácticas de gestión de riesgo. Ninguna regla se puede saltar por criterio personal: se cambia solo por el procedimiento de la sección 7.

Este documento organiza la operativa del equipo. No es asesoría de inversión. Si el fondo gestiona dinero de terceros, también debe cumplir la regulación que le aplique, que este reglamento no cubre.

---

## 1. Alcance

| | |
|---|---|
| Activo | XAUUSD |
| Bróker y plataforma | IC Markets, MetaTrader 5 |
| Modalidades | Scalping (M1–M5, operaciones de minutos) e intradía (M15–H1, cerradas el mismo día) |
| Cuentas | Todas las cuentas reales y de prueba del fondo |
| Revisión | Cada mes, o antes si se activa un disparador de la sección 6 |

Cualquier otro activo necesita sus propias estadísticas y una versión del reglamento aprobada para él.

---

## 2. Roles

| Rol | Responsabilidades |
|---|---|
| **Responsable de riesgo** | Vigila los límites diarios y mensuales, aprueba o rechaza cambios de reglas, aplica las consecuencias de los incumplimientos y publica cada versión del reglamento. |
| **Trader** | Cumple las reglas, registra cada operación en el diario antes de que acabe el día y comunica cualquier incidencia. |
| **Analista** | Mide el spread, mantiene las estadísticas al día, prueba las hipótesis nuevas y entrega los datos para la revisión mensual. |

Si el equipo es pequeño, una persona puede tener dos roles. Lo único que no se permite es que alguien revise sus propias operaciones: el diario de un trader lo revisa otra persona.

---

## 3. Reglas

Cada regla indica de dónde sale:
- **Datos:** resultados medidos con el historial de IC Markets (sección del manual entre paréntesis).
- **Riesgo:** práctica de gestión de riesgo.
- **Método:** cómo se prueban y aprueban las ideas.

Y su estado:
- **Vigente:** se aplica tal cual.
- **Provisional:** se aplica ya, pero su valor se ajustará con nuevas mediciones (sección 5).

### 3.1 Señales

| ID | Regla | Origen | Cómo se audita | Estado |
|---|---|---|---|---|
| R1 | **No se debe** abrir una operación con un nivel sin mecha como único motivo. Toda entrada debe registrar en el diario una razón adicional, aprobada según la sección 7. | Datos (5, 5.1): tras el test, el precio queda del lado del rebote ~50% de las veces, igual que en velas normales. | Campo «regla aplicada» del diario | Vigente |
| R2 | **No se debe** abrir una operación cuya tesis sea que «el precio tiene que volver al nivel». | Datos (5): el precio vuelve ~99% de las veces, pero llegar al nivel antes que a un stop a la misma distancia es ~50%, y con costos se pierde. | Campo «motivo de entrada» | Vigente |
| R3 | **No se debe** aumentar el tamaño de una operación porque un nivel lleve mucho tiempo sin testear. | Datos (5.4): cuanto más antiguo el nivel, menos probable que vuelva pronto. | Tamaño frente a R12 | Vigente |
| R4 | **No se debe** asumir que un nivel nacido en la sesión de Nueva York (15:00–24:00 servidor) se cerrará. Esos niveles no pueden usarse como objetivo de precio. | Datos (5.2): quedan sin testear unas 2 veces más que las velas normales. | Campo «objetivo» y sesión del nivel | Vigente |
| R5 | La pista de las flechas verdes en H4 y D1 **solo se puede operar** como hipótesis en prueba, según R15 y R16. | Datos (5.1): 58,6% frente a 53,6%, no confirmado. | Cuenta o etiqueta de prueba | Vigente |

### 3.2 Horario

Hora del servidor de IC Markets (Nueva York + 7). Para El Salvador: servidor − 9 h de mediados de marzo al primer domingo de noviembre, y servidor − 8 h el resto del año.

| ID | Regla | Servidor | El Salvador (mar–nov) | El Salvador (nov–mar) | Origen | Estado |
|---|---|---|---|---|---|---|
| R6 | **No se debe** hacer scalping en esta franja. | 23:00–02:00 | 14:00–17:00 | 15:00–18:00 | Datos (5.5): a las 23 h el spread se duplica todos los días (percentil 90 de 40 puntos frente a 10–12 el resto del día); a la 01 h hay picos en el 8% de los días | Vigente |
| R7 | El scalping **solo se permite** de 02:00 a 23:00, respetando R8. La franja **preferente** es 16:00–19:00, la de más ticks por hora. | 02:00–23:00 (preferente 16:00–19:00) | 17:00–14:00 (preferente 07:00–10:00) | 18:00–15:00 (preferente 08:00–11:00) | Datos (5.5): de 02 a 23 h el spread típico es el mismo (8–9 puntos); 16–17 h concentra ~47.000 ticks por hora, frente a ~20.000 de media | Vigente |
| R8 | **No se debe** abrir una operación en los 5 minutos anteriores ni en los 15 posteriores a un dato económico de alto impacto de EE. UU. (la mayoría sale a las 15:30 servidor), ni en los 5 minutos alrededor de la apertura de la bolsa de NY. | 15:25–15:45 (datos) y 16:25–16:35 (apertura) | 06:25–06:45 y 07:25–07:35 | 07:25–07:45 y 08:25–08:35 | Datos (5.3 y 5.5): a las 15 y 16 h el spread se dispara en el 5–7% de los días (hasta 700 puntos) y la vela H1 de las 17:00 concentra movimientos direccionales | Vigente |
| R9 | El intradía (M15–H1) **debe cerrar** todas sus posiciones antes del corte diario. | Antes de 23:45 | Antes de 14:45 | Antes de 15:45 | Riesgo: evitar el hueco de la reapertura | Vigente |

### 3.3 Riesgo

| ID | Regla | Origen | Cómo se audita | Estado |
|---|---|---|---|---|
| R10 | **Riesgo máximo por operación:** 0,25% del capital de la cuenta en scalping y 0,5% en intradía, contando el spread y la comisión. | Riesgo | Columna «riesgo %» del diario | Vigente |
| R11 | **Toda operación debe tener stop** colocado en la plataforma al entrar. El stop **nunca** se mueve en contra; solo puede acercarse para proteger ganancias. | Riesgo | Historial de órdenes del bróker | Vigente |
| R12 | **Pérdida máxima diaria: 2%.** Al alcanzarla, el trader cierra todo y no opera más ese día. | Riesgo | Resultado diario por trader | Vigente |
| R13 | **Pérdida máxima mensual: 6%.** Al alcanzarla, **todo el equipo** deja de operar en real hasta la revisión extraordinaria (sección 6). | Riesgo | Resultado mensual del fondo | Vigente |
| R14 | **No se debe** entrar si el spread en ese momento supera **18 puntos (0,18 USD)**. Es el doble del spread típico (8–9 puntos) y solo se supera en momentos anómalos: noticias, reapertura o antes del corte. | Datos (5.5) | Campo «spread al entrar» | Vigente |
| R18 | **No se debe** abrir una operación en la que el costo total (spread + comisión de la cuenta) supere el **10% del riesgo**. Ejemplo: con un spread de 0,09 USD y una comisión de 0,07 USD por onza (7 USD por lote ida y vuelta, si es la que aplica a la cuenta), el costo es 0,16 USD, así que el stop debe estar como mínimo a **1,60 USD** (160 puntos) de la entrada. | Datos (5.5) y Riesgo | Entrada, stop, spread y comisión en el diario | Vigente |

### 3.4 Método

| ID | Regla | Origen | Cómo se audita | Estado |
|---|---|---|---|---|
| R15 | Una idea nueva **solo se valida** con datos que no se usaron para descubrirla: otro activo, otro periodo o los meses siguientes. | Método | Informe del analista | Vigente |
| R16 | Antes de operar con tamaño normal, una idea **debe pasar** 100 operaciones con tamaño mínimo (0,01 lotes o cuenta demo), registradas, y superar al grupo de control con p < 0,05 y un resultado positivo después de costos. | Método | Informe de la fase de prueba | Vigente |
| R17 | **Toda operación se registra** en el diario (sección 8) antes del final del día. Una operación sin registrar cuenta como incumplimiento. | Método | Diario frente al historial del bróker | Vigente |

---

## 4. Incumplimientos

| Situación | Consecuencia |
|---|---|
| Primer incumplimiento del mes | Queda registrado. Revisión con el responsable de riesgo en un máximo de 2 días. |
| Segundo incumplimiento en el mismo mes | Suspensión de la operativa real del trader hasta una revisión con el responsable de riesgo. Mientras tanto, solo opera en demo. |
| Incumplir R11 o R12 (stop o límite diario) | Suspensión inmediata de la operativa real ese día y revisión. |
| Se alcanza R13 (límite mensual) | Todo el equipo deja de operar en real hasta la revisión extraordinaria. |

---

## 5. Spread medido

Medido el 2026-10-07 con el script `ResumenSpread` sobre los ticks del 2026-01-02 al 2026-10-05 (196 días). El detalle está en la sección 5.5 del manual y en `resultados/XAUUSD_spread_2026-01-02_2026-10-05.csv`.

| Hora del servidor | Spread típico (ponderado por tiempo) | Percentil 90 | Días con percentil 90 > 20 puntos |
|---|---|---|---|
| 01 h | 9 puntos | 12 | 7,7% |
| 02–14 h | 8–9 | 10–12 | 0–2,6% |
| 15–16 h | 8–9 | 10 | 5–7% (datos de EE. UU.) |
| 17–22 h | 8 | 10–11 | 0–1,5% |
| 23 h | **18** | **40** | **100%** |

No hay diferencias entre días de la semana ni cambios importantes entre meses. El analista repite la medición cada 3 meses o si el bróker cambia condiciones.

---

## 6. Revisiones

**Revisión mensual** (primer día hábil del mes), con el analista y el responsable de riesgo:
- Resultado por trader y por regla aplicada.
- Incumplimientos del mes.
- Estado de las hipótesis en prueba (R15, R16).
- Spread medido, si hay datos nuevos.

**Revisión extraordinaria**, que se activa si:
- Se alcanza el límite mensual (R13).
- Hay 3 o más incumplimientos en el equipo en un mismo mes.
- El bróker cambia condiciones: horario, comisión o tipo de cuenta.

---

## 7. Cómo se cambia una regla

1. **Propuesta escrita:** qué regla se cambia, por qué y con qué evidencia.
2. **Prueba:** si la propuesta depende de una ventaja nueva, se aplican R15 y R16.
3. **Aprobación:** la aprueba o la rechaza el responsable de riesgo, por escrito.
4. **Publicación:** nueva versión del reglamento con fecha y una fila en el historial (sección 9). Las reglas nuevas aplican a partir del día siguiente.

---

## 8. Plantilla del diario

| Campo | Ejemplo |
|---|---|
| Fecha y hora (servidor) | 2026-10-07 16:42 |
| Sesión | Londres+NY |
| Trader | Iniciales |
| Activo / TF | XAUUSD / M5 |
| Modalidad | Scalping |
| Nivel (si aplica) | Verde H1 4152,30, formado 2026-10-06 09:00, no testeado |
| Dirección | Compra |
| Motivo de entrada | Regla o hipótesis aprobada (no vale «el precio vuelve») |
| Regla aplicada | ID de la regla o de la hipótesis en prueba |
| Entrada / stop / objetivo | 4155,10 / 4152,10 / 4161,10 |
| Riesgo % | 0,25% |
| Spread al entrar | 0,12 |
| Resultado (R y USD) | +2,0 R / +… |
| Incidencias | Deslizamiento, desconexión, noticia, etc. |

---

## 9. Historial de versiones

| Versión | Fecha | Cambio |
|---|---|---|
| 1.0 | 2026-10-06 | Primera versión. R6, R7 y R14 provisionales hasta medir el spread. |
| 1.1 | 2026-10-07 | Spread medido (196 días). R6 pasa a 23:00–02:00; R7 permite el scalping de 02:00 a 23:00 con franja preferente 16:00–19:00; R8 añade la ventana de las 15:30; R14 fija el tope en 18 puntos; nueva R18 (costo máximo 10% del riesgo). Todas vigentes. |
