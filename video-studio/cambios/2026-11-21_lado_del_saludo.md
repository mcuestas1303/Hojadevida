# Solicitud de cambio — con qué ala saluda Tiky

- **Fecha:** 2026-11-21
- **Origen:** lo detectó el director de prompts al preparar la definición de los clips. No es un pedido del dueño.
- **Estado:** APLICADA (pendiente de la revisión de la psicóloga junto con la definición de los clips)

## El problema

La toma 4 decía que Tiky mira «a su derecha, lejos de Lumi» y levanta «el ala derecha». Con Tiky de
frente a cámara y Lumi a la izquierda del cuadro, la derecha de Tiky es justamente el lado de Lumi:
la frase se contradecía y el generador podía resolverla de cualquier forma. Además, en las tomas
donde saludan los dos, el ala derecha de Tiky es la que queda pegada a Lumi.

## Qué cambia

| Definición | Archivo | Antes | Ahora |
|---|---|---|---|
| Ala con la que saluda Tiky | `personajes/tiky/ficha.md` y las 7 tomas donde saluda | Ala derecha | Ala izquierda: a la derecha del cuadro, del lado contrario a Lumi |
| Dirección de la mirada en la toma 4 | `proyectos/2026-11-20_hola_granja/02_prompt/prompt.md` | «a su derecha, lejos de Lumi» | «hacia la derecha del cuadro, lejos de Lumi» |
| Pezuña con la que saluda Lumi | `personajes/lumi/ficha.md` | No estaba escrito | Pezuña derecha (ya era así en el prompt): a la izquierda del cuadro |

No cambia el guion (dice «mirando hacia un lado, no a Lumi») ni la voz.

## Qué deja de valer

Nada: no hay clips generados y los keyframes muestran a los personajes con las alas y las pezuñas abajo. Costo: 0 créditos.
