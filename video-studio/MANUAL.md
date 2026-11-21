# Manual: montar un personaje de cero a publicación

Este es el procedimiento completo del estudio. Sirve para repetir con cualquier personaje nuevo
lo que se hizo con Tiky y Lumi. Cada fase dice qué se hace, quién lo hace, qué archivo queda,
con qué comando, cuándo se da por lista y cuánto cuesta. El caso real, con fechas, costos y
errores, está en `casos/tiky_y_lumi.md`.

Regla del dueño (2026-11-21): **todo lo que se trabaje queda documentado como plantilla.** Si
el proceso cambia, se cambia primero este manual; si aparece un paso nuevo, se agrega aquí con
su plantilla y su herramienta.

Para saber en qué fase está cada cosa:

```bash
python3 video-studio/herramientas/estado.py
```

## Las reglas que valen en todas las fases

| Regla | Dónde está escrita |
|---|---|
| Un intento por pieza: nada se regenera sin autorización del dueño para esa pieza | `generacion.md` |
| No se genera sin definición cerrada (personaje, lugar y pieza) y sin el costo a la vista | `generacion.md` |
| Todo cambio pasa primero por el equipo como solicitud en `cambios/` | `generacion.md`, `plantillas/solicitud_cambio.md` |
| Lo que falta se pregunta; no se supone ni se inventa | `generacion.md`, guía de cada agente |
| Toda cifra o requisito externo lleva fuente y fecha; si no se leyó, dice «sin verificar» | `comercial/base_conocimiento.md` |
| Línea editorial del dueño | `infantil/guia_1_a_3.md`, `series/<serie>/serie.md` |
| El contenido infantil nunca se cruza con personajes para adultos | `personajes/REGISTRO.md` |
| Las imágenes se revisan a tamaño completo antes de informar un fallo | Lección 3, más abajo |

## El equipo

| Agente | Disciplina | Qué entrega | Cuándo entra |
|---|---|---|---|
| `pedagoga-montessori` | Pedagogía de primera infancia y Montessori | Ficha pedagógica; palabra clave por idioma; sus criterios de la rúbrica | Fase 4 |
| `guionista-interactivo` | Aprendizaje interactivo | Guion plano por plano; voz en cada idioma; sus criterios | Fase 4 |
| `psicologa-infantil` | Psicología del desarrollo | Veredicto del guion y de cada definición; tiene veto | Fases 4, 6 y 8 |
| `comercial-inteligencia-digital` | Datos de plataformas e inteligencia digital | Paquete de publicación por idioma; estrategias; base de conocimiento | Fases 2, 4 y 9 |
| `director-de-prompts` | Producción | Prompt validado; definición de generación; sus criterios | Fases 5 y 6 |
| `analista-de-video` | Análisis de video | Desglose de un video de referencia o de uno generado | Fases 3 y 8 |

Las definiciones de los agentes están en `.claude/agents/`. Para otro tipo de público se
cambia la guía que leen (`infantil/guia_1_a_3.md`), no los agentes.

## Fase 0 — Decisiones del dueño antes de empezar

Sin estas respuestas no se avanza, porque cada una costó retrabajo o créditos cuando faltó.

| Decisión | Por qué importa | Dónde se anota |
|---|---|---|
| Quién es el público y qué edad tiene | Define la guía, el ritmo y lo que está prohibido | `series/<serie>/serie.md` |
| Para qué es: enseñar, vender, posicionar | Define rúbrica y estrategia | Brief y estrategias |
| Personajes que salen y cuáles no | El validador rechaza a los demás | «Elenco permitido» |
| Género y nombre de cada personaje | Lo exigen varios idiomas | Ficha del personaje |
| Lugar y si es real o de juguete | Define el entorno | `entorno.md` |
| Idiomas | Define voz y paquetes de publicación | `serie.md` |
| Voz: narrador o personajes; cómo se hace | Define costo y si hay que declarar IA | `serie.md` |
| Plataformas y formatos | Define aspecto y duración | `formatos.md`, `serie.md` |
| Canal de cada plataforma (nombre, identificador, si ya existe) | Un canal por público; define el paquete de publicación y la estrategia | `serie.md` |
| País del titular de las cuentas | Define qué programas de pago existen | `serie.md` |
| Generador, plan y saldo | Define precios y límites | `generador.md` |
| Línea editorial | Filtro de todo el contenido | Guía y `serie.md` |

