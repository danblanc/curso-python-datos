# Notas del docente — Clase 3

## Timing sugerido

| Bloque | Tiempo | Contenido |
|---|---|---|
| 1 | 5 min | Repaso: retomar la pregunta de cierre del ejercicio 2 |
| 2 | 20 min | Bucle `for` (slides 3-7) |
| 3 | 15 min | Bucle `while`, `break`/`continue` (slides 8-9) |
| 4 | 15 min | List comprehensions (slides 10-11) |
| 5 | 20 min | Funciones (slides 12-15) |
| 6 | 20 min | Manejo de errores (slides 16-19) |
| 7 | 5 min | Resumen |
| 8 | 30-40 min | Ejercicio práctico |

## Tips de dictado

- **Apertura:** arrancar retomando la reflexión del ejercicio anterior ("¿por qué tuvimos que acceder a mano?") — es el gancho natural hacia `for`. Si nadie lo intuyó, no importa, se resuelve solo con la primera slide.

- **`for` sobre listas de diccionarios (slide 7):** este es el punto más importante de conectar con lo que viene. Decirlo explícitamente: "esto que estamos haciendo ahora, recorrer una lista de diccionarios, es conceptualmente lo mismo que recorrer las filas de una tabla — en unas clases vamos a hacer esto mismo pero con Pandas, de forma mucho más cómoda".

- **`while` y bucle infinito:** vale la pena *provocar* un bucle infinito en vivo (con cuidado) y mostrar cómo cortarlo (`Ctrl+C` en la terminal, o el botón de detener en Jupyter). Que lo vean pasar una vez en un entorno controlado reduce el miedo cuando les pase solos.

- **List comprehensions:** no todos lo van a incorporar naturalmente en esta clase, y está bien. El objetivo es que lo *reconozcan* cuando lo vean (van a aparecer en código de ejemplo más adelante), no necesariamente que lo escriban con fluidez todavía.

- **Funciones — scope:** es un concepto abstracto. La forma más efectiva es mostrar el error en vivo (`NameError: name 'x' is not defined`) e ir despacio explicando por qué pasa.

- **Manejo de errores:** conectar explícitamente con el trabajo futuro en Pandas (slide 20) — no dejarlo como contenido aislado, sino anticipar por qué les va a servir pronto.

## Errores comunes a anticipar

- Olvidar los dos puntos (`:`) al final de `for`, `while`, `def`, `if`.
- En `while`, olvidarse de actualizar la variable de la condición → bucle infinito.
- Confundir `return` con `print` dentro de una función (la función "no devuelve nada" aunque imprima algo en pantalla).
- Nombrar una variable igual a una función ya usada (ej. `list = [1,2,3]`), lo cual sobreescribe el nombre `list` y genera errores confusos más adelante — mencionarlo brevemente como buena práctica a evitar.

## Cierre

Antes de la Clase 4, confirmar que el grupo puede escribir una función simple con `return` y usar `try/except` para capturar al menos un `ValueError`. Son las dos herramientas que más se van a apoyar en las próximas clases.
