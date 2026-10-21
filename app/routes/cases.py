from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import InvestigationCase, Evidence
from app.schemas import CaseCreate, CaseRead, EvidenceCreate, EvidenceRead

router = APIRouter(prefix="/cases", tags=["cases"])

@router.post("/", response_model=CaseRead)
def create_case(payload: CaseCreate, db: Session = Depends(get_db)):
    case = InvestigationCase(
        municipality_id=payload.municipality_id,
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

@router.get("/", response_model=list[CaseRead])
def get_cases(db: Session = Depends(get_db)):
    return db.query(InvestigationCase).all()

@router.get("/{case_id}", response_model=CaseRead)
def get_one(case_id: int, db: Session = Depends(get_db)):
    case = db.query(InvestigationCase).filter(InvestigationCase.id == case_id).first()
    if not case:
        raise HTTPException(status_code=404, detail="Case not found")
    return case

@router.post("/{case_id}/evidence", response_model=EvidenceRead)
def add_case_evidence(case_id: int, payload: EvidenceCreate, db: Session = Depends(get_db)):
    if payload.case_id != case_id:
        raise HTTPException(status_code=400, detail="case_id mismatch")
    item = Evidence(
        case_id=payload.case_id,
        evidence_type=payload.evidence_type,
        title=payload.title,
        file_path=payload.file_path,
        metadata_json=payload.metadata,
        extracted_text=payload.extracted_text,
        source=payload.source
    )
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

@router.get("/{case_id}/evidence", response_model=list[EvidenceRead])
def case_evidence(case_id: int, db: Session = Depends(get_db)):
    return db.query(Evidence).filter(Evidence.case_id == case_id).all()