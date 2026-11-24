# Revisión, vuelta 1 — short 3 de Tin & Tan («Jensen Huang Is Back as Nvidia CEO After 11 Days»)

Fecha: 2026-11-24. Pieza: `06_final/tin_y_tan_short03_v1.mp4` (se rehace con `python3 codigo/render.py`, unos 160 s).
Todo lo de aquí se comprobó **con medidas y mirando las hojas de contacto** (`analisis/hoja_01.jpg` a `hoja_04.jpg`).
**Ninguna persona ha escuchado la voz ni la mezcla**: lo que depende del oído está en «Sin comprobar».

## Tiempos reales (salen de `codigo/tiempos.py`, que lee `05_audio/linea_de_tiempo.json`)

- Duración: **31,0 s**, 930 fotogramas. Cortes: 1,0; 3,5; 6,5; 9,0; 12,0; 13,0; 14,5; 16,0; 19,0; 22,5; 24,5; 27,0; 30,0.
- Voz: entra en el fotograma 14 (0,467 s; lo pide la firma) y termina en 30,05 s (0,95 s sin voz hasta el empalme).
- Líneas (s): 1 Tan 0,47–3,46 · 2 Tin 3,69–6,55 · 3 Tin 6,78–9,10 · 4 Tin 9,33–11,74 · 5 Tin 11,97–14,23 ·
  6 Tan 14,46–16,12 · 7 Tin 16,35–18,77 · 8 Tin 19,00–22,48 (el número empieza en 20,63) · 9 Tan 22,71–24,49 ·
  10 Tin 24,72–26,73 · 11 Tan 26,96–30,05 (la invitación empieza en 28,29).
- **Pico** (primer fotograma con «4,382» en tomate, ding y golpe de zoom): **22,07 s = 71,2 %**. La cifra queda quieta
  hasta 24,4 s (70 fotogramas). El contador llega ≈ 0,4 s antes de que la voz termine de decir «days» (22,48): se
  adelantó para que el zoom de golpe (13 fotogramas) quepa antes del corte de 22,5.
- Subida 19,43–20,23; silencio de efectos y música 20,23–20,63 (12 fotogramas, en la pausa tras «Apple:»); contador 20,88–22,07.

## Controles y cifras

| Control | Resultado |
|---|---|
| `revisar_voz.py` sobre el video final (`voz_video_final.md`) | **87 palabras, 0 diferencias** |
| `revisar_voz.py` sobre el diálogo solo y sobre cada voz (`voz_dialogo_110.md`, `voz_tin.md`) | 1 diferencia que es del comparador, no de la voz: oye «November 12th» y lo escribe «twelveth» frente a «twelfth» del guion. En `voz_tin.md` además «C E O» frente a «CEO» (mismo caso) |
| `efectos.comprobar_destellos` sobre los 930 fotogramas, con margen de 2 por segundo (`destellos.json`) | **0 cambios bruscos**; mayor salto de luminosidad 5,7 de 255 |
| `postpro.py destellos` | 0 cambios fuertes de brillo |
| `comprobar_video.py` | formato pedido: sí (1080×1920, 30 fps, H.264, yuv420p, AAC 48 kHz, 930 fotogramas); los 13 cortes en la rejilla; ningún tramo de 0,5 s sin cambio; ningún fotograma vacío; sin tinta por encima de y = 250 ni fuera de x 100–980 en la mitad de arriba; media máxima del cuadro 229 (sin blanco a pantalla completa); **−14,0 LUFS, pico real −1,0 dBTP**; un silencio total de 0,4 s en 20,23 (el buscado antes del número) |
| Bucle | el fotograma 930 se dibuja con la misma función que el 0 (idénticos); último frente al 0: diferencia media 0,28 de 255 en el render y 0,57 en el archivo (un paso del vuelo del lápiz) |
| `revisar_fotogramas.py` | sin marcas (detecta 0 cortes porque el fondo es el mismo en todos los planos; los cortes los mide `comprobar_video.py`) |
| `revisar_color.py` | video ≈ **93 %** en paleta, saturación ≈ 16 %, luminosidad ≈ 89 %, ±1 % entre segundos; portada ≈ 93 % |
| `revisar_texto.py` | 0 errores en los textos de pantalla (inglés), las 12 tarjetas en español, `subtitulos.srt` y `subtitulos_es.srt` |
| `entrega.py` sobre `08_entrega/TIN-EN-S-003` | lista para entregar (1 aviso fijo de portada de Short) |
| `validar_prompt.py` | sin errores |
| Portada (`portada_medidas.txt`) | texto y 416–692 (franja 400–700); silla y 715–1104 con su contorno (franja 720–1100); caras dentro de x 60–960, y 380–1440; lápiz a 124 px de la silla, 103 px de la cara de Tin y 217 px de la de Tan |
| Firma (`efectos.comprobar_firma`, en `render.log`) | pasa: velocidad en el empalme 5,4 y 4,7 px/f; giro 4,4 y 4,0 °/f; máximo 66 px/f y 25 °/f; giro total 330°; despejes mínimos 34 px a la silla y 48 px a las caras |
| Subtítulos | renglón más ancho 854 px (máximo 856); 12 tarjetas de 36 a 83 fotogramas; ninguna en la portada |

