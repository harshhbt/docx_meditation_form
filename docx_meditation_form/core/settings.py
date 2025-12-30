# core/settings.py
from docx.document import Document
from docx.shared import Inches, Pt, RGBColor
from docx.text.run import Run

TOP_MARGIN = Inches(0.2291667)

FONT_NAME = "Times New Roman"
FONT_SIZE = Pt(10.82727336883545)


class Color:
    """Centralized color palette."""

    BLACK = RGBColor(0x00, 0x00, 0x00)


class DocxSettings:
    """
    Centralized document-wide styling and layout configuration.

    This class is responsible for:
    - Page margins
    - Default font name and size
    - Consistent run-level styling

    Parameters
    ----------
    doc : `docx.document.Document`
        Target document whose sections and runs will be modified.
    """

    def __init__(self, doc: Document) -> None:
        self.doc = doc

    def set_section(self):
        """
        Configure left and right margins for the first document section.
        Intended to match the original PDF layout measurements.
        """
        section = self.doc.sections[0]
        section.left_margin = Inches(0.45)
        section.right_margin = Inches(0.45)

    def set_top_margin(self):
        """
        Set the top margin of the first document section.
        """
        self.doc.sections[0].top_margin = TOP_MARGIN

    @staticmethod
    def apply_run_style(run: Run, *, bold=False, underline=False):
        """
        Apply the default font styling to a text run.

        :param run: The run to style.
        :type run: ``docx.text.run.Run``

        :param bold: Whether the text should be bold.
        :type bold: ``bool``

        :param underline: Whether the text should be underlined.
        :type underline: ``bool``
        """
        run.font.name = FONT_NAME
        run.font.size = FONT_SIZE
        run.font.color.rgb = Color.BLACK
        run.bold = bold
        run.underline = underline
