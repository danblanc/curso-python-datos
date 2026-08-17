# Solución — Ejercicio 4 (Clase 4)

```python
import csv
import numpy as np

# --- Parte 1 ---
tipos_tramite = [
    "Renovación de licencia",
    "Alta de comercio",
    "Cambio de domicilio",
]

with open("notas.txt", "w", encoding="utf-8") as archivo:
    for tipo in tipos_tramite:
        archivo.write(tipo + "\n")

# --- Parte 2 ---
with open("notas.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        print(linea.strip())

# --- Parte 3 ---
tramites = [
    {"id": 1, "tipo": "Renovación de licencia", "monto": 1500},
    {"id": 2, "tipo": "Alta de comercio", "monto": 8000},
    {"id": 3, "tipo": "Cambio de domicilio", "monto": 0},
    {"id": 4, "tipo": "Solicitud de subsidio", "monto": 25000},
    {"id": 5, "tipo": "Renovación de licencia", "monto": 1500},
]

with open("tramites_ejercicio.csv", "w", encoding="utf-8", newline="") as archivo:
    escritor = csv.DictWriter(archivo, fieldnames=["id", "tipo", "monto"])
    escritor.writeheader()
    escritor.writerows(tramites)

with open("tramites_ejercicio.csv", "r", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    total = 0
    for fila in lector:
        total += float(fila["monto"])

print("Total montos (desde CSV):", total)

# --- Parte 4 ---
montos = np.array([1500, 8000, 0, 25000, 1500])

print("Suma:", montos.sum())
print("Promedio:", montos.mean())
print("Máximo:", montos.max())
print("Mínimo:", montos.min())

promedio = montos.mean()
montos_sobre_promedio = montos[montos > promedio]
print("Montos sobre el promedio:", montos_sobre_promedio)
```

**Parte 5 (terminal):**

macOS / Linux:
```bash
ls
```

Windows (PowerShell):
```powershell
dir
```

Ambos deberían mostrar `notas.txt` y `tramites_ejercicio.csv` en el listado.

## Nota para el docente

En la Parte 3, remarcar que `fila["monto"]` al leer con `csv.DictReader` llega **siempre como texto** (string), aunque en el CSV se vea como número — por eso es necesario convertirlo con `float()` antes de sumarlo. Este es un anticipo directo de un problema real que van a encontrar en Pandas: los tipos de datos al leer un archivo no siempre son los esperados.
