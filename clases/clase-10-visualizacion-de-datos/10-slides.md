---
marp: true
theme: default
paginate: true
size: 16:9
---

# Clase 10
## Visualización de datos: Matplotlib, Seaborn y Plotly

Curso de Python para Análisis de Datos

---

# Agenda de hoy

1. Por qué visualizar, y cómo elegir el gráfico correcto
2. Matplotlib: la base de todo
3. Seaborn: gráficos estadísticos con menos código
4. Plotly: interactividad
5. Cuándo usar cada una
6. Tres ejercicios prácticos (uno por librería)

---

# ¿Por qué visualizar?

Una tabla con miles de filas no se "lee" de un vistazo. Un gráfico bien elegido comunica en segundos algo que una tabla tardaría minutos en transmitir.

Pero un gráfico mal elegido **confunde más de lo que ayuda**. Antes de graficar, conviene preguntarse: ¿qué pregunta estoy tratando de responder?

---

# Eligiendo el gráfico según la pregunta

| Pregunta | Tipo de gráfico |
|---|---|
| ¿Cómo cambia algo en el tiempo? | Línea |
| ¿Cómo se comparan categorías entre sí? | Barras |
| ¿Cómo se distribuyen mis datos? | Histograma / boxplot |
| ¿Hay relación entre dos variables numéricas? | Dispersión (scatter) |
| ¿Cómo se relacionan varias variables numéricas a la vez? | Mapa de calor (heatmap) |

---

# Tres librerías, tres propósitos

- **Matplotlib**: la librería base de visualización en Python. Todo lo demás se apoya en ella. Da control total, pero requiere más código.
- **Seaborn**: construida sobre Matplotlib, pensada específicamente para visualización **estadística**. Menos código para gráficos más comunes en análisis de datos.
- **Plotly**: gráficos **interactivos** (zoom, hover, filtros). Ideal para exploración y para integrarlos después en un dashboard.

---

# Parte 1: Matplotlib

---

# La lógica de `figure` y `axes`

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()   # fig = el "lienzo" completo, ax = el área del gráfico
ax.plot([1, 2, 3], [10, 20, 15])
plt.show()
```

- `fig` (figure): el lienzo completo, puede contener uno o más gráficos.
- `ax` (axes): el área específica donde se dibuja un gráfico. Es el objeto sobre el que se llama a casi todos los métodos de graficado.

Esta lógica se repite, casi sin cambios, en Seaborn.

---

# Gráfico de línea

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("datasets/clean/tramites_personas_combinado.csv")
df["fecha_inicio"] = pd.to_datetime(df["fecha_inicio"])
df["mes"] = df["fecha_inicio"].dt.to_period("M")

por_mes = df.groupby("mes").size()

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(por_mes.index.astype(str), por_mes.values)
plt.xticks(rotation=45)
plt.show()
```

Ideal para mostrar una evolución en el tiempo — en este caso, cantidad de trámites iniciados por mes.

---

# Gráfico de barras

```python
conteo = df["tipo_tramite"].value_counts()

fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(conteo.index, conteo.values)
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
```

`plt.tight_layout()` ajusta automáticamente los márgenes para que las etiquetas largas (como nombres de categorías) no queden cortadas.

---

# Histograma

```python
fig, ax = plt.subplots()
ax.hist(df["monto_asociado"], bins=20)
ax.set_xlabel("Monto asociado")
ax.set_ylabel("Frecuencia")
plt.show()
```

Un histograma agrupa valores numéricos en "cajones" (`bins`) y cuenta cuántas observaciones caen en cada uno — muestra la **forma de la distribución** de una variable.

---

# Gráfico de dispersión (scatter)

```python
fig, ax = plt.subplots()
ax.scatter(df["monto_asociado"], df["id_tramite"])
ax.set_xlabel("Monto asociado")
ax.set_ylabel("ID de trámite")
plt.show()
```

Útil para ver si existe algún patrón o relación entre dos variables numéricas.

---

# Personalización: títulos, etiquetas, leyendas

```python
fig, ax = plt.subplots()
ax.bar(conteo.index, conteo.values, color="steelblue")
ax.set_title("Cantidad de trámites por tipo")
ax.set_xlabel("Tipo de trámite")
ax.set_ylabel("Cantidad")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
```

