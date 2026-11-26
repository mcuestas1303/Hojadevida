# Consumo por video

Registro de lo que cuesta producir cada video, para estimar el siguiente. Pedido del dueño
(2026-11-21): «necesito que quede registrado aproximadamente cuánto se consumiría del límite
con la generación del video para ir estimando costos».

Se gastan dos límites distintos y se anotan los dos:

| Límite | En qué se mide | De dónde sale el dato | Qué no se sabe desde aquí |
|---|---|---|---|
| **Créditos de Higgsfield** | Créditos | Cotización antes de generar y `costos.md` de cada proyecto | El saldo exacto: la conexión no lo entrega. Último saldo anotado por el dueño: unos 888 créditos el 2026-11-09 |
| **Uso de Claude** | Tokens de los agentes del equipo (miles = k) | Lo que reporta cada agente al terminar | Qué porcentaje del límite del plan de Claude representa: eso solo se ve en la app (Configuración → Uso). La conversación principal también consume y no se puede medir desde dentro |

Cómo se usa: al terminar cada fase se anota aquí lo gastado. Antes de empezar un video nuevo se
mira el más parecido y se toma su total como estimación. Cuando el dueño anote cuánto subió su
medidor de uso de Claude durante un video, se agrega en la columna «% del límite de Claude» y
desde entonces la estimación se puede dar en porcentaje.

## Resumen

| Video | Tipo | Créditos gastados | Créditos que faltan (estimado) | Tokens de agentes | % del saldo de créditos (sobre 888) | % del límite de Claude |
|---|---|---|---|---|---|---|
| Hola, granja (cap. 1, 88 s, generador de video) | Capítulo infantil 16:9 | 7,5 | 44 en borrador + 88 en final = 132 | 885 k hasta la definición de clips | 0,8 % gastado; 15,7 % al terminar | sin dato |
| Tin y Tan: casete y lápiz (unos 30 s, dibujado con código) | Short 9:16 | 4,8 | 0 previstos | 558 k hasta el video v1 y su ficha; +160 k del prompt v2 (dos pasadas del director de prompts) | 0,3 % | sin dato |
| Tin y Tan: la espera de GTA 6 (26,5 s, dibujado con código) | Short 9:16 | 3,2 (voz) | 0 previstos | 57 k de investigación + 126 k del prompt + 74 k de color + 359 k de montaje, render y dos vueltas de revisión | sin dato | sin dato |

Lectura rápida:

- Un capítulo hecho con generador de video cuesta sobre todo **créditos**: unos 1,6 créditos por segundo de video terminado (0,5 en borrador + 1 en final + keyframes).
- Un video dibujado con código casi no cuesta créditos (solo la voz: unos 0,1 créditos por segundo de voz) y cuesta sobre todo **uso de Claude**.
- El primer video de una serie cuesta mucho más uso de Claude que los siguientes, porque incluye definir personajes, lugar, reglas y plantillas. Lo que sigue reutiliza todo eso.

## Hola, granja — detalle

Créditos (ver `proyectos/2026-11-20_hola_granja/costos.md`):

| Pieza | Créditos | Estado |
|---|---|---|
| 5 keyframes (1 descartado) | 7,5 | Gastado |
| 16 clips en borrador, 88 s a 480p | 44 | Cotizado, sin autorizar |
| 16 clips finales, 88 s a 720p | 88 | Cotizado |
| Voz en tres idiomas y música | sin cotizar | Falta decidir cómo se hacen |

Uso de Claude, por fase del manual (tokens que reportó cada agente):

