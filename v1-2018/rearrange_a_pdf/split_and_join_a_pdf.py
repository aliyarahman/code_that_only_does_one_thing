# This is the pyPdf library. Install with: $ pip install pyPdf
from pyPdf import PdfFileWriter, PdfFileReader

# Open a writer object
output = PdfFileWriter() 
# Load the pdf file(s) you want to input pages from
input1 = PdfFileReader(file("test.pdf", "rb"))

# Add some pages from your source/input files to the writer object
output.addPage(input1.getPage(8))
output.addPage(input1.getPage(15))

# For kicks, print the number of pages added to the console
print "number of pages is: %s " % output.getNumPages()

# Explain the kind of file this will be when outputted
outputStream = file("assembled_pdf.pdf", "wb")

# Write the actual output file
output.write(outputStream)

# Close the output file
outputStream.close()
