# Puesta al día — Clase 1 (para quienes se suman ahora)

Este documento es para vos si te sumaste al curso **después** de la primera clase. Te va a dejar al mismo nivel que tus compañeros: qué se vio, cómo, y con ejercicios para practicar cada parte. Además, incluye un adelanto de **condicionales** (contenido de la Clase 2) para que no te falte nada importante si la próxima clase avanza rápido.

No hace falta que hayas visto la clase grabada para usar este documento — está pensado para ser autosuficiente. Andá siguiendo el orden, probando cada cosa en tu computadora antes de pasar a la siguiente.

> 💡 A lo largo del curso vamos a usar **Cursor** (un editor basado en VS Code, con asistente de IA integrado) o **VS Code** directamente — cualquiera de los dos sirve igual para todo lo que sigue. Si ya tenés uno de los dos instalado, no hace falta que cambies.

---

## 1. ¿Qué es programar?

Programar es, en esencia, **darle órdenes a la computadora**: escribir instrucciones en un lenguaje que la máquina puede entender, para que ejecute una acción por nosotros.

Ya le damos órdenes a una computadora todo el tiempo con Excel o con SPSS. La diferencia con programar es el nivel de flexibilidad: las herramientas con botones (Excel, SPSS, cualquier herramienta *low-code*) están pensadas para casos generales, y muchas veces **no llegan** a cubrir necesidades específicas de nuestro trabajo — sobre todo cuando trabajamos con datos particulares, como registros administrativos, que rara vez calzan perfecto en una herramienta genérica.

Programar nos da control total: en vez de esperar a que una herramienta piense en nuestro caso, construimos nosotros la solución.

---

## 2. ¿Qué es Python?

Python es un lenguaje de programación cuya característica principal es ser **simple y legible**, parecido al lenguaje natural. Es un lenguaje **interpretado**: cuando ejecutamos un script de Python, la computadora lo lee y ejecuta **línea por línea**, de arriba hacia abajo.

### ¿Por qué Python para trabajar con datos?

- Es sencillo de aprender — muchas personas que trabajamos en datos no venimos de una carrera de tecnología, y eso ayuda.
- Al ser popular, tiene un ecosistema enorme de librerías ya hechas (como **Pandas**, que vamos a usar mucho) y una comunidad gigante — si te trabás con algo, es muy probable que alguien ya haya tenido el mismo problema.
- Con el mismo lenguaje podemos leer datos, transformarlos, automatizar tareas y hasta construir dashboards. No hace falta aprender una herramienta distinta para cada cosa.

---

## 3. La terminal

La terminal es una forma de interactuar con la computadora **escribiendo comandos**, en vez de hacer clic en íconos. Da un poco de respeto al principio, pero se le agarra la mano rápido — y es imprescindible: muchas herramientas (como Git, o los entornos virtuales que vamos a ver más adelante) **solo se manejan por terminal**.

### Comandos básicos

| Acción | Windows (PowerShell) | macOS / Linux |
|---|---|---|
| Ver en qué carpeta estoy | `pwd` (o se ve en el prompt) | `pwd` |
| Listar archivos de la carpeta | `dir` | `ls` |
| Cambiar de carpeta | `cd nombre_carpeta` | `cd nombre_carpeta` |
| Subir un nivel de carpeta | `cd ..` | `cd ..` |
| Crear una carpeta | `mkdir nombre` | `mkdir nombre` |
| Ver el contenido de un archivo | `type nombre.txt` | `cat nombre.txt` |

> ⚠️ El error más común al usar la terminal (le pasa a todo el mundo, no solo a quien empieza) es **no estar parado en la carpeta correcta**. Si un comando no funciona, lo primero que hay que chequear es dónde estás parado (`pwd` o `dir`/`ls` para ver qué hay ahí).

### Ejecutar un archivo de Python

Con un archivo `saludo.py` que contiene:

```python
print("Hola mundo")
```

Desde la terminal, **parados en la carpeta donde está el archivo**:

```bash
# Windows
python saludo.py

# macOS / Linux
python3 saludo.py
```

En Mac/Linux se usa `python3` en vez de `python` — es una convención de esos sistemas, no un error.

### Chequear que Python está instalado

