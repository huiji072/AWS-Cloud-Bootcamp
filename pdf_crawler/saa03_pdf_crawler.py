import PyPDF2

file = 'saa_dump.pdf'

with open(file, mode='rb') as f:

    reader = PyPDF2.PdfFileReader(f)

    page = reader.getPage(0)

    print(page.extractText())

