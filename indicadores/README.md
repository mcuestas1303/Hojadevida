# OpenCloseExtremos — indicador MT4 / MT5

Marca con una flecha las velas cuya **apertura o cierre es igual al máximo o al mínimo**
de la propia vela (vela sin mecha en ese extremo). Funciona en cualquier símbolo y
temporalidad (p. ej. XAUUSD M1 en IC Markets).

| Flecha | Posición | Significado |
|---|---|---|
| ▼ roja | encima | Apertura = Máximo |
| ▼ naranja | encima (más arriba) | Cierre = Máximo |
| ▲ verde | debajo | Apertura = Mínimo |
| ▲ azul | debajo (más abajo) | Cierre = Mínimo |

## Instalación
1. MT5: copiar `OpenCloseExtremos.mq5` en `Archivo > Abrir carpeta de datos > MQL5/Indicators`.
   MT4: copiar `OpenCloseExtremos.mq4` en `MQL4/Indicators`.
2. Abrir MetaEditor (F4), abrir el archivo y compilar (F7).
3. En el terminal: Navegador > Indicadores > arrastrar `OpenCloseExtremos` al gráfico.

## Parámetros
- **Tolerancia en puntos**: 0 = coincidencia exacta. En XAUUSD (2 decimales) 1 punto = 0.01.
  Subirla (p. ej. 3–5) marca también velas con mecha casi nula.
- **Marcar Apertura / Cierre**: activar cada condición por separado.
- **Marcar vela en formación**: por defecto sólo se marcan velas cerradas.
- **Alertas**: emergente, push al móvil y/o sonido cuando cierra una vela que cumple.
- **Mostrar panel de porcentajes** (activado por defecto): muestra en la esquina superior
  izquierda qué % de las velas cerradas cumple cada caso, el promedio de ticks de las velas
  marcadas frente a las no marcadas, y la referencia teórica de un movimiento aleatorio
  (teorema de Sparre Andersen: C(2m,m)/4^m ≈ 1/√(π·m) con m = ticks − 1).
- **Velas cerradas a analizar**: cuántas velas usa el panel (0 = todo el historial cargado).

## Niveles sin mecha (desequilibrios) — v1.20
Desde cada vela con **Apertura = Máximo** (flecha roja) o **Apertura = Mínimo** (flecha verde)
se dibuja una línea punteada fina en el extremo sin mecha:
- **Pendiente** (no testeado): verde apagado si está en un mínimo, rojo apagado si está en un máximo,
  y se prolonga hacia la derecha.
- **Testeado**: en cuanto una vela posterior toca el nivel, la línea se corta en esa vela y pasa a gris.

Parámetros: activar/desactivar niveles, incluir también los de cierre (suelen testearse en la
vela siguiente), mantener u ocultar los testeados, velas a revisar (500) y los tres colores.
