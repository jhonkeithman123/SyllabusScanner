# Class for the documents to be scanned
class Document:
    def __init__(self, filename, raw_text=""):
        self.filename = filename
        self.raw_text = raw_text
        self.lessons = []        # List of Lesson onjects
        self.references = []     # List of references strings

    def add_lesson(self, lesson):
        self.lessons.append(lesson)

    def add_references(self, reference):
        self.references.append(reference)

# Class for the lessons read from the file
class Lesson:
    def __init__(self, title, content=""):
        self.title = title
        self.content = content
        self.images = []         # List of Image objects
        self.summary = None      # Summarized text

    def add_image(self, image):
        self.images.append(image)

    def set_summary(self, summary):
        self.summary = summary

# Class for the images that was read from the file
class Image:
    def __init__(self, filepath, caption=None):
        self.filepath = filepath
        self.caption = caption

    def set_caption(self, caption):
        self.caption = caption

# Class for the summary of the lessons
class Summary:
    def __init__(self):
        self.lessons = []        # List of summarized lessons
        self.references = []     # References stored separately

    def add_lesson_summary(self, lesson_title, summary, images=None):
        self.lessons.append({
            "title": lesson_title,
            "summary": summary,
            "images": images or []
        })

    def add_reference(self, reference):
        self.references.append(reference)