Un gráfico sin título ni etiquetas de ejes obliga a quien lo mira a adivinar qué está viendo — nunca es opcional en un reporte real.

---

# Guardar una figura como archivo

```python
fig, ax = plt.subplots()
ax.bar(conteo.index, conteo.values)
plt.tight_layout()
plt.savefig("tramites_por_tipo.png", dpi=150)
```

`dpi` controla la resolución — 150 es un buen valor por defecto para uso en documentos o presentaciones.

---

# Ejercicio 1 (Matplotlib)

Ver [`ejercicios/ejercicio-10-matplotlib.md`](./ejercicios/ejercicio-10-matplotlib.md) — ~20-25 minutos.

---

# Parte 2: Seaborn

---

# ¿Qué agrega Seaborn?

Seaborn está construido **sobre** Matplotlib (por debajo, sigue usando `figure`/`axes`), pero:

- Funciona directamente con DataFrames de Pandas (le pasás columnas por nombre, no arrays sueltos).
- Tiene gráficos estadísticos ya armados (distribuciones, comparaciones con intervalos de confianza, correlaciones) que en Matplotlib puro requerirían mucho más código.
- Un estilo visual más prolijo por defecto.

```python
import seaborn as sns
```

---

# Distribuciones: `histplot`

```python
import seaborn as sns
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
sns.histplot(data=df, x="monto_asociado", bins=20, ax=ax)
plt.show()
```

Mismo resultado conceptual que el histograma de Matplotlib, pero recibe el DataFrame y el nombre de columna directamente — no hace falta extraer el array primero.

---

# Distribuciones: `boxplot`

```python
fig, ax = plt.subplots(figsize=(10, 5))
sns.boxplot(data=df, x="tipo_tramite", y="monto_asociado", ax=ax)
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
```

Un boxplot muestra, para cada categoría, la mediana, los cuartiles y los valores atípicos (*outliers*) — mucho más informativo que un promedio simple cuando querés comparar la dispersión entre grupos.

---

# Comparaciones entre categorías: `barplot`

```python
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(data=df, x="provincia_tramite", y="monto_asociado", estimator="mean", ax=ax)
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
```

A diferencia de `ax.bar()` de Matplotlib (que grafica valores ya calculados), `sns.barplot()` **calcula el agregado por vos** (por defecto, el promedio) a partir de los datos crudos.

---

# Dispersión con color por categoría: `scatterplot`

```python
fig, ax = plt.subplots()
sns.scatterplot(
    data=df.sample(200, random_state=1),
    x="monto_asociado", y="id_tramite",
    hue="estado", ax=ax,
)
plt.show()
```

El parámetro `hue` colorea los puntos según una columna categórica — agregar una tercera dimensión al gráfico sin esfuerzo extra.

---

# Correlaciones: `heatmap`

```python
numericas = df[["edad", "monto_asociado"]]

fig, ax = plt.subplots(figsize=(6, 5))
sns.heatmap(numericas.corr(), annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
plt.show()
```

`annot=True` muestra el valor numérico dentro de cada celda. Un valor cercano a 1 o -1 indica correlación fuerte; cercano a 0, poca o ninguna relación.

---

# Antes de graficar: revisá tus columnas calculadas

Si vas a calcular una columna nueva (como `edad` a partir de `fecha_nacimiento`) antes de graficarla, **no des por sentado que el cálculo salió bien**.

```python
df["fecha_nacimiento"] = pd.to_datetime(df["fecha_nacimiento"])
hoy = pd.Timestamp.today()
df["edad"] = (hoy - df["fecha_nacimiento"]).dt.days / 365.25

df["edad"].describe()   # ¿el mínimo y el máximo tienen sentido?
```

Un histograma de una columna calculada incorrectamente (por ejemplo, con edades negativas por un problema de formato de fecha) es, muchas veces, la primera señal visual de que algo salió mal antes en el proceso.

---

# Ejercicio 2 (Seaborn)

Ver [`ejercicios/ejercicio-10-seaborn.md`](./ejercicios/ejercicio-10-seaborn.md) — ~20-25 minutos.

---

# Parte 3: Plotly

---

# La idea de la interactividad

Los gráficos de Matplotlib y Seaborn son **imágenes estáticas**: una vez generados, no se pueden explorar más.

