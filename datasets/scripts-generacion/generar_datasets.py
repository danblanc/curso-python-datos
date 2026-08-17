"""
Generador de datasets sintéticos para el curso de Python.

Simula registros administrativos (personas, trámites, direcciones) con
"suciedad" intencional (nulos, duplicados, inconsistencias de formato,
texto sin normalizar) para practicar limpieza de datos con Pandas.

Uso:
    python generar_datasets.py

Genera archivos en:
    - datasets/raw/    (versión sucia, para practicar limpieza)
    - datasets/clean/  (versión limpia, para visualización/agregación)

Todos los datos son ficticios, generados con Faker (locale es_ES / es_AR).
No representan personas reales.
"""

import random
import string
from datetime import datetime, timedelta
from pathlib import Path

import numpy as np
import pandas as pd
from faker import Faker

# ---------------------------------------------------------------------------
# Configuración general
# ---------------------------------------------------------------------------

SEED = 42
random.seed(SEED)
np.random.seed(SEED)

fake = Faker("es_AR")
Faker.seed(SEED)

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "raw"
CLEAN_DIR = BASE_DIR / "clean"
RAW_DIR.mkdir(parents=True, exist_ok=True)
CLEAN_DIR.mkdir(parents=True, exist_ok=True)

N_PERSONAS = 600
N_TRAMITES = 1500

TIPOS_TRAMITE = [
    "Renovación de licencia",
    "Alta de comercio",
    "Baja de comercio",
    "Cambio de domicilio",
    "Solicitud de subsidio",
    "Inscripción registral",
    "Reclamo administrativo",
    "Certificado de residencia",
]

ESTADOS_TRAMITE = ["Iniciado", "En revisión", "Aprobado", "Rechazado", "Observado"]

PROVINCIAS = [
    "Buenos Aires", "Córdoba", "Santa Fe", "Mendoza", "Tucumán",
    "Entre Ríos", "Salta", "Chaco", "Misiones", "Neuquén",
]


# ---------------------------------------------------------------------------
# Utilidades para "ensuciar" datos de forma controlada
# ---------------------------------------------------------------------------

def maybe_none(value, p=0.05):
    """Devuelve None con probabilidad p, si no devuelve el valor original."""
    return None if random.random() < p else value


def variar_mayusculas(texto):
    """Introduce inconsistencia de mayúsculas/minúsculas."""
    if texto is None:
        return None
    opcion = random.choice(["upper", "lower", "title", "keep"])
    if opcion == "upper":
        return texto.upper()
    if opcion == "lower":
        return texto.lower()
    if opcion == "title":
        return texto.title()
    return texto


def agregar_espacios_extra(texto):
    """Agrega espacios extra al inicio/fin/medio, típico de carga manual."""
    if texto is None:
        return None
    if random.random() < 0.15:
        texto = f"  {texto}  "
    if random.random() < 0.1:
        texto = texto.replace(" ", "  ", 1)
    return texto


def variar_documento(doc):
    """Introduce formatos inconsistentes de documento (con/sin puntos, guiones)."""
    formato = random.choice(["plano", "puntos", "guion", "espacios"])
    doc_str = str(doc)
    if formato == "plano":
        return doc_str
    if formato == "puntos":
        return f"{doc_str[:2]}.{doc_str[2:5]}.{doc_str[5:]}"
    if formato == "guion":
        return f"{doc_str[:2]}-{doc_str[2:5]}-{doc_str[5:]}"
    return f"{doc_str[:2]} {doc_str[2:5]} {doc_str[5:]}"


def fecha_formato_random(fecha):
    """Devuelve la fecha como texto en distintos formatos comunes en cargas manuales."""
    if fecha is None:
        return None
    formatos = ["%Y-%m-%d", "%d/%m/%Y", "%d-%m-%Y", "%d/%m/%y"]
    return fecha.strftime(random.choice(formatos))


# ---------------------------------------------------------------------------
# Generación: PERSONAS
# ---------------------------------------------------------------------------

def generar_personas(n=N_PERSONAS):
    registros = []
    documentos_usados = set()

    for i in range(n):
        nombre = fake.first_name()
        apellido = fake.last_name()

        # Generar documento único de 8 dígitos
        while True:
            doc = random.randint(20000000, 45000000)
            if doc not in documentos_usados:
                documentos_usados.add(doc)
                break

        fecha_nac = fake.date_of_birth(minimum_age=18, maximum_age=90)

        registro = {
            "id_persona": i + 1,
            "documento": variar_documento(doc),
            "nombre": agregar_espacios_extra(variar_mayusculas(nombre)),
            "apellido": agregar_espacios_extra(variar_mayusculas(apellido)),
            "fecha_nacimiento": fecha_formato_random(fecha_nac),
            "email": maybe_none(fake.email(), p=0.08),
            "telefono": maybe_none(fake.phone_number(), p=0.12),
            "provincia": maybe_none(random.choice(PROVINCIAS), p=0.04),
            "direccion": agregar_espacios_extra(fake.street_address()),
        }
        registros.append(registro)

    df = pd.DataFrame(registros)

    # Duplicados intencionales (mismo documento, formato de nombre distinto)
    # para practicar detección de duplicados "no triviales"
    n_duplicados = int(n * 0.03)
    filas_a_duplicar = df.sample(n=n_duplicados, random_state=SEED).copy()
    filas_a_duplicar["nombre"] = filas_a_duplicar["nombre"].apply(
        lambda x: x.strip().upper() if x else x
    )
    filas_a_duplicar["id_persona"] = range(n + 1, n + 1 + n_duplicados)
    df = pd.concat([df, filas_a_duplicar], ignore_index=True)

    return df


