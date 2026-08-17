# Ejercicio 7 — Limpieza y normalización de texto

**Duración estimada:** 30-40 minutos

## Objetivo

Practicar normalización de texto: mayúsculas, espacios, tildes y expresiones regulares, aplicado a un caso de registros administrativos.

## Dataset

[`datasets/raw/registros_personas.csv`](../../../datasets/raw/registros_personas.csv)

## Consigna

### Parte 1 — Normalizar nombre y apellido

1. Cargá el dataset.
2. Creá las columnas `nombre_normalizado` y `apellido_normalizado`, aplicando `.str.strip()` y `.str.title()` sobre `nombre` y `apellido` respectivamente.
3. Comparate el resultado con los valores originales para al menos 5 filas — ¿ves alguna inconsistencia que `.str.title()` no resuelve del todo? (por ejemplo, con nombres compuestos)

### Parte 2 — Espacios en el medio del texto

4. Usando `.str.replace()` con una expresión regular (`\s+` → un solo espacio, con `regex=True`), corregí posibles espacios duplicados en el medio de la columna `direccion`. Guardá el resultado en `direccion_normalizada`.

### Parte 3 — Normalizar documento (el caso central de la clase)

5. Escribí una función `normalizar_documento(doc)` que reciba un valor de documento (con o sin puntos, guiones o espacios) y devuelva **solo los dígitos**, sin ningún otro caracter. Usá una expresión regular (`re.sub` o `.str.replace` con `[^\d]`).
6. Aplicá la función para crear la columna `documento_normalizado`.
7. Convertí `documento_normalizado` a tipo numérico con `pd.to_numeric(errors="coerce")` y verificá que ya no se generen valores `NaN` (a diferencia de lo que pasaba en el Ejercicio 6 al convertir la columna sin normalizar antes).

### Parte 4 — El problema de fondo, en un ejemplo controlado

8. Copiá y ejecutá el siguiente bloque, que simula el escenario real que motiva esta clase — dos registros que representan a la **misma persona**, pero con el documento escrito en formato distinto:

   ```python
   ejemplo = pd.DataFrame({
       "documento": ["30123456", "30.123.456"],
       "nombre": ["Ana Gomez", "ANA GOMEZ"],
   })

   print("Duplicados detectados SIN normalizar:", ejemplo.duplicated(subset=["documento"]).sum())

   ejemplo["documento_normalizado"] = ejemplo["documento"].apply(normalizar_documento)
   print("Duplicados detectados DESPUÉS de normalizar:", ejemplo.duplicated(subset=["documento_normalizado"]).sum())
   ```

9. Ejecutalo y confirmá la diferencia entre ambos resultados. En un comentario, explicá con tus palabras por qué ocurre esa diferencia.

### Parte 5 — Tildes (opcional, si llegás con tiempo)

10. Usando la función `quitar_tildes` vista en las slides (o escribiendo la tuya con `unicodedata`), creá una columna `provincia_sin_tildes` a partir de `provincia`.

## Qué se evalúa

- Uso correcto del accesor `.str` para operaciones de texto vectorizadas.
- Escritura y aplicación correcta de una expresión regular simple (`[^\d]`, `\s+`).
- Comprensión de por qué normalizar antes de comparar/convertir cambia el resultado.

## Ayuda

Solución de referencia en [`soluciones/clase-07/`](../../../soluciones/clase-07/).
