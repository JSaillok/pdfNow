import pdfplumber

with pdfplumber.open('file.pdf') as pdf:
    # iterate over each page
    for page in pdf.pages:
        print(page.extract_tables())