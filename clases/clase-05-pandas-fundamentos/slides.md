---
marp: true
theme: default
paginate: true
size: 16:9
---

# Clase 5
## Pandas: fundamentos

Curso de Python para Análisis de Datos

---

# Agenda de hoy

1. Qué es Pandas y por qué lo usamos
2. Series y DataFrame
3. Lectura de datos desde distintas fuentes
4. Exploración inicial de un dataset
5. Selección y filtrado
6. Ejercicio práctico

---

# ¿Qué es Pandas?

**Pandas** es la librería estándar de Python para manipulación y análisis de datos tabulares (tipo planilla/tabla).

Está construida sobre NumPy, y agrega:
- Estructuras con **etiquetas** (nombres de columnas, índices)
- Herramientas para leer/escribir múltiples formatos de archivo
- Funciones para limpiar, transformar, agregar y combinar datos

```python
import pandas as pd
```

---

# De listas de diccionarios a DataFrame

Recordemos esto de clases anteriores:

```python
personas = [
    {"nombre": "Ana", "edad": 34},
    {"nombre": "Luis", "edad": 17},
]
```

Un **DataFrame** es, conceptualmente, esto mismo — pero optimizado, con herramientas propias, y pensado para trabajar con muchísimos registros de forma eficiente.

```python
df = pd.DataFrame(personas)
```

---

# Series: la estructura unidimensional

Una **Series** es como una columna: una secuencia de valores, con un índice.

```python
edades = pd.Series([34, 17, 45], name="edad")
```

```
0    34
1    17
2    45
Name: edad, dtype: int64
```

Cada columna de un DataFrame es, internamente, una Series.

---

# DataFrame: la estructura tabular

```python
import pandas as pd

datos = {
    "nombre": ["Ana", "Luis", "Marta"],
    "edad": [34, 17, 45],
    "provincia": ["Córdoba", "Mendoza", "Santa Fe"],
}

df = pd.DataFrame(datos)
print(df)
```

```
   nombre  edad provincia
0     Ana    34   Córdoba
1    Luis    17  Mendoza
2   Marta    45  Santa Fe
```

---

# Leer un CSV

```python
df = pd.read_csv("datasets/raw/registros_personas.csv")
```

Parámetros útiles frecuentes:

```python
pd.read_csv("archivo.csv", sep=";")           # separador distinto de coma
pd.read_csv("archivo.csv", encoding="utf-8")  # codificación de caracteres
pd.read_csv("archivo.csv", dtype={"documento": str})  # forzar un tipo de columna
```

---

# Leer otros formatos

```python
# Excel (requiere el paquete openpyxl instalado)
df_excel = pd.read_excel("datos.xlsx", sheet_name="Hoja1")

# JSON
df_json = pd.read_json("datos.json")

# Desde una base de datos SQL (requiere una conexión, ej. con sqlalchemy)
df_sql = pd.read_sql("SELECT * FROM tramites", con=conexion)
```

Todos devuelven el mismo tipo de objeto: un **DataFrame**. Una vez que los datos están adentro, el resto del trabajo es igual sin importar de dónde vinieron.

---

# Primera mirada a los datos

```python
df.head()       # primeras 5 filas (podés pasar un número: head(10))
df.tail(3)       # últimas 3 filas
df.shape         # (cantidad de filas, cantidad de columnas)
df.columns       # nombres de las columnas
```

Siempre es el primer paso al recibir un dataset nuevo: **mirar antes de tocar**.

---

# `.info()`: radiografía del dataset

```python
df.info()
```

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 618 entries, 0 to 617
Data columns (total 9 columns):
 #   Column             Non-Null Count  Dtype
---  ------             --------------  -----
 0   id_persona          618 non-null    int64
 1   documento           618 non-null    object
 2   email                569 non-null    object
 ...
```

Muestra: tipo de dato por columna, y cuántos valores **no nulos** hay — clave para detectar nulos de un vistazo.

---

# `.describe()`: estadística rápida

```python
df.describe()
```

Para columnas numéricas: cuenta, promedio, desvío estándar, mínimo, máximo, cuartiles.

```python
df.describe(include="object")   # equivalente para columnas de texto
```

Un primer pantallazo estadístico sin escribir ninguna cuenta manual.

---

# Detectar valores nulos

```python
df.isnull()              # DataFrame de True/False
df.isnull().sum()         # cantidad de nulos por columna
df.isnull().sum().sum()    # total de nulos en todo el dataset
```

Este es siempre uno de los primeros chequeos al recibir datos reales — especialmente en registros administrativos, donde los nulos son la norma, no la excepción.

---

# Seleccionar columnas

```python
df["nombre"]                    # una columna (devuelve una Series)
df[["nombre", "apellido"]]       # varias columnas (devuelve un DataFrame)
```

Ojo con los corchetes dobles: `df[["nombre"]]` (con doble corchete) devuelve un DataFrame de una sola columna, no una Series.

---

# Filtrar filas con condiciones

```python
mayores = df[df["edad"] >= 18]

cordoba_mayores = df[(df["provincia"] == "Córdoba") & (df["edad"] >= 18)]
```

**Importante:** con Pandas, para combinar condiciones se usa `&` (y) y `|` (o) — no `and`/`or` como en Python puro — y cada condición va entre paréntesis.

---

# `loc` vs `iloc`

```python
df.loc[0]              # fila con índice/etiqueta 0
df.loc[0, "nombre"]      # valor en fila 0, columna "nombre"
df.loc[0:3, ["nombre", "edad"]]   # filas 0 a 3 (inclusive), columnas elegidas

df.iloc[0]              # fila en la posición 0 (por posición, no por etiqueta)
df.iloc[0:3, 0:2]         # filas y columnas por posición numérica
```

`loc` = por **etiqueta** (nombre de índice/columna). `iloc` = por **posición** (como en una lista).

---

# ¿Por qué importa la diferencia?

Si el índice del DataFrame no es 0, 1, 2... (por ejemplo, después de filtrar), `loc` y `iloc` pueden dar resultados distintos para "el mismo número":

```python
filtrado = df[df["edad"] >= 18]   # el índice original se mantiene, con "huecos"

filtrado.iloc[0]    # SIEMPRE la primera fila del resultado filtrado
filtrado.loc[0]      # busca la fila con ETIQUETA 0, puede no ser la primera
                      # (o directamente no existir, si se filtró)
```

---

# Resumen de la clase

- Pandas: Series (1D) y DataFrame (2D), construidos sobre NumPy
- `read_csv`, `read_excel`, `read_json`, `read_sql` — misma lógica, distinto origen
- `.head()`, `.info()`, `.describe()`, `.isnull()` — exploración inicial
- Selección de columnas, filtrado con `&`/`|`, `loc` vs `iloc`

---

# Ejercicio práctico

30-40 minutos — ver [`ejercicios/ejercicio-05.md`](./ejercicios/ejercicio-05.md)

Vamos a trabajar con el dataset real de personas del curso: `datasets/raw/registros_personas.csv`.
