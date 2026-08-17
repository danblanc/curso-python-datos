# Clase 8 — Pandas: fechas y agregación

**Duración:** 2 horas
**Modalidad:** Virtual

## Objetivos de aprendizaje

- Convertir columnas de texto a tipo fecha (`datetime`) con `pd.to_datetime()`.
- Extraer componentes de una fecha (año, mes, día, día de la semana).
- Calcular diferencias entre fechas.
- Agrupar datos con `.groupby()` y aplicar funciones de agregación.
- Construir tablas pivote con `pd.pivot_table()`.

## Contenidos

1. Conversión de texto a fecha: `pd.to_datetime()`, manejo de formatos mixtos
2. Componentes de una fecha: `.dt.year`, `.dt.month`, `.dt.day`, `.dt.day_name()`
3. Diferencias entre fechas (`timedelta`)
4. `.groupby()`: agrupar y agregar (`sum`, `mean`, `count`, `size`)
5. Múltiples agregaciones con `.agg()`
6. Agrupar por más de una columna
7. Tablas pivote con `pd.pivot_table()`

## Prerrequisitos

Clases 5 a 7.

## Material

- [`slides.md`](./slides.md)
- [`ejercicios/ejercicio-08.md`](./ejercicios/ejercicio-08.md) — 30-40 min
- [`recursos/`](./recursos/)

Este ejercicio usa [`datasets/raw/registros_tramites.xlsx`](../../datasets/raw/registros_tramites.xlsx).

Soluciones en [`soluciones/clase-08/`](../../soluciones/clase-08/).
