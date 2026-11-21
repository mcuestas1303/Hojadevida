# Caso: Tiky y Lumi en la granja

Registro de cómo se montó el primer par de personajes, para repetirlo con otro. Sigue las fases
de `MANUAL.md`. Se actualiza cada vez que el proyecto avanza.

## Fase 0 — Decisiones del dueño

| Decisión | Respuesta | Fecha |
|---|---|---|
| Público | Niños de 1 a 3 años | 2026-11-20 |
| Para qué | Enseñar y monetizar | 2026-11-20 |
| Quiénes actúan | Solo Tiky y Lumi en los primeros videos; hay secundarios sin definir | 2026-11-20 |
| Género | Tiky es él; Lumi es ella | 2026-11-20 |
| Línea editorial | Nada de identidad de género ni ideología de género | 2026-11-20 |
| Lugar | Una granja. Se planteó como granja de juguete en un cuarto de juegos (sin confirmar expresamente) | 2026-11-20 |
| Idiomas | Español, inglés y portugués de Brasil | 2026-11-20 |
| Voz | Narradora en off (propuesta, sin confirmar); cómo se hará la voz y la música, sin definir | — |
| Formatos | Capítulo 16:9; short 9:16 reutilizable en redes | 2026-11-20 |
| País del titular | El Salvador | 2026-11-21 |
| Generador | Higgsfield, plan Plus | anterior |
| Créditos | Un intento por pieza; todo definido antes; cambios por el equipo | 2026-11-20 |
| Altura de Tiky | Dos tercios de la de Lumi | 2026-11-21 |
| Documentación | Todo queda como plantilla para otros personajes | 2026-11-21 |

## Fase 1 — Los personajes

- Diseñados en otra conversación (rama `claude/focused-thompson-wojzu6`, carpeta
  `creador-personajes/`), con sus versiones 3D aprobadas el 2026-11-08.
- Aquí se cargaron a `personajes/tiky/` y `personajes/lumi/` con su imagen aprobada, su ID de
  Higgsfield, el bloque de identidad y, después de los primeros fallos, la «Definición para generar».

## Fase 2 — La serie

- `series/granja/`: biblia, entorno (lugares: patio, huerto, bebedero, pajar), temario de 8 episodios.
- Estrategias del comercial, con fuentes oficiales: `estrategia_monetizacion.md` (YouTube),
  `estrategia_tiktok.md`, `estrategia_instagram.md`, `evaluacion_vpn.md`.
- Conclusiones que afectan a cualquier personaje nuevo:
  - Un canal «hecho para niños» cobra anuncios contextuales y pierde membresías, comentarios y pantallas finales.
  - Desde el 1 de febrero de 2027 un canal nuevo necesita 1.000 suscriptores y 8.000 horas.
  - El Salvador está en la lista oficial del Programa de socios de YouTube.
  - YouTube no monetiza contenido que parece hecho con plantilla: cada capítulo debe ser distinto.
  - TikTok e Instagram sirven de vitrina; no se usa VPN.
- Dictámenes del equipo: sin compilados, sin alargar capítulos, un short por capítulo, un capítulo por semana.

## Fases 3 a 5 — Capítulo 1, «Hola, granja»

| Paso | Resultado |
|---|---|
| Objetivo | Saludar con la mano; 18 a 24 meses. Se dejó fuera «reconocer por el nombre» |
| Guion | 88 s, 13 planos, dos preguntas con pausa de 5 s. Aprobado en la tercera vuelta (9 cambios y luego 4) |
| Frases fijas | «Esta es la granja. Hola.» / «Ahora, a jugar. Adiós.» y sus versiones en inglés y portugués |
| Idiomas | Voz en tres idiomas aprobada; la psicóloga corrigió tres frases |
| Prompt | 16 tomas, imagen→video, cámara fija; con restricciones críticas; validado y archivado |
| Rúbrica | 38 criterios, 17 críticos, en seis disciplinas |
| Publicación | Paquete en tres idiomas |

Archivos: `proyectos/2026-11-20_hola_granja/` y `personajes/tiky/prompts/capitulos/`.

## Fase 6 — Generación

| Fecha | Pieza | Créditos | Resultado |
|---|---|---|---|
| 2026-11-20 | Keyframe C, intento 1 | 1,5 | Descartado: Tiky tan alto como Lumi, sin crayón, con una ventana |
| 2026-11-20 | Keyframe C, intento 2 | 1,5 | Válido. Se repitió sin autorización del dueño; de ahí salió la regla de un intento |
| 2026-11-20 | Keyframes A, B y C-entrada | 4,5 | Válidos |

- Total gastado: 7,5 créditos.
- Clips: definición de las 16 tomas escrita, 44 créditos cotizados a 480p. Pendiente de la
  revisión de la psicóloga y de la autorización del dueño.

## Cambios registrados

`cambios/`: encuadre de Lumi (aplicado), altura de Tiky (aplicado), lado del saludo (aplicado),
lo aprendido de dos videos de Instagram (aplicado en parte; pendiente el motor de gráficos por código).

## Pendiente

- Autorizar la generación de los clips, por etapas.
- Voz de la narradora y música: quién y con qué se hacen.
- Personajes secundarios de la granja.
- Confirmar granja de juguete y narradora en off.
- Motor de gráficos por código para piezas dirigidas a adultos.
