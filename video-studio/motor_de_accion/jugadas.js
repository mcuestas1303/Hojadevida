// Banco de jugadas del motor de acción (2026-11-27). Sale de la pelea del short 4 (TIN-EN-S-004, versión 5, la que pasó
// la puerta de presentación): lo que allí se ajustó a mano queda aquí con nombre y con sus distancias.
// Regla del banco (metodo/registro_de_fallos.md, sección 4): una jugada solo entra cuando pasó la puerta en un video real.
// Lo que el banco NO resuelve: la cámara (el juez sigue siendo control_encuadre.py) y la variedad (cada pelea combina
// distinto y el banco crece con cada video).
//
// Uso en un guion:   import { banco } from '../jugadas.js';
//                    const B = banco(m, ['tin', 'tan', 'duda']);  const { G, pos, pose, trayecto, ataque, J } = B;
//                    J.golpeDeFrente({ pega: 'tin', recibe: 'duda', k: K1, desde: [1.73, -1], rival: [0.1, -1] });
//                    B.cerrar();   const avisos = B.comprobar([K1, K2]);
// Coordenadas: los puntos son [x, z] en el suelo (o [x, y, z] donde se dice). Los fotogramas, a 30 f/s.

// ------------------------------------------------------------ poses que el short 4 dejó probadas (antes vivían en su guion)
export const POSES = {
  gancho: { t: 20, aF: [122, 148], aB: [40, 120], lF: [30, 0], lB: [-36, -14], c: -14 },
  bloqueo: { t: -8, aF: [84, 120], aB: [44, 132], lF: [28, 4], lB: [-30, -10], c: 0, armaAng: 140 },
  dibuja: { t: 6, aF: [58, 112], aB: [84, 96], lF: [14, 4], lB: [-14, -4], c: 8, armaAng: 150 },
  guardiaBaja: { t: 10, aF: [30, 105], aB: [12, 95], lF: [28, 6], lB: [-26, -8], c: 0 },
  acecha: { t: 22, aF: [-30, -70], aB: [-50, -30], lF: [70, -40], lB: [-50, -100], c: 0 },
  cargaGancho: { t: -6, aF: [18, 62], aB: [50, 140], lF: [42, -30], lB: [-30, -62], c: -10 },
  pateado: { t: 16, aF: [70, 40], aB: [-50, -20], lF: [40, 30], lB: [-30, -40], c: 14 },
  senala: { t: 6, aF: [82, 96], aB: [-22, -8], lF: [10, 4], lB: [-10, -4], c: 6 },
  pregunta: { t: 0, aF: [58, 152], aB: [-10, -5], lF: [8, 4], lB: [-8, -4], c: -10 },
  invita: { t: 2, aF: [104, 168], aB: [-22, -8], lF: [10, 4], lB: [-10, -4], c: -4 },
  mazoArriba: { t: -10, aF: [158, 184], aB: [150, 172], lF: [22, 0], lB: [-30, -10], c: -8, armaAng: 196 },
  mazoAbajo: { t: 40, aF: [62, 72], aB: [52, 62], lF: [52, -10], lB: [-40, -52], c: 12, armaAng: 78 },
  miraEspada: { t: -4, aF: [84, 166], aB: [20, 60], lF: [14, 4], lB: [-14, -4], c: 22, armaAng: 178 },
  atrapa: { t: 0, aF: [96, 150], aB: [-12, -6], lF: [10, 4], lB: [-10, -4], c: -6 },
  punio: { t: 14, aF: [90, 90], aB: [-25, 80], lF: [44, 0], lB: [-44, -24], c: 2 },          // puño erguido: la cabeza de quien pega queda lejos del impacto
  esquiva: { t: -22, aF: [60, 140], aB: [30, 120], lF: [52, -18], lB: [-28, -82], c: -10 },
  susto: { t: -12, aF: [70, 150], aB: [40, 140], lF: [20, 4], lB: [-22, -6], c: -8 },
  sentado: { t: -36, aF: [-40, 20], aB: [-70, -20], lF: [82, 22], lB: [70, 10], c: 10 },
  explica: { t: 6, aF: [55, 150], aB: [70, 160], lF: [12, 4], lB: [-12, -4], c: -4, armaAng: 150 },
  golpeErguido: { t: 14, aF: [150, 150], aB: [-40, 20], lF: [40, 0], lB: [-40, -20], c: -2, armaAng: 84 },   // se rellena en banco() desde P.golpe (GrTin del short 4)
};

