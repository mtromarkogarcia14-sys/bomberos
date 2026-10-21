from sqlalchemy.orm import Session
from app.models import Evidence
from app.schemas import EvidenceCreate

def add_evidence(db: Session, payload: EvidenceCreate):
    evidence = Evidence(
        case_id=payload.case_id,
        evidence_type=payload.evidence_type,
        title=payload.title,
        file_path=payload.file_path,
        metadata_json=payload.metadata,
        source=payload.source,
    )
    db.add(evidence)
    db.commit()
    db.refresh(evidence)
    return evidence

def list_evidence(db: Session, case_id: int):
    return db.query(Evidence).filter(Evidence.case_id == case_id).all()