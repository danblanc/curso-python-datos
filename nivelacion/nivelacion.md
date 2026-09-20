# Prueba de nivelación — Repaso general del curso

**Duración estimada:** ~1h30

## Antes de arrancar

Esto **no es una evaluación real** — es un ejercicio de repaso para que vos mismo/a puedas chequear en qué nivel estás parado/a con todo lo visto hasta ahora (desde programación básica hasta Pandas). No hay problema en volver atrás a revisar slides o material anterior mientras la hacés — de hecho, es parte del objetivo.

Los **entornos virtuales son opcionales**: si querés trabajar dentro de uno, perfecto; si no, no es un problema para esta prueba.

## Dataset

Vas a trabajar con [`solicitudes_beneficios.csv`](./solicitudes_beneficios.csv), un dataset nuevo (no el que usamos en las clases) que simula solicitudes de beneficios sociales, con columnas:

| Columna | Descripción |
|---|---|
| `id_solicitud` | Identificador interno |
| `documento` | Documento del solicitante (formato inconsistente, a propósito) |
| `nombre` / `apellido` | Nombre y apellido del solicitante |
| `tipo_beneficio` | Tipo de beneficio solicitado (5 categorías, con inconsistencias de formato) |
| `estado` | `Pendiente`, `Aprobada`, `Rechazada`, `En evaluación` |
| `fecha_solicitud` | Fecha en que se inició la solicitud (formatos mixtos) |
| `fecha_resolucion` | Fecha de resolución (nula si sigue en curso) |
| `ingreso_mensual` | Ingreso mensual declarado |
| `departamento` | Departamento de residencia |
| `cantidad_hijos` | Cantidad de hijos a cargo |

Trabajá en un notebook (`.ipynb`) o script (`.py`), como prefieras. Te recomendamos ir resolviendo en orden — los bloques finales (Pandas) se apoyan en resultados de los anteriores.

---

## Bloque 1 — Fundamentos de Python (sin Pandas)

Este bloque se resuelve con Python puro — sin usar Pandas todavía. Podés leer el CSV con el módulo `csv` de la librería estándar, o simplemente copiar los datos de ejemplo que te damos.

1. Escribí una función `es_documento_valido(doc)` que reciba un documento como texto y devuelva `True` si, luego de quitarle puntos, guiones y espacios, el resultado tiene **exactamente 7 dígitos numéricos**, y `False` en caso contrario. Probala con al menos 4 casos distintos (con puntos, con guiones, sin nada, y uno inválido).

2. Escribí una función `categorizar_ingreso(ingreso)` que reciba un número (o `None`) y devuelva:
   - `"Sin dato"` si el valor es `None`
   - `"Bajo"` si es menor a 30000
   - `"Medio"` si está entre 30000 y 60000 (inclusive)
   - `"Alto"` si es mayor a 60000

   Probala con al menos 4 valores distintos, incluyendo `None`.

3. Dada esta lista de solicitudes de ejemplo:
   ```python
   solicitudes = [
       {"documento": "4.259.420", "estado": "Aprobada", "ingreso": 45000},
       {"documento": "1864493", "estado": "Rechazada", "ingreso": None},
       {"documento": "4-088-417", "estado": "Aprobada", "ingreso": 72000},
       {"documento": "3120040", "estado": "Pendiente", "ingreso": 28000},
       {"documento": "1411008", "estado": "Aprobada", "ingreso": 59000},
   ]
   ```
   Escribí un bucle `for` que recorra la lista e imprima, para cada solicitud, si está **"Aprobada"** o no, usando un condicional. Además, usando las dos funciones que escribiste en los puntos 1 y 2, imprimí también si el documento es válido y en qué categoría de ingreso cae. El resultado para la primera solicitud debería verse similar a:
   ```
   Documento 4.259.420 (válido) - Estado: Aprobada - Ingreso: Medio
   ```

4. Usando una **list comprehension**, generá una lista con los documentos (sin normalizar) de todas las solicitudes que estén `"Aprobada"`.

5. Usando `try`/`except`, escribí una función `dividir_seguro(a, b)` que devuelva el resultado de `a / b`, pero que devuelva el texto `"No se puede dividir por cero"` en vez de fallar si `b` es `0`. Probala con al menos un caso que dispare la excepción.

---

## Bloque 2 — Archivos y NumPy

6. Sin usar Pandas todavía: usando `with open(...)` y el módulo `csv`, leé el archivo `solicitudes_beneficios.csv` y contá cuántas filas tiene en total (sin contar el encabezado).

7. Usando NumPy, creá un array con los siguientes ingresos mensuales: `[45000, None, 72000, 28000, 59000]` — como no podés poner `None` directamente en un array numérico de NumPy sin convertirlo a `NaN`, usá `np.nan` en su lugar (`import numpy as np`).
   - Calculá el promedio del array **ignorando** los `NaN` (buscá la función de NumPy indicada para eso — pista: existe una versión de `mean` que ignora nulos).
   - Calculá cuántos valores del array son mayores a 50000 (usando indexado booleano, sin bucles).

---

## Bloque 3 — Pandas: carga y exploración

A partir de acá, trabajá con Pandas y el dataset completo.

