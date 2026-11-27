# Método del Generador de prompts — del resultado del motor al paquete de prompt

> **Origen:** pedido del dueño (2026-11-26): «defíneme el método [para] tomar el resultado del motor y generar el prompt y
> los elementos del entregable del Generador de prompts con lo que hemos trabajado hasta ahorita, con base al universo».
> Sigue a `video-studio/MOTOR_DE_CONTENIDO.md` (pasos 1 a 9) y entrega a `metodo/2_produccion_audiovisual.md`.
> Versión 0.1. Probado en parte: los pasos existen desde antes; el orden y las bifurcaciones son de hoy.

## 1. Qué recibe: el resultado del motor

El Generador no empieza sin estas seis cosas. Si falta una, la pide; no la supone.

| # | Entrada | De dónde sale |
|---|---|---|
| E1 | Lectura vigente de estadísticas del canal | `estadisticas/datos/` (motor, paso 1) |
| E2 | Tema y pregunta validada, con sus hechos y fuentes | Definición del tema (motor, sección 7) |
| E3 | Filtro de políticas de YouTube pasado, renglón por renglón | Motor, sección 5b |
| E4 | Fecha límite y lugar en la tanda | Calendario de temporadas y plan de tanda |
| E5 | Lugar en el universo: hoja y paleta, entorno, conexión que cobra y que siembra, ajuste que aplica | Biblia, registro de pistas, repertorio de ajustes (privados) |
| E6 | Requisitos vigentes del formato y lo que no se mueve | `PARAMETROS.md` del canal |

## 2. Los pasos

| Paso | Qué hace | Quién | Sale |
|---|---|---|---|
| G1 | **Abrir el proyecto** con `nuevo_proyecto.py` y llenar el brief (estadísticas, tema, estrategia, universo, requisitos) | Generador | `00_brief.md` |
| G2 | **Inventario de piezas:** recorrer lo que el video necesita y marcar cada pieza como «existe en la biblioteca», «se adapta» o «no existe» | Generador, con `motor_de_accion/catalogo.json` y `personajes/REGISTRO.md` | Tabla de piezas en el brief |
| G3 | **Resolver lo que no existe** con la tabla de bifurcaciones (sección 4). Lo que bloquea se pide antes de seguir | Generador | Pedidos a otras conversaciones |
| G4 | **Dirección:** público, emoción y arco; guion por segundos con el dato fuerte antes del segundo 5; coreografía con los tiempos de golpe medidos; cámara; color; sonido | `director-creativo`, `director-de-fotografia`, `director-de-animacion`, `disenador-de-sonido` | `02_prompt/direccion.md` |
| G5 | **Fichas:** técnica (objetivos y requisitos uno por uno), perfil emocional, publicación con título y fuentes | `director-creativo`, `comercial-inteligencia-digital` | `ficha_tecnica.md`, `perfil_emocional.md`, `publicacion.md`, `ficha.json` |
| G6 | **Universo:** escribir la conexión que cobra y la que siembra (segundo y zona de pantalla) y anotar la fila en el registro de pistas | Generador, `supervisor-de-continuidad` | Sección del brief; registro (privado) |
| G7 | **Prompt:** el texto de producción, con elenco, entorno, paleta, tiempos y lo que no debe verse | `director-de-prompts` | `02_prompt/prompt.md` |
| G8 | **Controles:** `validar_prompt.py`, `revisar_texto.py`, `revisar_titulo.py`, filtro de políticas otra vez sobre el guion final, control «se entiende solo» | `director-de-prompts`, `supervisor-de-continuidad` | 0 errores, firmas |
| G9 | **Presentar al dueño** el prompt y las fichas (en esta conversación solo se ven prompts y fichas) | Generador | Su sí, o sus ajustes por `cambios/` |
| G10 | **Archivar y entregar:** `archivar_prompt.py`; aviso en `COORDINACION.md` con la ruta | Generador | Paquete entregado al equipo de producción |

## 3. El entregable: el paquete de prompt

