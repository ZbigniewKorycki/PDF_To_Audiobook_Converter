import PyPDF2
from gtts import gTTS
import os

file_path = r"C:\Users\zbign_x5x2ftd\OneDrive\Dokumenty\Overcoming_the_Five_Dysfunction.pdf"

with open(file_path, 'rb') as pdfFileObject:
    pdfReader = PyPDF2.PdfReader(pdfFileObject)
    page_len = len(pdfReader.pages)

    audiobook = []
    #extracting text from all pages
    for page_nr in range(10, 20):
        page = pdfReader.pages[page_nr]
        text_page = page.extract_text()
        audiobook.append(text_page)


text_audiobook = " ".join(map(str, audiobook))
print(text_audiobook)
language = 'en'


my_mp3 = gTTS(text=text_audiobook, lang=language, slow=False)

my_mp3.save("audiobook_1.mp3")

# os.system("mpg321 trial.mp3")