// Entorno: patio de carga de una tienda de computadoras, de noche (short 5 de Tin & Tan, TIN-EN-S-005).
// Fuente: proyectos/2026-11-26_tin_y_tan_gta_6_on_pc/02_prompt/direccion.md, 3.1, 4.2 y 7. Hoja Noche (paleta B).
// Versión 0 (2026-11-27), para la animática: las piezas están en su sitio y a su tamaño; el detalle de dibujo y las
// versiones rotas con nombre propio se terminan antes del render.
// Carriles: C1 z = −1,0 (frente) · C2 z = −2,7 (pelea) · C3 z = −4,6 (fondo) · pared de fondo z = −6,5.
// Contrato: construir({THREE, escena, caja, C, lienzo}) → { cajones, pilar, piezas, MEDIDAS }.
export const FICHA = {
  id: 'patio_tienda_de_computadoras', temas: ['tecnología', 'hardware', 'compras'], creado: '2026-11-27',
  rompibles: ['pila (torre_de_pc_rota, torre_de_pc_caida)', 'cajas_der', 'monitores (monitor_roto)', 'farol (farol_torcido)', 'cajas_izq (cajas_carbonizadas)', 'persiana (persiana_abollada)'],
  no_se_toca: ['pestana', 'caja_registradora_rota', 'monitor de portada (se inclina, no se rompe)'],
};
export const MEDIDAS = { ancho: 9, fondo_z: -6.5, C1: -1.0, C2: -2.7, C3: -4.6, pila: [0, -3.6], grieta: [1.3, -4.6], cajas_der: [2.9, -4.6], monitores: [-2.6, -4.6], farol: [-3.5, -4.6], cajas_izq: [-4.0, -4.2], persiana: [2.35, -6.44], pestana: [-1.4, -6.44], caja_registradora_rota: [-4.1, -1.0], telescopio: [2.6, -0.7] };

