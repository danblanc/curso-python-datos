---
marp: true
theme: default
paginate: true
size: 16:9
---

# Clase 2
## Tipos, estructuras y condicionales

Curso de Python para Análisis de Datos

---

# Agenda de hoy

1. Variables y tipos de datos
2. Listas, tuplas, diccionarios, sets
3. Operadores
4. Condicionales
5. Ejercicio práctico

---

# Variables

Una variable es un **nombre que apunta a un valor** guardado en memoria.

```python
edad = 30
nombre = "Ana"
activo = True
```

Reglas de nombres: empiezan con letra o `_`, no pueden tener espacios, son *case-sensitive* (`edad` ≠ `Edad`).

Convención: `snake_case` (minúsculas con guiones bajos), no `camelCase`.

---

# Tipos de datos básicos

| Tipo | Ejemplo | Descripción |
|---|---|---|
| `int` | `42` | Números enteros |
| `float` | `3.14` | Números decimales |
| `str` | `"hola"` | Texto (cadena de caracteres) |
| `bool` | `True` / `False` | Verdadero o falso |
| `None` | `None` | Ausencia de valor |

Para saber el tipo de algo: `type(variable)`

---

# Conversión de tipos

A veces necesitamos convertir un tipo a otro:

```python
edad_texto = "30"
edad_numero = int(edad_texto)   # convierte str -> int

precio = 19.99
precio_texto = str(precio)      # convierte float -> str

cantidad = int("7")
cantidad_float = float(cantidad)  # int -> float
```

Cuidado: `int("hola")` da error — no todo texto se puede convertir a número.

---

# Listas

Colección **ordenada** y **modificable** de elementos.

```python
frutas = ["manzana", "banana", "pera"]

frutas[0]          # "manzana" (el índice empieza en 0)
frutas.append("kiwi")     # agrega al final
frutas[1] = "durazno"     # modifica un elemento
len(frutas)         # cantidad de elementos
```

Pueden mezclar tipos, aunque en la práctica solemos usarlas con un solo tipo.

---

# Tuplas

Igual que una lista, pero **inmutable** (no se puede modificar después de creada).

```python
coordenada = (10, 20)
coordenada[0]        # 10
coordenada[0] = 5     # Error: las tuplas no se pueden modificar
```

¿Cuándo usar una tupla en vez de una lista? Cuando el dato no debería cambiar (por ejemplo, coordenadas fijas, o un registro que representa algo "cerrado").

---

# Diccionarios

Colección de pares **clave: valor**. No están ordenados por posición, se accede por clave.

```python
persona = {
    "nombre": "Ana",
    "edad": 30,
    "activo": True
}

persona["nombre"]        # "Ana"
persona["email"] = "ana@mail.com"   # agrega una nueva clave
persona.keys()           # todas las claves
persona.values()          # todos los valores
```

---

# Sets

Colección **sin duplicados** y sin orden garantizado.

```python
provincias = {"Córdoba", "Santa Fe", "Córdoba"}
print(provincias)   # {"Córdoba", "Santa Fe"} - el duplicado desaparece

provincias.add("Mendoza")
"Santa Fe" in provincias    # True
```

Muy útil para, por ejemplo, saber cuántos valores **distintos** hay en una columna de datos.

---

# ¿Cuál estructura uso?

| Necesito... | Uso |
|---|---|
| Orden, permitir duplicados, poder modificar | **Lista** |
| Orden, datos que no deben cambiar | **Tupla** |
| Acceder por nombre/clave, no por posición | **Diccionario** |
| Valores únicos, no me importa el orden | **Set** |

---

# Operadores aritméticos

```python
5 + 3   # 8
5 - 3   # 2
5 * 3   # 15
5 / 3   # 1.666... (división siempre da float)
5 // 3  # 1 (división entera)
5 % 3   # 2 (resto de la división)
5 ** 2  # 25 (potencia)
```

---

# Operadores de comparación

Devuelven siempre `True` o `False`:

```python
5 == 3    # False (igualdad)
5 != 3    # True  (distinto)
5 > 3     # True
5 < 3     # False
5 >= 5    # True
5 <= 3    # False
```

Ojo: `=` es asignación, `==` es comparación. Es el error de tipeo más común de quien empieza a programar.

---

# Operadores lógicos

```python
edad = 25
tiene_dni = True

edad >= 18 and tiene_dni     # True: ambas condiciones se cumplen
edad >= 18 or tiene_dni      # True: alcanza con que se cumpla una
not tiene_dni                # False: invierte el valor
```

`and`, `or`, `not` — en minúsculas, son palabras clave de Python.

---

# Condicionales: `if`

```python
edad = 20

if edad >= 18:
    print("Es mayor de edad")
```

**La indentación (sangría) no es estética: es sintaxis.** Python usa la indentación para saber qué código pertenece al `if`.

---

# `if` / `elif` / `else`

```python
edad = 15

if edad >= 65:
    print("Adulto mayor")
elif edad >= 18:
    print("Adulto")
else:
    print("Menor de edad")
```

Se evalúa en orden: apenas una condición es verdadera, se ejecuta ese bloque y se ignoran los siguientes.

---

# Condicionales anidados y combinados

```python
edad = 30
provincia = "Córdoba"

if edad >= 18:
    if provincia == "Córdoba":
        print("Adulto de Córdoba")

# Equivalente, más legible:
if edad >= 18 and provincia == "Córdoba":
    print("Adulto de Córdoba")
```

Cuando se puede, preferir condiciones combinadas con `and`/`or` antes que anidar demasiados `if`.

---

# Resumen de la clase

- Variables + tipos básicos: `int`, `float`, `str`, `bool`, `None`
- 4 estructuras nativas, cada una para un caso de uso distinto
- Operadores aritméticos, de comparación y lógicos
- Condicionales para tomar decisiones según los datos

---

# Ejercicio práctico

30-40 minutos — ver [`ejercicios/ejercicio-02.md`](./ejercicios/ejercicio-02.md)

Vamos a modelar un registro simple de una persona usando diccionarios y listas, y a tomar decisiones sobre esos datos con condicionales.
