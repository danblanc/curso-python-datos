# Clase 5 — Pandas: fundamentos

**Duración:** 2 horas
**Modalidad:** Virtual

## Objetivos de aprendizaje

- Explicar qué son las estructuras `Series` y `DataFrame` de Pandas.
- Leer datos desde distintas fuentes: CSV, Excel, JSON y una consulta SQL.
- Realizar una exploración inicial de un DataFrame (`.head()`, `.info()`, `.describe()`, detección de nulos).
- Seleccionar y filtrar filas y columnas usando `loc` e `iloc`.

## Contenidos

1. Series: la estructura unidimensional de Pandas
2. DataFrame: la estructura tabular de Pandas
3. Relación entre DataFrame, NumPy y diccionarios/listas
4. Lectura de datos: `read_csv`, `read_excel`, `read_json`, `read_sql`
5. Exploración inicial: `.head()`, `.tail()`, `.info()`, `.describe()`, `.shape`, `.dtypes`
6. Detección de valores nulos: `.isnull()`, `.sum()`
7. Selección de columnas
8. Filtrado de filas con condiciones booleanas
9. `loc` vs `iloc`: acceso por etiqueta vs. por posición

## Prerrequisitos

Clases 1 a 4, especialmente el manejo de NumPy y la lectura de archivos.

## Material

- [`slides.md`](./slides.md)
- [`ejercicios/ejercicio-05.md`](./ejercicios/ejercicio-05.md) — 30-40 min
- [`recursos/`](./recursos/)

Este ejercicio usa el dataset [`datasets/raw/registros_personas.csv`](../../datasets/raw/registros_personas.csv).

Soluciones en [`soluciones/clase-05/`](../../soluciones/clase-05/).
