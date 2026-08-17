# Notas del docente — Clase 2

## Timing sugerido

| Bloque | Tiempo | Contenido |
|---|---|---|
| 1 | 5 min | Repaso rápido Clase 1 (venv activado, dudas pendientes) |
| 2 | 15 min | Variables y tipos (slides 3-5) |
| 3 | 30 min | Listas, tuplas, diccionarios, sets (slides 6-11) |
| 4 | 15 min | Operadores (slides 12-14) |
| 5 | 20 min | Condicionales (slides 15-18) |
| 6 | 5 min | Resumen |
| 7 | 30-40 min | Ejercicio práctico |

## Tips de dictado

- **Tipos de datos:** hacer que todos ejecuten `type()` sobre distintos valores en vivo, en una notebook o en el intérprete interactivo de Python (`python` sin argumentos abre un modo interactivo, útil para probar cosas rápido).

- **Estructuras nativas (el bloque más largo):** no dar las 4 de corrido en abstracto. Ir con un mismo ejemplo (datos de una persona) y mostrar cómo cambiaría representarlo como lista, como diccionario, etc. La tabla comparativa (slide 12) es el cierre de este bloque, no el inicio — que la vean después de haber jugado con cada estructura.

- **Diccionarios:** este es el que más se usa después en el curso (JSON, registros). Vale la pena un ejemplo extra si sobra tiempo, conectando con "esto se parece a una fila de una tabla, donde cada clave es una columna" — ya empieza a preparar el terreno mental para Pandas.

- **`==` vs `=`:** remarcarlo explícitamente, es el error más común. Sugerido: escribir mal a propósito `if edad = 18:` y mostrar el error que tira Python, para que lo reconozcan cuando les pase.

- **Indentación:** mostrar en vivo qué pasa si la indentación está mal (`IndentationError`), para que no les genere pánico la primera vez que lo vean solos.

## Errores comunes a anticipar

- Confundir índice de lista empezando en 0 (muy común al principio).
- Intentar modificar una tupla y no entender el error — aprovechar para reforzar el concepto de inmutabilidad.
- Usar `=` en vez de `==` dentro de un `if`.
- Errores de indentación (mezclar espacios y tabs — recomendar consistencia, VS Code por defecto usa espacios).

## Cierre

Antes de pasar a la Clase 3, confirmar que el grupo distingue con claridad cuándo usar lista vs. diccionario — es la base conceptual para entender más adelante un DataFrame de Pandas (que es, esencialmente, una colección de diccionarios/filas con estructura).
