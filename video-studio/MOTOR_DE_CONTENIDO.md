# Motor de contenido — cómo se arma un universo que se ajusta con estadísticas

> **Origen:** ideas del dueño del 2026-11-26, trabajadas con Tin & Tan. Textual: «en la medida que vayamos generando
> videos todos los elementos los vayas almacenando, por si caben o se quieren reutilizar»; «todas las limitantes que se
> presenten se resuelvan con creatividad […] es parte de la naturaleza del motor: al trabajar con estadísticas debe saber
> ajustarse»; «si el universo es un cuaderno, podrían haber más cuadernos; lo que generamos en Shorts, ¿cómo se transforma
> en un video más largo? […] se vuelve parte de cómo definimos conceptualización, universo de los personajes y contexto
> para el motor […] dejando definido, en caso tomemos otro caso de otros personajes o marcas […], qué es lo que tendríamos
> que definir al principio con otra marca o personajes para aprovechar al máximo el motor».
>
> **Qué es este archivo:** el método, sin secretos de ningún universo. Sirve para Tin & Tan y para cualquier otro
> personaje o marca. El caso de Tin & Tan está en `canales/nostalgia-tin-y-tan/PARAMETROS.md`; la pieza técnica que dibuja
> la acción, en `motor_de_accion/`. El dueño tiene otra conversación llamada «Motor generador de contenido»: cuando
> explique lo que falte, se integra aquí.
>
> **Estado:** versión 0.1. Lo que es método probado lo dice; lo demás es **[hipótesis del equipo]**: hay dos videos
> medidos.

## 1. Las siete capas

Cada capa se define una vez, se guarda y se ajusta con datos. Ninguna se da por cerrada.

| # | Capa | Qué decide | Dónde vive (Tin & Tan) | Qué la ajusta |
|---|---|---|---|---|
| 1 | **Estadísticas y demanda** | A quién se le habla, qué busca, cuándo y desde dónde | `estadisticas/datos/` (no se sube), `comercial/radar_de_tendencias.md`, calendario de temporadas por país | Cada lectura de Studio; autocompletado y Trends antes de fijar una pregunta |
| 2 | **Conceptualización** | La metáfora que contiene todo (el «contenedor») y sus reglas | Biblia del universo (privada) | Limitantes y hallazgos: se resuelven dentro de la metáfora |
| 3 | **Personajes** | Quiénes son, qué no cambia nunca, quién es el rival o conflicto | `personajes/` | Solo el dueño cambia identidad; lo demás, variaciones permitidas |
| 4 | **Forma** | Cómo se cuenta: acción, pelea, tiempos, cámara, sonido | `PARAMETROS.md` sección 7; estudios de referencia | Retención por segundo; se quedó a mirar |
| 5 | **Biblioteca** | Todo elemento hecho: paletas, entornos, utilería, efectos, sonidos, poses, guiones | `motor_de_accion/catalogo.json` | Se añade tras cada video; nada se borra, se retira |
| 6 | **Conexión y plan** | Qué une un video con otro; tandas de 15 días a un mes; formatos por duración | Registro de pistas y plan de tanda (privados) | Regresos, suscriptores, comentarios; el tema entra tarde desde el radar |
| 7 | **Adaptación** | Qué se hace cuando algo falla o cambia | `PARAMETROS.md` sección 9 | Es la capa que mueve a las demás |

## 2. El contenedor: una metáfora con escalas

Un universo aguanta cualquier tema si su metáfora tiene **escalas**: cada tamaño de contenido es una unidad de la
metáfora. En Tin & Tan la metáfora es el papel:

| Escala | En el mundo real | En el universo de Tin & Tan | Formato |
|---|---|---|---|
| La unidad mínima | Un Short | **Una página** | 9:16, hasta ≈ 30 s |
| La unidad abierta | Un video largo | **El cuaderno abierto en doble página** (dos páginas lado a lado: por eso es horizontal) | 16:9, varios minutos |
| El universo alterno | Un tono o tipo de tema | **Una hoja** de otro papel (una por paleta) | cualquiera |
| La tanda | 15 días a un mes de producción | **Un cuadernillo** cosido: lo que se siembra y se cobra junto | — |
| La línea de contenido | Una serie, una temporada o un tema mayor | **Un cuaderno** | — |
| Todo lo del dueño o de la marca | Varios canales, personajes o marcas | **El estante**: cuadernos distintos que pueden prestarse hojas | — |

Reglas del contenedor:

1. **Lo corto y lo largo son la misma historia a otra escala.** El Short muestra una página; el video largo abre el
   cuaderno y deja ver lo que la página sola no muestra: cómo se tocan las páginas, qué quedó en los márgenes, por qué
   pasó lo que pasó. Un video largo nunca es un pegado de Shorts (política de contenido reutilizado): es la doble página.
