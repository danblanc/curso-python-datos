# Solución — Ejercicio 10.2 (Seaborn)

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- 1 ---
df = pd.read_csv("datasets/clean/tramites_personas_combinado.csv")

# --- 2 ---
fig, ax = plt.subplots()
sns.histplot(data=df, x="monto_asociado", bins=20, ax=ax)
plt.show()

# --- 3 ---
fig, ax = plt.subplots(figsize=(10, 5))
sns.boxplot(data=df, x="estado", y="monto_asociado", ax=ax)
plt.tight_layout()
plt.show()
# Los 5 estados muestran una dispersión bastante similar entre sí (los
# cuartiles y el rango de valores no difieren dramáticamente de un estado a
# otro) — no hay un estado que se destaque claramente por tener valores
# mucho más dispersos o concentrados que el resto, en este dataset.

# --- 4 ---
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(data=df, x="provincia_tramite", y="monto_asociado", estimator="mean", ax=ax)
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

promedio_manual = df.groupby("provincia_tramite")["monto_asociado"].mean().sort_values(ascending=False)
print(promedio_manual)
# Los valores coinciden exactamente con lo que muestra el gráfico de
# sns.barplot() — Santa Fe es la provincia con mayor monto promedio
# (~$18.939), Buenos Aires la de menor (~$15.390). Esto confirma que
# sns.barplot(), quí calcula el promedio internamente, hace lo mismo que
# un .groupby().mean() manual.

# --- 5 ---
df["fecha_nacimiento"] = pd.to_datetime(df["fecha_nacimiento"])
hoy = pd.Timestamp.today()
df["edad"] = (hoy - df["fecha_nacimiento"]).dt.days / 365.25

print(df["edad"].describe())
# count    1500.00
# mean       56.72
# min        18.19
# max        90.59
# El mínimo y máximo son razonables (entre 18 y 90 años, como corresponde
# a los datos originales de este dataset) — si vieras un mínimo negativo
# o un máximo de varios cientos de años, sería señal de un problema en la
# conversión de fecha_nacimiento (por ejemplo, años de 2 dígitos mal
# interpretados), algo que efectivamente pasó en una versión anterior de
# este mismo dataset y que se corrigió en el proceso de limpieza.

# --- 6 ---
fig, ax = plt.subplots()
sns.scatterplot(
    data=df.sample(200, random_state=1),
    x="edad", y="monto_asociado",
    hue="estado", ax=ax,
)
plt.show()

# --- 7 ---
fig, ax = plt.subplots(figsize=(6, 5))
sns.heatmap(df[["edad", "monto_asociado"]].corr(), annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
plt.show()

print(df[["edad", "monto_asociado"]].corr())
#                     edad  monto_asociado
# edad             1.000000       -0.011469
# monto_asociado  -0.011469        1.000000
# La correlación es prácticamente 0 (-0.01), lo que indica que NO hay
# relación entre la edad de la persona y el monto asociado a su trámite en
# este dataset — algo esperable, ya que no hay ningún motivo real por el
# que estas dos variables deberían estar relacionadas.
```

## Nota para el docente

En el punto 5, si alguien del grupo obtiene edades negativas o absurdamente altas, es una señal de que está trabajando con una versión del dataset generada antes de la corrección del problema de años de 2 dígitos (ver nota en `notas-docente.md`) — vale la pena tenerlo presente y sugerir regenerar los datasets desde `datasets/scripts-generacion/generar_datasets.py` si eso ocurre.
