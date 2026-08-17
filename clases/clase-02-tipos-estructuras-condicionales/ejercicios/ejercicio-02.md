# Ejercicio 2 — Modelando un registro administrativo

**Duración estimada:** 30-40 minutos

## Objetivo

Practicar el uso de variables, tipos de datos, estructuras nativas (listas y diccionarios) y condicionales, modelando un caso cercano al dominio del curso: un registro administrativo simple.

## Consigna

Trabajá en un archivo `ejercicio_02.py` (o una notebook, como prefieras).

### Parte 1 — Modelar una persona

1. Creá un diccionario `persona` con las siguientes claves: `nombre`, `apellido`, `edad`, `documento`, `provincia`.
2. Imprimí un mensaje usando varias de esas claves, por ejemplo:
   ```
   Ana Gómez, 34 años, DNI 30123456, reside en Córdoba.
   ```

### Parte 2 — Validaciones con condicionales

3. Escribí un condicional que imprima `"Mayor de edad"` si `persona["edad"]` es mayor o igual a 18, y `"Menor de edad"` en caso contrario.
4. Escribí un condicional que verifique si `persona["provincia"]` es `"Córdoba"` **o** `"Santa Fe"`, e imprima `"Zona centro"` si se cumple, y `"Otra zona"` si no.

### Parte 3 — Lista de personas

5. Creá una lista llamada `personas` con al menos 4 diccionarios como el de la Parte 1 (podés inventar los datos), cada uno con distintas edades y provincias.
6. Recorré la lista **manualmente, sin usar un `for`** (todavía no lo vimos) accediendo por índice (`personas[0]`, `personas[1]`, etc.) e imprimí el nombre de cada persona.

### Parte 4 — Sets

7. A partir de la lista `personas`, creá un set llamado `provincias_unicas` que contenga, sin duplicados, las provincias presentes en la lista. (Pista: podés ir agregando cada provincia con `.add()`, accediendo persona por persona con índice, igual que en la Parte 3.)
8. Imprimí cuántas provincias distintas hay, usando `len()`.

### Parte 5 — Para pensar

Respondé en un comentario al final del archivo:

- ¿Por qué en la Parte 3 tuvimos que acceder "a mano" a cada persona de la lista, en vez de hacerlo de forma más automática? (No hace falta que sepas la respuesta técnica todavía — es una reflexión para conectar con la próxima clase.)

## Qué se evalúa

- Uso correcto de diccionarios y listas.
- Condicionales que evalúan correctamente las condiciones pedidas (incluyendo el uso de `or`).
- Uso correcto de un set para eliminar duplicados.

## Ayuda

Solución de referencia en [`soluciones/clase-02/`](../../../soluciones/clase-02/).
