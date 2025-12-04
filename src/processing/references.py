import re

REF_PATTERNS = [r"\bReferences\b", r"\bBibliography\b", r"\bSources\b"]

def extract_references(text: str):
    for pat in REF_PATTERNS:
        m = re.search(pat, text, flags=re.IGNORECASE)

        if m:
            return text[m.start():].strip()
    return ""