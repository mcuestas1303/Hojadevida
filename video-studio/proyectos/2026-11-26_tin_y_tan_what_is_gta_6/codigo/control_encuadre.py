#!/usr/bin/env python3
"""Control automático de encuadre y de movimiento del short 4 (lo pidieron fotografía y animación al revisar la v2).

Lee lo que el motor escribe al grabar (`pistas.json`: dónde cae cada personaje en el cuadro y en el mundo, fotograma a
fotograma; `eventos.json`: medidas de cada contacto) y comprueba, sin mirar ninguna imagen:
  E1 nadie queda cortado por un borde (o está dentro, o está fuera del plano);
  E2 cabezas y pies dentro de la zona de acción (entre el dato y el subtítulo);
  E3 ninguna cabeza encima de otra;
  M1 cada carrera recorre distancia de verdad (u, u/s, px en pantalla, fotogramas por paso) y el pie de apoyo no resbala;
  M2 ningún salto de posición fuera de los contactos;
  M3 cada golpe cae sobre el rival, en su mismo carril, y la estrella no tapa la cara de quien pega;
  M4 nadie está idéntico más de 8 fotogramas; G1 ninguna clave cruzada en el guion.
Uso: python3 control_encuadre.py <carpeta de la grabación> [--md salida.md]      (código 1 si hay algún fallo)
"""
import json, math, sys
from pathlib import Path

W, H = 1080, 1920
ZONA = (705, 1376)            # y: debajo de la tarjeta del dato, encima del subtítulo
BORDE = 70                    # px: el centro de la cabeza no se acerca más que esto al borde si el personaje está en cuadro
DETALLE = ('P11', 'P12b', 'P4 ', 'P9 ', 'P13', 'P18')   # planos de detalle, de impacto (2 f) y héroe: el encuadre corta a propósito
QUIEN = {'tin': 'Tin', 'tan': 'Tan', 'duda': 'rival'}


def tramos(fs):
    out, a, b = [], None, None
    for f in fs:
        if a is None: a = b = f
        elif f == b + 1: b = f
        else: out.append((a, b)); a = b = f
    if a is not None: out.append((a, b))
    return ', '.join(f'f{a}' if a == b else f'f{a}–f{b}' for a, b in out)


