import fitz

# Create a document object
doc = fitz.open('file.pdf')  # or fitz.Document(filename)

# Get the page by their index
page = doc.load_page(0) # or page = doc[0]

# get all links on a page
links = page.get_links()
print(links)

# get the links on all pages
for i in range(doc.page_count):
  page = doc.load_page(i)
  link = page.get_links()
  print(link)