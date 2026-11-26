// Entorno «tienda de videojuegos» (noche de lanzamiento). Hecho para el short 4 de Tin & Tan (TIN-EN-S-004).
// Temas: juegos, compras, estrenos. Sin logotipos, sin texto, sin arte en las cajas, sin figuras humanas.
// Especificación: proyectos/2026-11-26_tin_y_tan_what_is_gta_6/02_prompt/direccion.md, sección 7.1.
// Ajuste de producción (2026-11-26): el cuadro vertical solo ve ≈ 5 u de ancho a la altura de los personajes y ≈ 8 u al
// fondo, así que la tienda mide 9 u de ancho (no 14) y los estantes van en x = ±2,8 para que se vean fugar hacia el televisor.
// Contrato: construir({THREE, escena, caja, C, lienzo}) → { cajones, pilar, piezas }. «piezas» son las que el guion mueve o rompe.
export const FICHA = {
  id: 'tienda_de_videojuegos', temas: ['juegos', 'compras', 'estrenos'], creado: '2026-11-26',
  rompibles: ['estante_izquierdo', 'estante_derecho', 'caja_de_juego', 'pila_de_cajas', 'cartel_de_pie', 'postes_de_fila', 'mostrador', 'caja_registradora', 'televisor_de_exhibicion', 'banderines'],
  no_se_toca: ['escaparate', 'mando_mostaza', 'pared_fondo (se quema, no se agujerea)'],
};
export const MEDIDAS = { ancho: 9, fondo_z: -10, pared_x: 4.5, alto: 7 };

