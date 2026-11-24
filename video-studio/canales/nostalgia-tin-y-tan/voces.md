# Prueba de voces · canal Tin & Tan

> **En curso desde el 2026-11-21.** Decide el dueño. Instalar o pagar cualquier cosa necesita su sí.

## Qué hay hoy en la PC del dueño

Solo las voces básicas de Windows: Mark, David y Zira en inglés; Raúl y Sabina en español. No hay ninguna librería
de voz instalada.

## Candidatas

| Letra | Voz | Licencia y costo | Qué pide | Nota |
|---|---|---|---|---|
| A | **Kokoro** | código abierto, Apache 2.0; local, gratis, se puede monetizar | instalar `kokoro` y PyTorch para CPU (~1 GB) | — |
| B | **Gemini TTS** | muy natural; unos US$0,0135 por minuto pagando | una llave de API | el nivel gratis permite a Google usar los textos |
| C | Windows Mark / David | incluidas en Windows | nada | solo para comparar |
| D | **`seed_audio` de Higgsfield** (agregada por este equipo) | 0,3 créditos por frase con el plan Plus (cotizado el 2026-11-20) | nada: ya está conectada | **verificar** en los términos de Higgsfield que permite uso comercial antes de elegirla |

Fuera por ahora: **ElevenLabs**, porque pide crear una cuenta y su opción gratis no permite uso comercial.

## Método (a ciegas)

1. El mismo texto de unos 60 s (por ejemplo, el guion de la prueba de 30 s más 4 líneas) con cada voz.
2. Archivos con letras (A, B, C, D) sin decir cuál es cuál; también se mezcla el orden.
3. Mismo volumen para todas (`postpro.py normalizar`, −14 LUFS) para que no gane la que suena más fuerte.
4. El dueño escucha, elige una para Tan y una para Tin, y recién entonces se revela qué voz era cada letra.
5. La elegida se anota en la línea **Voz:** de la ficha de cada personaje y en `../README.md`.

## Prueba en curso (2026-11-21, conversación «Generador de prompts»)

El dueño pidió hacer la prueba de sonido con Tin y Tan y eligió él mismo la voz a probar, sin prueba a ciegas.

| Fecha | Personaje | Voz | Texto | Créditos | Resultado |
|---|---|---|---|---|---|
| 2026-11-21 | Tin | Arthur (`30fc8796-ceb6-4a66-b3a7-4a145ef7f346`) | — | 0 | No se generó: el dueño cambió de voz antes y denegó la generación |
| 2026-11-21 | Tin | **Kevin** (`f1373f24-3b96-433f-9a68-e595810ef608`), `seed_audio`, ajustes por defecto | Las 5 líneas de Tin del guion del casete | 2,2 | ID `6ec0447b-6c43-4766-9a35-c4852b277c2d`, 21,8 s, `pruebas/voces/tin_kevin.wav`. Motivo del dueño: «tiene una energía más encendida al hablar». **Aprobada** |
| 2026-11-21 | Tan | **Zelda** (`b7aaea29-0c88-5925-90c0-8f66754cda53`), `seed_audio`, ajustes por defecto | Las 3 líneas de Tan del guion del casete | 0,8 | ID `86027f63-40fe-4a81-bdb3-4dd4b08e5483`, 12,5 s, `pruebas/voces/tan_zelda.wav`. **Aprobada** |

- Cotización del mismo día: las 5 líneas de Tin, 2,2 créditos; las 3 líneas de Tan, 0,8 créditos (el precio depende del largo del texto, no es fijo por frase).
- Uso comercial en Higgsfield: su centro de ayuda dice que no reclama propiedad de lo generado, audio incluido, ni restringe el uso comercial, y que no depende del plan ([fuente](https://higgsfield.ai/creator-hub/help-center/account-and-privacy/who-owns-my-generations-and-can-i-use-them-commercially), visto en resumen de buscador el 2026-11-21; conviene leer los términos completos antes de publicar).
- Total gastado en la prueba de voces: 3 créditos.

## Resultado (2026-11-21)

- **Tin: Kevin. Tan: Zelda.** Decisión del dueño, textual: «Ambas voces me gustan pero para el tipo de video necesita más energía y creo que eso se logra acelerando un poco la reproducción; tómalo en cuenta para cuando se esté trabajando».
- **Regla del canal:** la voz se acelera un poco en edición, sin cambiar el tono (`atempo` de ffmpeg) y sin volver a generar. Es gratis.
- Para elegir la velocidad se armó el diálogo completo en el orden del guion, con cada voz normalizada a −14 LUFS, a cuatro velocidades: `pruebas/voces/dialogo_tin_y_tan_velocidad_100.mp3` (original, 29,9 s), `_110` (27,2 s), `_115` (26,0 s) y `_120` (24,9 s). **Elegida por el dueño el 2026-11-21: 110** («me gusta 110»). Es la velocidad fija del canal: toda voz se acelera un 10 % en edición (`atempo=1.10`) y se normaliza a −14 LUFS.
- Los cortes entre líneas se hicieron por las pausas detectadas, sin escuchar el audio: conviene comprobar al oído que ninguna línea quedó cortada.
- Por probar más adelante (cuesta créditos, necesita autorización): el modelo tiene un ajuste propio de velocidad del habla (`speech_rate`) y otro de intensidad de la expresión; podrían dar más energía que acelerar en edición.
- Las voces de Windows, Kokoro y Gemini no se probaron: el dueño eligió directamente entre las de Higgsfield.