```bash
# Windows
python --version

# macOS / Linux
python3 --version
```

Esto también sirve como primer chequeo rápido de que todo está instalado correctamente.

### Un detalle importante: la extensión del archivo

Un archivo de código Python **siempre** debe guardarse con extensión `.py` (no `.txt`). Técnicamente Python puede ejecutar un `.txt` con código adentro, pero el editor de texto no va a saber que es código: no te va a marcar errores, ni te va a ayudar con el resaltado de sintaxis, ni nada. Por convención y por practicidad: **siempre `.py`**.

---

## 4. Cursor / VS Code: las tres partes básicas

Cualquier editor de código (Cursor, VS Code, y prácticamente todos desde hace muchos años) tiene tres zonas principales:

1. **El explorador de archivos** (generalmente a la izquierda): la lista de archivos y carpetas de tu proyecto.
2. **El editor** (el centro): donde escribís el código.
3. **La terminal** (generalmente abajo): se abre con `Terminal > New Terminal` (o el ícono correspondiente), y es donde ejecutás los comandos que vimos en la sección anterior.

Cursor, además, agrega un **chat con un agente de IA** (generalmente a la derecha), con el que podés pedirle ayuda para escribir o entender código. Vamos a hablar de esto en detalle en su momento — por ahora, alcanza con saber que existe.

### Markdown, de paso

Los archivos `.md` del material del curso (como este mismo documento) están escritos en **Markdown**: un lenguaje simple donde ciertos símbolos le dan formato al texto (por ejemplo, `#` hace un título, `**texto**` lo pone en negrita). Si en VS Code/Cursor abrís un `.md` y se ve "crudo" (con todos los símbolos), podés hacer clic derecho sobre la pestaña del archivo y elegir **"Open Preview"** para verlo ya formateado, como una página normal.

---

## 5. Script vs. Jupyter Notebook

Un **script** (archivo `.py`) es un archivo de texto plano con código, sin ninguna estructura especial: la computadora lo lee y ejecuta todo, de punta a punta, en una sola pasada. Todo lo que querés ver en pantalla tenés que imprimirlo explícitamente con `print(...)` — si no, no aparece nada.

Un **Jupyter Notebook** (archivo `.ipynb`) es distinto: está organizado en **celdas**, que podés ejecutar una por una, en el orden que quieras, viendo el resultado de cada una inmediatamente. Hay dos tipos de celda:

- **Celdas de Markdown**: para escribir texto (títulos, explicaciones), igual que en este documento.
- **Celdas de código**: para escribir y ejecutar Python.

### ¿Por qué existen los dos, si Notebook parece más cómodo?

Porque cada uno sirve para un momento distinto del trabajo:

- **Notebook** es ideal para **explorar** datos: ir probando cosas de a poco, ver resultados al instante, corregir sobre la marcha. Es mucho más amigable para el análisis del día a día.
- **Script** es necesario cuando el proceso ya está maduro y hay que **ejecutarlo de punta a punta**, por ejemplo de forma automática o remota (algo que un Notebook, al necesitar que alguien lo abra y ejecute celda por celda, no puede hacer tan fácilmente).

El flujo de trabajo típico de un analista suele ser: **explorar primero en un Notebook**, y una vez que sabés exactamente qué transformación necesitás, **pasarlo a un script** para poder ejecutarlo de forma repetible y automática.

En este curso vamos a trabajar principalmente en notebooks (es donde vamos a pasar la mayor parte del tiempo, especialmente en los módulos de Pandas), y vamos a volver al formato script cuando lleguemos a construir dashboards.

### Cómo crear y usar un Jupyter Notebook en Cursor/VS Code

1. Creá un archivo nuevo con extensión `.ipynb` (por ejemplo, `mi_notebook.ipynb`).
2. Cursor/VS Code va a reconocer automáticamente que es un notebook y te va a mostrar la interfaz de celdas.
3. La primera vez que ejecutes una celda, es posible que te pida elegir un **kernel** (básicamente, qué instalación de Python vas a usar) — elegí la que tengas instalada.
4. Para agregar una celda nueva, hay un botón `+ Code` o `+ Markdown` (según el tipo que quieras) que aparece al pasar el mouse cerca de una celda existente, o arriba del todo.
5. Para ejecutar una celda: hacé clic en el triángulo (▶) que aparece a la izquierda de la celda, o pará el cursor en la celda y presioná `Shift + Enter` (ejecuta la celda actual y salta a la siguiente).
6. El resultado de una celda de código aparece **justo debajo** de ella, inmediatamente.
7. Podés ejecutar las celdas en el orden que quieras, y volver a ejecutar una celda anterior si corregiste algo — el notebook mantiene el resultado de la última vez que ejecutaste cada celda.

