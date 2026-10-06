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
