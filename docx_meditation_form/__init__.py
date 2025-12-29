"""
Public API:
- HeaderWriter: writes the document header
- TableWriter: renders table based form layouts
- DocxSettings: applies global document styling
- ROWS_DATASET: declarative table layout definition
- GoogleDriveUploader: uploads generated files to Google Drive
"""

from .core import DocxSettings, HeaderWriter, TableWriter

__version__ = "0.0.1"

__all__ = [
    "HeaderWriter",
    "TableWriter",
    "DocxSettings",
]
