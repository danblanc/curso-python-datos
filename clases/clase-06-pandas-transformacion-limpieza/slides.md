---
marp: true
theme: default
paginate: true
size: 16:9
---

# Clase 6
## Pandas: transformación y limpieza

Curso de Python para Análisis de Datos

---

# Agenda de hoy

1. Crear columnas nuevas
2. `.apply()` y funciones lambda
3. Tratamiento de valores nulos
4. Duplicados
5. Conversión de tipos
6. Ejercicio práctico

---

# Por qué esta clase importa especialmente

Los datos administrativos **casi nunca llegan limpios**: formatos inconsistentes, nulos, duplicados, tipos de datos incorrectos.

Esta clase (y las próximas dos) son el corazón práctico del curso: acá es donde más tiempo se invierte en un proyecto real de análisis de datos.

---

# Crear columnas nuevas

La forma más simple: operar directamente entre columnas existentes.

```python
df["nombre_completo"] = df["nombre"] + " " + df["apellido"]

df["edad_en_dias"] = df["edad"] * 365
```

Pandas aplica la operación a **todas las filas a la vez** (vectorizado, como vimos con NumPy).

---

# Columnas nuevas con condiciones

```python
df["mayor_edad"] = df["edad"] >= 18   # columna booleana

df["categoria_edad"] = df["edad"].apply(
    lambda edad: "Adulto mayor" if edad >= 65
    else "Adulto" if edad >= 18
    else "Menor"
)
```

Para lógica simple con una sola condición, `np.where` también es muy usado:

```python
import numpy as np
df["mayor_edad_texto"] = np.where(df["edad"] >= 18, "Sí", "No")
```

---

# `.apply()` con funciones propias

Cuando la lógica es más compleja que una expresión simple, conviene definir una función y aplicarla:

```python
def categorizar_edad(edad):
    if edad >= 65:
        return "Adulto mayor"
    elif edad >= 18:
        return "Adulto"
    else:
        return "Menor"

df["categoria_edad"] = df["edad"].apply(categorizar_edad)
```

`.apply()` ejecuta la función sobre **cada valor** de la columna, uno por uno.

---

# `.apply()` con funciones lambda

Una `lambda` es una función corta, sin nombre, escrita en una sola línea — útil para lógica simple que no amerita definir una función aparte:

```python
df["nombre_mayuscula"] = df["nombre"].apply(lambda x: x.upper())

df["monto_con_recargo"] = df["monto"].apply(lambda x: x * 1.1)
```

Regla práctica: si la lambda no entra cómoda en una línea, mejor usar una función `def` normal — prioridad a la legibilidad, como con las list comprehensions.

---

# `.apply()` sobre una fila completa

Con `axis=1`, `.apply()` puede operar sobre **filas enteras**, no solo columnas:

```python
def resumen_persona(fila):
    return f"{fila['nombre']} ({fila['provincia']})"

df["resumen"] = df.apply(resumen_persona, axis=1)
```

Útil cuando la lógica de una columna nueva depende de **varias columnas a la vez**.

---

# Valores nulos: primer paso, diagnosticar

Ya vimos esto en la clase anterior:

```python
df.isnull().sum()
```

Antes de decidir qué hacer con un nulo, siempre preguntarse: **¿por qué está vacío este dato?** ¿Nunca se cargó? ¿No aplica para ese registro? ¿Fue un error de carga?

---

# Eliminar filas/columnas con nulos: `.dropna()`

```python
df_sin_nulos = df.dropna()                       # elimina filas con CUALQUIER nulo
df_sin_nulos = df.dropna(subset=["email"])         # solo si "email" es nulo
df_sin_nulos = df.dropna(axis=1)                   # elimina columnas con nulos
```

**Cuidado:** `.dropna()` sin argumentos puede eliminar muchísimas filas si hay nulos dispersos en varias columnas. Revisar antes con `.isnull().sum()`.

---

# Imputar valores nulos: `.fillna()`

```python
df["telefono"] = df["telefono"].fillna("Sin dato")

df["monto"] = df["monto"].fillna(0)

df["provincia"] = df["provincia"].fillna(df["provincia"].mode()[0])  # el valor más frecuente
```

---

# ¿Eliminar o imputar?

| Situación | Conviene... |
|---|---|
| Pocos nulos, no crítico para el análisis | Eliminar la fila (`dropna`) |
| Columna casi toda nula | Eliminar la columna completa |
| El nulo tiene un significado real (ej. "no aplica") | Imputar con un valor explícito ("Sin dato", 0) |
| Se puede inferir razonablemente | Imputar con promedio/mediana/moda |

No hay una regla única — depende del contexto y de qué se va a hacer después con los datos.

---

# Detectar duplicados

```python
df.duplicated()                    # Series de True/False por fila
df.duplicated().sum()               # cantidad total de duplicados
df.duplicated(subset=["documento"])  # duplicado según una columna específica
```

Por defecto, considera duplicada una fila si **todas** sus columnas coinciden con otra fila anterior.

---

# Eliminar duplicados

```python
df_sin_duplicados = df.drop_duplicates()

df_sin_duplicados = df.drop_duplicates(subset=["documento"], keep="first")
```

`keep="first"` (por defecto) conserva la primera aparición; `keep="last"` conserva la última; `keep=False` elimina **todas** las apariciones del duplicado.

---

# El problema de los "duplicados no triviales"

```python
# Documento "30123456" vs "30.123.456" — ¿son o no son duplicados?
```

Pandas, por defecto, los trata como **diferentes** (son strings distintos). Para detectarlos como duplicados, primero hay que **normalizar el formato** — esto es exactamente lo que vamos a trabajar en la próxima clase (limpieza de texto), y es la antesala directa a técnicas de similitud de registros.

---

# Conversión de tipos: `.astype()`

```python
df["edad"] = df["edad"].astype(int)
df["documento"] = df["documento"].astype(str)
```

Falla si algún valor no se puede convertir (por ejemplo, texto no numérico a `int`).

---

# Conversión de tipos: `pd.to_numeric()`

Más flexible que `.astype()` para manejar errores de conversión:

```python
df["monto"] = pd.to_numeric(df["monto"], errors="coerce")
```

`errors="coerce"` convierte los valores problemáticos en `NaN` en vez de hacer fallar todo el proceso — muy útil con datos administrativos reales, donde siempre aparece algún valor inesperado.

---

# Flujo típico de limpieza

1. Explorar (`.info()`, `.isnull().sum()`)
2. Decidir qué hacer con nulos (eliminar o imputar)
3. Normalizar tipos de datos (`astype`, `to_numeric`)
4. Detectar y resolver duplicados
5. Crear columnas derivadas que faciliten el análisis

Este flujo se repite constantemente en proyectos reales — no es lineal, se va iterando.

---

# Resumen de la clase

- Columnas nuevas: operaciones directas, `.apply()`, `lambda`, `np.where`
- Nulos: diagnosticar primero, después decidir entre `.dropna()` y `.fillna()`
- Duplicados: `.duplicated()` y `.drop_duplicates()`, ojo con los "no triviales"
- Conversión de tipos: `.astype()` vs `pd.to_numeric(errors="coerce")`

---

# Ejercicio práctico

30-40 minutos — ver [`ejercicios/ejercicio-06.md`](./ejercicios/ejercicio-06.md)
