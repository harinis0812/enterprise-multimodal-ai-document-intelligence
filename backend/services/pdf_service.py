import fitz
import os

from backend.services.ocr_service import extract_text_from_image


def extract_text_from_pdf(pdf_path):

    document = fitz.open(pdf_path)

    extracted_text = []

    for page in document:

        # Try normal text extraction first
        page_text = page.get_text().strip()

        if page_text:
            extracted_text.append(page_text)

        else:
            # Scanned PDF: convert page to image
            pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))

            image_path = (
                f"backend/uploads/temp_page_{page.number}.png"
            )

            pix.save(image_path)

            # OCR the converted image
            ocr_text = extract_text_from_image(image_path)

            extracted_text.append(ocr_text)

            # Remove temporary image
            if os.path.exists(image_path):
                os.remove(image_path)

    document.close()

    return "\n".join(extracted_text)