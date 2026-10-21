from sqlalchemy.orm import Session
from app.models import MunicipalRequirement, ComplianceMunicipal, NonConformityMunicipal, Evidence, Municipality
from app.rules.evaluation_engine import evaluate_municipal_requirement

def evaluate_case_against_requirements(db: Session, case_id: int, municipality_id: int):
    municipality = db.query(Municipality).filter(Municipality.id == municipality_id).first()
    municipality_name = municipality.name if municipality else "guadalajara"

    evidence_items = db.query(Evidence).filter(Evidence.case_id == case_id).all()
    evidence_text = "\n".join(item.extracted_text or "" for item in evidence_items if item.extracted_text)

    requirements = db.query(MunicipalRequirement).filter(MunicipalRequirement.municipality_id == municipality_id).all()
    results = []

    for req in requirements:
        status, notes = evaluate_municipal_requirement(
            municipality_name,
            req.requirement_text,
            evidence_text,
            category=req.category or "inspection"
        )
        item = ComplianceMunicipal(
            case_id=case_id,
            municipality_id=municipality_id,
            requirement_id=req.id,
            status=status,
            notes=notes,
            severity="medium"
        )
        db.add(item)
        results.append({
            "requirement_id": req.id,
            "status": status,
            "requirement_text": req.requirement_text,
            "notes": notes,
            "category": req.category
        })

    db.commit()
    return results

def add_non_conformity(db: Session, case_id: int, municipality_id: int, requirement_id: int, description: str, severity: str = "medium", recommendation: str = None):
    item = NonConformityMunicipal(
        case_id=case_id,
        municipality_id=municipality_id,
        requirement_id=requirement_id,
        description=description,
        severity=severity,
        recommendation=recommendation
    )
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

def get_compliance_for_case(db: Session, case_id: int):
    return db.query(ComplianceMunicipal).filter(ComplianceMunicipal.case_id == case_id).all()

def get_non_conformities_for_case(db: Session, case_id: int):
    return db.query(NonConformityMunicipal).filter(NonConformityMunicipal.case_id == case_id).all()