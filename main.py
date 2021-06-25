import pyttsx3
import pdfplumber
import PyPDF2
file = "Brave Man-converted.pdf"
pdf_file = open(file, 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_file)
pages = pdf_reader.numPages
with pdfplumber.open(file) as pdf:
    speaker = pyttsx3.init()
    for n in range(pages):
        page = pdf.pages[n]
        text = page.extract_text()
        print(text)
        # voices = speaker.getProperty('voices')
        # voice = voices[1]
        # speaker.setProperty('voice', voice.id)

        speaker.say(text)
        speaker.runAndWait()