8. Cargá `solicitudes_beneficios.csv` con `pd.read_csv()`.
9. Mostrá la cantidad de filas y columnas del dataset.
10. Ejecutá `.info()`. ¿Cuántas columnas tienen al menos un valor nulo? Nombralas.
11. Calculá la cantidad exacta de valores nulos por columna con `.isnull().sum()`.
12. Filtrá el dataset para quedarte solo con las solicitudes en estado `"Aprobada"` **y** con `ingreso_mensual` mayor a 50000. ¿Cuántas filas cumplen ambas condiciones?
13. Usando `.loc`, mostrá únicamente las columnas `nombre`, `apellido` y `estado` de las primeras 5 filas del dataset.

---

## Bloque 4 — Pandas: limpieza y transformación (énfasis especial)

14. Creá una columna nueva `nombre_completo`, combinando `nombre` y `apellido` (separados por un espacio).

15. La columna `tipo_beneficio` tiene inconsistencias de mayúsculas/minúsculas y espacios. Creá una columna `tipo_beneficio_normalizado` aplicando `.str.strip()` y `.str.lower()`. Compará cuántos valores únicos tiene la columna original (`.nunique()`) contra la normalizada. ¿Cuántas categorías "reales" hay en realidad?

16. La columna `documento` tiene formatos inconsistentes (con puntos, guiones o sin nada). Escribí una función (o usá una expresión regular con `.str.replace()`) que elimine todo lo que no sea un dígito, y creá una columna `documento_normalizado`. Convertila a tipo numérico con `pd.to_numeric()`.

17. Contá cuántas filas duplicadas hay considerando la columna `documento` **sin normalizar** (`.duplicated(subset=["documento"])`), y comparalo contra la cantidad de duplicados considerando `documento_normalizado`. En este dataset en particular, ¿el número cambia o se mantiene igual? Explicá con tus palabras, en un comentario, en qué situación **sí** cambiaría ese número (pensá en cómo se generan los duplicados en este dataset).

18. Eliminá los duplicados del dataset quedándote con la **primera aparición** de cada `documento_normalizado`, y guardá el resultado en un nuevo DataFrame `df_sin_duplicados`.

19. La columna `ingreso_mensual` tiene valores nulos. Creá una columna `ingreso_mensual_completo` donde los nulos se reemplacen por el **promedio general** de la columna (sin contar los nulos).

20. Convertí `fecha_solicitud` y `fecha_resolucion` a tipo fecha, usando `pd.to_datetime()` con los parámetros que correspondan para manejar formatos mixtos. Después de convertir, contá cuántos valores nulos (`NaT`) quedan en `fecha_resolucion`. ¿A qué se debe esa cantidad de nulos? (Pista: revisá la relación con la columna `estado`.)

21. Creá una columna `dias_para_resolucion` con la diferencia en días entre `fecha_resolucion` y `fecha_solicitud` (para las filas donde aplique). Ejecutá `.describe()` sobre esa columna y prestá atención al valor **mínimo**: ¿te parece razonable? Si ves algo raro, no lo ignores — es información real sobre un problema que ya vimos en el curso (pensalo en relación a cómo se convierten fechas con formato mixto).

---

## Bloque 5 — Pandas: agregación y combinación

22. Usando `.groupby()` sobre `tipo_beneficio_normalizado`, calculá el **ingreso promedio** (`ingreso_mensual_completo`) y la **cantidad de solicitudes** por tipo de beneficio, en una sola tabla usando `.agg()` con nombres de columna personalizados.

23. Generá una tabla pivote (`pd.pivot_table()`) con: filas = `departamento`, columnas = `estado`, valores = cantidad de solicitudes (usando `aggfunc="count"` sobre `id_solicitud`), rellenando con `0` donde no haya datos.

24. Creá un segundo DataFrame pequeño, a mano, con información adicional de departamentos:
    ```python
    info_departamentos = pd.DataFrame({
        "departamento": ["Montevideo", "Canelones", "Maldonado", "Salto", "Paysandú", "Rivera", "Colonia", "Rocha"],
        "region": ["Sur", "Sur", "Este", "Norte", "Litoral", "Norte", "Litoral", "Este"],
    })
    ```
    Combiná este DataFrame con tu dataset principal usando `pd.merge()`, de forma que cada solicitud quede asociada a su región, sin perder ninguna solicitud aunque su departamento sea nulo. ¿Qué tipo de `how` corresponde usar acá, y por qué?

25. Usando el resultado del punto anterior, agrupá por `region` y calculá la cantidad de solicitudes `"Aprobada"` en cada una.

---

## Bloque 6 — Para cerrar (reflexión corta)

26. En un comentario, respondé brevemente: de todo lo que resolviste en esta prueba, ¿qué fue lo que más te costó? ¿Hay algún bloque temático que sientas que necesitás repasar con más calma?

---

## Al terminar

La solución de referencia está en [`solucion-nivelacion.md`](./solucion-nivelacion.md) — te recomendamos comparar tus resultados numéricos (cantidades, promedios) con los de la solución para confirmar que llegaste a los mismos valores, no solo revisar que el código "se parezca".
