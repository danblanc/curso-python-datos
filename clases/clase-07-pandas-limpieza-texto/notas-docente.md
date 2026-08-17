# Notas del docente — Clase 7

## Timing sugerido

| Bloque | Tiempo | Contenido |
|---|---|---|
| 1 | 10 min | Retomar el problema abierto de la Clase 6 (slide 3) |
| 2 | 15 min | Accesor `.str`, mayúsculas/espacios (slides 4-6) |
| 3 | 15 min | Tildes y Unicode (slides 7-8) |
| 4 | 25 min | Expresiones regulares básicas (slides 9-12) |
| 5 | 20 min | `.str.extract()` y normalización completa de documento (slides 13-15) |
| 6 | 15 min | Verificación de duplicados + por qué importa esta clase (slides 16-18) |
| 7 | 5 min | Buenas prácticas + resumen |
| 8 | 30-40 min | Ejercicio práctico |

## Esta es la clase más importante del curso — dictarla con ese peso

Es la que más conecta con el objetivo final (la técnica de similitud que se da después). Vale la pena, si el tiempo lo permite, dedicar un minuto extra a contextualizar: "todo lo que están por aprender ahora es exactamente el tipo de trabajo que después van a necesitar para que la técnica de similitud funcione bien — sin esto, esa técnica compara texto sucio y da resultados poco confiables".

## Tips de dictado

- **Regex (el bloque más denso):** no intentar enseñar regex a fondo — es un tema que da para un curso propio. El objetivo es que el grupo reconozca y sepa aplicar 4-5 patrones básicos (`\d`, `\s`, `+`, `[^...]`) con confianza, no que dominen la sintaxis completa. Repetirlo explícitamente para bajar la ansiedad: "no hace falta memorizar esto, va a quedar en el cheatsheet del repo para consultar siempre que lo necesiten".

- **Tildes/Unicode:** este bloque puede sentirse "mágico" (`unicodedata.normalize`) sin mucha intuición de por qué funciona. No hace falta explicar en profundidad el estándar Unicode — alcanza con mostrar que "una tilde es, por dentro, un carácter combinable, y esta función separa la letra base del acento y descarta el acento". Suficiente con eso.

- **Normalización de documento (slide 15):** este es el momento cúlmine de la clase — conectar visualmente con el problema planteado al principio. **Importante:** el dataset sintético del curso no genera casos donde el mismo documento aparezca con formato distinto entre sí (cada duplicado intencional conserva el mismo formato de documento que su original), así que el before/after de duplicados NO se nota usando `registros_personas.csv` directamente. Usar en cambio el ejemplo controlado de dos filas (slide 17) para mostrar el efecto de forma clara y garantizada — es más contundente pedagógicamente por ser un caso mínimo y controlado.

- **Cierre (slide 18):** ser explícito y directo sobre la relación con la técnica de similitud que viene después — es el momento de mayor motivación de todo el curso, no lo dejes pasar rápido.

## Errores comunes a anticipar

- Olvidar `regex=True` en `.str.replace()` cuando se usa un patrón regex (sin ese parámetro, Pandas puede interpretar el patrón como texto literal en versiones nuevas, o directamente fallar).
- Aplicar `.str.upper()` sobre una columna con valores nulos sin verificar antes — en general Pandas maneja bien los `NaN` en estos métodos (los deja como `NaN`), pero conviene mencionarlo para que no genere sorpresa.
- Confundir `\d` (regex, dentro de un string) con un caracter de escape de Python — remarcar que conviene usar strings "raw" (`r"\d+"`, con la `r` adelante) para evitar conflictos entre el escape de Python y el de regex.

## Cierre

Antes de pasar a la Clase 8, confirmar que el grupo pudo generar una columna de documento normalizada y comparar la cantidad de duplicados antes/después — es el ejercicio más representativo de todo el curso.
