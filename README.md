# Agente de cumplimiento municipal para Protección Civil y Bomberos en Jalisco

Este proyecto es una base técnica para un agente de análisis y cumplimiento normativo enfocado en:
- investigación de incendios
- gestión de riesgos
- protección civil
- programas internos de bomberos
- requisitos municipales de Jalisco
- evaluación de cumplimiento por municipio

No sustituye la autoridad, el reglamento municipal ni la evaluación profesional de bomberos o Protección Civil. Está pensado como una herramienta de apoyo técnico, trazabilidad y análisis.

## Objetivo

Permitir que un sistema:
- registre casos por municipio
- relacione cada caso con su autoridad local
- evalúe cumplimiento municipal según programa interno
- compare la evidencia con requisitos formales de prevención y evacuación
- detecte no conformidades
- genere informes técnicos y de cumplimiento

## Arquitectura general

El sistema está diseñado en capas:

1. Capa de entrada
   - casos
   - evidencia
   - documentación
   - archivos y registros
   - reportes de bomberos y Protección Civil

2. Capa de análisis
   - evaluación de riesgo
   - análisis técnico del caso
   - correlación entre evidencia y requisito municipal

3. Capa normativa
   - reglamentos internos por municipio
   - programas internos
   - requisitos municipales
   - clasificación por tipo de riesgo

4. Capa de cumplimiento
   - cumplimiento
   - no conformidad
   - recomendaciones correctivas

5. Capa de salida
   - reportes
   - trazabilidad
   - evidencias y resultados

## Casos de uso principales

- evaluar un incendio en un edificio de una localidad en Jalisco
- verificar si la instalación cumple con requisitos de protección civil y bomberos del municipio
- revisar si existen registros de inspección, evacuación, capacitación y mantenimiento
- detectar incumplimientos específicos por municipio
- producir un informe técnico y uno de cumplimiento

## Entidades principales

### Municipio
Representa cada municipio de Jalisco.

Campos principales:
- id
- name
- state
- authority_protection_civil
- authority_bomberos
- regulation_reference
- regulation_version

### MunicipalRegulation
Representa el reglamento interno o documento base del municipio.

Campos principales:
- id
- municipality_id
- name
- regulation_type
- version
- document_url
- description

### InternalProgram
Representa un programa interno requerido por el municipio.

Ejemplos:
- Programa de brigada contra incendios
- Programa de evacuación
- Programa de inspección
- Programa de capacitación
- Programa de mantenimiento

Campos principales:
- id
- municipality_id
- name
- program_type
- objective
- frequency
- responsible
- status

### MunicipalRequirement
Representa un requisito municipal obligatorio o recomendado.

Ejemplos:
- inspección periódica
- mantenimiento de instalaciones eléctricas
- rutas de evacuación
- señalización
- simulacros
- brigada contra incendios

Campos principales:
- id
- municipality_id
- program_id
- requirement_text
- requirement_type
- evidence_required
- source_reference
- category

### InvestigationCase
Representa un caso real o simulado.

Campos principales:
- id
- municipality_id
- name
- case_type
- location
- incident_date
- summary
- risk_level
- confidence

### Evidence
Representa evidencia documental o física asociada al caso.

Campos principales:
- id
- case_id
- evidence_type
- title
- file_path
- metadata
- extracted_text
- source

### ComplianceMunicipal
Representa el resultado de evaluar un requisito del municipio para un caso.

Campos principales:
- id
- case_id
- municipality_id
- requirement_id
- status
- notes
- severity

Estados posibles:
- compliant
- partial
- non_compliant
- unknown

### NonConformityMunicipal
Representa una no conformidad detectada.

Campos principales:
- id
- case_id
- municipality_id
- requirement_id
- description
- severity
- recommendation

## Reglas de evaluación municipal

La evaluación no se hace bajo una sola regla. Se aplica una lógica de prioridad:

1. Evidencia del caso
2. Requisito municipal
3. Programa interno del municipio
4. Reglamento interno del municipio
5. Reglas generales de protección civil y bomberos
6. Recomendaciones de mejora

Cada requisito puede evaluarse con palabras clave. Por ejemplo:

- inspección
- mantenimiento
- evaluación
- registro
- simulacro
- evacuación
- señalización
- brigada
- electricidad
- panel
- extintor
- alarma
- rociador

El motor de evaluación considera lo siguiente:
- si hay evidencia directa de cumplimiento
- si hay evidencia insuficiente
- si hay ausencia de documentación
- si la evidencia sugiere incumplimiento

## Endpoints

### Municipios

POST /municipalities/
Crea un municipio.

Request body:
```json
{
  "name": "Guadalajara",
  "state": "Jalisco",
  "authority_protection_civil": "Protección Civil de Guadalajara",
  "authority_bomberos": "Bomberos Guadalajara",
  "regulation_reference": "Reglamento Interno de Protección Civil",
  "regulation_version": "2024"
}