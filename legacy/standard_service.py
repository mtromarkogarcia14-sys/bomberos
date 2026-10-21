from sqlalchemy.orm import Session
from app.models import Standard, StandardSection, Requirement
from app.schemas import StandardCreate, StandardSectionCreate, RequirementCreate

def create_standard(db: Session, payload: StandardCreate):
    item = Standard(
        name=payload.name,
        jurisdiction=payload.jurisdiction,
        version=payload.version,
        description=payload.description
    )
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

def list_standards(db: Session):
    return db.query(Standard).all()

def create_section(db: Session, payload: StandardSectionCreate):
    item = StandardSection(
        standard_id=payload.standard_id,
        code=payload.code,
        title=payload.title,
        chapter=payload.chapter,
        summary=payload.summary
    )
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

def create_requirement(db: Session, payload: RequirementCreate):
    item = Requirement(
        section_id=payload.section_id,
        requirement_text=payload.requirement_text,
        applicability=payload.applicability,
        risk_type=payload.risk_type,
        category=payload.category
    )
    db.add(item)
    db.commit()
    db.refresh(item)
    return item