# Brief — Tin & Tan, short 2: la espera de GTA 6

- **Título:** How Many Days Did We Wait for GTA 6?
- **Pedido del dueño (2026-11-21, textual):** «prepara un prompt para tin y tan con temática de gta6 agrega variaciones al sheet si es necesario».
- **Modo:** C desde cero, dibujado por código (método «edición», 0 créditos de imagen y video).
- **Objetivo comercial:** el del canal: presencia y línea base (canal nuevo, sin historial). El dueño no fijó otro para esta pieza.
- **Público objetivo:** EE. UU., adultos de 30 a 50 años que crecieron con la saga. Es más joven que el 45–70 del primer short: ver «Decisiones del equipo».
- **Para qué es el video:** que quien esperó el juego sienta el paso del tiempo y lo comparta («no puede ser tanto»).
- **Emoción principal:** nostalgia → sorpresa.
- **Plataforma y formato:** YouTube Shorts 9:16, 30 s o menos; se reutiliza en TikTok e Instagram.
- **Personajes que salen:** `@tan`, `@tin`.
- **Video de referencia o clip propio:** no hay. Hereda el formato del short 1 (`2026-11-21_tin_y_tan_casete_y_lapiz`).
- **Qué NO se copia:** nada de Rockstar Games ni de Take-Two: ni logotipo, ni letra del logo, ni arte, ni personajes, ni mapa, ni música, ni metraje, ni capturas. El juego solo se **nombra**.
- **Generador de video:** ninguno; `palitos.py` + render por código. Voces: Kevin (Tin) y Zelda (Tan) al 110 %, **sin generar**: necesitan cotización y el sí del dueño.
- **Presupuesto máximo:** 0 créditos en imagen y video; la voz se cotiza aparte.
- **Idioma de voz / texto en pantalla:** inglés de EE. UU.
- **Aprendizaje que aplicamos:** las tres lecciones de la revisión del short 1: el objeto y la voz desde el fotograma 0; gráficos y cifras grandes usando el tercio de abajo; el remate tiene que ser cierto.

## Datos del video (los únicos que se pueden afirmar)

| Dato | Valor | Fuente y fecha |
|---|---|---|
| Lanzamiento de Grand Theft Auto V | 17 de septiembre de 2013 (PlayStation 3 y Xbox 360) | Wikipedia en inglés, «Grand Theft Auto V», abierta y leída el 2026-11-21 |
| Lanzamiento de Grand Theft Auto VI | 19 de noviembre de 2026 (PlayStation 5 y Xbox Series X/S), tras dos retrasos | **Rockstar Games, sitio oficial**, https://www.rockstargames.com/VI, abierto y leído el 2026-11-23: «Grand Theft Auto VI Now Available — November 19, 2026». También Wikipedia en inglés (leída el 2026-11-21) |
| Años completos | 13 | 2013-09-17 → 2026-09-17 |
| Días de esos 13 años | 13 × 365 = 4.745, más 3 días bisiestos (2016, 2020, 2024) = 4.748 | cálculo |
| Del 17 de sept. al 19 de nov. | 13 + 31 + 19 = 63 días | cálculo |
| **Espera total** | **4.811 días** | comprobado con `datetime` de Python |
| Edad de quien nació el día de GTA V | 13 años: ya es adolescente | cálculo |

No se afirma: ventas, vistas de tráileres, clasificación por edades, motivos de los retrasos ni nada del contenido del juego.

## Decisiones del equipo (2026-11-21)

| Decisión | Porqué |
|---|---|
| Ángulo: «¿cuántos días esperamos GTA 6?», contado desde GTA V | Una sola cuenta con dos fechas firmes y una cifra que sorprende; es el formato del canal (pregunta + cuenta + cifra). Comparar las cinco esperas queda para otro video: las fechas de GTA III y San Andreas varían según la fuente |
| Público de 30 a 50 años para esta pieza | Quien jugó la saga en los 2000 tiene hoy esa edad. Es una prueba de línea base con otro público, no un cambio del canal |
| Se nombra el juego y no se usa nada suyo; descargo «Not affiliated with Rockstar Games or Take-Two Interactive» en la descripción | Es el menor riesgo de marca y de reclamo. No es garantía legal: la política de videos de Rockstar no se pudo leer completa |
| Remate: «A baby born that day is a teenager now.» | Es cierto por aritmética (13 años) y no depende de ninguna fuente externa |
| Sin violencia, armas, autos robados ni policía en la imagen | El video trata del tiempo, no del juego; evita restricción de anuncios y mantiene a Tin y Tan en carácter |
| Voz desde el fotograma 0 y bucle | Lecciones del short 1 |
| Portada (2026-11-23, director creativo): el fotograma 0 lleva el mando al centro (y 744–1075), con Tan y Tin debajo, de perfil y con la cabeza inclinada 25 grados hacia arriba, mirándolo; «GTA 5?» arriba (y 492–682), sin la respuesta. Las tomas 1 y 13 son ese mismo plano | Cumple la regla de portada del dueño (`ENTREGA_YOUTUBE.md`, «Portada de los Shorts», 2026-11-21), punto 5 incluido: objeto nostálgico en el centro y las caras de los dos dentro de la zona útil, con sorpresa y mirando el objeto. Sustituye a la portada de solo mando que el supervisor dejó sin firmar (control 4.5). Se mantiene la lección del short 1: el objeto y la voz están desde el fotograma 0. Límite aceptado: en ese plano las cabezas miden 176 px (236 px en el resto del video) |
| Medición (2026-11-23, director creativo): KPI principal «Viewed vs swiped away»; todas las metas son «establecer línea base»; se lee a 72 horas, 7 y 28 días | Canal sin historial: no hay mediana propia contra la que fijar un número, y no se inventa. Detalle en `02_prompt/direccion.md` (secciones 1 y 8) y en `02_prompt/perfil_emocional.md` |

## Lo que decide el dueño

- Generar la voz (créditos; se cotiza cuando el prompt esté cerrado) y renderizar.
- Publicar, y cuándo: el juego salió el 2026-11-19; el tema pierde fuerza cada semana.
