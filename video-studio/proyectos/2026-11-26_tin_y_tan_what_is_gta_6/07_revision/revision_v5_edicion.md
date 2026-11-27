# Revisión de edición, versión 5 — TIN-EN-S-004 (editor de video)

Pieza: `06_final/tin_y_tan_short04_v5.mp4` · sha256 `df6b8a638e86` (coincide con el indicado).
Fecha: 2026-11-27.

## 1. Qué miré y qué no

Miré:
- Medidas con ffprobe: H.264, 1080×1920, 30 f/s, 986 fotogramas (32,87 s), AAC mono 48 kHz. Sonoridad integrada −14,0 LUFS. `miniatura.png` de 1080×1920.
- Las 21 tiras de todo el video (tira 1, 4, 8, 15–21 con detalle).
- Fotogramas extraídos a resolución completa: f0, 15, 45, 120, 200, 290, 380, 405, 450, 540, 600, 650, 700, 717, 718, 735, 760, 820, 872, 900, 925, 950 y 985.
- Los 12 subtítulos grabados, recortados a resolución completa (franja y 1372–1552) y leídos uno por uno.
- Las tarjetas de dato: «GTA = Grand Theft Auto» (crece a tres renglones), «the sixth numbered game», «GTA 6 / out since», «13 years, 63 days» y «GTA 7: not announced / as of Nov 26, 2026».
- Portada en el primer segundo, empalme del bucle (f985 contra f0), cortes (por tiras) y la sección 6 de `direccion.md`.

No miré:
- La detección automática de cortes: la salida de ffmpeg salió ilegible y no la repetí. Los cortes los revisé a ojo en las tiras (1 de cada 2 fotogramas).
- Los fotogramas intermedios que no extraje a tamaño completo. Quedan cubiertos por las tiras.
- Las tiras 2, 3, 5–7 y 9–14 solo las hojeé de pasada para confirmar la ausencia de fotogramas muertos.
- La comparación píxel a píxel con la v4: no tengo sus fotogramas a mano. Las comparaciones de tapado se hacen contra mi revisión de la v4.
- El audio: no lo oigo. Solo comprobé la sonoridad.

## 2. Formato y duración

- 1080×1920, 30 f/s, 986 f, H.264, audio a −14,0 LUFS. Cumple.
- Sin `_sin_audio.mp4`, sin `.srt` ni otros intermedios en `06_final/` (solo `fotogramas/`, `miniatura.png` y la pieza).
- El espacio de color del video sigue sin etiquetar (`color_space=unknown`). Es b-10 de la v4 y no bloquea.

## 3. Estado de mis pendientes de la v4

| Pendiente | Estado | Evidencia |
|---|---|---|
| A-1 sección 6 de `direccion.md` | Resuelto con reserva (b) | Ver sección 3.1 |
| b-11 `_sin_audio.mp4` | Resuelto | El archivo ya no está en `06_final/`. |
| M-2 disco fuera de paleta f717–f718 | Sin resolver, sigue M | f717 y f718 a tamaño completo: disco gris azulado translúcido de unos 600 px de diámetro (≈ 280 px de radio) sobre la llama, con puntos amarillo oliva. En la tira 15, el último cuadro (≈ f720) lo muestra también, así que son 2–3 fotogramas (0,1 s). Tono fuera de la paleta C. No bloquea. |
| b-2 tarjetas fuera de zona útil | Sin cambio | La tarjeta de la respuesta (GTA 7: not announced) y ≈ 385–760, 55 px dentro de la zona de acción. La tarjeta «made today by Rockstar Games» llega a x ≈ 980 (> 960). Ninguna tapa caras. Sigue b. |

### 3.1 Sección 6 de `direccion.md` (antes A-1)

El bloque «Vigente desde la versión 3 y confirmado en la 5» (líneas 401–414) coincide con la pieza:
- 986 f, 32,87 s, 1080×1920, 30 f/s: coincide.
- 12 subtítulos en español, grabados, consecutivos, sin `.srt` a YouTube: coincide. El panel mide ≈ y 1378–1550.
- Tarjeta del dato arriba (y ≈ 385–725), acción en medio y subtítulo abajo: coincide.
- Respiro de un solo plano fijo de f750 a f873, que viene del héroe P18 (f719–749): coincide. En las tiras 17–18 no hay corte entre f750 y f873 (la tarjeta de «13 years» entra en f750 y el plano no cambia hasta ≈ f874).
- Tarjeta «rated M» hasta el fin de T6 y tarjeta de la respuesta desde y ≈ 385–397: coincide.
- Sello «as of Nov 26, 2026» y tipografía: coinciden.

Reserva (b): debajo del bloque quedan la tabla de ritmo y la capa de datos con las cifras de la v2 (respiro 697–776, firma 915–944, franja y 905–1085 al 0,82, datos x 100–980). El bloque dice que se conservan «solo como historia», así que no engañan, pero el mapa de ritmo oficial sigue siendo el de la v2. Se puede cerrar sustituyendo la tabla por la medida de la v5. No bloquea la presentación al dueño.

## 4. Lo que cambió en la v5 (planos P4, P5, P7, P15, P18 y P20)

