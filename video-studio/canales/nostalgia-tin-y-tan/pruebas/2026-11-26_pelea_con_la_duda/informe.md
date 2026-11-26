# Prueba técnica — Tin y Tan pelean contra «la Duda» (2026-11-26)

- **Qué es:** 6 s, 1080×1920, 30 f/s, sin audio, dibujados por código. **0 créditos.** Dos pasadas (la segunda corrige la
  coreografía de la primera; es código, no una pieza generada).
- **Cómo se rehace:** `python3 prueba_pelea.py salida` y luego `ffmpeg -framerate 30 -i salida/fotogramas/f_%04d.png
  -c:v libx264 -pix_fmt yuv420p salida/prueba_pelea_con_la_duda.mp4`. El video y los fotogramas no se suben.
- **Qué se ve:** `salida/contacto_1.png` a `contacto_3.png` (un fotograma cada 0,2 s) y `salida/hoja_personaje_borrador.png`.

## Qué demuestra

| Pregunta | Resultado |
|---|---|
| ¿Se puede inclinar, agachar y hacer saltar a Tin y a Tan sin tocar `palitos.py`? | Sí: cada figura se dibuja en una capa y se gira alrededor de los pies; agacharse y saltar salen de poses como diccionario más un desplazamiento del suelo |
| ¿Se lee el rival sin nombre ni rótulo? | En la hoja, sí: madeja de tinta con rizo de pregunta. A tamaño de celular falta comprobarlo con personas |
| ¿Aparece y desaparece? | Sí: se dibuja de un solo trazo y se borra en sentido contrario; queda un resto |
| ¿Hay golpe legible? | A medias: estrella de impacto, pausa de 3 fotogramas, gotas de tinta y sacudida solo en el golpe final (≤ 16 px, ≤ 8 f) |

## Defectos de la prueba (no se esconden)

1. En el golpe de Tin y en la patada de Tan el cuerpo **se mete dentro de la madeja**: falta medir el contacto para que el
   puño o el pie lleguen al borde y no más allá.
2. En el empujón, Tin **se corta contra el borde derecho** del cuadro durante unos fotogramas.
3. La guardia se lee poco: de frente, los puños quedan pegados al cuerpo. Hace falta la vista de perfil con torso
   inclinado de verdad (no toda la figura girada).
4. No se comprobó con `efectos.comprobar_destellos` ni con `revisar_fotogramas.py`; no hay sonido ni texto.
5. Todo junto se sintió apretado en 9:16: el rival y los dos personajes ocupan el mismo renglón. En producción el rival
   va más arriba o en un plano más abierto, y hay que respetar la franja de subtítulos.

## Estimación de trabajo

Escribir la prueba llevó una fracción del trabajo de un short. Un short de 30 s con esta forma pide: pasar a `palitos.py`
la inclinación de torso y las poses de combate, medir contactos, la coreografía sincronizada con la voz y el dibujo del
rival con sus variaciones. La estimación del estudio (≈ 1,5 a ≈ 2 veces el short 3) no se contradice, pero sigue siendo
una estimación.
