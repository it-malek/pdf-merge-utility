# PDF Merge Utility

A Python tool for automating PDF document organization and merging, built to streamline repetitive reporting workflows through intelligent filename-based matching.

**Author:** Malek Elaghel · [malekelaghel@gmail.com](mailto:malekelaghel@gmail.com) · MIT License

## Overview

The utility pairs related PDFs by matching document IDs embedded in filenames (e.g., `G12345 Report.pdf` with `G12345 Data.pdf`), merges them with an optional appendix, and writes the results in batch. A Tkinter GUI guides users through folder selection; the underlying `DocumentProcessor` class is also usable programmatically.

## GUI

<!-- Provide a screenshot of the Tkinter selection flow and replace this comment with: -->
<!-- ![GUI Screenshot](docs/images/gui_screenshot.png) -->
> Screenshot coming soon.

## Core Features

- **Intelligent file matching** — pairs documents using configurable ID patterns in filenames
- **Date filtering** — limits processing to files modified on or after a specified date
- **Appendix insertion** — optionally appends a standard last page to every merged output
- **Batch processing** — handles entire folder trees with optional recursion
- **Detailed logging** — reports processed, skipped, and errored file counts per run

## Getting Started

### Requirements

- Python 3.7+
- [pypdf](https://github.com/py-pdf/pypdf) >= 3.0.0

### Installation

```bash
git clone https://github.com/it-malek/pdf-merge-utility.git
cd pdf-merge-utility
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Usage

**Interactive (GUI):**

```bash
python main.py
```

**Programmatic:**

```python
from src.config import ProcessorConfig
from src.document_processor import DocumentProcessor

config = ProcessorConfig(
    source_folder="path/to/source",
    output_folder="path/to/output",
)
processor = DocumentProcessor(config)
stats = processor.process_documents()
print(stats)
```

## Project Structure

```
pdf-merge-utility/
├── main.py                   # Entry point (GUI workflow)
├── requirements.txt
├── setup.py
├── src/
│   ├── config.py             # ProcessorConfig dataclass
│   ├── document_processor.py # Core merge orchestration
│   ├── file_utils.py         # Filename parsing & file search
│   ├── gui_utils.py          # Tkinter folder/file dialogs
│   ├── pdf_operations.py     # PDF merge via pypdf
│   └── __init__.py
└── tests/
    ├── test_file_utils.py
    └── test_document_processor.py
```

## Running Tests

```bash
pip install pytest
pytest tests/ -v
```

## Design Notes

The current design is optimized for a specific workplace reporting workflow. Planned enhancements include customizable filename patterns, user-defined merge workflows, and expanded GUI accessibility to make the tool applicable to a broader range of use cases.

## Contributing

Open an issue or submit a pull request. Please include a test for any new behavior.
