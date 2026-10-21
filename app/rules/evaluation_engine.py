from app.rules.municipal_rules import MUNICIPAL_RULES

def evaluate_municipal_requirement(municipality_name: str, requirement_text: str, evidence_text: str, category: str = "inspection"):
    municipality_key = municipality_name.lower().replace(" ", "").replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u")
    ruleset = MUNICIPAL_RULES.get(municipality_key, MUNICIPAL_RULES["guadalajara"])

    if category not in ruleset:
        category = "inspection"

    rule = ruleset.get(category, {})
    keywords = rule.get("keywords", [])
    text = (requirement_text + " " + (evidence_text or "")).lower()

    if any(k in text for k in keywords):
        if any(token in text for token in ["no", "falta", "ausente", "inoperante", "sin", "nunca"]):
            return "non_compliant", rule.get("requirement_text", "No cumple con el requisito municipal")
        return "partial", rule.get("requirement_text", "Cumplimiento parcial o evidencia insuficiente")

    return "unknown", "Sin evidencia que permita determinar el cumplimiento; revisión manual requerida"