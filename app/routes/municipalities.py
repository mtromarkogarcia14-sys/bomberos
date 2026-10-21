from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import MunicipalityCreate, MunicipalityRead, MunicipalRegulationCreate, MunicipalRegulationRead
from app.services.municipality_service import create_municipality, list_municipalities, get_municipality, create_regulation, list_regulations

router = APIRouter(prefix="/municipalities", tags=["municipalities"])

@router.post("/", response_model=MunicipalityRead)
def add_municipality(payload: MunicipalityCreate, db: Session = Depends(get_db)):
    return create_municipality(db, payload)

@router.get("/", response_model=list[MunicipalityRead])
def get_all(db: Session = Depends(get_db)):
    return list_municipalities(db)

@router.get("/{municipality_id}", response_model=MunicipalityRead)
def get_one(municipality_id: int, db: Session = Depends(get_db)):
    item = get_municipality(db, municipality_id)
    if not item:
        raise HTTPException(status_code=404, detail="Municipality not found")
    return item

@router.post("/regulations", response_model=MunicipalRegulationRead)
def add_regulation(payload: MunicipalRegulationCreate, db: Session = Depends(get_db)):
    return create_regulation(db, payload)

@router.get("/{municipality_id}/regulations", response_model=list[MunicipalRegulationRead])
def get_regulations(municipality_id: int, db: Session = Depends(get_db)):
    return list_regulations(db, municipality_id)