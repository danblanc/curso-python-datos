# Ejercicio 10.3 — Plotly

**Duración estimada:** 20-25 minutos

## Objetivo

Practicar la construcción de gráficos interactivos con Plotly Express, y experimentar con la interactividad que agrega por defecto.

## Dataset

[`datasets/clean/tramites_personas_combinado.csv`](../../../datasets/clean/tramites_personas_combinado.csv)

## Consigna

1. Cargá el dataset (si ya lo tenés cargado, podés seguir usándolo) e importá `plotly.express as px`.

2. Usando `px.histogram()`, graficá la distribución de `monto_asociado`. Pasá el mouse sobre las barras y confirmá que ves los valores exactos (*hover*).

3. Contá la cantidad de trámites por `tipo_tramite` y graficalo con `px.bar()`, con título incluido.

4. Usando `px.scatter()`, graficá `monto_asociado` contra `id_tramite`, coloreando por `estado` con el parámetro `color`. Probá hacer zoom sobre una zona del gráfico, y probá hacer clic en un valor de la leyenda para ocultar esa categoría.

5. Usando `px.box()`, comparná la distribución de `monto_asociado` por `tipo_tramite`. Compará este resultado con el boxplot que hiciste en el ejercicio de Seaborn — ¿qué diferencias notás en la experiencia de uso, más allá de que muestran la misma información?

6. Exportá alguno de los gráficos anteriores a un archivo `.html` con `fig.write_html(...)`, abrilo con tu navegador, y confirmá que la interactividad se mantiene incluso fuera de la notebook.

## Qué se evalúa

- Uso correcto de `px.histogram()`, `px.bar()`, `px.scatter()` y `px.box()`.
- Uso del parámetro `color` para diferenciar categorías.
- Haber probado activamente la interactividad (zoom, hover, leyenda), no solo generado el gráfico.
- Exportación correcta a `.html`.

## Ayuda

Solución de referencia en [`soluciones/clase-10/`](../../../soluciones/clase-10/).
