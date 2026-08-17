---
marp: true
theme: default
paginate: true
size: 16:9
---

# Clase 8
## Pandas: fechas y agregación

Curso de Python para Análisis de Datos

---

# Agenda de hoy

1. Fechas: conversión y componentes
2. Diferencias entre fechas
3. `.groupby()`: agrupar y agregar
4. `.agg()`: múltiples agregaciones
5. Tablas pivote
6. Ejercicio práctico

---

# El problema de las fechas como texto

En nuestro dataset de trámites, la columna `fecha_inicio` tiene valores como:

```
19/05/2025
08/12/25
2023-01-16
25/11/24
03-07-2025
```

Mientras sean texto, Pandas no puede ordenarlas cronológicamente ni calcular diferencias entre ellas correctamente.

---

# Convertir a fecha: `pd.to_datetime()`

```python
df["fecha_inicio"] = pd.to_datetime(df["fecha_inicio"], errors="coerce")
```

Con formatos mixtos como los nuestros, conviene ayudar a Pandas:

```python
df["fecha_inicio"] = pd.to_datetime(
    df["fecha_inicio"], format="mixed", dayfirst=True, errors="coerce"
)
```

`format="mixed"` le indica que infiera el formato fila por fila. `dayfirst=True` resuelve la ambigüedad día/mes (formato usado en Argentina/España).

---

# Verificando la conversión

```python
df["fecha_inicio"].dtype
# dtype('<M8[ns]')  -> tipo datetime de Pandas

df["fecha_inicio"].isnull().sum()
# cantidad de fechas que no se pudieron convertir (quedaron NaT)
```

`NaT` ("Not a Time") es el equivalente de `NaN` para fechas — vale la pena revisar cuántos casos genera antes de seguir.

---

# Componentes de una fecha: accesor `.dt`

Similar al accesor `.str` para texto, Pandas tiene `.dt` para fechas:

```python
df["anio"] = df["fecha_inicio"].dt.year
df["mes"] = df["fecha_inicio"].dt.month
df["dia"] = df["fecha_inicio"].dt.day
df["dia_semana"] = df["fecha_inicio"].dt.day_name()
```

---

# Diferencias entre fechas

```python
df["dias_resolucion"] = (df["fecha_resolucion"] - df["fecha_inicio"]).dt.days
```

El resultado de restar dos fechas es un `timedelta` (una duración). Con `.dt.days` lo convertimos a un número entero de días.

Útil, por ejemplo, para medir cuánto tardó en resolverse cada trámite.

---

# Filtrar por rango de fechas

```python
tramites_2024 = df[
    (df["fecha_inicio"] >= "2024-01-01") &
    (df["fecha_inicio"] < "2025-01-01")
]
```

Pandas puede comparar fechas directamente contra strings con formato `YYYY-MM-DD`, sin necesidad de convertirlos primero.

---

# `.groupby()`: la idea central

"Agrupar por" una columna, y aplicar una función sobre cada grupo:

```python
df.groupby("tipo_tramite")["monto_asociado"].sum()
```

Esto responde: **"¿Cuál es el monto total asociado, para cada tipo de trámite?"**

Es el equivalente en Pandas a una tabla dinámica de Excel.

---

# `.groupby()` con distintas agregaciones

```python
df.groupby("estado")["monto_asociado"].mean()    # promedio por estado
df.groupby("provincia").size()                    # cantidad de filas por provincia
df.groupby("tipo_tramite")["id_tramite"].count()   # cantidad de trámites por tipo
```

`.size()` cuenta filas (incluye nulos). `.count()` sobre una columna específica cuenta solo los valores no nulos de esa columna.

---

# `.agg()`: múltiples agregaciones a la vez

```python
df.groupby("tipo_tramite")["monto_asociado"].agg(["sum", "mean", "count"])
```

```
                          sum       mean  count
tipo_tramite
Alta de comercio      541230.5   9843.3    55
Baja de comercio      398120.0   8765.2    45
...
```

---

# `.agg()` con nombres de columna personalizados

```python
df.groupby("tipo_tramite").agg(
    monto_total=("monto_asociado", "sum"),
    monto_promedio=("monto_asociado", "mean"),
    cantidad=("id_tramite", "count"),
)
```

Esta sintaxis (agregación con nombre) es la más clara para reportes, porque las columnas resultantes ya quedan bien nombradas.

---

# Agrupar por más de una columna

```python
df.groupby(["provincia", "estado"])["monto_asociado"].sum()
```

Agrupa primero por provincia, y dentro de cada provincia, por estado. El resultado tiene un índice de dos niveles (jerárquico).

Para volver a un DataFrame "plano": agregar `.reset_index()` al final.

---

# Tablas pivote: `pd.pivot_table()`

```python
pd.pivot_table(
    df,
    values="monto_asociado",
    index="provincia",
    columns="estado",
    aggfunc="sum",
    fill_value=0,
)
```

Convierte los valores de una columna (`estado`) en **columnas nuevas**, cruzando con otra dimensión (`provincia`) — igual que una tabla dinámica de Excel.

---

# `.groupby()` vs `pivot_table()`

| | `.groupby()` | `pivot_table()` |
|---|---|---|
| Resultado | Índice jerárquico o Series | Formato de tabla cruzada |
| Uso típico | Cálculos y análisis posteriores | Reportes y visualización rápida |

En la práctica, muchas veces se puede llegar al mismo resultado con ambos — es cuestión de qué formato final se necesita.

---

# Resumen de la clase

- `pd.to_datetime(format="mixed", dayfirst=True)` para fechas con formato inconsistente
- `.dt` para extraer componentes, restar fechas da un `timedelta`
- `.groupby()` + `.agg()` para agregaciones flexibles
- `pivot_table()` para tablas cruzadas tipo Excel

---

# Ejercicio práctico

30-40 minutos — ver [`ejercicios/ejercicio-08.md`](./ejercicios/ejercicio-08.md)

Vamos a trabajar con `datasets/raw/registros_tramites.xlsx`.
