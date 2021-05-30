from reportlab.pdfgen import canvas

class pdfrep:
    def __init__(self):
        self.pdf = canvas.Canvas("Violation Report")
        self.pdf.setTitle("ViolationReport")

