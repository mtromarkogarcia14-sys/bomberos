class FireRules:
    @staticmethod
    def evaluate_origin(text: str):
        t = (text or "").lower()
        signals = []

        if "panel" in t or "electricidad" in t or "cortocircuito" in t:
            signals.append("electric")
        if "gas" in t and ("olor" in t or "fuga" in t):
            signals.append("gas")
        if "cocina" in t or "grasa" in t:
            signals.append("kitchen")
        if "quimico" in t or "sustancia" in t:
            signals.append("chemical")
        if "humano" in t or "negligencia" in t:
            signals.append("human")

        return signals