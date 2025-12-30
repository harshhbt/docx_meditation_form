"""
Public API:
- `HeaderWriter`: writes the document header
- `TableWriter`: renders table based form layouts
- `DocxSettings`: applies global document styling
- `ROW_HEIGHTS_DATASET`: declarative table layout definition
- `FormValues`: represents one complete form submission
- `COLUMN_WIDTHS_DATASET`: declarative column-width definitions (in inches)
- `GoogleDriveUploader`: uploads generated files to Google Drive
"""

from .core import DocxSettings, HeaderWriter, TableWriter
from .dataset import ROW_HEIGHTS_DATASET, COLUMN_WIDTHS_DATASET, FormValues
from .integrations import GoogleDriveUploader

__version__ = "0.0.3"

__all__ = [
    "HeaderWriter",
    "TableWriter",
    "DocxSettings",
    "ROW_HEIGHTS_DATASET",
    "COLUMN_WIDTHS_DATASET",
    "GoogleDriveUploader",
    "FormValues"
]
