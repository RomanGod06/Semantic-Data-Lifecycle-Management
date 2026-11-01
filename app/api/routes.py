# app/api/routes.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
import os
from app.services.nlp_service import ingest_directory, semantic_search
from app.schemas.document import FileDocument
import shutil

router = APIRouter()


# Add this to your existing imports at the top of app/api/routes.py

from fastapi import HTTPException

# Add this below your existing SearchQuery class
class FileActionRequest(BaseModel):
    filepath: str

# Add this endpoint at the very bottom of the file
@router.post("/quarantine")
def quarantine_file(request: FileActionRequest):
    """Moves a dormant file to a secure local quarantine vault."""
    if not os.path.exists(request.filepath):
        raise HTTPException(status_code=404, detail="File no longer exists.")
        
    vault_dir = os.path.join("data", "quarantine_vault")
    os.makedirs(vault_dir, exist_ok=True)
    
    filename = os.path.basename(request.filepath)
    safe_path = os.path.join(vault_dir, filename)
    
    try:
        shutil.move(request.filepath, safe_path)
        return {"status": "success", "message": f"Secured {filename} in vault."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class SearchQuery(BaseModel):
    query: str
    n_results: int = 3

class IngestRequest(BaseModel):
    directory_path: str

@router.post("/ingest")
def trigger_ingestion(request: IngestRequest):
    """Endpoint to trigger scanning on any provided local directory."""
    if not os.path.exists(request.directory_path):
        raise HTTPException(status_code=400, detail="Directory path does not exist on this machine.")
        
    total_files = ingest_directory(request.directory_path)
    return {"status": "success", "message": f"Successfully safely ingested {total_files} text/log files."}

@router.post("/search", response_model=List[FileDocument])
def perform_search(request: SearchQuery):
    results = semantic_search(request.query, request.n_results)
    return results