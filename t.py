from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_dummy_resume(pdf_path):
    c = canvas.Canvas(pdf_path, pagesize=letter)
    
    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, 750, "Candidate Resume")
    
    # Name Section
    c.setFont("Helvetica-Bold", 12)
    c.drawString(100, 730, "**Name: Sunil Kumar**")
    
    # Email Section
    c.setFont("Helvetica", 12)
    c.drawString(100, 710, "Email: sunilm2011@gmail.com")
    
    # Phone Section
    c.drawString(100, 690, "Phone: +1234567890")
    
    # Education Section
    c.setFont("Helvetica-Bold", 12)
    c.drawString(100, 670, "## Education")
    c.setFont("Helvetica", 12)
    c.drawString(100, 650, "BSc Computer Science, XYZ University")
    c.drawString(100, 630, "Graduated: 2020")
    
    # Work Experience Section
    c.setFont("Helvetica-Bold", 12)
    c.drawString(100, 610, "## Work Experience")
    c.setFont("Helvetica", 12)
    c.drawString(100, 590, "Software Developer at ABC Corp")
    c.drawString(100, 570, "Worked on various web applications")
    
    # Skills Section
    c.setFont("Helvetica-Bold", 12)
    c.drawString(100, 550, "## Skills")
    c.setFont("Helvetica", 12)
    c.drawString(100, 530, "Python, JavaScript, SQL, React")
    
    # Certifications Section
    c.setFont("Helvetica-Bold", 12)
    c.drawString(100, 510, "## Certifications")
    c.setFont("Helvetica", 12)
    c.drawString(100, 490, "AWS Certified Solutions Architect")
    c.drawString(100, 470, "Certified Kubernetes Administrator")
    
    # Tech Stack Section
    c.setFont("Helvetica-Bold", 12)
    c.drawString(100, 450, "## Tech Stack")
    c.setFont("Helvetica", 12)
    c.drawString(100, 430, "Python, JavaScript, Node.js, AWS")
    
    # Save PDF
    c.save()

# Generate the dummy resume PDF
pdf_path = "dummy_resume.pdf"
generate_dummy_resume(pdf_path)
print(f"Dummy resume PDF saved at: {pdf_path}")