2. **Para qué sirve el video largo:** (a) explicar el universo a quien ya vio varias páginas; (b) explicar con
   estadísticas un escenario actual de la realidad que no cabe en 30 segundos (varios asaltos, varias fuentes); (c) abrir
   el camino de horas del Programa de socios. Cuándo empieza lo decide el dato (regresos, comentarios), no el calendario.
3. **Más cuadernos:** cuando un tema mayor, una temporada u otro personaje no quepa en el cuaderno actual, se abre otro.
   Cada cuaderno tiene sus reglas; el estante dice cuáles pueden cruzarse. **Lo infantil está en otro estante y nunca se
   cruza** (regla del dueño).
4. **Toda limitante se traduce a la metáfora** (capa 7): un video sin distribución es una página arrancada; un orden
   roto, un cuaderno desencuadernado; un remake, pasar en limpio.

Otra marca u otros personajes no usan el papel: eligen **su** metáfora con el mismo criterio (sección 4, punto 5).

## 3. El ciclo de cada video

1. **Leer** estadísticas y demanda (capa 1). La pregunta del video se valida en datos de búsqueda, no en que existan
   videos parecidos.
2. **Recorrer el repertorio de ajustes** (capa 7): ¿algo cambió o falló desde el último video?
3. **Elegir** tema, paleta y entorno; decir qué conexión se cobra y cuál se siembra (capas 5 y 6).
4. **Brief** que abre con «Estadísticas en que se basa»; prompt validado; prueba completa (ninguna prueba a medias).
5. **Producir** con lo que haya en la biblioteca; lo nuevo entra al catálogo.
6. **Publicar** con el sí del dueño; **medir** a 48 horas, 7 días y 28 días.
7. **Ajustar** parámetros y universo con el dato, y anotarlo.

## 4. Qué hay que definir al principio con otra marca u otros personajes

La plantilla para llenar está en `plantillas/arranque_de_universo.md`. En resumen, antes del primer video:

| # | Qué | Por qué no se puede saltar |
|---|---|---|
| 1 | **Objetivo comercial** con métrica, meta y plazo | Todo se justifica contra él |
| 2 | **Accesos a los datos**: quién lee las estadísticas, cada cuánto y dónde se guardan | Sin dato no hay prompt |
| 3 | **Público y países reales** (o la hipótesis, marcada como hipótesis) y su calendario de temporadas | Tema, horario, idioma y color salen de aquí |
| 4 | **Lo que no se mueve**: identidad, manual de marca, tono, lo legal, lo que la marca no dice nunca, línea editorial | Es el borde de la creatividad |
| 5 | **La metáfora contenedora** y sus escalas (corto, largo, universo alterno, tanda, línea, estante) | Es lo que permite conectar y crecer |
| 6 | **Personajes**: quiénes, rasgos fijos, hoja de personaje, y **el conflicto o rival** (qué se enfrenta en cada pieza) | Sin conflicto no hay acción ni serie |
| 7 | **La firma**: lo que se repite en todos los videos y une uno con el siguiente | Reconocimiento y primera conexión |
| 8 | **La forma**: referencias medidas cuadro a cuadro, nivel de intensidad permitido, idioma, subtítulos | «Parecido a» sin medir es adivinar |
| 9 | **Paletas por tema**, con estudio de color sobre el público real | El color también se justifica |
| 10 | **Qué se promete y cómo se comprueba**: fuentes, qué se afirma y qué no | Confianza y políticas |
| 11 | **Canales y permisos**: cuentas, verificación, funciones disponibles, quién publica | Define qué conexiones existen |
| 12 | **Dinero y herramientas**: créditos, qué se puede instalar, en qué máquina se produce | Ruta de producción |
| 13 | **Quién decide qué** y qué necesita el sí del dueño o de la marca | Evita rehacer |
| 14 | **Dónde viven los secretos** del universo (nunca en un repositorio público) | Las teorías dependen de eso |
| 15 | **Qué se hereda del estante**: elementos de la biblioteca que sirven tal cual y cuáles nunca se cruzan | Aprovechar lo ya hecho |

Lo que el motor ya trae hecho y una marca nueva puede usar desde el primer día: el método de validación de preguntas, el
esqueleto de personajes 2D en mundo 3D, los efectos de acción, el sonido por código, la gramática de golpe medida, el
formato de biblia, registro de pistas y plan de tanda, el repertorio de ajustes y los controles de calidad.

## 5. Lo que no sé todavía

- Si las conexiones entre videos convierten en regresos y suscriptores: no hay ningún video conectado publicado.
- Cuánto del método sirve para una marca comercial con productos reales (logotipos, precios, promesas de venta): el caso
  de Tin & Tan no tiene nada de eso.
- Cómo se une esto con lo que el dueño llama «Motor generador de contenido» en su otra conversación.
