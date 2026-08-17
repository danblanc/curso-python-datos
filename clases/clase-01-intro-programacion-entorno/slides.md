---
marp: true
theme: default
paginate: true
size: 16:9
---

# Clase 1
## Introducción a la programación y configuración del entorno

Curso de Python para Análisis de Datos

---

# Agenda de hoy

1. ¿Qué es programar? ¿Qué es Python?
2. La terminal
3. VS Code y Jupyter Notebook
4. Paquetes y librerías
5. Entornos virtuales
6. Ejercicio práctico

---

# ¿Qué es programar?

Programar es **escribir instrucciones** para que una computadora las ejecute, paso a paso.

Un **algoritmo** es una secuencia ordenada de pasos para resolver un problema.

Un **lenguaje de programación** es la forma en que escribimos esas instrucciones de manera que:
- una persona pueda leerlas y entenderlas,
- una computadora pueda traducirlas a algo que puede ejecutar.

---

# ¿Qué es Python?

- Lenguaje de programación creado por **Guido van Rossum** (1991).
- Se destaca por su **sintaxis simple y legible** (parecida al lenguaje natural).
- Es un lenguaje **interpretado**: no se compila a un ejecutable, se ejecuta línea por línea mediante un programa llamado *intérprete*.
- Es el lenguaje más usado hoy en **análisis de datos, ciencia de datos y automatización**.

---

# Interpretado vs. compilado (idea general)

**Compilado** (ej: C, C++)
Todo el código se traduce a lenguaje de máquina *antes* de ejecutarse, generando un archivo ejecutable.

**Interpretado** (ej: Python)
El código se traduce y ejecuta línea por línea, en el momento, mediante un intérprete.

> Consecuencia práctica: con Python no "compilamos" nada, directamente ejecutamos el archivo `.py` y el intérprete hace el resto.

---

# ¿Por qué Python para datos?

- Sintaxis simple → curva de aprendizaje más corta
- Enorme ecosistema de librerías: **Pandas, NumPy, Matplotlib, Seaborn, Streamlit** (todo lo que vamos a usar en este curso)
- Comunidad enorme → fácil encontrar ayuda y documentación
- Mismo lenguaje sirve para automatizar tareas, analizar datos, construir dashboards, y mucho más

---

# La terminal

La **terminal** (o consola/línea de comandos) es una forma de interactuar con la computadora escribiendo comandos de texto, en vez de hacer clic en íconos.

¿Por qué la usamos en programación?
- Es la forma más directa de ejecutar código
- Muchas herramientas (Git, entornos virtuales, `pip`) se manejan por terminal
- Es más rápida una vez que le agarrás la mano

---

# Comandos básicos de terminal

| Acción | Windows (PowerShell) | macOS / Linux |
|---|---|---|
| Ver carpeta actual | `pwd` (o se ve en el prompt) | `pwd` |
| Listar archivos | `dir` | `ls` |
| Cambiar de carpeta | `cd nombre_carpeta` | `cd nombre_carpeta` |
| Subir un nivel | `cd ..` | `cd ..` |
| Crear carpeta | `mkdir nombre` | `mkdir nombre` |

---

# Ejecutar un script de Python

Con un archivo `saludo.py` que contiene:

```python
print("Hola, mundo")
```

Desde la terminal, parados en la carpeta donde está el archivo:

```bash
python saludo.py
```

En macOS/Linux, si `python` no funciona, probar `python3 saludo.py`.

---

# VS Code vs. Jupyter Notebook

**VS Code** (editor de código)
- Ideal para escribir **scripts** (`.py`): programas completos, reutilizables, pensados para ejecutarse de punta a punta.
- Mejor para organizar proyectos con varios archivos.

**Jupyter Notebook** (`.ipynb`)
- Ideal para **exploración**: ejecutar código de a partes ("celdas"), ver resultados inmediatos, iterar rápido.
- Muy usado en análisis de datos exploratorio.

---

# ¿Cuál uso yo?

En este curso vamos a usar **ambos**, según el momento:

- **Notebooks** → cuando estemos explorando datos, probando cosas, viendo resultados paso a paso (gran parte de las clases de Pandas).
- **Scripts** → cuando el código ya está más maduro y necesita ejecutarse como un programa completo (por ejemplo, nuestras apps de Streamlit).

No es "uno mejor que el otro": son herramientas para momentos distintos.

---

# ¿Qué es un paquete / librería?

Es **código ya escrito por otras personas**, empaquetado para que lo podamos reutilizar sin reinventarlo.

Ejemplo: en vez de programar nosotros mismos toda la lógica para leer un Excel, usamos la librería **Pandas**, que ya lo resuelve.

```python
import pandas as pd

df = pd.read_excel("archivo.xlsx")
```

---

# Instalar paquetes con `pip`

`pip` es el gestor de paquetes de Python. Se usa desde la terminal:

```bash
pip install pandas
```

Esto descarga el paquete desde **PyPI** (Python Package Index, el repositorio oficial de paquetes de Python) y lo deja disponible para usar con `import`.

---

# El problema sin entornos virtuales

Imaginá que:
- El **Proyecto A** necesita la versión 1.0 de una librería.
- El **Proyecto B** necesita la versión 2.0 de esa misma librería.

Si instalás los paquetes "globalmente" (para toda la computadora), **no podés tener las dos versiones a la vez** sin que se pisen entre sí.

---

# ¿Qué es un entorno virtual?

Un **entorno virtual** es una "burbuja" aislada con su propia instalación de Python y sus propios paquetes, independiente del resto de la computadora.

Cada proyecto puede tener su propio entorno virtual, con exactamente las versiones de librerías que necesita — sin interferir con otros proyectos.

---

# Por qué es una buena práctica

- **Aislamiento:** evita conflictos de versiones entre proyectos
- **Reproducibilidad:** cualquier persona puede recrear el mismo entorno (mismas versiones) a partir de una lista de dependencias
- **Orden:** queda claro qué necesita cada proyecto para funcionar

En este curso, **todos los proyectos van a trabajar dentro de un entorno virtual**, como práctica desde el día 1.

---

# Crear y activar un entorno virtual

**Crear** (una sola vez, dentro de la carpeta del proyecto):
```bash
python -m venv venv
```

**Activar:**

```bash
# Windows (PowerShell)
venv\Scripts\Activate.ps1

# macOS / Linux
source venv/bin/activate
```

Vas a ver `(venv)` al inicio de la línea de la terminal — indica que está activo.

---

# Instalar paquetes dentro del entorno

Con el entorno activado:

```bash
pip install pandas numpy
```

Estos paquetes quedan instalados **solo dentro de ese entorno virtual**, no en toda la computadora.

Para salir del entorno:
```bash
deactivate
```

---

# Resumen de la clase

- Programar = dar instrucciones; Python = lenguaje interpretado, simple, ideal para datos
- La terminal es la forma directa de ejecutar código y manejar herramientas
- VS Code para scripts, Jupyter para exploración
- Los paquetes se instalan con `pip install`
- Los entornos virtuales aíslan las dependencias de cada proyecto

---

# Ejercicio práctico

30-40 minutos — ver [`ejercicios/ejercicio-01.md`](./ejercicios/ejercicio-01.md)

Vamos a:
1. Crear una carpeta de proyecto
2. Crear y activar un entorno virtual
3. Instalar un paquete
4. Escribir y ejecutar un script simple