| # | Pieza | Archivo | Bloquea si falta |
|---|---|---|---|
| P1 | Brief con «Estadísticas en que se basa», tema validado, estrategia, universo y requisitos | `00_brief.md` | Sí |
| P2 | Dirección | `02_prompt/direccion.md` | Sí |
| P3 | Ficha técnica (rúbrica) | `02_prompt/ficha_tecnica.md` | Sí |
| P4 | Perfil emocional | `02_prompt/perfil_emocional.md` | Sí |
| P5 | Prompt validado | `02_prompt/prompt.md` | Sí |
| P6 | Publicación: título con su ficha, descripción con fuentes, portada, etiquetas | `publicacion.md`, `ficha.json` | Sí |
| P7 | Guion de voz y subtítulos (idioma del canal y traducción) | dentro de la dirección; `subtitulos_*.srt` los hace producción | Sí |
| P8 | Lista de piezas: qué se reutiliza de la biblioteca, qué se adapta, qué se construye, con quién lo hace | tabla en el brief | Sí |
| P9 | Pedidos abiertos a otras conversaciones y su estado | `COORDINACION.md` | Sí, si alguno bloquea |
| P10 | Definición de generación, si alguna pieza se genera con créditos: modelo, imagen de arranque, costo cotizado | `03_keyframes/definicion.md` | Solo si hay generación |
| P11 | Licencias y costos previstos | `licencias.md`, `costos.md` | Sí |
| P12 | Fila del registro de pistas y entrada prevista del catálogo | privados y `catalogo.json` | Sí, si el canal tiene universo |

## 4. Bifurcaciones: qué pasa cuando el prompt pide algo que no existe

| Si el prompt necesita… | y no existe… | Se le pide a | Qué se le entrega | Qué devuelve | ¿Bloquea el prompt? |
|---|---|---|---|---|---|
| Un **personaje** | no está en `personajes/REGISTRO.md` | **Creador de personajes** (`metodo/3_creador_de_personajes.md`) | Pedido de personaje (`plantillas/pedido_de_personaje.md`): papel en el universo, público, qué hace en el video, restricciones, cómo se dibuja, fecha | Ficha, hoja aprobada por el dueño, fila en el registro, dibujo en el motor | **Sí** |
| Una variación de un personaje (pose, objeto, expresión) | no está en su ficha | Creador de personajes, o el equipo si es variación permitida | Qué variación y para qué plano | Ficha actualizada | Sí, si toca un rasgo fijo |
| Un **entorno** | no hay uno del tema en el catálogo | Equipo de producción (motor de acción) | Tema, lugar, paleta, qué se rompe, qué pista aloja | `entornos/<id>.js` y entrada del catálogo | No: se construye en producción |
| Una **paleta** | las aprobadas no sirven al tema | `director-de-fotografia`, con estudio | Tema, público, por qué no sirve ninguna | Paleta con medidas y su porqué; el dueño la aprueba | Sí |
| Un **efecto o sonido** | no está en la biblioteca | Equipo de producción | Qué comunica, emoción, referencia medida | Función o sonido nuevo y entrada del catálogo | No |
| Una **forma de moverse** | no hay referencia medida | Keter, con autorización del dueño | Qué video y qué medir | Informe cuadro a cuadro en el Drive | Sí, si el dueño pidió parecido a una referencia |
| Un **dato** | no tiene fuente abierta | `comercial-inteligencia-digital`, o permiso de red, o Keter | El dato y dónde debería estar | Fuente con fecha, o «sin dato» | **Sí**: sin fuente no se afirma |
| Una **pregunta** | no está validada en búsqueda | Motor (pasos 3 y 4) | Los candidatos | Lista de consultas | **Sí** |
| Una **regla del universo** | la biblia no la tiene o la contradice | Dueño, vía `cambios/` | La regla propuesta y qué toca | Su decisión | Sí |
| Una **función de la plataforma** (series, comentario fijado, miniatura) | el canal no la tiene | Regla de adaptación | — | La conexión se lleva dentro del video | No |
| **Créditos** para generar una pieza | no están aprobados | Dueño | Cotización con modelo y número | Su sí para esa pieza | Solo esa pieza |
| Una **herramienta** | no está instalada | Dueño | Qué es y para qué | Su sí | Depende |

Regla general: **lo que toca identidad, hechos o reglas del universo bloquea; lo que es construcción (entorno, efecto,
sonido) viaja como pedido dentro del paquete.**

## Dónde termina este método (dueño, 2026-11-26)

En la entrega del paquete de prompt validado a producción, anotada en `COORDINACION.md`. El Generador no genera voz, no
construye en el motor, no renderiza y no presenta piezas: eso es el método 2, del Equipo de producción audiovisual.

