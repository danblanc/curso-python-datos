---
marp: true
theme: default
paginate: true
size: 16:9
---

# Clase 7
## Pandas: limpieza de texto

Curso de Python para Análisis de Datos

---

# Agenda de hoy

1. El accesor `.str`
2. Mayúsculas, espacios, tildes
3. Expresiones regulares básicas
4. Normalización de identificadores
5. Por qué esto es clave para el curso
6. Ejercicio práctico

---

# El problema que dejamos abierto

En la clase anterior vimos que el mismo documento puede estar escrito como:

```
30123456
30.123.456
30-123-456
30 123 456
```

Para Pandas, estos son **4 strings distintos**. Hoy vemos cómo normalizarlos a un único formato.

---

# El accesor `.str`

Pandas permite aplicar métodos de texto de Python a **toda una columna a la vez**, sin necesidad de `.apply()`:

```python
df["nombre"].str.upper()
df["nombre"].str.lower()
df["nombre"].str.strip()
df["nombre"].str.len()
```

Es la forma vectorizada (más eficiente y más legible) de trabajar con texto en Pandas.

---

# Mayúsculas y minúsculas

```python
df["nombre"] = df["nombre"].str.strip()      # quita espacios al inicio/fin
df["nombre"] = df["nombre"].str.title()       # "ana maria" -> "Ana Maria"
df["nombre"] = df["nombre"].str.upper()       # "Ana Maria" -> "ANA MARIA"
df["nombre"] = df["nombre"].str.lower()       # "Ana Maria" -> "ana maria"
```

`.title()` es especialmente útil para nombres propios cargados en mayúscula o minúscula sin criterio consistente.

---

# Espacios extra (más allá del `.strip()`)

`.strip()` solo quita espacios al **inicio y al final**. Para espacios duplicados en el medio del texto:

```python
df["nombre"] = df["nombre"].str.strip()
df["nombre"] = df["nombre"].str.replace(r"\s+", " ", regex=True)
```

`\s+` es nuestra primera expresión regular: significa "uno o más espacios seguidos".

---

# El problema de las tildes

```python
"Córdoba" != "Cordoba"    # True, para Python son distintos
```

En registros administrativos, es común que la misma palabra aparezca con y sin tilde por errores de carga o distintos sistemas de origen.

---

# Normalizar tildes (Unicode)

```python
import unicodedata

def quitar_tildes(texto):
    if texto is None:
        return None
    nfkd = unicodedata.normalize("NFKD", texto)
    return "".join(c for c in nfkd if not unicodedata.combining(c))

df["provincia_sin_tildes"] = df["provincia"].apply(quitar_tildes)
```

`unicodedata` es un módulo de la librería estándar de Python (no requiere instalación).

---

# ¿Qué son las expresiones regulares?

Un **patrón** que describe una forma de texto, para buscar, validar o reemplazar contenido que cumple ese patrón.

```python
import re

texto = "Documento: 30123456"
patron = r"\d+"                    # \d = un dígito, + = uno o más
resultado = re.findall(patron, texto)
print(resultado)   # ['30123456']
```

No hace falta dominarlas a fondo — con un puñado de símbolos básicos ya se resuelve el 90% de los casos en limpieza de datos.

---

# Símbolos básicos de regex

| Símbolo | Significado |
|---|---|
| `\d` | un dígito (0-9) |
| `\s` | un espacio |
| `+` | uno o más del elemento anterior |
| `*` | cero o más del elemento anterior |
| `[abc]` | cualquiera de los caracteres a, b o c |
| `[^abc]` | cualquier caracter que NO sea a, b o c |
| `.` | cualquier caracter |

---

# Regex en Pandas: `.str.replace()`

```python
# Eliminar todo lo que NO sea un dígito
df["documento_limpio"] = df["documento"].str.replace(r"[^\d]", "", regex=True)
```

`[^\d]` significa "cualquier caracter que no sea un dígito" — así eliminamos puntos, guiones y espacios de una sola vez, sin importar cuál de los 4 formatos tenía cada fila.

---

# Verificando el resultado

```python
print(df["documento"].head())
# 0    30.123.456
# 1    30-123-456
# 2    30 123 456

print(df["documento_limpio"].head())
# 0    30123456
# 1    30123456
# 2    30123456
```

Ahora sí, los 3 formatos distintos quedan representados de la misma forma — y recién ahí se pueden comparar o convertir a numérico de forma confiable.

---

# `.str.extract()`: extraer patrones

Cuando necesitamos **extraer** una parte específica del texto, no solo limpiar:

```python
df["codigo_area"] = df["telefono"].str.extract(r"(\d{2,4})\s")
```

Esto extrae el primer grupo de 2 a 4 dígitos seguido de un espacio — por ejemplo, el código de área de un teléfono.

---

# Reconstruyendo la normalización completa

```python
def normalizar_documento(doc):
    if pd.isnull(doc):
        return None
    return re.sub(r"[^\d]", "", str(doc))

df["documento_normalizado"] = df["documento"].apply(normalizar_documento)
df["documento_normalizado"] = pd.to_numeric(
    df["documento_normalizado"], errors="coerce"
)
```

Con esta columna ya podemos, por ejemplo, detectar los duplicados "no triviales" de la clase anterior correctamente.

---

# Verificando el efecto de normalizar

```python
ejemplo = pd.DataFrame({
    "documento": ["30123456", "30.123.456"],
    "nombre": ["Ana Gomez", "ANA GOMEZ"],
})

ejemplo.duplicated(subset=["documento"]).sum()              # 0 -> no detecta nada
ejemplo["documento_normalizado"] = ejemplo["documento"].apply(normalizar_documento)
ejemplo.duplicated(subset=["documento_normalizado"]).sum()   # 1 -> ahora sí

```

Dos registros que representan a la **misma persona** solo se detectan como duplicados **después** de normalizar el formato — antes, para Pandas, son simplemente strings distintos.

---

# ¿Por qué esta clase es tan importante?

El curso que sigue a este (fuera de este programa) trabaja con **técnicas de similitud de registros administrativos**: comparar personas, direcciones o trámites que deberían ser "la misma entidad" aunque estén escritos de forma distinta.

**Ninguna técnica de similitud funciona bien sobre texto sucio.** La normalización que vimos hoy es el trabajo previo obligatorio para que esas técnicas tengan sentido.

---

# Buenas prácticas de normalización

- Definir un **criterio único** de normalización por tipo de dato (documentos, nombres, direcciones) y aplicarlo siempre igual
- Guardar tanto el valor original como el normalizado (no perder la trazabilidad)
- Documentar las reglas de normalización usadas (para que el proceso sea reproducible)

---

# Resumen de la clase

- `.str` permite aplicar métodos de texto vectorizados sobre columnas completas
- Tildes, mayúsculas y espacios son fuentes comunes de inconsistencia
- Expresiones regulares básicas resuelven la mayoría de los casos de limpieza
- Esta normalización es el paso previo obligatorio antes de comparar/vincular registros

---

# Ejercicio práctico

30-40 minutos — ver [`ejercicios/ejercicio-07.md`](./ejercicios/ejercicio-07.md)
