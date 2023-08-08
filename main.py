import PyPDF2

file_path = r"C:\Users\zbign_x5x2ftd\OneDrive\Dokumenty\Overcoming_the_Five_Dysfunction.pdf"

with open(file_path, 'rb') as pdfFileObject:
    pdfReader = PyPDF2.PdfReader(pdfFileObject)
    page_len = len(pdfReader.pages)

    #extracting text from all pages
    for page_nr in range(15, page_len):
        page = pdfReader.pages[page_nr]
        print(page.extract_text())
