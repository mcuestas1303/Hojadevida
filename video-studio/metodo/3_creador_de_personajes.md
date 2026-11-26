# Método del Creador de personajes — del pedido al personaje en el elenco

> **Origen:** pedido del dueño (2026-11-26): «si el prompt, según el universo, estipula que hay algún personaje que no
> está creado, entonces deberá darle todos los detalles al creador de personajes; por tanto el creador de personajes
> también debe definir el método». El procedimiento largo, fase por fase, sigue en `video-studio/MANUAL.md`; el afinado
> vuelta a vuelta, en la habilidad `/afinar-personaje`. Este archivo fija la entrada, la salida y las bifurcaciones.
> Versión 0.1. Caso que lo probó: el rival de Tin y Tan (2026-11-26), creado en dos vueltas.

## 1. Qué recibe: el pedido de personaje

Plantilla: `plantillas/pedido_de_personaje.md`. Sin estos renglones el Creador no empieza:

| Renglón | Por qué |
|---|---|
| Quién lo pide, para qué video o tanda y para cuándo | Prioridad |
| **Papel en el universo:** qué es dentro de la metáfora, de dónde viene, qué quiere, qué relación tiene con los demás | Sin eso es un dibujo, no un personaje |
| Qué hace en pantalla en el primer video (acciones, poses, si habla) | Define la hoja mínima |
| Público medido y canal | Tono, intensidad, color |
| Lo que no puede ser ni parecer (línea editorial, personas reales, marcas, personajes ajenos, público infantil) | Borde |
| Cómo se va a dibujar (código, generado o mixto) y en qué motor | Define el entregable técnico |
| Si tiene nombre en pantalla, voz y sonidos | Ficha y voz |
| Qué se sabe del dueño: frases textuales, gustos y disgustos ya dichos | Evita vueltas |

## 2. Los pasos

| Paso | Qué hace | Quién | Sale |
|---|---|---|---|
| C1 | **Leer** el pedido, el universo del canal, las fichas de los personajes con los que convive y las estadísticas | Creador | Dudas, si las hay, en una sola tanda |
| C2 | **Concepto:** qué es, en una frase; qué lo hace reconocible en miniatura; qué nunca cambia | `afinador-de-personajes` | Borrador de ficha |
| C3 | **Revisión de atención y público:** para quién está diseñado frente al público medido; qué frena el dedo | `revisor-de-atencion` | Sección de revisión en la bitácora |
| C4 | **Primer dibujo** por la ruta pedida. Por código: 0 créditos. Generado: cotizar y pedir el sí; una generación por pieza | Creador | Imagen o función de dibujo |
| C5 | **Hoja de personaje:** vueltas, poses que el universo necesita (no un catálogo genérico), estados, escala junto a los demás | Creador | `referencias/hoja_vN.png` |
| C6 | **Presentar al dueño** la ficha y la hoja. Sus correcciones se aplican vuelta a vuelta y quedan en la bitácora con su texto textual | Creador | Su sí, o la vuelta siguiente |
| C7 | **Cerrar la ficha:** bloque de identidad, definición para generar o dibujar, medidas, lista de comprobación, lo que nunca cambia, variaciones permitidas, prohibido | Creador | `personajes/<id>/ficha.md` |
| C8 | **Registrar:** fila en `personajes/REGISTRO.md`; carpeta en el Drive | Creador | Personaje disponible para prompts |
| C9 | **Entregar al motor:** función de dibujo o sprites por paleta, poses como datos, entrada en el catálogo | Creador con producción | Personaje usable en la escena |
| C10 | **Avisar** al Generador y al equipo en `COORDINACION.md` | Creador | Pedido cerrado |

## 3. Bifurcaciones

| Si… | Entonces… |
|---|---|
| El personaje es para público infantil | Pasa además por `pedagoga-montessori` y `psicologa-infantil`, y vive en otro estante: nunca se cruza con los de adultos |
| Se dibuja por código | La función es el diseño oficial; la hoja se saca de la misma función que pinta los videos |
| Se genera con IA | Definición cerrada, cotización, sí del dueño, una generación por pieza; se guarda lo descartado aparte |
| Es una persona real | Solo el dueño, con sus fotos; nadie más |
| Se parece a un personaje ajeno | No pasa: se rediseña |
| Es para una marca comercial | Manual de marca primero; lo que la marca no permite va en «prohibido» |
| El dueño corrige el concepto | La vuelta anterior queda como historia en la ficha; la nueva dice qué deja sin efecto |
| El personaje ya existe y solo falta una pose u objeto | No es personaje nuevo: variación permitida, se añade a la ficha |
| El universo necesita que cambie de aspecto según la hoja o la paleta | Se define qué cambia (por ejemplo, la línea) y qué no (rasgos y colores de identidad) |

## 4. Qué devuelve

Ficha, hoja aprobada, bitácora de vueltas, fila en el registro, dibujo en el motor y aviso en coordinación. Un prompt
solo puede usar al personaje cuando están las seis cosas.
