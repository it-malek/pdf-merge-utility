# PDF Merge Utility

A Python utility for merging and organizing PDF documents, designed to automate repetitive document workflows in a professional setting. This tool was originally built to streamline a specific reporting process at work, but demonstrates skills and techniques applicable to a wide range of document automation tasks.

## Key Features

- **Intelligent File Matching:** Automatically matches and merges related PDF files using document IDs embedded in filenames (e.g., "G12345 Report.pdf" with "G12345 Data.pdf").
- **Batch Processing:** Processes large sets of documents efficiently, saving significant manual effort.
- **Date Filtering:** Optionally filter and process only files created or modified after a specified start date.
- **Dynamic Appending:** Adds a standard appendix/end-page to all merged documents for consistency.
- **Interactive GUI:** User-friendly interface for selecting files, folders, and configuration options (built with Tkinter).
- **Detailed Logging \& Statistics:** Provides clear logs and a summary of processed, skipped, and errored files.


## Why This Project?

> **Note:** Many design choices (such as filename conventions, folder structure, and the inclusion of a standard appendix) were made to optimize a specific workflow at my current job. This version prioritizes speed and reliability for that use case.
> **Future updates** will focus on making the tool more customizable and flexible for broader applications.

## Installation

**Prerequisites:**

- Python 3.7+
- pip

**Install dependencies:**

```
pip install -r requirements.txt
```


## Usage

**Interactive Mode:**

```
python main.py
```

The application will guide you through:

1. Selecting the source folder for main PDFs
2. Selecting the supplementary data folder (optional)
3. Selecting a standard appendix/end-page PDF (optional)
4. Selecting the output folder
5. Entering a start date for processing

**Programmatic Usage:**

```python
from pdf_document_processor import ProcessorConfig, DocumentProcessor

config = ProcessorConfig(
    source_folder="/path/to/source",
    supplementary_folder="/path/to/supplementary",
    appendix_file="/path/to/appendix.pdf",
    output_folder="/path/to/output",
    start_date="YYYY-MM-DD"
)
processor = DocumentProcessor(config)
stats = processor.process_documents()
print(f"Processed: {stats['processed']}, Errors: {stats['errors']}")
```


## Project Structure

```
pdf-merge-utility/
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── document_processor.py
│   ├── file_utils.py
│   ├── gui_utils.py
│   └── pdf_operations.py
├── README.md
├── requirements.txt
├── setup.py
└── main.py
```


## Dependencies

- [pypdf](https://pypdf.readthedocs.io/): PDF manipulation library
- [tkinter](https://docs.python.org/3/library/tkinter.html): GUI toolkit (included with Python)


## Future Plans

- Add support for custom filename patterns and matching rules
- Allow user-defined processing workflows
- Improve error reporting and batch processing options
- Enhance UI for broader usability


## License

MIT License – see [LICENSE](LICENSE) for details.


## Acknowledgments

- [pypdf](https://github.com/py-pdf/pypdf) for PDF manipulation

---

**Contact:**
Malek Elaghel – malekelaghel@gmail.com | [GitHub Repo](https://github.com/it-malek/)