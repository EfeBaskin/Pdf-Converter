from pdf2docx import Converter

pdf_path = 'samplePdf.pdf'
docx_path = 'samplePdf.docx'

cv = Converter(pdf_file=pdf_path)
cv.convert(docx_filename=docx_path)
cv.close()