> 💡 Un consejo práctico: si algo empieza a comportarse raro en un notebook (por ejemplo, una variable "no se actualiza" como esperabas), muchas veces se debe a que ejecutaste las celdas en un orden distinto al que aparecen escritas. Ante la duda, podés reiniciar el kernel (buscá la opción "Restart Kernel" en la interfaz) y ejecutar todo de nuevo, de arriba hacia abajo.

---

## 6. ¿Qué es un paquete o librería?

Un paquete (o librería, se usan como sinónimos) es **código que alguien más ya escribió**, empaquetado para que lo podamos reutilizar sin tener que reinventarlo.

Ejemplo concreto: si quisiéramos leer un archivo CSV y convertirlo en una tabla usando solamente Python "de fábrica", tendríamos que escribir nosotros mismos toda la lógica para abrir el archivo, separar el contenido por comas, identificar qué es texto y qué es número, etc. Es **posible**, pero enormemente trabajoso y poco práctico.

En cambio, con la librería **Pandas** (la que vamos a usar durante todo el curso), leer un CSV se resuelve así:

```python
import pandas as pd

df = pd.read_csv("mi_archivo.csv")
print(df)
```

Las librerías son gratuitas y públicas — las escribió y las mantiene la comunidad de Python. La regla general es: **si existe una librería que ya resuelve lo que necesitás, usala** — no tiene sentido reinventar algo que ya está hecho y probado por miles de personas.

### Instalar una librería: `pip install`

Las librerías se descargan e instalan desde la terminal, con el comando `pip`:

```bash
pip install pandas
```

> 📶 Las librerías se descargan de internet, así que para instalar necesitás conexión. Si estás trabajando en un entorno con acceso restringido a internet, este es un punto para coordinar con tu equipo de informática antes de la próxima clase.

### Dos pasos, no uno: instalar Y llamar

Ojo con un punto importante: instalar una librería y usarla en tu código **son dos pasos distintos**.

1. **Instalarla** (una sola vez por computadora/proyecto): `pip install pandas` desde la terminal.
2. **Llamarla** (en cada script o notebook donde la vayas a usar): `import pandas as pd` al principio del archivo.

Si instalaste la librería pero te olvidaste del `import`, Python no sabe qué es `pd` y te va a tirar un error. Si hiciste el `import` pero nunca la instalaste, el error va a ser distinto (`No module named 'pandas'` o similar) — pero en ambos casos, la solución es asegurarte de haber hecho los dos pasos.

---

## 7. Entornos virtuales (opcional — podés saltear esta sección por ahora)

> Esta parte es **para tener una primera idea**, no hace falta que la domines ni que la uses todavía en los ejercicios. La vamos a retomar con más calma más adelante en el curso.

Un entorno virtual es una especie de "burbuja" aislada, donde las librerías que instalás quedan encerradas dentro de esa carpeta/proyecto en particular, sin mezclarse con las de otros proyectos en tu computadora.

¿Por qué importa? Porque puede pasar que un proyecto necesite la versión 1.0 de una librería, y otro proyecto necesite la versión 2.0 de esa misma librería. Sin entornos virtuales, esas dos versiones "se pisan" en tu computadora. Con un entorno virtual por proyecto, cada uno tiene sus propias versiones, sin conflicto.

Por ahora, si no usaste todavía un entorno virtual, no hay ningún problema — podés seguir instalando paquetes de forma normal (`pip install pandas`, por ejemplo) y avanzar con el resto de los ejercicios sin inconveniente.

---

## Ejercicios para practicar

Hacé estos ejercicios en orden. Están pensados para que repliques, con tus propias manos, todo lo que vimos arriba.

### Ejercicio A — Terminal y tu primer script

