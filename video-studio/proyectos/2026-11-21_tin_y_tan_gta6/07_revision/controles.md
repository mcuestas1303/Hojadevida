# Controles de calidad — short 2 de Tin & Tan (la espera de GTA 6)

Regla: `video-studio/manual/12_controles_de_calidad.md`. Estado: **video renderizado (v1), revisado con medidas; falta la escucha y faltan las firmas** (ver «Vuelta 1» al final).

## Control de texto (2026-11-21, Generador)

- `revisar_texto.py 02_prompt/subtitulos.srt --idioma en`: 9 textos, **no pasa** por un solo motivo: falta el
  corrector ortográfico (`pyspellchecker`), que se instala con el sí del dueño. Ningún otro hallazgo.
- **Lectura a mano, palabra por palabra** (mientras no haya corrector), de las 9 líneas de voz/subtítulos, los 19
  textos de pantalla de §12 del prompt y el título: sin faltas. Nombres propios: no aparece ninguno en pantalla;
  «GTA» va en mayúsculas por ser sigla. Todas las cifras son enteras (13, 365, 4,745, 3, 4,748, 63, 4,811): no
  hay decimales ni fracciones, así que no hace falta «≈». Separador de miles con coma, correcto en inglés.
- **Falta** (no es de esta etapa): la firma del supervisor de continuidad, y repetir el control sobre la ficha de
  publicación, la miniatura y el texto dibujado en el código cuando existan.

## Control de texto con corrector (2026-11-21, Generador)

El dueño autorizó instalar `pyspellchecker` («sí a todo, instala el corrector»). Instalado con `pip install
pyspellchecker`. «GTA» se añadió a `video-studio/glosario.txt` con su porqué.
`revisar_texto.py 02_prompt/subtitulos.srt --idioma en`: 9 textos, **PASA: 0 errores**.
Falta la firma del supervisor de continuidad y repetirlo sobre la ficha de publicación, la miniatura y el código.

## Vuelta 1 del video (2026-11-21, montaje y render por código)

Pieza: `06_final/tin_y_tan_short02_v1.mp4` (28,5 s, 855 fotogramas). Evidencia y detalle: `07_revision/vuelta_01/notas.md`
(hojas de contacto en `vuelta_01/analisis/`, salidas en `comprobar_video.txt`, `revisar_color.txt`, `revisar_texto.txt`,
`fotogramas/revision.md`; niveles en `05_audio/medidas_audio.json`). Quien montó se revisó primero; **ningún control
está firmado por su responsable todavía**.

| Control (manual 12) | Resultado | Quién | Evidencia |
|---|---|---|---|
| 1. Texto: `revisar_texto.py` sobre `subtitulos.srt`, `codigo/render.py` y `codigo/miniatura.py` (`--idioma en`) | **PASA: 0 errores** (44 textos) | quien montó; **falta la firma del supervisor de continuidad** | `vuelta_01/revisar_texto.txt` |
| 1. Texto leído a mano en las hojas de contacto, glifos y zona segura | PASA: igual que la tabla de §12, sin cuadros, las 12 filas dentro de la zona segura | quien montó; falta el supervisor | `vuelta_01/analisis/hoja_01..03.jpg` |
| 2. Cifras | PASA en pantalla: 13, 365, 4,745, 3, 4,748, 63, 4,811 y 13, enteras y las mismas que la voz del guion y los subtítulos; **no recalculadas en esta vuelta** (la cuenta está en §3 del prompt) | falta el supervisor | prompt §3 |
| 3. Voz y audio: sonoridad | **PASA con medida**: −14,0 LUFS, pico real −1,3 dBTP (archivo final) | quien montó | `comprobar_video.txt`, `medidas_audio.json` |
| 3. Voz y audio: transcripción contra guion, clics, música que tape la voz | **NO COMPROBADO: nadie ha escuchado la voz ni la mezcla** | **falta el diseñador de sonido** | `notas.md`, «No se pudo comprobar» |
| 4. Imagen: personajes contra ficha, nada tapado | PASA a la vista (lados, espejo, colores, objetos de mano de las fichas); Tan ya no sale con `concentrado` (se leía como enojo); el mando quedó dentro de la zona segura (x 109–971); el calendario sale 6 px en la toma 12 | falta el supervisor | `notas.md`, defecto 2 |
| 4.5 Portada del Short | `06_final/portada_short02.png` (1080x1920; texto en x 114–850, y 484–686, dentro de la zona útil). En el video el «GTA 5?» va en y = 288, fuera de esa zona | falta el supervisor | `notas.md`, defecto 10 |
| 5. Video: formato | PASA: 1080x1920, 30 fps, H.264, yuv420p, AAC, 28,5 s | quien montó | `comprobar_video.txt` |
| 5. Video: `revisar_fotogramas.py` | PASA: «Sin marcas» (ni congelados, ni vacíos, ni destellos) | quien montó | `vuelta_01/fotogramas/revision.md` |
| 5. Video: bucle | PASA con medida (el último fotograma empalma con el 0) | quien montó | `comprobar_video.txt` |
| 5. Video: cortes contra la voz | Con medida: ningún corte llega tarde; cuatro pisan el final de la línea anterior (0,04 a 0,15 s) y el de 25,5 no tiene margen. **Falta comprobarlo al oído** | falta el editor y el diseñador de sonido | `notas.md`, defecto 3 |
| 8. Color: `revisar_color.py` | PASA con medida: ≈ 93 % en paleta, saturación ≈ 17 %, variación ±2 %; mostaza único acento y tomate solo en las tomas 10, 11 y 12 (la cifra «4,811» sigue en la 11) | quien montó; **falta la firma del supervisor** | `vuelta_01/revisar_color.txt` |
| Rúbrica (`07_revision/`) | sin puntuar | — | — |
| 6. Entrega | no corresponde todavía (faltan la escucha y las firmas) | — | — |

