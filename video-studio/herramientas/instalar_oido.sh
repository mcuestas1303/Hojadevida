#!/usr/bin/env bash
# Instala el «oído» del estudio (lo usa revisar_voz.py). Autorizado por el dueño el 2026-11-23.
# - sherpa-onnx (Apache-2.0): motor de reconocimiento de voz sin conexión.
# - Modelo Whisper small.en de OpenAI (MIT), convertido a ONNX por k2-fsa y publicado en sus «releases» de GitHub.
#   Pesa ≈ 1,3 GB y no se sube al repositorio: se descarga aquí, en herramientas/modelos_voz/.
set -euo pipefail
DESTINO="$(cd "$(dirname "$0")" && pwd)/modelos_voz"
pip install -q sherpa-onnx
if [ ! -f "$DESTINO/sherpa-onnx-whisper-small.en/small.en-tokens.txt" ]; then
  mkdir -p "$DESTINO"
  curl -sS -L -m 900 -o "$DESTINO/m.tar.bz2" \
    https://github.com/k2-fsa/sherpa-onnx/releases/download/asr-models/sherpa-onnx-whisper-small.en.tar.bz2
  tar xjf "$DESTINO/m.tar.bz2" -C "$DESTINO" && rm "$DESTINO/m.tar.bz2"
fi
echo "Oído listo: $DESTINO"
