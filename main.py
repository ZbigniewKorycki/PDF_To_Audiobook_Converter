import PyPDF2
from gtts import gTTS

file_path = r"C:\Users\zbign_x5x2ftd\OneDrive\Dokumenty\Overcoming_the_Five_Dysfunction.pdf"


reader = PyPDF2.PdfReader(file_path)
page = reader.pages[82]
parts = []


def visitor_body(text, cm, tm, fontDict, fontSize):
        y = tm[5]
        if 0 < y < 590:
            parts.append(text)


page.extract_text(visitor_text=visitor_body)
text_body = "".join(parts)

# def get_text(path_to_file):
#     with open(path_to_file, 'rb') as pdfFileObject:
#         reader = PyPDF2.PdfReader(pdfFileObject)
#         book_length = len(reader.pages)
#
#         # extracting text from all pages
#         book_text = []
#         for page_nr in range(30, 31):
#             page = reader.pages[page_nr]
#             text_page = page.extract_text()
#             book_text.append(text_page)
#         book_text_combined = "".join(book_text)
#         return book_text_combined


def correct_words(text):
    corrected_text = (text_body.replace("\n", " ").
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
    print(corrected_text)
    return corrected_text


language = 'en'
my_mp3 = gTTS(text=correct_words(text_body), lang=language, slow=False)

my_mp3.save("audiobook_2-compare.mp3")
