from sqlalchemy.orm import Session
from app.models import RiskAssessment
from app.schemas import RiskCreate

def add_risk_assessment(db: Session, payload: RiskCreate):
    item = RiskAssessment(
        case_id=payload.case_id,
        threat=payload.threat,
        vulnerability=payload.vulnerability,
        exposure=payload.exposure,
        consequence=payload.consequence,
        risk_level=payload.risk_level,
        probability=payload.probability,
        impact=payload.impact,
        score=payload.score,
        recommendation=payload.recommendation,
    )
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

def get_risk_assessment(db: Session, case_id: int):
    return db.query(RiskAssessment).filter(RiskAssessment.case_id == case_id).first()