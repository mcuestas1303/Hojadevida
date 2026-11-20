# 08 · Audio

El sonido carga la mitad de la emoción y es lo más barato del proyecto. Se diseña con la tabla del cap. 01.

## Capas

| Capa | Fuente | Herramienta | Costo |
|---|---|---|---|
| Voz | grabada por el dueño, o TTS | `seed_audio` (TTS por defecto), `create_voice` para fijar la voz de un personaje, `voice_change` para convertir una voz grabada | 0,3 por frase |
| Labios | si el personaje habla en cuadro | `sync_so` sobre la toma ya aprobada | 3,6 por segundo |
| Música | la pone el dueño (regla actual) o se genera | ElevenLabs Music v2 en Higgsfield (0,77 por 12 s); `suno_music` no está en la cuenta | bajo |
| Efectos | biblioteca libre o generados | `mirelo_text_to_audio` (0,25 por segundo) | bajo |
| Ambiente | generado o biblioteca libre | `mirelo_text_to_audio` | bajo |

**Narradora en off antes que labios:** una voz en off no exige sincronizar labios (ahorra `sync_so`). Es la opción
por defecto de la serie infantil hasta que el dueño decida otra cosa.

## Voces del elenco

Cada personaje con voz tiene **un** ID de voz anotado en su `ficha.md` (línea **Voz:**). Se crea una vez y se
reutiliza; cambiar de voz entre videos rompe la identidad igual que cambiar de cara.

| Personaje | Voz (propuesta, por aprobar) |
|---|---|
| Tiky | aguda, curiosa, frases de 2–4 palabras, ritmo lento para bebés |
| Lumi | cálida, pausada, media-grave, nombra las cosas con claridad |
| Spike | seria, monótona, segura de sí (el humor sale del contraste con su aspecto) |

## Prompts de audio

**Voz (seed_audio):** el texto exacto, con la puntuación que marque las pausas («¿Lo… ves?»). Para bebés, frases
cortas y repetidas.

**Efecto:** qué suena + material + duración + intensidad.
`soft cartoon boing of a rubber toy landing on grass, short, 1 second, gentle`

**Música:** género + tempo (BPM) + instrumentos + emoción + estructura con tiempos.
`playful children's ukulele and glockenspiel, 95 BPM, major key, warm and calm, steady loop, no drums, 30 seconds`
`minimal electro-house, 120 BPM, minor key, quiet intro for 5 seconds then a clear beat drop at second 6`

## Mezcla

- Voz siempre por encima: la música **se agacha** cuando hay voz (`postpro.py mezclar` lo hace solo, con ducking).
- Niveles orientativos: voz −16 a −12 LUFS de corto plazo, música −24 a −20 debajo de la voz, efectos según la acción.
- Final a −14 LUFS integrados, picos bajo −1 dBTP (`postpro.py normalizar`).
- En infantil: sin golpes fuertes ni sonidos estridentes; volumen parejo.

## Derechos

No se usa música, voces ni efectos con derechos de terceros. En TikTok y Reels se puede usar la música licenciada de
la propia app **dentro de la app**, al publicar; en YouTube, solo la Biblioteca de Audio o música propia.
