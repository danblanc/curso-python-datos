# Guía de instalación del entorno

Esta guía debe completarse **antes de la Clase 1**. El objetivo es llegar a la primera clase con Python y el editor de código ya instalados, para no perder tiempo de clase en instalaciones.

## 1. Instalar Python

### Windows

1. Ir a [python.org/downloads](https://www.python.org/downloads/).
2. Descargar la última versión estable de Python 3 (3.11 o superior).
3. **Importante:** al ejecutar el instalador, marcar la casilla **"Add Python to PATH"** antes de hacer clic en "Install Now".
4. Verificar la instalación abriendo la terminal (buscar "cmd" o "PowerShell") y ejecutando:
   ```
   python --version
   ```

### macOS

1. Ir a [python.org/downloads](https://www.python.org/downloads/) y descargar el instalador para macOS.
2. Ejecutar el instalador `.pkg` y seguir los pasos.
3. Verificar en la Terminal:
   ```
   python3 --version
   ```

### Linux

La mayoría de las distribuciones ya traen Python 3 instalado. Verificar con:
```
python3 --version
```
Si no está instalado (Ubuntu/Debian):
```
sudo apt update && sudo apt install python3 python3-pip python3-venv
```

## 2. Instalar Visual Studio Code

1. Ir a [code.visualstudio.com](https://code.visualstudio.com/) y descargar la versión para tu sistema operativo.
2. Instalar siguiendo los pasos por defecto.
3. Abrir VS Code e instalar las siguientes extensiones (ícono de cuadrados en la barra lateral izquierda, o `Ctrl+Shift+X` / `Cmd+Shift+X`):
   - **Python** (de Microsoft)
   - **Jupyter** (de Microsoft)
   - **Marp for VS Code** (para visualizar las diapositivas del curso)

## 3. Verificar que todo funciona

1. Abrir VS Code.
2. Crear una carpeta nueva en tu computadora, por ejemplo `curso-python`.
3. Abrir esa carpeta en VS Code (`File > Open Folder`).
4. Crear un archivo llamado `prueba.py` con el siguiente contenido:
   ```python
   print("Hola, curso de Python")
   ```
5. Ejecutarlo: clic derecho sobre el archivo → "Run Python File in Terminal", o desde la terminal integrada de VS Code (`Terminal > New Terminal`):
   ```
   python prueba.py
   ```
   (en macOS/Linux puede ser `python3 prueba.py`)
6. Si ves el mensaje `Hola, curso de Python` en la terminal, la instalación está correcta.

## 4. Clonar (o descargar) el repositorio del curso

Si ya tenés Git instalado:
```
git clone <URL-del-repositorio>
```

Si no tenés Git instalado todavía, no hay problema: se puede descargar el repositorio como archivo ZIP directamente desde GitHub (botón verde "Code" → "Download ZIP") y descomprimirlo. Git se ve más adelante en el curso.

## Problemas comunes

| Problema | Solución |
|---|---|
| `python` no se reconoce como comando (Windows) | Reinstalar Python marcando "Add Python to PATH", o agregar la ruta manualmente a las variables de entorno |
| En macOS/Linux `python` no funciona pero `python3` sí | Es normal, usar `python3` y `pip3` en su lugar |
| VS Code no detecta el intérprete de Python | `Ctrl+Shift+P` / `Cmd+Shift+P` → "Python: Select Interpreter" → elegir la versión instalada |

## Cualquier duda

Traer las dudas de instalación al inicio de la Clase 1 — se dedican los primeros minutos a resolver problemas de entorno antes de arrancar con contenido.