def main():
    carpeta = Path(sys.argv[1])
    P = json.loads((carpeta / 'pistas.json').read_text())
    EV = json.loads((carpeta / 'eventos.json').read_text())
    M = EV['medidas']
    TL = json.loads((Path(__file__).resolve().parent.parent / '05_audio' / 'linea_de_tiempo.json').read_text(encoding='utf-8'))
    K = TL['K']
    planos = M['planos']
    def plano(f):
        n = 'firma'
        for p in planos:
            if f >= p['f0']: n = p['nombre']
        return 'firma' if (f < 30 or f >= K['cierre']) else n
    fallos, avisos, lineas = [], [], []
    def sec(t): lineas.append(''); lineas.append(f'## {t}'); lineas.append('')

    # G1
    sec('G1 · Claves del guion')
    cr = M.get('claves_cruzadas', [])
    lineas.append('Ninguna clave cruzada ni repetida.' if not cr else 'CRUZADAS: ' + '; '.join(cr))
    if cr: fallos.append(f'G1: {len(cr)} claves cruzadas')

    # E1, E2, E3
    cortado = {q: [] for q in QUIEN}; alto = {q: [] for q in QUIEN}; bajo = {q: [] for q in QUIEN}; encima = {}
    KS = [K[k] for k in ('K1', 'K2', 'K3', 'KB', 'K4', 'K5', 'KR', 'K6')]
    previa = None
    for fila in P:
        f = fila['f']; pl = plano(f)
        paneo = previa is not None and math.dist(previa['cam'][:3], fila['cam'][:3]) > 0.05; previa = fila      # la cámara acompaña: entrar o salir de cuadro no es quedar cortado
        if pl == 'firma': continue
        det = pl.startswith(DETALLE)
        vis = {}
        for q in QUIEN:
            d = fila[q]
            if not d['v']: continue
            x, y = d['c']; r = d['r']
            fuera = x < -r or x > W + r or y > H + r or y < -r
            if fuera: continue
            vis[q] = d
            if det: continue
            if (x < BORDE or x > W - BORDE) and not d['modo'] and d['rap'] < 3 and not paneo: cortado[q].append(f)      # entrar o salir corriendo no es quedar cortado
            if y - r < ZONA[0] - (140 if q == 'duda' else 0) - (130 if d['y'] > 0.25 else 0): alto[q].append(f)      # en un salto la cabeza puede subir a la franja libre bajo el dato
            if d['s'][1] > ZONA[1] and d['y'] < 0.05: bajo[q].append(f)
        qs = list(vis)
        for i in range(len(qs)):
            for j in range(i + 1, len(qs)):
                a, b = vis[qs[i]], vis[qs[j]]
                dist = math.hypot(a['c'][0] - b['c'][0], a['c'][1] - b['c'][1])
                if dist < 0.8 * (a['r'] + b['r']) and not a['modo'] and not b['modo'] and not any(k <= f <= k + 2 for k in KS):
                    encima.setdefault(f'{QUIEN[qs[i]]} y {QUIEN[qs[j]]}', []).append(f)
    sec('E1 · Personajes cortados por un borde lateral (centro de la cabeza a menos de %d px)' % BORDE)
    for q in QUIEN:
        if cortado[q]:
            lineas.append(f'- {QUIEN[q]}: {tramos(cortado[q])}'); (fallos if q != 'duda' else avisos).append(f'E1: {QUIEN[q]} cortado en {tramos(cortado[q])}')
    if not any(cortado.values()): lineas.append('Ninguno.')
    sec('E2 · Fuera de la zona de acción (y %d–%d)' % ZONA)
    for q in QUIEN:
        if alto[q]:
            lineas.append(f'- {QUIEN[q]}, cabeza por encima de la zona: {tramos(alto[q])}'); (fallos if q != 'duda' else avisos).append(f'E2: {QUIEN[q]} alto en {tramos(alto[q])}')
        if bajo[q]:
            lineas.append(f'- {QUIEN[q]}, pies por debajo de la zona: {tramos(bajo[q])}'); fallos.append(f'E2: {QUIEN[q]} bajo en {tramos(bajo[q])}')
    if not any(alto.values()) and not any(bajo.values()): lineas.append('Nadie.')
    sec('E3 · Cabezas encimadas')
    for k, fs in encima.items():
        lineas.append(f'- {k}: {tramos(fs)}')
        (fallos if len(fs) > 3 else avisos).append(f'E3: {k} encimadas en {tramos(fs)}')
    if not encima: lineas.append('Ninguna.')

    # M1 carreras
    sec('M1 · Carreras y caminatas')
    lineas.append('| Quién | Fotogramas | Modo | Recorre (u) | u/s | En pantalla (px) | f por paso | Pie de apoyo resbala (u, máx.) | |')
    lineas.append('|---|---|---|---|---|---|---|---|---|')
    for q in QUIEN:
        i = 0
        while i < len(P):
            if P[i][q]['modo']:
                j = i
                while j + 1 < len(P) and P[j + 1][q]['modo']: j += 1
                b = P[j][q]
                rec = sum(math.hypot(P[k][q]['pos'][0] - P[k - 1][q]['pos'][0], P[k][q]['pos'][2] - P[k - 1][q]['pos'][2]) for k in range(i, j + 1))
                lateral = abs(sum(P[k][q]['vlat'] for k in range(i, j + 1)))
                n = j - i + 1; vel = rec / n * 30
                px = sum(P[k][q]['dpx'] for k in range(i, j + 1))          # camino sobre el suelo, en px de pantalla (no cuenta el movimiento de cámara)
                modo = P[i][q]['modo'].split('_')[0]
                largo = {'corre': 1.9, 'camina': 0.9}[modo] * b['esc'] * ({'duda': 2.05}.get(q, 1.65) / 1.65)
                vueltas = sum((P[k][q]['fase'] - P[k - 1][q]['fase']) % 1 for k in range(i + 1, j + 1) if P[k][q]['fase'] is not None and P[k - 1][q]['fase'] is not None)
                pasos = vueltas * 2; fpp = n / pasos if pasos else 0      # dos pasos por vuelta del ciclo
                # pie de apoyo: mientras un pie está en el suelo, cuánto se corre a lo ancho del cuadro (en u del mundo, sobre el
                # eje lateral de la cámara). Solo tiene sentido si la carrera es lateral; en diagonal el dibujo de perfil no puede
                # plantar el pie y se anota como diagonal.
                res = 0.0
                for pie, eje in (('pf', 'lat'), ('pb', 'latB')):
                    ini = None
                    for k in range(i + 3, j - 1):
                        y = P[k][q][pie][1]; v = P[k][q][eje]
                        suelo = y < 0.06 * b['esc'] + 0.045
                        if suelo and ini is None: ini = v
                        if suelo and ini is not None: res = max(res, abs(v - ini))
                        if not suelo: ini = None
                diagonal = lateral < 0.8 * rec
                mal = []
                if modo == 'corre':
                    if rec < 1.6: mal.append('recorre poco')
                    if vel < 3.0: mal.append('lenta')
                    if not 3.5 <= fpp <= 8.5: mal.append('cadencia')
                    crece = max(P[j][q]['r'], 1) / max(P[i][q]['r'], 1)
                    if px < 300 and not (diagonal and (crece > 1.25 or crece < 0.8)): mal.append('poco en pantalla')      # hacia la cámara o alejándose: lo que cambia es el tamaño
                if res > 0.12 and not diagonal: mal.append('resbala')
                lineas.append(f"| {QUIEN[q]} | f{P[i]['f']}–f{P[j]['f']} | {P[i][q]['modo']}{' (diagonal)' if diagonal else ''} | {rec:.2f} | {vel:.1f} | {px:.0f} | {fpp:.1f} | {res:.2f}{' (no aplica)' if diagonal else ''} | {'; '.join(mal) or 'bien'} |")
                if mal: fallos.append(f"M1: {QUIEN[q]} f{P[i]['f']}–f{P[j]['f']}: {', '.join(mal)}")
                i = j + 1
            else: i += 1

    # M2 saltos
    sec('M2 · Saltos de posición de Tin y de Tan (> 0,36 u en un fotograma, fuera del contacto)')
    sal = {}
    for i in range(1, len(P)):
        f = P[i]['f']
        if plano(f) == 'firma' or plano(f - 1) == 'firma': continue
        for q in ('tin', 'tan'):
            a, b = P[i - 1][q], P[i][q]
            d = math.hypot(a['pos'][0] - b['pos'][0], a['pos'][2] - b['pos'][2])
            if d > 0.36 and not any(f in (k, k + 1) for k in KS):
                x, r = b['c'][0], b['r']
                oculto = x < -r or x > W + r
                (avisos if oculto else fallos).append(f'M2: {QUIEN[q]} salta {d:.2f} u en f{f}' + (' (fuera de cuadro)' if oculto else ''))
                sal.setdefault(q, []).append(f'f{f} ({d:.2f} u' + (', fuera de cuadro' if oculto else '') + ')')
    for q, v in sal.items(): lineas.append(f'- {QUIEN[q]}: ' + ', '.join(v))
    if not sal: lineas.append('Ninguno.')

    # M3 contactos
    sec('M3 · Contactos')
    lineas.append('| Golpe | Con qué | Del punto de golpe al rival (u) | Diferencia de carril (u) | Estrella a la cabeza de quien pega (u) | |')
    lineas.append('|---|---|---|---|---|---|')
    for c in M.get('contactos', []):
        if 'golpe_a_rival_u' not in c:
            ok = c['espada_a_cabeza_de_tin_u'] >= 0.45
            lineas.append(f"| {c['nombre']} | {c['parte']} | — | — | {c['espada_a_cabeza_de_tin_u']:.2f} (a la cabeza de Tin) | {'bien' if ok else 'cerca de la cara de Tin'} |")
            if not ok: fallos.append('M3: el bloqueo cae sobre la cara de Tin')
            continue
        mal = []
        if c['golpe_a_rival_u'] > 0.45: mal.append('no llega al rival')
        if c['dz_u'] > 0.15: mal.append('otro carril')
        if c['estrella_a_cabeza_de_quien_pega_u'] < 0.45: mal.append('estrella sobre quien pega')
        if '--ajuste' in sys.argv: print('   ajuste', c['nombre'], c.get('vector'))
        lineas.append(f"| {c['nombre']} | {c['parte']} | {c['golpe_a_rival_u']:.2f} | {c['dz_u']:.2f} | {c['estrella_a_cabeza_de_quien_pega_u']:.2f} | {'; '.join(mal) or 'bien'} |")
        if mal: fallos.append(f"M3: {c['nombre']}: {', '.join(mal)}")
    if len(M.get('contactos', [])) < 9: fallos.append('M3: faltan contactos medidos')

    # M4 quietud
    sec('M4 · Quietud (mano de Tin o de Tan sin moverse más de 8 f estando en cuadro)')
    q8 = []
    for q in ('tin', 'tan'):
        n = 0
        for i in range(1, len(P)):
            a, b = P[i - 1][q], P[i][q]
            if plano(P[i]['f']) == 'firma' or not b['v']: n = 0; continue
            mov = math.hypot(a['m'][0] - b['m'][0], a['m'][1] - b['m'][1]) + math.hypot(a['c'][0] - b['c'][0], a['c'][1] - b['c'][1])
            n = n + 1 if mov < 1 else 0
            if n == 9: q8.append(f"{QUIEN[q]} desde f{P[i]['f'] - 8}")
    lineas.append('Nadie.' if not q8 else '; '.join(q8))
    if q8: fallos.append('M4: ' + '; '.join(q8))

    sec('Encuadre por plano (px): dónde quedan las cabezas y los pies')
    lineas.append('| Plano | Fotogramas | Tin: x de la cabeza | Tan: x de la cabeza | Rival: x de la cabeza | Cabeza más alta (y) | Pies más bajos (y) | Alto de Tin o Tan (px) |')
    lineas.append('|---|---|---|---|---|---|---|---|')
    grupos = {}
    for fila in P:
        pl = plano(fila['f'])
        if pl != 'firma': grupos.setdefault(pl, []).append(fila)
    for pl, filas in grupos.items():
        col = []
        ymin, ymax, altos = 9999, 0, []
        for q in QUIEN:
            xs = [f[q]['c'][0] for f in filas if f[q]['v'] and -60 < f[q]['c'][0] < W + 60]
            col.append(f'{min(xs)}–{max(xs)}' if xs else 'fuera')
            for f in filas:
                d = f[q]
                if d['v'] and 0 < d['c'][0] < W:
                    ymin = min(ymin, d['c'][1] - d['r']); ymax = max(ymax, d['s'][1])
                    if q != 'duda' and d['y'] < 0.05: altos.append(d['s'][1] - (d['c'][1] - d['r']))
        lineas.append(f"| {pl} | f{filas[0]['f']}–f{filas[-1]['f']} | {col[0]} | {col[1]} | {col[2]} | {ymin} | {ymax} | {int(sorted(altos)[len(altos)//2]) if altos else '—'} |")

    cab = ['# Control automático de encuadre y movimiento — short 4, versión 3', '',
           f'Grabación: `{carpeta.name}` · {len(P)} fotogramas · hecho por `codigo/control_encuadre.py`.', '',
           f"**Resultado: {'PASA' if not fallos else 'NO PASA'}** · {len(fallos)} fallos, {len(avisos)} avisos.", '']
    if fallos: cab += ['Fallos:'] + [f'- {x}' for x in fallos] + ['']
    if avisos: cab += ['Avisos (no bloquean; se miran en las hojas):'] + [f'- {x}' for x in avisos] + ['']
    txt = '\n'.join(cab + lineas) + '\n'
    if '--md' in sys.argv: Path(sys.argv[sys.argv.index('--md') + 1]).write_text(txt, encoding='utf-8')
    print(txt)
    return 1 if fallos else 0


if __name__ == '__main__':
    sys.exit(main())
