# Solución de referencia — Prueba de nivelación

> Los valores numéricos corresponden al dataset `solicitudes_beneficios.csv` generado con semilla fija (`SEED = 77`). Si por algún motivo tu archivo es distinto, los números pueden no coincidir exactamente — lo importante es que el **método** sea correcto.

---

## Bloque 1 — Fundamentos de Python

```python
import re

# --- 1 ---
def es_documento_valido(doc):
    limpio = re.sub(r"[^\d]", "", str(doc))
    return len(limpio) == 7 and limpio.isdigit()

print(es_documento_valido("4.259.420"))   # True
print(es_documento_valido("1-864-493"))   # True
print(es_documento_valido("3120040"))     # True
print(es_documento_valido("12345"))       # False (5 dígitos, no 7)

# --- 2 ---
def categorizar_ingreso(ingreso):
    if ingreso is None:
        return "Sin dato"
    if ingreso < 30000:
        return "Bajo"
    elif ingreso <= 60000:
        return "Medio"
    else:
        return "Alto"

print(categorizar_ingreso(None))    # Sin dato
print(categorizar_ingreso(25000))   # Bajo
print(categorizar_ingreso(45000))   # Medio
print(categorizar_ingreso(75000))   # Alto

# --- 3 ---
solicitudes = [
    {"documento": "4.259.420", "estado": "Aprobada", "ingreso": 45000},
    {"documento": "1864493", "estado": "Rechazada", "ingreso": None},
    {"documento": "4-088-417", "estado": "Aprobada", "ingreso": 72000},
    {"documento": "3120040", "estado": "Pendiente", "ingreso": 28000},
    {"documento": "1411008", "estado": "Aprobada", "ingreso": 59000},
]

for s in solicitudes:
    valido = "válido" if es_documento_valido(s["documento"]) else "inválido"
    categoria = categorizar_ingreso(s["ingreso"])
    print(f'Documento {s["documento"]} ({valido}) - Estado: {s["estado"]} - Ingreso: {categoria}')

# Salida esperada:
# Documento 4.259.420 (válido) - Estado: Aprobada - Ingreso: Medio
# Documento 1864493 (válido) - Estado: Rechazada - Ingreso: Sin dato
# Documento 4-088-417 (válido) - Estado: Aprobada - Ingreso: Alto
# Documento 3120040 (válido) - Estado: Pendiente - Ingreso: Bajo
# Documento 1411008 (válido) - Estado: Aprobada - Ingreso: Medio

# --- 4 ---
aprobados = [s["documento"] for s in solicitudes if s["estado"] == "Aprobada"]
print(aprobados)
# ['4.259.420', '4-088-417', '1411008']

# --- 5 ---
def dividir_seguro(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "No se puede dividir por cero"

print(dividir_seguro(10, 2))   # 5.0
print(dividir_seguro(10, 0))   # No se puede dividir por cero
```

---

## Bloque 2 — Archivos y NumPy

```python
import csv
import numpy as np

# --- 6 ---
with open("solicitudes_beneficios.csv", "r", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    filas = list(lector)

print(len(filas))   # 364

# --- 7 ---
ingresos = np.array([45000, np.nan, 72000, 28000, 59000])

promedio = np.nanmean(ingresos)
print(promedio)   # 51000.0
# (np.mean() a secas hubiera devuelto NaN, porque cualquier operación
# aritmética con un NaN de por medio da NaN — por eso se necesita nanmean)

mayores_a_50000 = (ingresos > 50000).sum()
print(mayores_a_50000)   # 2
```

---

## Bloque 3 — Pandas: carga y exploración

```python
import pandas as pd

# --- 8-9 ---
df = pd.read_csv("solicitudes_beneficios.csv")
print(df.shape)   # (364, 11)

# --- 10-11 ---
df.info()
nulos = df.isnull().sum()
print(nulos)
# fecha_resolucion    187
# ingreso_mensual      95
# departamento         17
# cantidad_hijos       39
# (el resto, 0)
#
# 4 columnas tienen al menos un nulo: fecha_resolucion, ingreso_mensual,
# departamento, cantidad_hijos.

# --- 12 ---
aprobadas_altas = df[(df["estado"] == "Aprobada") & (df["ingreso_mensual"] > 50000)]
print(len(aprobadas_altas))   # 33

# --- 13 ---
print(df.loc[0:4, ["nombre", "apellido", "estado"]])
```

---

## Bloque 4 — Pandas: limpieza y transformación

