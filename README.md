# Curso de Python para Análisis de Datos y Construcción del Registro Base Poblacional

Curso introductorio de programación en Python orientado al análisis y procesamiento de datos, con foco en registros administrativos. El curso cubre desde los fundamentos de programación hasta la construcción de dashboards interactivos, como base previa a la aplicación de técnicas de análisis de similitud de registros (que se dicta en una instancia posterior, fuera de este curso).

## A quién está dirigido

Personas sin experiencia previa en programación (o con experiencia mínima) que necesitan aprender Python aplicado al manejo, limpieza y visualización de datos, particularmente en el contexto de registros administrativos (personas, trámites, direcciones, documentos).

## Duración y modalidad

- **Carga horaria total:** 50 horas
- **Semana 1 y 2:** 10 clases de 2 horas (modalidad virtual/asincrónica)
- **Semana 3:** 5 clases de 6 horas (modalidad presencial)

Ver el detalle completo en [`CRONOGRAMA.md`](./CRONOGRAMA.md).

## Requisitos previos

- No se requiere experiencia previa en programación.
- Computadora personal con posibilidad de instalar software (Python, VS Code).
- Ver [`recursos-generales/instalacion-entorno.md`](./recursos-generales/instalacion-entorno.md) para la guía de instalación, a completar **antes de la Clase 1**.

## Estructura del repositorio

```
curso-python-datos/
├── CRONOGRAMA.md               # Cronograma completo: clases, fechas, temas, duración
├── clases/                     # Material de cada clase (slides, ejercicios, recursos)
├── soluciones/                 # Soluciones a los ejercicios de cada clase
├── datasets/                   # Datasets sintéticos usados a lo largo del curso
├── proyecto-final/             # Consigna y datos del proyecto integrador (clases 13-15)
└── recursos-generales/         # Guías de instalación, cheatsheets, glosario
```

### Cómo usar cada carpeta de clase

Cada clase en `clases/clase-XX-tema/` contiene:

- **`README.md`** — objetivos de aprendizaje y contenidos de la clase.
- **`slides.md`** — diapositivas en formato [Marp](https://marp.app/).
- **`ejercicios/`** — consignas de práctica (30-45 min por clase).
- **`recursos/`** — código de ejemplo usado durante la clase.

Las soluciones a los ejercicios **no** están en la carpeta de la clase, sino en `soluciones/clase-XX/`, para que quien cursa pueda intentarlo primero sin ver la resolución.

## Temario general

| Módulo | Contenido |
|---|---|
| 0 | Introducción a la programación y configuración del entorno |
| 1 | Bases del lenguaje Python |
| 2 | Buenas prácticas y manejo de archivos |
| 3 | NumPy |
| 4 | Pandas: manipulación, limpieza y transformación de datos |
| 5 | Visualización de datos (Matplotlib, Seaborn, Plotly) |
| 6 | Dashboards interactivos con Streamlit |
| 7 | Proyecto integrador (y, opcionalmente, introducción a Git) |

## Cómo visualizar las diapositivas (Marp)

Las slides están escritas en Markdown con formato Marp. Para verlas como presentación:

- **VS Code:** instalar la extensión "Marp for VS Code" y abrir el `slides.md` correspondiente.
- **Línea de comandos:** con [Marp CLI](https://github.com/marp-team/marp-cli) instalado:
  ```bash
  marp slides.md --pdf
  # o
  marp slides.md --html
  ```

## Licencia y uso

Material desarrollado para uso educativo del curso. Los datasets son completamente sintéticos (generados con `Faker`) y no contienen datos reales de personas.
