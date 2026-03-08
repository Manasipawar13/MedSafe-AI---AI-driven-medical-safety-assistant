import streamlit as st

st.write("Medical Safety Assistant")


import pytesseract
from PIL import Image
menu = st.sidebar.selectbox(
    "Select Feature",
    ["Prescription Scanner","Symptom Checker","Drug Interaction"]
)


pytesseract.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR\tesseract.exe"

st.title("MedSafe AI - Prescription Scanner")

uploaded_file = st.file_uploader("Upload Prescription Image")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Prescription")

    text = pytesseract.image_to_string(image)

    st.subheader("Extracted Text")

    st.write(text)

