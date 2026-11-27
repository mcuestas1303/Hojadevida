# Origen y licencia de cada recurso

Todo lo que entra al video se anota aquí: imágenes, clips, música, efectos, voces, tipografías.
No se usa metraje ni audio ajeno sin permiso; dar crédito no da derechos.

> Escrito el 2026-11-27 por el comercial, **antes de producir**: es el plan de origen de cada recurso. Ningún archivo existe todavía;
> la columna «Archivo» dice dónde quedará. Cuando producción construya y genere, confirma cada fila con la herramienta y el
> trabajo real (en la voz, el número de trabajo de Higgsfield) y la fecha. **Resumen: todo propio, hecho por código, salvo la
> voz, que es sintética; ninguna música, imagen, tipografía ni metraje ajeno; nada del juego, de la filtración ni del port.**

| Recurso | Archivo | Origen (generado, propio, comprado, libre) | Herramienta o autor | Licencia o condiciones | Fecha |
|---|---|---|---|---|---|
| Voz de Tin (Kevin) | 05_audio/voz_tin_kevin.wav | **generado** (una generación, por hacer, con el sí del dueño; estimación ≈ 2,0 a 2,3 créditos) | Higgsfield `seed_audio`, voz Kevin (`f1373f24-3b96-433f-9a68-e595810ef608`); trabajo: por generar | Uso comercial según el centro de ayuda de Higgsfield (misma base que los shorts 3 y 4); se vuelve a confirmar al generar | por generar |
| Voz de Tan (Zelda) | 05_audio/voz_tan_zelda.wav | **generado** (una generación, por hacer, con el sí del dueño; estimación ≈ 0,6 a 0,7 créditos) | Higgsfield `seed_audio`, voz Zelda (`b7aaea29-0c88-5925-90c0-8f66754cda53`); trabajo: por generar | Ídem | por generar |
| Aceleración de la voz al 110 % | 05_audio/ (mezcla) | propio, edición por código | `codigo/audio.py` del proyecto | Propio. Es ritmo, no evasión de detecciones | por hacer |
| Efectos de sonido (golpes, choques, grieta, regla, papel que se rasga, caída, explosión, implosión, goteo, firma) | 05_audio/efectos.wav (no se sube; se regenera) | hecho por código (numpy), 0 créditos; ningún sonido grabado ni de biblioteca | `codigo/audio.py` y el catálogo del motor | Propio | por hacer |
| Percusión (música sin melodía: `tic_de_regla` y `latido`) | 05_audio/musica.wav (no se sube; se regenera) | hecho por código, 0 créditos; ninguna música ajena ni generada | `codigo/audio.py` | Propio | por hacer |
| Mundo, entorno `patio_tienda_de_computadoras`, piezas y versiones rotas, regla y paquete de tinta, telescopio de cartón, pestaña, fuego, humo | fotogramas del motor | hecho por código (three.js, MIT, instalado con el sí del dueño el 2026-11-26; Chromium de la sesión) | `motor_de_accion/` | Propio; three.js, licencia MIT | por hacer |
| Tin, Tan y el rival (`@duda`, hoja v2) y sus poses | fotogramas del motor | propio: dibujo por código sobre las hojas de personaje aprobadas por el dueño | `motor_de_accion/personajes/`, `palitos.py` | Propio | por hacer |
| Firma del lápiz bumerán, textos, datos, subtítulos y portada | composición | hecho por código (`componer.py`); tipografía Inter Display | `codigo/componer.py` del proyecto | Propio; Inter, SIL Open Font License 1.1 | por hacer |
| Paleta B, noche de tinta | `motor_de_accion/paletas/b_noche_de_tinta.json` | propio | Fotografía y producción del canal | Propio. No usa colores ni tipografía del juego | 2026-11-26 |
| Datos y fuentes de la capa de datos y de la descripción | `publicacion.md` | **no son un recurso gráfico:** hechos con fuente y fecha (Rockstar, PlayStation, Take-Two, Wikipedia, Steam, Malwarebytes, Huntress); las frases son propias, no se copian de ninguna nota | `comercial/2026-11-27_hechos_short5_gta_6_on_pc.md` | Se citan, no se reproducen. Ninguna imagen, logotipo, captura ni texto de las fuentes entra al video | 2026-11-27 |

**Lo que no entra, por regla:** nada del juego (imágenes, capturas, música, tipografía, logotipos, nombres de sus personajes);
nada del port no oficial ni de la filtración (ni su nombre, ni su imagen, ni cómo conseguirlo); ninguna marca como objeto del
mundo (las marcas son solo texto en la capa de datos); ninguna persona real. Si alguna pieza que se agregue no es propia, se anota
aquí antes de usarla.
