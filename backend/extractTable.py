import os
import pdfplumber

images_folder = os.path.expanduser("~/Tables")  # Path to the "Images" folder on your computer
output_directory = os.path.join(images_folder, "pdfNow")  # Create "pdfNow" directory in "Images" folder

def tables_pdf(filename, output_directory):
  if not os.path.exists(output_directory):
    os.makedirs(output_directory)

    with pdfplumber.open(filename) as pdf:
        # iterate over each page
        for page in pdf.pages:
            print(page.extract_tables())