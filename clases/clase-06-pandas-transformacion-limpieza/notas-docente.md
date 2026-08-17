# Notas del docente — Clase 6

## Timing sugerido

| Bloque | Tiempo | Contenido |
|---|---|---|
| 1 | 20 min | Columnas nuevas: directo, condiciones, `np.where` (slides 4-6) |
| 2 | 20 min | `.apply()`, funciones propias y lambda (slides 7-9) |
| 3 | 25 min | Nulos: diagnóstico, `.dropna()`, `.fillna()`, criterio de decisión (slides 10-13) |
| 4 | 20 min | Duplicados, incluyendo el caso "no trivial" (slides 14-16) |
| 5 | 15 min | Conversión de tipos (slides 17-18) |
| 6 | 5 min | Flujo típico + resumen (slides 19-20) |
| 7 | 30-40 min | Ejercicio práctico |

## Tips de dictado

- **Apertura (slide 3):** vale la pena remarcar que esta clase, junto con la 7 y la 8, son "el corazón práctico" del curso — en cualquier trabajo real de análisis de datos, la limpieza ocupa la mayor parte del tiempo, mucho más que el análisis en sí. Bajar expectativas de que esto sea "rápido y aburrido": es la parte más importante.

- **`.apply()` con `axis=1`:** suele costar más que el resto. Mostrar primero un caso sin `axis=1` (aplicando a una sola columna) y recién después el caso con `axis=1` (fila completa) — no presentarlos juntos de entrada.

- **"¿Eliminar o imputar?" (slide 13):** esta tabla es un buen momento para abrir a discusión grupal, no solo leerla. Preguntar: "en nuestro dataset de personas, ¿qué harían con los nulos de teléfono? ¿Y con los de provincia?" — generar debate antes de dar la respuesta "correcta" (que de hecho no es única).

- **Duplicados no triviales (slide 16):** esta slide es un gancho intencional hacia la Clase 7. No resolver el problema ahora — dejarlo abierto, generar la pregunta, y decir explícitamente "esto lo resolvemos la clase que viene". Es importante para mantener el hilo conductor hacia el objetivo final del curso (registros administrativos, similitud).

- **`errors="coerce"`:** mostrar en vivo qué pasa SIN ese parámetro (el error que tira `pd.to_numeric` al toparse con un valor no convertible) antes de mostrar la solución — ayuda a que el parámetro tenga sentido y no parezca magia.

## Errores comunes a anticipar

- Confundir `.apply()` sobre una Series (una columna) con `.apply()` sobre un DataFrame (con `axis=1`) — son dos usos distintos de la misma función y genera confusión al principio.
- Usar `.dropna()` sin `subset` y perder muchas más filas de las esperadas.
- Olvidar que `.fillna()` y `.drop_duplicates()` (y la mayoría de los métodos de Pandas) **no modifican el DataFrame original** a menos que se reasigne (`df = df.fillna(...)`) o se use `inplace=True` (mencionar que existe, pero recomendar la reasignación explícita por legibilidad).

## Cierre

Antes de pasar a la Clase 7, confirmar que el grupo entendió el problema de los "duplicados no triviales" (documento con o sin puntos) — es el motivo por el cual la próxima clase existe, y conecta directamente con el objetivo final del curso.
