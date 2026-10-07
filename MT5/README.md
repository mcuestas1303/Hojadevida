# Zonas de eventos NY (indicador para MetaTrader 5)

Indicador `ZonasEventosNY.mq5` que marca en el gráfico:

- **La vela de apertura de Nueva York** (NYSE y Nasdaq abren a la misma hora, 9:30 hora de Nueva York). Dibuja una zona (rectángulo gris detrás de las velas) con el máximo y el mínimo de la **vela de 1 minuto** de la apertura y una etiqueta al final, por ejemplo `Apertura NY 07 OCT 26`. Como la zona se calcula siempre con la vela M1, se ve igual aunque cambies la temporalidad del gráfico. Solo se marca la apertura de los **días con noticia** (las de importancia alta o, en el modo estudio, la noticia elegida); se puede cambiar con *Marcar la apertura solo en días con noticia*. La zona de la apertura más reciente se extiende hasta la vela en curso; las de días anteriores terminan al cierre (16:00 NY).
- **Las noticias del calendario económico de MT5**, tanto las pasadas como las próximas:
  - cuando la noticia sale, se marca como **zona** el máximo y el mínimo de su vela de 1 minuto, con una etiqueta al final como `PPI m/m SEP 26` (color según importancia: rosa alta, naranja media, amarillo baja);
  - las noticias que aún no salen se ven como línea punteada; las pasadas no llevan línea, solo la zona;
  - al pasar el ratón por la zona o la etiqueta se ve la hora de NY, la previsión, el dato anterior, el dato real y si salió por encima o por debajo de lo esperado.

## Modo estudio: una noticia en los últimos años

Para ver, por ejemplo, **todas las publicaciones del IPC (CPI) de los últimos 5 años**:

1. En los parámetros, grupo *Estudio histórico de una noticia*: activar **Activar el estudio histórico**, escribir la noticia en **Noticia a estudiar** (`CPI`) y los **Años hacia atrás** (`5`).
2. El indicador carga solo esa noticia y marca en cada publicación:
   - la línea de la noticia y el recuadro de **su vela**;
   - el recuadro de la **vela de apertura de NY de ese mismo día**.
3. Abajo a la izquierda aparece un panel con:
   - botones **◄ Anterior** y **Siguiente ►**, que mueven el gráfico a cada publicación (la línea elegida se ve más gruesa);
   - fecha y hora de NY, previsión, dato anterior y dato real de cada parte de la noticia (por ejemplo IPC m/m, a/a y subyacente);
   - apertura, máximo, mínimo, cierre, rango y dirección de la vela de la noticia y de la vela de apertura;
   - el **promedio** de rango y el porcentaje de velas alcistas de todas las publicaciones.
4. **Exportar CSV** guarda una fila por publicación en `MQL5/Files` para abrirla en Excel.

Para estudiar otra noticia basta con cambiar el texto: `Nonfarm` (nóminas), `FOMC` o `Interest Rate` (Fed), `GDP` (PIB), `Retail Sales`, `ISM`, `PPI`… Se pueden juntar varias con `;`, por ejemplo `CPI;PPI`. Los nombres son los del calendario de MetaQuotes, normalmente en inglés.

**Historial necesario:** las zonas usan velas de 1 minuto, y 5 años de M1 son cerca de 1,8 millones de barras. En **Herramientas → Opciones → Gráficos** hay que subir **Máx. barras en el gráfico** (o ponerlo en *Ilimitado*); si no alcanza, el panel dice "sin datos (falta historial)" y la pestaña Expertos muestra un aviso. La primera vez MT5 puede tardar en descargar el historial: los recuadros aparecen solos a medida que llega.

Al usar los botones se desactiva el desplazamiento automático del gráfico; para volver a la vela actual, pulsa el botón de desplazamiento automático de la barra de herramientas o la tecla *Fin*.

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
| Rellenar el recuadro | Activado: la zona es un rectángulo gris detrás de las velas. MT5 no permite transparencia real en sus objetos; si se desactiva, queda solo el borde. |
| Extender también las zonas anteriores | Si se activa, todos los recuadros (también los de días y noticias anteriores) llegan hasta la vela en curso. |
| Vela que forma la zona | M1 por defecto: la zona cubre la vela de 1 minuto y es la misma en todas las temporalidades. |
| Líneas en noticias pasadas / próximas | Por defecto solo se ven las líneas punteadas de las noticias que aún no salen. |
| Extender la zona de la noticia | Cuánto se extienden las zonas de noticias anteriores (1 día por defecto); la más reciente llega hasta la vela en curso. |
| Moneda | `USD` por defecto. Vacío = todas las monedas. |
| Importancia mínima para la línea | Qué noticias se dibujan (media y alta por defecto). |
| Importancia mínima para zona y avisos | Qué noticias marcan la vela y generan alertas (alta por defecto). |
| Solo noticias que contengan | Filtro por nombre separado por `;`, por ejemplo `CPI;Nonfarm;FOMC;GDP`. |
| Días hacia atrás / adelante | Cuántas noticias y aperturas pasadas se marcan y cuántos días de noticias futuras se muestran. |

## Notas

- El calendario usa la hora del servidor del bróker, igual que las velas, así que las líneas caen en la vela correcta.
- El calendario de MT5 no funciona en el Probador de estrategias; el indicador está pensado para el gráfico en vivo.
- Los nombres de las noticias aparecen como los da el calendario de MetaQuotes (normalmente en inglés), por eso el filtro por nombre se escribe en ese idioma.
