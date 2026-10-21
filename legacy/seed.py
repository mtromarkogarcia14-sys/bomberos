from app.database import SessionLocal, Base, engine
from app.models import Standard, StandardSection, Requirement

Base.metadata.create_all(bind=engine)
db = SessionLocal()

# NFPA 70
nfpa70 = Standard(name="NFPA 70", jurisdiction="nfpa", version="2023", description="Instalaciones eléctricas")
db.add(nfpa70)
db.commit()
db.refresh(nfpa70)

section1 = StandardSection(
    standard_id=nfpa70.id,
    code="70-1",
    title="Instalaciones eléctricas",
    chapter="General",
    summary="Mantenimiento, protección y seguridad del sistema eléctrico"
)
db.add(section1)
db.commit()
db.refresh(section1)

db.add(Requirement(
    section_id=section1.id,
    requirement_text="Debe existir documentación de mantenimiento del sistema eléctrico.",
    applicability="electric",
    risk_type="electrical",
    category="electrical"
))
db.add(Requirement(
    section_id=section1.id,
    requirement_text="Debe existir protección adecuada del panel y circuitos para evitar cortocircuitos.",
    applicability="electric",
    risk_type="electrical",
    category="electrical"
))

# NFPA 101
nfpa101 = Standard(name="NFPA 101", jurisdiction="nfpa", version="2021", description="Vida segura / evacuación")
db.add(nfpa101)
db.commit()
db.refresh(nfpa101)

section2 = StandardSection(
    standard_id=nfpa101.id,
    code="101-1",
    title="Evacuación",
    chapter="Seguridad",
    summary="Rutas de evacuación, señalización y entrenamiento"
)
db.add(section2)
db.commit()
db.refresh(section2)

db.add(Requirement(
    section_id=section2.id,
    requirement_text="Debe existir señalización y rutas de evacuación funcionales.",
    applicability="evacuation",
    risk_type="evacuation",
    category="evacuation"
))
db.add(Requirement(
    section_id=section2.id,
    requirement_text="Debe existir simulacro o entrenamiento para evacuaciones.",
    applicability="evacuation",
    risk_type="evacuation",
    category="evacuation"
))

# NOM
nom = Standard(name="NOM-018-STPS-2015", jurisdiction="mexico", version="2015", description="Seguridad en el trabajo y protección contra incendios")
db.add(nom)
db.commit()
db.refresh(nom)

section3 = StandardSection(
    standard_id=nom.id,
    code="NOM-018-1",
    title="Protección contra incendios y evacuación",
    chapter="Seguridad",
    summary="Se requiere mantenimiento e inspección de sistemas y rutas"
)
db.add(section3)
db.commit()
db.refresh(section3)

db.add(Requirement(
    section_id=section3.id,
    requirement_text="Debe existir mantenimiento e inspección documental de sistemas de protección contra incendios.",
    applicability="fire_systems",
    risk_type="fire_systems",
    category="fire_systems"
))
db.add(Requirement(
    section_id=section3.id,
    requirement_text="Debe existir señalización y rutas de evacuación funcionales.",
    applicability="evacuation",
    risk_type="evacuation",
    category="evacuation"
))

db.commit()
print("Seeds loaded successfully.")