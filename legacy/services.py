from sqlalchemy.orm import Session

from app.models import (
    InvestigationCase,
    Evidence,
    EventRecord,
    Hypothesis,
    RiskAssessment,
    Report,
    AuditLog,
)
from app.schemas import (
    CaseCreate,
    EvidenceCreate,
    EventCreate,
    HypothesisCreate,
    RiskCreate,
    ReportCreate,
)

# ---- CASES ----
def create_case(db: Session, payload: CaseCreate):
    case = InvestigationCase(
        name=payload.name,
        case_type=payload.case_type,
        location=payload.location,
        incident_date=payload.incident_date,
        summary=payload.summary,
    )
    db.add(case)
    db.commit()
    db.refresh(case)
    return case

def get_case(db: Session, case_id: int):
    return db.query(InvestigationCase).filter(InvestigationCase.id == case_id).first()

def list_cases(db: Session):
    return db.query(InvestigationCase).all()

# ---- EVIDENCE ----
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

# ---- EVENTS ----
def add_event(db: Session, payload: EventCreate):
    event = EventRecord(
        case_id=payload.case_id,
        timestamp=payload.timestamp,
        event_type=payload.event_type,
        description=payload.description,
        source=payload.source,
        confidence=payload.confidence,
    )
    db.add(event)
    db.commit()
    db.refresh(event)
    return event

def list_events(db: Session, case_id: int):
    return db.query(EventRecord).filter(EventRecord.case_id == case_id).all()

# ---- HYPOTHESES ----
def add_hypothesis(db: Session, payload: HypothesisCreate):
    hypothesis = Hypothesis(
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
    db.add(hypothesis)
    db.commit()
    db.refresh(hypothesis)
    return hypothesis

def list_hypotheses(db: Session, case_id: int):
    return db.query(Hypothesis).filter(Hypothesis.case_id == case_id).all()

# ---- RISK ----
def add_risk_assessment(db: Session, payload: RiskCreate):
    risk = RiskAssessment(
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
    db.add(risk)
    db.commit()
    db.refresh(risk)
    return risk

def get_risk_assessment(db: Session, case_id: int):
    return db.query(RiskAssessment).filter(RiskAssessment.case_id == case_id).first()

# ---- REPORTS ----
def add_report(db: Session, payload: ReportCreate):
    report = Report(
        case_id=payload.case_id,
        report_type=payload.report_type,
        title=payload.title,
        content=payload.content,
    )
    db.add(report)
    db.commit()
    db.refresh(report)
    return report

def list_reports(db: Session, case_id: int):
    return db.query(Report).filter(Report.case_id == case_id).all()

# ---- AUDIT ----
def add_audit(db: Session, case_id: int, action: str, actor: str, details: str):
    item = AuditLog(
        case_id=case_id,
        action=action,
        actor=actor,
        details=details,
    )
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

def list_audit(db: Session, case_id: int):
    return db.query(AuditLog).filter(AuditLog.case_id == case_id).all()