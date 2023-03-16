import PyPDF2

# Open the input PDF files that we will use
template = PyPDF2.PdfFileReader(open('input.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))

# Create a new PDF writer that will contain our watermarked pages
output = PyPDF2.PdfFileWriter()

# Loop through each page in the input PDF
for i in range(template.getNumPages()):
	# Get the current page from the input PDF
	page = template.getPage(i)

	# Merge the watermark PDF onto the current page
	page.mergePage(watermark.getPage(0))

	# Add the watermarked page to our output PDF writer
	output.addPage(page)

# Write the watermarked PDF to a file
with open('watermarked_output.pdf', 'wb') as file:
	output.write(file)
