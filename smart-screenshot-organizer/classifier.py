import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Tesseract-OCR\tesseract.exe"


def preprocess_image(image):

    # Convert to grayscale
    image = image.convert("L")

    # Increase contrast
    image = image.point(lambda x: 0 if x < 140 else 255)

    return image


def extract_text(image_path):

    img = Image.open(image_path)

    img = preprocess_image(img)

    text = pytesseract.image_to_string(img, config="--psm 6")

    text = text.lower()

    text = text.replace("\n", " ")
    text = text.replace("\t", " ")

    return text


def categorize_image(text):

    if "amazon" in text or "price" in text or "buy" in text:
        return "Shopping"

    elif "python" in text or "error" in text or "code" in text:
        return "Coding"

    elif "study" in text or "lecture" in text or "assignment" in text:
        return "Study"

    elif "chat" in text or "message" in text or "whatsapp" in text:
        return "Social"

    else:
        return "Others"
