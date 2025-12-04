# Class for the documents to be scanned
from pathlib import Path
from typing import Any

class Document:
    def __init__(self, filename: Path, raw_text: str="") -> None:
        self.filename = filename
        self.raw_text = raw_text
        self.lessons: list[str] = []        # List of Lesson onjects
        self.references: list[str] = []     # List of references strings

    def add_lesson(self, lesson: str) -> None:
        self.lessons.append(lesson)

    def add_references(self, reference: str) -> None:
        self.references.append(reference)

# Class for the lessons read from the file
class Lesson:
    def __init__(self, title: str, content: str, images: list["Image"] | None=None, summary: str | None=None) -> None:
        self.title = title
        self.content = content
        self.images: list["Image"] = images or []        # List of Image objects
        self.summary: str | None = summary      # Summarized text

    def add_image(self, image: "Image") -> None:
        self.images.append(image)

    def set_summary(self, summary: str) -> None:
        self.summary = summary

# Class for the images that was read from the file
class Image:
    def __init__(self, filepath: str, caption: str | None=None) -> None:
        self.filepath = filepath
        self.caption = caption

    def set_caption(self, caption: str) -> None:
        self.caption = caption

# Class for the summary of the lessons

class Summary:
    def __init__(self) -> None:
        self.lessons: list[dict[str, Any]] = []        # List of summarized lessons
        self.references: list[str] = []     # References stored separately

    def add_lesson_summary(self, lesson_title: str, summary: str, images: list["Image"] | None=None) -> None:
        self.lessons.append({
            "title": lesson_title,
            "summary": summary,
            "images": images or []
        })

    def add_reference(self, reference: str) -> None:
        self.references.append(reference)