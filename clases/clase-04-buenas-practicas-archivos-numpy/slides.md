---
marp: true
theme: default
paginate: true
size: 16:9
---

# Clase 4
## Buenas prácticas, archivos y NumPy

Curso de Python para Análisis de Datos

---

# Agenda de hoy

1. Buenas prácticas de código (PEP8)
2. Organización en módulos
3. Lectura y escritura de archivos
4. Introducción a NumPy
5. Ejercicio práctico

---

# ¿Por qué "buenas prácticas"?

El código no se escribe una sola vez: se **lee** muchas veces (por vos mismo/a en el futuro, y por otras personas).

Código prolijo:
- Es más fácil de entender y de corregir
- Genera menos errores
- Facilita trabajar en equipo

---

# PEP8: la guía de estilo de Python

PEP8 es el documento oficial que define convenciones de estilo. Algunas de las más importantes:

- Nombres de variables y funciones en `snake_case`
- 4 espacios de indentación (no tabs)
- Máximo ~79-99 caracteres por línea (orientativo)
- Espacios alrededor de operadores: `x = 5`, no `x=5`
- Nombres descriptivos: `cantidad_tramites` mejor que `ct`

---

# PEP8 en la práctica

VS Code puede ayudarte automáticamente:

- La extensión de Python marca advertencias de estilo
- Herramientas como `black` o `ruff` formatean el código automáticamente

No hace falta memorizar todo PEP8: con buenos hábitos básicos (nombres claros, indentación consistente) ya se cubre el 90% del beneficio.

---

# Organización de código en módulos

Hasta ahora escribimos todo en un solo archivo. A medida que un proyecto crece, conviene separar el código en varios archivos (**módulos**).

```python
# archivo: utilidades.py
def saludar(nombre):
    return f"Hola, {nombre}!"
```

```python
# archivo: main.py
import utilidades

mensaje = utilidades.saludar("Ana")
print(mensaje)
```

Ambos archivos deben estar en la misma carpeta (por ahora).

---

# Lectura de archivos de texto

```python
archivo = open("datos.txt", "r", encoding="utf-8")
contenido = archivo.read()
print(contenido)
archivo.close()   # importante: siempre cerrar el archivo
```

Problema: si el código falla antes del `close()`, el archivo queda abierto (puede causar problemas).

---

# La forma correcta: `with`

```python
with open("datos.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
    print(contenido)

# Acá afuera, el archivo ya se cerró automáticamente,
# incluso si hubo un error adentro del bloque.
```

`with` es el estándar recomendado en Python para trabajar con archivos.

---

# Escritura de archivos

```python
with open("salida.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Primera línea\n")
    archivo.write("Segunda línea\n")
```

Modos comunes: `"r"` (leer), `"w"` (escribir, sobrescribe si existe), `"a"` (agregar al final).

---

# Leyendo línea por línea

```python
with open("datos.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        print(linea.strip())   # strip() quita el salto de línea al final
```

Útil cuando el archivo es grande y no queremos cargarlo todo en memoria de una vez.

---

# El módulo `csv`

Python trae un módulo para trabajar con archivos CSV sin instalar nada extra:

```python
import csv

with open("personas.csv", "r", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        print(fila["nombre"], fila["edad"])
```

`DictReader` convierte cada fila en un diccionario, usando la primera fila como encabezados.

---

# Escribir un CSV

```python
import csv

personas = [
    {"nombre": "Ana", "edad": 34},
    {"nombre": "Luis", "edad": 28},
]

with open("salida.csv", "w", encoding="utf-8", newline="") as archivo:
    escritor = csv.DictWriter(archivo, fieldnames=["nombre", "edad"])
    escritor.writeheader()
    escritor.writerows(personas)
```

---

# ¿Por qué ver esto si después usamos Pandas?

Porque **Pandas hace exactamente esto por debajo**, de forma optimizada.

Entender qué pasa "manualmente" ayuda a:
- No tratar a Pandas como una caja negra
- Diagnosticar errores cuando algo falla al leer un archivo
- Saber cuándo *no* hace falta Pandas (archivos chicos, tareas simples)

---

# Introducción a NumPy

**NumPy** (*Numerical Python*) es la librería base para cálculo numérico en Python. Pandas está construido sobre NumPy.

Su estructura central es el **array**: parecido a una lista, pero pensado para operaciones matemáticas eficientes sobre grandes volúmenes de datos.

```python
import numpy as np

numeros = np.array([1, 2, 3, 4, 5])
```

---

# Array vs. lista

```python
lista = [1, 2, 3, 4, 5]
array = np.array([1, 2, 3, 4, 5])

# Multiplicar todos los elementos por 2:

# Con lista: necesito un bucle o comprehension
resultado_lista = [x * 2 for x in lista]

# Con array: operación directa (vectorizada)
resultado_array = array * 2
```

Los arrays permiten operar sobre **todos los elementos a la vez**, sin bucles explícitos — y son mucho más rápidos con grandes volúmenes de datos.

---

# Operaciones vectorizadas

```python
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

a + b        # array([11, 22, 33])
a * 2        # array([2, 4, 6])
a > 2        # array([False, False, True])
```

Todas estas operaciones se aplican elemento por elemento, automáticamente.

---

# Funciones estadísticas de NumPy

```python
montos = np.array([1500, 8000, 25000, 1500, 0])

montos.mean()    # promedio
montos.sum()     # suma total
montos.std()     # desvío estándar
montos.min()     # mínimo
montos.max()     # máximo
```

Estas mismas funciones (y muchas más) las vamos a volver a ver, aplicadas sobre columnas enteras, cuando lleguemos a Pandas.

---

# Indexado y filtrado de arrays

```python
montos = np.array([1500, 8000, 25000, 1500, 0])

montos[0]          # 1500 (primer elemento)
montos[montos > 1000]   # array([1500, 8000, 25000, 1500])
```

Esta última línea es un adelanto de cómo vamos a filtrar datos en Pandas: "quiero solo los elementos que cumplen esta condición".

---

# Resumen de la clase

- PEP8 y organización en módulos hacen el código más mantenible
- `with open(...)` es la forma segura de trabajar con archivos
- El módulo `csv` permite leer/escribir CSV sin librerías externas
- NumPy introduce arrays y operaciones vectorizadas, base de Pandas

---

# Ejercicio práctico

30-40 minutos — ver [`ejercicios/ejercicio-04.md`](./ejercicios/ejercicio-04.md)

**Nota:** a partir de esta clase, algunos ejercicios usan la terminal para verificar resultados. Recordá los comandos equivalentes en Mac y Windows si hace falta consultar la [guía de instalación](../../recursos-generales/instalacion-entorno.md).
