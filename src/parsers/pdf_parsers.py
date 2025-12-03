from pdfplumber import open as pdf_open

def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF file."""

    text = ""

    with pdf_open(pdf_open) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
            
    return text.strip()