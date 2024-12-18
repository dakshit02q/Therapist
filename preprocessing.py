import pandas 
import os 
import PyPDF2

pdf_folder = './books'

pdfs = []
titles = []
all_text = []
for filename in os.listdir(pdf_folder):
    if filename.endswith(".pdf"):
        path = os.path.join(pdf_folder, filename)
        reader =  PyPDF2.PdfReader(path)

        text_data = []
        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            text_data.append(text)
        
        





