from PyPDF2 import PdfFileWriter, PdfFileReader

pdfWriter = PdfFileWriter()
pdf = PdfFileReader("1.pdf")
for page_num in range(pdf.numPages):
    pdfWriter.addPage(pdf.getPage(page_num))
password = "123"
pdfWriter.encrypt(password)
with open('ho.pdf', 'wb') as f:
    pdfWriter.write(f)
    f.close()
