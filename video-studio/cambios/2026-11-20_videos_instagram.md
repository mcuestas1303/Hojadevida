# Solicitud de cambio — lo que enseñan dos videos de Instagram

- **Fecha:** 2026-11-20
- **Pedido del dueño, textual** (llegó por la conversación «Keter: habilidades y crecimiento»): «Lo que dice en los ultimos 2 videos necesito que se implemente en el equipo creativo de producción y en generador de prompts lo que aplique».
- **Videos:** desglose de un video viral (willrvail) y estudio de gráficos animados con código (silvesttre.ai). Esta conversación no los vio: trabajó con el resumen que envió la otra. Nada de lo que afirman está probado con datos.
- **Estado:** PRESENTADA AL DUEÑO

## Qué se aplicó ya (no toca nada definido, 0 créditos)

| Idea del video | Qué se hizo | Dónde |
|---|---|---|
| Revisar los propios fotogramas y marcar los «muertos» | Herramienta que marca imagen congelada, fotogramas vacíos, destellos de más y planos demasiado cortos | `herramientas/revisar_fotogramas.py`; resultados en `07_revision/` de cada proyecto |
| No más de 3 destellos por segundo | Lo comprueba la misma herramienta | Igual |
| Origen y licencia de cada recurso | Registro por proyecto | `licencias.md` en cada proyecto |
| Campos de un prompt para redes (gancho, mapa de ritmo, motivo que vuelve, cierre en bucle, sistema de diseño, texto con posición en %, golpes de sonido atados a cortes, un solo llamado a la acción) | Plantilla aparte para contenido de adultos y redes | `plantillas/prompt_video_redes.md`; se crea con `nuevo_proyecto.py <nombre> --redes` |
| Restricciones críticas al inicio del prompt y tiempos al décimo de segundo | Incluidas en esa plantilla | Sección 10 y 11 de la plantilla de redes |
| No reutilizar metraje ajeno | Ya era regla del estudio | `README.md`, `licencias.md` |

## Qué NO se aplica a la serie infantil, y por qué

| Idea del video | Choca con | Quién lo decidió antes |
|---|---|---|
| Arrancar con 4 cortes en 0,6 s; ráfagas de cortes; unos 52 cambios en 30 s | Guía de 1 a 3 años, sección 7: cada plano dura 6 s o más, cámara fija o lenta, un solo foco | Psicóloga y pedagoga |
| Gancho en el primer segundo | Guía, sección 1: sin ganchos para seguir mirando | Psicóloga (veto a retocar el inicio del short) |
| Final que repite el inicio para encadenar en bucle | Veto de la psicóloga al short que se repite sin fin; la despedida debe cerrar de verdad | Psicóloga |
| Destellos, transiciones con desenfoque, obturador lento | Guía, sección 7: corte directo o fundido lento, sin efectos | Psicóloga |
| Subtítulos y texto en pantalla | Guía, sección 7: ningún texto (el público no lee); además permite usar el mismo video en tres idiomas | Pedagoga |
| Llamado a la acción | «Hecho para niños»: no se pide suscribir ni comentar | Comercial y psicóloga |

Estas ideas sí sirven para lo que le habla al **adulto**: los reels y carruseles de Instagram para padres, una posible línea para padres, y los personajes que no son infantiles (Spike, «M», Lumi Bravo).

## Qué queda por decidir

| Tema | Opciones | Costo |
|---|---|---|
| Motor de gráficos por código (el video se dibuja fotograma a fotograma, sin créditos de generador) | (a) probar HyperFrames, que ya trae el motor y el ciclo de revisión: hay que instalarlo; (b) hacer uno propio con el navegador y FFmpeg que ya están en este entorno; (c) no hacerlo ahora | 0 créditos en los tres casos; (a) necesita tu permiso para instalar |
| Para qué se usaría primero | Piezas para adultos en Instagram (carruseles animados, reels explicativos) y títulos o cortinillas; en la serie infantil solo serviría para tomas sin personajes | — |
| Añadir las «restricciones críticas» al inicio de cada prompt de video de «Hola, granja» antes de generar los clips | Sí o no. Es texto, no cambia el guion; lo revisaría el director de prompts | 0 créditos |
| Estructura de carpetas del resumen (01_brief … 09_publicacion) | El estudio ya tiene la suya y las herramientas dependen de ella. Se agregó lo que faltaba (`07_revision/`, `licencias.md`); no se renumeró | 0 créditos |

## Opinión del equipo

| Quién | Opinión | Condiciones |
|---|---|---|
| Coordinación | Aplicar a contenido de adultos; no tocar el ritmo ni la estructura de la serie infantil | Lo ya dictaminado por la psicóloga se mantiene |
| psicologa-infantil | Ya dictaminó en `series/granja/estrategia_monetizacion.md` y en la revisión de los guiones: sin ganchos, sin bucles, planos de 6 s o más | — |

## Decisión del dueño

pendiente: motor de gráficos por código y restricciones críticas en «Hola, granja».
