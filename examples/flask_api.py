from flask import Flask, request, jsonify
from functools import wraps
import tempfile
import os
import base64

from docx import Document

from docx_meditation_form.core import DocxSettings, HeaderWriter, TableWriter
from docx_meditation_form.dataset import (
    COLUMN_WIDTHS_DATASET,
    ROW_HEIGHTS_DATASET,
    FormValues,
)
from docx_meditation_form.integrations import GoogleDriveUploader

app = Flask(__name__)

API_PASSWORD = b'https://www.youtube.com/watch?v=dQw4w9WgXcQ' # change this with a secure secret
API_KEY = base64.b64encode(API_PASSWORD).decode("utf-8")
GOOGLE_TOKEN_PATH = "token.json"


def require_auth(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if request.headers.get("X-API-KEY") != API_KEY:
            return jsonify({"error": "unauthorized"}), 401
        return fn(*args, **kwargs)
    return wrapper

# Test endpoint:
# curl -X POST http://localhost:8080/generate-docx \
#   -H "Content-Type: application/json" \
#   -H "X-API-KEY: ${base64-api-key}" \
#   -d '{
#     "APPLICANT_NAME": "HARSH KUMAR",
#     "APPLICANT_BRANCH_ADDRESS": "2nd Floor, Orion Plaza, MG Road, Bengaluru",
#     "APPLICANT_CORRESPONDENCE_BRANCH_ADDRESS": "Same as above",
#     "APPLICANT_PHONE": "080-12345678",
#     "APPLICANT_MOBILE": "+91-9876543210",
#     "APPLICANT_EMAIL_ID": "info@kslegal.co.in",
#     "DEFENDANT_NAME": "RAHUL SHARMA",
#     "DEFENDANT_BRANCH_ADDRESS": "Flat 504, Shanti Residency, Noida",
#     "DEFENDANT_CORRESPONDENCE_BRANCH_ADDRESS": "Same as above",
#     "DEFENDANT_PHONE": "0120-4455667",
#     "DEFENDANT_MOBILE": "+91-9123456789",
#     "DEFENDANT_EMAIL_ID": "rahul.sharma@example.com"
#   }'
@app.route("/generate-docx", methods=["POST"])
@require_auth
def generate_docx():
    data = request.json or {}
    values = FormValues(**data)

    doc = Document()
    settings = DocxSettings(doc)
    settings.set_top_margin()
    settings.set_section()
    HeaderWriter(doc).write()

    table_writer = TableWriter(doc)
    table = table_writer.init_table()
    table_writer.set_columns_width(table, COLUMN_WIDTHS_DATASET)
    table_writer.set_rows_height(table, ROW_HEIGHTS_DATASET)
    table_writer.merge_required_rows(table)
    table_writer.write_table(table, values)

    # write to temp file
    with tempfile.NamedTemporaryFile(suffix=".docx", delete=False) as tmp:
        doc.save(tmp.name)
        tmp_path = tmp.name

    uploader = GoogleDriveUploader(GOOGLE_TOKEN_PATH)
    file_id = uploader.upload_file(tmp_path)
    uploader.make_public(file_id)

    os.remove(tmp_path)

    return jsonify({
        "url": f"https://drive.google.com/file/d/{file_id}"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
