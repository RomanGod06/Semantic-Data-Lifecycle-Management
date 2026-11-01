# app/services/nlp_service.py
import os
import chromadb
from sentence_transformers import SentenceTransformer
from app.schemas.document import FileDocument

CHROMA_PATH = os.path.join("data", "chroma_storage")
chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)
collection = chroma_client.get_or_create_collection(name="semantic_file_index")

print("Loading MiniLM Edge NLP model...")
model = SentenceTransformer('all-MiniLM-L6-v2')

# Engineering Guardrails
ALLOWED_EXTENSIONS = {'.txt', '.log', '.json', '.csv', '.md', '.tmp'}
MAX_TEXT_LENGTH = 1500  # Truncate long files to fit the NLP context window and save RAM

def ingest_directory(directory_path: str):
    """Safely scans a real directory, with a bulletproof block on system and venv files."""
    if not os.path.exists(directory_path):
        return 0

    # WIPE THE OLD DATABASE BEFORE SCANNING A NEW FOLDER
    global collection
    try:
        chroma_client.delete_collection("semantic_file_index")
    except ValueError:
        pass # Ignores error if collection doesn't exist yet
    collection = chroma_client.get_or_create_collection(name="semantic_file_index")

    # Add .venv and the data folders to the ignore list
    IGNORE_DIRS = {'venv', '.venv', 'env', '.env', '.git', '__pycache__', 'node_modules', '.pytest_cache', 'quarantine_vault', 'chroma_storage'}
    
    count = 0
    for root, _, files in os.walk(directory_path):
        # Bulletproof block: split the path (e.g., C:\...\venv\Lib) and check for forbidden folders
        path_parts = set(root.split(os.sep))
        if IGNORE_DIRS.intersection(path_parts):
            continue  # Skip this entire directory instantly
            
        for filename in files:
            ext = os.path.splitext(filename)[1].lower()
            if ext not in ALLOWED_EXTENSIONS:
                continue 
            
            filepath = os.path.join(root, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read(MAX_TEXT_LENGTH)
                
                if not content.strip():
                    continue

                embedding = model.encode(content).tolist()
                
                collection.upsert(
                    ids=[filepath],
                    embeddings=[embedding],
                    metadatas=[{"filepath": filepath, "filename": filename}],
                    documents=[content]
                )
                count += 1
            except (PermissionError, UnicodeDecodeError, OSError):
                continue
                
    return count

def semantic_search(query: str, n_results: int = 3):
    query_embedding = model.encode(query).tolist()
    results = collection.query(query_embeddings=[query_embedding], n_results=n_results)
    
    parsed_results = []
    if results['documents'] and results['documents'][0]:
        for i in range(len(results['documents'][0])):
            doc = FileDocument(
                filename=results['metadatas'][0][i]['filename'],
                filepath=results['metadatas'][0][i]['filepath'],
                content=results['documents'][0][i],
                distance=results['distances'][0][i] if results.get('distances') else None
            )
            parsed_results.append(doc)
    return parsed_results