# Procedimiento para crear personajes gastando lo mínimo en Higgsfield

> Objetivo: llegar al personaje y al video que el dueño quiere **gastando créditos solo cuando el diseño ya está
> decidido**. Costos verificados con `get_cost` el 2026-11-07 (plan Plus). Saldo ese día: 915,23 créditos.
> Los precios cambian: antes de cada generación se vuelve a cotizar.

## El flujo en tres fases (decisión del dueño, 2026-11-07)

> Textual: *«creamos prompt luego lo visualizo y ajustamos con el método sin costo y por último producimos con
> higgsfield»*.

1. **Crear el prompt** — el afinador escribe el prompt y la ficha `fichas/<personaje>.json`; el revisor de atención
   dice para qué público está diseñado y qué capta la atención. **Gratis.**
2. **Visualizar y ajustar sin costo** — se dibuja el boceto con `herramientas/boceto.js` y se le muestra al dueño en el
   chat (o él lo ajusta en `index.html`). Se repite hasta que le convenza. **Gratis.**
3. **Producir en Higgsfield** — solo con el diseño aprobado: cotizar, aprobar, generar. Primero la imagen oficial;
   después, si hay video, prueba corta y luego el final (ver la escalera).

Z Image (0,15) queda como paso **opcional** entre la fase 2 y la 3, si el dueño quiere ver una aproximación
fotográfica antes de pagar la imagen oficial.

## Precios verificados

| Uso | Modelo | Ajuste | Créditos |
|---|---|---|---|
| Boceto de exploración | Z Image | 1 imagen | **0,15** |
| Imagen buena | Nano Banana 2 | 1 imagen | 1,5 |
| Imagen final | Nano Banana Pro | 1 imagen (1k o 2k) | 2 |
| Prueba de movimiento | Seedance 2.0 Mini | 5 s · 480p | **2,5** |
| Video de calidad media | Seedance 2.0 Mini | 5 s · 720p | 5 |
| Video de calidad media | Seedance 2.0 Mini | 12 s · 720p | 12 |
| Video alternativo | Kling 3.0 | 5 s · std · sin sonido | 7,5 |
| Video de calidad alta | Seedance 2.0 | 5 s · 480p | 15 |
| Video de calidad alta | Seedance 2.0 | 12 s · 480p | 36 |
| Video de calidad alta | Seedance 2.0 | 12 s · 720p | 54 |
| Transferir movimiento de un clip propio | Genjutsu | 12 s · 480p | 36 |
| Transferir movimiento de un clip propio | Genjutsu | 12 s · 720p | 84 |
| Música | ElevenLabs Music v2 | 12 s | 0,77 |

**Lo que ya se gastó** (2026-11-07): 94,77 créditos. Lo más caro fue el video de Seedance 2.0 en 720p (54).

## La escalera: cada escalón se paga solo si el anterior quedó aprobado

| Escalón | Qué se decide | Herramienta | Costo |
|---|---|---|---|
| **0. Idea y prompt** | Quién es, rasgo icónico, público | Afinador + revisor de atención | **gratis** |
| **1. Boceto** | Colores, peinado, ropa | Vista previa `index.html` | **gratis** |
| **2. Exploración (opcional)** | Una aproximación fotográfica si hay dudas | Z Image | 0,15 c/u |
| **3. Imagen del personaje** | La versión «oficial» que será referencia | Nano Banana Pro (o Nano Banana 2) | 1,5–2 |
| **4. Prueba de movimiento** | Que la escena y la acción funcionen | Seedance 2.0 Mini · 5 s · 480p | 2,5 |
| **5. Video final** | El Short para publicar | Seedance 2.0 Mini 12 s 720p (12) · solo si hace falta más calidad, Seedance 2.0 | 12–54 |

**Presupuesto de referencia:** un personaje nuevo, de 1 a 3 créditos hasta tener su imagen oficial. Un Short de 12 s,
unos 15 créditos (prueba más final en Mini). Seedance 2.0 en 720p solo para un video que ya funcionó en Mini.

## Reglas para no tirar créditos

1. **Cotizar siempre antes** (`get_cost`) y decir el número antes de generar. Sin aprobación no se genera.
2. **Nunca explorar en video.** El diseño se decide en imagen (escalones 2 y 3); el video solo anima algo ya aprobado.
3. **Una variante por vez en video** (`count: 1`). Las variantes se prueban en imagen, que es barata.
4. **Primero corto y en baja resolución:** 5 s en 480p. Si funciona, recién entonces 12 s en 720p.
5. **Sin audio generado:** la música la pone el dueño. Ahorra créditos y evita una pista que después no se usa.
6. **Reusar referencias:** la imagen oficial de cada personaje (su ID) va siempre como referencia en los videos.
   Así no hay que «volver a encontrarlo».
7. **Freno de pérdidas:** si dos intentos seguidos no salen bien, **no se genera un tercero**. Se vuelve al
   escalón 0 (gratis) a revisar el prompt con el afinador y el revisor.
8. **Registrar el gasto** de cada intento en la bitácora del personaje (modelo, ajuste, créditos, veredicto).

## Cómo tiene que ser un prompt de video eficiente

- **Una acción clara por plano**, y como máximo 3 o 4 planos en 12 s (2 en 5 s).
- **Personajes por referencia:** «the character from image reference 1» más sus 2 o 3 rasgos fijados, no la
  descripción completa.
- **El mismo fondo, dicho igual en todas las partes** de un video largo (lección del Short 02: la parte 2 cambió de
  estudio). Por ejemplo: «same seamless white infinity studio, no visible lights or ceiling».
- **Cámara y encuadre explícitos** («close-up», «wide shot», «handheld documentary camera»).
- **Sin diálogo ni texto en pantalla** salvo que sea el objetivo.
- **Movimiento antes que conversación:** baile, poses y gestos grandes se entienden sin audio (lección del caso de
  estudio).
- **En positivo:** decir lo que sí va. Las negaciones solo al final y cortas.

## Quién hace qué

- **Afinador de personajes:** escribe el prompt de cada escalón y sugiere el modelo más barato que alcance.
- **Revisor de atención:** revisa público y atención antes de subir al escalón 3 y antes del video.
- **Sesión principal:** cotiza, pide aprobación, genera, revisa el resultado y anota el costo.
