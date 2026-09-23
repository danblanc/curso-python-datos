# Clase 10 — Visualización de datos: Matplotlib, Seaborn y Plotly

**Duración:** ~4 horas (consolidación de tres librerías — ver nota en [`CRONOGRAMA.md`](../../CRONOGRAMA.md))
**Modalidad:** según el cronograma vigente del grupo

## Objetivos de aprendizaje

- Entender la lógica de `figure` y `axes` de Matplotlib, base sobre la que se apoyan las demás librerías de visualización en Python.
- Construir gráficos básicos con Matplotlib: líneas, barras, histogramas y dispersión.
- Usar Seaborn para gráficos estadísticos (distribuciones, comparaciones entre categorías, correlaciones) con menos código que Matplotlib puro.
- Construir visualizaciones interactivas con Plotly (zoom, hover, filtros).
- Tener un criterio propio para elegir qué herramienta usar según la situación: exploración rápida, reporte estático, o visualización interactiva.

## Contenidos

1. ¿Por qué visualizar? Elegir el gráfico adecuado para la pregunta
2. Matplotlib: la lógica de `figure` y `axes`
3. Matplotlib: gráficos de línea, barras, histograma y dispersión
4. Matplotlib: personalización (títulos, etiquetas, leyendas) y guardado de figuras
5. Seaborn: qué agrega por sobre Matplotlib
6. Seaborn: distribuciones (`histplot`, `boxplot`)
7. Seaborn: comparaciones entre categorías (`barplot`, `scatterplot`)
8. Seaborn: correlaciones (`heatmap`)
9. Plotly: la idea de interactividad
10. Plotly Express: gráficos interactivos equivalentes a los de Matplotlib/Seaborn
11. Matplotlib vs. Seaborn vs. Plotly: cuándo usar cada uno

## Prerrequisitos

Clases 5 a 9 completas (el dataset de esta clase ya viene limpio y combinado, dando por sentado todo el trabajo previo de Pandas).

## Material

- [`slides.md`](./slides.md)
- [`ejercicios/ejercicio-10-matplotlib.md`](./ejercicios/ejercicio-10-matplotlib.md) — ~20-25 min
- [`ejercicios/ejercicio-10-seaborn.md`](./ejercicios/ejercicio-10-seaborn.md) — ~20-25 min
- [`ejercicios/ejercicio-10-plotly.md`](./ejercicios/ejercicio-10-plotly.md) — ~20-25 min
- [`recursos/`](./recursos/)

Los tres ejercicios usan [`datasets/clean/tramites_personas_combinado.csv`](../../datasets/clean/tramites_personas_combinado.csv) — el dataset ya limpio y combinado de trámites + personas, generado a partir del trabajo de las Clases 5 a 9.

Soluciones en [`soluciones/clase-10/`](../../soluciones/clase-10/).

## Nota sobre el paquete a instalar

Vas a necesitar tres librerías nuevas en tu entorno:

```bash
pip install matplotlib seaborn plotly
```
