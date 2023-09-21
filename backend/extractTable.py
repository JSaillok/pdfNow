import os
import tabula

tables_folder = os.path.expanduser("~/pdfNow")  # Path to the "Images" folder on your computer
output_directory = os.path.join(tables_folder, "Tables")  # Create "pdfNow" directory in "Images" folder

def tables_pdf(filename, output_directory):
  if not os.path.exists(output_directory):
    os.makedirs(output_directory)

  # read PDF file
  tables = tabula.read_pdf(filename, pages='all')
  pdf_name = os.path.splitext(os.path.basename(filename))[0]

  for i, table in enumerate(tables):
    table.to_excel(os.path.join(output_directory, f"{pdf_name}_table_{i + 1}.xlsx"), index=False)