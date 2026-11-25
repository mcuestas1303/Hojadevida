# Palabras clave por producto (para el prompt 01)

Copia la línea del producto en **PALABRAS CLAVE** y **EXCLUIR** del prompt 01. Si agregas un producto nuevo, agrega su bloque aquí.

| Producto | Perfil del script | PALABRAS CLAVE | EXCLUIR |
|---|---|---|---|
| Uniformes y prendas con logo | `uniformes` | "uniforme", "uniformes", "camisa", "camiseta", "polo", "playera", "gabacha", "pantalón", "chumpa", "vestuario", "uniforme deportivo", "prendas de vestir", "bordado", "serigrafía", "estampado", "promocional" | uniformes escolares del MINEDUCYT, tela suelta y materia prima |
| Zapatos / calzado | `generico` | "zapato", "zapatos", "calzado", "botas", "botines", "bota de seguridad", "bota industrial", "botas de hule", "zapato escolar", "calzado de trabajo" | lo que no sea calzado |
| Chalecos | `generico` | "chaleco", "chalecos", "chaleco reflectivo", "chaleco de seguridad", "chaleco identificativo", "chaleco bordado", "chaleco táctico", "chaleco antibalas", "chaleco balístico", "chaleco salvavidas", "chaleco de brigadista" | lo que no sea chaleco |
| Gorras y promocionales textiles | `generico` | "gorra", "gorras", "gorro", "bolsa de tela", "bolsa ecológica", "camiseta promocional", "artículos promocionales", "estampado", "sublimado" | artículos que no sean textiles |

**Perfiles:**
- `generico`: incluye todo lo que trae la extensión, en una sola categoría. Sirve para empezar.
- `uniformes`: tiene reglas propias de exclusión y categorías.

Cuando un producto se vuelva frecuente, pídele a Claude Code que le arme su propio perfil en `scripts/datos.py`, siguiendo el de uniformes.
