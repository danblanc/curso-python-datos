# Ejercicio 10.1 — Matplotlib

**Duración estimada:** 20-25 minutos

## Objetivo

Practicar la lógica de `figure`/`axes` y los cuatro tipos de gráfico básicos de Matplotlib.

## Dataset

[`datasets/clean/tramites_personas_combinado.csv`](../../../datasets/clean/tramites_personas_combinado.csv)

## Consigna

1. Cargá el dataset y convertí `fecha_inicio` a tipo fecha.

2. Creá una columna `mes` con el mes-año de `fecha_inicio` (pista: `.dt.to_period("M")`), agrupá por esa columna contando la cantidad de trámites, y graficá un **gráfico de línea** mostrando la evolución mes a mes.

3. Contá la cantidad de trámites por `estado` y graficalo como un **gráfico de barras**. Agregale título y etiquetas a los ejes.

4. Graficá un **histograma** de la columna `monto_asociado`, probando con al menos dos valores distintos de `bins` (por ejemplo, 10 y 30). ¿Cambia mucho la lectura del gráfico según cuántos `bins` uses?

5. Graficá un **gráfico de dispersión** entre `monto_asociado` (eje x) y `id_tramite` (eje y), usando una muestra de 200 filas al azar (`.sample(200, random_state=1)`) para que no quede sobrecargado de puntos.

6. Elegí uno de los gráficos anteriores, agregale título, etiquetas de ejes, y guardalo como archivo `.png` usando `plt.savefig()`.

## Qué se evalúa

- Uso correcto de `fig, ax = plt.subplots()` en cada gráfico.
- Los cuatro tipos de gráfico (línea, barras, histograma, dispersión) funcionando correctamente.
- Al menos un gráfico con título, etiquetas de ejes, y exportado a archivo.

## Ayuda

Solución de referencia en [`soluciones/clase-10/`](../../../soluciones/clase-10/).
