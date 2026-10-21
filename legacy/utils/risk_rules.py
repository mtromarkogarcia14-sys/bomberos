class RiskRules:
    @staticmethod
    def score_risk(vulnerability: str, exposure: str, consequence: str):
        levels = {"baja": 0.2, "media": 0.5, "alta": 0.8}
        score = 0.3
        score += levels.get(vulnerability.lower(), 0.3)
        score += levels.get(exposure.lower(), 0.3)
        score += levels.get(consequence.lower(), 0.3)

        score = min(score, 1.0)

        if score >= 0.8:
            risk_level = "high"
        elif score >= 0.5:
            risk_level = "medium"
        else:
            risk_level = "low"

        return round(score, 2), risk_level