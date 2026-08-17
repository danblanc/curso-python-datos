# Ejercicio 1 — Configurando mi primer proyecto

**Duración estimada:** 30-40 minutos

## Objetivo

Practicar de punta a punta el flujo que vamos a usar durante todo el curso: crear un proyecto, aislar sus dependencias en un entorno virtual, instalar un paquete, y ejecutar un script.

## Consigna

### Parte 1 — Crear el proyecto

1. Desde la terminal, creá una carpeta llamada `ejercicio-clase-01` (podés usar `mkdir` o crearla desde el explorador de archivos).
2. Abrí esa carpeta en VS Code.
3. Abrí la terminal integrada de VS Code (`Terminal > New Terminal`).

### Parte 2 — Entorno virtual

4. Creá un entorno virtual llamado `venv` dentro de la carpeta del proyecto.
5. Activalo. Confirmá que ves `(venv)` al inicio de la línea de la terminal.

### Parte 3 — Instalar un paquete

6. Con el entorno activado, instalá el paquete `requests` (lo vamos a usar más adelante en el curso):
   ```bash
   pip install requests
   ```
7. Verificá que se instaló correctamente ejecutando:
   ```bash
   pip list
   ```
   Deberías ver `requests` en la lista.

### Parte 4 — Primer script

8. Creá un archivo llamado `mi_primer_script.py` con el siguiente contenido:
   ```python
   nombre_curso = "Python para Análisis de Datos"
   print("Bienvenido/a al curso:", nombre_curso)
   print("Este script se está ejecutando dentro de un entorno virtual.")
   ```
9. Ejecutalo desde la terminal (con el entorno virtual activado):
   ```bash
   python mi_primer_script.py
   ```
10. Confirmá que ves los dos mensajes impresos en la terminal.

### Parte 5 — Para pensar (no requiere código)

Respondé brevemente, en un comentario al final del mismo archivo `.py` (usando `#` al inicio de la línea):

- ¿Qué pasaría si compartís este script con un compañero que no tiene el paquete `requests` instalado en su computadora?
- ¿Para qué sirve, entonces, tener el entorno virtual asociado a este proyecto en particular?

## Qué se evalúa

- Que el entorno virtual se haya creado y activado correctamente.
- Que el paquete se haya instalado dentro del entorno (no de forma global).
- Que el script se ejecute sin errores y muestre la salida esperada.

## Ayuda

Si te trabás en algún paso, revisá la [guía de instalación](../../../recursos-generales/instalacion-entorno.md) o las slides de la clase. La solución de referencia está en [`soluciones/clase-01/`](../../../soluciones/clase-01/).
