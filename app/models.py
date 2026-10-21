from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.database import Base

class Municipality(Base):
    __tablename__ = "municipalities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    state = Column(String(100), default="Jalisco")
    authority_protection_civil = Column(String(255), nullable=True)
    authority_bomberos = Column(String(255), nullable=True)
    regulation_reference = Column(String(255), nullable=True)
    regulation_version = Column(String(50), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class MunicipalRegulation(Base):
    __tablename__ = "municipal_regulations"

    id = Column(Integer, primary_key=True, index=True)
    municipality_id = Column(Integer, ForeignKey("municipalities.id"), nullable=False)
    name = Column(String(255), nullable=False)
    regulation_type = Column(String(100), nullable=False)
    version = Column(String(50), nullable=True)
    document_url = Column(String(500), nullable=True)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class InternalProgram(Base):
    __tablename__ = "internal_programs"

    id = Column(Integer, primary_key=True, index=True)
    municipality_id = Column(Integer, ForeignKey("municipalities.id"), nullable=False)
    name = Column(String(255), nullable=False)
    program_type = Column(String(100), nullable=False)
    objective = Column(Text, nullable=True)
    frequency = Column(String(100), nullable=True)
    responsible = Column(String(255), nullable=True)
    status = Column(String(50), default="draft")
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class MunicipalRequirement(Base):
    __tablename__ = "municipal_requirements"

    id = Column(Integer, primary_key=True, index=True)
    municipality_id = Column(Integer, ForeignKey("municipalities.id"), nullable=False)
    program_id = Column(Integer, ForeignKey("internal_programs.id"), nullable=True)
    requirement_text = Column(Text, nullable=False)
    requirement_type = Column(String(100), nullable=False)
    evidence_required = Column(Text, nullable=True)
    source_reference = Column(String(255), nullable=True)
    category = Column(String(100), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class InvestigationCase(Base):
    __tablename__ = "cases"

    id = Column(Integer, primary_key=True, index=True)
    municipality_id = Column(Integer, ForeignKey("municipalities.id"), nullable=False)
    name = Column(String(255), nullable=False)
    case_type = Column(String(100), nullable=False)
    status = Column(String(50), default="draft")
    location = Column(String(255), nullable=True)
    incident_date = Column(DateTime(timezone=True), nullable=True)
    summary = Column(Text, nullable=True)
    risk_level = Column(String(50), default="unknown")
    confidence = Column(Float, default=0.0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

class Evidence(Base):
    __tablename__ = "evidence"

    id = Column(Integer, primary_key=True, index=True)
    case_id = Column(Integer, ForeignKey("cases.id"), nullable=False)
    evidence_type = Column(String(100), nullable=False)
    title = Column(String(255), nullable=False)
    file_path = Column(String(500), nullable=True)
    metadata_json = Column("metadata", Text, nullable=True)
    extracted_text = Column(Text, nullable=True)
    source = Column(String(255), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class ComplianceMunicipal(Base):
    __tablename__ = "compliance_municipal"

    id = Column(Integer, primary_key=True, index=True)
    case_id = Column(Integer, ForeignKey("cases.id"), nullable=False)
    municipality_id = Column(Integer, ForeignKey("municipalities.id"), nullable=False)
    requirement_id = Column(Integer, ForeignKey("municipal_requirements.id"), nullable=False)
    status = Column(String(50), nullable=False)
    notes = Column(Text, nullable=True)
    severity = Column(String(50), default="medium")
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class NonConformityMunicipal(Base):
    __tablename__ = "non_conformities_municipal"

    id = Column(Integer, primary_key=True, index=True)
    case_id = Column(Integer, ForeignKey("cases.id"), nullable=False)
    municipality_id = Column(Integer, ForeignKey("municipalities.id"), nullable=False)
    requirement_id = Column(Integer, ForeignKey("municipal_requirements.id"), nullable=False)
    description = Column(Text, nullable=False)
    severity = Column(String(50), default="medium")
    recommendation = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())