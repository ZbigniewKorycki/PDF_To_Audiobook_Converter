import PyPDF2
from gtts import gTTS

file_path = r"C:\Users\zbign_x5x2ftd\OneDrive\Dokumenty\Overcoming_the_Five_Dysfunction.pdf"


reader = PyPDF2.PdfReader(file_path)
book_parts = []


def visitor_body(text, cm, tm, fontDict, fontSize):
    y = tm[5]
    if 0 < y < 590:
        book_parts.append(text)


def correct_words(text):
    corrected_text = (text.replace("\n", " ").
                      replace("  ", " ").
                      replace(" , ", ", ").
                      replace(" ’s", "’s").
                      replace(" ’ve", "’ve").
                      replace(" ’m", "’m").
                      replace(" ’t", "’t").
                      replace(" ’re", "’re").
                      replace("- ", "-").
                      replace(" ’s", "’s").
                      replace(" ’ll", "’ll").
                      replace(" ’d", "’d")
                      )
    return corrected_text


for page in range(0, len(reader.pages)):
    page_nr = reader.pages[page]
    text_page = page_nr.extract_text(visitor_text=visitor_body)
book_text_combined = "".join(book_parts)


language = 'en'
my_mp3 = gTTS(text=correct_words(book_text_combined), lang=language, slow=False)

my_mp3.save("audiobook.mp3")
