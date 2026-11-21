# Estudio — reel de marca en 20 planos, blanco y negro, corte al golpe

- **Fecha:** 2026-11-21
- **Origen:** lo envió la conversación «Keter: habilidades y crecimiento» con la nota del dueño «Para replicar».
- **Referencia:** reel de una marca de ropa, https://www.instagram.com/p/Df1VfeVAbWO/ (cuenta `lmksilv`).
- **Cómo se vio:** este equipo **no vio el video**; la ficha es de Keter. Antes de escribir un prompt, el
  `analista-de-video` debe verlo con `analizar_video.py` si el dueño deja el archivo en `01_referencia/`.
- **Uso:** se toma la fórmula. No se usa el metraje, la marca, las personas ni la música del original.

## Ficha (según Keter)

| Dato | Valor |
|---|---|
| Duración y formato | 15,9 s, 9:16, 30 fps |
| Voz y texto | sin voz, sin texto en pantalla; la frase va en la descripción («YOU CAN SCROLL. AFTER THIS») |
| Planos | 20 de unos 0,8 s, uno por golpe de una base a unos 75 BPM; corte seco; el último empalma con el primero |
| Imagen | blanco y negro de alto contraste con grano: une material muy distinto |
| Marca | dentro de la imagen (prendas, matrícula, tatuaje, vehículos rotulados), nunca como texto sobrepuesto |
| Contenido | estilo de vida extremo alternado con escenas «imposibles», probablemente hechas con IA |
| Cámara | 16–35 mm para la acción, 85 mm para retratos y animales; contraluz o sol duro, bruma y polvo |

## La fórmula, en lo que sirve al estudio

1. **Un plano por golpe.** El ritmo lo pone la música; la imagen solo tiene que caer en el golpe.
2. **Un tratamiento único tapa las costuras.** El blanco y negro con grano se pone en edición (gratis con
   `postpro.py`) y hace que clips de orígenes distintos parezcan una sola pieza.
3. **Generar largo, usar corto.** Cada clip se genera de 3 a 5 s y se usan los mejores 0,8 s: un defecto en el
   resto del clip no obliga a rehacerlo. Encaja con la regla de un solo intento.
4. **La marca vive en los objetos**, así el video no lleva texto y sirve en cualquier idioma.
5. **Bucle** por empalme del último plano con el primero.

## Qué choca con las reglas del estudio

- **Elenco.** Solo actúan los personajes de `personajes/REGISTRO.md` (Tiky, Lumi, Spike, Tin, Tan). La referencia usa
  personas reales, animales y vehículos fotorrealistas: no hay hoy un personaje del registro que encaje. Lo define el dueño.
- **Público.** Es ritmo de redes para adultos (`prompt_video_redes.md`, proyecto con `--redes`). Nunca Tiky y Lumi.
- **Costo.** 20 clips de 3 a 5 s son de 60 a 100 s generados. Con el precio que ya conocemos (`seedance_2_0_mini`,
  0,5 créditos por segundo en borrador y 1 en 720p) serían del orden de 30 a 100 créditos solo en video, más un
  keyframe por plano (1,5 créditos cada uno, 30 en total). Es una cuenta gruesa, **sin cotizar**; ese modelo además
  no está probado con imagen realista.
- **Marca y etiquetado.** Hace falta saber qué marca propia sale; las escenas realistas hechas con IA se etiquetan
  como tales al publicar.

## Pendiente para abrir el proyecto

Elenco, marca y objetivo comercial: los fija el dueño. Con eso se crea con
`nuevo_proyecto.py <nombre> --redes`, se cotiza y se le presenta el costo antes de generar nada.

## Del mismo lote (sin pedido de aplicar)

- Hoja de personaje de 3 paneles sobre fondo gris: frente y espalda de cuerpo entero, más la cara.
- Hoja de locación como referencia.
- Nombrar lente, luz y película en el prompt («35mm lens, soft window light, shot on Kodak Vision3 500T»).
- Lista de 34 estilos de luz con nombre (Rembrandt, rim, golden hour, venetian blinds, volumetric, teal and orange…).
  Keter no pasó la lista completa; si se quiere en el manual, hay que pedírsela.
