import pyttsx3
import PyPDF2
from tkinter.filedialog import *

libro = askopenfilename()

pdf = PyPDF2.PdfReader(libro)  # Cambiado de PdfFileReader a PdfReader
pages = len(pdf.pages)  # Corregido de pdf.numPages a len(pdf.pages)

for num in range(0, pages):
    page = pdf.pages[num]  # Actualizado para usar pdf.pages[num]
    text = page.extract_text()  # Actualizado a extract_text() según la nueva API
    player = pyttsx3.init()
    player.say(text)
    player.runAndWait()
