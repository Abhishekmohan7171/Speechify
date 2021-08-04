import pyttsx3
import PyPDF2
book = open("trial.pdf", 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)

# for a certain page
# speaker = pyttsx3.init()
# page = pdfReader.getPage(1)
# text = page.extractText()
# speaker.say(text)
# speaker.runAndWait()

#for a range of pages
speaker = pyttsx3.init()
for num in range(7, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()