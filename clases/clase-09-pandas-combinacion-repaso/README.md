# Clase 9 — Pandas: combinación de datos y repaso

**Duración:** 2 horas
**Modalidad:** Virtual

## Objetivos de aprendizaje

- Combinar DataFrames con `pd.merge()`, entendiendo los distintos tipos de join (`inner`, `left`, `right`, `outer`).
- Concatenar DataFrames con `pd.concat()`.
- Diagnosticar problemas comunes al combinar datos (columnas clave no coincidentes, duplicados post-merge).
- Integrar, en un caso práctico, todo el flujo trabajado en las Clases 5 a 9 (lectura, limpieza, normalización, fechas, agregación, combinación).

## Contenidos

1. `pd.merge()`: sintaxis básica
2. Tipos de join: `inner`, `left`, `right`, `outer`
3. `left_on` / `right_on` cuando las columnas clave tienen distinto nombre
4. Verificación post-merge: `indicator=True`, chequeo de duplicados
5. `pd.concat()`: unir DataFrames por filas o columnas
6. Repaso integrador: caso práctico combinando personas + trámites + direcciones

## Prerrequisitos

Clases 5 a 8 completas — esta clase depende fuertemente de todo lo anterior.

## Material

- [`slides.md`](./slides.md)
- [`ejercicios/ejercicio-09.md`](./ejercicios/ejercicio-09.md) — 30-40 min (repaso integrador)
- [`recursos/`](./recursos/)

Este ejercicio usa los tres datasets: [`registros_personas.csv`](../../datasets/raw/registros_personas.csv), [`registros_tramites.xlsx`](../../datasets/raw/registros_tramites.xlsx) y [`registros_direcciones.json`](../../datasets/raw/registros_direcciones.json).

Soluciones en [`soluciones/clase-09/`](../../soluciones/clase-09/).

## Nota

Esta es la última clase del bloque de Pandas antes de pasar a visualización. Si el módulo de Pandas viene atrasado, esta es la clase más flexible para correr contenido hacia la Semana 3 (ver [`CRONOGRAMA.md`](../../CRONOGRAMA.md)).
