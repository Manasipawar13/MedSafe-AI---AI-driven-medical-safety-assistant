import pytesseract
pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"
from PIL import Image


def extract_text_from_image(uploaded_file):

    image = Image.open(uploaded_file)

    text = pytesseract.image_to_string(image)


    return text

