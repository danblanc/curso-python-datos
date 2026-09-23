# Solución — Ejercicio 10b (Quarto)

> Todos los comandos de esta solución fueron probados de punta a punta (instalación real de Quarto, TinyTeX vía apt, render a HTML y PDF) antes de escribirse.

## Parte 1 — Primer render

```bash
quarto render tu_notebook.ipynb --to html
```

Esto genera `tu_notebook.html` en la misma carpeta, junto con una carpeta `tu_notebook_files/` que contiene las imágenes de los gráficos y los archivos de estilo. Abriendo el `.html`, los gráficos deberían verse igual que en el notebook original.

## Parte 2 — El error típico

Al modificar el código de una celda **sin volver a ejecutarla**, y renderizar de nuevo con:

```bash
quarto render tu_notebook.ipynb --to html
```

**El cambio NO aparece en el informe.** Esto es así porque Quarto, por defecto, no vuelve a ejecutar el notebook: toma los resultados que ya están guardados dentro del archivo `.ipynb` (el output de la última vez que corriste esa celda), no el código tal como está escrito ahora.

Al agregar `--execute`:

```bash
quarto render tu_notebook.ipynb --to html --execute
```

Ahora sí, Quarto vuelve a ejecutar **todas** las celdas del notebook desde cero, y el cambio aparece reflejado en el informe.

**Conclusión práctica:** si vas a modificar un notebook y renderizarlo, la forma más segura es usar `Run All` en el editor antes de renderizar, o directamente agregar `--execute` al comando — así no dependés de acordarte de re-ejecutar manualmente.

## Parte 3 — PDF

```bash
quarto render tu_notebook.ipynb --to pdf
```

Si `quarto install tinytex` no se pudo completar (por ejemplo, por restricciones de red), Quarto va a devolver un error indicando que no encuentra un motor LaTeX. En ese caso, HTML sigue siendo un resultado completamente válido para el resto del ejercicio.

## Parte 4 — Controlar la visibilidad del código

**Ocultar todo el código, sin tocar el notebook:**
```bash
quarto render tu_notebook.ipynb --to html -M echo:false
```

**Código plegado pero disponible:**
```bash
quarto render tu_notebook.ipynb --to html -M code-fold:true
```
Al abrir el resultado, cada bloque de código aparece colapsado bajo un texto "Code" — haciendo clic se despliega y se puede leer con normalidad.

**YAML en una celda Raw**, agregada al principio del notebook:
```yaml
---
title: "Mi informe de trámites"
author: "Tu Nombre"
---
```
Después de renderizar (`quarto render tu_notebook.ipynb --to html`, sin necesidad de flags adicionales), el título de la pestaña del navegador y el encabezado del informe deberían reflejar estos valores.

**`#| echo: false` en una celda puntual:**
```python
#| echo: false
import pandas as pd
df = pd.read_csv("tramites_personas_combinado.csv")
```
Al renderizar, esta celda específica no muestra su código (solo su resultado, si lo tuviera), mientras que el resto de las celdas se comportan según el default general (todas visibles, salvo que hayas configurado `code-fold` o `echo:false` a nivel de todo el documento).

## Parte 5 (opcional) — Migrar a `.qmd`

```markdown
---
title: "Mi informe de trámites"
author: "Tu Nombre"
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

## Trámites por tipo

​```{python}
conteo = df["tipo_tramite"].value_counts()
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.bar(conteo.index, conteo.values)
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
​```
```

```bash
quarto render informe.qmd --to html
```

El resultado debería ser equivalente al generado desde el notebook — la diferencia está en el proceso de edición (archivo de texto plano vs. notebook con celdas), no en el resultado final.

## Nota para el docente

La Parte 2 es el corazón pedagógico de este ejercicio. Si alguien del grupo no logra reproducir la diferencia (por ejemplo, porque sin querer sí ejecutó la celda antes de guardar), vale la pena hacerlo de nuevo en vivo, proyectando la pantalla, para que quede clara la distinción entre "lo que dice el código" y "lo que Quarto realmente toma" (los resultados ya guardados). Es un matiz que, sin verlo pasar una vez, es fácil pasarlo por alto y generar informes desactualizados sin darse cuenta.
