# Solución — Ejercicio 2 (Clase 2)

```python
# --- Parte 1 ---
persona = {
    "nombre": "Ana",
    "apellido": "Gómez",
    "edad": 34,
    "documento": 30123456,
    "provincia": "Córdoba",
}

print(
    f'{persona["nombre"]} {persona["apellido"]}, {persona["edad"]} años, '
    f'DNI {persona["documento"]}, reside en {persona["provincia"]}.'
)

# --- Parte 2 ---
if persona["edad"] >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")

if persona["provincia"] == "Córdoba" or persona["provincia"] == "Santa Fe":
    print("Zona centro")
else:
    print("Otra zona")

# --- Parte 3 ---
personas = [
    {"nombre": "Ana", "apellido": "Gómez", "edad": 34, "documento": 30123456, "provincia": "Córdoba"},
    {"nombre": "Luis", "apellido": "Pérez", "edad": 17, "documento": 41987654, "provincia": "Mendoza"},
    {"nombre": "Marta", "apellido": "Díaz", "edad": 45, "documento": 25456789, "provincia": "Santa Fe"},
    {"nombre": "Juan", "apellido": "López", "edad": 22, "documento": 38765432, "provincia": "Córdoba"},
]

print(personas[0]["nombre"])
print(personas[1]["nombre"])
print(personas[2]["nombre"])
print(personas[3]["nombre"])

# --- Parte 4 ---
provincias_unicas = set()
provincias_unicas.add(personas[0]["provincia"])
provincias_unicas.add(personas[1]["provincia"])
provincias_unicas.add(personas[2]["provincia"])
provincias_unicas.add(personas[3]["provincia"])

print(provincias_unicas)
print("Cantidad de provincias distintas:", len(provincias_unicas))

# --- Parte 5 ---
# Tuvimos que acceder "a mano" (personas[0], personas[1], ...) porque todavía
# no vimos una herramienta para recorrer automáticamente todos los elementos
# de una lista sin importar cuántos sean. Si la lista tuviera 1000 personas,
# este enfoque sería impracticable. Eso es exactamente lo que resuelven los
# bucles (for/while), que vemos en la próxima clase.
```

## Nota para el docente

La Parte 5 está pensada como gancho hacia la Clase 3 — si en la corrección grupal alguien ya intuye la respuesta ("con un for sería más fácil"), es una buena oportunidad para validarlo y generar expectativa por el contenido que sigue.
