# Ejercicio 5 — Primera exploración con Pandas

**Duración estimada:** 30-40 minutos

## Objetivo

Practicar lectura, exploración inicial, selección y filtrado sobre un dataset real del curso.

## Dataset

Vamos a usar [`datasets/raw/registros_personas.csv`](../../../datasets/raw/registros_personas.csv). Asegurate de tener el repositorio del curso clonado o descargado, y ajustá la ruta según dónde esté ubicado tu script respecto a la carpeta `datasets/`.

## Consigna

Trabajá en una notebook (`.ipynb`) o script (`ejercicio_05.py`), como prefieras.

### Parte 1 — Cargar y explorar

1. Importá Pandas y cargá el dataset con `read_csv`.
2. Mostrá las primeras 5 filas con `.head()`.
3. Mostrá la forma del dataset (`.shape`) e imprimí un mensaje con la cantidad de filas y columnas.
4. Ejecutá `.info()` y respondé (en un comentario): ¿qué columnas tienen valores nulos?

### Parte 2 — Estadística rápida

5. Ejecutá `.describe()` sobre el dataset completo.
6. Ejecutá `.describe(include="object")` y compará qué información distinta te da respecto al paso anterior.

### Parte 3 — Nulos

7. Calculá la cantidad de valores nulos por columna con `.isnull().sum()`.
8. Identificá cuál es la columna con más valores nulos.

### Parte 4 — Selección y filtrado

9. Seleccioná solo las columnas `nombre`, `apellido` y `provincia`, y guardalas en un nuevo DataFrame.
10. Filtrá el DataFrame original para quedarte solo con las personas de la provincia `"Córdoba"`. ¿Cuántas hay? (usá `.shape` o `len()` sobre el resultado)
11. Filtrá para quedarte con las personas de `"Córdoba"` **que además** tengan el campo `email` no nulo. (pista: combiná el filtro de provincia con `.notnull()` sobre la columna `email`, usando `&`)

### Parte 5 — `loc` / `iloc`

12. Usando `.iloc`, mostrá las primeras 3 filas y solo las columnas `nombre` y `documento`.
13. Usando `.loc`, mostrá la fila con índice `0`, solo la columna `nombre`.

## Qué se evalúa

- Lectura correcta del CSV.
- Uso correcto de `.head()`, `.shape`, `.info()`, `.describe()`.
- Detección correcta de nulos por columna.
- Filtrado correcto combinando condiciones con `&`.
- Uso correcto de `loc` e `iloc` según lo pedido en cada caso.

## Ayuda

Solución de referencia en [`soluciones/clase-05/`](../../../soluciones/clase-05/).
