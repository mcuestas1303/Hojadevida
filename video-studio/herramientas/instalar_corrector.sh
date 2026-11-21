#!/usr/bin/env bash
# Instala el corrector ortográfico del estudio (lo usa revisar_texto.py). Autorizado por el dueño el 2026-11-21.
# - spylls 0.1.7: motor Hunspell en Python puro (MPL-2.0).
# - Diccionarios de LibreOffice publicados por wooorm/dictionaries en npm (versión 4.0.0):
#     en: inglés de EE. UU. (MIT AND BSD) · es: español (GPL-3.0 OR LGPL-3.0 OR MPL-1.1) · pt: portugués de Brasil
#     (LGPL-3.0 OR MPL-2.0). No se suben al repositorio: se descargan aquí, en herramientas/diccionarios/.
set -euo pipefail
DESTINO="$(cd "$(dirname "$0")" && pwd)/diccionarios"
pip install -q spylls==0.1.7
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
for idioma in en es pt; do
  if [ -f "$DESTINO/$idioma/index.dic" ]; then continue; fi
  (cd "$TMP" && npm pack -q "dictionary-$idioma@4.0.0" >/dev/null)
  mkdir -p "$DESTINO/$idioma"
  tar xzf "$TMP/dictionary-$idioma-4.0.0.tgz" -C "$DESTINO/$idioma" --strip-components=1 \
    package/index.aff package/index.dic package/license
done
echo "Corrector listo: $DESTINO (en, es, pt)"
