import sys
from pathlib import Path
from parsers.pdf_parsers import parse_pdf
from parsers.docx_parser import parse_docx
from processing.boundary_detection import split_lessons
from processing.references import extract_references
from summarizers.text_rank import summarize_text
from summarizers.formatter import format_summary
from typing import Any, Optional

def process_file(input_path: str) -> str:
    p: Path = Path(input_path)

    if not p.exists(): # Raise a File not found error if the file is not found
        raise FileNotFoundError(f"File not found: {input_path}")

    ext = p.suffix.lower()
    if ext == ".pdf":
        raw_text, _images = parse_pdf(p)
    elif ext == ".docx":
        raw_text, _images = parse_docx(p)
    else:
        raise ValueError(f"Unsupported file type: {ext}")

    cleaned_text = raw_text.strip()
    lessons = split_lessons(cleaned_text)

    references = extract_references(cleaned_text)
    summaries: list[dict[str, Any]] = []
    for lesson in lessons:
        summary = summarize_text(lesson["content"], max_points=3)
        summaries.append({
            "title": lesson["title"],
            "summary": summary,
            "images": [] # placeholder
        })

    return format_summary(summaries, references)

def main(argv: Optional[list[str]] = None) -> int:
    args: list[str] = argv or sys.argv[1:]
    if not args:
        print("Usage: python -m src.cli <file.pdf|file.docx>")
        return 1
    output = process_file(args[0])
    print(output)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())