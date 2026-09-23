# Notas del docente — Clase 10

Esta clase consolida tres librerías (Matplotlib, Seaborn, Plotly) y por eso es más larga que el resto — se recomienda dictarla en un bloque de **~4 horas**, con un descanso a mitad de camino. Si el cronograma efectivo del grupo usa clases de 4h (formato 5x4h + 5x6h), esta es una candidata natural para ese formato.

## Timing sugerido (bloque de ~4h)

| Bloque | Tiempo | Contenido |
|---|---|---|
| 1 | 10 min | Por qué visualizar, cómo elegir el gráfico (slides 3-5) |
| 2 | 45 min | Matplotlib: figure/axes, línea, barras, histograma, scatter (slides 7-12) |
| 3 | 15 min | Personalización y guardado de figuras (slides 13-14) |
| 4 | 20-25 min | **Ejercicio 1 (Matplotlib)** |
| — | 10 min | Descanso |
| 5 | 10 min | Qué agrega Seaborn (slides 17-18) |
| 6 | 40 min | Seaborn: histplot, boxplot, barplot, scatterplot, heatmap (slides 19-23) |
| 7 | 10 min | Antes de graficar: revisar columnas calculadas (slide 24) |
| 8 | 20-25 min | **Ejercicio 2 (Seaborn)** |
| 9 | 10 min | La idea de interactividad (slides 27-28) |
| 10 | 25 min | Plotly Express y equivalentes (slides 29-31) |
| 11 | 10 min | Guardar gráficos de Plotly (slide 32) |
| 12 | 20-25 min | **Ejercicio 3 (Plotly)** |
| 13 | 10 min | Comparación de las tres + resumen (slides 34-36) |

Total aproximado: ~4h con descanso incluido. Si el grupo dispone de menos tiempo, la sección más recortable es la de Matplotlib (bloques 2-3): el objetivo mínimo ahí es que entiendan `figure`/`axes`, ya que Seaborn se apoya en la misma lógica.

## Preparación previa a la clase

```bash
pip install matplotlib seaborn plotly
```

Confirmar que el grupo ya tiene generado (o descargado) `datasets/clean/tramites_personas_combinado.csv` — si alguien solo trabajó con los datasets `raw/` hasta ahora, este archivo puede no estar en su carpeta.

## Tips de dictado

- **Apertura (slide 5):** la tabla "pregunta → tipo de gráfico" es más útil si se las hace completar a ellos primero con ejemplos propios, antes de mostrarla armada — genera más enganche que presentarla directamente.

- **`figure`/`axes` (slide 8):** este concepto se resiste un poco al principio, porque en muchos tutoriales online se usa `plt.plot()` directamente (sin `fig, ax = plt.subplots()`), lo cual funciona pero oculta la lógica de fondo. Vale la pena remarcar que `plt.subplots()` es la forma recomendada porque escala mejor (permite varios gráficos en una misma figura más adelante), aunque no lleguemos a cubrir subplots múltiples en este curso.

- **Seaborn — el salto de "qué agrega" (slide 18):** la mejor forma de que se sienta el salto es mostrar el **mismo gráfico** (por ejemplo, el barplot de monto promedio por provincia) primero armado a mano con Matplotlib puro (calculando el promedio con `.groupby()` y después graficando) y después con una sola línea de `sns.barplot()`. La diferencia de líneas de código habla por sí sola.

- **`edad` con dato corregido (slide 24):** el dataset del curso tenía originalmente un problema real de años de 2 dígitos mal interpretados (fechas de nacimiento que quedaban en el futuro). Ya está corregido en `datasets/clean/`, pero vale la pena **contar esto como anécdota real** en vez de ocultarlo — es exactamente el tipo de verificación que venimos reforzando en todo el curso, y refuerza que ni siquiera el dataset "ya limpio" está exento de revisión.

- **Plotly — la demo en vivo importa más que las slides:** en esta sección específicamente, mostrar la interactividad en vivo (zoom, hover, click en la leyenda) tiene mucho más impacto que cualquier slide. Si el tiempo aprieta, es preferible recortar texto de las slides y no la demo en vivo.

- **Cierre (slide 37):** conectar explícitamente con la próxima clase — que quede claro que el trabajo de hoy con Plotly no es un cierre en sí mismo, sino la base directa de lo que viene.

## Errores comunes a anticipar

- Olvidar `plt.show()` al final de un bloque de Matplotlib/Seaborn en un script (no hace falta en Jupyter, donde el gráfico se muestra automáticamente al final de la celda — puede generar confusión si el grupo alterna entre notebook y script).
- Etiquetas de eje x superpuestas por texto largo (categorías con nombres largos) — recordar `plt.xticks(rotation=45, ha="right")` y `plt.tight_layout()`.
- Confundir `ax.bar()` (Matplotlib, espera valores ya agregados) con `sns.barplot()` (Seaborn, agrega internamente) — es una fuente común de gráficos "que no dan los números esperados" si se usan como si fueran intercambiables.
- Con Plotly, olvidar que `fig.show()` puede no renderizar directamente en algunos entornos de terminal/script — en notebook funciona sin problemas.

## Cierre

Antes de pasar a Streamlit, confirmar que el grupo puede armar, sin ayuda, al menos un gráfico de cada librería sobre el dataset del curso — es la base directa sobre la que se construye el dashboard de las próximas clases.
