import PyPDF2
import os

merger = PyPDF2.PdfMerger()

lista_documents = os.listdir("Documents")
lista_documents.sort()
print(lista_documents)

for documents in lista_documents:
    if ".pdf" in documents:
        merger.append(f"documents/{documents}")

merger.write("PDF Final.pdf")