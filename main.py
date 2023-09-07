#here will be the menu of application

import extractImg
import extractTable
import fitz

# Create a document object
doc = fitz.open('file.pdf')  # or fitz.Document(filename)

# the metadata (dict) e.g., the author,...
print(doc.metadata)
