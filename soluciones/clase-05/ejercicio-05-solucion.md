# Solución — Ejercicio 5 (Clase 5)

> Los valores mostrados corresponden al dataset generado con la semilla fija del curso (`SEED = 42`). Si regeneraste los datasets, los números deberían coincidir; si no coinciden exactamente, no es un error — depende de la versión del dataset con la que se trabaje.

```python
import pandas as pd

# --- Parte 1 ---
df = pd.read_csv("datasets/raw/registros_personas.csv")

print(df.head())
print(df.shape)
print(f"El dataset tiene {df.shape[0]} filas y {df.shape[1]} columnas.")

df.info()
# Columnas con nulos: email, telefono, provincia
# (documento, nombre, apellido, fecha_nacimiento y direccion no tienen nulos)

# --- Parte 2 ---
print(df.describe())
print(df.describe(include="object"))
# .describe() (numérico) solo describe id_persona, que no aporta demasiado
# (es un identificador, no una medida). .describe(include="object") en cambio
# muestra, para las columnas de texto: cantidad de valores no nulos, cantidad
# de valores únicos, el valor más frecuente y su frecuencia — más relevante
# para este dataset en particular.

# --- Parte 3 ---
nulos_por_columna = df.isnull().sum()
print(nulos_por_columna)

columna_mas_nulos = nulos_por_columna.idxmax()
print("Columna con más nulos:", columna_mas_nulos)
# -> "telefono", con 85 valores nulos

# --- Parte 4 ---
seleccion = df[["nombre", "apellido", "provincia"]]
print(seleccion.head())

cordoba = df[df["provincia"] == "Córdoba"]
print("Personas de Córdoba:", len(cordoba))
# -> 69

cordoba_con_email = df[(df["provincia"] == "Córdoba") & (df["email"].notnull())]
print("Personas de Córdoba con email:", len(cordoba_con_email))
# -> 63

# --- Parte 5 ---
print(df.iloc[0:3, :][["nombre", "documento"]])
# forma alternativa más directa:
print(df.iloc[0:3][["nombre", "documento"]])

print(df.loc[0, "nombre"])
```

## Nota para el docente

Si alguien regeneró los datasets con un `SEED` distinto o modificó el script generador, los números de la Parte 3 y 4 (85 nulos en teléfono, 69 personas de Córdoba, etc.) van a diferir — no es un error del ejercicio, sino una consecuencia de trabajar con datos generados. Vale la pena aclararlo antes de que alguien piense que hizo algo mal por no obtener los mismos números exactos.
