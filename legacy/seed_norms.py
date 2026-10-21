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
    title="Instalaciones eléctricas y seguridad",
    chapter="General",
    summary="Requisitos de seguridad eléctrica"
)
db.add(section1)
db.commit()
db.refresh(section1)

db.add(Requirement(
    section_id=section1.id,
    requirement_text="Debe existir documentación de mantenimiento y revisiones del sistema eléctrico.",
    applicability="electric",
    risk_type="electrical",
    category="electrical"
))

db.add(Requirement(
    section_id=section1.id,
    requirement_text="Debe existir protección adecuada para paneles y circuitos para evitar fallas y cortocircuitos.",
    applicability="electric",
    risk_type="electrical",
    category="electrical"
))

# NOM ejemplo
nom = Standard(name="NOM-018-STPS-2015", jurisdiction="mexico", version="2015", description="Requisitos de seguridad")
db.add(nom)
db.commit()
db.refresh(nom)

sec_nom = StandardSection(
    standard_id=nom.id,
    code="NOM-018-1",
    title="Evacuación y protección contra incendios",
    chapter="Seguridad",
    summary="Evaluación de rutas de evacuación y prevención"
)
db.add(sec_nom)
db.commit()
db.refresh(sec_nom)

db.add(Requirement(
    section_id=sec_nom.id,
    requirement_text="Debe existir señalización y rutas de evacuación funcionales.",
    applicability="evacuation",
    risk_type="evacuation",
    category="evacuation"
))

db.add(Requirement(
    section_id=sec_nom.id,
    requirement_text="Debe existir registro de inspecciones y mantenimiento del sistema de protección.",
    applicability="safety",
    risk_type="fire_systems",
    category="fire_systems"
))

db.commit()
print("Normas cargadas correctamente.")