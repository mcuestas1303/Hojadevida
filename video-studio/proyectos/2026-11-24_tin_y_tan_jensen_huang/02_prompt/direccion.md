# Dirección del video

> La llena el equipo, cada uno su sección, **antes** del prompt. `director-de-prompts` escribe `prompt.md` a partir
> de esto; `supervisor-de-continuidad` revisa contra esto. Manual: `video-studio/manual/`.

## 1. Objetivo y público — director-creativo

- **Objetivo comercial:** (copiado del brief: monetizar · presencia · recordación · comunidad · conversión · viralidad · otro)
- **KPI principal y meta:** (p. ej. compartidos por mil ≥ 15; meta inicial si aún no hay datos propios)
- **Cómo cambia el objetivo las decisiones:** (duración, gancho, llamada a la acción, formato)
- **Público objetivo:** (edad, intereses, plataforma, por qué lo compartiría)
- **Idea en una línea:**
- **Por qué funciona para ese público:**
- **Aprendizaje que aplicamos:** (del último informe de `video-studio/estadisticas/`, o «sin datos todavía»)

## 2. Emoción, arco y gancho — director-creativo

- **Duración total:**
- **Gancho A (0–1 s):** (movimiento desde el primer fotograma + afirmación de contraste o cifra con fuente)
- **Gancho B (para probar):**
- **Curiosidades encadenadas:** (qué pregunta abre cada tramo y dónde se resuelve)
- **Capítulos visibles:** (« 1/5 » o lista que crece; «no aplica» si no enumera)
- **Cierre que empalma con el inicio (loop):**
- **Llamado a la acción (uno solo):**

| Tiempo | Segundos | Emoción (fila del cap. 01) | Qué pasa |
|---|---|---|---|
| Gancho | | | |
| Tensión | | | |
| Giro / remate | | | |
| Salida | | | |

## 3. Cámara y luz — director-de-fotografia

- **Luz y paleta por escenario:**

| Toma | Dur. | Emoción | Plano | Ángulo | Lente | Movimiento | Frase de cámara (inglés) |
|---|---|---|---|---|---|---|---|
| 1 | | | | | | | |

- **Motivos visuales que vuelven (1 o 2):**
- **Fondo que se mantiene entre planos de objeto:**
- **Tipos de plano (videos de más de 20 s):** detalle · héroe abierto (cerca de la mitad) · subjetivo · revelado
- **Referencias cargadas:** (imagen aprobada, hoja de emociones, `DESIGN.md` si hay gráficos)
- **Se resuelve en edición:**
- **Tomas encadenadas (último fotograma → keyframe):**

## 3b. Color con intención — director-de-fotografia (valida director-creativo)

> `video-studio/manual/13_color_con_intencion.md`. Regla: 2 neutros + 1 acento; el acento va solo en el título y en
> un elemento.

- **Neutros (2):** (hex · para qué: fondo, texto/líneas)
- **Acento (1):** (hex · dónde va · dónde no va)
- **Por qué esta paleta:** (emoción que busca, para este público)
- **Cómo ayuda al objetivo:** (objetivo comercial del brief → qué hace el color → con qué métrica se verá)
- **Riesgos de lectura:** (público mayor, daltonismo, pantalla chica; contraste de texto ≥ 4,5:1, ≥ 7:1 para 45+)
- **Medido (lo llena el supervisor):** (salida de `revisar_color.py`: % en paleta, contraste, saltos entre planos)

## 4. Actuación — director-de-animacion

| Toma | Personaje | Pose inicial (keyframe) | Anticipación → acción → pose final | Secundaria | Mirada | Panel de la hoja |
|---|---|---|---|---|---|---|
| 1 | | | | | | |

- **Frases de actuación (inglés), por toma:**
- **¿Hace falta grabar un clip propio para transferir movimiento?:**

## 5. Sonido — disenador-de-sonido

| Toma | Voz (texto exacto) | Efectos (segundo) | Música |
|---|---|---|---|
| 1 | | | |

- **Lista de golpes** (cada corte, destello o salto del mapa de ritmo con su sonido):

| Segundo | Qué pasa en imagen | Sonido |
|---|---|---|
| | | |

- **Voz en off o labios:**
- **Música:** (la pone el dueño / prompt en `05_audio/audio.md`)

## 6. Montaje y salida — editor-de-video

- **Mapa de ritmo:** (tramos densos y respiros de 2–3 s; nunca pulso plano; acelera hacia el final y remata con el plano del inicio)

| Tramo | Segundos | Densidad (cambios) | Qué pasa |
|---|---|---|---|
| | | | |

- **Orden y duración de tomas:**
- **Cortes y transiciones:**
- **Loop:**
- **Subtítulos y texto en pantalla:**
- **Color:** (igualar tomas según la sección 3b; `postpro.py color` o LUT; nada fuera de la paleta decidida)
- **Salidas por plataforma:**

## 7. Ruta de producción y presupuesto — jefe-de-produccion

- **Modo:** (A clip propio · B réplica · C desde cero)

| Toma | Método | Borrador (modelo, ajuste) | Final (modelo, ajuste) | Intentos | Créditos |
|---|---|---|---|---|---|
| 1 | | | | 1 | |

- **Ahorro por edición:**
- **Total estimado / presupuesto del brief:**
- **Alternativa más barata:**

## 8. Publicación y medición — director-creativo

- **Plataforma(s) y hora:**
- **Título:**
- **Descripción y etiquetas:**
- **Llamada a la acción:**
- **Etiquetas para estadísticas:** (personaje, modo, gancho, emoción, duración, formato; van a `estadisticas/etiquetas.csv`)
- **Revisión de resultados:** (fecha: 72 h para Shorts, 7 días para videos largos)