# ---------------------------------------------------------------------------
# Generación: TRÁMITES
# ---------------------------------------------------------------------------

def generar_tramites(df_personas, n=N_TRAMITES):
    registros = []
    documentos = df_personas["documento"].tolist()

    fecha_inicio_rango = datetime(2023, 1, 1)
    fecha_fin_rango = datetime(2025, 12, 31)

    for i in range(n):
        doc = random.choice(documentos)
        fecha_inicio = fake.date_time_between(
            start_date=fecha_inicio_rango, end_date=fecha_fin_rango
        )
        estado = random.choice(ESTADOS_TRAMITE)

        # Fecha de resolución solo si el trámite no está "Iniciado"/"En revisión"
        if estado in ("Aprobado", "Rechazado", "Observado"):
            dias_resolucion = random.randint(1, 90)
            fecha_resolucion = fecha_inicio + timedelta(days=dias_resolucion)
        else:
            fecha_resolucion = None

        registro = {
            "id_tramite": i + 1,
            "documento_solicitante": variar_documento(doc) if random.random() < 0.5 else doc,
            "tipo_tramite": variar_mayusculas(random.choice(TIPOS_TRAMITE)),
            "estado": estado,
            "fecha_inicio": fecha_formato_random(fecha_inicio.date()),
            "fecha_resolucion": fecha_formato_random(
                fecha_resolucion.date()
            ) if fecha_resolucion else None,
            "monto_asociado": maybe_none(
                round(random.uniform(500, 50000), 2), p=0.3
            ),
            "provincia": random.choice(PROVINCIAS),
        }
        registros.append(registro)

    return pd.DataFrame(registros)


# ---------------------------------------------------------------------------
# Generación: DIRECCIONES (JSON, formato semi-estructurado)
# ---------------------------------------------------------------------------

def generar_direcciones(df_personas):
    registros = []
    for _, row in df_personas.drop_duplicates(subset="id_persona").iterrows():
        registros.append({
            "documento": row["documento"],
            "direccion_normalizada": None,  # se completa en clase de limpieza
            "direccion_original": row["direccion"],
            "provincia": row["provincia"],
            "codigo_postal": maybe_none(fake.postcode(), p=0.2),
        })
    return pd.DataFrame(registros)


# ---------------------------------------------------------------------------
# Versión limpia (para módulos de visualización / agregación / Streamlit)
# ---------------------------------------------------------------------------

def limpiar_personas(df):
    df = df.copy()
    df["nombre"] = df["nombre"].str.strip().str.title()
    df["apellido"] = df["apellido"].str.strip().str.title()
    df["documento"] = df["documento"].astype(str).str.replace(r"[.\-\s]", "", regex=True)
    df["documento"] = pd.to_numeric(df["documento"], errors="coerce")
    df = df.drop_duplicates(subset="documento", keep="first")
    df["fecha_nacimiento"] = pd.to_datetime(df["fecha_nacimiento"], errors="coerce", format="mixed")
    df["provincia"] = df["provincia"].fillna("Sin dato")
    return df.reset_index(drop=True)


def limpiar_tramites(df):
    df = df.copy()
    df["documento_solicitante"] = (
        df["documento_solicitante"].astype(str).str.replace(r"[.\-\s]", "", regex=True)
    )
    df["documento_solicitante"] = pd.to_numeric(df["documento_solicitante"], errors="coerce")
    df["tipo_tramite"] = df["tipo_tramite"].str.title()
    df["fecha_inicio"] = pd.to_datetime(df["fecha_inicio"], errors="coerce", format="mixed")
    df["fecha_resolucion"] = pd.to_datetime(df["fecha_resolucion"], errors="coerce", format="mixed")
    df["monto_asociado"] = df["monto_asociado"].fillna(0)
    return df.reset_index(drop=True)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("Generando dataset de personas...")
    df_personas = generar_personas()

    print("Generando dataset de trámites...")
    df_tramites = generar_tramites(df_personas)

    print("Generando dataset de direcciones...")
    df_direcciones = generar_direcciones(df_personas)

    # --- RAW (sucio, para practicar limpieza) ---
    df_personas.to_csv(RAW_DIR / "registros_personas.csv", index=False)
    df_tramites.to_excel(RAW_DIR / "registros_tramites.xlsx", index=False)
    df_direcciones.to_json(
        RAW_DIR / "registros_direcciones.json", orient="records", indent=2, force_ascii=False
    )
    print(f"Datasets RAW guardados en: {RAW_DIR}")

    # --- CLEAN (para módulos de visualización, agregación, Streamlit) ---
    df_personas_clean = limpiar_personas(df_personas)
    df_tramites_clean = limpiar_tramites(df_tramites)

    df_personas_clean.to_csv(CLEAN_DIR / "personas_clean.csv", index=False)
    df_tramites_clean.to_csv(CLEAN_DIR / "tramites_clean.csv", index=False)

    # Dataset combinado, útil para clases de visualización/Streamlit
    df_combinado = df_tramites_clean.merge(
        df_personas_clean,
        left_on="documento_solicitante",
        right_on="documento",
        how="left",
        suffixes=("_tramite", "_persona"),
    )
    df_combinado.to_csv(CLEAN_DIR / "tramites_personas_combinado.csv", index=False)

    print(f"Datasets CLEAN guardados en: {CLEAN_DIR}")
    print("\nResumen:")
    print(f"  - Personas (raw):   {len(df_personas)} filas")
    print(f"  - Trámites (raw):   {len(df_tramites)} filas")
    print(f"  - Direcciones:      {len(df_direcciones)} filas")
    print(f"  - Combinado (clean): {len(df_combinado)} filas")


if __name__ == "__main__":
    main()
