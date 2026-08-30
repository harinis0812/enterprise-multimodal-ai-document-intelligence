from fastapi import APIRouter, UploadFile, File, HTTPException
import shutil
import os
import json

from backend.services.pdf_service import extract_text_from_pdf
from backend.services.ocr_service import extract_text_from_image
from backend.services.document_classifier import detect_document_type
from backend.services.document_intelligence import analyze_document

from backend.database.database import SessionLocal
from backend.database.models import Document


router = APIRouter()

UPLOAD_FOLDER = "backend/uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):

    # Create file path
    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    # Save uploaded file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer
        )

    extracted_text = ""

    filename = file.filename.lower()

    # PDF processing
    if filename.endswith(".pdf"):

        extracted_text = extract_text_from_pdf(
            file_path
        )

    # Image OCR processing
    elif filename.endswith(
        (".jpg", ".jpeg", ".png")
    ):

        extracted_text = extract_text_from_image(
            file_path
        )

    # Detect document type
    document_type = detect_document_type(
        extracted_text
    )

    # Document-specific intelligence
    document_information = analyze_document(
        extracted_text,
        document_type
    )

    # Create database session
    db = SessionLocal()

    # Create document record
    new_document = Document(
        filename=file.filename,
        document_type=document_type,
        extracted_text=extracted_text,
        extracted_information=json.dumps(
            document_information
        )
    )

    # Save document
    db.add(new_document)

    db.commit()

    db.refresh(new_document)

    document_id = new_document.id

    db.close()

    return {
        "id": document_id,
        "filename": file.filename,
        "message": "Document processed and saved successfully",
        "document_type": document_type,
        "document_information": document_information,
        "text": extracted_text[:2000]
    }


@router.get("/documents")
def get_documents():

    db = SessionLocal()

    documents = db.query(
        Document
    ).all()

    results = []

    for document in documents:

        results.append(
            {
                "id": document.id,
                "filename": document.filename,
                "document_type": document.document_type,
                "document_information": json.loads(
                    document.extracted_information
                ),
                "uploaded_at": document.uploaded_at
            }
        )

    db.close()

    return results


@router.get("/documents/{document_id}")
def get_document(document_id: int):

    db = SessionLocal()

    document = db.query(
        Document
    ).filter(
        Document.id == document_id
    ).first()

    if not document:

        db.close()

        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )

    result = {
        "id": document.id,
        "filename": document.filename,
        "document_type": document.document_type,
        "document_information": json.loads(
            document.extracted_information
        ),
        "extracted_text": document.extracted_text,
        "uploaded_at": document.uploaded_at
    }

    db.close()

    return result