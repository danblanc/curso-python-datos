---
marp: true
theme: default
paginate: true
size: 16:9
---

# Clase 10b
## De notebook a informe: Quarto

Curso de Python para Análisis de Datos

---

# Agenda de hoy

1. El problema: tengo un notebook, necesito un informe
2. Instalar Quarto
3. Renderizar un notebook a HTML y PDF
4. Mostrar u ocultar el código
5. Introducción a `.qmd`
6. Ejercicio práctico

---

# El problema

Después de la Clase 10 ya sabés generar gráficos dentro de un notebook. Pero un notebook:

- Mezcla código, resultados y (a veces) errores de prueba
- No está pensado para entregarle algo prolijo a alguien que no programa
- No se exporta fácilmente a un PDF prolijo

Necesitamos una forma de convertir ese mismo trabajo en un **informe presentable**.

---

# ¿Qué es Quarto?

Una herramienta que toma un notebook (o un archivo de texto especial) y lo convierte en un documento final: HTML, PDF, Word, y más.

Lo más importante para hoy: **puede tomar el `.ipynb` que ya tenés, tal cual, sin que tengas que reescribir nada**.

---

# Instalación

**Windows:**
Descargar el instalador desde [quarto.org/docs/get-started](https://quarto.org/docs/get-started/) y ejecutarlo (como cualquier instalador de Windows).

**macOS:**
Descargar el instalador `.pkg` del mismo sitio, o `brew install quarto` si usás Homebrew.

Verificar que funcionó:
```bash
quarto --version
```

---

# Extensión para VS Code / Cursor

Instalá la extensión **Quarto** — misma lógica que ya usás con la extensión **Marp** para ver las slides. Te da resaltado de sintaxis y un botón de "Render" directo desde el editor.

---

# Renderizar un notebook a HTML

Con un notebook `informe.ipynb` que ya tiene tus gráficos de la Clase 10:

```bash
quarto render informe.ipynb --to html
```

Esto genera `informe.html` — abrilo con cualquier navegador.

---

# ⚠️ Un detalle importante

Quarto **no vuelve a ejecutar tu notebook por defecto** — usa los resultados que ya están guardados adentro del archivo `.ipynb`.

**Esto significa:** antes de renderizar, asegurate de haber corrido todas las celdas (`Run All`) y guardado el notebook. Si no, el informe va a salir sin gráficos ni resultados.

Si querés forzar que Quarto vuelva a ejecutar todo desde cero:

```bash
quarto render informe.ipynb --to html --execute
```

---

# Renderizar a PDF

```bash
quarto render informe.ipynb --to pdf
```

Para que esto funcione, Quarto necesita un motor LaTeX instalado (se usa por dentro para armar el PDF). Se instala una sola vez:

```bash
quarto install tinytex
```

> Esta instalación pesa varios cientos de MB y necesita internet en el momento de instalar — si falla en una red restringida, HTML es la alternativa sin esta dependencia.

---

# Ocultar el código: la forma más simple

Sin tocar el notebook para nada, desde la terminal:

```bash
quarto render informe.ipynb --to html -M echo:false
```

`-M` le pasa una opción de configuración a Quarto en el momento de renderizar. `echo:false` oculta todo el código, dejando solo el texto y los resultados (gráficos, tablas).

---

# Código plegable (solo tiene sentido en HTML)

```bash
quarto render informe.ipynb --to html -M code-fold:true
```

El código no desaparece: queda **colapsado**, con un botón "Code" para desplegarlo si alguien quiere revisarlo.

En PDF no aplica (un PDF no tiene botones interactivos) — ahí la opción es mostrar el código entero, o directamente `echo:false` para ocultarlo del todo.

---

# Control más fino: metadatos dentro del notebook

Si no querés depender de pasar opciones por la terminal cada vez, podés agregar una **celda de tipo "Raw"** al principio del notebook con:

```yaml
---
title: "Informe de trámites administrativos"
author: "Tu nombre"
format:
  html:
    code-fold: true
  pdf:
    echo: false
---
```

Esto define título, autor, y **opciones distintas según el formato de salida** — podés tener el código plegado en HTML pero completamente oculto en PDF, a partir del mismo notebook.

---

# Control por celda individual

Dentro de una celda de código específica, la primera línea puede llevar una opción que aplica **solo a esa celda**:

```python
#| echo: false
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("tramites_personas_combinado.csv")
```

Útil para ocultar, por ejemplo, los imports y la carga de datos (poco interesante para el lector), pero dejar visible el código de un gráfico puntual que sí querés mostrar.

---

# Repaso de las tres formas de controlar el código

| Forma | Alcance | Dónde se define |
|---|---|---|
| `-M echo:false` | Todo el documento | Comando de terminal |
| YAML en celda Raw | Todo el documento, por formato | Dentro del notebook |
| `#| echo: false` | Una celda puntual | Dentro de esa celda |

Podés combinarlas: un default general en el YAML, con excepciones puntuales por celda.

---

# Introducción a `.qmd`

Un archivo `.qmd` es, en esencia, **lo mismo que venimos haciendo**, pero en un archivo de texto plano en vez de un notebook — sin la estructura de celdas de Jupyter.

```markdown
---
title: "Informe de trámites administrativos"
format:
  html:
    code-fold: true
---

## Carga de datos

​```{python}
#| echo: false
import pandas as pd
df = pd.read_csv("tramites_personas_combinado.csv")
​```
```

---

# Anatomía de un `.qmd`

- El bloque `---` ... `---` al principio es el mismo YAML que vimos en la celda Raw del notebook.
- El texto normal es Markdown (títulos con `#`, negrita con `**texto**`), igual que en las celdas de Markdown de un notebook.
- Los bloques de código van entre ```` ```{python} ```` y ```` ``` ````, con las mismas opciones `#|` que ya usamos.

---

# Renderizar un `.qmd`

Exactamente el mismo comando que con un notebook:

```bash
quarto render informe.qmd --to html
quarto render informe.qmd --to pdf
```

No hace falta el flag `--execute`: un `.qmd` siempre se ejecuta al renderizar (no tiene "resultados guardados" como un notebook, porque no es un notebook).

---

# `.ipynb` vs. `.qmd`: ¿cuándo uso cada uno?

| Situación | Conviene... |
|---|---|
| Ya tenés todo el análisis armado en un notebook | Exportar el `.ipynb` directamente |
| Vas a escribir el informe desde cero, pensado para publicarse | `.qmd` |
| Necesitás explorar datos de forma interactiva, celda por celda | Notebook (`.ipynb`) |
| El documento final es lo único que importa, no el proceso exploratorio | `.qmd` |

No es una decisión de una sola vez para todo el curso — es común explorar en notebook y, si el resultado va a convertirse en un informe recurrente, migrar después a `.qmd`.

---

# Resumen de la clase

- Quarto exporta notebooks existentes a HTML/PDF sin reescribir nada
- Ojo: por defecto usa los resultados ya guardados, no re-ejecuta el notebook
- El código se puede ocultar (`echo:false`) o plegar (`code-fold:true`), a nivel documento o por celda
- `.qmd` es la misma lógica en un archivo de texto plano, útil para informes escritos desde cero

---

# Ejercicio práctico

~20-25 minutos — ver [`ejercicios/ejercicio-10b-quarto.md`](./ejercicios/ejercicio-10b-quarto.md)
