import re


def extract_report_information(text):

    information = {}

    patterns = {
        "employee_name": r"employee name:\s*(.+)",
        "department": r"department:\s*(.+)",
        "experience": r"experience:\s*(.+)"
    }

    for key, pattern in patterns.items():

        match = re.search(
            pattern,
            text,
            re.IGNORECASE
        )

        if match:
            information[key] = match.group(1).strip()

    return information


def extract_invoice_information(text):

    information = {}

    patterns = {
        "invoice_number": r"invoice\s*(number|no|#)?\s*[:\-]?\s*([A-Za-z0-9\-]+)",
        "invoice_date": r"(invoice date|date)\s*[:\-]?\s*(.+)",
        "vendor": r"(vendor|seller|company)\s*[:\-]?\s*(.+)",
        "total_amount": r"(total|grand total|amount due)\s*[:\-]?\s*[$₹]?\s*([0-9,]+(?:\.\d{2})?)"
    }

    for key, pattern in patterns.items():

        match = re.search(
            pattern,
            text,
            re.IGNORECASE
        )

        if match:

            if key == "invoice_number":
                information[key] = match.group(2).strip()

            elif key in ["invoice_date", "vendor"]:
                information[key] = match.group(2).strip()

            elif key == "total_amount":
                information[key] = match.group(2).strip()

    return information


def extract_resume_information(text):

    information = {}

    # Email
    email_match = re.search(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        text
    )

    if email_match:
        information["email"] = email_match.group()

    # Phone number
    phone_match = re.search(
        r"\+?\d[\d\s-]{8,}\d",
        text
    )

    if phone_match:
        information["phone"] = phone_match.group()

    # Skills
    skills = []

    skill_keywords = [
        "python",
        "machine learning",
        "deep learning",
        "fastapi",
        "docker",
        "tensorflow",
        "pytorch",
        "sql",
        "java"
    ]

    text_lower = text.lower()

    for skill in skill_keywords:

        if skill in text_lower:
            skills.append(skill.title())

    if skills:
        information["skills"] = skills

    return information