import PyPDF2
from gtts import gTTS

file_path = r"C:\Users\zbign_x5x2ftd\OneDrive\Dokumenty\Overcoming_the_Five_Dysfunction.pdf"


def get_text(path_to_file):
    with open(path_to_file, 'rb') as pdfFileObject:
        reader = PyPDF2.PdfReader(pdfFileObject)
        book_length = len(reader.pages)

        # extracting text from all pages
        book_text = []
        for page_nr in range(0, book_length):
            page = reader.pages[page_nr]
            text_page = page.extract_text()
            book_text.append(text_page)
        book_text_combined = " ".join(map(str, book_text))
        return book_text_combined


language = 'en'
my_mp3 = gTTS(text=get_text(file_path), lang=language, slow=False)

my_mp3.save("audiobook_1.mp3")

# os.system("mpg321 trial.mp3")