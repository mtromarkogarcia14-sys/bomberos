from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import ComplianceCheckCreate, ComplianceCheckRead, NonConformityCreate, NonConformityRead
from app.services.compliance_service import (
    evaluate_case_against_requirements,
    add_non_conformity,
    get_compliance_for_case,
    get_non_conformities_for_case
)

router = APIRouter(prefix="/compliance", tags=["compliance"])

@router.post("/cases/{case_id}")
def run_compliance(case_id: int, db: Session = Depends(get_db)):
    return {
        "case_id": case_id,
        "results": evaluate_case_against_requirements(db, case_id)
    }

@router.get("/cases/{case_id}", response_model=list[ComplianceCheckRead])
def read_compliance(case_id: int, db: Session = Depends(get_db)):
    return get_compliance_for_case(db, case_id)

@router.post("/cases/{case_id}/non-conformities", response_model=NonConformityRead)
def create_non_conformity(case_id: int, payload: NonConformityCreate, db: Session = Depends(get_db)):
    if payload.case_id != case_id:
        raise ValueError("case_id mismatch")
    return add_non_conformity(
        db,
        case_id=case_id,
        requirement_id=payload.requirement_id,
        description=payload.description,
        severity=payload.severity,
        recommendation=payload.recommendation
    )

@router.get("/cases/{case_id}/non-conformities", response_model=list[NonConformityRead])
def read_non_conformities(case_id: int, db: Session = Depends(get_db)):
    return get_non_conformities_for_case(db, case_id)