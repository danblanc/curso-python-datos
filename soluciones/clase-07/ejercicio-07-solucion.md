# Solución — Ejercicio 7 (Clase 7)

```python
import re
import unicodedata

import pandas as pd

# --- Parte 1 ---
df = pd.read_csv("datasets/raw/registros_personas.csv")

df["nombre_normalizado"] = df["nombre"].str.strip().str.title()
df["apellido_normalizado"] = df["apellido"].str.strip().str.title()

print(df[["nombre", "nombre_normalizado", "apellido", "apellido_normalizado"]].head())
# Nota: .title() capitaliza cada palabra, lo cual funciona bien para nombres
# compuestos ("Mateo Benjamin" -> "Mateo Benjamin"), pero puede fallar con
# apellidos con partículas ("de la cruz" -> "De La Cruz", cuando tal vez se
# prefiera "de la Cruz"). No hay una solución automática perfecta para esto;
# depende del criterio que se defina.

# --- Parte 2 ---
df["direccion_normalizada"] = df["direccion"].str.replace(r"\s+", " ", regex=True).str.strip()

# --- Parte 3 ---
def normalizar_documento(doc):
    if pd.isnull(doc):
        return None
    return re.sub(r"[^\d]", "", str(doc))

df["documento_normalizado"] = df["documento"].apply(normalizar_documento)
df["documento_normalizado"] = pd.to_numeric(df["documento_normalizado"], errors="coerce")

nulos_generados = df["documento_normalizado"].isnull().sum()
print("Valores NaN después de normalizar:", nulos_generados)
# -> 0 (comparar con los 480 NaN que se generaban en el Ejercicio 6 al
# convertir la columna SIN normalizar primero)

# --- Parte 4 ---
ejemplo = pd.DataFrame({
    "documento": ["30123456", "30.123.456"],
    "nombre": ["Ana Gomez", "ANA GOMEZ"],
})

print("Duplicados SIN normalizar:", ejemplo.duplicated(subset=["documento"]).sum())
# -> 0

ejemplo["documento_normalizado"] = ejemplo["documento"].apply(normalizar_documento)
print("Duplicados DESPUÉS de normalizar:", ejemplo.duplicated(subset=["documento_normalizado"]).sum())
# -> 1

# La diferencia ocurre porque, antes de normalizar, Pandas compara los
# strings "30123456" y "30.123.456" tal cual están escritos, y para Python
# son dos textos distintos (uno tiene puntos, el otro no) aunque representen
# el mismo número de documento. Recién después de quitar todo lo que no sea
# un dígito, ambos quedan representados exactamente igual ("30123456"), y
# Pandas los reconoce correctamente como el mismo valor.

# --- Parte 5 (opcional) ---
def quitar_tildes(texto):
    if pd.isnull(texto):
        return None
    nfkd = unicodedata.normalize("NFKD", texto)
    return "".join(c for c in nfkd if not unicodedata.combining(c))

df["provincia_sin_tildes"] = df["provincia"].apply(quitar_tildes)
print(df[["provincia", "provincia_sin_tildes"]].dropna().head())
```

## Nota para el docente

El resultado de la Parte 3 (0 valores `NaN` después de normalizar, contra 480 en el Ejercicio 6 sin normalizar) es el dato más contundente de todo el bloque de limpieza — vale la pena escribirlo explícitamente en el pizarrón o remarcarlo en la corrección grupal, ya que conecta directamente ambos ejercicios y deja muy clara la necesidad de este paso.

Sobre la Parte 4: el dataset real del curso (`registros_personas.csv`) **no** contiene casos donde el mismo documento aparezca con formato distinto entre las filas duplicadas — por eso se usa un ejemplo controlado de dos filas para demostrar el efecto de forma garantizada. Si alguien pregunta por qué no se ve este efecto directamente en el dataset grande, es una buena oportunidad para aclarar que los duplicados "sucios" del dataset son de otro tipo (incluidos a propósito para otros fines), y que en datos reales este tipo de inconsistencia de formato entre duplicados es sumamente común, aunque no esté representada en este dataset sintético puntual.
