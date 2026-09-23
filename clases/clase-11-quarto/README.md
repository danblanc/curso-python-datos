# Clase 10b — De notebook a informe: Quarto

**Duración:** ~1-1.5 horas (sesión corta, tipo comodín)
**Modalidad:** según el cronograma vigente del grupo

## Por qué esta clase

Después de la Clase 10 ya sabés generar visualizaciones dentro de un notebook. El paso que falta es poder **entregar ese trabajo** como algo presentable — un informe en PDF o HTML, sin código de más si el destinatario no lo necesita, pero con el código disponible si alguien técnico quiere revisarlo.

Esta clase es corta y modular: se puede dar como sesión independiente en cualquier punto después de la Clase 10, o dejarse como contenido de reserva si el cronograma lo permite.

## Objetivos de aprendizaje

- Instalar Quarto y entender qué resuelve.
- Exportar un notebook (`.ipynb`) ya existente a HTML y a PDF, sin modificar su contenido.
- Controlar la visibilidad del código en el informe exportado: ocultarlo por completo, o dejarlo plegado y disponible con un clic.
- Escribir un archivo `.qmd` desde cero (texto + código + metadatos), como alternativa a partir de un notebook existente.
- Tener criterio para elegir cuándo alcanza con exportar un notebook tal cual, y cuándo conviene migrar a `.qmd`.

## Contenidos

1. De la exploración al informe: qué problema resuelve Quarto
2. Instalación de Quarto
3. Renderizar un notebook existente a HTML (`quarto render`)
4. Un detalle importante: Quarto usa los resultados ya guardados en el notebook, no lo vuelve a ejecutar por defecto
5. Renderizar a PDF: instalar un motor LaTeX (TinyTeX)
6. Ocultar el código sin tocar el notebook (`-M echo:false`)
7. Código plegable en HTML (`-M code-fold:true`)
8. Control más fino: metadatos en una celda "raw" del notebook, y `#| echo: false` por celda
9. Introducción a `.qmd`: la misma lógica, en un archivo de texto plano
10. `.ipynb` vs. `.qmd`: cuándo conviene cada uno

## Prerrequisitos

Clase 10 completa (vas a reutilizar un notebook con al menos un gráfico).

## Material

- [`slides.md`](./slides.md)
- [`ejercicios/ejercicio-10b-quarto.md`](./ejercicios/ejercicio-10b-quarto.md) — ~20-25 min
- [`recursos/`](./recursos/)

Soluciones en [`soluciones/clase-10b/`](../../soluciones/clase-10b/).

## Instalación necesaria

**Quarto CLI** (no se instala con `pip`, es una herramienta aparte):

- **Windows:** descargar el instalador desde [quarto.org/docs/get-started](https://quarto.org/docs/get-started/) y ejecutarlo.
- **macOS:** descargar el instalador `.pkg` desde el mismo sitio, o `brew install quarto` si usás Homebrew.

Verificar la instalación:
```bash
quarto --version
```

Para exportar a PDF vas a necesitar además un motor LaTeX — se instala con:
```bash
quarto install tinytex
```

> **Nota:** esta instalación descarga varios cientos de MB y requiere conexión a internet en el momento de instalar. Si trabajás en una red corporativa restringida, puede ser el paso que más fricción genere de todo el curso — si el PDF no sale por un problema de instalación, HTML es un camino alternativo sin esta dependencia.

Extensión recomendada para VS Code/Cursor: **Quarto** (misma lógica que la extensión Marp que ya venís usando para las slides).
