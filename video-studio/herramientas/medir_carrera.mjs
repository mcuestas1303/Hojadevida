// Control de carreras del motor de acción (gratis, sin renderizar). Equipo de producción, 2026-11-26.
// Origen: el dueño sobre TIN-EN-S-004 v2, «intentan correr y casi no se mueven».
// Evalúa un guion del motor con objetos vacíos, reproduce pista() de escena.html y proyecta con la cámara de cada plano
// (PerspectiveCamera 36°, 1080×1920). Para cada tramo con pose de carrera dice: pasos por segundo, zancada, cuánto
// avanza el cuerpo, si avanza hacia donde mira y cuánto se mueve en pantalla.
// Criterio de la v3 (director de animación): avance_vs_paso entre 0,8 y 1,2; corre_hacia = adelante; ≥ 0,6 cuerpos/s.
// Uso: node --no-warnings medir_carrera.mjs <carpeta motor_de_accion> [guion=tin_en_s_004]
//      node --no-warnings medir_carrera.mjs <motor> <guion> cabezas <salida.json> "45-70,195-300"   (cabezas previstas)
import fs from 'fs'; import path from 'path'; import { pathToFileURL } from 'url';
const MOTOR = process.argv[2], GUION = process.argv[3] || 'tin_en_s_004';
const T = JSON.parse(fs.readFileSync(path.join(MOTOR, `guiones/${GUION}.tiempos.json`)));
globalThis.fetch = async () => ({ json: async () => T });

// ---- copia literal de utilidades del motor (escena.html)
const clamp = (u, a = 0, b = 1) => Math.max(a, Math.min(b, u));
const EASE = { lin: u => u, in: u => u * u * u, out: u => 1 - Math.pow(1 - u, 3), io: u => u * u * (3 - 2 * u), salto: u => (u < 1 ? 0 : 1),
  back: u => { const c = 1.9; return 1 + (c + 1) * Math.pow(u - 1, 3) + c * Math.pow(u - 1, 2); } };
function mezcla(a, b, p) { if (typeof a === 'number') return a + (b - a) * p; if (Array.isArray(a)) return a.map((v, i) => mezcla(v, b[i], p));
  if (typeof a === 'object' && a) { const o = {}; for (const k in a) o[k] = mezcla(a[k], b[k] === undefined ? a[k] : b[k], p); return o; } return p < 0.5 ? a : b; }
function pista(c, S) { if (S <= c[0][0]) return c[0][1]; for (let i = 1; i < c.length; i++) if (S <= c[i][0]) { const [s0, v0] = c[i - 1], [s1, v1, e] = c[i]; return mezcla(v0, v1, EASE[e || 'io'](clamp((S - s0) / (s1 - s0)))); } return c[c.length - 1][1]; }
function escalon(c, S) { let v = c[0][1]; for (const k of c) if (S >= k[0]) v = k[1]; return v; }
const P = {
  quieto: { t: 0, aF: [10, 5], aB: [-10, -5], lF: [8, 4], lB: [-8, -4], c: 0 }, guardia: { t: 12, aF: [55, 150], aB: [25, 140], lF: [28, 6], lB: [-26, -8], c: 0 },
  carga: { t: -14, aF: [-55, 55], aB: [60, 150], lF: [18, 0], lB: [-34, -12], c: -6 }, golpe: { t: 30, aF: [90, 90], aB: [-25, 80], lF: [44, 0], lB: [-44, -24], c: 6 },
  embiste: { t: 42, aF: [-40, -80], aB: [-60, -100], lF: [62, -10], lB: [-55, -70], c: 10 }, patada: { t: -22, aF: [-60, -110], aB: [50, 140], lF: [95, 92], lB: [-25, -70], c: 0 },
  recogido: { t: 22, aF: [100, 150], aB: [-80, -120], lF: [72, -30], lB: [40, -60], c: 0 }, recibe: { t: -32, aF: [-100, -140], aB: [-60, -20], lF: [18, 40], lB: [-30, -8], c: -18 },
  vuela: { t: -72, aF: [-140, -160], aB: [-120, -150], lF: [60, 80], lB: [40, 70], c: -20 }, caido: { t: -88, aF: [-150, -175], aB: [-70, -95], lF: [80, 96], lB: [86, 62], c: 0 },
  agachado: { t: 30, aF: [40, 90], aB: [-20, 40], lF: [70, -40], lB: [-50, -100], c: 0 }, poder: { t: -8, aF: [150, 175], aB: [-150, -175], lF: [30, 4], lB: [-30, -4], c: -12 },
  pisoton: { t: 36, aF: [60, 30], aB: [-40, -10], lF: [50, -20], lB: [-45, -60], c: 12 }, festeja: { t: 0, aF: [140, 165], aB: [-140, -165], lF: [14, 4], lB: [-14, -4], c: -8 },
  corre1: { t: 30, aF: [70, 120], aB: [-60, -10], lF: [55, 10], lB: [-40, -95], c: 4 }, corre2: { t: 30, aF: [-60, -10], aB: [70, 120], lF: [-40, -95], lB: [55, 10], c: 4 },
  resbala: { t: -26, aF: [30, 100], aB: [60, 120], lF: [36, 10], lB: [-10, 10], c: -8 },
};
const MUNDO_R = 0.36, MUSLO = 0.85, PIERNA = 0.80;
const pie = (l) => { const s = d => Math.sin(d * Math.PI / 180), c = d => Math.cos(d * Math.PI / 180);
  return [MUSLO * s(l[0]) + PIERNA * s(l[1]), MUSLO * c(l[0]) + PIERNA * c(l[1])]; };   // x (+ = hacia donde mira), y (abajo)