## Fase 1 — El personaje

**Quién:** el dueño aprueba el diseño; la coordinación documenta. **Costo:** 1,5 créditos por
imagen (referencia de 2026-11); la hoja de personaje, aparte.

1. Crear la carpeta:

   ```bash
   python3 video-studio/herramientas/nuevo_personaje.py <id> "<Nombre>" "<rol>" --publico "<público>"
   ```

2. Diseñar y aprobar la imagen del personaje (cuerpo entero, fondo liso). Guardarla en
   `personajes/<id>/referencias/` y anotar su ID del generador.
3. Completar `ficha.md`:
   - Datos (nombre, género, rol, personalidad, voz).
   - **Bloque de identidad:** un párrafo en inglés que describe solo lo que se ve y nunca
     cambia. Se pega tal cual en cada prompt. Si cambia, se cambia en todos los prompts.
   - Lo que nunca cambia, variaciones permitidas, prohibido.
   - **Definición para generar:** medidas contra un punto de referencia (otro personaje, un
     objeto del lugar), posición exacta de cada rasgo (de qué lado, contra qué fondo), con qué
     extremidad hace su gesto, lista de comprobación y fallos conocidos del generador.
4. Opcional: hoja de personaje con vistas y emociones (`plantillas/hoja_de_personaje.md`).

**Listo cuando:** `estado.py` marca las tres casillas del personaje.

## Fase 2 — La serie y el lugar

**Quién:** coordinación con el dueño; pedagoga para el temario; comercial para la estrategia.
**Costo:** 0 créditos.

1. Crear la serie:

   ```bash
   python3 video-studio/herramientas/nueva_serie.py <serie> --copiar-reglas-de granja
   ```

   Con `--copiar-reglas-de` hereda el ritmo, los idiomas y las reglas de revisión de una serie
   que ya funciona. Sin esa opción parte de la plantilla vacía (`plantillas/serie/`).
2. Completar `serie.md`: reglas que comprueba el validador, quiénes salen, la pareja,
   estructura del episodio, formatos, voz, estilo y negativo globales, publicación.
3. Completar `entorno.md`: reglas del lugar y un bloque en inglés por cada lugar fijo. La
   «definición cerrada» de cada lugar se escribe a partir del primer keyframe aprobado, y esa
   imagen se guarda en `series/<serie>/referencias/`.
4. Temario: la pedagoga propone los primeros episodios (un objetivo cada uno); el dueño elige.
5. Estrategia: el comercial escribe la de cada plataforma con fuentes oficiales; la pedagoga y
   la psicóloga dictaminan cada ajuste que toque el contenido. Ver `series/granja/estrategia_*.md`.

**Listo cuando:** `estado.py` marca los tres archivos de la serie.

## Fase 3 — El proyecto de un video

```bash
python3 video-studio/herramientas/nuevo_proyecto.py "<título>" --serie <serie>
```

- Con un video de referencia: se pasa su ruta como segundo argumento y el `analista-de-video`
  escribe `01_referencia/analisis.md`. Se copia la estructura, nunca el metraje ni las personas.
- Para contenido de adultos o redes: `--redes` en lugar de `--serie` (plantilla con gancho,
  rejilla de tiempo y texto). Nunca en series infantiles.
- Se llena `00_brief.md`. Lo que el dueño no haya dicho queda escrito como «por confirmar».

## Fase 4 — Del objetivo al guion aprobado

**Costo:** 0 créditos. Todo queda en `<proyecto>/02_prompt/`.

| Orden | Quién | Archivo | Qué decide |
|---|---|---|---|
| 1 | Pedagoga | `ficha_pedagogica.md` | Un solo objetivo observable, tramo de edad, material, palabra clave por idioma |
| 2 | Comercial | `publicacion.md` (+ `_en`, `_pt-BR`) | Búsqueda, título, descripción, miniatura, shorts derivados |
| 3 | Guionista | `guion.md` | Planos, voz exacta, preguntas y pausas |
| 4 | Psicóloga | `revision.md` | APROBADO o CAMBIOS; si hay cambios, vuelve al guionista |
| 5 | Guionista | `voz_idiomas.md` | La voz en cada idioma, en los mismos tiempos |
| 6 | Pedagoga y psicóloga | `voz_idiomas.md`, `revision.md` | Dudas de idioma y veredicto de los tres idiomas |
| 7 | Cada uno | `ficha_tecnica.md` | Sus criterios de la rúbrica, comprobables en el video |

