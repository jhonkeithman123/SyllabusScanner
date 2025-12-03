from docx import Document as DocxDocument

def parse_docx(file_path):
    doc = DocxDocument(file_path)
    text = []

    for paragraph in doc.paragraphs:
        text.append(paragraph.text)

    return "\n".join(text)