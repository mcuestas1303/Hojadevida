> **EN PAUSA (2026-11-26), por decisión del dueño.** Este prompt se escribió siguiendo la línea del short 3 y su promesa
> de cierre, sin basarse en estadísticas del canal. Regla nueva: ningún prompt sin estadísticas. No se cotiza ni se
> genera. Además, la demanda medida el 2026-11-24 para esta familia («comparación de regresos», «días») era la más baja
> de la lista: 427, 10, 5 y 1 vistas en los Shorts de ese ángulo. Se retoma, se cambia o se descarta con los datos de Studio.

# Brief — Tin & Tan, short 4: «CEO Comebacks Ranked: Jensen Huang vs. Steve Jobs»

> Cumple la promesa con la que cerró el short 3 («Who else came back? Subscribe for the next count.»): el siguiente
> conteo es el de otros regresos de directores ejecutivos, en días, con el mismo método para todos. El short 3 dejó a
> Jensen Huang como vara de medir (11 días); este video lo pone en una lista de seis. Se entiende sin haber visto el 3.

- **Título:** CEO Comebacks Ranked: Jensen Huang vs. Steve Jobs (49 caracteres; `revisar_titulo.py` 1.1: PASA, 0 errores, 0 avisos)
- **Modo:** C desde cero, dibujado por código con `palitos.py` 1.4 y `efectos.py` 1.1 (0 créditos de imagen y video).
- **Objetivo comercial (dueño, 2026-11-23, para todos los canales):** entrar al Programa de socios de YouTube lo antes posible. Textual: «Entonces el objetivo inicial es entrar al programa de socios; todo debe girar en torno a lograr el objetivo a la mayor brevedad posible».
- **Cómo se mide en este video:** se quedó a mirar frente a deslizó (meta: superar el 20,7 % del short 1 y comparar con el short 3, el primero con portada que nombra al sujeto), retención por segundo con el pico en 19,13 s, compartidos y suscriptores por cada mil vistas, tráfico de búsqueda por «ceo comebacks» y por los nombres. Línea base: no hay datos propios de este formato.
- **Público:** quien sigue la noticia de Jensen Huang en EE. UU. y quien busca regresos de directores ejecutivos; sin edad fija (parámetro flexible: manda el dato de Studio). Hispanohablantes con los subtítulos quemados.
- **Para qué es el video:** que quien llegó por Huang entienda en 30 segundos dónde queda su regreso entre otros seis, con las fechas y los números, y se quede con un dato que no traía («Jobs: casi 12 años»; «solo Altman fue más rápido que Huang»).
- **Emoción:** curiosidad en el gancho («¿quién tardó más?») → asombro creciente con cada barra más larga → pico (Jobs, 4.382 días) → remate cerrado → curiosidad nueva («¿cuánto duraron tras volver?»). Alta activación (`manual/14`); sin burla.
- **Plataforma y formato:** YouTube Shorts 9:16, 31,0 s; se reutiliza en TikTok e Instagram.
- **Personajes:** `@tan` pregunta lo que el público se pregunta; `@tin` responde con datos. Ninguna persona real aparece dibujada ni imitada: se les nombra.
- **Presupuesto:** 0 créditos en imagen y video; la voz (dos generaciones, una por personaje) se cotiza con `estimate_audio_cost` y necesita el sí del dueño. Referencia por analogía con el short 3: ≈ 3,5 créditos.
- **Idioma:** inglés de EE. UU. en voz, rótulos y título; subtítulos quemados y `subtitulos_es.srt` en español.

## El ángulo y por qué (decisión del equipo)

**Ranking de seis regresos medido en días sin el cargo, con Huang como vara.** Responde «Who else came back?» con un
número por persona, lo que pide la forma de ranking: cada barra nueva es más larga que la anterior y sube el asombro
hasta el pico. Se descartó la línea de tiempo (seis fechas de 1985 a 2026 en 30 s son demasiadas para leer en vertical)
y la comparación de dos barras (ya la hizo el short 3 con Altman y Jobs). El pico es la barra más larga: Jobs,
4.382 días.

## Datos del video (los únicos que se pueden afirmar)

**Método único para todos:** del día en que la persona deja el puesto de director ejecutivo al día en que vuelve a él
(las dos fechas con día exacto), calculado con `datetime` de Python el 2026-11-24. Se cuenta el cargo, no la empresa: tres
de los seis siguieron en la compañía con otro puesto y eso se dice en la descripción.

