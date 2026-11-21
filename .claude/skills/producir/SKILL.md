---
name: producir
description: Produce un video o pieza de contenido con un personaje terminado, coordinando al equipo (director creativo y comercial, jefe de producción, fotografía, animación, prompts, sonido, edición, continuidad). Usar con «/producir <personaje> <idea o clip>», o cuando el dueño pida «haz un video de…», «genera contenido con…», «edita este clip», «replica este video con…», «qué publicamos esta semana».
---

# /producir

Coordinas al equipo de `video-studio/manual/README.md`. Tú hablas con el dueño; los agentes hacen cada oficio.
Nada se genera sin cotización y aprobación del dueño.

## 0. Arranque

**Si el video viene con prompt y carpeta de la conversación «Generador de prompts y carpetas para videos»**
(pedido del dueño, 2026-11-20: el equipo trabaja según los prompts generados), se parte de ese prompt: se copia a
`02_prompt/`, el equipo completa `direccion.md` desde él y solo propone cambios donde choque con el manual o con una
decisión del dueño. Los canales con reglas propias están en `video-studio/canales/` (hoy: `nostalgia-tin-y-tan/`).

1. Identifica **personaje(s)** en `video-studio/personajes/REGISTRO.md`. Si piden a alguien no cargado, dilo y ofrece
   los disponibles. No mezcles públicos (infantil vs. adultos).
2. Identifica el **modo**: A clip propio · B clip para replicar · C desde cero (`manual/06_modos.md`).
3. Pregunta en **una sola vez** solo lo que falte de esto: **objetivo comercial** (monetizar, presencia,
   recordación, comunidad, conversión, viralidad u otra estrategia: lo fija el dueño), plataforma y presupuesto
   máximo. No preguntes lo que ya está en el pedido.
4. Crea el proyecto:
   ```bash
   python3 video-studio/herramientas/nuevo_proyecto.py "<nombre>" [clip] [--serie granja]
   ```
   y llena `00_brief.md` con lo que dijo el dueño.

## 1. Dirección (sin costo)

En este orden, cada agente sobre el mismo proyecto:

| Paso | Agente | Cuándo |
|---|---|---|
| 1 | `analista-de-video` | solo si hay clip (modo A o B) |
| 2 | `director-creativo` | siempre: §1, §2, §8 de `02_prompt/direccion.md` |
| 2b | `pedagoga-montessori` → `guionista-interactivo` → `psicologa-infantil` | solo series infantiles; hasta `APROBADO` |
| 3 | `director-de-fotografia` y `director-de-animacion` | en paralelo: §3 y §4 |
| 4 | `disenador-de-sonido` | §5 |
| 5 | `editor-de-video` | §6 (plan de montaje) |
| 6 | `jefe-de-produccion` | §7: ruta, modelos y presupuesto cotizado |
| 7 | `director-de-prompts` | `prompt.md` validado con `validar_prompt.py` |

Muéstrale al dueño un resumen corto: idea, gancho, emoción por tiempo, tomas, presupuesto y lo que se resuelve en
edición. **Espera su aprobación** antes del paso 2.

## 2. Producción (con costo, por escalones)

1. **Keyframes** con el modelo barato que fijó el jefe de producción. Cotiza, pide aprobación, genera.
   `supervisor-de-continuidad` los revisa contra la carpeta del personaje. Muéstralos al dueño.
2. **Borradores de video** (480p, 5 s, `count: 1`) solo de keyframes aprobados. Revisión del supervisor.
3. **Finales** solo de borradores aprobados.
4. **Audio** (voz, efectos, música si el dueño no la trae).
5. Anota **cada** generación en `costos.md` (modelo, ajuste, créditos, veredicto).

**Un intento por pieza** (regla del dueño, `video-studio/generacion.md`): nada se genera sin `03_keyframes/definicion.md`
cerrada y autorizada; si una pieza sale mal no se repite: se informa qué falló y cuánto cuesta rehacerla. Los cambios que
pide el dueño se abren en `video-studio/cambios/`. Procedimiento completo por fases: `video-studio/MANUAL.md`.

Herramientas que hay que instalar (HyperFrames, Remotion, Earshot, transcripción con tiempos): **solo con el sí del
dueño**. Mientras tanto, la versión simple con `postpro.py` o CapCut.

## 3. Post y entrega (sin costo)

1. `editor-de-video` arma el montaje y las salidas por plataforma (`postpro.py`, `ensamblar.py`).
2. `disenador-de-sonido` mezcla a −14 LUFS.
3. `supervisor-de-continuidad` revisa el final con hoja de contactos a 2 fotogramas por segundo, `postpro.py
   destellos` y las preguntas fijas del cap. 11 → `APROBADO` o `CAMBIOS`. Solo se rehacen los tramos marcados; si cuesta
   créditos, con autorización del dueño.
4. Archiva el prompt (`archivar_prompt.py`), agrega la fila del video a `video-studio/estadisticas/etiquetas.csv`
   y entrega: video final, costo total y qué se mide en la revisión de resultados.
5. Los videos no se suben al repo (es público): quedan en el historial de Higgsfield y en la carpeta del dueño.

## Revisión de resultados

Cuando el dueño traiga estadísticas (o en la fecha de revisión de §8), pásaselas a `director-creativo` para el
informe y las 3 decisiones de la semana (`manual/10_algoritmo_y_monetizacion.md`).
