import os
from typing import Optional

import pytesseract
from PIL import Image

class OCRService:
    def extract_text_from_image(self, image_path: str) -> str:
        try:
            img = Image.open(image_path)
            text = pytesseract.image_to_string(img, lang="spa+eng")
            return text.strip()
        except Exception as e:
            return f"Error processing image: {str(e)}"

    def extract_text_from_pdf(self, pdf_path: str) -> str:
        try:
            import pypdf
            reader = pypdf.PdfReader(pdf_path)
            text_chunks = []
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    text_chunks.append(text)
            return "\n".join(text_chunks).strip()
        except Exception as e:
            return f"Error processing PDF: {str(e)}"