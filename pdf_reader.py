import PyPDF2
import re

def pdf_to_text(pdf_file: str) -> str:
    with open(pdf_file, 'rb') as pdf:
        reader = PyPDF2.PdfReader(pdf)
        pdf_text = []

        try:
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                content = page.extract_text()
                content = content.replace('\n', '')
                content = content.replace('-','')
                pdf_text.append(content)

        except Exception as e:
            print(f"An error occurred: {e}")
        return pdf_text

extracted_text = pdf_to_text('Azkar-idatzi_abf.pdf')
print(extracted_text)
text=[]
for lines in extracted_text:
    words = lines.split()
    for word in words:
        text.append(word)
    print(text)