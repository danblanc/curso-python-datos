# Ejercicio 9 — Repaso integrador: combinando las tres fuentes

**Duración estimada:** 30-40 minutos

## Objetivo

Integrar en un solo flujo todo lo trabajado en las Clases 5 a 9: lectura de múltiples fuentes, normalización de texto y documentos, manejo de fechas, combinación de datos y agregación.

## Datasets

Vas a combinar los tres datasets crudos del curso:

- [`datasets/raw/registros_personas.csv`](../../../datasets/raw/registros_personas.csv)
- [`datasets/raw/registros_tramites.xlsx`](../../../datasets/raw/registros_tramites.xlsx)
- [`datasets/raw/registros_direcciones.json`](../../../datasets/raw/registros_direcciones.json) *(opcional, ver Parte 5)*

## Consigna

### Parte 1 — Cargar y normalizar documentos

1. Cargá `registros_personas.csv` y `registros_tramites.xlsx`.
2. En cada uno, creá una columna `documento_normalizado` (dígitos únicamente, convertida a numérico) — la columna se llama `documento` en personas y `documento_solicitante` en trámites.

### Parte 2 — Resolver duplicados antes de combinar

3. Antes de cualquier combinación, revisá si `registros_personas` tiene duplicados según `documento_normalizado`. Si los hay, quedate con la primera aparición de cada uno (esto es importante: si no lo hacés, el merge del siguiente paso puede multiplicar filas inesperadamente).

### Parte 3 — Convertir fechas y combinar

4. En el dataset de trámites, convertí `fecha_inicio` y `fecha_resolucion` a tipo fecha (recordá el formato mixto que vimos en la Clase 8).
5. Combiná trámites con personas (ya sin duplicados) usando la columna `documento_normalizado`, de forma que **no se pierda ningún trámite**, tenga o no una persona asociada. Usá `indicator=True` y verificá cuántos trámites efectivamente encontraron una persona correspondiente.

### Parte 4 — Responder preguntas con el dataset combinado

6. Normalizá también la columna `tipo_tramite` (mayúsculas/espacios inconsistentes, como vimos en la Clase 7).
7. Con el dataset ya combinado y normalizado, respondé:
   - ¿Cuál es el monto total asociado (`monto_asociado`), agrupado por provincia del trámite?
   - Agrupando por `tipo_tramite` (normalizado) y `estado` a la vez, ¿cuál es la suma y la cantidad de trámites en cada combinación?
8. Usando un merge en sentido inverso (personas → trámites), identificá cuántas personas **no tienen ningún trámite asociado**.

### Parte 5 — Para quienes lleguen con tiempo (opcional)

9. Cargá también `registros_direcciones.json`, normalizá su columna `documento` de la misma forma, y combinala con el dataset de personas para agregar la dirección de cada una al análisis.

## Qué se evalúa

- Normalización correcta y consistente del documento en más de un dataset.
- Verificar y resolver duplicados **antes** de combinar, no después.
- Uso correcto de `pd.merge()` con el `how` apropiado, y verificación del resultado con `indicator=True`.
- Combinación correcta de agrupación (`.groupby()`) sobre datos ya combinados y normalizados.

## Ayuda

Solución de referencia en [`soluciones/clase-09/`](../../../soluciones/clase-09/).
