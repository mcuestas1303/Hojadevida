# Procedimiento para crear personajes gastando lo mínimo en Higgsfield

> Objetivo: llegar al personaje y al video que el dueño quiere **gastando créditos solo cuando el diseño ya está
> decidido**. Costos verificados con `get_cost` el 2026-11-07 (plan Plus). Saldo ese día: 915,23 créditos.
> Los precios cambian: antes de cada generación se vuelve a cotizar.

## El flujo en tres fases (decisión del dueño, 2026-11-07)

> Textual: *«creamos prompt luego lo visualizo y ajustamos con el método sin costo y por último producimos con
> higgsfield»*.

1. **Crear el prompt** — el afinador escribe el prompt y la ficha `fichas/<personaje>.json`; el revisor de atención
   dice para qué público está diseñado y qué capta la atención. **Gratis.**
2. **Visualizar y ajustar sin costo, fuera de Higgsfield** — el método principal es el cuaderno de Google Colab
   `colab/bocetos_flux_schnell.ipynb`: genera imágenes realistas con **FLUX.1 schnell** (modelo abierto, Apache-2.0) en
   la GPU T4 gratuita de Colab. El dueño pega el prompt del afinador, mira 4 variantes (semillas) y dice qué le gusta;
   se ajusta y se repite. Para cambios rápidos de color o peinado sirve también el boceto SVG
   (`herramientas/boceto.js` o `index.html`). **Gratis.**
   Abrir en Colab: https://colab.research.google.com/github/mcuestas1303/Hojadevida/blob/claude/focused-thompson-wojzu6/creador-personajes/colab/bocetos_flux_schnell.ipynb
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
| Prueba de escena completa | Seedance 2.0 Mini | 12 s · 480p | **6** |
| Prueba rápida alternativa | Grok Video 1.5 Lite | 5 s · 720p | 5 |
| Video de calidad media | Seedance 2.0 Mini | 5 s · 720p | 5 |
| Video de calidad media | Seedance 2.0 Mini | 12 s · 720p | 12 |
| Video alternativo | Kling 3.0 | 5 s · std · sin sonido | 7,5 |
| Video de calidad alta | Seedance 2.0 | 5 s · 480p | 15 |
| Video de calidad alta | Seedance 2.0 | 12 s · 480p | 36 |
| Video de calidad alta, más barato | Seedance 2.0 modo fast | 12 s · 720p | 30 |
| Video de calidad alta | Seedance 2.0 (std) | 12 s · 720p | 54 |
| No conviene | Seedance 2.5 | borrador 5 s: 15 · 5 s 720p: 35 | caro |
| Transferir movimiento de un clip propio | Genjutsu | 12 s · 480p | 36 |
| Transferir movimiento de un clip propio | Genjutsu | 12 s · 720p | 84 |
| Música | ElevenLabs Music v2 | 12 s | 0,77 |
| Ampliar una imagen a 4K | Upscale (ByteDance) | 1 imagen | 2 (no conviene: es lo mismo que generarla en Nano Banana Pro) |

**Lo que ya se gastó** (2026-11-07): 94,77 créditos. Lo más caro fue el video de Seedance 2.0 en 720p (54).

## La escalera: cada escalón se paga solo si el anterior quedó aprobado

| Escalón | Qué se decide | Herramienta | Costo |
|---|---|---|---|
| **0. Idea y prompt** | Quién es, rasgo icónico, público | Afinador + revisor de atención | **gratis** |
| **1. Boceto y definición** | Silueta, colores, ropa, actitud | FLUX.1 schnell en Colab (realista) · boceto SVG (rápido) | **gratis** |
| **2. Exploración (opcional)** | Una aproximación fotográfica si hay dudas | Z Image | 0,15 c/u |
| **3. Imagen del personaje** | La versión «oficial» que será referencia | En la **web**, con un modelo ilimitado del plan (gratis); si no, Nano Banana Pro por aquí | 0–2 |
| **4. Prueba de movimiento** | Que la escena y la acción funcionen | Créditos diarios gratis de otra plataforma, o Seedance 2.0 Mini 480p (5 s: 2,5 · 12 s: 6) | 0–6 |
| **5. Video final** | El Short para publicar | Seedance 2.0 Mini 12 s 720p (12) · si falta calidad, Seedance 2.0 fast (30) | 12–30 |

**Presupuesto de referencia:** un personaje nuevo, **0 créditos** si la imagen se hace en la web con un modelo
ilimitado (de 1 a 3 si no). Un Short de 12 s, unos **18 créditos** (prueba de 6 más final de 12, en Mini). Seedance 2.0 en 720p solo para un video que ya funcionó en Mini.

## Métodos para mantener la calidad gastando menos (2026-11-07)

1. **Imágenes ilimitadas en la web de Higgsfield.** Según el blog de Higgsfield y guías de 2026, el plan Plus trae
   modelos de imagen **ilimitados por 365 días** (entre los citados: Nano Banana, Seedream 4.5, Seedream 5.0 Lite,
   FLUX.2 Pro, Kling O1 Image, GPT Image) y ventanas de 7 días para otros (Nano Banana 2 en 2K, Kling 3.0). **Solo
   funcionan en la web higgsfield.ai, no por la conexión de Claude (MCP)**, que siempre cobra créditos. Confianza media:
   la lista exacta hay que verla en la cuenta (los modelos marcados «Unlimited»).
   → **Toda la exploración y la imagen oficial se hacen en la web, gratis.** Lo generado en la web aparece en el
   historial y su ID se puede usar desde aquí como referencia para los videos.
2. **Video: probar barato y terminar en Mini.** Prueba de escena completa en Mini 12 s 480p (**6**); final en Mini 12 s
   720p (**12**). Si falta calidad, Seedance 2.0 en modo **fast** (30) antes que el normal (54). Seedance 2.5 no
   conviene.
3. **Créditos diarios gratis de otras plataformas para ensayar movimiento** (sin publicar): Kling (unos 66 por día),
   PixVerse (unos 60 por día), Dreamina o CapCut (Seedance). Suelen tener marca de agua, 720p o menos y prohibir uso
   comercial; sirven para probar si una acción o un prompt funciona antes de pagarlo en Higgsfield. Cifras de blogs de
   terceros, sin verificar: confianza baja.
4. **Clips cortos y edición.** Generar de a 5 s y armar el video en un editor (CapCut o el del celular) repitiendo o
   recortando, en vez de generar 24 s de una.
5. **Sin ampliaciones pagas de imagen:** cuestan lo mismo que generar en Nano Banana Pro. La ampliación de video no
   permite cotizar antes: no usarla sin saber el costo.
6. **El mayor ahorro es no repetir:** prompt afinado, boceto gratis y freno de pérdidas (dos intentos fallidos →
   volver al prompt).

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

## Fuentes (consultadas el 2026-11-07)

- Higgsfield, «Introducing New Unlimited»: https://higgsfield.ai/blog/new-unlimited-more-models
- Higgsfield, planes ilimitados anuales: https://higgsfield.ai/blog/annual-unlimited-ai-video-plans
- Krea, precios de Higgsfield 2026: https://www.krea.ai/blog/higgsfield-pricing-explained-2026-unlimited-credits-and-real-monthly-costs
- Límites gratis de video con IA 2026: https://whichoneisreal.com/compare/best-free-ai-video/
- Generadores gratis de imagen a video 2026: https://shhots.ai/blog/best-free-ai-image-to-video-generators/
- Los precios en créditos de las tablas salen de `get_cost` en Higgsfield, el mismo día.