| Fase | Trabajo | Tokens |
|---|---|---|
| 4 | Ficha pedagógica y su corrección | 57 k |
| 4 | Guion: primera versión y dos reescrituras | 54 k |
| 4 | Revisión del guion: tres vueltas | 64 k |
| 4 | Paquete de publicación en español | 127 k |
| 4 | Voz en inglés y portugués | 29 k |
| 4 | Decisiones de idioma de la pedagoga y revisión de la psicóloga | 154 k |
| 5 | Prompt de video | 60 k |
| 6 | Definición de dos keyframes | 72 k |
| 6 | Opinión sobre el encuadre | 34 k |
| 6 | Restricciones críticas y definición de los 16 clips | 119 k |
| 6 | Revisión de la definición de clips | 117 k |
| | **Total del capítulo hasta aquí** | **885 k** |

Faltan: generación por etapas, revisión de cada clip, montaje, rúbrica y publicación.

Trabajo de una sola vez para toda la serie (no se repite en cada capítulo):

| Trabajo | Tokens |
|---|---|
| Estrategia de monetización, primera versión | 164 k |
| Estrategias de TikTok e Instagram | 312 k |
| Evaluación del VPN y vías desde El Salvador | 183 k |
| Estudio de la biblioteca de prompts | 150 k |
| Estrategia de monetización con fuentes oficiales | sin dato (no se recuperó la cifra) |

## Tin y Tan: casete y lápiz — detalle

| Pieza | Créditos | Estado |
|---|---|---|
| Voz de Tin (Kevin), 21,8 s | 2,2 | Gastado |
| Voz de Tin v2, líneas 4, 5, 6 y 8 en pulgadas y pies (autorizada por el dueño; la generó producción) | 1,8 | Gastado |
| Voz de Tan (Zelda), 12,5 s | 0,8 | Gastado |
| Imagen | 0 | Se dibuja con código |
| Música y efectos | 0 previstos | Con código; si hubiera que generarlos, se cotiza antes |

| Fase | Trabajo | Tokens |
|---|---|---|
| 3 | Carpeta, brief, línea de tiempo de la voz (conversación principal) | sin medir |
| 5 | Prompt del video (16 tomas, 30 s) | 131 k |

| 6 y 7 | Dibujo, audio, render y dos vueltas de revisión con código (20 min de trabajo) | 274 k |
| 4 | Ficha de publicación en el formato del publicador | 153 k |
| | **Total hasta el video renderizado y su ficha** | **558 k** |

Faltan: revisión del equipo de producción, escucha del audio, ajustes y publicación.

## Trabajo de estudio que no es de un video (2026-11-21)

| Qué | Tokens de agentes | Créditos |
|---|---|---|
| Radar de tendencias, primera versión (comercial) | sin anotar al entregarse | 0 |
| Estudio de títulos (comercial), 64 consultas | 223 k | 0 |
| Color con intención en el prompt del short 2 (director de prompts) | 74 k | 0 |
| Short 2: firmas del equipo (sonido 110 k, supervisor 358 k, fotografía 71 k), perfil emocional 219 k, montaje y cinco renders 559 k | ≈ 1,3 M | 0 |
| Plan para entrar al Programa de socios (comercial) | 173 k | 0 |
| Biblioteca de efectos y prueba técnica de profundidad (4 renders) | 324 k | 0 |
| Investigación: capítulo 14, efectos y emoción | 293 k | 0 |
| Short 3 (Jensen Huang y la tarjeta de 1999): análisis de temáticas en dos vueltas 305 k; prompt, perfil emocional y ficha 352 k | 657 k | 0 gastados; 3,7 cotizados de voz |
| Short 3 (regreso de Jensen Huang): prompt de la noticia 390 k; firma del lápiz bumerán 222 k; montaje y tres renders 1,06 M; supervisor en dos vueltas 596 k | ≈ 2,3 M | 3,7 (voz de Tan 1,1 y de Tin 2,6) |
| Short 4 (What Is GTA 6 / GTA 7): brief, dirección y prompt (agentes) + construcción en el motor de acción, composición, sonido y controles (una bifurcación; tokens sin medir) | sin medir | 3,1 (voz de Tin 2,6 y de Tan 0,5) |