// ---- stubs para evaluar el guion
const nada = new Proxy(function () {}, { get: (t, k) => k === Symbol.toPrimitive ? () => 0 : nada, apply: () => nada, construct: () => nada, set: () => true });
class V3 { constructor(x = 0, y = 0, z = 0) { this.x = x; this.y = y; this.z = z; } clone() { return new V3(this.x, this.y, this.z); } add() { return this; } }
const personajes = { tin: { tex: nada, malla: nada }, tan: { tex: nada, malla: nada }, duda: { tex: nada, malla: nada } };
const { guion } = await import(pathToFileURL(path.join(MOTOR, `guiones/${GUION}.js`)).href);
const GU = await guion({ THREE: nada, P, V: (x, y, z) => new V3(x, y, z), C: {}, EASE, clamp, ra: () => 0.5, pista, escalon, mezcla, marca: () => {}, grieta() {}, quemadura() {}, mancha() {},
  trazoSuelo() {}, garabatoResto() {}, onda() {}, soltar() {}, estrella() {}, focos: [], romperCajones() {}, empujarTrozos() {}, trozos: [], estado: {}, entorno: { piezas: nada },
  personajes, escena: nada, caja: () => nada, camara: nada, lienzo: () => nada, disco: () => nada, W: 1080, H: 1920, FPS: 30 });
const { G } = GU;

// ---- cámara de cada fotograma (copia de camaraDe) y proyección (PerspectiveCamera 36°, 1080×1920)
const W = 1080, H = 1920, FOV = 36, f_px = (H / 2) / Math.tan(FOV / 2 * Math.PI / 180);
function plano(f) { let p = T.planos[0]; for (const q of T.planos) if (f >= q.f0) p = q; return p; }
function proyecta(f, X) {
  const p = plano(f), D = p.D + (p.D1 - p.D) * clamp((f - p.f0) / (p.f1 - 1 - p.f0));
  const pos = [p.cx, p.h, p.z + D], mira = [p.cx, p.h + (p.sube || 0), p.z];
  let fw = [mira[0] - pos[0], mira[1] - pos[1], mira[2] - pos[2]]; const n = Math.hypot(...fw); fw = fw.map(v => v / n);
  let r = [fw[1] * 0 - fw[2] * 1, fw[2] * 0 - fw[0] * 0, fw[0] * 1 - fw[1] * 0]; const nr = Math.hypot(...r); r = r.map(v => v / nr); // fw × up
  const u = [r[1] * fw[2] - r[2] * fw[1], r[2] * fw[0] - r[0] * fw[2], r[0] * fw[1] - r[1] * fw[0]];
  const d = [X[0] - pos[0], X[1] - pos[1], X[2] - pos[2]], xc = d[0] * r[0] + d[1] * r[1] + d[2] * r[2], yc = d[0] * u[0] + d[1] * u[1] + d[2] * u[2], zc = d[0] * fw[0] + d[1] * fw[1] + d[2] * fw[2];
  return [W / 2 + f_px * xc / zc, H / 2 - f_px * yc / zc, zc, p.nombre];
}

