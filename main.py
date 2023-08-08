import PyPDF2

file_path = r"C:\Users\zbign_x5x2ftd\OneDrive\Dokumenty\Overcoming_the_Five_Dysfunction.pdf"

with open(file_path, 'rb') as pdfFileObject:
    pdfReader = PyPDF2.PdfReader(pdfFileObject)
    pageObj = pdfReader.pages[0ą]
    print(pageObj.extract_text())
