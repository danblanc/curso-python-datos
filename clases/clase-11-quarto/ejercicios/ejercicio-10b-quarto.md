# Ejercicio 10b — De notebook a informe con Quarto

**Duración estimada:** 20-25 minutos

## Objetivo

Tomar un notebook con gráficos ya hechos (de la Clase 10) y convertirlo en un informe en HTML y PDF, controlando qué código se ve y cuál no.

## Punto de partida

Necesitás un notebook con al menos dos gráficos generados a partir de [`datasets/clean/tramites_personas_combinado.csv`](../../../datasets/clean/tramites_personas_combinado.csv) — podés reutilizar el que armaste en los ejercicios de la Clase 10, o armar uno nuevo rápido con, por ejemplo, un gráfico de barras (cantidad de trámites por tipo) y un gráfico de Seaborn (boxplot de montos por estado).

**Importante:** antes de seguir, ejecutá **todas las celdas** del notebook (`Run All`) y guardalo.

## Consigna

### Parte 1 — Primer render

1. Desde la terminal, en la carpeta donde está tu notebook, ejecutá:
   ```bash
   quarto render tu_notebook.ipynb --to html
   ```
2. Abrí el archivo `.html` generado en tu navegador. Confirmá que los gráficos aparecen correctamente.

### Parte 2 — Provocar el error típico, a propósito

3. Modificá algo del código de una celda (por ejemplo, cambiá el color de un gráfico o el título), pero **no vuelvas a ejecutar la celda**. Guardá el notebook así, sin ejecutar el cambio.
4. Volvé a renderizar con `quarto render tu_notebook.ipynb --to html`. ¿El cambio aparece en el informe? ¿Por qué sí o por qué no?
5. Ahora renderizá con la opción `--execute` agregada al final del comando. ¿Cambió el resultado esta vez?

### Parte 3 — PDF

6. Si tenés Quarto y TinyTeX instalados correctamente, renderizá el mismo notebook a PDF:
   ```bash
   quarto render tu_notebook.ipynb --to pdf
   ```
   Si no lográs instalar TinyTeX (por ejemplo, por restricciones de red), no hay problema — seguí con el resto del ejercicio usando solo HTML.

### Parte 4 — Controlar la visibilidad del código

7. Generá una versión del informe **sin ningún código visible**, sin modificar el notebook, usando la opción correspondiente desde la terminal.
8. Generá otra versión donde el código esté **plegado pero disponible** (no oculto del todo). Abrí el resultado y probá desplegar el código haciendo clic.
9. Agregá una celda de tipo **Raw** al principio de tu notebook con un YAML que defina un título y tu nombre como autor. Volvé a renderizar a HTML y confirmá que el título cambió.
10. En una celda de código puntual (por ejemplo, la que carga los datos), agregá `#| echo: false` como primera línea, dejando el resto de las celdas sin esa opción. Renderizá de nuevo: ¿esa celda específica quedó oculta mientras las demás se ven?

### Parte 5 — Para cerrar (opcional, si llegás con tiempo)

11. Copiá el contenido de tu notebook (texto y código) a un archivo nuevo `informe.qmd`, replicando la misma estructura de YAML + Markdown + bloques de código que viste en las slides. Renderizalo con `quarto render informe.qmd --to html` y compará el resultado contra la versión generada desde el notebook.

## Qué se evalúa

- Render exitoso de un notebook existente a HTML (y a PDF, si el entorno lo permite).
- Haber entendido, de forma práctica y no solo teórica, por qué Quarto no siempre refleja cambios recientes sin re-ejecutar.
- Uso correcto de al menos dos de las tres formas de controlar la visibilidad del código (comando, YAML, `#|` por celda).

## Ayuda

Solución de referencia en [`soluciones/clase-10b/`](../../../soluciones/clase-10b/).
