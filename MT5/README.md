# Zonas de eventos NY (indicador para MetaTrader 5)

Indicador `ZonasEventosNY_vX.YY.mq5` (la versión va en el nombre del archivo; la actual es `ZonasEventosNY_v1.43.mq5`) que marca en el gráfico:

- **La vela de apertura de Nueva York** (NYSE y Nasdaq abren a la misma hora, 9:30 hora de Nueva York). Dibuja una zona (rectángulo gris detrás de las velas) con el máximo y el mínimo de la **vela de 1 minuto** de la apertura y una etiqueta al final con **el nombre de la noticia de ese día**, por ejemplo `FOMC Meeting Minutes OCT 26` (si hay varias, separadas con `/`; si se marcan todos los días, los que no tienen noticia dicen `Apertura NY (sin noticia) 07 OCT 26`). Como la zona se calcula siempre con la vela M1, se ve igual aunque cambies la temporalidad del gráfico. Solo se marca la apertura de los **días con noticia** (las de importancia alta o, en el modo estudio, la noticia elegida); se puede cambiar con *Marcar la apertura solo en días con noticia*. La zona de la apertura más reciente se extiende hasta la vela en curso; las de días anteriores terminan al cierre (16:00 NY).
- **Las noticias del calendario económico de MT5**, tanto las pasadas como las próximas:
  - cuando la noticia sale, se marca como **zona** el máximo y el mínimo de su vela de 1 minuto, con una etiqueta al final como `PPI m/m SEP 26` (color según importancia: rosa alta, naranja media, amarillo baja);
  - las noticias que aún no salen se ven como línea punteada; las pasadas no llevan línea, solo la zona;
  - al pasar el ratón por la zona o la etiqueta se ve la hora de NY, la previsión, el dato anterior, el dato real y si salió por encima o por debajo de lo esperado.

## Elegir qué noticias se muestran

En los parámetros, grupo **Noticias a mostrar (true = activada)**, hay una casilla por cada noticia importante de EE. UU.: CPI, PPI, nóminas (NFP), ADP, solicitudes de desempleo, JOLTS, decisión de tipos de la Fed, actas del FOMC, Powell, PIB, PCE, ventas minoristas, ISM, confianza del consumidor y bienes duraderos. Las activadas se marcan con su zona, con la apertura de NY de ese día y con alertas, sin importar la importancia que les dé MT5.

- **Otras noticias que contengan**: agrega cualquier otra escribiendo parte de su nombre, separadas con `;`.
- **Ignorar la lista y mostrar TODAS**: en `false` (por defecto) solo se muestran las activadas; en `true` se muestran todas las noticias desde la importancia mínima.
- En `presets/` hay configuraciones listas para cargar con el botón **Cargar** de la ventana de parámetros, por ejemplo `IPC_e_IPP.set` (solo CPI y PPI).
- **Escribir en Expertos todos los nombres**: imprime en la pestaña *Expertos* todas las noticias de la moneda con `[X]` en las que se van a mostrar; sirve para ver los nombres exactos y comprobar que cada casilla atrapa lo que esperas.

MT5 no permite que la lista de parámetros se llene sola con el calendario, por eso es una lista fija; las noticias que no estén ahí se agregan por texto.

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
2. Copiar ahí `ZonasEventosNY_v1.43.mq5`. Conviene borrar las versiones anteriores para no confundirlas.
3. Abrir el archivo en **MetaEditor** (F4 desde MT5) y compilar con **F7**.
4. En MT5, en el Navegador → Indicadores, arrastrar **ZonasEventosNY_v1.43** al gráfico (US30, NAS100, SPX500, etc.). No pongas dos versiones en el mismo gráfico: usan las mismas zonas y se pisan entre sí. En la lista de indicadores (Ctrl+I) aparece como `ZonasEventosNY v1.43`.
5. Revisar la pestaña **Expertos** de la caja de herramientas: el indicador escribe la hora del servidor en que cae la apertura de NY (por ejemplo `16:30`). Compruébalo con una vela real; si no coincide, ajusta el horario del bróker en los parámetros.

Para recibir los avisos en el móvil: **Herramientas → Opciones → Notificaciones**, poner el MetaQuotes ID de la app MT5 del teléfono y activar el parámetro *Enviar también al móvil*.

## Parámetros (ordenados en grupos numerados)

| Grupo | Qué contiene |
| --- | --- |
| **1. Noticias a mostrar** | Una casilla por noticia (CPI, PPI, NFP, Fed, PIB, PCE, ISM…) y *Otras noticias que contengan* para agregar más por texto. |
| **2. Años a proyectar** | *Noticias del año en curso* y *Noticias del año pasado*: se activan o desactivan por separado. *Proyectar las zonas hasta el último minuto*: todas las zonas de esos años se extienden hasta la vela del último minuto, así se ve dónde queda cada nivel respecto al precio actual. |
| **3. Zonas que se dibujan** | Zona de la vela de la noticia, zona de la apertura de NY, apertura solo en días con noticia, vela que forma la zona (M1) y líneas de noticias próximas o pasadas. |
| **4. Colores y estilo** | Colores de las zonas y etiquetas, relleno, grosor y estilo del borde. |
| **5. Avisos** | Alerta al publicarse el dato, preaviso en minutos y envío al móvil. |
| **6. Estudio histórico** | El modo estudio de una noticia en varios años. |
| **7. Horario del bróker y de Nueva York** | Cambio de horario del servidor, desfase manual y hora de apertura (9:30). Normalmente no se tocan. |
| **8. Avanzado** | Moneda, importancia mínima cuando no se usa la lista, largo de las zonas sin proyectar, días de noticias próximas y la opción de escribir en Expertos todos los nombres de noticias. |

Con los dos años activados y proyección, las zonas cubren desde el 1 de enero del año pasado: son unas 700 000 velas de M1, así que *Máx. barras en el gráfico* debe estar en *Ilimitado*. Si no alcanza, la pestaña Expertos lo avisa al cargar.

## Notas

- El calendario usa la hora del servidor del bróker, igual que las velas, así que las líneas caen en la vela correcta.
- El calendario de MT5 no funciona en el Probador de estrategias; el indicador está pensado para el gráfico en vivo.
- Los nombres de las noticias aparecen como los da el calendario de MetaQuotes (normalmente en inglés), por eso el filtro por nombre se escribe en ese idioma.
