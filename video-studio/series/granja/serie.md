# Serie: Tiky y Lumi en la granja

Biblia de la serie. La leen el equipo creativo y `validar_prompt.py` (las líneas de «Reglas
que comprueba el validador» no se renombran).

## Reglas que comprueba el validador

- **Público:** 1 a 3 años
- **Elenco permitido:** @tiky, @lumi
- **Duración máxima del episodio:** 90 s
- **Duración mínima de toma:** 4 s
- **Cámaras permitidas:** fija, paneo lento, acercamiento lento, alejamiento lento, seguimiento lento
- **Términos prohibidos en prompts:** fast cut, quick cut, whip pan, crash zoom, shaky, handheld, flash, strobe, glitch, flicker, lens flare, explosion, scary, storm, text, subtitle, caption, logo
- **Idiomas:** es, en, pt-BR
- **Requiere revisión aprobada:** sí
- **Requiere ficha técnica:** sí

## Quiénes salen

En los primeros videos solo actúan Tiky y Lumi (decisión del dueño, 2026-11-20). Los
personajes secundarios de la granja todavía no tienen ficha: mientras no la tengan no entran
al elenco, no tienen nombre ni acción, y como mucho se oyen fuera de cuadro o se ven quietos
al fondo. Para sumar uno se crea su ficha en `personajes/` y se agrega a «Elenco permitido».

## Línea editorial

Decisión del dueño (2026-11-20), válida para todo el contenido del estudio:

- Tiky es él y Lumi es ella. Su género es fijo en todos los idiomas y no es tema de ningún episodio.
- El contenido no trata identidad de género ni ideología de género, en ningún idioma ni
  formato: ni en guiones, ni en títulos, descripciones, etiquetas o miniaturas.

## La pareja

| | Tiky | Lumi |
|---|---|---|
| Papel para el niño | Es él: pequeño, curioso, quiere hacerlo solo | Es el adulto que acompaña: observa, espera y muestra |
| Qué hace | Descubre, pregunta, intenta, se equivoca, repite | Nombra, muestra despacio una vez, deja que Tiky lo haga |
| Qué no hace | No se burla ni hace travesuras peligrosas | No regaña, no lo hace por él, no premia |
| Gesto propio | Se inclina hacia adelante en puntas de pie y ladea la cabeza cuando algo le da curiosidad | Se lleva una pezuña al mentón antes de mostrar algo; saca el crayón solo para marcar o dibujar |

Tiky va adelante y Lumi lo sigue. Lumi es más alta: en los planos de los dos, la cámara queda
a la altura de los ojos de Tiky.

## Estructura de cada episodio

| # | Momento | Duración | Qué pasa |
|---|---|---|---|
| 1 | Saludo | 8–10 s | Siempre igual: los dos entran, miran a cámara y saludan con el ala y la pezuña |
| 2 | Presentación | 15–20 s | Tiky encuentra el objeto o la tarea. Lumi lo nombra: «Esto es…» |
| 3 | Práctica | 25–40 s | Tiky lo intenta. Dos preguntas al niño, cada una con su pausa. El concepto se repite |
| 4 | Cierre | 8–10 s | Se guarda todo en su lugar. Se dice una vez más la palabra del día |
| 5 | Invitación | 6–8 s | A cámara, para el niño y el adulto: hacerlo en casa con algo real |
| 6 | Despedida | 6 s | Siempre igual: los dos saludan a cámara. Sin gancho para seguir viendo |

## Frases fijas

Fijadas en el capítulo 1 y aprobadas por la psicóloga (2026-11-20). Van palabra por palabra
en todos los episodios, con los mismos gestos y el mismo encuadre de los dos. Están escritas
para narradora en off; si los personajes pasan a hablar, se revisan de nuevo.

- **Saludo (10 s):** «Esta es la granja. Hola.» Los dos entran, miran a cámara y saludan con
  el ala y la pezuña al oírse «Hola»; quedan 2 s con el ala y la pezuña en alto. La música
  suena solo mientras entran y baja en un fundido lento antes de la voz.
- **Despedida (6 s):** «Ahora, a jugar. Adiós.» Los dos saludan a cámara al oírse «Adiós».
  Sin música durante la voz; después entra y se funde despacio. «Hola» nunca se usa para despedirse.

