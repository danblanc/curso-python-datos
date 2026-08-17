# Notas del docente — Clase 5

## Timing sugerido

| Bloque | Tiempo | Contenido |
|---|---|---|
| 1 | 10 min | Qué es Pandas, Series y DataFrame (slides 3-6) |
| 2 | 20 min | Lectura de datos: CSV, Excel, JSON, SQL (slides 7-8) |
| 3 | 20 min | Exploración inicial: head, info, describe, nulos (slides 9-12) |
| 4 | 20 min | Selección de columnas y filtrado (slides 13-14) |
| 5 | 20 min | `loc` vs `iloc` (slides 15-16) |
| 6 | 5 min | Resumen |
| 7 | 30-40 min | Ejercicio práctico |

## Preparación previa a la clase

Confirmar que todos tienen instalado, dentro de su entorno virtual:
```bash
pip install pandas openpyxl
```
`openpyxl` es necesario para leer/escribir Excel — es un error común olvidarlo y encontrarse con un `ImportError` recién al intentar `read_excel`.

## Tips de dictado

- **Apertura:** conectar explícitamente con la Clase 2/3 — "el DataFrame es, en el fondo, la lista de diccionarios que ya vimos, llevada a una herramienta especializada". Ese puente conceptual ya lo veníamos preparando desde antes.

- **Lectura de SQL (`read_sql`):** este curso no entra en detalle de cómo conectarse a una base de datos (queda fuera de alcance), así que conviene mostrarlo como **mención conceptual** con una captura o ejemplo ya resuelto, no como algo para que todos ejecuten en vivo (requeriría una base de datos disponible). Aclarar esto explícitamente para no generar expectativa de que van a conectarse a un SQL real en esta clase.

- **`.info()` y `.describe()`:** usar el dataset real del curso (`registros_personas.csv`) desde el principio, no un ejemplo de juguete — así el grupo ya empieza a familiarizarse con los datos que van a usar durante el resto del curso.

- **`&`/`|` vs `and`/`or`:** error clásico. Mostrar en vivo qué pasa si alguien usa `and` dentro de un filtro de Pandas (el error que tira, `ValueError: The truth value of a Series is ambiguous`) — así lo reconocen cuando les pase.

- **`loc` vs `iloc`:** es el concepto más confuso de la clase. Armar el ejemplo en vivo: filtrar el DataFrame, mostrar que el índice queda "con huecos", y ahí recién mostrar la diferencia entre ambos accesos. Verlo abstracto sin ese paso previo no ayuda a fijar la diferencia.

## Errores comunes a anticipar

- Olvidar `openpyxl` instalado para leer Excel.
- Usar `and`/`or` en vez de `&`/`|` en filtros.
- Olvidar los paréntesis al combinar condiciones: `df[df["edad"] >= 18 & df["provincia"] == "Córdoba"]` (sin paréntesis) da error — hay que aclarar que es obligatorio entre paréntesis cada condición.
- Confundir `df["columna"]` (Series) con `df[["columna"]]` (DataFrame de una columna).

## Cierre

Este es el arranque del módulo más largo del curso (Pandas). Vale la pena cerrar la clase remarcando que **todo lo que sigue construye sobre esto**: selección y filtrado son la base de transformación, limpieza y agregación que vienen en las próximas clases.
