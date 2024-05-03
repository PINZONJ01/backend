import pyttsx3  # Importa la biblioteca pyttsx3 para la conversión de texto a voz.
import PyPDF2  # Importa la biblioteca PyPDF2 para manipular archivos PDF.
from tkinter.filedialog import *  # Importa todo desde tkinter.filedialog para usar cuadros de diálogo de archivos.

libro = askopenfilename()  # Abre un cuadro de diálogo para que el usuario seleccione un archivo PDF y guarda la ruta del archivo seleccionado.

pdf = PyPDF2.PdfReader(libro)  # Abre el archivo PDF seleccionado por el usuario para su lectura.
pages = len(pdf.pages)  # Obtiene el número total de páginas en el archivo PDF.

for num in range(0, pages):  # Itera sobre cada página del archivo PDF.
    page = pdf.pages[num]  # Obtiene la página actual en la iteración.
    text = page.extract_text()  # Extrae el texto de la página actual.
    player = pyttsx3.init()  # Inicializa el motor de texto a voz.
    player.say(text)  # Agrega el texto extraído a la cola de mensajes a ser leídos en voz alta.
    player.runAndWait()  # Procesa la cola de mensajes, leyendo el texto en voz alta, y espera hasta que la lectura termine antes de continuar.
