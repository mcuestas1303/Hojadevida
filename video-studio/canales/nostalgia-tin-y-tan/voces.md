# Prueba de voces · canal de nostalgia (Tin & Tan)

> **Pendiente, sin empezar.** Decide el dueño. Instalar o pagar cualquier cosa necesita su sí.

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
