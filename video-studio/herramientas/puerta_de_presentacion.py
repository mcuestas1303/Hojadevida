#!/usr/bin/env python3
"""Puerta de presentación: ninguna pieza terminada se le presenta al dueño sin la firma de los oficios.

Regla del dueño (2026-11-26): «La idea de definir un método es que no te lo saltes, que no vuelva a pasar».
El short 4 se le presentó sin que animación, fotografía, sonido, edición ni continuidad lo hubieran visto.

Uso:  python3 video-studio/herramientas/puerta_de_presentacion.py <carpeta del proyecto> <archivo de video o pieza>

Lee <proyecto>/07_revision/firmas.md, que lleva una fila por oficio:
| Oficio | Pieza (sha256, 12 primeros) | Veredicto | Informe | Fecha |
Pasa (código 0) solo si TODOS los oficios obligatorios tienen «APROBADO» sobre ESTA pieza (mismo sha256) y su
informe existe. Si no pasa, dice qué falta y de quién depende. Una pieza nueva (otro sha) necesita firmas nuevas.
"""
import hashlib, pathlib, re, sys

OFICIOS = ['animacion', 'fotografia', 'sonido', 'edicion', 'continuidad']   # infantil añade: pedagogia, psicologia


def main():
    if len(sys.argv) < 3:
        print(__doc__); return 2
    proyecto, pieza = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
    if not pieza.is_file():
        print(f'NO PASA: no existe la pieza {pieza}'); return 1
    sha = hashlib.sha256(pieza.read_bytes()).hexdigest()[:12]
    firmas = proyecto / '07_revision' / 'firmas.md'
    filas = {}
    if firmas.is_file():
        for l in firmas.read_text(encoding='utf-8').splitlines():
            c = [x.strip().strip('`') for x in l.strip().strip('|').split('|')]
            if len(c) >= 4 and c[0].lower() in OFICIOS:
                filas[c[0].lower()] = c
    faltan = []
    for o in OFICIOS:
        c = filas.get(o)
        if not c: faltan.append(f'{o}: sin fila en firmas.md'); continue
        if c[1] != sha: faltan.append(f'{o}: firmó otra pieza ({c[1]}), no esta ({sha})'); continue
        if not re.fullmatch(r'APROBADO', c[2]): faltan.append(f'{o}: veredicto «{c[2]}»'); continue
        if not (proyecto / '07_revision' / c[3]).is_file(): faltan.append(f'{o}: no existe el informe {c[3]}')
    print(f'Pieza: {pieza.name} · sha256 {sha}')
    if faltan:
        print('NO PASA: no se presenta al dueño. Falta:'); [print('  -', f) for f in faltan]; return 1
    print('PASA: los cinco oficios aprobaron esta pieza. Queda lo que solo puede hacer una persona (ver y oír).'); return 0


if __name__ == '__main__':
    sys.exit(main())
