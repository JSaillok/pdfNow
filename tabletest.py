import camelot

# PDF file to extract tables from
file = "table.pdf"

# extract all the tables in the PDF file
tables = camelot.read_pdf(file)

# number of tables extracted
print("Total tables extracted:", tables.n)

# print the first table as a Pandas DataFrame
print(tables[0].df)

# export individually as Excel (.xlsx extension)
tables[0].to_excel("foo.xlsx")

# or export all in a zip
tables.export("foo.csv", f="csv", compress=True)