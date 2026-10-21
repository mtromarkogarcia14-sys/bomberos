import os
from openai import OpenAI

class LLMService:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def summarize_case(self, text: str) -> str:
        if not os.getenv("OPENAI_API_KEY"):
            return "LLM no configurado. Se omite el resumen automático."

        prompt = f"""
Eres un experto en investigación de incendios, gestión de riesgos, protección civil y bomberos.
Analiza este texto y responde en español con:
- resumen ejecutivo
- posibles hipótesis de origen
- principales riesgos
- recomendaciones preventivas
- incertidumbres

Texto:
{text}
"""

        response = self.client.chat.completions.create(
            model=os.getenv("MODEL_NAME", "gpt-4o-mini"),
            messages=[
                {"role": "system", "content": "Eres un experto técnico en investigación de incendios y riesgos."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.2,
        )

        return response.choices[0].message.content