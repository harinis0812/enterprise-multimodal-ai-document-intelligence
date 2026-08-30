from fastapi import FastAPI

from backend.api.document import router as document_router
from backend.database.database import Base, engine
from backend.database import models


# Create database tables
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Enterprise Multimodal AI Document Intelligence Platform",
    description="AI-powered document processing and intelligence platform",
    version="1.0.0"
)


app.include_router(
    document_router
)


@app.get("/")
def root():

    return {
        "message": "Enterprise Multimodal AI Document Intelligence Platform is running"
    }


@app.get("/about")
def about():

    return {
        "project": "Enterprise Grade Multimodal AI Document Intelligence Platform using Agentic AI"
    }