**Segundo render de la vuelta 1 (2026-11-21, ajustes de la coordinación):** cifra «4,811» en tomate de 22,5 a 25,4
(toda la toma 11), «GTA 6» de 19,4 a 20,9, Tan con `curiosidad` en la toma 5 y mando de 800 px. Se repitieron todos los
controles de la tabla sobre el archivo nuevo, con el mismo resultado (texto 0 errores, fotogramas sin marcas, color
≈ 93 % en paleta, −14,0 LUFS y −1,3 dBTP, bucle que empalma, prompt con 0 errores). Sigue sin escucha y sin firmas.

## Firmas del supervisor de continuidad (2026-11-23, sobre el archivo del 2026-11-23 16:27)

Revisión hecha de cero. Detalle, evidencia y lista completa de defectos: `07_revision/vuelta_01/firma_supervisor.md`
(hojas propias en `vuelta_01/supervisor/`). **Veredicto general: CAMBIOS.**

| Control (manual 12) | Resultado | Firma | Por qué |
|---|---|---|---|
| 1. Texto | NO PASA | **NO FIRMADO** | El `.srt` dice «G T A five» y «G T A six» en las líneas 1 y 2 (y «GTA 5» en la 3); la descripción da 2 errores en `revisar_texto.py` («Xbox» y «Rockstar» fuera del glosario); los dígitos clave con trazo («5», «3», «6», «13», «63») salen deformados. El texto en pantalla, leído a mano, no tiene faltas |
| 2. Cifras | PASA CON SALVEDAD | **FIRMADO** | Recalculado: 4.745, +3 = 4.748, +63 = 4.811; contadores que solo suben; fechas y bloques bisiestos correctos. Salvedad: el número llega 0,2 s antes que su `pop` y su ding (22,3 contra 22,5 s) |
| 4. Imagen | NO PASA | **NO FIRMADO** | Palanca del mando que corta el contorno; Tan con `pensando` de 15,0 a 21,0 s se lee como molestia; 9 px fuera de la zona segura en la toma 12 |
| 4.5 Portada | NO PASA | **NO FIRMADO** | En el video «GTA 5?» va en y ≈ 288–380, fuera de la zona útil (380–1440) y de la franja 400–700; `portada_short02.png` cumple, pero no es el fotograma 0; sin caras |
| 5. Video | PASA CON SALVEDAD en lo técnico | **NO FIRMADO** | Formato, fotogramas, destellos y bucle pasan; pendiente del nuevo render que exigen los controles 1 y 4, y del control 3 |
| 7. Marca del canal | PASA CON SALVEDAD | **FIRMADO** | Paleta, tipografía, capitalización y lados según `DESIGN.md`. Salvedad: el lápiz de Tin no aparece en todo el video |
| 8. Color (medición) | PASA CON SALVEDAD | **FIRMADO** | Video ≈ 93 % en paleta, portada ≈ 95 %, tramo 21,0–27,5 s ≈ 94 %; ±2 % entre segundos; tinta/papel 12,6:1; tinta/tomate 3,5:1 aceptado en 3b; falta copiarlo a `ficha.json` cuando exista |
| Rúbrica | no existe | — | Ni en `07_revision/` ni en el prompt hay criterios con puntaje; §10 y §14 se repasaron como lista |
| Título (`revisar_titulo.py`) | PASA con `--proyecto` y `--descripcion` | — | Sin `--proyecto` da M13 contra su propia entrada en `titulos_usados.json` |

