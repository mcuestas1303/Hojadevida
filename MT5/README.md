# Zonas de eventos NY (indicador para MetaTrader 5)

Indicador `ZonasEventosNY.mq5` que marca en el gráfico:

- **La vela de apertura de Nueva York** (NYSE y Nasdaq abren a la misma hora, 9:30 hora de Nueva York). Dibuja un recuadro transparente (solo el borde) con el máximo y el mínimo de esa vela. El recuadro de la apertura más reciente se extiende hasta la vela en curso y avanza con cada vela nueva; los de días anteriores terminan al cierre (16:00 NY).
- **Las noticias del calendario económico de MT5**, tanto las pasadas como las próximas:
  - línea vertical sólida = noticia que ya salió; punteada = noticia que aún no sale;
  - color según importancia (rojo alta, naranja media, amarillo baja);
  - al pasar el ratón por la línea se ve la hora de NY, la previsión, el dato anterior, el dato real y si salió por encima o por debajo de lo esperado;
  - en las noticias de importancia alta marca también la **vela de la noticia** (máximo y mínimo) como zona.

## Actualización automática

No hay que hacer nada cuando sale una noticia: cada 10 segundos el indicador pregunta al calendario de MT5 si hubo cambios (`CalendarValueLast`). Cuando se publica un dato:

1. la línea y la zona se actualizan solas con el dato real;
2. salta una alerta en MT5 (y, si se activa, una notificación al móvil).

También avisa unos minutos **antes** de cada noticia importante (5 minutos por defecto).

## Instalación

1. En MT5: **Archivo → Abrir carpeta de datos**, y entrar en `MQL5/Indicators`.
2. Copiar ahí `ZonasEventosNY.mq5`.
3. Abrir el archivo en **MetaEditor** (F4 desde MT5) y compilar con **F7**.
4. En MT5, en el Navegador → Indicadores, arrastrar **ZonasEventosNY** al gráfico (US30, NAS100, SPX500, etc.).
5. Revisar la pestaña **Expertos** de la caja de herramientas: el indicador escribe la hora del servidor en que cae la apertura de NY (por ejemplo `16:30`). Compruébalo con una vela real; si no coincide, ajusta el horario del bróker en los parámetros.

Para recibir los avisos en el móvil: **Herramientas → Opciones → Notificaciones**, poner el MetaQuotes ID de la app MT5 del teléfono y activar el parámetro *Enviar también al móvil*.

## Parámetros principales

| Parámetro | Para qué sirve |
| --- | --- |
| Cambio de horario del servidor | Cómo cambia de hora tu bróker. La mayoría usa GMT+2 en invierno y GMT+3 en verano siguiendo a EE. UU. (opción por defecto). |
| Desfase del servidor en invierno | Déjalo en 99 para detectarlo solo; si la apertura sale corrida, pon el desfase en horas (por ejemplo `2`). |
| Hora / minuto de apertura | 9:30 por defecto. Se puede cambiar, por ejemplo, a 8:30 para la hora de las noticias de empleo e IPC. |
| Rellenar el recuadro | Desactivado por defecto para que el recuadro sea transparente. MT5 no permite rellenos semitransparentes en sus objetos: si se activa, el relleno queda detrás de las velas pero tapa la cuadrícula. |
| Extender también las zonas anteriores | Si se activa, todos los recuadros (también los de días y noticias anteriores) llegan hasta la vela en curso. |
| Temporalidad de la vela | Qué vela se usa como "vela de apertura" y "vela de la noticia" (M15 por defecto; M5, H1 o la del gráfico). |
| Moneda | `USD` por defecto. Vacío = todas las monedas. |
| Importancia mínima para la línea | Qué noticias se dibujan (media y alta por defecto). |
| Importancia mínima para zona y avisos | Qué noticias marcan la vela y generan alertas (alta por defecto). |
| Solo noticias que contengan | Filtro por nombre separado por `;`, por ejemplo `CPI;Nonfarm;FOMC;GDP`. |
| Días hacia atrás / adelante | Cuántas noticias y aperturas pasadas se marcan y cuántos días de noticias futuras se muestran. |

## Notas

- El calendario usa la hora del servidor del bróker, igual que las velas, así que las líneas caen en la vela correcta.
- El calendario de MT5 no funciona en el Probador de estrategias; el indicador está pensado para el gráfico en vivo.
- Los nombres de las noticias aparecen como los da el calendario de MetaQuotes (normalmente en inglés), por eso el filtro por nombre se escribe en ese idioma.
