# Compras públicas (COMPRASAL) · kit para ofertar

Kit para encontrar oportunidades de compras públicas en COMPRASAL y preparar ofertas sin olvidar ningún requisito. Sirve para cualquier producto, sin tener que reescribir las instrucciones cada vez.

## Los dos flujos

| Quiero… | Pego en la extensión de Chrome | Guardo la respuesta en | En Claude Code escribo |
|---|---|---|---|
| Saber quién compra un producto, cuándo y por cuánto | `prompts/01_buscar_procesos.md` | `datos/<producto>/*.csv` | `/compras-calendario <producto>` |
| Preparar una oferta para un proceso concreto | `prompts/02_extraer_bases_y_requisitos.md` | `procesos/<CÓDIGO>/respuesta.md` (y los PDF en `procesos/<CÓDIGO>/pdf/`) | `/compras-revisar-proceso <CÓDIGO>` |

Claude Code arma el Excel, pone a agentes a revisarlo y, si falta algo, te da el **prompt 03** con solo las preguntas pendientes.

## Qué hay en cada carpeta

- **`prompts/`**: los textos para pegar en la extensión. Solo cambias las líneas entre corchetes.
- **`catalogo/palabras_clave.md`**: palabras de búsqueda probadas por producto: uniformes, zapatos, chalecos y promocionales.
- **`catalogo/requisitos_comunes.csv`**: requisitos que las bases suelen pedir. Sirve de red de seguridad: si la respuesta no menciona alguno, la lista de verificación avisa para confirmarlo. No significa que el proceso lo exija.
- **`scripts/`**:
  - `datos.py`: carga y limpieza de los CSV.
  - `calendario.py`: arma el calendario de oportunidades.
  - `checklist.py`: arma la lista de verificación de una oferta.
- **`datos/`**: los CSV de cada producto.
- **`procesos/`**: una carpeta por proceso revisado.
- **`calendario_uniformes_2027.xlsx`**: el calendario actual de uniformes.

## Hacerlo sin copiar y pegar

Las sesiones de Claude Code en la nube **no pueden manejar tu Chrome**.

Si abres Claude Code en tu computadora (app de escritorio o terminal) con la extensión Claude in Chrome conectada, los dos comandos usan la extensión directamente:
- buscan y leen los procesos;
- descargan los PDF;
- lanzan a los agentes a revisar;
- repreguntan lo que falte.

Todo eso sin que tengas que pegar nada.

## Comandos a mano (opcional)

```bash
python3 compras-publicas/scripts/calendario.py --datos compras-publicas/datos/uniformes --perfil uniformes --producto "Uniformes y prendas" --anio 2027 --salida compras-publicas/calendario_uniformes_2027.xlsx
```

```bash
python3 compras-publicas/scripts/checklist.py compras-publicas/procesos/<CÓDIGO>/respuesta.md
```

Necesitan Python 3 con `pandas` y `openpyxl`.
