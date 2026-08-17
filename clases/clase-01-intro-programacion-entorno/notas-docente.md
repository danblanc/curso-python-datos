# Notas del docente — Clase 1

Guion orientativo con timing sugerido para las 2 horas. No es un libreto rígido — ajustar según cómo responda el grupo.

## Timing sugerido

| Bloque | Tiempo | Contenido |
|---|---|---|
| 1 | 10 min | Apertura, resolución de problemas de instalación pendientes |
| 2 | 15 min | Qué es programar / qué es Python (slides 3-6) |
| 3 | 20 min | Terminal: demo en vivo, no solo slides (slides 7-10) |
| 4 | 15 min | VS Code vs. Jupyter — demo abriendo ambos (slides 11-12) |
| 5 | 15 min | Paquetes y `pip` (slides 13-14) |
| 6 | 20 min | Entornos virtuales — demo en vivo creando uno (slides 15-18) |
| 7 | 5 min | Resumen (slide 19) |
| 8 | 35-40 min | Ejercicio práctico guiado |

## Tips de dictado

- **Bloque 1 (apertura):** siempre va a haber alguien con problemas de instalación. No dedicar más de 10 min en grupo — a quien le falte algo, anotar y resolver en paralelo o al final, para no frenar al resto.

- **Bloque 3 (terminal):** esto es lo que más ansiedad genera a quien nunca programó. No apurar. Hacer la demo compartiendo pantalla y pedir que todos repitan los comandos en simultáneo (`cd`, `ls`/`dir`, crear una carpeta). Insistir en que "no rompen nada" navegando con la terminal.

- **Bloque 4 (VS Code vs Jupyter):** mostrar ambos en vivo con el mismo ejemplo (`print("hola")`) — que vean la diferencia de experiencia, no solo la teoría.

- **Bloque 6 (entornos virtuales):** es el concepto más abstracto de la clase. Usar la analogía de "cajas separadas" o "departamentos aislados" — cada proyecto vive en su propia caja con sus propias herramientas. Hacer la creación del entorno en vivo, paso a paso, y que todos lo repliquen antes de seguir. Este es el bloque donde más se atrasa el grupo — está contemplado en el timing.

- Si el grupo viene con algo de experiencia previa (algunos "ya usaron Python en la facultad"), este es el momento de detectarlo — va a ser útil para calibrar el ritmo de las próximas clases y saber si en algún momento conviene usar el comodín de Git.

## Errores comunes a anticipar

- Windows: PowerShell puede bloquear la ejecución de scripts de activación del entorno virtual (`Activate.ps1`) por política de ejecución. Si pasa, alternativa rápida: usar `cmd` en vez de PowerShell, o ejecutar `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned` (explicar que es una config local, no algo riesgoso).
- macOS: confundir `python` con `python3`. Aclarar desde el vamos que en Mac/Linux se usa `python3` y `pip3`.
- Confusión entre "abrir una carpeta en VS Code" y "abrir un archivo suelto" — insistir en que siempre trabajamos abriendo la **carpeta del proyecto**, no archivos sueltos.

## Cierre

Antes de terminar, confirmar que todos lograron:
1. Crear un entorno virtual
2. Activarlo (ver el `(venv)` en la terminal)
3. Instalar al menos un paquete dentro de él

Si alguien no llegó, es el primer punto a resolver al inicio de la Clase 2.
