# Custom types and interfaces used throughout the project

from typing import List, Optional, Dict, Any

# Type for a lesson
LessonType = Dict[str, Any]

# Type for a document
DocumentType = Dict[str, Any]

# Type for an image
ImageType = Dict[str, Optional[str]]

# Type for a summary
SummaryType = Dict[str, Any]

# Type for references
ReferenceType = List[str]