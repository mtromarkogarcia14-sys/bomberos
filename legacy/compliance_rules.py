from typing import List, Dict

def evaluate_requirement(requirement_text: str, evidence_text: str) -> str:
    t = (requirement_text + " " + evidence_text).lower()

    if "evacuacion" in t and ("sin" in t or "falta" in t or "no" in t):
        return "non_compliant"

    if "mantenimiento" in t and ("ausente" in t or "no" in t or "falta" in t):
        return "non_compliant"

    if "alarma" in t and ("sin" in t or "inoperante" in t or "falla" in t):
        return "non_compliant"

    if "panel" in t and ("dañado" in t or "fallo" in t):
        return "non_compliant"

    if "documentado" in t and ("no" in t or "falta" in t):
        return "requires_review"

    return "compliant"