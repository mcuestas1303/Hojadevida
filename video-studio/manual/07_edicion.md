# 07 · Edición

La edición es donde más se ahorra: todo lo que se resuelve aquí no se paga en créditos.

Reglas de retención (mapa de ritmo, aceleración final, loop, subtítulos de 1–3 palabras, primer corte de material
grabado): [cap. 11](11_retencion_y_revision.md).

## Ritmo según la emoción

| Emoción / formato | Duración media de plano | Corte |
|---|---|---|
| Humor absurdo (Spike) | 1,5–3 s | seco, en el remate; pausa de silencio antes |
| Energía / trend | 0,5–1,5 s | al beat de la música |
| Ternura / calma | 4–8 s | lento, a veces fundido corto |
| Infantil 1–3 años | 4 s o más (regla de la serie) | sin cortes bruscos; fundidos suaves o corte en reposo |
| Épica («M») | acelera hacia el clímax | al golpe de percusión |

## Técnicas

- **Corte en la acción:** se corta a mitad del movimiento y la siguiente toma lo continúa. Oculta defectos.
- **J-cut / L-cut:** el sonido de la toma siguiente entra antes (J) o el de la anterior sigue (L). Da fluidez.
- **Match cut:** dos tomas con la misma forma o movimiento (el crayón de Lumi → un lápiz real del niño).
- **Loop:** el último fotograma empalma con el primero; el video se repite sin que se note y suma reproducciones.
- **Pausa dramática:** congelar o alargar 0,3–0,5 s antes del remate (`postpro.py velocidad` o duplicar fotogramas).
- **Gancho en el segundo 0:** si la mejor imagen está en el segundo 6, se pone un trozo al inicio («flash-forward»).

## Formatos de salida

| Plataforma | Aspecto | Resolución | Duración que rinde | Notas |
|---|---|---|---|---|
| YouTube Shorts | 9:16 | 1080×1920 | 15–60 s | sin marca de agua de otras apps |
| TikTok | 9:16 | 1080×1920 | 15–60 s (monetiza desde 1 min) | |
| Reels | 9:16 | 1080×1920 | 15–90 s | |
| YouTube largo | 16:9 | 1920×1080 | 3–10 min (infantil) | capítulos, miniatura propia |

**Zona segura 9:16:** nada importante (texto, cara) en el 15 % de arriba ni en el 20 % de abajo ni en el borde
derecho (botones de la app). `postpro.py subtitulos` ya coloca el texto dentro de la zona segura.

**Audio de salida:** −14 LUFS integrados, picos bajo −1 dBTP (`postpro.py normalizar`).

## Subtítulos

En redes la mayoría ve sin sonido: subtítulos grandes, 2–4 palabras por línea, contraste alto, en el tercio central.
El texto **nunca** se genera dentro del video: se escribe en un `.srt` y se quema en edición.
En la serie infantil (1–3 años) no se usa texto en pantalla.

## `herramientas/postpro.py` (gratis, ffmpeg)

```bash
python3 video-studio/herramientas/postpro.py info clip.mp4
python3 video-studio/herramientas/postpro.py recortar clip.mp4 salida.mp4 --desde 1.2 --hasta 4.8
python3 video-studio/herramientas/postpro.py vertical clip_16x9.mp4 salida.mp4 --modo desenfoque   # o --modo recorte
python3 video-studio/herramientas/postpro.py velocidad clip.mp4 salida.mp4 --factor 0.5            # cámara lenta
python3 video-studio/herramientas/postpro.py fotograma clip.mp4 keyframe.png --ultimo              # encadenar tomas
python3 video-studio/herramientas/postpro.py color clip.mp4 salida.mp4 --estilo calido
python3 video-studio/herramientas/postpro.py subtitulos clip.mp4 subs.srt salida.mp4
python3 video-studio/herramientas/postpro.py unir toma_01.mp4 toma_02.mp4 -o salida.mp4 --transicion fundido --dur 0.4
python3 video-studio/herramientas/postpro.py mezclar video.mp4 salida.mp4 --voz voz.wav --musica musica.mp3 --efectos sfx.wav@2.5
python3 video-studio/herramientas/postpro.py normalizar video.mp4 salida.mp4
python3 video-studio/herramientas/postpro.py zoom imagen.png salida.mp4 --dur 4                    # zoom lento sobre una imagen
python3 video-studio/herramientas/postpro.py pausas crudo.mp4                                      # lista silencios del material grabado
python3 video-studio/herramientas/postpro.py quitar-pausas crudo.mp4 primer_corte.mp4              # primer corte sin pausas
python3 video-studio/herramientas/postpro.py destellos final.mp4                                   # máx. 3 destellos por segundo
```

`ensamblar.py` une los seleccionados de un proyecto con cortes directos; `postpro.py unir` permite fundidos.
Para retoques finos (curvas de color, máscaras, keyframes de texto animado) el dueño usa CapCut o DaVinci Resolve con
el plan de montaje que entrega el editor.
