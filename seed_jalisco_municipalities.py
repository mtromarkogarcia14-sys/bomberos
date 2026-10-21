from app.database import Base, engine, SessionLocal
from app.models import Municipality, MunicipalRegulation, InternalProgram, MunicipalRequirement

Base.metadata.create_all(bind=engine)

db = SessionLocal()

municipalities = [
    {
        "name": "Guadalajara",
        "state": "Jalisco",
        "authority_protection_civil": "Protección Civil de Guadalajara",
        "authority_bomberos": "Bomberos Guadalajara",
        "regulation_reference": "Reglamento Interno de Protección Civil",
        "regulation_version": "2024"
    },
    {
        "name": "Zapopan",
        "state": "Jalisco",
        "authority_protection_civil": "Protección Civil de Zapopan",
        "authority_bomberos": "Bomberos Zapopan",
        "regulation_reference": "Reglamento Interno de Protección Civil",
        "regulation_version": "2024"
    },
    {
        "name": "Tonalá",
        "state": "Jalisco",
        "authority_protection_civil": "Protección Civil de Tonalá",
        "authority_bomberos": "Bomberos Tonalá",
        "regulation_reference": "Reglamento Interno de Protección Civil",
        "regulation_version": "2024"
    },
    {
        "name": "Tlaquepaque",
        "state": "Jalisco",
        "authority_protection_civil": "Protección Civil de Tlaquepaque",
        "authority_bomberos": "Bomberos Tlaquepaque",
        "regulation_reference": "Reglamento Interno de Protección Civil",
        "regulation_version": "2024"
    }
]

for item in municipalities:
    mu = Municipality(
        name=item["name"],
        state=item["state"],
        authority_protection_civil=item["authority_protection_civil"],
        authority_bomberos=item["authority_bomberos"],
        regulation_reference=item["regulation_reference"],
        regulation_version=item["regulation_version"]
    )
    db.add(mu)
    db.commit()
    db.refresh(mu)

    regulation = MunicipalRegulation(
        municipality_id=mu.id,
        name=item["regulation_reference"],
        regulation_type="protection_civil",
        version=item["regulation_version"],
        description=f"Reglamento interno de Protección Civil para {mu.name}",
        document_url="https://example.com/reglamento"
    )
    db.add(regulation)
    db.commit()

    program = InternalProgram(
        municipality_id=mu.id,
        name="Programa Interno de Brigada y Evacuación",
        program_type="brigade",
        objective="Prevención, evacuación y respuesta inmediata",
        frequency="Semestral",
        responsible="Responsable de seguridad",
        status="active"
    )
    db.add(program)
    db.commit()
    db.refresh(program)

    requirements = [
        {
            "requirement_text": "Debe existir inspección documental y física del sitio",
            "requirement_type": "mandatory",
            "evidence_required": "Actas de inspección, fotografías, registro",
            "source_reference": item["regulation_reference"],
            "category": "inspection"
        },
        {
            "requirement_text": "Debe existir señalización y rutas de evacuación funcionales",
            "requirement_type": "mandatory",
            "evidence_required": "Plano de evacuación, señalización",
            "source_reference": item["regulation_reference"],
            "category": "evacuation"
        },
        {
            "requirement_text": "Debe existir capacitación y brigada para respuesta inicial",
            "requirement_type": "mandatory",
            "evidence_required": "Lista de asistencia, programas de entrenamiento",
            "source_reference": item["regulation_reference"],
            "category": "training"
        },
        {
            "requirement_text": "Debe existir mantenimiento documental de instalaciones eléctricas",
            "requirement_type": "mandatory",
            "evidence_required": "Reportes de mantenimiento, inspección eléctrica",
            "source_reference": item["regulation_reference"],
            "category": "electrical"
        },
        {
            "requirement_text": "Debe existir mantenimiento y prueba de equipos de protección contra incendios",
            "requirement_type": "mandatory",
            "evidence_required": "Extintores, alarmas, rociadores, registros",
            "source_reference": item["regulation_reference"],
            "category": "fire_systems"
        }
    ]

    for req in requirements:
        db.add(MunicipalRequirement(
            municipality_id=mu.id,
            program_id=program.id,
            requirement_text=req["requirement_text"],
            requirement_type=req["requirement_type"],
            evidence_required=req["evidence_required"],
            source_reference=req["source_reference"],
            category=req["category"]
        ))

db.commit()
print("Municipios de Jalisco cargados con programa interno y requisitos.")