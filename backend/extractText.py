import pdfplumber

with pdfplumber.open('example.pdf') as pdf:
    # iterate over each page
    for page in pdf.pages:
        # extract text
        text = page.extract_text()
        print(text)