# Notas del docente — Clase 4

## Timing sugerido

| Bloque | Tiempo | Contenido |
|---|---|---|
| 1 | 15 min | PEP8 y organización en módulos (slides 3-6) |
| 2 | 30 min | Lectura/escritura de archivos, `with` (slides 7-11) |
| 3 | 15 min | Módulo `csv` (slides 12-13) |
| 4 | 5 min | Por qué ver esto antes de Pandas (slide 14) |
| 5 | 30 min | NumPy: arrays, vectorización, estadística básica (slides 15-19) |
| 6 | 5 min | Resumen |
| 7 | 30-40 min | Ejercicio práctico |

## Rutas de archivo: Mac vs. Windows

A partir de esta clase empezamos a trabajar con rutas de archivo explícitamente — es un buen momento para mencionar la diferencia:

- **Windows** usa `\` como separador de carpetas (aunque Python también acepta `/`).
- **macOS / Linux** usa `/`.

Recomendación práctica para evitar problemas: usar siempre `/` en el código Python (funciona en los tres sistemas), o mejor aún, usar el módulo `pathlib` más adelante en el curso si se quiere ser prolijo multiplataforma. Para esta clase, alcanza con trabajar con archivos en la misma carpeta del script (rutas relativas simples, sin barras).

## Tips de dictado

- **PEP8:** no convertir esto en una clase de reglas de estilo exhaustiva — mostrar 3-4 reglas clave y, sobre todo, mostrar cómo VS Code ya ayuda automáticamente (subrayado, autoformato). El objetivo es generar el hábito, no la memorización.

- **`with` vs `open`/`close`:** vale la pena mostrar en vivo un caso donde el `close()` "se olvida" (comentando la línea) y explicar el riesgo, antes de presentar `with` como la solución. Ayuda a que no se sienta como una regla arbitraria.

- **CSV con Python puro:** este bloque es un poco denso. El mensaje clave a remarcar (slide 14) es que **todo esto lo hace Pandas por vos, mejor y más rápido** — no es que vayan a programar lectores de CSV a mano en el día a día, es para que entiendan la mecánica de fondo.

- **NumPy:** el salto conceptual importante es "vectorización" (slide 17-18). Usar la comparación directa lista vs. array con el mismo ejemplo, y si es posible, mostrar con `%timeit` (en Jupyter) la diferencia de velocidad entre un bucle y una operación vectorizada sobre un array grande (por ejemplo, un millón de elementos) — el efecto visual de "esto tarda X, esto tarda casi nada" suele ser muy convincente.

## Errores comunes a anticipar

- Olvidar `encoding="utf-8"` al abrir archivos con texto en español (tildes, ñ) — puede day error o texto corrupto en Windows si no se especifica.
- Confundir el modo `"w"` (sobrescribe) con `"a"` (agrega) y perder contenido de un archivo sin querer.
- Con NumPy: esperar que `array * 2` funcione igual sobre una lista común (`lista * 2` en Python puro **duplica la lista**, no multiplica sus elementos — es un contraste interesante para mostrar en vivo).

## Cierre

Confirmar que el grupo entiende la diferencia central entre lista y array de NumPy (vectorización) antes de avanzar a Pandas en la próxima clase, ya que un DataFrame de Pandas se apoya conceptualmente en esta misma idea.
