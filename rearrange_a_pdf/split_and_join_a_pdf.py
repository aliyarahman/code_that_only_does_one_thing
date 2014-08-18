from pyPdf import PdfFileWriter, PdfFileReader

output = PdfFileWriter()
input1 = PdfFileReader(file("test.pdf", "rb"))

output.addPage(input1.getPage(8))
output.addPage(input1.getPage(15))

print "number of pages is: %s " % output.getNumPages()

outputStream = file("assembled_pdf.pdf", "wb")
output.write(outputStream)
outputStream.close()