1. Desde la terminal, creá una carpeta llamada `puesta-al-dia` (`mkdir puesta-al-dia`).
2. Entrá a esa carpeta (`cd puesta-al-dia`).
3. Abrí esa carpeta en Cursor o VS Code.
4. Desde el editor, creá un archivo llamado `saludo.py` con el siguiente contenido:
   ```python
   print("Hola, este es mi primer script")
   ```
5. Abrí la terminal integrada del editor (`Terminal > New Terminal`) y ejecutalo:
   ```bash
   # Windows
   python saludo.py

   # macOS / Linux
   python3 saludo.py
   ```
6. Confirmá que ves el mensaje en la terminal.

### Ejercicio B — Provocar y entender un error

Este ejercicio es a propósito para que veas un error común y aprendas a leerlo — no te preocupes si te pasa, es exactamente la idea.

1. En el mismo archivo `saludo.py`, escribí esta línea (fijate que le falta algo, es intencional):
   ```python
   print("Esta línea tiene un error
   ```
2. Guardá y ejecutalo. Vas a ver un error de sintaxis.
3. Leé el mensaje de error con atención — te va a decir en qué línea está el problema. Corregilo (falta cerrar las comillas) y volvé a ejecutar.

### Ejercicio C — Tu primer Jupyter Notebook

1. En la misma carpeta, creá un archivo llamado `practica.ipynb`.
2. Agregá una celda de Markdown con un título, por ejemplo: `# Mi primera práctica`.
3. Agregá una celda de código con:
   ```python
   print("Este es un notebook")
   ```
4. Ejecutá ambas celdas (con el botón ▶ o `Shift + Enter`) y confirmá que ves el resultado debajo de la celda de código.
5. Agregá una tercera celda de código que calcule e imprima el resultado de `15 * 3`.

### Ejercicio D — Instalar y usar una librería

1. Desde la terminal, instalá la librería `pandas`:
   ```bash
   pip install pandas
   ```
2. Creá un archivo `datos.csv` (podés hacerlo desde el editor) con este contenido exacto:
   ```
   id,nombre,edad
   1,Daniel,34
   2,Amalia,26
   3,Héctor,45
   4,Sonia,70
   ```
3. En tu notebook `practica.ipynb` (o en un script nuevo, como prefieras), agregá:
   ```python
   import pandas as pd

   df = pd.read_csv("datos.csv")
   print(df)
   ```
4. Ejecutalo y confirmá que ves la tabla completa impresa.

### Ejercicio E — Adelanto: condicionales

> A partir de acá, contenido que corresponde a la próxima clase — un adelanto para que no llegues de cero.

Los condicionales le permiten a tu código **tomar decisiones**: ejecutar una cosa u otra, según se cumpla o no una condición.

```python
edad = 20

if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")
```

Puntos clave:
- `if` seguido de una condición, y **dos puntos** (`:`) al final de esa línea.
- Lo que va **indentado** (con sangría) debajo del `if` es lo que se ejecuta si la condición es verdadera.
- `else` (opcional) cubre el caso contrario.
- `==` compara si dos cosas son iguales; `=` asigna un valor. Son cosas **distintas** — confundirlos es el error más común al empezar con condicionales.

También se pueden encadenar varias condiciones con `elif` ("else if"):

```python
edad = 15

if edad >= 65:
    print("Adulto mayor")
elif edad >= 18:
    print("Adulto")
else:
    print("Menor de edad")
```

Python evalúa las condiciones **en orden**, de arriba hacia abajo, y ejecuta la primera que se cumpla.

**Ejercicio práctico:** usando el `df` que creaste en el Ejercicio D, escribí un condicional que revise la edad de la primera persona de la tabla (pista: `df["edad"][0]` te da ese valor) y que imprima `"Mayor de edad"` o `"Menor de edad"` según corresponda. Si te sentís con ganas, probá también con `elif` agregando una categoría para `"Adulto mayor"` (65 años o más).

---

## ¿Y ahora?

Con esto ya estás al día con lo que vio el resto del grupo en la primera clase, más un adelanto de condicionales. Cualquier duda, preguntala apenas arranque la próxima clase — es totalmente normal tener preguntas en esta etapa, es la parte más densa del curso en términos de conceptos nuevos de una sola vez.
