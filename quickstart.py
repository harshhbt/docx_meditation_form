from docx import Document

from docx_meditation_form.core import DocxSettings, HeaderWriter, TableWriter
from docx_meditation_form.dataset import (
    COLUMN_WIDTHS_DATASET,
    ROW_HEIGHTS_DATASET,
    FormValues,
)
from docx_meditation_form.integrations import GoogleDriveUploader


def main():
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
    uploader = GoogleDriveUploader("token.json")
    file_id = uploader.upload_file(
        "demo.docx",
        drive_folder_id=None,
    )
    uploader.make_public(file_id) # this allows anyone with the link to view the document
    print(f"https://drive.google.com/file/d/{file_id}/view")


if __name__ == "__main__":
    main()
