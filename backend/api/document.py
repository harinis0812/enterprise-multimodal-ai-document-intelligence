from fastapi import APIRouter, UploadFile, File
import shutil
import os

from backend.services.pdf_service import extract_text_from_pdf
from backend.services.ocr_service import extract_text_from_image

router = APIRouter()

UPLOAD_FOLDER = "backend/uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    extracted_text = ""

    filename = file.filename.lower()

    # PDF processing
    if filename.endswith(".pdf"):
        extracted_text = extract_text_from_pdf(file_path)

    # Image OCR
    elif filename.endswith((".jpg", ".jpeg", ".png")):
        extracted_text = extract_text_from_image(file_path)

    return {
        "filename": file.filename,
        "message": "Document processed successfully",
        "text": extracted_text[:2000]
    }