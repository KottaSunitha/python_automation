import PyPDF2
import pyttsx3

"""A Pure-Python library built as a PDF toolkit used to 
extracting document information,splitting documents page by page,
merging documents,cropping pages"""

story_book = open(r"C:\Users\sk21163\Downloads\short-stories-for-children.pdf",'rb')
pdf_reader = PyPDF2.PdfFileReader(story_book)
pages = pdf_reader.numPages
print("success")
speaker = pyttsx3.init()
page = pdf_reader.getPage(5)
text = page.extractText()
print(text)
speaker.say(text)
speaker.runAndWait()
