from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

class MunicipalReportService:
    def build_pdf(self, output_path: str, title: str, body: str):
        doc = SimpleDocTemplate(output_path, pagesize=A4)
        styles = getSampleStyleSheet()
        story = []
        story.append(Paragraph(title, styles["Title"]))
        story.append(Spacer(1, 20))
        story.append(Paragraph(body, styles["BodyText"]))
        doc.build(story)
        return output_path