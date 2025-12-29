import json
from pathlib import Path
from typing import Any, Dict, Optional

from google.oauth2.credentials import Credentials as OAuthCredentials
from google.oauth2.service_account import Credentials as SACredentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

SCOPES = ["https://www.googleapis.com/auth/drive.file"]


class GoogleDriveUploader:
    """
    Uploads files to Google Drive using either OAuth or Service Account credentials.

    Supported credential formats:
    - Service Account JSON
    - OAuth token.json (with refresh token)

    Parameters
    ----------
    credentials_json_path : str
        Path to the credentials JSON file.
    """

    def __init__(self, credentials_json_path: str) -> None:
        path = Path(credentials_json_path)
        if not path.exists():
            raise FileNotFoundError(f"Credentials file not found: {path}")

        data: Dict[str, Any] = json.loads(path.read_text())

        # Service Account credentials
        if data.get("type") == "service_account":
            self.creds = SACredentials.from_service_account_info(
                data,
                scopes=SCOPES,
            )

        # OAuth credentials
        elif "refresh_token" in data:
            self.creds = OAuthCredentials(
                token=data.get("access_token"),
                refresh_token=data.get("refresh_token"),
                token_uri=data.get("token_uri", "https://oauth2.googleapis.com/token"),
                client_id=data.get("client_id"),
                client_secret=data.get("client_secret"),
                scopes=SCOPES,
            )

        else:
            raise ValueError(
                "Unrecognized credentials JSON format. "
                "Expected service account or OAuth token JSON."
            )

        self.service = build("drive", "v3", credentials=self.creds)

    def upload_file(
        self,
        file_path: str,
        *,
        drive_folder_id: Optional[str] = None,
    ) -> str:
        """
        Upload a file to Google Drive.

        Parameters
        ----------
        file_path : str
            Local path to the file to upload.
        drive_folder_id : str, optional
            Target Drive folder ID. If omitted, uploads to root.

        Returns
        -------
        str
            The Google Drive file ID of the uploaded file.
        """
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"File not found: {path}")

        metadata: Dict[str, Any] = {"name": path.name}

        if drive_folder_id:
            metadata["parents"] = [drive_folder_id]

        media = MediaFileUpload(
            filename=str(path),
            mimetype=(
                "application/vnd.openxmlformats-officedocument."
                "wordprocessingml.document"
            ),
            resumable=True,
        )

        response = (
            self.service.files()
            .create(
                body=metadata,
                media_body=media,
                fields="id",
            )
            .execute()
        )

        return response["id"]