## Idiomas

Español (maestro), inglés y portugués de Brasil. El video es el mismo en los tres; cambia la
pista de voz (`voz_idiomas.md` en cada proyecto) y el paquete de publicación, que el comercial
prepara por mercado. Las frases fijas en los tres idiomas están en «Frases fijas».

## Formatos

- **Capítulo e intro:** video largo, 16:9, de 60 a 90 s, con la estructura de arriba.
- **Short:** 9:16, de 20 a 45 s. Es un solo momento de un capítulo ya aprobado: una pregunta
  con su pausa entera y su respuesta, y termina con la invitación o con la despedida. Como
  máximo uno por capítulo. No se hace un short que sea solo el saludo: en reproducción en
  bucle se repetiría sin fin (veto de la psicóloga, 2026-11-20). Lleva su propia ficha pedagógica y pasa por la
  psicóloga igual que un capítulo. Detalle técnico en `video-studio/formatos.md`.

Frases fijas por idioma, aprobadas por la psicóloga el 2026-11-20:

| Frase | es | en | pt-BR |
|---|---|---|---|
| Saludo | Esta es la granja. Hola. | This is the farm. Hello. | Esta é a fazenda. Oi. |
| Despedida | Ahora, a jugar. Adiós. | Time to play. Bye-bye. | Agora, vamos brincar. Tchau. |

La palabra de saludo (hola, hello, oi) nunca se usa para despedirse, en ningún idioma.

## Voz y sonido

- Por confirmar con el dueño: **narradora en off** (propuesta, por costo: no exige sincronizar
  labios) o los personajes hablando. Hasta que se decida, los guiones se escriben con
  narradora y los personajes se expresan con gestos y sonidos cortos.
- La voz se graba o se genera aparte y se monta en edición; los clips se generan sin audio.
- Idioma: español.

## Estilo

Figuras de juguete de vinilo mate en 3D, formas redondeadas, colores limpios. Es el estilo
aprobado de Tiky y Lumi; el escenario se construye en el mismo material y a su escala.

Estilo global para todos los prompts de la serie:

```text
Modern 3D cartoon render, soft matte vinyl toy figures, children's animation style, simple rounded shapes, clean bright colors, soft even daylight, gentle soft shadows, uncluttered background, calm and slow, eye-level camera at the chick's height.
```

Negativo global:

```text
text, letters, watermark, logo, extra characters, extra animals, humans, realistic fur, scary faces, sharp teeth, dark shadows, night, fire, weapons, fast motion, motion blur, camera shake, flashing lights
```

## Publicación

- **Canal de YouTube:** Tiky & Lumi (`@TikyAndLumi`, ID `UCO6HZWJfilFtsrI4GBEm2gw`, https://www.youtube.com/channel/UCO6HZWJfilFtsrI4GBEm2gw). Es el canal infantil de la serie (confirmado por el dueño el
  2026-11-21). Su página pública dice que se unió el 20 de noviembre de 2026 y no muestra
  videos ni suscriptores (consultada el 2026-11-21): para la estrategia sigue siendo un canal
  nuevo, sin historial. Los personajes de otros públicos van a otros canales.

- Titular de las cuentas: reside en El Salvador (dato del dueño, 2026-11-20). El Programa de
  socios de YouTube está disponible allí. El comercial evaluó usar un VPN para entrar a
  programas de otros países y lo desaconseja (`evaluacion_vpn.md`); la decisión es del dueño.

- En YouTube va como «hecho para niños».
- Decisión del dueño (2026-11-08): en el contenido infantil no se declara que está hecho con
  IA, porque se produce revisado. Conviene volver a revisar la política vigente antes de publicar.
- Los personajes y la granja son originales: no se imita a pollitos, vacas ni granjas de
  series infantiles conocidas, ni se usan sus canciones.

## Objetivo comercial del canal (dueño, 2026-11-23)

Entrar al Programa de socios de YouTube lo antes posible; rige para todos los canales («Rige para todos los canales
que trabajemos»). En esta serie se persigue sin salirse de `infantil/guia_1_a_3.md`: nada de ganchos para seguir
mirando ni de pedirle nada al niño; lo que se le diga al adulto lo deciden la pedagoga y la psicóloga. Estrategia:
`estrategia_monetizacion.md`.