### Subtítulos grabados (12/12 leídos a tamaño completo)
1. «¿Habrá un GTA 7?» (f30–64)
2. «GTA es Grand Theft Auto:» (f84–171)
3. «una serie de juegos / que empezó en 1997»
4. «y que hoy hace / Rockstar Games.»
5. «GTA 6 salió el 19 de / noviembre de 2026.»
6. «Es el sexto juego numerado.»
7. «Suscríbete. Aquí / comprobamos los datos.»
8. «Clasificación M: mayores de 17.»
9. «De GTA 5 a GTA 6:»
10. «trece años y / sesenta y tres días.»
11. «¿Y GTA 7?»
12. «Rockstar no ha anunciado / ninguno. Hasta hoy.»

- Coinciden con `subtitulos_es.srt`, con tildes, signos ¿? y glifos completos. Ninguno se corta ni desborda el panel.
- Cada panel termina cuando entra el siguiente. Hay una pausa sin subtítulo entre f683 y f738 (la voz cuenta la pausa antes de «trece años»), sin voz activa: correcto.
- Sin subtítulo en la portada f0–f29 ni en f915–f944 (solo la portada): correcto.

### Tapado de cabezas o golpes por tarjeta o subtítulo
- f750–f880 (respiro): la tarjeta «13 years» ocupa y ≈ 385–725; las cabezas de Tin y Tan están en y ≈ 870–1080. Humo y bolas de humo pasan por detrás de la tarjeta, pero eso no es un golpe. El subtítulo (y 1378–1550) no toca a nadie. Sin tapado.
- f890–f953 (tarjeta de la respuesta): tarjeta en y 385–760; f900 y f950 a tamaño completo: la cabeza de Tin queda en y ≈ 760–1000 y la de Tan en y ≈ 890–1080, sin solape; en f900 la cima de la gorra de Tin queda a ≈ 5 px bajo el borde de la tarjeta. El estallido gris del fondo queda parcialmente detrás de la tarjeta, no un golpe activo. Sin tapado de cabezas ni golpes.
- f386–f432 (P7, tarjeta «GTA 6 / out since»): en f405 la tarjeta tapa el gancho («?») del rival en la parte alta de la maraña. La cara del rival queda visible y el golpe no se tapa. Vale como M-3 baja, un detalle y no bloquea (ver defectos).
- Resto de planos cambiados (P4, P5, P15, P20): sin tapado nuevo; el subtítulo queda siempre en el tercio inferior, sobre suelo.
- Ningún texto del video tapa una cara. Los paneles opacos cumplen la regla.

## 5. Revisión de portada, bucle, cortes y color

- Portada (f0, primer segundo): «GTA 7? / Facts, Checked», 4 palabras con mayúscula inicial, dentro de x 60–960 e y 380–1440, tipografía del canal, Tan mira el lápiz y el objeto en el centro. El gancho está en el segundo 0. Corte duro de firma hacia f30 (b-1 declarado de versiones anteriores).
- Bucle (f985 contra f0): mismo lápiz en el aire, mismas poses, mismo texto y cámara. Cambia el fondo (ahora destruido contra intacto), excepción D6 declarada. Sin fotograma muerto. Aceptable.
- Cortes: la distribución sigue el mapa de la v4 (portada, ráfagas, subida, ráfaga 2, pico, respiro único, salida y firma). Sin fotogramas muertos al principio o al final de las tomas, sin parpadeos blancos ni negros. Los dos fotogramas de sacudida en f717–f718 son los de M-2.
- Color: paleta C respetada salvo M-2. El acento amarillo va solo en las tarjetas, la mascota y el lápiz.
- Velocidad de lectura del subtítulo: 2 renglones de ≈ 54 px, contraste alto, panel opaco; legible en pantalla móvil.

## 6. Defectos de la v5

| ID | Gravedad | Dónde | Defecto y corrección |
|---|---|---|---|
| M-2 | M | f717–f720 | Disco gris azulado translúcido fuera de paleta (2–3 f). Corrección: `efectos_post`, rama `invertidos` con `mezcla=1.0`, borde de tinta y relleno de paleta, o quitar esos cuadros. Se arrastra desde la v3. |
| M-3 | M (baja) | f ≈ 395–420 | La tarjeta «GTA 6 / out since» tapa el gancho del rival mientras sube al mostrador; cara y golpe visibles. Se puede ignorar. |
| b-A1 | b | `direccion.md` sección 6 | La tabla de ritmo bajo el bloque «Vigente» sigue con cifras de la v2 (marcada como historia). Sustituir por la tabla medida de la v5. |
| b-2, b-4 a b-7, b-10 | b | ver v4 | Sin cambio. Ninguno bloquea. |

Sin defectos B ni A. Lo que cambió en la v5 (coreografía y cámaras) no introduce tapados nuevos graves ni fotogramas muertos. La pieza es presentable al dueño. Recordatorios para la entrega: no subir `.srt` a YouTube y recomponer el sello «as of Nov 26, 2026» con la fecha del día de publicar.

Veredicto: APROBADO

Firma: editor de video · 2026-11-27 (sobre sha256 `df6b8a638e86`).
