from fastapi import FastAPI
from backend.api.document import router as document_router

app = FastAPI(
    title="Enterprise Grade Multimodal AI Document Intelligence Platform",
    description="Agentic AI powered enterprise document processing system",
    version="1.0.0"
)

app.include_router(document_router)

@app.get("/")
def home():
    return {
        "message": "Welcome to Enterprise Grade Multimodal AI Document Intelligence Platform!"
    }

@app.get("/about")
def about():
    return {
        "project": "Enterprise-Grade Multimodal AI Document Intelligence Platform using Agentic AI",
        "version": "1.0.0"
    }