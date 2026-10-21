from sqlalchemy.orm import Session
from app.models import InternalProgram, MunicipalRequirement
from app.schemas import InternalProgramCreate, MunicipalRequirementCreate

def create_program(db: Session, payload: InternalProgramCreate):
    item = InternalProgram(
        municipality_id=payload.municipality_id,
        name=payload.name,
        program_type=payload.program_type,
        objective=payload.objective,
        frequency=payload.frequency,
        responsible=payload.responsible,
        status=payload.status
    )
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

def list_programs(db: Session, municipality_id: int):
    return db.query(InternalProgram).filter(InternalProgram.municipality_id == municipality_id).all()

def create_requirement(db: Session, payload: MunicipalRequirementCreate):
    item = MunicipalRequirement(
        municipality_id=payload.municipality_id,
        program_id=payload.program_id,
        requirement_text=payload.requirement_text,
        requirement_type=payload.requirement_type,
        evidence_required=payload.evidence_required,
        source_reference=payload.source_reference,
        category=payload.category
    )
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

def list_requirements(db: Session, municipality_id: int):
    return db.query(MunicipalRequirement).filter(MunicipalRequirement.municipality_id == municipality_id).all()