# Solución — Ejercicio 10.3 (Plotly)

```python
import pandas as pd
import plotly.express as px

# --- 1 ---
df = pd.read_csv("datasets/clean/tramites_personas_combinado.csv")

# --- 2 ---
fig = px.histogram(df, x="monto_asociado", nbins=20, title="Distribución de montos asociados")
fig.show()

# --- 3 ---
conteo = df["tipo_tramite"].value_counts().reset_index()
conteo.columns = ["tipo_tramite", "cantidad"]

fig = px.bar(conteo, x="tipo_tramite", y="cantidad", title="Cantidad de trámites por tipo")
fig.show()
# Reclamo Administrativo es el tipo más frecuente (214), Cambio de
# Domicilio el menos frecuente (157) — aunque las diferencias entre todos
# los tipos son relativamente chicas, ninguno domina de forma aplastante.

# --- 4 ---
fig = px.scatter(df, x="monto_asociado", y="id_tramite", color="estado")
fig.show()
# Al hacer zoom sobre una zona se puede examinar un grupo específico de
# puntos con más detalle; al hacer clic en un valor de la leyenda (por
# ejemplo, "Rechazado"), esa categoría se oculta del gráfico temporalmente,
# permitiendo comparar visualmente el resto sin ese grupo.

# --- 5 ---
fig = px.box(df, x="tipo_tramite", y="monto_asociado")
fig.show()
# La información que muestra es la misma que el boxplot de Seaborn (mismos
# cuartiles, mismos outliers) — la diferencia está en la EXPERIENCIA: acá
# se puede pasar el mouse sobre cada caja para ver los valores exactos de
# cada cuartil, en vez de tener que estimarlos visualmente como en la
# versión estática de Seaborn.

# --- 6 ---
fig.write_html("boxplot_tramites.html")
# Al abrir el archivo .html en el navegador (sin necesidad de tener Python
# corriendo), el gráfico sigue siendo completamente interactivo: zoom,
# hover y leyenda clickeable funcionan igual que en la notebook.
```

## Nota para el docente

El punto 5 es el más importante de este ejercicio a nivel conceptual: el objetivo es que el grupo note que Plotly y Seaborn muchas veces producen **la misma información estadística**, y la decisión de cuál usar pasa por el contexto de uso (¿el gráfico va a un documento estático o a algo que alguien va a explorar por su cuenta?), no por que uno sea "mejor" que el otro en términos de contenido.
