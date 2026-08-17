---
marp: true
theme: default
paginate: true
size: 16:9
---

# Clase 9
## Pandas: combinación de datos y repaso

Curso de Python para Análisis de Datos

---

# Agenda de hoy

1. `pd.merge()` y tipos de join
2. Verificación post-merge
3. `pd.concat()`
4. Repaso integrador (caso práctico)

---

# El escenario

Tenemos tres fuentes de datos separadas:

- `registros_personas.csv` — quiénes son las personas
- `registros_tramites.xlsx` — qué trámites hizo cada una
- `registros_direcciones.json` — dónde vive cada una

Para analizarlos juntos, necesitamos **combinarlos** por una columna en común (el documento).

---

# `pd.merge()`: sintaxis básica

```python
resultado = pd.merge(
    df_tramites,
    df_personas,
    left_on="documento_solicitante",
    right_on="documento",
    how="left",
)
```

- `left_on` / `right_on`: columnas clave de cada DataFrame (si tienen el mismo nombre, alcanza con `on="documento"`)
- `how`: tipo de unión

---

# Tipos de join: la idea visual

Pensemos en dos conjuntos: **A** (trámites) y **B** (personas).

- `inner`: solo lo que está en **A y B a la vez**
- `left`: todo **A**, complementado con B donde haya coincidencia (si no hay, queda `NaN`)
- `right`: todo **B**, complementado con A donde haya coincidencia
- `outer`: todo lo de **A y B**, coincida o no

---

# `inner`: solo las coincidencias

```python
pd.merge(df_tramites, df_personas, left_on="documento_solicitante",
         right_on="documento", how="inner")
```

Se quedan **solo** los trámites cuyo documento existe en la tabla de personas. Si un trámite tiene un documento que no está en `personas`, esa fila **desaparece** del resultado.

---

# `left`: todo lo de la izquierda

```python
pd.merge(df_tramites, df_personas, left_on="documento_solicitante",
         right_on="documento", how="left")
```

Se conservan **todos** los trámites, tengan o no coincidencia en `personas`. Donde no hay coincidencia, las columnas de `personas` quedan en `NaN`.

Es el join más usado cuando queremos "enriquecer" una tabla principal sin perder ninguna fila de ella.

---

# `right` y `outer`

```python
how="right"   # todos los de personas, complementado con trámites si hay
how="outer"   # todo de ambos lados, coincida o no
```

`outer` es útil justamente para **detectar** registros sin correspondencia en ninguno de los dos lados — por ejemplo, personas sin ningún trámite, o trámites con un documento que no existe en la tabla de personas.

---

# Elegir el `how` correcto

| Pregunta que quiero responder | `how` recomendado |
|---|---|
| Solo lo que tiene información completa en ambos lados | `inner` |
| Todos los trámites, aunque falte info de la persona | `left` |
| Todas las personas, aunque no tengan trámites | `right` (o invertir el orden y usar `left`) |
| Quiero ver TODO, incluyendo lo que no cruza | `outer` |

---

# Verificar el resultado de un merge

```python
resultado = pd.merge(
    df_tramites, df_personas,
    left_on="documento_solicitante", right_on="documento",
    how="left", indicator=True,
)

resultado["_merge"].value_counts()
```

`indicator=True` agrega una columna `_merge` que indica si cada fila vino de `"left_only"`, `"right_only"` o `"both"` — clave para auditar que el cruce salió como esperábamos.

---

# El riesgo de duplicar filas en un merge

Si la columna clave tiene valores repetidos de un lado, el merge puede **multiplicar filas** inesperadamente:

```python
# Si df_personas tiene 2 filas con el mismo documento (duplicado),
# cada trámite de esa persona va a aparecer DUPLICADO en el resultado.
```

Por eso, antes de un merge, conviene verificar duplicados en la columna clave del lado que "no debería" tenerlos (`.duplicated().sum()`).

---

# `pd.concat()`: apilar DataFrames

A diferencia de `merge` (que combina por columnas en común), `concat` **apila** DataFrames, típicamente por filas:

```python
df_2024 = pd.read_csv("tramites_2024.csv")
df_2025 = pd.read_csv("tramites_2025.csv")

df_todos = pd.concat([df_2024, df_2025], ignore_index=True)
```

`ignore_index=True` genera un índice nuevo y continuo, en vez de repetir los índices originales de cada parte.

---

# `merge` vs `concat`: ¿cuál uso?

| Situación | Herramienta |
|---|---|
| Dos tablas con información **distinta** sobre las mismas entidades (personas + sus trámites) | `merge` |
| Varias tablas con la **misma estructura**, distintas filas (trámites de enero + trámites de febrero) | `concat` |

---

# Repaso integrador: el caso completo

Vamos a combinar todo lo visto en las Clases 5 a 9:

1. Leer los 3 datasets (`personas`, `trámites`, `direcciones`)
2. Normalizar la columna `documento` en los 3 (Clase 7)
3. Convertir fechas en `trámites` (Clase 8)
4. Combinar `trámites` + `personas` con `merge` (esta clase)
5. Agrupar y responder preguntas de negocio con `.groupby()` (Clase 8)

---

# Resumen de la clase

- `pd.merge()` combina por columnas clave; el `how` define qué filas se conservan
- Siempre verificar el resultado de un merge (`indicator=True`, chequeo de duplicados)
- `pd.concat()` apila DataFrames con estructura similar
- Con esto se cierra el módulo de Pandas: base para todo lo que sigue (visualización, dashboards)

---

# Ejercicio práctico

30-40 minutos — ver [`ejercicios/ejercicio-09.md`](./ejercicios/ejercicio-09.md)

Es un ejercicio de **repaso integrador**: combina contenidos de toda la Semana 2.
