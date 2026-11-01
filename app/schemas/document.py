# app/schemas/document.py
from pydantic import BaseModel
from typing import Optional

class FileDocument(BaseModel):
    filename: str
    filepath: str
    content: str
    semantic_category: Optional[str] = None
    distance: Optional[float] = None