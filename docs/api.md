# Documentación de API

## 1. Municipios

### Crear municipio
POST /municipalities/

Request body:
```json
{
  "name": "Zapopan",
  "state": "Jalisco",
  "authority_protection_civil": "Protección Civil de Zapopan",
  "authority_bomberos": "Bomberos Zapopan",
  "regulation_reference": "Reglamento Interno de Protección Civil",
  "regulation_version": "2024"
}
```

### Listar municipios
GET /municipalities/

### Obtener municipio por id
GET /municipalities/{municipality_id}

---

## 2. Reglamentos municipales

### Crear reglamento
POST /municipalities/regulations

Request body:
```json
{
  "municipality_id": 1,
  "name": "Reglamento Interno de Protección Civil",
  "regulation_type": "protection_civil",
  "version": "2024",
  "document_url": "https://example.com/reglamento",
  "description": "Reglamento local aplicable al caso"
}
```

### Listar reglamentos
GET /municipalities/{municipality_id}/regulations

---

## 3. Programas internos

### Crear programa
POST /municipalities/{municipality_id}/programs

Request body:
```json
{
  "municipality_id": 1,
  "name": "Programa Interno de Brigada contra Incendios",
  "program_type": "brigade",
  "objective": "Preparar a la organización para intervenir ante incendios",
  "frequency": "Semestral",
  "responsible": "Responsable de seguridad",
  "status": "active"
}
```

### Listar programas
GET /municipalities/{municipality_id}/programs

---

## 4. Requisitos municipales

### Crear requisito
POST /municipalities/{municipality_id}/requirements

Request body:
```json
{
  "municipality_id": 1,
  "program_id": 1,
  "requirement_text": "Debe existir inspección documental y física del sitio.",
  "requirement_type": "mandatory",
  "evidence_required": "Actas de inspección, fotos, reporte de revisión",
  "source_reference": "Reglamento Interno de Protección Civil",
  "category": "inspection"
}
```

### Listar requisitos
GET /municipalities/{municipality_id}/requirements

---

## 5. Casos

### Crear caso
POST /cases/

Request body:
```json
{
  "municipality_id": 1,
  "name": "Incendio en local comercial",
  "case_type": "fire",
  "location": "Centro de Guadalajara",
  "incident_date": "2026-10-21T10:00:00",
  "summary": "Se reporta humo y daño localizado en panel eléctrico."
}
```

### Listar casos
GET /cases/

### Obtener caso
GET /cases/{case_id}

---

## 6. Evidencia

### Agregar evidencia
POST /cases/{case_id}/evidence

Request body:
```json
{
  "case_id": 1,
  "evidence_type": "document",
  "title": "Reporte interno de bomberos",
  "extracted_text": "Se observa daño localizado en panel eléctrico. No hay registro de mantenimiento ni simulacro.",
  "source": "bomberos"
}
```

### Listar evidencia
GET /cases/{case_id}/evidence

---

## 7. Evaluación municipal

### Ejecutar evaluación
POST /cases/{case_id}/municipal-evaluation?municipality_id=1

### Obtener evaluación
GET /cases/{case_id}/municipal-evaluation

---

## 8. No conformidades

### Crear no conformidad
POST /cases/{case_id}/non-conformities

Request body:
```json
{
  "case_id": 1,
  "municipality_id": 1,
  "requirement_id": 2,
  "description": "No se cuenta con señalización ni rutas de evacuación documentadas.",