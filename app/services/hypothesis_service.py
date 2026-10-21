from sqlalchemy.orm import Session
from app.models import Hypothesis
from app.schemas import HypothesisCreate

def add_hypothesis(db: Session, payload: HypothesisCreate):
    item = Hypothesis(
        case_id=payload.case_id,
        name=payload.name,
        description=payload.description,
        category=payload.category,
        score=payload.score,
        confidence=payload.confidence,
        evidence_support=payload.evidence_support,
        evidence_against=payload.evidence_against,
        status=payload.status,
    )
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

def list_hypotheses(db: Session, case_id: int):
    return db.query(Hypothesis).filter(Hypothesis.case_id == case_id).all()