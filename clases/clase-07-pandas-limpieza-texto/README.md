# Clase 7 — Pandas: limpieza de texto

**Duración:** 2 horas
**Modalidad:** Virtual

## Objetivos de aprendizaje

- Usar los métodos de texto vectorizados de Pandas (accesor `.str`).
- Normalizar strings: mayúsculas/minúsculas, espacios, tildes.
- Escribir y aplicar expresiones regulares básicas para limpiar formatos inconsistentes.
- Normalizar columnas de identificadores (documentos) a un formato único.
- Comprender por qué la normalización de texto es un paso crítico previo a comparar o vincular registros administrativos.

## Contenidos

1. El accesor `.str` de Pandas
2. Mayúsculas, minúsculas y capitalización (`.upper()`, `.lower()`, `.title()`)
3. Espacios: `.strip()`, `.replace()`
4. Tildes y caracteres especiales (normalización Unicode)
5. Expresiones regulares: conceptos básicos (`re`, `.str.replace()` con regex)
6. Extracción de patrones con `.str.extract()`
7. Normalización de documentos/identificadores a un formato único
8. Por qué esto importa: puente hacia análisis de similitud de registros

## Prerrequisitos

Clase 6 (transformación, `.apply()`, nulos, duplicados).

## Material

- [`slides.md`](./slides.md)
- [`ejercicios/ejercicio-07.md`](./ejercicios/ejercicio-07.md) — 30-40 min
- [`recursos/`](./recursos/)

Este ejercicio usa [`datasets/raw/registros_personas.csv`](../../datasets/raw/registros_personas.csv).

Soluciones en [`soluciones/clase-07/`](../../soluciones/clase-07/).

## Nota

Esta clase tiene peso especial dentro del curso: la normalización de texto es la habilidad que conecta más directamente con el trabajo de análisis de similitud de registros administrativos que se dicta después de este curso.
