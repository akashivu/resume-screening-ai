import fitz
import re

def extract_text_from_pdf(pdf_path):

    text=""

    pdf_document=fitz.open(pdf_path)

    for page in pdf_document:
        text+=page.get_text()

    return text

#clean text
def clean_text(text):
    text=text.lower()

    text=re.sub(r'\n',' ', text)
    
    text = re.sub(r'[^a-zA-Z0-9 ]', '', text)

    text = re.sub(r'\s+', ' ', text)

    return text