| Persona y empresa | Sale del puesto | Vuelve al puesto | Días | Fuente (Wikipedia en inglés, leída el 2026-11-24) | Matiz que se dice en la descripción |
|---|---|---|---|---|---|
| Sam Altman, OpenAI | 2023-11-17 | 2023-11-22 | **5** | «Removal of Sam Altman from OpenAI» (destituido el 17; «reinstated on November 22») | Fue destituido por la junta; no renunció |
| Jensen Huang, Nvidia | 2026-11-12 | 2026-11-23 | **11** | «Jensen Huang» («resigned as president and CEO on November 12»; «On November 23, 2026, Huang was reinstated as president and CEO»; «reinstated … 11 days later») | Renunció. **El comunicado de Nvidia no se abrió**; la fecha del 23 descansa en Wikipedia y en los títulos de las cadenas ya leídos para el short 3 |
| Bob Iger, Disney | 2020-02-25 | 2022-11-20 | **999** | «Bob Iger» («On February 25, the board … named Bob Chapek the new chief executive»; infobox: «October 1, 2005 – February 25, 2020, November 20, 2022 – March 18, 2026 (CEO)»; «returned to Disney as CEO on November 20, 2022») | Fue presidente ejecutivo hasta el 31 de diciembre de 2021; **no salió de la empresa hasta entonces** |
| Michael Dell, Dell | 2004-03-04 | 2007-01-31 | **1.063** | «Michael Dell» («On March 4, 2004, Dell stepped down as CEO, but stayed as chairman … On January 31, 2007, Dell returned as CEO at the request of the board»). **Una sola página** | Siguió de presidente de la junta; **no salió de la empresa** |
| Jack Dorsey, Twitter | 2008-10-16 | 2015-07-01 | **2.449** (≈ 6,7 años) | «Jack Dorsey» («On October 16, 2008, Williams took over as CEO, while Dorsey became chairman»; «In July 2015 … Dorsey assuming the post of interim CEO») y «Dick Costolo» («would step down as CEO on July 1, 2015 … replaced by … Jack Dorsey on an interim basis») | Siguió de presidente; volvió como director **interino** (permanente en octubre de 2015). El día 1 sale de la página de Costolo |
| Steve Jobs, Apple | 1985-09-17 | 1997-09-16 | **4.382** (≈ 12 años: 11,9975) | «Steve Jobs» («on September 17, 1985, Jobs submitted a letter of resignation»; «formally named interim chief executive on September 16» de 1997) | Salió de verdad; volvió antes a Apple en febrero de 1997 con la compra de NeXT (sin día en la fuente); un título del NYT es del 17 de septiembre de 1997: un día de diferencia |

Cuentas con `datetime`: 5 · 11 · 999 · 1.063 · 2.449 · 4.382. Años: 999 d = 2,74; 1.063 d = 2,91; 2.449 d = 6,71;
4.382 d = 11,9975. Veces: 4.382 ÷ 11 ≈ 398 (no se usa en el video).

**Cálculo para el siguiente conteo** (ya con día exacto en las mismas páginas, para cumplir el compromiso del cierre; se
vuelve a verificar al producirlo): Jobs 1997-09-16 → 2011-08-24 (renuncia como director ejecutivo) = 5.090 días; Iger
2022-11-20 → 2026-03-18 = 1.214; Dorsey 2015-07-01 → 2021-11-29 (renuncia anunciada) = 2.343. Dell, Altman y Huang siguen
(o seguían) en el cargo según las páginas leídas: se cuentan hasta la fecha de producción o se dejan fuera, y se dice.

## Decisiones del equipo (2026-11-24), cada una con su porqué

