# Solución — Ejercicio 8 (Clase 8)

> Valores correspondientes al dataset generado con `SEED = 42`.

```python
import pandas as pd

# --- Parte 1 ---
df = pd.read_excel("datasets/raw/registros_tramites.xlsx")

df["fecha_inicio"] = pd.to_datetime(
    df["fecha_inicio"], format="mixed", dayfirst=True, errors="coerce"
)
df["fecha_resolucion"] = pd.to_datetime(
    df["fecha_resolucion"], format="mixed", dayfirst=True, errors="coerce"
)

print("Nulos en fecha_inicio:", df["fecha_inicio"].isnull().sum())        # 0
print("Nulos en fecha_resolucion:", df["fecha_resolucion"].isnull().sum())  # 603

print(df["estado"].value_counts())
# "En revisión" (302) + "Iniciado" (301) = 603 -> coincide exactamente con
# los nulos de fecha_resolucion: son los trámites que todavía no se
# resolvieron, por lo que no tienen fecha de resolución. No es un error de
# datos, es información correcta (el trámite sigue en curso).

# --- Parte 2 ---
df["anio_inicio"] = df["fecha_inicio"].dt.year
print(df.groupby("anio_inicio").size())

df["dias_resolucion"] = (df["fecha_resolucion"] - df["fecha_inicio"]).dt.days
print(df["dias_resolucion"].describe())
# El mínimo da negativo (por ejemplo, -200), lo cual no tiene sentido: un
# trámite no puede resolverse antes de iniciarse.

negativos = df[df["dias_resolucion"] < 0]
print(negativos[["fecha_inicio", "fecha_resolucion", "dias_resolucion"]].head())
# Esto ocurre por ambigüedad al interpretar fechas con formato mixto: cuando
# el día es menor o igual a 12, una fecha como "03/07/2025" puede
# interpretarse como 3 de julio (dayfirst=True) o como 7 de marzo, y con
# formatos mezclados en la misma columna, la conversión automática no
# siempre acierta con el criterio correcto en todos los casos. Es una buena
# lección: SIEMPRE conviene revisar los resultados de una conversión de
# fechas con .describe() o valores extremos, en vez de asumir que salió bien.

# --- Parte 3 ---
suma_sin_normalizar = df.groupby("tipo_tramite")["monto_asociado"].sum()
print(suma_sin_normalizar)

print("Tipos únicos (sin normalizar):", df["tipo_tramite"].nunique())   # 32

df["tipo_tramite_normalizado"] = df["tipo_tramite"].str.lower().str.strip()
print("Tipos únicos (normalizado):", df["tipo_tramite_normalizado"].nunique())  # 8

suma_normalizada = df.groupby("tipo_tramite_normalizado")["monto_asociado"].sum()
print(suma_normalizada)
# Sin normalizar, Pandas trata "Alta de comercio", "ALTA DE COMERCIO" y
# "alta de comercio" como 3 categorías DISTINTAS (32 grupos en total en vez
# de los 8 tipos reales), lo que hace que la suma de cada tipo real quede
# repartida entre varias filas del resultado, en vez de consolidada en una
# sola. Es el mismo problema de fondo que vimos con los documentos en la
# Clase 7, aplicado ahora a una columna categórica.

# --- Parte 4 ---
resumen = df.groupby("tipo_tramite_normalizado").agg(
    monto_total=("monto_asociado", "sum"),
    monto_promedio=("monto_asociado", "mean"),
    cantidad=("id_tramite", "count"),
)
print(resumen)

pivot = pd.pivot_table(
    df,
    values="monto_asociado",
    index="provincia",
    columns="estado",
    aggfunc="sum",
    fill_value=0,
)
print(pivot)
```

## Nota para el docente

Los dos "descubrimientos" de este ejercicio (fechas negativas por ambigüedad, y 32 vs. 8 tipos de trámite por falta de normalización) son intencionales y muy valiosos — conectan directamente con la Clase 7 y refuerzan que **la limpieza de datos no es un paso único al principio, es algo que hay que seguir vigilando en cada análisis posterior**. Vale la pena remarcarlo explícitamente en la corrección grupal: ambos casos son ejemplos reales de por qué siempre hay que revisar resultados con sentido crítico, no solo ejecutar código y asumir que está bien.
