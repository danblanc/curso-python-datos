# Solución — Ejercicio 9 (Clase 9)

> Valores correspondientes a los datasets del curso generados con `SEED = 42`.

```python
import pandas as pd
import re

# --- Parte 1 ---
personas = pd.read_csv("datasets/raw/registros_personas.csv")
tramites = pd.read_excel("datasets/raw/registros_tramites.xlsx")

def normalizar_documento(doc):
    if pd.isnull(doc):
        return None
    return re.sub(r"[^\d]", "", str(doc))

personas["documento_normalizado"] = pd.to_numeric(
    personas["documento"].apply(normalizar_documento), errors="coerce"
)
tramites["documento_normalizado"] = pd.to_numeric(
    tramites["documento_solicitante"].apply(normalizar_documento), errors="coerce"
)

# --- Parte 2 ---
duplicados_personas = personas.duplicated(subset=["documento_normalizado"]).sum()
print("Duplicados en personas:", duplicados_personas)   # 18

personas_dedup = personas.drop_duplicates(subset=["documento_normalizado"], keep="first")
print("Personas tras deduplicar:", len(personas_dedup))   # 600 (618 - 18)

# --- Parte 3 ---
tramites["fecha_inicio"] = pd.to_datetime(
    tramites["fecha_inicio"], format="mixed", dayfirst=True, errors="coerce"
)
tramites["fecha_resolucion"] = pd.to_datetime(
    tramites["fecha_resolucion"], format="mixed", dayfirst=True, errors="coerce"
)

combinado = pd.merge(
    tramites, personas_dedup,
    on="documento_normalizado", how="left",
    indicator=True, suffixes=("_tramite", "_persona"),
)

print(combinado["_merge"].value_counts())
# both: 1500, left_only: 0, right_only: 0
# -> los 1500 trámites encontraron una persona correspondiente; no hay
# trámites "huérfanos" en este dataset en particular.

print("Filas del combinado:", len(combinado), "vs trámites original:", len(tramites))
# 1500 vs 1500 -> el merge NO multiplicó filas, justamente porque ya
# habíamos deduplicado personas_dedup antes de este paso.

# --- Parte 4 ---
combinado["tipo_tramite_normalizado"] = combinado["tipo_tramite"].str.strip().str.lower()

monto_por_provincia = combinado.groupby("provincia_tramite")["monto_asociado"].sum().sort_values(ascending=False)
print(monto_por_provincia)

resumen_doble = combinado.groupby(["tipo_tramite_normalizado", "estado"])["monto_asociado"].agg(["sum", "count"])
print(resumen_doble)

# Personas sin ningún trámite: merge en sentido inverso
combinado_inverso = pd.merge(
    personas_dedup, tramites,
    on="documento_normalizado", how="left", indicator=True,
)
sin_tramites = combinado_inverso[combinado_inverso["_merge"] == "left_only"]
print("Personas sin ningún trámite:", len(sin_tramites))   # 58 de 600

# --- Parte 5 (opcional) ---
direcciones = pd.read_json("datasets/raw/registros_direcciones.json")
direcciones["documento_normalizado"] = pd.to_numeric(
    direcciones["documento"].apply(normalizar_documento), errors="coerce"
)

# OJO: direcciones también tiene 18 duplicados (por el mismo motivo que
# personas). Si combinás sin deduplicar los dos lados, el resultado se
# infla:
combinado_dir_mal = pd.merge(
    personas_dedup, direcciones, on="documento_normalizado", how="left"
)
print("Filas SIN deduplicar direcciones:", len(combinado_dir_mal))   # 618 (¡mal!)

# La forma correcta: deduplicar TAMBIÉN direcciones antes de combinar
direcciones_dedup = direcciones.drop_duplicates(subset=["documento_normalizado"], keep="first")
combinado_dir_ok = pd.merge(
    personas_dedup, direcciones_dedup,
    on="documento_normalizado", how="left", suffixes=("_persona", "_direccion"),
)
print("Filas deduplicando ambos lados:", len(combinado_dir_ok))   # 600 (correcto)
```

## Nota para el docente

La Parte 5 (opcional) esconde una lección importante que conecta directamente con la advertencia de la slide "El riesgo de duplicar filas en un merge": **no alcanza con deduplicar un solo lado del merge**. Si alguien del grupo llega a esta parte y no le da 600 sino 618, es una excelente oportunidad para remarcar en vivo que el dataset de direcciones **también** tiene los mismos 18 duplicados que personas (porque ambos se generaron a partir de la misma fuente), y que hay que revisar duplicados en **cada** tabla que participa de un merge, no solo en la primera.

Si el grupo no llega a la Parte 5 por tiempo, no hay problema — es explícitamente opcional y el contenido central de la clase (Partes 1 a 4) queda cubierto igual.
