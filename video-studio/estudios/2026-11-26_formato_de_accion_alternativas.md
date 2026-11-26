# Formato de acción de Tin & Tan — alternativas de producción

- **Fecha:** 2026-11-26
- **Pedido del dueño:** el de `canales/nostalgia-tin-y-tan/PARAMETROS.md`, sección 7 (requisitos A1 a A10).
- **Regla de este documento:** una alternativa solo se presenta como válida si puede cumplir **todos** los requisitos. Lo
  que no puede cumplir alguno se dice y se descarta. Nada de aquí está probado todavía: lo que es estimación lo dice.
- **Lo que tengo delante:** en esta sesión hay Python con Pillow y numpy, ffmpeg y un navegador Chromium sin pantalla.
  **No hay** `three.js` ni Blender instalados; instalarlos necesita el sí del dueño.

## 1. Lo que hoy existe y por qué no alcanza

| Requisito | Con lo que hay (`palitos.py` 1.4, `efectos.py`) |
|---|---|
| A1 pelea del género | No. Torso siempre vertical, pies clavados, 9 poses de conversación. La prueba del 2026-11-26 giró la figura entera: se ve rígida |
| A2 aceleración y desaceleración | No. Hay curvas de entrada y salida, no cambios de velocidad del plano ni cámara lenta |
| A3 mundo con profundidad e interacción | No. `componer` mueve capas planas con paralaje y foco; los personajes no pisan, empujan ni rompen nada |
| A4 a A6 fuego, humo, choques, explosiones, implosiones | No existe ninguna función |
| A7 sonidos de golpes | No. El audio por código del short 3 (`codigo/audio.py`) tiene los sonidos de la firma |
| A8 daños que se quedan | No |

## 2. Alternativas

### Alternativa 1 — Mundo 3D por código en el navegador (`three.js` + Chromium), personajes 2D dentro

**Qué es:** una escena 3D de verdad (suelo, paredes, objetos, luces y cámara) escrita en un archivo y grabada fotograma a
fotograma con el Chromium que ya está en la sesión. Tin, Tan y el rival son dibujos 2D de tinta **puestos de pie dentro de
ese mundo**: caminan hacia la cámara y se alejan, pasan por detrás de las cosas, les dan sombra y las rompen. Es la forma
del ejemplo 5 que el dueño pasó el 2026-11-23 (escena 3D por código en un solo archivo).

| Requisito | Cómo lo cumple |
|---|---|
| A1 | Esqueleto de palitos con torso, cadera y articulaciones; poses clave tomadas de la referencia, vista plano por plano |
| A2 | Reloj de la escena con curva de velocidad por plano (cámara lenta y acelerones) y borrón de movimiento |
| A3 | Sí, real: profundidad, oclusión, sombras proyectadas y cámara que se mueve en el espacio |
| A4, A6 | Sistemas de partículas (fuego, humo, chispas), ondas de choque, colapso hacia adentro |
| A5, A8 | Motor de física para cuerpos rígidos: objetos que se parten, grietas y restos que se quedan |
| A7 | Sonido por código (numpy) atado al fotograma de cada impacto, o efectos de biblioteca (ver sección 3) |

- **Costo:** 0 créditos. **Necesita su sí:** instalar `three.js` y una biblioteca de física (paquetes de npm).
- **Riesgos:** que el Chromium sin tarjeta gráfica renderice lento o sin sombras (se sabe con una prueba de 6 s); la
  calidad de la pelea depende de cuánto se trabaje la animación a mano, y es el trabajo grande.
- **Lo que conserva:** Tin y Tan salen idénticos en cada video y todo se puede corregir sin volver a pagar.

### Alternativa 2 — Blender sin pantalla (Grease Pencil: dibujo 2D dentro de un mundo 3D)

**Qué es:** el programa de 3D libre, manejado por código. Su herramienta Grease Pencil existe exactamente para esto:
personajes dibujados en 2D que viven en un espacio 3D. Trae simulación de humo, fuego, cuerpos rígidos y fracturas.

| Requisito | Cómo lo cumple |
|---|---|
| A1, A2 | Esqueletos y curvas de animación completas; cámara lenta por reasignación de tiempo |
| A3 | Sí, real, y es el uso para el que está hecho |
| A4 a A6, A8 | Simulaciones propias de humo, fuego, explosión y fractura |
| A7 | No hace sonido: igual que la alternativa 1 |

