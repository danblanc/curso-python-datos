# Clase 6 — Pandas: transformación y limpieza

**Duración:** 2 horas
**Modalidad:** Virtual

## Objetivos de aprendizaje

- Crear nuevas columnas a partir de columnas existentes.
- Aplicar funciones propias sobre columnas con `.apply()`.
- Identificar y tratar valores nulos (eliminar o imputar, según el caso).
- Identificar y eliminar filas duplicadas, incluyendo duplicados "no triviales".
- Convertir tipos de datos de columnas (`astype`, `to_numeric`).

## Contenidos

1. Creación de columnas nuevas (operaciones directas entre columnas)
2. `.apply()` con funciones propias
3. `.apply()` con funciones lambda
4. Tratamiento de nulos: `.dropna()`, `.fillna()`
5. Criterios para decidir cuándo eliminar y cuándo imputar un nulo
6. Detección de duplicados: `.duplicated()`
7. Eliminación de duplicados: `.drop_duplicates()`
8. Conversión de tipos: `.astype()`, `pd.to_numeric()`, manejo de errores de conversión

## Prerrequisitos

Clase 5 (lectura, exploración, selección, filtrado).

## Material

- [`slides.md`](./slides.md)
- [`ejercicios/ejercicio-06.md`](./ejercicios/ejercicio-06.md) — 30-40 min
- [`recursos/`](./recursos/)

Este ejercicio usa [`datasets/raw/registros_personas.csv`](../../datasets/raw/registros_personas.csv).

Soluciones en [`soluciones/clase-06/`](../../soluciones/clase-06/).
