from app.rules.nfpa_rules import NFPA_RULES
from app.rules.nom_rules import NOM_RULES

def evaluate_rule(rule_name: str, evidence_text: str):
    text = (evidence_text or "").lower()
    mapping = NFPA_RULES.get(rule_name, {})
    mapping_nom = NOM_RULES.get(rule_name, {})

    # regla NFPA
    rule_keywords = mapping.get("keywords", [])
    if any(k in text for k in rule_keywords):
        return "non_compliant", mapping.get("requirement", "Requisito no identificado")

    # regla NOM
    nom_keywords = mapping_nom.get("keywords", [])
    if any(k in text for k in nom_keywords):
        return "requires_review", mapping_nom.get("requirement", "Requisito no identificado")

    return "compliant", "Se observa conformidad con la regla de referencia."