**Listo cuando:** `revision.md` dice APROBADO para todos los idiomas. Con «Hola, granja» hicieron
falta tres vueltas; es normal y no cuesta créditos.

## Fase 5 — El prompt

**Quién:** `director-de-prompts`. **Costo:** 0 créditos.

1. Traduce cada plano del guion aprobado a tomas (una acción, una cámara). No agrega ni quita planos.
2. Pega tal cual el bloque de identidad, el bloque del lugar y el estilo de la serie.
3. Cada «Prompt de video» empieza con las líneas `CRITICAL:` (sin palabras ni marcas,
   personajes idénticos a la imagen de partida, cámara, nada inventado).
4. Los lados se escriben respecto al cuadro («the right side of the frame»), no respecto al personaje.
5. Llena su sección de la rúbrica y el presupuesto con un intento por pieza.
6. Valida y archiva:

   ```bash
   python3 video-studio/herramientas/validar_prompt.py video-studio/proyectos/<proyecto>/02_prompt/prompt.md
   ```

   ```bash
   python3 video-studio/herramientas/archivar_prompt.py video-studio/proyectos/<proyecto>
   ```

El prompt, su rúbrica y su voz quedan en `personajes/<protagonista>/prompts/<tipo>/`.

## Fase 6 — Definición y generación

**Costos de referencia (2026-11):** keyframe 1,5 créditos; clip en borrador a 480p, 0,5 por
segundo; clip final a 720p, 1 por segundo. Antes de cada generación se cotiza de nuevo.

1. **Definición.** El director escribe `03_keyframes/definicion.md` y `04_clips/definicion.md`
   (`plantillas/definicion_generacion.md`): por cada pieza, referencias que se suben,
   composición con medidas, qué debe verse, qué no, modelo, ajustes y costo cotizado.
2. **Revisión.** La psicóloga la revisa y, si está conforme, el estado pasa a «REVISADA POR EL EQUIPO».
3. **Autorización.** El dueño la autoriza con el costo total a la vista. Sin eso no se genera.
4. **Orden.** Primero el keyframe donde sale todo el elenco en el lugar: sirve de referencia
   del lugar para los demás. En los clips, la primera etapa es una sola toma no encadenada.
5. **Una vez cada pieza.** Si sale mal: se anota en `costos.md`, se informa al dueño con el
   costo de rehacerla y se detiene lo que dependa de ella.
6. **Registro.** Cada generación va a `costos.md`; cada recurso, a `licencias.md`; cada fallo,
   a «Fallos conocidos» de la ficha del personaje o del lugar.

## Fase 7 — Montaje

**Costo:** 0 créditos.

1. Los clips aprobados van a `04_clips/seleccionados/` como `toma_01.mp4`, `toma_02.mp4`…
2. Voz, música y efectos van a `05_audio/`, anotados en `licencias.md`.
3. Ensamblar al formato de `formatos.md`:

   ```bash
   python3 video-studio/herramientas/ensamblar.py video-studio/proyectos/<proyecto> --formato largo
   ```

   `--formato short` para vertical. Un short no se recorta de un capítulo: lleva sus keyframes.
4. Un máster por idioma: mismo video, distinta pista de voz.

## Fase 8 — Revisión y rúbrica

1. Revisión automática de cada clip y del máster (gratis):

   ```bash
   python3 video-studio/herramientas/revisar_fotogramas.py <clip> video-studio/proyectos/<proyecto>/07_revision/<toma> --serie <serie>
   ```

2. El `analista-de-video` describe el video; cada profesional puntúa sus criterios (0, 1 o 2)
   con evidencia de plano y segundo en `02_prompt/ficha_tecnica.md`.
3. Calcular:

   ```bash
   python3 video-studio/herramientas/puntuar_ficha.py video-studio/proyectos/<proyecto>/02_prompt/ficha_tecnica.md
   ```

   «CUMPLE» con 80 % o más y todos los críticos en 2. Un crítico por debajo de 2 es «NO
   PUBLICAR». Rehacer algo sigue necesitando la autorización del dueño.
4. Volver a archivar para que la rúbrica puntuada quede junto al prompt.

## Fase 9 — Publicación y medición

1. Publicar con el paquete de `publicacion*.md` de cada idioma. Antes, el comercial vuelve a
   leer las políticas vigentes (cambian; la base tiene fecha).
