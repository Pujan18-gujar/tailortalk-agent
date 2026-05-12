import os
from googleapiclient.discovery import build
from google.oauth2 import service_account
from dotenv import load_dotenv

load_dotenv()

SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
SERVICE_ACCOUNT_FILE = 'credentials.json'
FOLDER_ID = os.getenv('GOOGLE_DRIVE_FOLDER_ID')

def get_drive_service():
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return build('drive', 'v3', credentials=creds)

def search_drive_files(query: str) -> str:
    try:
        service = get_drive_service()
        folder_query = f"'{FOLDER_ID}' in parents and {query}"
        results = service.files().list(
            q=folder_query,
            pageSize=10,
            fields="files(id, name, mimeType, modifiedTime, webViewLink)"
        ).execute()
        files = results.get('files', [])
        if not files:
            return "No files found matching your search."
        output = f"Found {len(files)} file(s):\n\n"
        for f in files:
            output += f"📄 **{f['name']}**\n"
            output += f"   Type: {f['mimeType']}\n"
            output += f"   Modified: {f['modifiedTime'][:10]}\n"
            output += f"   Link: {f.get('webViewLink', 'N/A')}\n\n"
        return output
    except Exception as e:
        return f"Error searching Drive: {str(e)}"