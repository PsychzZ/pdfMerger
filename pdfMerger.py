import os
import PyPDF2

pdfMerger = PyPDF2.PdfFileMerger()

for pdf in os.listdir(os.curdir):
    if pdf.endswith('.pdf'):
        pdfMerger.append(pdf)
pdfMerger.write('merged.pdf')