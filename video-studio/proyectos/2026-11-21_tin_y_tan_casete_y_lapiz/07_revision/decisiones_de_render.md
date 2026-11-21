# Decisiones de render

Dónde el prompt (`02_prompt/prompt.md`) tenía un hueco o una contradicción, qué se eligió y por qué. Ninguna cifra en
pantalla es nueva: todas salen de la tabla «Datos del video» del brief.

## Imagen

| # | Qué pedía el prompt | Problema | Qué se hizo |
|---|---|---|---|
| 1 | «how many turns?» a 6 % y «rewinding a cassette» a 5 %, en x = 10 %, dentro de la zona segura | A ese tamaño miden 876 y 874 px y la zona segura deja 872 px; además el trazo de 0,05 em pegaba las letras de la palabra clave | Entre las letras de la palabra con trazo hay un espacio igual al trazo, y esos dos textos se reducen lo justo: 5,70 % (109 px) y 4,70 % (90 px). Los demás van a su tamaño |
| 2 | Corchea de 86 px en (50 %, 26 %), «encima del casete y fuera de la etiqueta» (toma 15) | En 26 % la corchea pisa 25 px del casete y 14 de la etiqueta | Centro en (50 %, 24,2 %): queda entre el texto y el casete sin tocar ninguno |
| 3 | En 29,4 «el lápiz sale hacia arriba» (toma 16) y «el lápiz nunca sale de la ventana del casete» | Si sube, cruza la etiqueta | Se encoge hasta desaparecer en 0,2 s mientras sube 0,04 W: nunca sale de la ventana |
| 4 | Cinta a «4,76 marcas por segundo (572 px por segundo)» con marcas cada 12 % del ancho (toma 7) | 4,76 × 129,6 px = 617 px/s, no 572 | Manda el dato: 4,76 marcas por segundo, marcas cada 12 % → 617 px/s |
| 5 | Lápiz de gráfico «de largo 0,22 W» en el carrete del diagrama de 160 px (toma 9) | No hay casete ni W en ese diagrama | 0,9 del diámetro del carrete (144 px), como en la toma 4 |
| 6 | Lápiz de la mano de Tin con movimiento de ±3 grados (toma 9) | `palitos.dibujar` lo dibuja con ángulo fijo | Tin se dibuja con `objeto=False` y el lápiz se dibuja con `palitos.lapiz` en el mismo sitio (misma cuenta de la mano que hace `dibujar`), girado alrededor de la mano. Se usa igual en la toma 6. `palitos.py` no se tocó |
| 7 | Empujes «lentos» (tomas 3 y 6) y empujes con muelle `sello` (2, 4, 10, 12) | El prompt prohíbe lo lineal y `sello` se asienta en 0,4 s (dejaba la imagen congelada) | Lentos: ease-out cúbico en toda la toma. Los demás: toma 2 con `sello`; tomas 4, 10 y 12 con 70 % `sello` + 30 % ease-out cúbico. Todos centrados en (50 %, 50 %) salvo la toma 2 |
| 8 | Borrón en la imagen (sección 6) y «clic de borrón» en la tabla de sonido (sección 13) | La sección 6 dice corte seco en 3,5 y la 13 dice «de borrón» | La imagen sigue la sección 6 (borrón en 1,0; 5,0; 9,5; 12,0; 17,0; 18,5; 23,5; 28,0) y el sonido sigue la sección 13 (clic de borrón también en 3,5). El borrón se aplica a la escena, no al texto |
| 9 | Muelle que debe llegar a una pose exacta (entrada de Tin en 5,6; vuelta al fotograma 0 en 30,0) | Un muelle no termina exactamente en su destino | La respuesta del muelle se divide por su valor al final del tramo: llega justo. El fotograma 900 es idéntico al 0 |
| 10 | Salida de textos: «subir 2 % con ease-in en 3 fotogramas» | No dice si se desvanecen | Suben y bajan de opacidad con la misma curva. La y de la tabla (15 %) es el tope de las letras altas |
| 11 | Casete: etiqueta y ventana solo con relleno | Sobre el marrón quedaban sin borde | Contorno de tinta fino (0,006 W) hacia adentro, dentro de las medidas del prompt; tornillos en papel_sombra con aro de tinta |
| 12 | Entrada de Tin en pose `camina` (una sola pose) | Deslizada sin más parecía patinar | Un pequeño bote vertical de 14 px por paso (tres pasos: 5,0; 5,2; 5,4), atado a los pasos del sonido |
| 13 | Toma 4: giro «con muelle pop en el arranque» | — | El lápiz hace pop de escala (0,85 a 1) y gira a velocidad constante, una vuelta por pulso |
| 14 | Toma 11: «marcas finas, como cuadrícula densa» | — | 192 marcas de 1,4 px que crecen de 20,1 a 20,4; los cortes se alargan según el nivel, como una regla |
| 15 | Toma 9: desenrollado del arco | El carrete (x = 22 %) y el segmento (desde x = 34 %) no se tocan | El arco se borra desde su inicio mientras el segmento crece (503 px, ease-out cúbico) |

