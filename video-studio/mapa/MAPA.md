# Mapa del estudio

> Generado por `herramientas/mapa.py` desde `mapa/grafo.json` · actualizado: 2026-11-27 · 49 nodos, 80 relaciones.
> **Léelo antes de buscar en archivos.** Para cambiarlo se edita `grafo.json` y se vuelve a generar.

## 1. Nodos centrales (los más conectados)

| Nodo | Tipo | Relaciones | Dónde está | Estado |
|---|---|---|---|---|
| Motor de contenido | metodo | 13 | `video-studio/MOTOR_DE_CONTENIDO.md` | versión 0.4 (añade la puntuación de nicho y subnicho, sección 7b) |
| Universo de Tin & Tan (biblia, registro de pistas, plan de tanda, decisiones) | universo | 12 | `Drive «Canal YouTube - Entregas» (privado)` | versión 0.1, aprobado en lo principal |
| Método del Generador de prompts | metodo | 8 | `video-studio/metodo/1_generador_de_prompts.md` | versión 0.1 |
| Puntuación de nicho y subnicho | metodo | 8 | `video-studio/MOTOR_DE_CONTENIDO.md sección 7b` | pesos, escalas y cortes son hipótesis; una sola aplicación |
| Parámetros de Tin & Tan | canal | 7 | `video-studio/canales/nostalgia-tin-y-tan/PARAMETROS.md` | versión 2.3 |
| Lectura de Studio del 2026-11-26 | dato | 7 | `video-studio/estadisticas/datos/ (no se sube)` | dos videos medidos |
| Short 4 | video | 7 | — | pregunta aprobada; sin brief ni prompt; primera página de la tanda 01 |
| Motor de acción (escena 3D por código) | herramienta | 7 | `video-studio/motor_de_accion/` | funciona; guion aún dentro de la escena |
| Keter (PC del dueño) | conversacion | 5 | — | Studio, Trends, descargas, publicación, Cerebro |
| Catálogo de elementos | biblioteca | 5 | `video-studio/motor_de_accion/catalogo.json` | al día al 2026-11-26 |

## 2. La cadena de trabajo

- **Motor de contenido** (`video-studio/MOTOR_DE_CONTENIDO.md`): entrega a Método del Generador de prompts; usa Lectura de Studio del 2026-11-26; usa Datos de búsqueda del short 4 (Trends, autocompletado); usa Radar de tendencias; usa Calendario de temporadas por país; filtra con Políticas y funciones de YouTube; coloca cada video en Universo de Tin & Tan (biblia, registro de pistas, plan de tanda, decisiones); se replica con Arranque de universo (otra marca o personajes); incluye Puntuación de nicho y subnicho.
- **Método del Generador de prompts** (`video-studio/metodo/1_generador_de_prompts.md`): entrega a Método de producción audiovisual; pide personajes a Método del Creador de personajes; llena Brief del proyecto; usa Pedido de personaje.
- **Método del Creador de personajes** (`video-studio/metodo/3_creador_de_personajes.md`): entrega a Método del Generador de prompts; recibe Pedido de personaje.
- **Método de producción audiovisual** (`video-studio/metodo/2_produccion_audiovisual.md`): devuelve mediciones a Motor de contenido.

## 3. Pendientes (nodos cuyo estado lo dice)

| Nodo | Estado | De qué depende |
|---|---|---|
| Ciudad de cartón | de relleno | — |
| Alternativas de producción | alternativa 4 en prueba | dio lugar a Prueba del mundo 3D (alternativa 4) |
| Tema del short 4 | aprobado por el dueño: «What is GTA 6?»; faltan los hechos con fuente | define Short 4; se validó con Datos de búsqueda del short 4 (Trends, autocompletado) |
| Short 4 | pregunta aprobada; sin brief ni prompt; primera página de la tanda 01 | necesita un entorno nuevo en Motor de acción (escena 3D por código); espera el sí de El dueño |
| Prueba del mundo 3D (alternativa 4) | incompleta: le faltan pedidos; clip generado detenido | usa Motor de acción (escena 3D por código); necesita los tiempos de Referencias de pelea medidas cuadro a cuadro |
| PC de escritorio con GTX 1070 Ti | sin conectar; por validar | aceleraría Motor de acción (escena 3D por código) |
| Graphify (mapa estructural) | instalado el 2026-11-26; pasada de significado sin hacer | da el mapa estructural a Motor de contenido |
| Temas de diciembre puntuados (tanda 01) | entregada al Generador; faltan hechos de cinco temas y lecturas de Trends | usa Autocompletado de YouTube en EE. UU., Filipinas e India (2026-11-26); se entrega a Método del Generador de prompts; califica los temas de Calendario de temporadas por país |

## 4. Por tipo

