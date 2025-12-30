"""
Public API:
- HeaderWriter: writes the document header
- TableWriter: renders table based form layouts
- DocxSettings: applies global document styling
- ROWS_DATASET: declarative table layout definition
- COLUMN_WIDTHS_DATASET: declarative column-width definitions (in inches)
- GoogleDriveUploader: uploads generated files to Google Drive
"""

from .core import DocxSettings, HeaderWriter, TableWriter
from .dataset import ROW_HEIGHTS_DATASET, COLUMN_WIDTHS_DATASET
from .integrations import GoogleDriveUploader

__version__ = "0.0.2"

__all__ = [
    "HeaderWriter",
    "TableWriter",
    "DocxSettings",
    "ROW_HEIGHTS_DATASET",
    "COLUMN_WIDTHS_DATASET",
    "GoogleDriveUploader"
]