## Qué se vio en las hojas y qué se corrigió

1. El calendario de la toma 3 (840 × 700, capa lejana) quedaba detrás del panel de subtítulos: se bajó a 840 × 364, por encima de la banda.
2. Con `alto` de 557 px el rodete y la gorra tocaban el panel de dos renglones: los personajes van a **540 px (28,1 %)**.
3. El empuje de cámara anclado en el centro subía las cabezas hacia la banda: ahora se ancla en la línea de suelo.
4. La silla lejana (tomas 2 y 8), la mesa (toma 4) y el calendario (toma 3) rozaban el panel al principio del empuje: se subieron.
5. El zoom de golpe de +10 % sacaba la barra de 880 px de la zona segura 7 fotogramas: ahora la cámara se abre un 9 %
   mientras el contador sube y el golpe la devuelve al encuadre de diseño (nunca pasa de escala 1).
6. `revisar_fotogramas.py` marcó la toma 11 como imagen congelada (22,8–24,2 s): Tan pasa de `pregunta` a `encoge`
   al decir «twelve years?», más viento en la bufanda y un empuje lento; la cifra sigue quieta. Ya no hay marca.
7. El lápiz del pase (toma 13) cruzaba el panel de subtítulos: el arco bajó de 150 a 40 px.
8. La silla de la toma 13 tapaba los brazos: va más pequeña (236 px) y en el suelo, entre los dos.

## Apartes de la especificación (decididos al montar; todos anotados en el código)

- **Firma del lápiz bumerán** (`FIRMA_LAPIZ_BUMERAN.md`, manda sobre el prompt): Tan lanza y Tan atrapa; Tin sin lápiz
  en el plano de firma; la toma 14 dura 30 fotogramas (no 1,5 s); la silla de la portada está quieta (no crece de
  0,82 a 1); el golpe de la clave «11» va en el fotograma 14 (no en el 6, para no pisar el vuelo). Ajustes propios:
  lazo 10 px más abajo (la silla llega a y = 1100); desplazamiento del cuerpo de Tan a la mitad (−4/+5 px) para que
  no patine; **la cara de la anticipación es la de la portada, no `concentrado`** (el prompt la prohíbe).
  Solo se programó la variante de partida (bucle, atrapa Tan). La dirección en el empalme se mide por la tangente:
  por cuerdas de un fotograma da 73° y 83° (la tolerancia de 3° no se cumple así).
- **Portada a 7 % (134 px) en dos renglones**, no al 12 %: «Back In / 11 Days?» en dos renglones al 12 % no cabe entre y 400 y 700.
- **Subtítulos quemados = las 12 tarjetas cortas de la sección 12 del prompt**, no el texto completo de
  `subtitulos_es.srt` (que no cabe a 86 px en dos renglones). Los dos .srt se reescribieron con los tiempos reales.
- Tin señala la mesa (toma 4) con espejo y una pose propia hacia arriba y al centro; `senala` apuntaba hacia fuera.
- Las marcas mínimas de 4 px llevan 3 px de contorno de tinta por lado y sobresalen 12 px de la barra, para que se vean.
- El zoom de golpe vuelve al encuadre de diseño en vez de quedarse en +10 % (punto 5 de arriba).
- Entrega recomprimida con **CRF 26** (2,92 MB); con CRF 22 pesaba 4,21 MB por el grano del papel.

## Sin comprobar o sin resolver

- **Oído humano**: pronunciación de «Nvidia», «Huang», «OpenAI» y «C E O» (el reconocedor las transcribe bien, y eso
  solo dice que se entienden); la cola de «Altman» (cortada a 0,15 s de la coletilla, con fundido de 60 ms); si los
  golpes se oyen bajo la voz; el whoosh y el golpe de la firma; la música.
- La pausa tras «Apple:» se alargó con silencio digital de 0,14 a 0,45 s: puede oírse como un hueco.
- Los cortes de 6,5; 9,0 y 16,0 caen 0,05 a 0,12 s antes de que termine la línea anterior (rejilla de 0,5 s).
- Los números del calendario son pequeños (≈ 24 px en la toma 5) y la flecha del 17 al 23 casi no se lee; la fecha la da el rótulo.
- Las barras de 11 y 5 días son dos marcas sin nombre: quién es quién solo lo dice la voz.
- Tin con `curiosidad` en la toma 4 se lee algo serio (una ceja baja bajo la visera). No se cambió: es la expresión del prompt.
- Faltan las firmas del supervisor, del director de fotografía (color) y del director creativo (título); `direccion.md`
  sigue en plantilla; el código `TIN-EN-S-003` no está anotado en `registro_codigos.md`; `consumo.md` sin actualizar.