// ---- tramos de carrera: fotogramas cuya pose es una mezcla de corre1/corre2
const esCarrera = pose => Math.abs(pose.t - 30) < 0.01 && Math.abs(pose.c - 4) < 0.01;
const salida = { fps: 30, fov: FOV, tramos: [] };
for (const q of ['tin', 'tan', 'duda']) {
  const g = G[q]; let tramo = null;
  for (let f = 0; f <= T.N; f++) {
    const pose = pista(g.pose, f), c = esCarrera(pose) && escalon(g.visible, f) !== false;
    if (c && !tramo) tramo = { q, f0: f, fs: [] };
    if (tramo && c) tramo.fs.push(f);
    if (tramo && (!c || f === T.N)) { salida.tramos.push(tramo); tramo = null; }
  }
}
const filas = [];
for (const tr of salida.tramos) {
  const { q, fs } = tr, g = G[q], f0 = fs[0], f1 = fs[fs.length - 1], n = fs.length;
  const esc = q === 'duda' ? null : 1;
  // pasos: cambios de corre1 ↔ corre2 (pose de pierna delantera)
  let pasos = 0, prev = null, span = 0;
  for (const f of fs) { const pose = pista(g.pose, f); const lado = pose.lF[0] > 0 ? 1 : -1; if (prev !== null && lado !== prev) pasos++; prev = lado;
    const a = pie(pose.lF), b = pie(pose.lB); span = Math.max(span, Math.abs(a[0] - b[0])); }
  // pasos por cruce: la pierna delantera pasa por la vertical cada 4 f → se cuentan los cambios de signo
  const escala = q === 'duda' ? pista(g.escala, f0) : 1;
  const zancadaU = span * MUNDO_R * escala;             // distancia entre pies en la pose extrema, en u del mundo
  const p0 = pista(g.pos, f0), p1 = pista(g.pos, f1 + 1);
  const dx = p1[0] - p0[0], dz = p1[2] - p0[2], dist = Math.hypot(dx, dz), dur = (f1 + 1 - f0) / 30;
  const cadencia = pasos / dur, necesario = cadencia * zancadaU;  // u/s que haría falta para que el pie no patine
  const mira = escalon(g.mira, f0), dirX = Math.sign(dx);
  // desplazamiento en pantalla de la cadera, fotograma a fotograma (sin cortes de plano dentro)
  let px = 0, quietos = 0, planos = new Set(), maxSalto = 0;
  for (let i = 1; i < fs.length; i++) {
    const a = proyecta(fs[i - 1], pista(g.pos, fs[i - 1])), b = proyecta(fs[i], pista(g.pos, fs[i]));
    planos.add(a[3]); planos.add(b[3]);
    if (a[3] !== b[3]) continue; const d = Math.hypot(b[0] - a[0], b[1] - a[1]); px += d; if (d < 2) quietos++; maxSalto = Math.max(maxSalto, d);
  }
  const s0 = proyecta(f0, p0), s1 = proyecta(f1, pista(g.pos, f1));
  // altura en pantalla del personaje (≈ 1,9 u para Tin y Tan) al inicio
  const alto = Math.abs(proyecta(f0, [p0[0], 1.9 * escala, p0[2]])[1] - proyecta(f0, [p0[0], 0, p0[2]])[1]);
  filas.push({ q, f0, f1, s: `${(f0 / 30).toFixed(2)}–${((f1 + 1) / 30).toFixed(2)}`, fotogramas: n, pasos, cadencia_pasos_s: +cadencia.toFixed(1),
    zancada_u: +zancadaU.toFixed(2), recorre_u: +dist.toFixed(2), lateral_u: +dx.toFixed(2), profundidad_u: +dz.toFixed(2), velocidad_u_s: +(dist / dur).toFixed(2),
    necesaria_u_s: +necesario.toFixed(2), avance_vs_paso: +(dist / dur / necesario).toFixed(2), mira, corre_hacia: dirX === 0 ? 'quieto' : (dirX === mira ? 'adelante' : 'de_espaldas'),
    px_pantalla_total: Math.round(px), px_por_s: Math.round(px / dur), fotogramas_casi_quietos: quietos, alto_px: Math.round(alto), cuerpos_por_s: +((px / dur) / alto).toFixed(2),
    planos: [...planos].join(' / ') });
}
salida.filas = filas;
console.log(JSON.stringify(salida.filas, null, 1));
if (process.argv[4] === 'cabezas') {
  const T2 = (process.argv[6] || '0-' + T.N).split(',').map(r => r.split('-').map(Number)), pred = [];
  for (const [a, b] of T2) for (let f = a; f <= b; f++) { const o = { f, plano: plano(f).nombre };
    for (const q of ['tin', 'tan']) { const p = pista(G[q].pos, f); const s = proyecta(f, [p[0], 1.75, p[2]]); o[q] = [Math.round(s[0]), Math.round(s[1])]; o[q + '_corre'] = esCarrera(pista(G[q].pose, f)); }
    pred.push(o); }
  fs.writeFileSync(process.argv[5], JSON.stringify(pred));
}
