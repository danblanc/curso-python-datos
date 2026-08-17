# Solución — Ejercicio 3 (Clase 3)

```python
tramites = [
    {"id": 1, "tipo": "Renovación de licencia", "monto": 1500.0, "estado": "Aprobado"},
    {"id": 2, "tipo": "Alta de comercio", "monto": None, "estado": "En revisión"},
    {"id": 3, "tipo": "Cambio de domicilio", "monto": 0.0, "estado": "Aprobado"},
    {"id": 4, "tipo": "Solicitud de subsidio", "monto": 25000.0, "estado": "Rechazado"},
    {"id": 5, "tipo": "Renovación de licencia", "monto": 1500.0, "estado": "Aprobado"},
    {"id": 6, "tipo": "Alta de comercio", "monto": 8000.0, "estado": "Aprobado"},
]

# --- Parte 1 ---
for tramite in tramites:
    print(tramite["tipo"], "-", tramite["estado"])

# --- Parte 2 ---
def contar_por_estado(lista_tramites, estado):
    contador = 0
    for tramite in lista_tramites:
        if tramite["estado"] == estado:
            contador += 1
    return contador

print("Aprobados:", contar_por_estado(tramites, "Aprobado"))
print("En revisión:", contar_por_estado(tramites, "En revisión"))
print("Rechazados:", contar_por_estado(tramites, "Rechazado"))

# --- Parte 3 ---
# Enfoque con if:
def sumar_montos(lista_tramites):
    total = 0
    for tramite in lista_tramites:
        if tramite["monto"] is not None:
            total += tramite["monto"]
    return total

# Enfoque alternativo con try/except (equivalente):
def sumar_montos_try(lista_tramites):
    total = 0
    for tramite in lista_tramites:
        try:
            total += tramite["monto"]
        except TypeError:
            # ocurre al intentar sumar None con un número
            pass
    return total

print("Total montos:", sumar_montos(tramites))

# --- Parte 4 ---
tipos_aprobados = [t["tipo"] for t in tramites if t["estado"] == "Aprobado"]
tipos_aprobados_unicos = set(tipos_aprobados)

print(tipos_aprobados)
print(tipos_aprobados_unicos)

# --- Parte 5 ---
# Sí, las funciones seguirían funcionando igual sin cambiar el código: no
# dependen de la cantidad de elementos de la lista, sino que la recorren
# elemento por elemento sin importar cuántos haya. Esto es una ventaja
# central de encapsular la lógica en funciones y bucles, en vez de escribir
# el código "a mano" para cada caso puntual. (Nota: con 2 millones de
# registros, en la práctica preferiríamos Pandas por rendimiento — pero
# la lógica en sí seguiría siendo válida.)
```

## Nota para el docente

El enfoque con `try/except` de la Parte 3 es un buen momento para reforzar que **no siempre hay una única forma correcta** de resolver algo — ambas soluciones son válidas, y elegir una u otra es una cuestión de estilo y claridad, no de corrección.