**Tercer render de la vuelta 1 (2026-11-23, cambios pedidos por el supervisor de continuidad y el diseñador de
sonido):** subtítulos con «GTA 5» y «GTA 6»; «GTA 5?» de las tomas 1 y 13 en posición de portada (y 492–682) y la
portada es el fotograma 0; dígitos abiertos de Inter con trazo de 0,045 em; «Xbox» y «Rockstar» en el glosario; Tan sin
`pensando`; palancas del mando a la misma altura; `pop`, tomate y ding en el fotograma de llegada (22,53 s); lápiz de
Tin en la toma 4 con la cabecera de la hoja en marrón; la fecha entra en 6,6 s; toma 12 dentro de la zona segura;
fundido final de la voz de 0,20 s. Detalle, defecto por defecto, en `vuelta_01/notas.md`, «Tercer render».

| Control | Resultado sobre el archivo nuevo | Firma |
|---|---|---|
| 1. Texto (`revisar_texto.py`: srt, `render.py`, `miniatura.py`, descripción de §8) | PASA: 53 textos, 0 errores | **pendiente de que el supervisor vuelva a revisar** |
| 3. Voz (`revisar_voz.py` sobre el mp4, guion completo) y sonoridad | 75 palabras, 0 diferencias; −14,0 LUFS, −1,3 dBTP | firmado con salvedades sobre el render anterior; la voz solo cambió en el fundido final. **Sin escucha humana** |
| 4 y 4.5. Imagen y portada | dibujo dentro de la zona segura en todos los fotogramas (x 100–980, y 256–1662); portada = fotograma 0, texto en y 492–682; sin caras en la portada (decisión pendiente del director creativo) | **pendiente del supervisor** |
| 5. Video (`comprobar_video.py`, `revisar_fotogramas.py`) | formato correcto, sin marcas, bucle que empalma | **pendiente del supervisor** |
| 8. Color (`revisar_color.py`) | ≈ 93 % en paleta (portada ≈ 95 %), ±2 % | firmado sobre el render anterior; cambió el acento de la toma 4 (lápiz en lugar de cabecera) |
| Título (`revisar_titulo.py` con `--proyecto` y `--descripcion`) | PASA: 0 errores, 0 avisos | falta la revisión humana del director creativo |

## Firmas del supervisor de continuidad, segunda revisión (2026-11-23, tercer render, archivo de las 16:48)

Revisado de cero sobre el archivo nuevo. Detalle: `vuelta_01/firma_supervisor.md`, «Segunda revisión (tercer render)»;
hojas en `vuelta_01/supervisor_b/`. Estas firmas sustituyen a las de la primera revisión.

| Control (manual 12) | Resultado | Firma | Evidencia |
|---|---|---|---|
| 1. Texto | PASA | **FIRMADO** | `revisar_texto.py` (srt, `render.py`, `miniatura.py`, descripción): 53 textos, 0 errores; `.srt` leído línea por línea («GTA 5», «GTA 6», «13 years times 365»); dígitos clave limpios en los recortes ampliados |
| 2. Cifras | PASA | **FIRMADO** | 4.745 + 3 + 63 = 4.811 recalculado; contadores que solo suben; 4,811 pasa a tomate en el mismo fotograma en que aparece (22,53 s) |
| 4. Imagen | PASA CON SALVEDAD | **FIRMADO** | Personajes según ficha; Tan sin expresiones que se lean como enojo; mando con palancas dentro del cuerpo; todo el dibujo dentro de la zona segura salvo los fotogramas de borrón. Menores: cabecera de la hoja marrón en la toma 4 y mostaza en las 3 y 9; calendario rozando la visera en la toma 12 |
| 4.5 Portada | NO PASA (un punto) | **NO FIRMADO** | Fotograma 0: «GTA 5?» en x 116–848, y 492–682, 2 palabras, clave en mostaza, sin la respuesta; `portada_short02.png` es el fotograma 0. **Falta:** la portada no tiene caras (punto 5 de la regla del dueño) y la decisión no está escrita; con una línea del director creativo en el brief, informada al dueño, se firma sin render |
| 5. Video | PASA CON SALVEDAD | **FIRMADO** | Formato correcto, `revisar_fotogramas.py` sin marcas, 0 destellos, bucle 2,39 de 255, `.srt` igual a la línea de tiempo. El punto 5.4 depende además del control 3 |
| 7. Marca del canal | PASA CON SALVEDAD | **FIRMADO** | El lápiz de Tin ya aparece. Falta anotar en `DESIGN.md` los dígitos `ss01` y el trazo de 0,045 em |
| 8. Color (medición) | PASA CON SALVEDAD | **FIRMADO** | Video ≈ 93 %, portada ≈ 95 %, ±2 %; toma 4 con un solo acento (lápiz); tinta/tomate 3,5:1 aceptado en 3b |
| Título | PASA | — | `revisar_titulo.py` con `--proyecto` y `--descripcion`: 0 errores, 0 avisos; falta la revisión humana del director creativo |

