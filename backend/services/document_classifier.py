def detect_document_type(text):

    text = text.lower()

    # Invoice
    if (
        "invoice" in text
        or "invoice number" in text
        or "amount due" in text
        or "grand total" in text
    ):
        return "Invoice"

    # Report
    elif (
        "employee report" in text
        or "report" in text
        or "department" in text
    ):
        return "Report"

    # Resume
    elif (
        "resume" in text
        or "curriculum vitae" in text
        or "education" in text
        or "work experience" in text
    ):
        return "Resume"

    # Form
    elif (
        "form" in text
        or "date of birth" in text
    ):
        return "Form"

    else:
        return "Unknown"