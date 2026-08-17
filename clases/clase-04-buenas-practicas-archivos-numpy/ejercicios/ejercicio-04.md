# Ejercicio 4 — Archivos y primeros pasos con NumPy

**Duración estimada:** 30-40 minutos

## Objetivo

Practicar lectura/escritura de archivos con Python puro y operaciones básicas con NumPy.

## Consigna

### Parte 1 — Escribir un archivo de texto

1. Creá un script `ejercicio_04.py`.
2. Usando `with open(...)`, escribí un archivo `notas.txt` con 3 líneas, cada una con el nombre de un tipo de trámite (podés inventar los nombres o usar los del curso: "Renovación de licencia", "Alta de comercio", "Cambio de domicilio").

### Parte 2 — Leer el archivo

3. Abrí el archivo `notas.txt` y leelo línea por línea, imprimiendo cada línea sin el salto de línea al final (usá `.strip()`).

### Parte 3 — Trabajar con CSV

4. Creá un archivo `tramites_ejercicio.csv` con las columnas `id`, `tipo`, `monto`, con al menos 5 filas de datos inventados (podés escribirlo directamente en un editor de texto, o generarlo con el módulo `csv` desde Python — vos elegís).
5. Usando `csv.DictReader`, leé el archivo y calculá la suma total de la columna `monto`, imprimiendo el resultado.

### Parte 4 — NumPy

6. Creá un array de NumPy con los montos que usaste en la Parte 3 (podés escribirlos directamente como lista y convertirlos con `np.array(...)`, no hace falta leerlos del CSV para esta parte).
7. Calculá e imprimí: la suma, el promedio, el máximo y el mínimo del array, usando las funciones de NumPy.
8. Creá un nuevo array que contenga **solo los montos mayores al promedio** (pista: `array[array > promedio]`).

### Parte 5 — Terminal (verificación)

9. Desde la terminal, verificá que los archivos `notas.txt` y `tramites_ejercicio.csv` se crearon correctamente, listando el contenido de la carpeta:

   **macOS / Linux:**
   ```bash
   ls
   ```

   **Windows (PowerShell):**
   ```powershell
   dir
   ```

## Qué se evalúa

- Uso correcto de `with open(...)` para lectura y escritura.
- Uso correcto de `csv.DictReader` para leer el CSV.
- Cálculos correctos con funciones de NumPy.
- Filtrado correcto de un array según una condición.

## Ayuda

Solución de referencia en [`soluciones/clase-04/`](../../../soluciones/clase-04/).
