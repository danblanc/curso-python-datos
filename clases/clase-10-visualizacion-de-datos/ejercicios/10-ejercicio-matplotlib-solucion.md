# Solución — Ejercicio 10.1 (Matplotlib)

```python
import pandas as pd
import matplotlib.pyplot as plt

# --- 1 ---
df = pd.read_csv("datasets/clean/tramites_personas_combinado.csv")
df["fecha_inicio"] = pd.to_datetime(df["fecha_inicio"])

# --- 2 ---
df["mes"] = df["fecha_inicio"].dt.to_period("M")
por_mes = df.groupby("mes").size()

fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(por_mes.index.astype(str), por_mes.values)
ax.set_title("Trámites iniciados por mes")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# --- 3 ---
conteo_estado = df["estado"].value_counts()

fig, ax = plt.subplots()
ax.bar(conteo_estado.index, conteo_estado.values)
ax.set_title("Cantidad de trámites por estado")
ax.set_xlabel("Estado")
ax.set_ylabel("Cantidad")
plt.tight_layout()
plt.show()

# --- 4 ---
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
axes[0].hist(df["monto_asociado"], bins=10)
axes[0].set_title("bins=10")
axes[1].hist(df["monto_asociado"], bins=30)
axes[1].set_title("bins=30")
plt.show()
# Con bins=10, la distribución se ve más "aplanada" y general. Con bins=30
# se nota más detalle (más "escalones"), aunque en este dataset en
# particular los montos están bastante uniformemente distribuidos, así que
# el cambio no es dramático. En datasets con distribuciones más marcadas
# (por ejemplo, con un pico concentrado), la cantidad de bins SÍ puede
# cambiar mucho la interpretación visual — vale la pena probar más de un
# valor siempre que algo se vea "sospechosamente uniforme" o "sospechosamente
# picudo".

# --- 5 ---
muestra = df.sample(200, random_state=1)

fig, ax = plt.subplots()
ax.scatter(muestra["monto_asociado"], muestra["id_tramite"])
ax.set_xlabel("Monto asociado")
ax.set_ylabel("ID de trámite")
plt.show()

# --- 6 ---
fig, ax = plt.subplots()
ax.bar(conteo_estado.index, conteo_estado.values, color="steelblue")
ax.set_title("Cantidad de trámites por estado")
ax.set_xlabel("Estado")
ax.set_ylabel("Cantidad")
plt.tight_layout()
plt.savefig("tramites_por_estado.png", dpi=150)
```

## Nota para el docente

En el punto 4, lo importante no es que noten un cambio dramático (en este dataset no lo hay, porque los montos están generados de forma bastante uniforme), sino que se acostumbren a **probar más de un valor de `bins`** como hábito — en datasets reales con distribuciones no uniformes, la cantidad de bins puede cambiar completamente la lectura de un histograma.