2. A los 7 y 28 días, el dueño exporta los datos del canal a `video-studio/datos/`; el
   comercial llena «Metas después de publicar» y dice qué se aprendió.
3. Lo aprendido que cambie el proceso se trae a este manual.

## Mapa de archivos

| Qué | Dónde |
|---|---|
| Este manual y el caso de ejemplo | `MANUAL.md`, `casos/` |
| Reglas de créditos y cambios | `generacion.md` |
| Formatos de salida | `formatos.md` |
| Generador y precios | `generador.md` |
| Personajes | `personajes/<id>/` (ficha, referencias, prompts) y `personajes/REGISTRO.md` |
| Series | `series/<serie>/` (biblia, entorno, temario, estrategias, referencias) |
| Guía del público | `infantil/guia_1_a_3.md` |
| Plantillas | `plantillas/` (prompt, prompt de redes, proyecto, serie, definición, solicitud de cambio) e `infantil/plantilla_*.md` |
| Mesa de trabajo de cada video | `proyectos/<fecha>_<nombre>/` |
| Solicitudes de cambio | `cambios/` |
| Base de conocimiento del comercial | `comercial/base_conocimiento.md` |
| Datos del canal | `datos/` |
| Estudios y referencias externas | `estudios/`, `referencias_externas.md` |
| Herramientas | `herramientas/` |

## Herramientas

| Herramienta | Para qué | Fase |
|---|---|---|
| `estado.py` | Ver qué falta en cada personaje, serie y proyecto | Todas |
| `nuevo_personaje.py` | Dar de alta un personaje | 1 |
| `nueva_serie.py` | Crear una serie | 2 |
| `nuevo_proyecto.py` | Crear la carpeta de un video | 3 |
| `analizar_video.py` | Desarmar un video en fotogramas para poder verlo | 3 y 8 |
| `validar_prompt.py` | Comprobar elenco, formato, ritmo, idiomas, rúbrica y revisión | 5 |
| `archivar_prompt.py` | Guardar el prompt en la carpeta del personaje | 5 y 8 |
| `ensamblar.py` | Unir clips en el máster | 7 |
| `revisar_fotogramas.py` | Marcar imagen congelada, vacíos, destellos y planos cortos | 8 |
| `puntuar_ficha.py` | Calcular el cumplimiento de la rúbrica | 8 |

## Lecciones aprendidas

Cada una costó tiempo o créditos y por eso es un paso del manual.

1. **La altura entre personajes se define con un punto de referencia en el cuerpo del otro**
   («el copete le llega a los ojos»), no con «el doble» o «la mitad». Costó un keyframe.
2. **Los rasgos pequeños se piden diciendo dónde están y contra qué fondo se ven.** El crayón
   de Lumi desapareció cuando solo se describió.
3. **Las imágenes se revisan a tamaño completo antes de informar un fallo.** Se informó un
   techo distinto que no lo era; el dueño autorizó rehacer dos imágenes sin necesidad.
4. **El primer keyframe es el del elenco completo en el lugar**, y se usa como referencia del
   lugar para los demás. Así el escenario sale igual.
5. **Izquierda y derecha se escriben respecto al cuadro.** «A su derecha, lejos de Lumi» era
   una contradicción que se detectó antes de generar.
6. **Cada personaje tiene fijado con qué extremidad hace su gesto**, del lado que no tapa al otro.
7. **El presupuesto se calcula con un intento por pieza.** Calcular con dos invita a usarlos.
8. **Un solo objetivo por video.** El temario juntaba dos; la pedagoga dejó uno.
9. **La palabra clave no puede usarse con otro sentido.** «Hola» en la despedida enseñaba mal
   justo lo que se quería enseñar.
10. **Al adaptar a otro idioma se revisa qué se le pide al público.** En inglés y portugués se
    pedía decir la palabra cuando el objetivo era el gesto.
11. **Sin texto en pantalla ni labios sincronizados, un video sirve para todos los idiomas.**
12. **Las políticas de las plataformas se leen en la página oficial, descargada y fechada.**
    Los resúmenes de buscador dieron datos contradictorios.
13. **El ritmo de redes no se traslada al contenido infantil.** Son plantillas separadas.
14. **Lo que se genera con créditos y lo que se corrige con código son cosas distintas:** lo
    primero se hace una vez; lo segundo se puede repetir.
