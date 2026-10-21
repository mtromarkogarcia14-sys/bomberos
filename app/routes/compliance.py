from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import NonConformityMunicipalCreate, NonConformityMunicipalRead
from app.services.compliance_service import (
    evaluate_case_against_requirements,
    add_non_conformity,
    get_compliance_for_case,
    get_non_conformities_for_case
)

router = APIRouter(prefix="/cases", tags=["compliance"])

@router.post("/{case_id}/municipal-evaluation")
def evaluate_case_municipal(case_id: int, municipality_id: int, db: Session = Depends(get_db)):
    return {
        "case_id": case_id,
        "municipality_id": municipality_id,
        "results": evaluate_case_against_requirements(db, case_id, municipality_id)
    }

@router.get("/{case_id}/municipal-evaluation")
def get_case_municipal_evaluation(case_id: int, db: Session = Depends(get_db)):
    return get_compliance_for_case(db, case_id)

@router.post("/{case_id}/non-conformities", response_model=NonConformityMunicipalRead)
def create_nonconformity(case_id: int, payload: NonConformityMunicipalCreate, db: Session = Depends(get_db)):
    if payload.case_id != case_id:
        raise HTTPException(status_code=400, detail="case_id mismatch")
    return add_non_conformity(
        db=db,
        case_id=case_id,
        municipality_id=payload.municipality_id,
        requirement_id=payload.requirement_id,
        description=payload.description,
        severity=payload.severity,
        recommendation=payload.recommendation
    )

@router.get("/{case_id}/non-conformities", response_model=list[NonConformityMunicipalRead])
def list_nonconformities(case_id: int, db: Session = Depends(get_db)):
    return get_non_conformities_for_case(db, case_id)