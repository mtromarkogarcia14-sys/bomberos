from pydantic import Field
from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class MunicipalityCreate(BaseModel):
    name: str
    state: str = "Jalisco"
    authority_protection_civil: Optional[str] = None
    authority_bomberos: Optional[str] = None
    regulation_reference: Optional[str] = None
    regulation_version: Optional[str] = None

class MunicipalityRead(BaseModel):
    id: int
    name: str
    state: str
    authority_protection_civil: Optional[str]
    authority_bomberos: Optional[str]
    regulation_reference: Optional[str]
    regulation_version: Optional[str]

    class Config:
        from_attributes = True

class MunicipalRegulationCreate(BaseModel):
    municipality_id: int
    name: str
    regulation_type: str
    version: Optional[str] = None
    document_url: Optional[str] = None
    description: Optional[str] = None

class MunicipalRegulationRead(BaseModel):
    id: int
    municipality_id: int
    name: str
    regulation_type: str
    version: Optional[str]
    document_url: Optional[str]
    description: Optional[str]

    class Config:
        from_attributes = True

class InternalProgramCreate(BaseModel):
    municipality_id: int
    name: str
    program_type: str
    objective: Optional[str] = None
    frequency: Optional[str] = None
    responsible: Optional[str] = None
    status: str = "draft"

class InternalProgramRead(BaseModel):
    id: int
    municipality_id: int
    name: str
    program_type: str
    objective: Optional[str]
    frequency: Optional[str]
    responsible: Optional[str]
    status: str

    class Config:
        from_attributes = True

class MunicipalRequirementCreate(BaseModel):
    municipality_id: int
    program_id: Optional[int] = None
    requirement_text: str
    requirement_type: str
    evidence_required: Optional[str] = None
    source_reference: Optional[str] = None
    category: Optional[str] = None

class MunicipalRequirementRead(BaseModel):
    id: int
    municipality_id: int
    program_id: Optional[int]
    requirement_text: str
    requirement_type: str
    evidence_required: Optional[str]
    source_reference: Optional[str]
    category: Optional[str]

    class Config:
        from_attributes = True

class CaseCreate(BaseModel):
    municipality_id: int
    name: str
    case_type: str
    location: Optional[str] = None
    incident_date: Optional[datetime] = None
    summary: Optional[str] = None

class CaseRead(BaseModel):
    id: int
    municipality_id: int
    name: str
    case_type: str
    location: Optional[str]
    incident_date: Optional[datetime]
    summary: Optional[str]
    risk_level: str
    confidence: float

    class Config:
        from_attributes = True

class EvidenceCreate(BaseModel):
    case_id: int
    evidence_type: str
    title: str
    file_path: Optional[str] = None
    metadata: Optional[str] = None
    extracted_text: Optional[str] = None
    source: Optional[str] = None

class EvidenceRead(BaseModel):
    model_config = {"from_attributes": True}
    id: int
    case_id: int
    evidence_type: str
    title: str
    file_path: Optional[str]
    metadata: Optional[str] = Field(default=None, validation_alias="metadata_json")
    extracted_text: Optional[str]
    source: Optional[str]

class ComplianceMunicipalCreate(BaseModel):
    case_id: int
    municipality_id: int
    requirement_id: int
    status: str
    notes: Optional[str] = None
    severity: str = "medium"

class ComplianceMunicipalRead(BaseModel):
    id: int
    case_id: int
    municipality_id: int
    requirement_id: int
    status: str
    notes: Optional[str]
    severity: str

    class Config:
        from_attributes = True

class NonConformityMunicipalCreate(BaseModel):
    case_id: int
    municipality_id: int
    requirement_id: int
    description: str
    severity: str = "medium"
    recommendation: Optional[str] = None

class NonConformityMunicipalRead(BaseModel):
    id: int
    case_id: int
    municipality_id: int
    requirement_id: int
    description: str
    severity: str
    recommendation: Optional[str]

    class Config:
        from_attributes = True