# Ejercicio 3 — Procesando una lista de trámites

**Duración estimada:** 30-40 minutos

## Objetivo

Practicar bucles, funciones y manejo de errores, trabajando sobre una lista de trámites similar a la que vamos a encontrar más adelante en Pandas.

## Consigna

Partimos de esta lista (copiala al inicio de tu archivo `ejercicio_03.py`):

```python
tramites = [
    {"id": 1, "tipo": "Renovación de licencia", "monto": 1500.0, "estado": "Aprobado"},
    {"id": 2, "tipo": "Alta de comercio", "monto": None, "estado": "En revisión"},
    {"id": 3, "tipo": "Cambio de domicilio", "monto": 0.0, "estado": "Aprobado"},
    {"id": 4, "tipo": "Solicitud de subsidio", "monto": 25000.0, "estado": "Rechazado"},
    {"id": 5, "tipo": "Renovación de licencia", "monto": 1500.0, "estado": "Aprobado"},
    {"id": 6, "tipo": "Alta de comercio", "monto": 8000.0, "estado": "Aprobado"},
]
```

### Parte 1 — Recorrer con `for`

1. Con un `for`, imprimí el `tipo` y el `estado` de cada trámite.

### Parte 2 — Función de conteo

2. Escribí una función `contar_por_estado(lista_tramites, estado)` que reciba la lista de trámites y un estado (por ejemplo `"Aprobado"`), y devuelva **cuántos** trámites tienen ese estado.
3. Probala con los tres estados presentes (`"Aprobado"`, `"En revisión"`, `"Rechazado"`) e imprimí los resultados.

### Parte 3 — Función de suma con manejo de errores

4. Escribí una función `sumar_montos(lista_tramites)` que recorra la lista y sume el campo `monto` de todos los trámites, **pero que no falle** si algún trámite tiene `monto` igual a `None` (en ese caso, ese trámite no debería sumar nada, sin interrumpir el resto).

   Pista: podés resolverlo con un `if` (verificando si es `None` antes de sumar) o con `try`/`except` capturando el error que ocurriría al sumar `None` con un número — probá ambos enfoques si te da el tiempo, y quedate con el que te resulte más claro.

5. Probá la función con la lista completa e imprimí el resultado.

### Parte 4 — List comprehension

6. Usando una list comprehension, creá una lista `tipos_aprobados` con el `tipo` de todos los trámites cuyo `estado` sea `"Aprobado"`.
7. Convertí esa lista a un `set` para ver los tipos únicos de trámites aprobados, e imprimilo.

### Parte 5 — Para pensar

En un comentario al final del archivo: ¿qué pasaría si en vez de 6 trámites tuviéramos 2 millones? ¿Las funciones que escribiste seguirían funcionando igual, sin cambiar el código?

## Qué se evalúa

- Uso correcto de `for` sobre una lista de diccionarios.
- Funciones que reciben parámetros y devuelven un valor con `return`.
- Manejo correcto del caso `None` sin que el programa falle.
- Uso de list comprehension y set para obtener valores únicos.

## Ayuda

Solución de referencia en [`soluciones/clase-03/`](../../../soluciones/clase-03/).
