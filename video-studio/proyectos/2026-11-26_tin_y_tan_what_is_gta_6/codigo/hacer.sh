#!/usr/bin/env bash
# Hace el short 4 entero, de la voz al video con sonido (0 créditos; ≈ 15 min). Uso: bash codigo/hacer.sh <carpeta de trabajo> [versión]
# La carpeta de trabajo va FUERA del repositorio (pesa ≈ 300 MB de fotogramas). La voz no se regenera: solo se recorta y se coloca.
set -euo pipefail
PROY="$(cd "$(dirname "$0")/.." && pwd)"; MOTOR="$PROY/../../motor_de_accion"; T="${1:?carpeta de trabajo}"; V="${2:-v5}"
python3 "$PROY/codigo/tiempos.py" > /dev/null                                   # voz real → fotogramas, subtítulos y tiempos del motor
[ -d "$MOTOR/sprites/c_alto_voltaje" ] || (cd "$MOTOR" && python3 personajes/exportar_sprites.py sprites)
(cd "$MOTOR" && node render.js "$T" 1000 c_alto_voltaje tienda_de_videojuegos 1 tin_en_s_004)     # mundo 3D y pelea: fotogramas, eventos y pistas
python3 "$PROY/codigo/control_encuadre.py" "$T" --md "$PROY/07_revision/control_encuadre_$V.md" > /dev/null || echo "AVISO: el control de encuadre NO PASA (ver 07_revision/control_encuadre_$V.md)"
python3 "$PROY/codigo/audio.py" "$T/eventos.json"                               # efectos, percusión y mezcla con la voz
python3 "$PROY/codigo/componer.py" "$T/fotogramas" --video                      # firma, datos, subtítulos → video sin sonido
ffmpeg -hide_banner -loglevel error -y -i "$PROY/06_final/tin_y_tan_short04_${V}_sin_audio.mp4" -i "$PROY/05_audio/mezcla_final.wav" \
  -c:v copy -c:a aac -b:a 192k -shortest -movflags +faststart "$PROY/06_final/tin_y_tan_short04_$V.mp4"
python3 "$PROY/codigo/hojas.py" "$PROY/06_final/fotogramas" f_ "$PROY/07_revision/hoja_$V" 7 270 > /dev/null
cp "$T/eventos.json" "$PROY/07_revision/eventos_y_medidas_del_motor_$V.json"
sha256sum "$PROY/06_final/tin_y_tan_short04_$V.mp4"