```python
import re

# --- 14 ---
df["nombre_completo"] = df["nombre"] + " " + df["apellido"]

# --- 15 ---
df["tipo_beneficio_normalizado"] = df["tipo_beneficio"].str.strip().str.lower()

print(df["tipo_beneficio"].nunique())               # 20
print(df["tipo_beneficio_normalizado"].nunique())    # 5
# Hay solo 5 categorías reales de beneficio. Las 20 "variantes" que aparecen
# sin normalizar son la misma información escrita con mayúsculas, minúsculas
# y capitalización inconsistente — el mismo problema que vimos con
# tipo_tramite en la Clase 8.

# --- 16 ---
def normalizar_documento(doc):
    return re.sub(r"[^\d]", "", str(doc))

df["documento_normalizado"] = df["documento"].apply(normalizar_documento)
df["documento_normalizado"] = pd.to_numeric(df["documento_normalizado"], errors="coerce")

# --- 17 ---
dup_crudo = df.duplicated(subset=["documento"]).sum()
dup_normalizado = df.duplicated(subset=["documento_normalizado"]).sum()

print(dup_crudo)         # 14
print(dup_normalizado)    # 14

# En este dataset en particular, el número NO cambia: los duplicados
# intencionales que se generaron conservan el mismo formato de documento
# que su fila original (por ejemplo, si el original tenía puntos, el
# duplicado también los tiene). Por eso Pandas ya los detecta como
# duplicados incluso sin normalizar.
#
# El número SÍ cambiaría (aumentaría después de normalizar) en un escenario
# donde dos filas representan a la MISMA persona pero el documento está
# escrito con distinto formato entre sí (por ejemplo, una fila con
# "1864493" y otra con "1.864.493") — en ese caso, sin normalizar, Pandas
# los trataría como valores distintos y no los detectaría como duplicados.

# --- 18 ---
df_sin_duplicados = df.drop_duplicates(subset=["documento_normalizado"], keep="first")
print(len(df_sin_duplicados))   # 350 (364 - 14)

# --- 19 ---
promedio_ingreso = df["ingreso_mensual"].mean()
df["ingreso_mensual_completo"] = df["ingreso_mensual"].fillna(promedio_ingreso)
print(round(promedio_ingreso, 2))   # ~51340.03

# --- 20 ---
df["fecha_solicitud"] = pd.to_datetime(
    df["fecha_solicitud"], format="mixed", dayfirst=True, errors="coerce"
)
df["fecha_resolucion"] = pd.to_datetime(
    df["fecha_resolucion"], format="mixed", dayfirst=True, errors="coerce"
)

print(df["fecha_resolucion"].isnull().sum())   # 187

print(df["estado"].value_counts())
# Pendiente        99
# Rechazada        91
# En evaluación    88
# Aprobada         86
#
# 99 (Pendiente) + 88 (En evaluación) = 187 -> coincide exactamente con los
# nulos de fecha_resolucion: son las solicitudes que todavía no se
# resolvieron, por eso no tienen fecha de resolución. Es información
# correcta, no un error de carga.

# --- 21 ---
df["dias_para_resolucion"] = (df["fecha_resolucion"] - df["fecha_solicitud"]).dt.days
print(df["dias_para_resolucion"].describe())
# El valor mínimo da negativo (por ejemplo, -273), lo cual no tiene sentido
# lógico: una solicitud no puede resolverse antes de haberse solicitado.
# Esto ocurre por la misma razón que vimos en la Clase 8: con fechas de
# formato mixto y dayfirst=True, algunas fechas ambiguas (día y mes ambos
# menores a 12) pueden interpretarse de forma incorrecta en la conversión.
# Es una buena práctica SIEMPRE revisar con .describe() los resultados de
# una conversión de fechas, en vez de asumir que salió perfecta.
```

---

## Bloque 5 — Pandas: agregación y combinación

```python
# --- 22 ---
resumen = df.groupby("tipo_beneficio_normalizado").agg(
    ingreso_promedio=("ingreso_mensual_completo", "mean"),
    cantidad=("id_solicitud", "count"),
)
print(resumen)
#                              ingreso_promedio  cantidad
# tipo_beneficio_normalizado
# asignación familiar              ~53952.92        74
# ayuda habitacional               ~53532.05        63
# beca estudiantil                 ~43861.67        74
# pensión por invalidez            ~55499.68        79
# subsidio por desempleo           ~49898.60        74

# --- 23 ---
pivot = pd.pivot_table(
    df,
    values="id_solicitud",
    index="departamento",
    columns="estado",
    aggfunc="count",
    fill_value=0,
)
print(pivot)

# --- 24 ---
info_departamentos = pd.DataFrame({
    "departamento": ["Montevideo", "Canelones", "Maldonado", "Salto", "Paysandú", "Rivera", "Colonia", "Rocha"],
    "region": ["Sur", "Sur", "Este", "Norte", "Litoral", "Norte", "Litoral", "Este"],
})

combinado = pd.merge(df, info_departamentos, on="departamento", how="left")
print(len(combinado))   # 364 (igual al original)
print(combinado["region"].isnull().sum())   # 17 (las mismas filas que ya tenían departamento nulo)

# Corresponde usar how="left", porque queremos conservar TODAS las
# solicitudes del dataset principal (df), tengan o no un departamento
# válido para cruzar con info_departamentos. Con "inner" hubiéramos perdido
# las 17 filas con departamento nulo (porque no encuentran coincidencia);
# con "right" hubiéramos priorizado la tabla de departamentos, lo cual no
# tiene sentido acá porque esa tabla es solo información complementaria.

# --- 25 ---
aprobadas_por_region = combinado[combinado["estado"] == "Aprobada"].groupby("region")["id_solicitud"].count()
print(aprobadas_por_region)
# region
# Este       18
# Litoral    23
# Norte      20
# Sur        23
```

---

## Bloque 6 — Reflexión

No tiene una respuesta "correcta" — es una autoevaluación personal. Si te costó especialmente el Bloque 4 (limpieza de texto/duplicados) o el Bloque 5 (agregación/merge), vale la pena repasar las Clases 6 a 9 antes de seguir avanzando, ya que son la base directa de todo lo que viene después (visualización y dashboards).

## Nota general sobre esta prueba

Los puntos 17, 20 y 21 están diseñados a propósito para que **no salga "perfecto" a la primera** — son los mismos tipos de sorpresas (ambigüedad de fechas, formato inconsistente en texto) que aparecen en cualquier trabajo real con registros administrativos. Si te encontraste con el valor negativo en `dias_para_resolucion` y te generó dudas en vez de ignorarlo, esa reacción es exactamente la que buscamos reforzar durante todo el curso.
