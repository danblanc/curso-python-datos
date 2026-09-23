# Notas del docente — Clase 10b

Sesión corta tipo comodín (~1-1.5h). Todo el material de esta clase fue **verificado de punta a punta** instalando Quarto y ejecutando cada comando (incluyendo renderizado a PDF con motor LaTeX) antes de escribirlo — no es contenido de memoria sin probar.

## Timing sugerido (~1h15)

| Bloque | Tiempo | Contenido |
|---|---|---|
| 1 | 5 min | El problema: de notebook a informe (slides 3-4) |
| 2 | 10 min | Instalación de Quarto (slides 5-6) |
| 3 | 10 min | Renderizar a HTML + el detalle de "no re-ejecuta por defecto" (slides 7-9) |
| 4 | 10 min | Renderizar a PDF + TinyTeX (slide 10) |
| 5 | 15 min | Ocultar/plegar código: `-M echo`, `-M code-fold`, YAML, `#|` por celda (slides 11-15) |
| 6 | 10 min | Introducción a `.qmd` (slides 16-18) |
| 7 | 5 min | `.ipynb` vs `.qmd` + resumen (slides 19-20) |
| 8 | 20-25 min | Ejercicio práctico |

## Preparación previa a la clase — MUY importante en esta sesión

A diferencia del resto del curso, acá hay una instalación de herramienta externa (no un paquete de `pip`) que puede fallar por motivos ajenos al alumno: permisos de administrador, antivirus corporativo, o falta de conexión en el momento. **Probar la instalación en al menos una máquina Windows y una Mac antes de la clase**, si es posible, para anticipar variantes según la versión del sistema operativo.

Confirmar también que `datasets/clean/tramites_personas_combinado.csv` esté disponible, y que cada alumno tenga a mano un notebook de la Clase 10 con al menos un gráfico ya generado y guardado (con el notebook ya ejecutado — es un prerrequisito real para esta clase, no solo una sugerencia).

## Tips de dictado

- **El detalle de "no re-ejecuta por defecto" (slide 9):** este es, con diferencia, el punto donde más gente se va a trabar en el ejercicio — alguien va a renderizar su notebook y le va a faltar el gráfico porque no corrió todas las celdas antes de guardar. Vale la pena remarcarlo con énfasis explícito ANTES de que lo intenten, no solo dejarlo en la slide.

- **PDF y TinyTeX:** este es el paso con más probabilidad de fallar por motivos de entorno (red restringida, antivirus, permisos). Tené a mano la alternativa de HTML lista para quien no logre instalar TinyTeX a tiempo — no dejar que se frene el resto de la clase por este paso puntual. Si el grupo trabaja en un entorno con acceso a internet restringido (como se vio en la Clase 1 con salas seguras sin conexión), directamente arrancar por HTML y dejar PDF como demostración tuya en pantalla compartida, sin pedirles que lo repliquen en el momento.

- **`-M echo:false` en vivo:** mostrar el mismo HTML generado dos veces (con y sin la opción) lado a lado, para que se vea el contraste de forma directa — es más efectivo que explicarlo solo con palabras.

- **YAML en celda Raw:** aclarar que la celda debe ser específicamente de tipo **"Raw"** (no "Markdown" ni "Code") — en Jupyter/VS Code hay un selector de tipo de celda, y es un error común dejarla como Markdown por costumbre.

- **`.qmd` (cierre):** no hace falta que se sientan obligados a migrar todo a `.qmd` — el mensaje central es que la sintaxis interna (YAML, `#|`, bloques de código) es la **misma** que ya vieron dentro del notebook, así que no es contenido nuevo, es el mismo conocimiento en otro contenedor.

## Errores comunes a anticipar

- Renderizar un notebook sin haberlo ejecutado antes (informe sin gráficos ni resultados) — el error más probable de toda la clase, ver arriba.
- Confundir el flag `--to` (formato de salida: `html`, `pdf`) con `-M` (opciones de metadata como `echo`, `code-fold`) — son cosas distintas y van por separado.
- Dejar la celda de metadata YAML como tipo "Markdown" en vez de "Raw", lo cual hace que Quarto no la interprete como configuración y en cambio la muestre como texto literal en el informe.
- No tener instalado un kernel de Python válido y asociado al notebook — si el notebook nunca se ejecutó localmente al menos una vez, puede no tener la metadata de kernel necesaria para que `--execute` funcione.

## Cierre

Esta clase es un buen punto para recordar el hilo conductor de todo el curso: cada herramienta nueva (Pandas, Seaborn, Plotly, y ahora Quarto) resuelve un problema concreto en la cadena que va desde datos crudos hasta algo que otra persona pueda leer y usar. Quarto es, en ese sentido, el cierre natural del trabajo de visualización antes de pasar a Streamlit — la otra forma de "entregar" un análisis, pero interactiva en vez de estática.
