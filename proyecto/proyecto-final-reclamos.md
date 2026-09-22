# Proyecto final — Reclamos ciudadanos a la Intendencia

**Duración estimada:** una clase presencial completa (~3-4 horas)

## El escenario

Empezaste a trabajar como analista de datos en el área de Atención a la Ciudadanía de la Intendencia. Te pasan una exportación cruda del sistema de reclamos ciudadanos (`reclamos_ciudadanos.csv`) y una serie de preguntas que distintas áreas necesitan para un informe de gestión.

Nadie te va a decir qué función o método de Pandas usar para cada cosa — de eso se trata este proyecto. Las preguntas están formuladas como te las haría un responsable de área, no como una consigna técnica. Vas a tener que decidir vos, en cada caso, qué herramienta de todo lo visto hasta la Clase 8 (Pandas: fundamentos, transformación y limpieza, limpieza de texto, fechas y agregación) es la adecuada.

Una advertencia: en más de una pregunta vas a necesitar combinar **más de una técnica de limpieza** para llegar a una respuesta correcta — no asumas que la primera corrección que se te ocurra ya resuelve el problema del todo. Revisá siempre tus resultados con sentido crítico antes de darlos por buenos.

## El dataset

**Archivo:** `reclamos_ciudadanos.csv`

| Columna | Descripción |
|---|---|
| `id_reclamo` | Identificador interno del reclamo |
| `documento` | Documento de identidad de quien realizó el reclamo |
| `nombre` | Nombre de quien realizó el reclamo |
| `apellido` | Apellido de quien realizó el reclamo |
| `tipo_reclamo` | Categoría del reclamo |
| `barrio` | Barrio donde se originó el reclamo |
| `fecha_reclamo` | Fecha en la que se registró el reclamo |
| `fecha_resolucion` | Fecha en la que se resolvió el reclamo (si corresponde) |
| `estado` | Estado actual del reclamo (`Pendiente`, `En proceso`, `Resuelto`, `Desestimado`) |
| `prioridad` | Prioridad asignada al reclamo (`Baja`, `Media`, `Alta`) |
| `costo_estimado` | Costo estimado de atender el reclamo |

## Preguntas

1. ¿Cuántos reclamos hay registrados en total, y cuántos campos de información se cargan por cada uno?

2. ¿Cuántos reclamos no tienen registrado el barrio donde ocurrieron? ¿Y cuántos no tienen un costo estimado cargado?

3. El área de fiscalización quiere atender primero los casos más urgentes que todavía no se atendieron. ¿Cuántos reclamos son de prioridad `"Alta"` y siguen en estado `"Pendiente"`?

4. Para las comunicaciones oficiales necesitan el nombre y apellido de cada denunciante juntos, como un solo dato. Generá esa información.

5. En el sistema, el tipo de reclamo se cargó sin ningún control de formato. ¿Cuántas variantes "distintas" aparecen tal como están los datos? Una vez que identifiques y corrijas el problema, ¿cuántos tipos de reclamo hay en realidad?

6. El documento de la persona que hizo la denuncia tiene un problema parecido, pero de otro tipo. Dejalo representado de una forma única y consistente en todos los registros.

7. Con el documento ya corregido: ¿cuántas personas *distintas* hicieron al menos un reclamo? (Pensalo bien: no es necesariamente lo mismo que la cantidad total de reclamos.)

8. En el área sospechan que algunos reclamos quedaron cargados más de una vez por error, por una falla del sistema. Confirmá si eso ocurrió, y quedate con un único registro por cada reclamo real para el resto del análisis.

9. Las fechas de reclamo y de resolución están cargadas como texto, y no todas con el mismo formato. Dejalas en un formato que te permita trabajar con ellas como fechas.

10. ¿Cuántos reclamos todavía no tienen fecha de resolución? ¿Ese número tiene sentido en relación con alguna otra columna del dataset? Justificá tu respuesta.

11. Calculá cuántos días pasaron, para cada reclamo que ya se resolvió, entre la fecha del reclamo y su resolución. Revisá los resultados obtenidos: ¿te parecen razonables? Si encontrás algo que no debería pasar, explicá a qué podría deberse.

12. Una parte importante de los reclamos no tiene cargado un costo estimado. Completá esos valores faltantes con el criterio que te parezca más razonable, y justificá tu elección.

13. ¿Cuál es el costo estimado promedio para cada tipo de reclamo (ya corregido)? ¿Cuál es el tipo de reclamo más costoso, en promedio?

14. ¿En qué mes del año se concentran más reclamos?

15. El área de gestión quiere ver, de un vistazo, cuántos reclamos hay en cada estado (`Pendiente`, `En proceso`, `Resuelto`, `Desestimado`), separados por barrio. Armá esa información.

16. ¿El tiempo promedio de resolución cambia según la prioridad del reclamo? ¿El resultado es el que esperarías (que a mayor prioridad, menor tiempo de resolución)?

17. Con todo lo que encontraste, escribí un resumen breve (2 o 3 oraciones) con las conclusiones más relevantes, como si se lo tuvieras que presentar al área de Atención a la Ciudadanía.

## Al terminar

Podés comparar tus respuestas contra `solucion-proyecto-final.md`. Ahí vas a encontrar, para cada pregunta, la respuesta esperada y, si querés revisar cómo resolverla, el código correspondiente escondido en un desplegable — intentá responder primero por tu cuenta antes de abrirlo.
