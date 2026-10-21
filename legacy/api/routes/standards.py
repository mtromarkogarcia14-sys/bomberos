from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import StandardCreate, StandardRead, StandardSectionCreate, StandardSectionRead, RequirementCreate, RequirementRead
from app.services.standard_service import create_standard, list_standards, create_section, create_requirement

router = APIRouter(prefix="/standards", tags=["standards"])

@router.post("/", response_model=StandardRead)
def add_standard(payload: StandardCreate, db: Session = Depends(get_db)):
    return create_standard(db, payload)

@router.get("/", response_model=list[StandardRead])
def get_standards(db: Session = Depends(get_db)):
    return list_standards(db)

@router.post("/sections", response_model=StandardSectionRead)
def add_section(payload: StandardSectionCreate, db: Session = Depends(get_db)):
    return create_section(db, payload)

@router.post("/requirements", response_model=RequirementRead)
def add_requirement(payload: RequirementCreate, db: Session = Depends(get_db)):
    return create_requirement(db, payload)