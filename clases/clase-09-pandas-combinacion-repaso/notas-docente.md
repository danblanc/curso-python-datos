# Notas del docente — Clase 9

## Timing sugerido

| Bloque | Tiempo | Contenido |
|---|---|---|
| 1 | 10 min | El escenario (3 fuentes a combinar) (slide 3) |
| 2 | 25 min | `merge()` y tipos de join (slides 4-8) |
| 3 | 15 min | Verificación post-merge (slides 9-10) |
| 4 | 15 min | `pd.concat()` y cuándo usar cada herramienta (slides 11-12) |
| 5 | 10 min | Presentación del caso integrador (slide 13) |
| 6 | 5 min | Resumen |
| 7 | 30-40 min | Ejercicio práctico (repaso integrador) |

## Esta clase es la más flexible del cronograma

Si Pandas viene atrasado (muy probable si el grupo tuvo más dificultad de la esperada en las Clases 5-8), esta es la clase indicada para recortar y correr hacia la Semana 3 — ver la nota en `CRONOGRAMA.md`. El contenido nuevo real es solo `merge`/`concat` (bloques 2-4); el resto es integración de lo ya visto, por lo que se puede comprimir sin perder contenido nuevo crítico.

## Tips de dictado

- **Tipos de join (slides 5-7):** la explicación visual con diagramas de Venn (A y B) ayuda mucho más que solo código. Si es posible, dibujar (a mano, en pizarra virtual, o con una slide adicional) los 4 diagramas de Venn correspondientes a `inner`/`left`/`right`/`outer` antes de mostrar el código de cada uno.

- **`indicator=True` (slide 10):** hacer la demo en vivo con un caso donde a propósito algunos documentos no cruzan (por ejemplo, filtrando antes una porción de `personas`), para que se vea claramente la columna `_merge` con sus tres valores posibles.

- **Riesgo de duplicar filas (slide 11):** este es un error muy común y silencioso en la práctica — nadie nota que un merge duplicó filas hasta que las sumas totales "no cierran". Vale la pena mostrar el efecto en vivo: hacer un merge con una tabla que tiene un documento duplicado, y contar filas antes/después para que se vea el salto inesperado.

- **Caso integrador:** dejar tiempo suficiente para que el grupo entienda la consigna completa antes de que empiecen — es un ejercicio más largo y con más pasos que los anteriores, conviene leerlo en voz alta y confirmar que se entiende el objetivo general antes de que se pongan a programar.

## Errores comunes a anticipar

- Usar `on="documento"` cuando las columnas tienen nombres distintos en cada DataFrame (hay que usar `left_on`/`right_on`).
- No normalizar la columna clave (documento) en ambos DataFrames de la misma forma antes de mergear — si un lado tiene el documento con puntos y el otro sin puntos, el merge no va a encontrar coincidencias, aunque los datos "deberían" cruzar.
- Sorprenderse por una cantidad de filas mayor a la esperada después de un merge, sin pensar en duplicados de la columna clave como causa probable.

## Cierre

Este es el cierre del bloque de Pandas. Antes de pasar a visualización (Clase 10), vale la pena un cierre explícito: repasar en una frase todo el camino recorrido (leer → explorar → limpiar → normalizar texto → fechas → agregar → combinar), para que el grupo tenga el mapa mental completo antes de pasar a la siguiente etapa del curso.
