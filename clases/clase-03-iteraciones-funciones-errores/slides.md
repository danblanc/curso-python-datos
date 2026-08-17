---
marp: true
theme: default
paginate: true
size: 16:9
---

# Clase 3
## Iteraciones, funciones y manejo de errores

Curso de Python para Análisis de Datos

---

# Agenda de hoy

1. Bucle `for`
2. Bucle `while`
3. List comprehensions
4. Funciones
5. Manejo de errores
6. Ejercicio práctico

---

# El problema de la clase pasada

En el ejercicio anterior, recorrimos una lista de personas "a mano":

```python
print(personas[0]["nombre"])
print(personas[1]["nombre"])
print(personas[2]["nombre"])
print(personas[3]["nombre"])
```

¿Y si tenemos 10.000 personas? Necesitamos una forma de repetir una acción automáticamente.

---

# Bucle `for`

Recorre cada elemento de una colección (lista, diccionario, etc.):

```python
personas = ["Ana", "Luis", "Marta"]

for nombre in personas:
    print(nombre)
```

`nombre` es una variable temporal que, en cada vuelta, toma el valor del siguiente elemento.

---

# `for` con `range()`

`range()` genera una secuencia de números, útil para repetir algo "N veces":

```python
for i in range(5):
    print(i)          # imprime 0, 1, 2, 3, 4

for i in range(2, 10, 2):
    print(i)          # imprime 2, 4, 6, 8 (inicio, fin, salto)
```

---

# `for` sobre diccionarios

```python
persona = {"nombre": "Ana", "edad": 34, "provincia": "Córdoba"}

for clave in persona:
    print(clave, "->", persona[clave])

# Forma más directa:
for clave, valor in persona.items():
    print(clave, "->", valor)
```

---

# `for` sobre lista de diccionarios

El caso que nos interesa para datos administrativos:

```python
personas = [
    {"nombre": "Ana", "edad": 34},
    {"nombre": "Luis", "edad": 17},
]

for persona in personas:
    print(persona["nombre"], persona["edad"])
```

Esto es, conceptualmente, muy parecido a recorrer las filas de una tabla — la base de lo que vamos a hacer con Pandas.

---

# Bucle `while`

Repite mientras una condición sea verdadera:

```python
contador = 0

while contador < 5:
    print(contador)
    contador += 1   # equivalente a: contador = contador + 1
```

**Cuidado:** si la condición nunca se vuelve falsa, el bucle nunca termina (*bucle infinito*). Siempre asegurate de que algo dentro del bucle mueva la condición hacia su fin.

---

# `break` y `continue`

```python
for numero in range(10):
    if numero == 5:
        break          # corta el bucle completamente
    print(numero)

for numero in range(10):
    if numero % 2 == 0:
        continue       # salta a la siguiente vuelta, sin ejecutar lo de abajo
    print(numero)       # solo imprime los impares
```

---

# List comprehensions

Una forma compacta de crear listas a partir de otra colección:

```python
numeros = [1, 2, 3, 4, 5]

# Forma tradicional
cuadrados = []
for n in numeros:
    cuadrados.append(n ** 2)

# List comprehension (equivalente)
cuadrados = [n ** 2 for n in numeros]
```

Con condición:

```python
pares = [n for n in numeros if n % 2 == 0]
```

---

# ¿Cuándo usar comprehensions?

- Cuando la lógica es simple (una transformación o un filtro).
- Si la lógica tiene varios pasos o condiciones complejas, mejor usar un `for` tradicional — prioridad siempre a la **legibilidad**.

```python
# Legible
pares = [n for n in numeros if n % 2 == 0]

# Ilegible (evitar esto)
resultado = [n**2 if n % 2 == 0 else n**3 for n in numeros if n > 0 and n < 100]
```

---

# ¿Por qué funciones?

Evitan repetir el mismo código una y otra vez. Empaquetan una tarea con un nombre.

```python
# Sin función: repetimos la lógica cada vez
print("Hola, Ana!")
print("Hola, Luis!")

# Con función: la lógica está en un solo lugar
def saludar(nombre):
    print(f"Hola, {nombre}!")

saludar("Ana")
saludar("Luis")
```

---

# Definición de funciones

```python
def sumar(a, b):
    resultado = a + b
    return resultado

total = sumar(3, 5)   # total = 8
```

- `def` inicia la definición
- Los parámetros (`a`, `b`) son las entradas
- `return` define qué devuelve la función (si no hay `return`, devuelve `None`)

---

# Parámetros por defecto

```python
def saludar(nombre, saludo="Hola"):
    print(f"{saludo}, {nombre}!")

saludar("Ana")               # Hola, Ana!
saludar("Luis", "Buenas")    # Buenas, Luis!
```

Los parámetros con valor por defecto son opcionales al llamar la función.

---

# Scope (alcance) de variables

```python
def calcular():
    x = 10   # x es local a esta función
    return x

calcular()
print(x)   # Error: x no existe fuera de la función
```

Una variable definida **dentro** de una función no existe fuera de ella. Esto evita que funciones distintas "se pisen" entre sí.

---

# Errores en Python (excepciones)

Cuando algo sale mal, Python lanza una **excepción** y el programa se detiene:

```python
edad = int("no soy un número")
# ValueError: invalid literal for int() with base 10: 'no soy un número'
```

Tipos comunes: `ValueError`, `TypeError`, `KeyError`, `ZeroDivisionError`, `FileNotFoundError`.

---

# `try` / `except`

Permite **anticipar** un posible error y decidir qué hacer en vez de que el programa se caiga:

```python
try:
    edad = int(input("Ingresá tu edad: "))
    print("Tu edad es", edad)
except ValueError:
    print("Eso no es un número válido")
```

---

# `try` / `except` / `else` / `finally`

```python
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir por cero")
else:
    print("Todo salió bien:", resultado)   # solo si NO hubo error
finally:
    print("Esto se ejecuta siempre")        # con o sin error
```

`finally` es útil para tareas de limpieza (por ejemplo, cerrar un archivo) que deben pasar sí o sí.

---

# ¿Por qué importa esto para datos?

Cuando trabajemos con archivos reales (Pandas), es común encontrar:

- Un archivo que no existe
- Una columna con un valor que no se puede convertir a número
- Una fecha con formato inesperado

`try`/`except` nos va a permitir **anticipar** estos casos, en vez de que todo el análisis se caiga por un solo dato mal cargado.

---

# Resumen de la clase

- `for` para recorrer colecciones, `while` para repetir según condición
- List comprehensions: forma compacta para casos simples
- Funciones para organizar y reutilizar código
- `try`/`except` para manejar errores sin que el programa se caiga

---

# Ejercicio práctico

30-40 minutos — ver [`ejercicios/ejercicio-03.md`](./ejercicios/ejercicio-03.md)
