from sqlalchemy.orm import Session
from app.models import Municipality, MunicipalRegulation
from app.schemas import MunicipalityCreate, MunicipalRegulationCreate

def create_municipality(db: Session, payload: MunicipalityCreate):
    item = Municipality(
        name=payload.name,
        state=payload.state,
        authority_protection_civil=payload.authority_protection_civil,
        authority_bomberos=payload.authority_bomberos,
        regulation_reference=payload.regulation_reference,
        regulation_version=payload.regulation_version
    )
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

def list_municipalities(db: Session):
    return db.query(Municipality).all()

def get_municipality(db: Session, municipality_id: int):
    return db.query(Municipality).filter(Municipality.id == municipality_id).first()

def create_regulation(db: Session, payload: MunicipalRegulationCreate):
    item = MunicipalRegulation(
        municipality_id=payload.municipality_id,
        name=payload.name,
        regulation_type=payload.regulation_type,
        version=payload.version,
        document_url=payload.document_url,
        description=payload.description
    )
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

def list_regulations(db: Session, municipality_id: int):
    return db.query(MunicipalRegulation).filter(MunicipalRegulation.municipality_id == municipality_id).all()