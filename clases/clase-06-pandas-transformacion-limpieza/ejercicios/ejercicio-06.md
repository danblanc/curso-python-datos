# Ejercicio 6 — Transformación y limpieza

**Duración estimada:** 30-40 minutos

## Objetivo

Practicar creación de columnas, `.apply()`, tratamiento de nulos, detección de duplicados y conversión de tipos.

## Dataset

[`datasets/raw/registros_personas.csv`](../../../datasets/raw/registros_personas.csv)

## Consigna

### Parte 1 — Columnas nuevas

1. Cargá el dataset.
2. Creá una columna `nombre_completo` que combine `nombre` y `apellido` (separados por un espacio).
3. Creá una columna `tiene_email` de tipo booleano, que indique si la columna `email` no es nula.

### Parte 2 — `.apply()`

4. Escribí una función `formatear_provincia(valor)` que devuelva `"Sin dato"` si el valor es nulo, y el valor tal cual si no lo es. Aplicala sobre la columna `provincia` para crear una nueva columna `provincia_formateada`.
5. Usando una función lambda con `.apply()`, creá una columna `apellido_mayuscula` con el apellido en mayúsculas. (Pista: puede que algunos apellidos tengan espacios extra — no hace falta resolverlo todavía, eso lo vemos en la próxima clase.)

### Parte 3 — Nulos

6. Contá cuántos valores nulos tiene la columna `telefono`.
7. Creá una copia del dataset donde los nulos de `telefono` se reemplacen por el texto `"No informado"`.
8. Creá otra copia del dataset donde se eliminen **solo** las filas que tengan nulo en la columna `provincia` (sin afectar nulos en otras columnas).

### Parte 4 — Duplicados

9. Verificá cuántas filas duplicadas exactas hay en el dataset completo (considerando todas las columnas) con `.duplicated().sum()`.
10. Verificá cuántas filas tienen el mismo valor de `documento` (aunque el resto de las columnas no sea idéntico), con `.duplicated(subset=["documento"])`.
11. Compará ambos resultados: ¿son iguales? ¿A qué creés que se debe la diferencia? (Respondé en un comentario. Pista: revisá cómo está formateada la columna `documento` en distintas filas con el mismo valor real.)

### Parte 5 — Conversión de tipos

12. Verificá el tipo de dato actual de la columna `documento` con `df.dtypes` o `df["documento"].dtype`.
13. Usando `pd.to_numeric()` con `errors="coerce"`, intentá convertir la columna `documento` a numérico directamente (sin limpiar el formato primero) y contá cuántos valores quedaron como `NaN` después de la conversión. ¿Por qué creés que pasa esto?

## Qué se evalúa

- Creación correcta de columnas nuevas, incluyendo uso de `.apply()` con función propia y con lambda.
- Manejo correcto de `.fillna()` y `.dropna(subset=...)`.
- Comprensión de la diferencia entre duplicados exactos y duplicados por columna clave.
- Uso correcto de `pd.to_numeric(errors="coerce")` y comprensión de por qué genera `NaN`.

## Ayuda

Solución de referencia en [`soluciones/clase-06/`](../../../soluciones/clase-06/).
