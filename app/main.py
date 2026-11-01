# app/main.py
from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="Semantic Data Lifecycle Manager API",
    description="Backend API for local NLP storage optimization",
    version="1.0.0"
)

# Register the API routes
app.include_router(router, prefix="/api")

@app.get("/")
def health_check():
    return {"status": "active", "system": "Semantic Data Manager Backend running."}