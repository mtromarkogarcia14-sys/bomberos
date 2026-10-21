from sqlalchemy.orm import Session
from app.models import InvestigationCase
from app.schemas import CaseCreate

def create_case(db: Session, payload: CaseCreate):
    case = InvestigationCase(
        name=payload.name,
        case_type=payload.case_type,
        location=payload.location,
        incident_date=payload.incident_date,
        summary=payload.summary
    )
    db.add(case)
    db.commit()
    db.refresh(case)
    return case

def get_case(db: Session, case_id: int):
    return db.query(InvestigationCase).filter(InvestigationCase.id == case_id).first()

def list_cases(db: Session):
    return db.query(InvestigationCase).all()