// Distancias medidas en el short 4, versión 5 (unidades del mundo). Son el contenido del banco: no se cambian a ojo.
export const MEDIDAS = {
  retroceso: 0.09,          // la anticipación echa el cuerpo hacia atrás
  contacto: 0.6,            // distancia entre quien pega y quien recibe en el fotograma K (puño)
  recupera: 1.1,            // distancia a la que queda quien pega 11 f después
  patada_minimo: 0.6,       // la carga del rival termina a esta distancia, o más, de quien patea
  gancho: 0.9,              // quien espera con el gancho, al punto donde cae el rival
  doble: [1.4, 1.5],        // cada uno de los dos que pegan, al rival que está en medio
  carril_libre: 1.1,        // el tercero, en z, respecto de la línea del golpe
  carrera_minima: 1.8, velocidad_minima: 4,     // una carrera recorre distancia de verdad (u y u/s)
  vivo: [14, 8],            // reposo vivo apagado desde K − 14 hasta K + 8
  cuerpos: 0.45,            // dos cuerpos en el suelo no se acercan más que esto (salvo en un contacto)
};

export function banco(m, ids = ['tin', 'tan', 'duda']) {
  const { P, clamp } = m, M = MEDIDAS;
  for (const [k, v] of Object.entries(POSES)) if (!P[k]) P[k] = v;
  if (P.golpe) P.golpeErguido = { ...P.golpe, t: 14, c: -2, armaAng: 84 };
  const lerp = (a, b, u) => a + (b - a) * u, entre = (f, a, b) => clamp((f - a) / (b - a));
  const A = (pose, ang) => ({ ...pose, armaAng: ang });          // la misma pose con el arma en otro ángulo
  const nueva = () => ({ pos: [], pose: [], mira: [], cara: [], escala: [], visible: [], modo: [[0, null]] });
  const G = {}; for (const id of ids) G[id] = nueva();
  const pos = (q, ...ks) => G[q].pos.push(...ks), pose = (q, ...ks) => G[q].pose.push(...ks);
  const corre = (q, f0, f1, modo = 'corre') => G[q].modo.push([f0, modo], [f1, null]);
  const carreras = [], contactos = [];                           // lo que después revisa comprobar()

  // ---------------------------------------------------------- gestos con su gramática de tiempo
  // trayecto: línea quebrada a velocidad pareja, con arranque y frenada de 3 f, una clave por fotograma; marca el modo de piernas
  const trayecto = (q, f0, f1, puntos, modo = 'corre') => {
    const largos = puntos.slice(1).map((b, i) => Math.hypot(b[0] - puntos[i][0], b[2] - puntos[i][2])), total = largos.reduce((a, b) => a + b, 0), n = f1 - f0, r = Math.min(3, n / 3) / n;
    const avance = u => { const v = 1 / (1 - r); return u < r ? v * u * u / (2 * r) : u > 1 - r ? 1 - v * (1 - u) * (1 - u) / (2 * r) : v * (u - r / 2); };
    for (let f = f0; f <= f1; f++) { let d = avance((f - f0) / n) * total, i = 0; while (i < largos.length - 1 && d > largos[i]) { d -= largos[i]; i++; } const u = largos[i] ? Math.min(1, d / largos[i]) : 0, a = puntos[i], b = puntos[i + 1]; G[q].pos.push([f, [lerp(a[0], b[0], u), 0, lerp(a[2], b[2], u)], 'lin']); }
    if (modo) corre(q, f0, f1, modo);
    carreras.push({ q, f0, f1, total, modo });
  };
  // ataque: anticipación K−13 a K−7, pausa quieta K−6 a K−1, contacto K (salto de pose), sostén y recuperación
  const ataque = (q, k, antes, carga, golpe, despues, sostiene = 5) => pose(q, [k - 13, antes], [k - 7, carga, 'out'], [k - 1, carga], [k, golpe, 'salto'], [k + sostiene, golpe], [k + sostiene + 6, despues]);

  // ---------------------------------------------------------- jugadas (escriben las claves de los dos)
  const v2 = p => [p[0], p.length > 2 ? p[2] : p[1]];            // admite [x, z] y [x, y, z]
  const hacia = (a, b) => { const dx = b[0] - a[0], dz = b[1] - a[1], d = Math.hypot(dx, dz) || 1; return [dx / d, dz / d]; };
  const a3 = (p, y = 0) => [p[0], y, p[1]];
  const J = {};

  // Golpe de frente (puño, empujón, patada frontal, estocada): quien pega retrocede, se queda quieto y salta al contacto.
  //   pega, recibe, k; desde = dónde espera quien pega; rival = dónde está quien recibe.
  //   poses = { antes, carga, golpe, despues } de quien pega; recibePose = pose del que recibe en K.
  //   Devuelve el punto del contacto y la dirección, para la estrella y para `despedido`.
  J.golpeDeFrente = ({ pega, recibe, k, desde, rival, poses = {}, recibePose = P.recibe, previa = null, contacto = M.contacto, recupera = M.recupera, sostiene = 5, retroceso = M.retroceso }) => {
    const a = v2(desde), r = v2(rival), d = hacia(a, r), en = dist => [r[0] - d[0] * dist, r[1] - d[1] * dist];
    pos(pega, [k - 13, a3(a)], [k - 7, a3([a[0] - d[0] * retroceso, a[1] - d[1] * retroceso]), 'out'], [k - 1, a3([a[0] - d[0] * retroceso, a[1] - d[1] * retroceso])], [k, a3(en(contacto)), 'salto'], [k + 11, a3(en(recupera))]);
    ataque(pega, k, poses.antes || P.guardia, poses.carga || P.carga, poses.golpe || P.punio, poses.despues || P.guardia, sostiene);
    pos(recibe, [k + 1, a3(r)]);
    if (previa) pose(recibe, [k - 1, previa]);
    pose(recibe, [k, recibePose, 'salto']);
    contactos.push({ k, pega, recibe, tipo: 'frente' });
    return { punto: [lerp(a[0], r[0], 0.75), lerp(a[1], r[1], 0.75)], dir: d, queda: en(recupera) };
  };

  // Patada por detrás: el rival carga, se pasa de largo y quien patea lo alcanza por la espalda. El rival recibe doblado
  // hacia delante (`pateado`) y se da la vuelta al salir. La carga del rival tiene que acabar a ≥ 0,6 u de quien patea.
  J.patadaPorDetras = ({ pega, recibe, k, desde, rival, avance = 0.55 }) => {
    const a = v2(desde), r = v2(rival), d = hacia(a, r);
    pos(pega, [k - 1, a3(a)], [k, a3([a[0] + d[0] * avance, a[1] + d[1] * avance]), 'salto'], [k + 11, a3([a[0] + d[0] * (avance - 0.15), a[1] + d[1] * (avance - 0.15)])]);
    ataque(pega, k, P.guardia, P.carga, P.patada, P.guardia);
    pos(recibe, [k + 1, a3(r)]);
    pose(recibe, [k - 1, P.guardia], [k, P.pateado, 'salto'], [k + 2, P.pateado]);
    contactos.push({ k, pega, recibe, tipo: 'detras', minimo: M.patada_minimo });
    return { dir: d };
  };

  // Gancho contra uno que baja de un mueble: quien pega espera erguido (`cargaGancho`) a 0,9 u; el rival baja con el brazo atrás.
  J.ganchoAlQueSalta = ({ pega, recibe, k, desde, cae, alto = 0.95, sostiene = 8 }) => {
    const a = v2(desde), c = v2(cae);
    pos(pega, [k - 7, a3(a), 'out'], [k - 1, a3(a)], [k, [a[0] + (c[0] - a[0]) * 0.27, 0.18, a[1]], 'salto'], [k + 6, a3([a[0] + (c[0] - a[0]) * 0.18, a[1]]), 'in']);
    ataque(pega, k, P.guardia, P.cargaGancho, P.gancho, P.guardia, sostiene);
    pos(recibe, [k - 1, [c[0], alto, c[1]], 'in'], [k + 1, [c[0], alto, c[1]]]);
    pose(recibe, [k - 11, P.acecha], [k - 7, P.recogido, 'out'], [k - 1, P.recogido], [k, P.recibe, 'salto'], [k + 4, P.vuela]);
    contactos.push({ k, pega, recibe, tipo: 'gancho', esperado: M.gancho });
  };

  // Golpe doble: el rival en medio; quien pega por el lado de la cámara lo hace erguido (su cabeza no tapa al rival).
  J.golpeDoble = ({ a, b, recibe, k, rival, lado = 1, deCamara = a, poses = {} }) => {
    const r = v2(rival), z = r[1];
    for (const [q, s, dist] of [[a, -lado, M.doble[1]], [b, lado, M.doble[0]]]) {
      const x0 = r[0] + s * (dist + 0.12), x1 = r[0] + s * dist;
      pos(q, [k - 7, a3([x0, z]), 'out'], [k - 1, a3([x0, z])], [k, a3([x1, z]), 'salto'], [k + 12, a3([r[0] + s * (dist + 0.08), z])]);
      ataque(q, k, poses.antes || P.guardia, poses.carga || P.carga, q === deCamara ? P.golpeErguido : (poses.golpe || P.golpe), poses.despues || P.guardia);
    }
    pos(recibe, [k + 1, a3(r)]);
    pose(recibe, [k - 1, P.guardia], [k, P.recogido, 'salto']);
    contactos.push({ k, pega: a, recibe, tipo: 'doble' }, { k, pega: b, recibe, tipo: 'doble' });
  };

  // Despedido: el rival sale del golpe por el aire. `via` son puntos [x, y, z]; el último es donde aterriza.
  //   Se da la vuelta al salir (mira) para caer con la cabeza hacia el lado libre.
  J.despedido = ({ q, k, via, aterriza, mira = null, caida = true }) => {
    const n = via.length, ult = via[n - 1];
    via.slice(0, -1).forEach((p, i) => pos(q, [Math.round(k + 2 + (aterriza - 7 - k - 2) * (i + 1) / (n - 1 || 1)), p, i ? 'out' : 'salto']));
    pos(q, [aterriza, [ult[0], 0, ult[2]], 'in']);
    pose(q, [k + 3, P.vuela], [aterriza - 7, P.vuela]);
    if (caida) pose(q, [aterriza, P.caido]);
    if (mira !== null) G[q].mira.push([k + 7, mira]);
    return aterriza;
  };

  // Caída y levantada: tendido → sentado → de pie → guardia. Sin `agachado`: mete la cabeza 0,6 u hacia delante (P4).
  J.levantada = ({ q, desde, hasta = P.guardia, tendido = 8 }) => pose(q, [desde, P.caido], [desde + tendido, P.caido], [desde + tendido + 8, P.sentado], [desde + tendido + 18, P.quieto], [desde + tendido + 26, hasta]);

  // Saltito de guardia: ajuste corto de posición (nunca «correr en el sitio»). De `a` a `b` en 6 f, con un bote bajo.
  J.saltito = ({ q, f, a, b, alto = 0.12 }) => { const A0 = v2(a), B0 = v2(b); pos(q, [f, a3(A0)], [f + 3, [lerp(A0[0], B0[0], 0.5), alto, lerp(A0[1], B0[1], 0.5)], 'out'], [f + 6, a3(B0), 'in']); pose(q, [f + 1, P.agachado, 'out'], [f + 4, P.guardia]); };

  // Bloqueo de arma: la estrella va en el punto medio entre las dos manos, 0,3 u por encima; las gotas salen hacia el rival.
  J.puntoDeBloqueo = (manoA, manoB) => [(manoA[0] + manoB[0]) / 2, (manoA[1] + manoB[1]) / 2 + 0.3, (manoA[2] + manoB[2]) / 2];

  // Reposo vivo: devuelve la función `vivo(id, f)` que pide escena.html; se apaga de K − 14 a K + 8 y en los tramos `quietos`.
  const reposoVivo = (ks, quietos = []) => (id, f) => {
    for (const k of ks) if (f >= k - M.vivo[0] && f <= k + M.vivo[1]) return { k: 0 };
    for (const [a, b] of quietos) if (f >= a && f <= b) return { k: 0 };
    return { k: 1 };
  };

  // ---------------------------------------------------------- cierre y comprobación sin render
  const cerrar = (escalaFija = []) => {
    for (const q of ids) for (const k of ['pos', 'pose', 'mira', 'cara', 'escala', 'visible', 'modo']) { G[q][k].sort((a, b) => a[0] - b[0]); if (!G[q][k].length) G[q][k].push([0, k === 'escala' ? 1 : k === 'visible' ? true : null]); }
    for (const q of escalaFija) G[q].escala = [[0, 1]];
    return G;
  };
  const posEn = (q, f) => { const ks = G[q].pos; if (!ks.length) return null; let i = 0; while (i < ks.length - 1 && ks[i + 1][0] <= f) i++; const a = ks[i], b = ks[i + 1]; if (!b || f <= a[0]) return a[1]; if (b[2] === 'salto') return a[1]; const u = (f - a[0]) / (b[0] - a[0]); return [lerp(a[1][0], b[1][0], u), lerp(a[1][1], b[1][1], u), lerp(a[1][2], b[1][2], u)]; };
  const visibleEn = (q, f) => { let v = true; for (const k of G[q].visible) if (k[0] <= f) v = k[1]; return v; };
  // comprobar: en milisegundos, antes de la pasada en seco. Interpola en línea recta (aproximado): lo que salga aquí es
  // aviso para mirar, no veredicto; el veredicto es control_encuadre.py sobre las pistas reales.
  const comprobar = (N) => {
    const av = [];
    for (const c of carreras) { const seg = (c.f1 - c.f0) / 30, v = c.total / seg; if (c.modo && c.modo.startsWith('corre') && (c.total < M.carrera_minima || v < M.velocidad_minima)) av.push(`carrera corta o lenta: ${c.q} f${c.f0}–f${c.f1}, ${c.total.toFixed(2)} u a ${v.toFixed(1)} u/s`); }
    for (const c of contactos) {
      const a = posEn(c.pega, c.k), r = posEn(c.recibe, c.k); if (!a || !r) continue;
      const d = Math.hypot(a[0] - r[0], a[2] - r[2]);
      if (d < 0.45 || d > 1.7) av.push(`contacto f${c.k} (${c.tipo}): ${c.pega} queda a ${d.toFixed(2)} u de ${c.recibe}`);
      for (const t of ids) if (t !== c.pega && t !== c.recibe && visibleEn(t, c.k)) { const p = posEn(t, c.k); if (p && Math.abs(p[2] - r[2]) < M.carril_libre && Math.abs(p[0] - r[0]) < 1.6 && Math.abs(p[0] - a[0]) < 1.6) av.push(`contacto f${c.k}: ${t} está en el carril del golpe (Δz ${Math.abs(p[2] - r[2]).toFixed(2)} u)`); }
    }
    const ks = contactos.map(c => c.k);
    for (let f = 0; f <= N; f += 2) for (let i = 0; i < ids.length; i++) for (let j = i + 1; j < ids.length; j++) {
      const a = ids[i], b = ids[j]; if (!visibleEn(a, f) || !visibleEn(b, f) || ks.some(k => Math.abs(f - k) <= 12)) continue;
      const p = posEn(a, f), q = posEn(b, f); if (!p || !q || p[1] > 0.3 || q[1] > 0.3) continue;
      if (Math.hypot(p[0] - q[0], p[2] - q[2]) < M.cuerpos) { av.push(`cuerpos encimados: ${a} y ${b} en f${f}`); f += 20; }
    }
    return av;
  };

  return { G, P, A, lerp, entre, nueva, pos, pose, corre, trayecto, ataque, J, reposoVivo, cerrar, comprobar, posEn, carreras, contactos, MEDIDAS: M };
}
