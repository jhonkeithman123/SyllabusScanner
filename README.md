# SyllabusScanner

## Overview

SyllabusScanner is an AI tool designed to scan syllabus files in various formats (PDF, DOCX, etc.) and produce concise, structured summaries of lessons. The tool aims to simplify the process of extracting key information from educational documents, making it easier for educators and students to access relevant content quickly.

## Features

- **File Parsing**: Supports PDF and DOCX formats for syllabus files.
- **Lesson Summarization**: Utilizes extractive summarization techniques to condense lesson content.
- **Image Handling**: Captures and organizes images associated with lessons.
- **Reference Management**: Allows for the addition and organization of references within the syllabus.

## Project Structure

```
syllabus-scanner-ai
├── src
│   ├── app.py                # Main entry point for the application
│   ├── models
│   │   ├── document.py       # Defines Document, Lesson, Image, and Summary classes
│   │   └── __init__.py       # Initializes the models package
│   ├── parsers
│   │   ├── pdf_parser.py      # Functions for extracting text from PDF files
│   │   ├── docx_parser.py     # Functions for parsing DOCX files
│   │   └── __init__.py       # Initializes the parsers package
│   ├── summarizers
│   │   ├── rule_based.py      # Implements extractive summarization techniques
│   │   └── __init__.py       # Initializes the summarizers package
│   ├── utils
│   │   ├── file_loader.py      # Utility functions for loading files
│   │   ├── text_cleaner.py     # Functions for cleaning and preprocessing text
│   │   └── __init__.py       # Initializes the utils package
│   └── types
│       └── index.py          # Defines custom types and interfaces
├── requirements.txt           # Lists project dependencies
├── pyproject.toml            # Project configuration and metadata
└── README.md                 # Documentation for the project
```

## Installation

To set up the project, clone the repository and install the required dependencies:

```bash
git clone <repository-url>
cd syllabus-scanner-ai
pip install -r requirements.txt
```

## Usage

To run the application, execute the following command:

```bash
python src/app.py <path_to_syllabus_file>
```

Replace `<path_to_syllabus_file>` with the path to the syllabus file you wish to scan.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