export function construir({ THREE, escena, caja, C, lienzo }) {
  const tinta = C.linea, piezas = {}, M = MEDIDAS;
  const G = () => new THREE.Group();
  const en = (o, x, y, z) => { o.position.set(x, y, z); return o; };
  const liso = (w, h, color) => new THREE.Mesh(new THREE.PlaneGeometry(w, h), new THREE.MeshBasicMaterial({ color, side: THREE.DoubleSide }));
  const dibujo = (w, h, pw, ph, pinta) => { const cv = lienzo(pw, ph, pinta), tex = new THREE.CanvasTexture(cv); tex.colorSpace = THREE.SRGBColorSpace; const o = new THREE.Mesh(new THREE.PlaneGeometry(w, h), new THREE.MeshBasicMaterial({ map: tex, transparent: true, side: THREE.DoubleSide })); o.userData = { lienzo: cv, tex }; return o; };

  // pared de fondo del patio: muro bajo de bloque; por encima, cielo (el fondo de la hoja)
  const muro = en(liso(9.6, 4.4, C.bloque_lejos), 0, 2.2, M.fondo_z); escena.add(muro);
  escena.add(en(caja(9.6, 0.14, 0.1, tinta, 0), 0, 4.4, M.fondo_z + 0.04));
  escena.add(en(caja(9.6, 0.12, 0.08, tinta, 0), 0, 0.06, M.fondo_z + 0.05));

  // persiana metálica (golpe 5): lamas horizontales; la abolladura se dibuja en su lienzo
  const persiana = dibujo(4.3, 3.3, 860, 660, (g) => {
    g.fillStyle = C.bloque_cerca; g.fillRect(0, 0, 860, 660); g.strokeStyle = tinta; g.lineWidth = 8; g.strokeRect(4, 4, 852, 652);
    g.lineWidth = 3; for (let y = 44; y < 660; y += 44) { g.beginPath(); g.moveTo(8, y); g.lineTo(852, y); g.stroke(); }
  });
  en(persiana, M.persiana[0], 1.65, M.persiana[1]); escena.add(persiana);
  piezas.persiana = { malla: persiana, lienzo: persiana.userData.lienzo, tex: persiana.userData.tex, abollada: false };

  // pestaña de cartón con marcas de asterisco (P-001 / P-004): no se toca; la segunda marca la pone el guion
  const asterisco = (g, cx, cy, r) => { g.strokeStyle = C.linea; g.lineWidth = 9; g.lineCap = 'round'; for (let i = 0; i < 3; i++) { const a = i * Math.PI / 3 + 0.26; g.beginPath(); g.moveTo(cx - Math.cos(a) * r, cy - Math.sin(a) * r); g.lineTo(cx + Math.cos(a) * r, cy + Math.sin(a) * r); g.stroke(); } };
  const pestana = dibujo(1.25, 1.2, 250, 240, (g) => { g.fillStyle = C.utileria; g.fillRect(0, 0, 250, 240); g.strokeStyle = tinta; g.lineWidth = 8; g.strokeRect(4, 4, 242, 232); asterisco(g, 78, 120, 34); });
  en(pestana, M.pestana[0], 3.2, M.pestana[1]); escena.add(pestana);
  piezas.pestana = { malla: pestana, lienzo: pestana.userData.lienzo, tex: pestana.userData.tex, marca: (n = 2) => { const g = pestana.userData.lienzo.getContext('2d'); asterisco(g, 78 + 94 * (n - 1), 120, 34); pestana.userData.tex.needsUpdate = true; } };

  // pila de torres con el monitor apagado de la portada (golpe 1): tres torres acostadas y el monitor encima
  const pila = G(), torres = [];
  for (let i = 0; i < 3; i++) { const t = en(caja(1.05, 0.5, 0.62, C.bloque_cerca, 0.05), i === 1 ? 0.05 : 0, 0.25 + i * 0.5, 0); const boton = en(liso(0.1, 0.1, tinta), 0.36, 0, 0.32); t.add(boton); const ranura = en(liso(0.42, 0.05, tinta), -0.2, 0.08, 0.32); t.add(ranura); pila.add(t); torres.push(t); }
  const monitor = G(); monitor.add(en(caja(0.95, 0.62, 0.08, C.sombra, 0.06), 0, 0.5, 0)); monitor.add(en(caja(0.1, 0.2, 0.06, tinta, 0), 0, 0.1, 0)); monitor.add(en(caja(0.4, 0.05, 0.2, tinta, 0), 0, 0.02, 0));
  en(monitor, 0, 1.5, 0); pila.add(monitor);
  en(pila, M.pila[0], 0, M.pila[1]); escena.add(pila);
  piezas.pila = { grupo: pila, torres, monitor };

  // cajas de cartón de la derecha (golpe 2): se aplastan
  const pilaCajas = (x, z, lista) => { const g = G(), cajas = []; for (const [dx, y, dz, w, h, d] of lista) { const c = en(caja(w, h, d, C.utileria, 0.05), dx, y, dz); g.add(c); cajas.push(c); } en(g, x, 0, z); escena.add(g); return { grupo: g, cajas }; };
  piezas.cajas_der = pilaCajas(M.cajas_der[0], M.cajas_der[1], [[-0.4, 0.3, 0, 0.75, 0.6, 0.6], [0.4, 0.3, 0.05, 0.7, 0.6, 0.6], [0, 0.88, 0, 0.7, 0.55, 0.55], [0.85, 0.25, -0.5, 0.6, 0.5, 0.5], [-0.05, 1.38, 0.02, 0.5, 0.42, 0.45]]);
  // cajas al pie del farol (golpe 4): arden
  piezas.cajas_izq = pilaCajas(M.cajas_izq[0], M.cajas_izq[1], [[0, 0.28, 0, 0.7, 0.56, 0.6], [0.62, 0.24, 0.1, 0.55, 0.48, 0.5], [0.15, 0.78, 0, 0.5, 0.42, 0.45]]);

  // tres monitores sobre un palé (golpe 3): uno se rompe
  const pale = G(), monitores = []; pale.add(en(caja(2.0, 0.16, 0.9, C.utileria, 0.04), 0, 0.08, 0));
  for (let i = 0; i < 3; i++) { const mo = G(); mo.add(en(caja(0.56, 0.4, 0.07, C.sombra, 0.05), 0, 0.3, 0)); mo.add(en(caja(0.24, 0.06, 0.16, tinta, 0), 0, 0.03, 0)); en(mo, -0.66 + i * 0.66, 0.16, 0); pale.add(mo); monitores.push(mo); }
  en(pale, M.monitores[0], 0, M.monitores[1]); escena.add(pale);
  piezas.monitores = { grupo: pale, lista: monitores };

  // farol con poste, brazo, lámpara, caja de conexiones a 1,3 u y pozo de luz (óvalo 2D en el suelo, no luz real)
  const farol = G();
  farol.add(en(caja(0.14, 4.3, 0.14, tinta, 0), 0, 2.15, 0)); farol.add(en(caja(0.9, 0.1, 0.1, tinta, 0), 0.4, 4.25, 0));
  const lampara = G(); lampara.add(en(caja(0.5, 0.16, 0.3, tinta, 0), 0, 0, 0)); lampara.add(en(liso(0.4, 0.1, C.fuego_nucleo), 0, -0.1, 0.16)); en(lampara, 0.8, 4.12, 0); farol.add(lampara);
  farol.add(en(caja(0.3, 0.36, 0.2, C.bloque_cerca, 0.05), 0, 1.3, 0.14));
  en(farol, M.farol[0], 0, M.farol[1]); escena.add(farol);
  const pozo = dibujo(4.6, 2.6, 256, 144, (g) => { const gr = g.createRadialGradient(128, 72, 6, 128, 72, 124); gr.addColorStop(0, 'rgba(243,233,210,0.20)'); gr.addColorStop(0.7, 'rgba(243,233,210,0.08)'); gr.addColorStop(1, 'rgba(243,233,210,0)'); g.fillStyle = gr; g.fillRect(0, 0, 256, 144); });
  pozo.rotation.x = -Math.PI / 2; en(pozo, M.farol[0] + 1.6, 0.012, M.farol[1] + 1.4); escena.add(pozo);
  piezas.farol = { grupo: farol, lampara, pozo };

  // caja registradora rota (P-003, viene del short 4): quieta desde f0, extremo izquierdo del suelo
  const reg = G(); reg.add(en(caja(0.5, 0.3, 0.42, C.bloque_cerca, 0.05), 0, 0.15, 0)); const pant = en(caja(0.26, 0.16, 0.05, tinta, 0), 0.02, 0.34, -0.1); pant.rotation.z = 1.05; reg.add(pant); reg.add(en(caja(0.44, 0.06, 0.3, C.utileria, 0.03), 0, 0.05, 0.3));
  reg.rotation.y = 0.35; reg.scale.setScalar(0.62); en(reg, M.caja_registradora_rota[0], 0, M.caja_registradora_rota[1]); escena.add(reg);
  piezas.caja_registradora_rota = { grupo: reg };

  return { cajones: [], pilar: new THREE.Group(), piezas, MEDIDAS };
}
