from docx.shared import Inches

"""Table layout constants for DOCX generation."""

# Fixed column widths for the form table
COLUMN_WIDTHS_DATASET = [Inches(0.39), Inches(1.30), Inches(5.68)]

# Fixed row heights mapped to semantic layout roles
ROW_HEIGHTS_DATASET = {
    "tiny_gap": Inches(0.24),  # Minimal vertical spacing
    "small_text": Inches(0.38),  # Short label rows
    "base_text": Inches(0.46),  # Default text rows
    "section": Inches(1.13),  # Section header blocks
    "major_section": Inches(1.57),  # Large multi-line sections
}
