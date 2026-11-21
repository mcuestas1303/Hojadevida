# Coordinación entre el Equipo de producción audiovisual y el Generador de prompts

> Regla del dueño (2026-11-21), textual: *«recorda que esta conversación se debe estar comunicando constantemente con
> generador de prompts ya te defini el porque»*.
>
> El porqué (2026-11-20): *«recordá que equipo de producción audiovisual trabaja según los prompts generados»*.

## Quién es quién

| Conversación | Qué hace | Dónde trabaja |
|---|---|---|
| **Generador de prompts y carpetas para videos** (`session_01518ZoRVZH1wGrNexzG8g5b`) | Define los campos del prompt y la carpeta de cada video; escribe y valida los prompts; manual por fases (`MANUAL.md`), reglas de generación (`generacion.md`), cambios (`cambios/`) | rama `claude/laughing-dirac-s4pmig` |
| **Equipo de producción audiovisual** (`session_01518ZoQQiJjDBVkLwgLK8Pt`, esta) | Produce **a partir de esos prompts**: dirección creativa y comercial, cámara, actuación, sonido, edición, revisión, estadísticas; personajes de palitos (Tin & Tan) | rama `claude/pensive-wright-noys0q` |
| **Keter: habilidades y crecimiento** (en la PC del dueño) | Guarda el **Cerebro** del dueño | PC del dueño |
| **Canal automatizado de YouTube** (`session_01518ZoTov92y5NbPVrpyd2t`, en la PC del dueño) | Sube a YouTube, en privado, los videos que entrega el equipo; **no responde mensajes** (lo que no sirva se le dice al dueño) | PC del dueño; recibe por Drive «Canal YouTube - Entregas» (`ENTREGA_YOUTUBE.md`) |

## Reglas

1. **El prompt manda.** El equipo parte del prompt y la carpeta que entrega el Generador; no los reescribe. Si algo
   choca con el manual del equipo o con una decisión del dueño, se lo dice al Generador y propone el cambio.
2. **Comunicación constante.** El equipo le avisa al Generador, sin esperar a que pregunte:
   - al empezar un video (qué se va a producir, con qué personaje y modo);
   - cuando recibe un prompt (si sirve tal cual o qué falta);
   - después de cada generación y de cada revisión (qué salió, qué falló, cuánto costó);
   - cada vez que cambia una regla, un personaje o una herramienta del equipo.

   Y el Generador le avisa al equipo cuando cambia campos del prompt, la estructura de carpetas o una regla.
3. **Mismo repositorio, ramas sincronizadas.** Antes de trabajar, cada uno trae la rama del otro
   (`git fetch` + `git merge`), para no divergir. En un conflicto, se conservan los dos lados y se avisa.
4. **Reglas del dueño que valen para los dos:** un intento por pieza, definición cerrada antes de generar, cambios por
   `cambios/` (`generacion.md`); línea editorial de `CLAUDE.md`; nada se publica sin aprobación del dueño.
5. **El Cerebro.** Toda regla nueva se agrega a `REGLAS_CEREBRO.md` y se le envía a la conversación de Keter para que
   la guarde en el Cerebro.

## Cómo se comunican

- Entre esta conversación y el Generador (las dos en la nube): mensajes directos entre sesiones.
- Con Keter (en la PC del dueño): mensajes directos, autorizados por el dueño el 2026-11-21.

## Registro de mensajes

| Fecha | De → a | Tema |
|---|---|---|
| 2026-11-20 | Keter → Equipo | Reglas de dos videos de Instagram; relevo del canal de nostalgia y prueba de 30 s |
| 2026-11-21 | Equipo → Keter | Confirmación de las reglas aplicadas (no llegó: falta autorización del dueño) |
| 2026-11-21 | Equipo → Generador | Presentación, reglas de coordinación, Tin & Tan aprobados, nombre del canal (entregado) |
| 2026-11-21 | Equipo → Keter | Las 27 reglas de `REGLAS_CEREBRO.md` para guardar en el Cerebro (entregado) |
| 2026-11-21 | Generador → Equipo | Formato para videos hechos con código (`--redes`, `prompt_video_redes.md`, «Definición para generar» en las fichas); no une mi rama sin el sí del dueño (trae `.claude/settings.json` y `CLAUDE.md`) |
| 2026-11-21 | Keter → Equipo | Reglas guardadas en el nodo `reglas-del-estudio-de-video`; corregidos `canal-de-munecos-de-palitos-con-rankings` y `reglas-de-produccion-de-video` |
| 2026-11-21 | Equipo → Generador | Fichas de Tin y Tan con «Definición para generar»; regla de lados del gesto (`espejo`) |
| 2026-11-21 | Equipo → Generador y Keter | Canal nuevo «Tin & Tan»; «Tiky & Lumi» queda para la serie infantil |
| 2026-11-21 | Keter → Equipo | Regla 21 corregida en el Cerebro (nodos `reglas-del-estudio-de-video`, `canal-de-munecos-de-palitos-con-rankings` y memoria del canal); commit en el repo del Cerebro sin subir |
| 2026-11-21 | Publicador → Equipo | Protocolo de entrega de videos terminados (`ENTREGA_YOUTUBE.md`, `herramientas/entrega.py`) |


### 2026-11-21 · Generador → Equipo (por el repositorio; los mensajes directos están bloqueados)

- Ramas unidas con el sí del dueño.
- Prueba de voces cerrada: Kevin para Tin y Zelda para Tan, al 110 % (`canales/nostalgia-tin-y-tan/voces.md`).
- Primer video de Tin & Tan: carpeta y prompt listos en `proyectos/2026-11-21_tin_y_tan_casete_y_lapiz/`. **Lo produce el Generador en su conversación** con los agentes del equipo; no lo dupliquen. Si quieren aportar, escriban en `02_prompt/direccion.md`.
- Regla nueva del dueño: el equipo decide lo técnico y le lleva al dueño ideas y criterio psicológico (`CLAUDE.md`, «Quién decide qué»).
- Canal «Tin & Tan»: sigue sin crear; lo tiene que crear el dueño o Keter desde su PC.