| Decisión | Porqué |
|---|---|
| Forma: ranking en barras, de la más corta a la más larga, con Huang como vara fija | Es la forma que mejor responde «who else» con un número por persona; una barra más larga que la anterior sube el asombro (R37, `manual/14`); se lee en vertical con seis filas de 68 px y nombres de 56 px |
| El gancho es una pregunta de Tan que contiene el hecho que enlaza con el short 3: «Jensen Huang came back as C E O in eleven days. Who took longer?» | Quien no vio el short 3 recibe el dato y la incógnita en una frase; quien lo vio reconoce la vara. Una sola incógnita abierta (R28) |
| Entran seis: Altman, Huang, Iger, Dell, Dorsey y Jobs | Son los únicos con las dos fechas con día exacto y fuente en las páginas leídas hoy |
| **Quedan fuera Howard Schultz y Larry Page** | Schultz: la salida de 2000 no trae día en su página ni en la de Starbucks, y además tuvo tres etapas (2000–2008, 2016–2022, 2022–2023): contarlo mal sería peor que no contarlo. Page: salió en «August 2001» sin día; el regreso (2011-04-04) sí lo tiene. Quedan para otro conteo si se consigue la fecha. La lista no es exhaustiva: no se afirma «todos» ni «el más largo de la historia» |
| El pico es Jobs, 4.382 días, y la voz dice «almost twelve years» | Asombro = magnitud comparada con algo conocido (R37). 4.382 días son 12 años menos un día: si se dice «casi», la voz lleva «almost» (la lección del short 3: la voz sin aproximación y la tarjeta con ella obligaron a un documento de aceptación) |
| **Se repite el dato de Jobs del short 3** | Declarado como riesgo. Se justifica porque la pregunta («¿quién tardó más?») no se contesta sin la barra más larga, y el contexto es otro (cuatro personas nuevas, otra pregunta, otro remate). Si la política de contenido repetitivo lo marca, se mira en los datos antes de repetir el patrón (`plan_programa_de_socios.md`, 4.3) |
| No se cuenta por qué ni cómo salió nadie en el video: la voz no dice «resigned», «fired» ni «scandal». Solo la descripción dice «removed» (Altman) y «resigned» (Huang y Jobs) | Cada salida es un hecho distinto; el video compara días, no personas. Sin escándalo, sin terceros, sin juicio (`PARAMETROS.md`, sección 2). El short 3 ya nombró una vez el motivo de Huang; aquí no hace falta y se evita arrastrarlo a una lista de seis |
| Caras: solo `curiosidad` y `sorpresa` en los datos; `risa` y `feliz` solo en el remate y en la invitación | Nadie sonríe sobre una salida o un despido. No se usa la cara `neutra` de Tin: sigue sin estar en `palitos.py` 1.4 ni en su ficha |
| Cierre: remate («The other four took longer.») + pregunta nueva que el canal puede responder («How long did they stay after coming back?») + una sola invitación («Subscribe for the next count.») + lápiz lanzado | `manual/14`, 4b: se cierra la pregunta de apertura, se deja una nueva sobre hechos públicos y se invita una vez. **Compromiso:** publicar el conteo de permanencia en 7 días, con las fechas de arriba; si no sale, se avisa en un comentario fijado |
| Portada de tres renglones: «CEO Comebacks / Huang 11 Days / vs. Jobs?» | Regla del dueño (2026-11-24): la portada nombra al sujeto con las palabras que se buscan: «CEO» y dos nombres reconocibles. El «11» va a la vista (parámetro flexible): es la vara, no la respuesta; el número de Jobs queda oculto |
| 31,0 s, 12 tomas, 11 cortes | Rango del canal: 15 a 45 s y 8 a 25 cortes en 30 s. El pico llega al 61,7 % (≤ 75 %) |
| Música en re menor a 120 BPM que pasa a re mayor en el pico | Distinta de la del short 2 (do mayor) y del short 3 (mi menor a mi mayor); mismo mecanismo emocional (tensión que se resuelve en asombro) |
| Un cambio grande por video | Cambia la **forma** (ranking de seis, no cuenta lineal de hechos). También cambian la portada (regla nueva) y el cierre (pregunta sobre permanencia): no se podrán separar en la medición; los resultados son «a prueba» (`PARAMETROS.md`, sección 4) |
| Publicar cuanto antes, después del short 3 | La noticia es del 23 de noviembre; cada día pierde demanda |

## Qué se mira de la competencia (lectura del 2026-11-24, de `00_analisis_de_tematicas.md`)

Ya existen comparaciones con el mismo tema, con poca tracción: «Steve Jobs Came Back. Can Jensen Huang?» (427 vistas en
11 h) y «CEO Comeback Speedrun: Jobs vs Huang vs Altman» (10 vistas en 9 h). Lo que este video añade: tres regresos más
(Iger, Dell, Dorsey) con fechas y fuente, un solo método y una descripción que dice qué no mide el número.

## Lo que no se cruza (fijo, `PARAMETROS.md`, sección 2)

Hechos públicos con fuente; sin detalles íntimos ni terceros ni motivos de las salidas; sin burla ni juicio moral; sin
sus caras ni sus voces ni frases puestas en su boca; sin cifras de bolsa ni de fortuna; marcas solo nombradas (sin
logotipo, tipografía ni color), con descargo de no afiliación.

## Lo que no se pudo verificar

- El comunicado de Nvidia (la fecha del 23 se apoya en Wikipedia y en los títulos de las cadenas).
- Michael Dell: una sola página (y su fecha del 4 de marzo de 2004 no se contrastó con otra fuente).
- El día exacto del regreso de Jobs en febrero de 1997 (no se usa) y la diferencia de un día con el NYT (se declara).
- Que los seis sean «todos los regresos conocidos»: no se afirma.
- Ninguna de las páginas de las empresas (Disney, Dell, Twitter, Apple, OpenAI) se abrió.

## Lo que necesita el sí del dueño

- Los créditos de la voz (Tan con Zelda y Tin con Kevin; una generación cada una).
- Publicar.
