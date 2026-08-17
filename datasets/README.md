# Datasets del curso

Todos los datasets son **completamente sintéticos**, generados con la librería [Faker](https://faker.readthedocs.io/) (locale `es_AR`). No representan personas ni trámites reales. Fueron diseñados para simular registros administrativos típicos (personas, trámites, direcciones) con inconsistencias reales de carga de datos, útiles para practicar limpieza en Pandas.

## Reproducibilidad

Los datasets se generan con el script [`scripts-generacion/generar_datasets.py`](./scripts-generacion/generar_datasets.py), con semilla fija (`SEED = 42`), por lo que ejecutarlo nuevamente produce los mismos datos:

```bash
cd datasets/scripts-generacion
python generar_datasets.py
```

## Estructura

- **`raw/`** — versión "sucia" de los datos. Se usa en las clases de limpieza (Clases 6, 7 y 8).
- **`clean/`** — versión ya procesada. Se usa en las clases de visualización y Streamlit (Clases 10, 11, 12), para no depender de que la limpieza de clases anteriores haya sido perfecta.

## `raw/registros_personas.csv`

Listado de personas (solicitantes de trámites).

| Columna | Tipo | Descripción | Problemas intencionales |
|---|---|---|---|
| `id_persona` | int | Identificador interno | — |
| `documento` | texto | Número de documento | Formato inconsistente: con puntos, guiones, espacios o plano |
| `nombre` | texto | Nombre de pila | Mayúsculas/minúsculas inconsistentes, espacios extra |
| `apellido` | texto | Apellido | Mayúsculas/minúsculas inconsistentes, espacios extra |
| `fecha_nacimiento` | texto | Fecha de nacimiento | Múltiples formatos de fecha (`YYYY-MM-DD`, `DD/MM/YYYY`, etc.) |
| `email` | texto | Correo electrónico | ~8% de valores nulos |
| `telefono` | texto | Teléfono de contacto | ~12% de valores nulos |
| `provincia` | texto | Provincia de residencia | ~4% de valores nulos |
| `direccion` | texto | Dirección de residencia | Espacios extra |

**Nota:** este dataset incluye ~3% de registros duplicados de forma intencional (mismo documento, con variación de formato en el nombre), para practicar detección de duplicados "no triviales" — un anticipo conceptual de lo que luego se trabaja en la técnica de similitud de registros.

## `raw/registros_tramites.xlsx`

Trámites administrativos asociados a personas.

| Columna | Tipo | Descripción | Problemas intencionales |
|---|---|---|---|
| `id_tramite` | int | Identificador interno | — |
| `documento_solicitante` | texto | Documento de quien inicia el trámite | Formato inconsistente (para practicar `merge` con `registros_personas`) |
| `tipo_tramite` | texto | Tipo de trámite (8 categorías) | Mayúsculas inconsistentes |
| `estado` | texto | Estado del trámite (`Iniciado`, `En revisión`, `Aprobado`, `Rechazado`, `Observado`) | — |
| `fecha_inicio` | texto | Fecha de inicio del trámite | Múltiples formatos de fecha |
| `fecha_resolucion` | texto | Fecha de resolución (si aplica) | Nulo si el trámite sigue en curso |
| `monto_asociado` | float | Monto asociado al trámite (si aplica) | ~30% de valores nulos |
| `provincia` | texto | Provincia donde se inició el trámite | — |

## `raw/registros_direcciones.json`

Direcciones en formato semi-estructurado (JSON), para practicar lectura de fuentes no tabulares.

| Campo | Tipo | Descripción |
|---|---|---|
| `documento` | texto | Documento de la persona (mismo formato inconsistente que en `registros_personas`) |
| `direccion_normalizada` | null | Vacío intencionalmente — se completa como ejercicio en la Clase 7 |
| `direccion_original` | texto | Dirección tal como fue cargada |
| `provincia` | texto | Provincia |
| `codigo_postal` | texto | Código postal (~20% nulo) |

## `clean/`

Versión procesada de los datasets anteriores (documentos normalizados a numérico, fechas parseadas, nulos tratados, duplicados eliminados). Incluye además:

- **`tramites_personas_combinado.csv`** — resultado de unir `tramites_clean` y `personas_clean` por documento. Es el dataset base sugerido para las clases de visualización (10, 11) y para el dashboard de Streamlit (12).

## `proyecto-final/datasets/`

Dataset adicional, más grande y con mayor variedad de inconsistencias, reservado para el proyecto integrador de las Clases 13-15. Ver [`proyecto-final/README.md`](../proyecto-final/README.md).
