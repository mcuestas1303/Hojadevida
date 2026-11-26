# Prueba de la alternativa 4 — mundo 3D por código, personajes 2D dentro (2026-11-26)

- **Qué eligió el dueño:** «Probemos 4 y dejemos las demás alternativas como pendientes después de la prueba». Aprobó la
  hoja v2 del rival («sí apruebo la hoja»).
- **Qué es esta prueba:** la **parte por código** de la alternativa 4: 6 s (179 fotogramas), 1080×1920, 30 f/s, con sonido.
  **0 créditos.** La parte generada (los golpes más difíciles con Higgsfield) está **cotizada y sin generar**: necesita
  su sí con el número a la vista.
- **Instalado** (autorizado al elegir la alternativa 4): `three.js` 0.170.0, solo en esta carpeta (`npm install`). No se
  instaló biblioteca de física: los trozos usan una física sencilla escrita en la escena.
- **Dos pasadas de render** (la segunda corrige cámara, tamaño de las estrellas y cantidad de humo). Es código.

> **2026-11-26, más tarde:** el código de esta prueba se mudó a `video-studio/motor_de_accion/` (ver su `README.md`),
> donde las paletas y el entorno ya son piezas separadas. Aquí quedan el informe, la hoja de contacto y el clip sin generar.

## Cómo se rehace

```bash
npm install                                  # three.js
python3 exportar_sprites.py sprites          # cabezas oficiales de Tin, Tan y el rival (palitos.py y duda_v2.py)
node render.js salida                        # graba los fotogramas con el Chromium de la sesión (≈ 90 s)
python3 sonido.py salida/eventos.json salida/sonido.wav
ffmpeg -framerate 30 -i salida/fotogramas/f_%04d.jpg -i salida/sonido.wav -c:v libx264 -pix_fmt yuv420p -c:a aac -shortest salida/prueba_accion_mundo_3d.mp4
```

El video, el audio y los fotogramas no se suben. `salida/contacto.png` muestra 18 fotogramas.

## Requisito por requisito (`PARAMETROS.md` 2.0, sección 7)

| Requisito | En la prueba | ¿Cumple? |
|---|---|---|
| A1 pelea del género | Caída del rival, embestida y golpe de Tin, el rival sale volando, se levanta y crece, Tan corre y da una patada en el aire, golpe doble final. Esqueleto con torso que se inclina | **A medias.** Se lee como pelea, pero **no se comparó con la referencia** (nadie ha visto el reel plano por plano) y la animación es de un solo pase: poses rígidas entre golpes, pies que resbalan |
| A2 aceleración y desaceleración | Reloj de la escena con velocidad variable: cámara lenta (≈ 0,2×) en cada impacto y ≈ 1,2× en el resto; arranques con curva de aceleración; calco translúcido en lo rápido | Sí, en lo básico. Falta borrón de movimiento de verdad |
| A3 mundo con profundidad e interacción 3D | Escena 3D real: suelo en perspectiva, bloques a distintas distancias, cámara que se mueve dentro del espacio, sombras de los personajes sobre el suelo, el rival pasa por detrás de Tan y cae sobre los cajones, Tan corre desde el fondo hacia la cámara | **Sí** |
| A4 fuego y humo | La cabeza del rival arde y humea; fuego que queda en el suelo tras la explosión | Sí. El fuego es de bolitas suaves: se ve simple |
| A5 choques | Caída contra el suelo, cuerpo contra los cajones, aterrizaje, pilar que cae | Sí |
| A6 explosión e implosión | Explosión con bola de fuego, humo, chispas y dos ondas; implosión final con anillos que se cierran y tinta que se recoge | Sí. Sin blanco a pantalla completa; falta pasarla por `comprobar_destellos` |
| A7 sonidos de golpes | 15 sonidos hechos con numpy, atados al fotograma: silbidos, golpes, choques, madera, explosión, implosión | Sí, pero **suenan sintéticos**: es lo más flojo de la prueba |
| A8 daños que se quedan | Grietas, quemadura, cajones rotos, pilar caído y un garabato del rival quedan hasta el final | Sí |
| A9 rival con cuerpo | Hoja v2 aprobada; el rival de la prueba es ese | Sí |
| A10 color | Papel, tinta y la paleta del canal | **Pendiente:** el dueño no ha repetido qué pidió sobre los colores |

## Defectos que se ven

1. Tin y Tan casi no festejan al final: el plano de cierre queda soso.
2. La bufanda de Tan cae más abajo de lo que marca su ficha en varias poses.
3. Los bloques del fondo son cajas lisas: el mundo se ve vacío. Falta dirección de arte (qué mundo es).
4. El pilar cae fuera de cuadro: el daño existe pero casi no se ve.
5. Sin voz, sin datos en pantalla, sin subtítulos ni firma del lápiz: la prueba solo mide la acción.
6. El render es por software (sin tarjeta gráfica): ≈ 0,5 s por fotograma. Un short de 30 s tarda ≈ 8 min; se puede.

## Parte generada de la alternativa 4 (cotizada, **sin generar**)

Cotización del 2026-11-26 con `estimate_video_cost`, un clip de 5 s en 9:16, solo con texto (con imagen de arranque el
número puede cambiar; se vuelve a cotizar antes de generar):

| Modelo | Créditos por clip de 5 s |
|---|---|
| `seedance_2_0_mini` | 5 |
| `kling3_0` | 10 |
| `seedance_2_5` | 35 |

Para comparar hace falta generar **un** clip del golpe más difícil (propuesta: la patada en el aire de Tan) partiendo de
un fotograma de esta prueba. No se generó: falta el sí del dueño con el modelo y el número.

## Pendientes (después de esta prueba)

| Pendiente | De quién depende |
|---|---|
| Alternativas 1, 2 y 3 del estudio `estudios/2026-11-26_formato_de_accion_alternativas.md` | Quedan en espera por decisión del dueño |
| **Validar si con la tarjeta gráfica del dueño se pueden generar los videos** (pedido del dueño, 2026-11-26). Desde esta sesión de la nube no se puede comprobar: hay que mirarlo desde una sesión conectada a su PC (modelo de tarjeta, memoria, y si corre un modelo de video local o acelera el render de esta escena) | Dueño y una sesión en su PC (Keter) |
| El archivo del reel de referencia, para comparar la pelea plano por plano | Dueño o Keter |
| Qué pidió el dueño sobre los colores | Dueño |
| Sí o no a generar un clip de comparación, con modelo y créditos | Dueño |
| Revisión del director de animación, del director de fotografía y del supervisor | Equipo |
