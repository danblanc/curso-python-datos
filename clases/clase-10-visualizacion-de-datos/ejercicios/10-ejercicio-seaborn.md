# Ejercicio 10.2 — Seaborn

**Duración estimada:** 20-25 minutos

## Objetivo

Practicar gráficos estadísticos con Seaborn: distribuciones, comparaciones entre categorías y correlaciones.

## Dataset

[`datasets/clean/tramites_personas_combinado.csv`](../../../datasets/clean/tramites_personas_combinado.csv)

## Consigna

1. Cargá el dataset (si ya lo tenés cargado del ejercicio anterior, podés seguir usándolo).

2. Graficá la distribución de `monto_asociado` con `sns.histplot()`.

3. Usando `sns.boxplot()`, comparná la distribución de `monto_asociado` según `estado` (un boxplot por cada estado). ¿Alguno de los estados muestra una dispersión claramente distinta a los demás?

4. Usando `sns.barplot()`, graficá el monto promedio por `provincia_tramite`. Compará el resultado con lo que obtendrías calculando el promedio "a mano" con `.groupby()` — ¿coinciden los valores?

5. Calculá una columna nueva `edad`, a partir de `fecha_nacimiento`, expresada en años. Antes de graficarla, revisá con `.describe()` que los valores tengan sentido (mínimo y máximo razonables para una edad).

6. Usando `sns.scatterplot()`, graficá `edad` (eje x) contra `monto_asociado` (eje y), coloreando los puntos según `estado` con el parámetro `hue`.

7. Generá un `sns.heatmap()` con la correlación entre `edad` y `monto_asociado`. ¿Qué tan fuerte es la relación entre ambas variables, según el resultado?

## Qué se evalúa

- Uso correcto de `histplot`, `boxplot`, `barplot`, `scatterplot` y `heatmap`.
- Verificación de la columna `edad` antes de graficarla (no asumir que el cálculo salió bien sin revisar).
- Uso correcto del parámetro `hue` para agregar una dimensión categórica a un gráfico.

## Ayuda

Solución de referencia en [`soluciones/clase-10/`](../../../soluciones/clase-10/).
