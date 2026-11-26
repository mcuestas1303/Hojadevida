// Entorno «ciudad de cartón»: bloques a distintas distancias, tres cajones apilados y un pilar que se cae.
// Tema para el que se hizo: prueba técnica del 2026-11-26 (sin tema). Se puede reutilizar en videos de ciudad o de calle.
// Contrato de todo entorno: construir({THREE, escena, caja, C}) → { cajones: [objetos que se rompen], pilar: grupo que cae }.
export const FICHA = { id: 'ciudad_de_carton', temas: ['ciudad', 'calle', 'genérico'], rompibles: ['cajones', 'pilar'], creado: '2026-11-26' };

export function construir({ THREE, escena, caja, C }) {
  for (const [x, z, w, h] of [[-9, -9, 3, 7], [-5.2, -11, 2.4, 10], [-1.5, -13, 3.2, 6], [2.6, -10.5, 2.6, 9], [6.5, -9, 3, 5.5], [10, -12, 3, 11], [-12, -13, 3, 8], [0.5, -17, 4, 13]]) {
    const b = caja(w, h, w, z < -12 ? C.bloque_lejos : C.bloque_cerca, 0.08); b.position.set(x, h / 2, z); escena.add(b);
  }
  const cajones = [];
  for (const [x, y, z] of [[-3.5, 0.45, -1.9], [-2.6, 0.45, -1.9], [-3.05, 1.35, -1.9]]) { const c = caja(0.9, 0.9, 0.9, C.utileria); c.position.set(x, y, z); escena.add(c); cajones.push(c); }
  const pilar = new THREE.Group(); { const c = caja(0.7, 4.4, 0.7, C.bloque_lejos); c.position.y = 2.2; pilar.add(c); } pilar.position.set(3.7, 0, -2.3); escena.add(pilar);
  return { cajones, pilar };
}
