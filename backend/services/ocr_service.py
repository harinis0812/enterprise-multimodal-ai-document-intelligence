from paddleocr import PaddleOCR


ocr = PaddleOCR(
    lang="en",
    enable_mkldnn=False
)


def extract_text_from_image(file_path):

    result = ocr.predict(file_path)

    extracted_text = []

    for res in result:

        if isinstance(res, dict):

            rec_texts = res.get("rec_texts", [])

            extracted_text.extend(rec_texts)

    return " ".join(extracted_text)