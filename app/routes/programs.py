from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import InternalProgramCreate, InternalProgramRead, MunicipalRequirementCreate, MunicipalRequirementRead
from app.services.program_service import create_program, list_programs, create_requirement, list_requirements

router = APIRouter(prefix="/municipalities", tags=["programs"])

@router.post("/{municipality_id}/programs", response_model=InternalProgramRead)
def add_program(municipality_id: int, payload: InternalProgramCreate, db: Session = Depends(get_db)):
    if payload.municipality_id != municipality_id:
        raise ValueError("municipality_id mismatch")
    return create_program(db, payload)

@router.get("/{municipality_id}/programs", response_model=list[InternalProgramRead])
def get_programs(municipality_id: int, db: Session = Depends(get_db)):
    return list_programs(db, municipality_id)

@router.post("/{municipality_id}/requirements", response_model=MunicipalRequirementRead)
def add_requirement(municipality_id: int, payload: MunicipalRequirementCreate, db: Session = Depends(get_db)):
    if payload.municipality_id != municipality_id:
        raise ValueError("municipality_id mismatch")
    return create_requirement(db, payload)

@router.get("/{municipality_id}/requirements", response_model=list[MunicipalRequirementRead])
def get_requirements(municipality_id: int, db: Session = Depends(get_db)):
    return list_requirements(db, municipality_id)