Lienzo: `palitos.Lienzo` (supermuestreo x3, reducción LANCZOS). Todo depende del número de fotograma.

## Sonido (no se pudo escuchar: todo lo que sigue es medido)

| # | Tema | Qué se hizo |
|---|---|---|
| A | **Música dentro del video.** La sección 7 dice que «no entra al video hasta que el dueño lo decida»; el encargo de este render pide la mezcla con música a −24 LUFS | El video lleva `mezcla.wav` (con música). También queda `05_audio/mezcla_sin_musica.wav`: cambiarla es una línea de ffmpeg, sin volver a dibujar |
| B | Voz | `dialogo_110.mp3` sin tocar: solo se convierte a 48 kHz y se retrasa 1,0 s. Mide **−14,7 LUFS** (no −14,0), pico real −1,7 dBTP. No se corrigió porque la orden era no modificarla |
| C | «Golpes a −18 LUFS» y «los golpes bajo la voz, a −24 dB respecto a ella» | Lectura literal: los golpes entre 1,0 y 27,9 s se llevan a −38 LUFS (−14 − 24) y los del gancho y el cierre se suben hasta que la pista entera mida −18. Medido: `efectos.wav` **−17,8 LUFS**, pico −3,7 dBTP; bajo la voz −38,0 LUFS; fuera de la voz −15,5 LUFS. Si al oído los golpes bajo la voz quedan demasiado bajos, se cambia `DB_BAJO_VOZ` en `codigo/audio.py` |
| D | Techo de los golpes | Sonidos tan cortos no llegan a −18 LUFS sin recortar: se empujan hasta 6 dB contra un limitador suave (tanh) con techo de −3 dBFS. Eso los redondea un poco; al oído hay que comprobar que no suenen sucios |
| E | Música | Patrón de 120 BPM en do mayor, 15 compases de 2,0 s (C, Am, F, G ×3 y C, F, G): bajo y bombo suave en los pulsos 1 y 3, arpegio en corcheas y shaker a contratiempo. Las colas se envuelven al principio para que el bucle empalme. Medido: **−24,0 LUFS**, pico −10,3 dBTP |
| F | Thunk de 30,0 | El video dura 30,0 s justos: el thunk de 30,0 es el del segundo 0,0 de la vuelta siguiente (es el mismo sonido). No se añadió otro |
| G | Mezcla | Suma sin compresor ni limitador: `mezcla.wav` **−14,5 LUFS**, pico real −1,3 dBTP; sin música −14,7 LUFS, −1,7 dBTP |
| H | Golpes en su tiempo | `audio.py --verificar` lee `efectos.wav` y busca el arranque de cada uno de los 44 golpes: todos empiezan entre 0,1 y 1,7 ms después de su segundo (`05_audio/medidas_audio.json`) |

Sin comprobar al oído: que los cortes de la voz caigan donde dice la sección 6, que los golpes no tapen ni se pierdan y
que la música acompañe. El prompt ya pedía esa escucha antes de publicar.
