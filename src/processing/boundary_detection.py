import re

LESSON_PATTERNS = [
    r"(?:^|\n)\s*(Lesson\s+\d+[:\-]?\s*[^\n]*)",
    r"(?:^|\n)\s*(Module\s+\d+[:\-]?\s*[^\n]*)",
]
PAGE_NUM_RE = re.compile(r"^\s*\d+\s*$")
SINGLE_LETTER_RE = re.compile(r"^\s*[a-zA-Z]\.\s*$")

def _cleanup_chunk(text: str) -> str:
    lines = [ln.strip() for ln in text.splitlines()]
    cleaned: list[str] = []
    for ln in lines:
        if not ln:
            continue
        # Drop page numbers and orphaned outline letters (e.g., "a.", "b.")
        if PAGE_NUM_RE.match(ln) or SINGLE_LETTER_RE.match(ln):
            continue
        cleaned.append(ln)
    return "\n".join(cleaned).strip()

def split_lessons(text: str) -> list[dict[str, str]]:
    pattern = re.compile("|".join(LESSON_PATTERNS), flags=re.IGNORECASE)
    matches = list(pattern.finditer(text))

    if not matches:
        # Fallback to single lesson
        return [{"title": "Lesson", "content": _cleanup_chunk(text)}]

    lessons: list[dict[str, str]] = []
    for i, m in enumerate(matches):
        # Title line
        title_line = m.group(0).strip().split("\n")[0]

        # Exclude the title from content
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text) 
        content = _cleanup_chunk(text[start:end])

        # Remove any repeated title echo at the start of content
        if content.lower().startswith(title_line.lower()):
            content = text[start:end].lstrip()

        lessons.append({"title": title_line, "content": content})
    return lessons