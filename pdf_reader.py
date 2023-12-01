import PyPDF2,os,re,csv
from datetime import datetime

current_date = datetime.now().strftime("%Y-%m-%d")
csv_dict = {"Index":'',
            "Title":'',
            "Content":''}
csv_list=[]
def pdf_to_text(pdf_file: str) -> str:

    with open('books/'+pdf_file, 'rb') as pdf:
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


books = os.listdir('books')



c=1
content = []


for book in books:
    extracted_text = pdf_to_text(book)
    book = book.replace('.pdf','')
    text=""
    for lines in extracted_text:
        words = lines.split()
        for word in words:
            clean_word = re.sub(r'[^a-zA-Z0-9\s]','',word)
            clean_word = re.sub(r'\s+', ' ', clean_word)
            clean_word = clean_word.strip()
            text += word + ' '

        len_text=len(text)
    csv_dict = {"Index": c,
                "Title": book,
                "Lenght":len_text,
                "Content": text,
                "Current_date":current_date}
    csv_list.append(csv_dict)

    print(f'{c}: {book} with len:{len_text} is added')

    c += 1

with open(f'Liburu_dataseta__{current_date}.csv', mode='w', encoding='utf-8', newline='') as f:
    csv_writer = csv.DictWriter(f, fieldnames=["Index", "Title","Lenght", "Content","Current_date"])
    csv_writer.writeheader()
    csv_writer.writerows(csv_list)

print('The conversion was successful!')