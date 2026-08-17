# Notas del docente — Clase 8

## Timing sugerido

| Bloque | Tiempo | Contenido |
|---|---|---|
| 1 | 20 min | El problema de fechas como texto + conversión (slides 3-6) |
| 2 | 15 min | Componentes (`.dt`) y diferencias entre fechas (slides 7-9) |
| 3 | 15 min | Filtrado por rango de fechas (slide 10) |
| 4 | 25 min | `.groupby()` básico y con `.agg()` (slides 11-14) |
| 5 | 15 min | Agrupar por múltiples columnas (slide 15) |
| 6 | 15 min | `pivot_table()` (slides 16-17) |
| 7 | 5 min | Resumen |
| 8 | 30-40 min | Ejercicio práctico |

## Tips de dictado

- **Conversión de fechas mixtas:** este dataset (`registros_tramites.xlsx`) tiene formatos de fecha genuinamente variados a propósito. Mostrar primero qué pasa con `pd.to_datetime()` "a secas" (sin `format="mixed"`) — en versiones recientes de Pandas suele funcionar igual, pero vale la pena mostrar el parámetro explícito para que quede claro qué está pasando, y qué hacer si en algún momento falla por ambigüedad.

- **`dayfirst=True`:** explicar el porqué con un ejemplo concreto: `"03/07/2025"` — ¿es 3 de julio o 7 de marzo? En Argentina/España es 3 de julio (día primero), pero Pandas por defecto asume el formato estadounidense (mes primero) si no se lo indicamos.

- **`.groupby()`:** es un concepto potente pero puede sentirse abstracto la primera vez. Antes de mostrar código, plantear la pregunta en palabras ("quiero saber el monto total por cada tipo de trámite") y recién después mostrar cómo se traduce a `.groupby()` — que la sintaxis responda a una pregunta concreta, no al revés.

- **`.agg()` con nombres personalizados (slide 14):** remarcar que esta forma es la que se va a usar en la práctica para armar reportes, porque el resultado ya sale con nombres de columna legibles — es más código que la versión simple, pero ahorra trabajo de renombrar después.

- **Tablas pivote:** si el grupo tiene experiencia con Excel, apoyarse en esa analogía explícitamente — suele ser el momento donde más "clic" hace la clase para quienes vienen de un perfil más administrativo que técnico.

## Errores comunes a anticipar

- Intentar operaciones de fecha (`.dt.year`, restas) sobre una columna que sigue siendo texto (olvidar la conversión con `pd.to_datetime` antes).
- Confundir `.count()` (cuenta no nulos de una columna específica) con `.size()` (cuenta todas las filas del grupo, incluyendo nulos) — mostrar un caso donde ambos dan resultados distintos.
- En `pivot_table()`, olvidar `fill_value=0` y encontrarse con `NaN` en combinaciones que no tienen datos, lo cual puede ser confuso en un reporte.

## Cierre

Antes de pasar a la Clase 9 (merge/combinación), confirmar que el grupo puede resolver una pregunta de agregación de punta a punta: convertir fecha, agrupar, aplicar `.agg()` con nombres — es la habilidad que más se reutiliza en la clase siguiente y en el proyecto final.
