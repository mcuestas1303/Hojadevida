# Traspaso: Equipo de producción audiovisual → conversación en el PC del dueño

> Pedido del dueño (2026-11-27): «todo lo que estaba en las conversaciones de equipo audiovisual lo pases para ahí».
> Desde hoy, el Equipo de producción audiovisual trabaja en **una sola conversación, la del PC del dueño**. Las
> anteriores («Equipo de producción audiovisual», «… (escritorio)» y «… PC», esta última en la nube) quedan cerradas.

## Primer paso en la conversación nueva

```bash
git fetch origin claude/pensive-wright-noys0q claude/laughing-dirac-s4pmig
```

```bash
git checkout claude/pensive-wright-noys0q
```

Después lee, en este orden: `CLAUDE.md`, `video-studio/REGLAS_CEREBRO.md`, `video-studio/COORDINACION.md` (registro
de mensajes completo), `video-studio/manual/12_controles_de_calidad.md`, `13_color_con_intencion.md` y este archivo.
Todo lo que pasó en las conversaciones anteriores está escrito en el repositorio. No hay nada que solo exista en ellas.

## Quién es quién (sin cambios)

- **Generador de prompts:** rama `claude/laughing-dirac-s4pmig`. Su conversación activa es «Continuar el Generador
  de prompts en el escritorio». Allí solo se ven prompts y fichas. Lo terminado se presenta aquí.
- **Equipo de producción audiovisual:** rama `claude/pensive-wright-noys0q`, ahora en el PC.
- **Keter** (Cerebro) y **Canal automatizado de YouTube:** en el PC del dueño.
- El dueño autorizó, de forma permanente, que las sesiones se escriban entre sí sin pedirle permiso.

## Estado del trabajo

### Short 4 · «What Is GTA 6» (TIN-EN-S-004)

- **v2: NO aprobada.** Textual del dueño: «intentan correr y casi no se mueven». La revisión está en
  `proyectos/2026-11-26_tin_y_tan_what_is_gta_6/07_revision/revision_v2_animacion.md`, con el veredicto **CAMBIOS**.
  Su sección 5 (2026-11-27) la confirma con el archivo real y una medición propia de las cabezas. Color y destellos
  PASAN.
  - El MP4 está en `C:\Users\HP\Desktop\Proyectos Claude\Canal YouTube\entregas\TIN-EN-S-004 v2 (NO aprobada)\`
    (20.794.162 bytes, sha256 `9d6d9048…5c35e7dc`).
- **v3: ya renderizada por el Generador** (`06_final/tin_y_tan_short04_v3.mp4` en su rama, sha256
  `511571dd5f4d…`). Hay revisiones del 2026-11-27 de edición, animación, continuidad, fotografía y sonido
  (`07_revision/revision_v3_*.md` en `claude/laughing-dirac-s4pmig`). El Generador espera que el dueño diga quién hace
  la segunda vuelta de correcciones: él (aplica, regraba y pide firmas hasta que pase) o producción (la retoma desde la
  rama).
- **Siguiente tarea del equipo:** ver la v3 **en movimiento** en el PC, porque ningún revisor la ha visto en movimiento
  ni la ha oído. Pasar sobre ella `medir_carrera.mjs`, `revisar_color.py` y `postpro.py destellos`, y firmar el
  control 3 (voz) con una escucha. Después se le presenta al dueño aquí.
- **Pendiente del dueño:** el MP4 de la v2 sigue en el historial público de la rama del Generador (commit 84d4263).
  Borrarlo exige reescribir esa rama, y eso lo decide el dueño.

### Otros pendientes conocidos

- **TIN-EN-S-001:** publicado (https://youtube.com/shorts/s9r5bmmNykY). Las revisiones de estadísticas se hacen el
  2026-11-28 y el 2026-12-19.
- El Generador pregunta: «¿Descarto el short 4 de los regresos? ¿Das el sí a los "figurantes de tinta" para el
  duelo?». Contesta el dueño.
- El estado de cada personaje, serie y proyecto se consulta con `python3 video-studio/herramientas/estado.py`.

## Reglas que no cambian

Nada cuesta créditos sin el sí del dueño. Un intento por pieza. Nada se publica sin el dueño. Rehacer una pieza
necesita su sí, aunque sea código y cueste 0 créditos. Los nombres propios van con mayúscula y las cifras con
decimales llevan «≈». El repositorio es público: no van a él videos, fotogramas, audio ni estadísticas.
