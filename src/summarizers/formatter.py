from typing import Any, List
import textwrap

def wrap_lines(lines: List[str], width: int = 80) -> List[str]:
    wrapped: List[str] = []
    for ln in lines:
        if not ln:
            wrapped.append("")
            continue
        # Preserve bullet formatting: "- " prefix
        if ln.startswith("- "):
            body = ln[2:]
            for i, w in enumerate(textwrap.wrap(body, width=width - 2)):
                wrapped.append(("- " + w) if i == 0 else (" " + w))
        else:
            wrapped.extend(textwrap.wrap(ln, width=width) or [""])
    return wrapped

def format_summary(lessons: list[dict[str, Any]], references: str) -> str:
    lines: list[str]= []
    for _idx, lesson in enumerate(lessons, start=1):
        # Section header
        title = lesson["title"].strip()
        lines.append(f"{title}")
        lines.append("")
        # Bullet points
        for point in lesson["summary"]:
            point = point.strip()
            if not point:
                continue
            lines.append(f"- {point}")
        lines.append("")

    if references:
        lines.append("References (stored):")
        lines.append("")
        lines.append(references.strip())

    # Finak wrap for readability
    return "\n".join(wrap_lines(lines, width=88))