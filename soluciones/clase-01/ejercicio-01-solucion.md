# Solución — Ejercicio 1 (Clase 1)

## Parte 1 — Crear el proyecto

```bash
mkdir ejercicio-clase-01
cd ejercicio-clase-01
code .
```

(`code .` abre la carpeta actual en VS Code; también se puede hacer desde `File > Open Folder`.)

## Parte 2 — Entorno virtual

```bash
python -m venv venv
```

Activar:

```bash
# Windows (PowerShell)
venv\Scripts\Activate.ps1

# macOS / Linux
source venv/bin/activate
```

La terminal debería mostrar algo como:

```
(venv) usuario@computadora ejercicio-clase-01 %
```

## Parte 3 — Instalar un paquete

```bash
pip install requests
pip list
```

Salida esperada (puede variar la versión):

```
Package            Version
------------------- -------
requests            2.31.0
...
```

## Parte 4 — Primer script

Archivo `mi_primer_script.py`:

```python
nombre_curso = "Python para Análisis de Datos"
print("Bienvenido/a al curso:", nombre_curso)
print("Este script se está ejecutando dentro de un entorno virtual.")
```

Ejecución:

```bash
python mi_primer_script.py
```

Salida esperada:

```
Bienvenido/a al curso: Python para Análisis de Datos
Este script se está ejecutando dentro de un entorno virtual.
```

## Parte 5 — Para pensar

```python
# Si comparto este script con alguien que no tiene "requests" instalado,
# el script fallaría en cuanto intente hacer "import requests", con un
# error de tipo ModuleNotFoundError.
#
# El entorno virtual no resuelve esto automáticamente por sí solo, pero
# permite dejar registradas (más adelante, con un archivo de requerimientos)
# exactamente las dependencias que el proyecto necesita, para que
# cualquier persona pueda recrear el mismo entorno con los mismos paquetes
# y versiones, evitando el clásico "en mi máquina funciona".
```

## Nota para el docente

Si algún alumno llega con el error de `ModuleNotFoundError: No module named 'requests'` al ejecutar el script, lo más probable es que el entorno virtual no esté activado en la terminal donde se ejecuta el script — es un buen momento para reforzar que la activación es **por sesión de terminal**, no persiste automáticamente.
