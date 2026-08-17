# Solución — Ejercicio 6 (Clase 6)

> Los valores numéricos corresponden al dataset generado con `SEED = 42`.

```python
import pandas as pd

df = pd.read_csv("datasets/raw/registros_personas.csv")

# --- Parte 1 ---
df["nombre_completo"] = df["nombre"] + " " + df["apellido"]
df["tiene_email"] = df["email"].notnull()

# --- Parte 2 ---
def formatear_provincia(valor):
    if pd.isnull(valor):
        return "Sin dato"
    return valor

df["provincia_formateada"] = df["provincia"].apply(formatear_provincia)

df["apellido_mayuscula"] = df["apellido"].apply(lambda x: x.upper())

# --- Parte 3 ---
nulos_telefono = df["telefono"].isnull().sum()
print("Nulos en telefono:", nulos_telefono)   # 85

df_telefono_completo = df.copy()
df_telefono_completo["telefono"] = df_telefono_completo["telefono"].fillna("No informado")

df_sin_nulos_provincia = df.dropna(subset=["provincia"])
print("Filas originales:", len(df))                       # 618
print("Filas sin nulos en provincia:", len(df_sin_nulos_provincia))  # 593

# --- Parte 4 ---
duplicados_exactos = df.duplicated().sum()
print("Duplicados exactos:", duplicados_exactos)   # 0

duplicados_por_documento = df.duplicated(subset=["documento"]).sum()
print("Duplicados por documento:", duplicados_por_documento)   # 18

# Los resultados son distintos porque, aunque hay filas que representan a la
# MISMA persona (mismo documento real), el formato en que está escrito el
# documento varía entre filas (por ejemplo "30123456" vs "30.123.456"), lo
# que hace que Pandas no las reconozca como duplicados exactos: son strings
# distintos, aunque representen el mismo número. El chequeo por "documento"
# también puede fallar en detectarlos si el formato varía ENTRE las dos
# filas duplicadas (por eso el número 18 puede no capturar el 100% de los
# casos reales) — este es justamente el problema que vamos a resolver
# normalizando el texto en la próxima clase.

# --- Parte 5 ---
print(df["documento"].dtype)   # object (texto), no numérico

documento_convertido = pd.to_numeric(df["documento"], errors="coerce")
nulos_generados = documento_convertido.isnull().sum()
print("Valores que quedaron como NaN:", nulos_generados)   # 480

# Pasa porque gran parte de los documentos tienen puntos, guiones o espacios
# (por ejemplo "30.123.456" o "30-123-456"), y pd.to_numeric no puede
# interpretar esos caracteres como parte de un número — por eso los
# convierte en NaN en vez de fallar todo el proceso. Antes de convertir a
# numérico, primero habría que "limpiar" el string (quitar puntos, guiones,
# espacios), algo que vemos en la Clase 7.
```

## Nota para el docente

El resultado de la Parte 5 (480 de 618 documentos se vuelven `NaN`) suele sorprender bastante — es un buen dato para remarcar en la corrección grupal, porque demuestra de forma contundente por qué la normalización de texto (próxima clase) no es un detalle menor, sino un paso obligatorio antes de poder trabajar numéricamente con estos datos.
