import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import Tool
from drive_tool import search_drive_files

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0.3
)

drive_tool = Tool(
    name="DriveSearchTool",
    func=search_drive_files,
    description="Search files in Google Drive"
)

def _build_query(message: str) -> str:
    message = message.lower()
    if "pdf" in message:
        return "mimeType = 'application/pdf'"
    elif "image" in message or "photo" in message:
        return "mimeType contains 'image'"
    elif "sheet" in message:
        return "mimeType contains 'spreadsheet'"
    elif "doc" in message:
        return "mimeType contains 'document'"
    elif "folder" in message:
        return "mimeType = 'application/vnd.google-apps.folder'"
    else:
        words = [w for w in message.split() if len(w) > 3 and w not in ["find","show","get","list","all","files","search"]]
        if words:
            return f"name contains '{words[0]}'"
        return "trashed = false"

def chat(message: str, history: list) -> str:
    try:
        query = _build_query(message)
        result = drive_tool.func(query)
        return result
    except Exception as e:
        return f"Error: {str(e)}"
