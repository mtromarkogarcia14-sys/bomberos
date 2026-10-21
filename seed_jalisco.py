from app.database import Base, engine, SessionLocal
from app.models import Municipality, MunicipalRegulation, InternalProgram, MunicipalRequirement

Base.metadata.create_all(bind=engine)
db = SessionLocal()

# Municipio de ejemplo: Guadalajara
mu = Municipality(
    name="Guadalajara",
    state="Jalisco",
    authority_protection_civil="Protección Civil de Guadalajara",
    authority_bomberos="Bomberos Guadalajara",
    regulation_reference="Reglamento Interno de Protección Civil",
    regulation_version="2024"
)
db.add(mu)
db.commit()
db.refresh(mu)

# Reglamento
reg = MunicipalRegulation(
    municipality_id=mu.id,
    name="Reglamento Interno de Protección Civil",
    regulation_type="protection_civil",
    version="2024",
    document_url="https://example.com/guadalajara/proteccion-civil",
    description="Programa de prevención y evacuación"
)
db.add(reg)
db.commit()
db.refresh(reg)

# Programa
program = InternalProgram(
    municipality_id=mu.id,
    name="Programa Interno de Brigada contra Incendios",
    program_type="brigade",
    objective="Preparar a la organización para responder ante incendios y evacuaciones",
    frequency="Semestral",
    responsible="Responsable de seguridad",
    status="active"
)
db.add(program)
db.commit()
db.refresh(program)

# Requisitos
requirements = [
    {
        "requirement_text": "Debe existir inspección documental y física de la instalación.",
        "requirement_type": "mandatory",
        "evidence_required": "Actas, fotografías, registro de inspección",
        "source_reference": "Reglamento Interno de Protección Civil",
        "category": "inspection"
    },
    {
        "requirement_text": "Debe existir señalización y rutas de evacuación funcionales.",
        "requirement_type": "mandatory",
        "evidence_required": "Plano, señalización, simulacro",
        "source_reference": "Reglamento Interno de Protección Civil",
        "category": "evacuation"
    },
    {
        "requirement_text": "Debe existir capacitación y brigada contra incendios documentada.",
        "requirement_type": "mandatory",
        "evidence_required": "Registro de capacitación, listas de asistencia",
        "source_reference": "Reglamento Interno de Protección Civil",
        "category": "training"
    },
    {
        "requirement_text": "Debe existir mantenimiento documental de instalaciones eléctricas.",
        "requirement_type": "mandatory",
        "evidence_required": "Reporte de mantenimiento de paneles y circuitos",
        "source_reference": "Reglamento Interno de Bomberos",
        "category": "electrical"
    },
    {
        "requirement_text": "Debe existir mantenimiento y prueba de equipos de protección contra incendios.",
        "requirement_type": "mandatory",
        "evidence_required": "Extintores, alarmas, rociadores, mantenimiento",
        "source_reference": "Reglamento Interno de Bomberos",
        "category": "fire_systems"
    }
]

for item in requirements:
    db.add(MunicipalRequirement(
        municipality_id=mu.id,
        program_id=program.id,
        requirement_text=item["requirement_text"],
        requirement_type=item["requirement_type"],
        evidence_required=item["evidence_required"],
        source_reference=item["source_reference"],
        category=item["category"]
    ))

db.commit()
print("Seed de Guadalajara cargado correctamente.")