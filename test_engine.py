# test_engine.py
from app.services.nlp_service import ingest_directory, semantic_search
import os

dummy_dir = os.path.join("data", "dummy_files")

print("1. Ingesting files into Vector DB...")
total_files = ingest_directory(dummy_dir)
print(f"Ingested {total_files} files.\n")

print("2. Running Semantic Search for: 'useless web trackers and session data'")
results = semantic_search("useless web trackers and session data", n_results=2)

for result in results:
    print(f"Match: {result.filename} | Distance (lower is closer): {result.distance:.4f}")
    print(f"Content: {result.content}\n")