from backend.services.information_extractor import (
    extract_report_information,
    extract_invoice_information,
    extract_resume_information
)


def analyze_document(text, document_type):

    if document_type == "Report":

        return extract_report_information(text)

    elif document_type == "Invoice":

        return extract_invoice_information(text)

    elif document_type == "Resume":

        return extract_resume_information(text)

    elif document_type == "Form":

        return {
            "message": "Form intelligence will be added next"
        }

    else:

        return {
            "message": "Document type not supported yet"
        }