**Cuarto render de la vuelta 1 (2026-11-23, portada):** las tomas 1 y 13 son la portada completa (texto en y 492–682,
mando en y 744–1075 y caras de Tan y Tin en y 1142–1356, dentro de la zona útil, de perfil hacia el mando); «GTA 6»
entra en 19,5 s con la hoja ya en noviembre. Tabla de la regla punto por punto en `vuelta_01/notas.md`, «Cuarto
render». Todos los controles repetidos sobre el archivo nuevo con el mismo resultado (texto 0 errores, voz 75 palabras
sin diferencias, fotogramas sin marcas, color ≈ 93 %, −14,0 LUFS y −1,3 dBTP, bucle que empalma, prompt con 0 errores).
**Control 4.5 (portada): pendiente de que el supervisor lo revise sobre este archivo.** Salvedad anotada: la mirada de
perfil es horizontal y el mando queda por encima de las cabezas.

**Quinto render de la vuelta 1 (2026-11-23, portada):** Tan (`eureka`) y Tin (`sorpresa`) miran el mando con la cabeza
inclinada 25° (`palitos.py` 1.3, `cabeza_giro`); los cuatro botones del mando iguales en el fotograma 0. Tabla de la
regla de portada, punto por punto y con medidas, en `vuelta_01/notas.md`, «Quinto render». Controles repetidos con el
mismo resultado. **Control 4.5 (portada): pendiente de la firma del supervisor sobre este archivo.**

## Firmas del supervisor de continuidad, tercera revisión (2026-11-23, quinto render, archivo de las 17:10)

Revisado sobre el archivo nuevo; la portada, de cero y con medidas propias. Detalle: `vuelta_01/firma_supervisor.md`,
«Tercera revisión (quinto render)»; hojas en `vuelta_01/supervisor_c/`. Estas firmas sustituyen a las anteriores.
**Veredicto general: APROBADO.**

| Control (manual 12) | Resultado | Firma | Evidencia |
|---|---|---|---|
| 1. Texto | PASA | **FIRMADO** | `revisar_texto.py` (srt, `render.py`, `miniatura.py`, descripción): 53 textos, 0 errores; `.srt` y textos en pantalla leídos a mano |
| 2. Cifras | PASA | **FIRMADO** | Mismos valores y contadores que en la segunda revisión; 4.745 + 3 + 63 = 4.811 |
| 4. Imagen | PASA CON SALVEDAD | **FIRMADO** | Tomas 1 y 13 nuevas según las fichas (inclinación de cabeza anotada); todo dentro de la zona segura salvo los borrones; «GTA 6» entra ya con la hoja de noviembre. Menores: cabecera marrón en la toma 4; calendario rozando la visera en la toma 12 |
| 4.5 Portada | PASA CON SALVEDAD | **FIRMADO** | Fotograma 0 = `portada_short02.png` (1080×1920). Texto x 116–848, y 492–682; mando x 240–840, y 745–1075; Tan x 114–310; Tin x 745–962. Caras con sorpresa y mirando al mando. Huecos mínimos 46 y 60 px. Salvedad: el contorno de atrás de la gorra de Tin pasa de x = 960 por 2 px (5 con el rebote); `notas.md` dice 955–958 |
| 5. Video | PASA CON SALVEDAD | **FIRMADO** | Formato correcto, `revisar_fotogramas.py` sin marcas, 0 destellos, bucle 1,68 de 255. El punto 5.4 depende además del control 3 |
| 7. Marca del canal | PASA | **FIRMADO** | `DESIGN.md` ya recoge los dígitos `ss01` y el contorno de 0,045 em |
| 8. Color (medición) | PASA CON SALVEDAD | **FIRMADO** | Video ≈ 93 %, portada ≈ 94 %, luminosidad ±2 %; tinta/tomate 3,5:1 aceptado en 3b |
| Short 1 con `palitos.py` 1.3 | sin cambios | — | Fotogramas 0, 450 y 800 de `render_v2.py` idénticos byte a byte con `palitos.py` 1.3 y con el 1.2 del commit `139da05` |
| Título | PASA | — | 0 errores, 0 avisos; falta la revisión humana del director creativo |

## Escucha del dueño (2026-11-23)

Textual: «Punto 1 sí escuché y está bien». Cierra la salvedad de escucha humana del control 3 (voz y audio) sobre el quinto render. No es todavía la autorización para publicar.
