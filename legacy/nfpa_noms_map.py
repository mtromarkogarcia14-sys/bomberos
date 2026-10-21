# Esta lista sirve como proxy de conectividad normativa.
# En producción debería cargarse desde BD o YAML/JSON.
# Aquí solo ilustramos la forma en que se acoplan normas, riesgos y requisitos.

NFPA_BY_RISK = {
    "electrical": [
        {"standard": "NFPA 70", "section": "Instalaciones eléctricas"},
        {"standard": "NFPA 72", "section": "Alarmas y detección"}
    ],
    "evacuation": [
        {"standard": "NFPA 101", "section": "Vida segura"},
        {"standard": "NFPA 72", "section": "Alarmas y sistemas de emergencia"}
    ],
    "fire_systems": [
        {"standard": "NFPA 13", "section": "Rociadores automáticos"},
        {"standard": "NFPA 25", "section": "Inspección, prueba y mantenimiento"},
        {"standard": "NFPA 14", "section": "Standpipes y hidrantes"}
    ],
    "investigation": [
        {"standard": "NFPA 921", "section": "Guía para investigación de incendios"},
        {"standard": "NFPA 1033", "section": "Calificación de investigadores"}
    ]
}

MEXICAN_NOMS_BY_RISK = {
    "electrical": [
        {"standard": "NOM-001-SEDE-2012", "section": "Instalaciones eléctricas y seguridad"},
        {"standard": "NOM-029-STPS-2011", "section": "Seguridad en centros de trabajo"}
    ],
    "evacuation": [
        {"standard": "NOM-004-STPS-1999", "section": "Señalización de seguridad"},
        {"standard": "NOM-018-STPS-2015", "section": "Prevención de incendios y evacuación"}
    ],
    "fire_systems": [
        {"standard": "NOM-002-STPS-2010", "section": "Mantenimiento de extintores y equipos"},
        {"standard": "NOM-005-STPS-1998", "section": "Seguridad en áreas de trabajo"}
    ]
}