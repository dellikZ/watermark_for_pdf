import sys
import PyPDF2



pdf_file = sys.argv[1]
watermark = sys.argv[2]
final_pdf = sys.argv[3]

with open(pdf_file, mode = 'rb') as file, open(watermark, mode = 'rb') as wtr:
	original_pdf = PyPDF2.PdfFileReader(file)
	wtr_pdf = PyPDF2.PdfFileReader(wtr)
	wtr_page = wtr_pdf.getPage(0)

	output = PyPDF2.PdfFileWriter()

	for item in range(original_pdf.getNumPages()):
		pdf_page = original_pdf.getPage(item)
		pdf_page.mergePage(wtr_page)
		output.addPage(pdf_page)

	with open(final_pdf, "wb") as final:
		output.write(final)