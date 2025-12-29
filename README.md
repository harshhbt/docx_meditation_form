# docx-forms

A small library for generating court-ready DOCX files (Mediation Application Form).

**Documentation:** https://harshhbt.github.io/docx_meditation_form/

## Installation

```console
git clone --depth 1 https://github.com/harshhbt/docx_meditation_form
cd docx_meditation_form
pip install -e .
```

## Quick start

```python
from docx import Document

from docx_meditation_form.core import DocxSettings, HeaderWriter, TableWriter
from docx_meditation_form.dataset import (
    COLUMN_WIDTHS_DATASET,
    ROW_HEIGHTS_DATASET,
    FormValues,
)

doc = Document()
settings = DocxSettings(doc)
settings.set_top_margin()
settings.set_section()

HeaderWriter(doc).write()

values = FormValues(
    # Applicant
    APPLICANT_NAME="HARSH KUMAR",
    APPLICANT_BRANCH_ADDRESS="2nd Floor, Orion Plaza, MG Road, Bengaluru",
    APPLICANT_CORRESPONDENCE_BRANCH_ADDRESS="Same as above",
    APPLICANT_PHONE="080-12345678",
    APPLICANT_MOBILE="+91-9876543210",
    APPLICANT_EMAIL_ID="info@kslegal.co.in",
    # Defendant
    DEFENDANT_NAME="RAHUL SHARMA",
    DEFENDANT_BRANCH_ADDRESS="Flat 504, Shanti Residency, Noida",
    DEFENDANT_CORRESPONDENCE_BRANCH_ADDRESS="Same as above",
    DEFENDANT_PHONE="0120-4455667",
    DEFENDANT_MOBILE="+91-9123456789",
    DEFENDANT_EMAIL_ID="rahul.sharma@example.com",
)

table_writer = TableWriter(doc)
table = table_writer.init_table()
table_writer.set_columns_width(table, COLUMN_WIDTHS_DATASET)
table_writer.set_rows_height(table, ROW_HEIGHTS_DATASET)
table_writer.merge_required_rows(table)
table_writer.write_table(table, values)

doc.save("demo.docx")
```

This will create your `demo.docx` file in your current folder.

![DOCX preview](.github/images/Screenshot%20from%202025-12-30%2004-11-43.png)


## Upload to Google Drive

make sure you have dependencies installed:

```console
pip install python-docx google-api-python-client google-auth
```

then:

```python
from docx_meditation_form.integrations import GoogleDriveUploader

uploader = GoogleDriveUploader("path/to/credentials.json")
file_id = uploader.upload_file(
    "demo.docx",
    drive_folder_id="YOUR_FOLDER_ID",
)
print(f"https://drive.google.com/file/d/{file_id}")
```

Supported credentials: Service Account JSON or OAuth `token.json` (see https://support.google.com/cloud/answer/15549257?sjid=2279917415296057426-NC
).

## Methodology (How the PDF was converted to DOCX manually)

1. The first step involved reverse-engineering the original PDF to identify the exact typography used in the form. Using [**pdfplumber**](https://github.com/jsvine/pdfplumber), each character was extracted along with its font name and font size, allowing precise inspection of the document’s text styling.

```python
import pdfplumber  # pip install pdfplumber

with pdfplumber.open("input.pdf") as pdf:
    for page_no, page in enumerate(pdf.pages):
        for char in page.chars:
            print({
                "page": page_no + 1,
                "text": char["text"],
                "font": char["fontname"],
                "size": char["size"],
            })
```

2. After identifying fonts and sizes, the physical spacing of the document was analyzed. Line gaps, section spacing, and layout measurements were taken using a PDF scale-measurement tool ([apitemplate.io's](https://apitemplate.io/pdf-tools/pdf-measuring-tool/) PDF measuring utility was used). For sensitive documents, offline tools such as Adobe Acrobat are recommended.

![preview](.github/images/Screenshot%20from%202025-12-28%2005-30-51.png)

3. Using the collected typography and spacing data, the entire form was reconstructed programmatically with **python-docx**, ensuring that margins, row heights, borders, alignments, and text formatting closely match the original PDF layout.

## Project structure

```console
docx_meditation_form/
├── __init__.py                  # package entrypoint + public API re-exports
│
├── core/
│   ├── __init__.py              # defines core subpackage boundary and exports writers/settings
│   ├── header_writer.py         # writes the fixed court-mandated document header
│   ├── table_writer.py          # orchestrates table creation, layout rules, and data rendering
│   ├── cell_formatter.py        # low-level helpers for cell + paragraph formatting
│   ├── settings.py              # single source of truth for margins, fonts, run styling
│   └── colors.py                # centralized RGB color constants
│
├── dataset/
│   ├── __init__.py              # exposes layout constants and FormValues container
│   ├── dataset.py               # declarative table layout (column widths, row heights)
│   └── form_values.py           # normalized data container for one form submission
│
├── integrations/
│   ├── __init__.py              # integration namespace boundary
│   └── google_drive.py          # uploads generated DOCX files to Google Drive
│
├── quickstart.py                # runnable end-to-end usage example
├── README.md                    # user-facing docs and methodology
├── setup.py                     # packaging, dependencies, and install metadata
├── .gitignore                   # git ignore rules
└── .gitattributes               # git attributes (LFS config)
```
