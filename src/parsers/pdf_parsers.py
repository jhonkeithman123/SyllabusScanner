import pdfplumber
from pathlib import Path

def parse_pdf(path: Path) -> tuple[str, list[str]]:
    text_parts: list[str] = []
    images: list[str] = []  # placeholder; can extract later

    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            text_parts.append(page.extract_text() or "")
    return "\n".join(text_parts), images