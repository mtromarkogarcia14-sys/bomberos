class FireAnalysisEngine:
    def analyze(self, text: str):
        t = (text or "").lower()

        hypotheses = []

        if "panel" in t or "electricidad" in t or "cortocircuito" in t:
            hypotheses.append({
                "name": "Origen eléctrico",
                "score": 0.76,
                "confidence": 0.72,
                "reason": "Se observan elementos asociados a instalación eléctrica o daño localizado en un panel."
            })

        if ("gas" in t and ("fuga" in t or "olor" in t)) or "gas" in t:
            hypotheses.append({
                "name": "Origen por gas",
                "score": 0.48,
                "confidence": 0.4,
                "reason": "Se reportan indicios de fuga o presencia de gas y materiales combustibles."
            })

        if "cocina" in t or "grasa" in t:
            hypotheses.append({
                "name": "Origen por cocina",
                "score": 0.42,
                "confidence": 0.35,
                "reason": "Se reportan condiciones asociadas a cocina, grasa o acumulación combustible."
            })

        if not hypotheses:
            hypotheses.append({
                "name": "Origen no determinado",
                "score": 0.2,
                "confidence": 0.15,
                "reason": "La evidencia disponible no permite identificar un origen claro."
            })

        return hypotheses

class RiskAnalysisEngine:
    def analyze(self, threat: str, vulnerability: str, exposure: str, consequence: str):
        score = 0.35

        mapping = {
            "baja": 0.1,
            "media": 0.2,
            "alta": 0.35,
        }

        score += mapping.get(vulnerability.lower(), 0.2)
        score += mapping.get(exposure.lower(), 0.2)
        score += mapping.get(consequence.lower(), 0.2)

        if score >= 0.9:
            level = "high"
        elif score >= 0.6:
            level = "medium"
        else:
            level = "low"

        return {
            "threat": threat,
            "vulnerability": vulnerability,
            "exposure": exposure,
            "consequence": consequence,
            "risk_level": level,
            "score": round(score, 2)
        }