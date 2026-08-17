# Ejercicio 8 — Fechas y agregación

**Duración estimada:** 30-40 minutos

## Objetivo

Practicar conversión y componentes de fechas, cálculo de diferencias, `.groupby()` y tablas pivote.

## Dataset

[`datasets/raw/registros_tramites.xlsx`](../../../datasets/raw/registros_tramites.xlsx)

## Consigna

### Parte 1 — Convertir fechas

1. Cargá el dataset con `pd.read_excel()`.
2. Convertí `fecha_inicio` y `fecha_resolucion` a tipo fecha usando `pd.to_datetime()` con `format="mixed"`, `dayfirst=True` y `errors="coerce"`.
3. Contá cuántos valores nulos (`NaT`) quedaron en cada columna después de la conversión. Para `fecha_resolucion`, pensá: ¿por qué tiene tantos nulos? (Pista: revisá la columna `estado` — ¿todos los trámites tienen fecha de resolución?)

### Parte 2 — Componentes y diferencias

4. Creá una columna `anio_inicio` con el año de `fecha_inicio`.
5. Agrupá por `anio_inicio` y contá cuántos trámites se iniciaron cada año.
6. Creá una columna `dias_resolucion` con la diferencia en días entre `fecha_resolucion` y `fecha_inicio`.
7. Ejecutá `df["dias_resolucion"].describe()` y fijate el valor **mínimo**. ¿Te parece un resultado razonable para una diferencia de días? Investigá al menos una fila con valor negativo: mostrá sus columnas `fecha_inicio` y `fecha_resolucion` completas.

   > Esto no es un error tuyo: es un problema real de ambigüedad al convertir fechas con formatos mixtos (por ejemplo, `"03/07/2025"` puede interpretarse como 3 de julio o como 7 de marzo, según el criterio). Es exactamente el tipo de cosas que hay que revisar siempre después de convertir fechas con formato inconsistente — nunca asumir que la conversión salió perfecta sin verificar.

### Parte 3 — `.groupby()`

8. Agrupá por `tipo_tramite` y calculá la suma de `monto_asociado` para cada grupo.
9. Mirá la lista de valores únicos de `tipo_tramite` con `.unique()`. ¿Notás algo que podría estar afectando el resultado del punto anterior? (Pista: repasá lo que vimos en la Clase 7 sobre normalización de texto.)
10. Aplicá `.str.lower().str.strip()` sobre `tipo_tramite` para crear una versión normalizada, y repetí el `.groupby()` de suma de montos con esa versión. Compará la cantidad de grupos antes y después.

### Parte 4 — `.agg()` y tabla pivote

11. Usando `.agg()` con nombres personalizados, generá una tabla con, para cada `tipo_tramite` normalizado: monto total, monto promedio y cantidad de trámites.
12. Generá una tabla pivote con `pd.pivot_table()`: filas = `provincia`, columnas = `estado`, valores = suma de `monto_asociado`, con `fill_value=0`.

## Qué se evalúa

- Conversión correcta de fechas con manejo de formato mixto.
- Detección y verificación crítica de un resultado sospechoso (fechas negativas), no solo ejecutar código sin revisar el resultado.
- Uso correcto de `.groupby()`, `.agg()` con nombres, y `pivot_table()`.
- Conexión entre el contenido de esta clase y la normalización de texto de la clase anterior.

## Ayuda

Solución de referencia en [`soluciones/clase-08/`](../../../soluciones/clase-08/).