export function construir({ THREE, escena, caja, C, lienzo }) {
  const tinta = C.linea, blanco = C.bloque_cerca, lejos = C.bloque_lejos, gris = C.utileria;
  const piezas = {};
  const G = () => new THREE.Group();
  const en = (o, x, y, z) => { o.position.set(x, y, z); return o; };
  const plano = (w, h, color, lados = THREE.FrontSide) => { const m = new THREE.Mesh(new THREE.PlaneGeometry(w, h), new THREE.MeshBasicMaterial({ color, side: lados })); return m; };   // pared lisa: color exacto de la paleta, sin sombreado
  const liso = (w, h, color) => new THREE.Mesh(new THREE.PlaneGeometry(w, h), new THREE.MeshBasicMaterial({ color, side: THREE.DoubleSide }));

  // paredes: una sola cara, mirando hacia adentro (la cámara lateral, que queda fuera, ve a través de la suya)
  const fondo = en(plano(9, 7, C.fondo), 0, 3.5, -10); escena.add(fondo);
  const zocalo = en(caja(9, 0.16, 0.06, tinta, 0), 0, 0.08, -9.96); escena.add(zocalo);
  const pIzq = en(plano(22, 7, C.fondo), -4.5, 3.5, 1); pIzq.rotation.y = Math.PI / 2; escena.add(pIzq);
  const pDer = en(plano(22, 7, C.fondo), 4.5, 3.5, 1); pDer.rotation.y = -Math.PI / 2; escena.add(pDer);
  // quemadura de la pared del fondo: capa que el guion pinta (no se agujerea)
  const cvPared = lienzo(1024, 800, () => {}), texPared = new THREE.CanvasTexture(cvPared); texPared.colorSpace = THREE.SRGBColorSpace;
  const hollin = new THREE.Mesh(new THREE.PlaneGeometry(9, 7), new THREE.MeshBasicMaterial({ map: texPared, transparent: true, depthWrite: false }));
  en(hollin, 0, 3.5, -9.98); escena.add(hollin);
  piezas.pared_fondo = { malla: fondo, lienzo: cvPared, tex: texPared };

  // escaparate: vidrio en tinta con 5 puntos claros (dice «es de noche»)
  const texVidrio = new THREE.CanvasTexture(lienzo(600, 440, (g, w, h) => {
    g.fillStyle = tinta; g.fillRect(0, 0, w, h); g.fillStyle = C.fondo;
    for (const [x, y, r] of [[90, 120, 9], [210, 300, 7], [330, 90, 10], [450, 250, 8], [540, 140, 6]]) { g.beginPath(); g.arc(x, y, r, 0, 7); g.fill(); }
    g.strokeStyle = blanco; g.lineWidth = 16; g.strokeRect(8, 8, w - 16, h - 16); g.beginPath(); g.moveTo(w / 2, 0); g.lineTo(w / 2, h); g.stroke();
  })); texVidrio.colorSpace = THREE.SRGBColorSpace;
  const escaparate = new THREE.Mesh(new THREE.PlaneGeometry(3, 2.2), new THREE.MeshBasicMaterial({ map: texVidrio }));
  en(escaparate, -4.47, 2.3, 1.5); escaparate.rotation.y = Math.PI / 2; escena.add(escaparate); piezas.escaparate = escaparate;

  // caja de juego: blanca, con una banda de tinta, lisa
  function cajaDeJuego(w = 0.32, h = 0.42, d = 0.06) {
    const g = G(); g.add(caja(w, h, d, blanco, 0.03));
    const banda = new THREE.Mesh(new THREE.BoxGeometry(w * 1.02, h * 0.16, d * 1.06), new THREE.MeshBasicMaterial({ color: tinta })); banda.position.y = h * 0.22; g.add(banda);
    g.userData = { v: new THREE.Vector3(), w: new THREE.Vector3(), quieto: true, piso: Math.max(d, 0.06) / 2 + 0.01 };
    return g;
  }
  // estante: 4,5 de largo (en z) × 3,2 de alto × 0,6 de fondo; 4 baldas; 24 cajas mirando al pasillo
  function estante(lado) {                       // lado = -1 izquierda, +1 derecha
    const g = G(), baldas = [], cajas = [];
    g.add(en(caja(0.08, 3.2, 4.5, lejos, 0.04), lado * 0.26, 1.6, 0));
    for (const z of [-2.21, 2.21]) g.add(en(caja(0.6, 3.2, 0.08, blanco, 0.04), 0, 1.6, z));
    for (let i = 0; i < 4; i++) {
      const y = 0.25 + i * 0.78, b = en(caja(0.56, 0.07, 4.34, blanco, 0.03), 0, y, 0); g.add(b); baldas.push(b);
      for (let k = 0; k < 6; k++) { const c = cajaDeJuego(); c.rotation.y = Math.PI / 2; en(c, -lado * 0.12, y + 0.26, -1.8 + k * 0.72); g.add(c); cajas.push(c); }
    }
    en(g, lado * 2.8, 0, -6.25); escena.add(g);
    return { grupo: g, baldas, cajas, lado };
  }
  piezas.estante_izquierdo = estante(-1); piezas.estante_derecho = estante(1);

  // pila de cajas: pirámide de 10 (4, 3, 2, 1)
  const pila = [];
  for (let fila = 0; fila < 4; fila++) for (let k = 0; k < 4 - fila; k++) {
    const c = cajaDeJuego(0.42, 0.32, 0.3); en(c, 1.25 + (k - (3 - fila) / 2) * 0.45, 0.17 + fila * 0.33, -7.0); escena.add(c); pila.push(c);
  }
  piezas.pila_de_cajas = pila;

  // cartel de pie, en blanco, en dos mitades (el rival lo parte en zigzag)
  const cartel = G(); const cAbajo = en(caja(0.7, 0.85, 0.06, blanco, 0.05), 0, 0.425, 0), cArriba = G(); cArriba.add(en(caja(0.7, 0.85, 0.06, blanco, 0.05), 0, 0.425, 0)); en(cArriba, 0, 0.85, 0);
  cartel.add(cAbajo, cArriba); en(cartel, 3.0, 0, -0.5); cartel.rotation.y = -0.2; escena.add(cartel);
  piezas.cartel_de_pie = { grupo: cartel, abajo: cAbajo, arriba: cArriba };

  // postes de fila (4, con cinta), a la derecha y delante
  const postes = [], cintas = [];
  const px = [[1.9, 0.5], [2.6, 0.5], [3.3, 0.5], [3.3, -0.5]];
  for (const [x, z] of px) {
    const p = G(); const palo = new THREE.Mesh(new THREE.CylinderGeometry(0.05, 0.05, 1.0, 10), new THREE.MeshLambertMaterial({ color: gris })); palo.position.y = 0.5; palo.castShadow = true;
    const base = new THREE.Mesh(new THREE.CylinderGeometry(0.2, 0.22, 0.06, 16), new THREE.MeshLambertMaterial({ color: gris })); base.position.y = 0.03;
    const bola = new THREE.Mesh(new THREE.SphereGeometry(0.08, 10, 8), new THREE.MeshBasicMaterial({ color: tinta })); bola.position.y = 1.02;
    p.add(palo, base, bola); en(p, x, 0, z); escena.add(p); postes.push(p);
  }
  for (let i = 0; i < 3; i++) {
    const [a, b] = [px[i], px[i + 1]], l = Math.hypot(b[0] - a[0], b[1] - a[1]);
    const c = new THREE.Mesh(new THREE.BoxGeometry(l, 0.07, 0.015), new THREE.MeshBasicMaterial({ color: tinta })); en(c, (a[0] + b[0]) / 2, 0.92, (a[1] + b[1]) / 2); c.rotation.y = -Math.atan2(b[1] - a[1], b[0] - a[0]); escena.add(c); cintas.push(c);
  }
  piezas.postes_de_fila = { postes, cintas };

  // mostrador en dos mitades (se agrieta y luego se parte), con tapa blanca, y la caja registradora encima
  const mostrador = G(), mitades = [];
  for (const s of [-1, 1]) { const m = G(); m.add(en(caja(1.2, 0.94, 0.8, lejos, 0.05), 0, 0.47, 0)); m.add(en(caja(1.26, 0.07, 0.86, blanco, 0.04), 0, 0.975, 0)); en(m, s * 0.6, 0, 0); mostrador.add(m); mitades.push(m); }
  en(mostrador, 3.0, 0, -3.4); escena.add(mostrador);
  const reg = G();
  reg.add(en(caja(0.6, 0.26, 0.45, gris, 0.04), 0, 0.13, 0));
  const gaveta = en(caja(0.5, 0.1, 0.4, blanco, 0.03), 0, 0.07, 0.03); reg.add(gaveta);
  const teclado = en(caja(0.5, 0.06, 0.24, blanco, 0.03), 0, 0.29, 0.08); teclado.rotation.x = 0.35; reg.add(teclado);
  const pantalla = G(); pantalla.add(en(caja(0.3, 0.2, 0.05, tinta, 0), 0, 0.16, 0)); pantalla.add(en(caja(0.05, 0.12, 0.05, gris, 0.02), 0, 0.03, 0)); en(pantalla, 0.1, 0.26, -0.14); reg.add(pantalla);
  const cinta = new THREE.Mesh(new THREE.BoxGeometry(0.1, 0.012, 0.5), new THREE.MeshBasicMaterial({ color: blanco })); en(cinta, -0.2, 0.3, 0.1); cinta.visible = false; reg.add(cinta);
  en(reg, 2.55, 1.01, -3.4); escena.add(reg);
  piezas.mostrador = { grupo: mostrador, mitades };
  piezas.caja_registradora = { grupo: reg, gaveta, pantalla, cinta, rota: false };   // al romperse pasa a llamarse caja_registradora_rota

  // isla del televisor: columna de 1,6 y pantalla en blanco de 2,4 × 1,4
  const isla = G();
  isla.add(en(caja(0.9, 1.6, 0.6, blanco, 0.05), 0, 0.8, 0));
  const tele = G(); tele.add(caja(2.4, 1.4, 0.12, tinta, 0));
  const pant = new THREE.Mesh(new THREE.PlaneGeometry(2.2, 1.2), new THREE.MeshBasicMaterial({ color: C.fondo })); pant.position.z = 0.065; tele.add(pant);
  const cvTele = lienzo(880, 480, () => {}), texTele = new THREE.CanvasTexture(cvTele); texTele.colorSpace = THREE.SRGBColorSpace;
  const grietas = new THREE.Mesh(new THREE.PlaneGeometry(2.2, 1.2), new THREE.MeshBasicMaterial({ map: texTele, transparent: true, depthWrite: false })); grietas.position.z = 0.07; tele.add(grietas);
  en(tele, 0, 2.3, 0); isla.add(tele); en(isla, 0, 0, -7.5); escena.add(isla);
  piezas.isla_televisor = { grupo: isla, tele, pantalla: pant, lienzo: cvTele, tex: texTele };

  // banderines: 12 triángulos en una cuerda corta, justo por encima del televisor y detrás de él. Con el origen en el
  // extremo izquierdo, para que tras la explosión cuelguen de ese lado. A esta altura no entran nunca en la zona de datos.
  const banderines = G(), tri = new THREE.Shape(); tri.moveTo(-0.13, 0); tri.lineTo(0.13, 0); tri.lineTo(0, -0.34); tri.closePath();
  const geoTri = new THREE.ShapeGeometry(tri), lista = [], LARGO = 3.6;
  for (let i = 0; i < 12; i++) {
    const u = (i + 0.5) / 12, x = LARGO * u, y = -Math.sin(u * Math.PI) * 0.2;
    const b = G(), borde = new THREE.Mesh(geoTri, new THREE.MeshBasicMaterial({ color: tinta, side: THREE.DoubleSide })); borde.scale.set(1.2, 1.14, 1); borde.position.set(0, 0.02, -0.005);
    b.add(borde, new THREE.Mesh(geoTri, new THREE.MeshBasicMaterial({ color: i % 2 ? lejos : blanco, side: THREE.DoubleSide })));
    en(b, x, y, 0); banderines.add(b); lista.push(b);
  }
  const pts = []; for (let i = 0; i <= 24; i++) { const u = i / 24; pts.push(new THREE.Vector3(LARGO * u, -Math.sin(u * Math.PI) * 0.2 + 0.015, 0)); }
  const cuerda = new THREE.Mesh(new THREE.TubeGeometry(new THREE.CatmullRomCurve3(pts), 24, 0.014, 5), new THREE.MeshBasicMaterial({ color: tinta })); banderines.add(cuerda);
  en(banderines, -1.8, 3.36, -8.4); escena.add(banderines);
  piezas.banderines = { grupo: banderines, lista, cuerda };

  // repisa del fondo con el mando mostaza (no se toca en todo el video)
  const repisa = en(caja(1.0, 0.07, 0.4, blanco, 0.04), -2.36, 3.02, -9.78); escena.add(repisa);
  const texMando = new THREE.CanvasTexture(lienzo(440, 260, (g, w, h) => {
    g.lineJoin = 'round'; g.lineCap = 'round'; g.fillStyle = '#E8B33B'; g.strokeStyle = tinta; g.lineWidth = 16;
    g.beginPath(); g.moveTo(90, 60); g.lineTo(350, 60); g.quadraticCurveTo(420, 70, 415, 170); g.quadraticCurveTo(400, 235, 340, 205); g.lineTo(300, 160); g.lineTo(140, 160); g.lineTo(100, 205); g.quadraticCurveTo(40, 235, 25, 170); g.quadraticCurveTo(20, 70, 90, 60); g.closePath(); g.fill(); g.stroke();
    g.fillStyle = tinta; g.fillRect(100, 92, 16, 52); g.fillRect(82, 110, 52, 16);
    for (const [x, y] of [[315, 96], [345, 122], [285, 122], [315, 146]]) { g.beginPath(); g.arc(x, y, 11, 0, 7); g.fill(); }
  })); texMando.colorSpace = THREE.SRGBColorSpace;
  const mando = new THREE.Mesh(new THREE.PlaneGeometry(0.5, 0.3), new THREE.MeshBasicMaterial({ map: texMando, transparent: true, alphaTest: 0.3 }));
  en(mando, -2.36, 3.21, -9.72); escena.add(mando); piezas.mando_mostaza = mando;

  // compatibilidad con el contrato anterior: nada de «cajones» ni «pilar» en esta tienda
  return { cajones: [], pilar: new THREE.Group(), piezas, MEDIDAS };
}
