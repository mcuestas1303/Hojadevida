// Graba la escena fotograma a fotograma con el Chromium de la sesión.
// Uso: node render.js <carpeta> [max_cuadros] [paleta] [entorno] [cada] [guion]   (cada = guarda 1 de cada N fotogramas; para revisar)
// Variables: SOLO=0,82 graba solo esos fotogramas; DESDE=300 empieza a grabar ahí; SECO=1 no graba ninguno (solo eventos y pistas: ≈ 1 min).
const { chromium } = (() => { try { return require('playwright'); } catch (e) { return require('playwright-core'); } })();   // NAVEGADOR=chrome|msedge usa el navegador instalado (playwright-core no trae uno)
const http = require('http'), fs = require('fs'), path = require('path');
const desde = parseInt(process.env.DESDE || '0', 10), solo = (process.env.SOLO || '').split(',').filter(Boolean).map(Number);
const salida = process.argv[2] || 'salida', maximo = parseInt(process.argv[3] || '230', 10);
const paleta = process.argv[4] || 'a_papel_con_fondo_frio', entorno = process.argv[5] || 'ciudad_de_carton', cada = parseInt(process.argv[6] || '1', 10), guion = process.argv[7] || 'prueba_2026-11-26';
const tipos = { '.html': 'text/html', '.js': 'text/javascript', '.png': 'image/png', '.json': 'application/json' };
const srv = http.createServer((q, r) => {
  const f = path.join(__dirname, decodeURIComponent(q.url.split('?')[0]));
  fs.readFile(f, (e, d) => { if (e) { r.writeHead(404); r.end(); } else { r.writeHead(200, { 'Content-Type': tipos[path.extname(f)] || 'application/octet-stream' }); r.end(d); } });
});
(async () => {
  await new Promise(ok => srv.listen(0, '127.0.0.1', ok));
  const url = `http://127.0.0.1:${srv.address().port}/escena.html?paleta=${paleta}&entorno=${entorno}&guion=${guion}`;
  fs.mkdirSync(path.join(salida, 'fotogramas'), { recursive: true });
  const b = await chromium.launch({ channel: process.env.NAVEGADOR || undefined, args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'] });
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  p.on('console', m => { if (m.type() === 'error') console.log('consola:', m.text()); });
  p.on('pageerror', e => console.log('error de página:', e.message));
  await p.goto(url); await p.waitForFunction('window.LISTO === true', null, { timeout: 60000 });
  const t0 = Date.now(); let n = 0, velocidades = [];
  for (; n < maximo; n++) {
    const guarda = process.env.SECO === '1' ? false : solo.length ? solo.includes(n) : (n >= desde && n % cada === 0);
    const r = await p.evaluate((g) => window.cuadro(g), guarda);
    velocidades.push(+r.velocidad.toFixed(2));
    if (guarda) {
    const d = await p.evaluate(() => window.foto());
    if (n % 100 === 0) console.log('fotograma', n);
    fs.writeFileSync(path.join(salida, 'fotogramas', `f_${String(n).padStart(4, '0')}.jpg`), Buffer.from(d.split(',')[1], 'base64'));
    }
    if (r.fin) { n++; break; }
  }
  const eventos = await p.evaluate(() => window.EVENTOS), medidas = await p.evaluate(() => window.MEDIDAS || {});
  fs.writeFileSync(path.join(salida, 'eventos.json'), JSON.stringify({ fps: 30, cuadros: n, eventos, medidas, velocidades }, null, 1));
  const pistas = await p.evaluate(() => window.PISTAS || []);
  if (pistas.length) fs.writeFileSync(path.join(salida, 'pistas.json'), JSON.stringify(pistas));
  console.log(`${n} fotogramas en ${((Date.now() - t0) / 1000).toFixed(0)} s`);
  await b.close(); srv.close();
})();