- **biblioteca:** Catálogo de elementos (`video-studio/motor_de_accion/catalogo.json`)
- **canal:** Parámetros de Tin & Tan (`video-studio/canales/nostalgia-tin-y-tan/PARAMETROS.md`)
- **comercial:** Radar de tendencias (`video-studio/comercial/radar_de_tendencias.md`); Calendario de temporadas por país (`video-studio/comercial/2026-11-26_calendario_de_temporadas_por_pais.md`); Tema del short 4 (`video-studio/comercial/2026-11-26_tema_short4_tin_y_tan.md`); Potencial de pago por nicho (`video-studio/comercial/2026-11-27_potencial_de_pago_por_nicho.md`); Temas de diciembre puntuados (tanda 01) (`video-studio/comercial/2026-11-27_puntuacion_de_nichos_tanda_01.md`)
- **conversacion:** Generador de prompts; Equipo de producción audiovisual; Creador de personajes; Keter (PC del dueño); Motor generador de contenido
- **dato:** Lectura de Studio del 2026-11-26 (`video-studio/estadisticas/datos/ (no se sube)`); Datos de búsqueda del short 4 (Trends, autocompletado) (`video-studio/estadisticas/datos/ (no se sube)`); Autocompletado de YouTube en EE. UU., Filipinas e India (2026-11-26) (`video-studio/comercial/2026-11-27_puntuacion_de_nichos_tanda_01.md sección 5`)
- **entorno:** Ciudad de cartón (`video-studio/motor_de_accion/entornos/ciudad_de_carton.js`)
- **estudio:** Acción de palitos y políticas de YouTube (`video-studio/estudios/2026-11-26_accion_stickman_y_tin_y_tan.md`); Referencias de pelea medidas cuadro a cuadro (`video-studio/estudios/2026-11-26_referencias_de_pelea_estudio_de_keter.md`); Color por estadísticas y psicología (`video-studio/estudios/2026-11-26_color_por_estadisticas_y_psicologia.md`); Investigación del universo conectado (`video-studio/estudios/2026-11-26_universo_conectado_investigacion.md`); Alternativas de producción (`video-studio/estudios/2026-11-26_formato_de_accion_alternativas.md`)
- **herramienta:** Motor de acción (escena 3D por código) (`video-studio/motor_de_accion/`); Graphify (mapa estructural) (`video-studio/graphify-out/GRAPH_REPORT.md`)
- **metodo:** Motor de contenido (`video-studio/MOTOR_DE_CONTENIDO.md`); Método del Generador de prompts (`video-studio/metodo/1_generador_de_prompts.md`); Método de producción audiovisual (`video-studio/metodo/2_produccion_audiovisual.md`); Método del Creador de personajes (`video-studio/metodo/3_creador_de_personajes.md`); Puntuación de nicho y subnicho (`video-studio/MOTOR_DE_CONTENIDO.md sección 7b`)
- **paleta:** A · Papel con fondo frío (hoja Día) (`video-studio/motor_de_accion/paletas/a_papel_con_fondo_frio.json`); B · Noche de tinta (hoja Noche) (`video-studio/motor_de_accion/paletas/b_noche_de_tinta.json`); C · Alto voltaje (hoja Voltaje) (`video-studio/motor_de_accion/paletas/c_alto_voltaje.json`)
- **pendiente:** PC de escritorio con GTX 1070 Ti
- **persona:** El dueño
- **personaje:** Tin (`video-studio/personajes/tin/ficha.md`); Tan (`video-studio/personajes/tan/ficha.md`); El rival (la duda) (`video-studio/personajes/duda/ficha.md`)
- **plantilla:** Arranque de universo (otra marca o personajes) (`video-studio/plantillas/arranque_de_universo.md`); Pedido de personaje (`video-studio/plantillas/pedido_de_personaje.md`); Brief del proyecto (`video-studio/plantillas/proyecto/00_brief.md`)
- **plataforma:** Políticas y funciones de YouTube (`video-studio/MOTOR_DE_CONTENIDO.md sección 5b`)
- **prueba:** Prueba del mundo 3D (alternativa 4) (`video-studio/canales/nostalgia-tin-y-tan/pruebas/2026-11-26_accion_mundo_3d/informe.md`)
- **regla:** Reglas del dueño (`CLAUDE.md`); Reglas para el Cerebro (`video-studio/REGLAS_CEREBRO.md`); Firma del lápiz bumerán (`video-studio/canales/nostalgia-tin-y-tan/FIRMA_LAPIZ_BUMERAN.md`)
- **universo:** Universo de Tin & Tan (biblia, registro de pistas, plan de tanda, decisiones) (`Drive «Canal YouTube - Entregas» (privado)`)
- **video:** Short 1 · casete (`video-studio/proyectos/2026-11-21_tin_y_tan_casete_y_lapiz`); Short 2 · GTA 6 (`video-studio/proyectos/2026-11-21_tin_y_tan_gta6`); Short 3 · Jensen Huang (`video-studio/proyectos/2026-11-24_tin_y_tan_jensen_huang`); Short 4

## 5. Sueltos e hipótesis

- Nodos sin ninguna relación: ninguno.
- Relaciones que son hipótesis, no hechos: PC de escritorio con GTX 1070 Ti aceleraría Motor de acción (escena 3D por código); Puntuación de nicho y subnicho se revisa cada 5 videos con las mediciones de Método de producción audiovisual.