- **Costo:** 0 créditos. **Necesita su sí:** instalar Blender (descarga grande).
- **Riesgos:** en un contenedor sin tarjeta gráfica algunos motores de render no arrancan o tardan mucho; **no lo he
  probado aquí**. Es la más capaz y la más pesada de montar.

### Alternativa 3 — Generar los planos de pelea con Higgsfield (la ruta del reel de referencia)

**Qué es:** lo que muestra el reel de sanji.chien: guion por segundos, imágenes de arranque y clips generados. Aquí las
imágenes de arranque serían Tin, Tan y el rival dibujados por código, para que el modelo parta del diseño oficial.

| Requisito | Cómo lo cumple |
|---|---|
| A1, A2 | Es lo que más se parece al género sin animar a mano: el modelo ya sabe mover una pelea de palitos |
| A3 a A6, A8 | Sí, si el prompt los pide; el control fino (qué se rompe, dónde queda) es limitado |
| A7 | Los clips se generan sin audio (regla 10 del estudio): el sonido se pone aparte |

- **Costo:** créditos por cada imagen y cada clip; el reel usa 6 imágenes y 3 clips para ≈ 10 s. **No lo he cotizado**: se
  cotiza con `estimate_video_cost` antes de cualquier generación y se le dice el número.
- **Riesgos:** Tin y Tan «no se generan con IA» (`REGISTRO.md`): el modelo puede cambiarles la cara, los colores o los
  accesorios de un clip a otro; con la regla de un intento por pieza, un clip que salga mal se queda o se paga otra vez;
  los datos, los subtítulos y la firma se ponen encima por código.
- **Necesita su sí:** los créditos, y aceptar que los personajes salgan de un modelo.

### Alternativa 4 — Mixta: mundo y efectos por código (1 o 2) y solo los golpes más difíciles generados (3)

Cumple todo lo de la alternativa de código elegida y compra con créditos solo los 2 o 3 planos donde la animación a mano
no llegue. Es más trabajo de montaje (hay que igualar el dibujo generado con el de código) y hereda el riesgo de
identidad de la alternativa 3 en esos planos.

### Descartada — Ampliar el motor 2D actual con perspectiva falsa

Capas con escala, suelo en perspectiva dibujado y partículas en Pillow. Es lo más barato y lo que se parece a la prueba
de hoy. **No cumple A3 con rigor**: sería profundidad simulada, sin oclusión real ni cámara en el espacio, que es
justo lo que el dueño dice que ya había pedido y no se hizo. No se propone.

## 3. Sonido (requisito A7), común a todas

| Opción | Qué es | Costo | Necesita su sí |
|---|---|---|---|
| Por código | Golpes, choques, explosiones e implosiones sintetizados con numpy, como los sonidos de la firma | 0 | No |
| Biblioteca de efectos de Higgsfield | Buscar y descargar efectos ya hechos | **sin verificar** si consume créditos | Si cuesta, sí |
| Generar el audio | `generate_audio` por efecto | créditos (se cotiza) | Sí |

Partida propuesta: por código, y se sube de opción solo si en la escucha del dueño los golpes suenan pobres.

## 4. Lo que falta para que la pelea sea «casi idéntica» (requisito A1)

Nadie del equipo ha visto el reel plano por plano: solo hay el enlace y el resumen de Keter. Sin eso, «casi idéntica» sería
adivinar. Hace falta el archivo del reel (Instagram pide iniciar sesión desde esta sesión) para pasarlo por
`analizar_video.py` y sacar: poses clave, duración de cada golpe en fotogramas, dónde acelera y dónde frena, qué hace la
cámara, qué se rompe y cómo suena. Se copia esa gramática; no el metraje, ni los personajes negro y rojo, que son de
*Animator vs. Animation*.

## 5. Recomendación del equipo

**Alternativa 1, con una prueba de 6 s antes de comprometer el short 4**, y la alternativa 3 cotizada al lado para que
el dueño compare número contra resultado. Motivo: es la única que cumple A3 de verdad sin créditos y sin poner en riesgo
el diseño de Tin y Tan, y coincide con el ejemplo que él mismo señaló como «forma barata de producir». Si la prueba
muestra que el navegador sin tarjeta gráfica no da, se pasa a la alternativa 2.

Esto es la opinión del equipo; la elección, con su aporte, es del dueño.
