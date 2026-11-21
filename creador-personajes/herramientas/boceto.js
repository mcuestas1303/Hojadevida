#!/usr/bin/env node
/*
 * Dibuja el boceto gratis de un personaje a partir de su ficha JSON, usando la misma
 * vista previa del creador (index.html). No llama a ninguna API ni gasta créditos.
 *
 * Uso:  node creador-personajes/herramientas/boceto.js <ficha.json> [salida.png]
 * Imprime también el prompt para Higgsfield que arma la vista previa con esa ficha.
 */
'use strict';
const path = require('path');
const fs = require('fs');
const { chromium } = require('playwright');

(async () => {
  const [, , fichaRuta, salidaArg] = process.argv;
  if (!fichaRuta) { console.error('Uso: node boceto.js <ficha.json> [salida.png]'); process.exit(1); }
  const ficha = JSON.parse(fs.readFileSync(fichaRuta, 'utf8'));
  const salida = salidaArg || fichaRuta.replace(/\.json$/i, '') + '.png';
  const pagina = 'file://' + path.resolve(__dirname, '..', 'index.html');

  const navegador = await chromium.launch();
  const p = await navegador.newPage({ viewport: { width: 1200, height: 900 }, deviceScaleFactor: 2 });
  const errores = [];
  p.on('pageerror', (e) => errores.push(e.message));
  await p.goto(pagina);
  await p.evaluate((f) => cargar(f), ficha);           // cargar() es global en app.js
  await p.locator('#avatar svg').screenshot({ path: salida });
  const prompt = await p.textContent('#oImagen');
  await navegador.close();

  if (errores.length) { console.error('Errores en la página:', errores.join(' | ')); process.exit(2); }
  console.log('BOCETO: ' + path.resolve(salida));
  console.log('PROMPT_VISTA_PREVIA: ' + prompt);
})();
