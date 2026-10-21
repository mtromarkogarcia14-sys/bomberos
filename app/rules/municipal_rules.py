# Reglas municipales base para Jalisco
# Se pueden adaptar por municipio de forma individual o mediante seed.

MUNICIPAL_RULES = {
    "guadalajara": {
        "inspection": {
            "requirement_text": "Debe existir inspección documental y física del sitio.",
            "keywords": ["inspeccion", "mantenimiento", "registro", "revisión", "periodica"]
        },
        "evacuation": {
            "requirement_text": "Debe existir rutas de evacuación y señalización funcionales.",
            "keywords": ["evacuacion", "salida", "simulacro", "señalizacion", "ruta"]
        },
        "training": {
            "requirement_text": "Debe existir brigada y capacitación documentada.",
            "keywords": ["brigada", "capacitacion", "entrenamiento", "personal"]
        },
        "electrical": {
            "requirement_text": "Debe existir mantenimiento documental del sistema eléctrico.",
            "keywords": ["panel", "electricidad", "circuito", "mantenimiento electrico", "cortocircuito"]
        },
        "fire_systems": {
            "requirement_text": "Debe existir mantenimiento y prueba de equipos contra incendios.",
            "keywords": ["extintor", "rociador", "alarma", "manguera", "hidrante"]
        }
    },
    "zapopan": {
        "inspection": {
            "requirement_text": "Debe existir registro y revisión periódica del sitio.",
            "keywords": ["registro", "inspeccion", "revisión", "periodica"]
        },
        "evacuation": {
            "requirement_text": "Debe existir plan de evacuación y señalización visible.",
            "keywords": ["evacuacion", "salida", "plan de evacuacion", "señalizacion"]
        },
        "training": {
            "requirement_text": "Debe existir entrenamiento especializado por brigada.",
            "keywords": ["brigada", "capacitacion", "simulacro", "entrenamiento"]
        },
        "electrical": {
            "requirement_text": "Debe existir revisión eléctrica y mantenimiento documental.",
            "keywords": ["panel", "circuito", "electricidad", "mantenimiento"]
        },
        "fire_systems": {
            "requirement_text": "Debe existir operación y validación del sistema contra incendios.",
            "keywords": ["extintor", "alarma", "rociador", "mantenimiento"]
        }
    },
    "tonala": {
        "inspection": {
            "requirement_text": "Debe existir inspección periódica documentada.",
            "keywords": ["inspeccion", "mantenimiento", "periodica", "registro"]
        },
        "evacuation": {
            "requirement_text": "Debe existir señalización y evacuación con simulacro.",
            "keywords": ["evacuacion", "simulacro", "salida", "señalizacion"]
        },
        "training": {
            "requirement_text": "Debe existir brigada y capacitación para respuesta inmediata.",
            "keywords": ["brigada", "capacitacion", "respuesta", "entrenamiento"]
        },
        "electrical": {
            "requirement_text": "Debe existir revisión periódica de instalación eléctrica.",
            "keywords": ["electricidad", "panel", "circuito", "mantenimiento"]
        },
        "fire_systems": {
            "requirement_text": "Debe existir mantenimiento y prueba de equipos de protección.",
            "keywords": ["extintor", "rociador", "alarma", "mantenimiento"]
        }
    }
}