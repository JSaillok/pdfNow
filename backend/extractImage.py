import os
import fitz

images_folder = os.path.expanduser("~/Images")  # Path to the "Images" folder on your computer
output_directory = os.path.join(images_folder, "pdfNow")  # Create "pdfNow" directory in "Images" folder


def prosses_pdf(filename, output_directory):
  if not os.path.exists(output_directory):
    os.makedirs(output_directory)

  pdf_document = fitz.open(filename)
  pdf_name = os.path.splitext(os.path.basename(filename))[0]

  for page_number in range(len(pdf_document)):
     page= pdf_document[page_number]
     image_list = page.get_images(full=True)

     for img_index, img in enumerate(image_list):
        xref = img[0]
        base_image = pdf_document.extract_image(xref)
        image_data = base_image["image"]
        image_filename = os.path.join(output_directory, f"{pdf_name}_page_{page_number + 1}_img_{img_index}.png")

        with open(image_filename, "wb") as image_file:
           image_file.write(image_data)

  pdf_document.close()