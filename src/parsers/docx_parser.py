from docx import Document as DocxDocument
from pathlib import Path

def parse_docx(file_path: Path) -> tuple[str, list[str]]:
    doc = DocxDocument(str(file_path))
    text_parts: list[str] = []

    for paragraph in doc.paragraphs:
        if paragraph.text:
            text_parts.append(paragraph.text)
    
    images: list[str] = []

    return "\n".join(text_parts), images