Plotly genera gráficos **interactivos**: se puede hacer zoom, pasar el mouse para ver valores exactos (*hover*), ocultar/mostrar categorías haciendo clic en la leyenda, y más — todo sin escribir código adicional.

---

# Plotly Express: la forma rápida

```python
import plotly.express as px

fig = px.histogram(df, x="monto_asociado", nbins=20)
fig.show()
```

`plotly.express` (se importa como `px`) ofrece funciones de alto nivel muy similares en espíritu a Seaborn — mucho resultado con poco código.

---

# Equivalentes directos a lo que ya vimos

```python
# Barras
conteo = df["tipo_tramite"].value_counts().reset_index()
conteo.columns = ["tipo_tramite", "cantidad"]
fig = px.bar(conteo, x="tipo_tramite", y="cantidad", title="Trámites por tipo")
fig.show()

# Dispersión con color por categoría
fig = px.scatter(df, x="monto_asociado", y="id_tramite", color="estado")
fig.show()

# Boxplot
fig = px.box(df, x="tipo_tramite", y="monto_asociado")
fig.show()
```

La sintaxis es muy parecida a Seaborn — si ya entendiste Seaborn, Plotly Express se aprende rápido.

---

# ¿Dónde se ve la interactividad?

- **Zoom**: hacer clic y arrastrar sobre una zona del gráfico
- **Hover**: pasar el mouse sobre un punto/barra muestra sus valores exactos
- **Leyenda clickeable**: hacer clic en una categoría de la leyenda la oculta/muestra
- **Exportar la imagen**: botón de cámara que aparece al pasar el mouse por la esquina del gráfico

Todo esto viene incluido **sin escribir código adicional** — es el comportamiento por defecto de cualquier gráfico de Plotly.

---

# Guardar un gráfico de Plotly

```python
fig.write_html("grafico_interactivo.html")   # mantiene la interactividad
fig.write_image("grafico_estatico.png")       # imagen fija (requiere el paquete kaleido)
```

El archivo `.html` se puede abrir directamente en un navegador y mantiene todo el comportamiento interactivo, sin necesidad de tener Python instalado para verlo.

---

# ¿Por qué nos importa Plotly en particular?

Plotly es la librería de visualización que vamos a **integrar directamente en Streamlit** para construir el dashboard del curso (próximas clases).

Los mismos gráficos que armamos hoy con `px.bar()`, `px.scatter()`, etc. van a insertarse tal cual dentro de una app de Streamlit, con muy pocos cambios.

---

# Ejercicio 3 (Plotly)

Ver [`ejercicios/ejercicio-10-plotly.md`](./ejercicios/ejercicio-10-plotly.md) — ~20-25 minutos.

---

# Matplotlib vs. Seaborn vs. Plotly

| | Matplotlib | Seaborn | Plotly |
|---|---|---|---|
| Control fino | Máximo | Medio | Medio |
| Rapidez para gráficos estadísticos | Baja | Alta | Alta |
| Interactividad | No | No | Sí |
| Uso típico | Base, personalización total | Análisis exploratorio | Exploración + dashboards |

---

# ¿Cuál uso en cada momento?

- **Explorando datos por tu cuenta, rápido:** Seaborn primero — resuelve la mayoría de los casos con poco código.
- **Necesitás algo muy personalizado o específico que Seaborn no ofrece:** Matplotlib directamente (o Seaborn + ajustes finales en Matplotlib, ya que son compatibles entre sí).
- **El gráfico va a un dashboard, o alguien más lo va a explorar interactivamente:** Plotly.

No es necesario elegir una sola para todo el curso — de hecho, es común combinarlas según el momento del análisis.

---

# Resumen de la clase

- Matplotlib: la base (`figure`/`axes`), control total, más código
- Seaborn: gráficos estadísticos con menos código, pensado para DataFrames
- Plotly: interactividad, base para los dashboards que vienen
- La elección de herramienta depende del momento: exploración rápida, análisis a fondo, o producto final interactivo

---

# Próxima clase

Vamos a dar el salto de "generar gráficos" a "construir una aplicación": introducción a Streamlit, donde estos mismos gráficos de Plotly se van a integrar en un dashboard funcional.
