import tkinter as tk # módulo tkinter
import PyPDF2 # Para poder cargar PDFs
from PIL import Image, ImageTk #Para importar imágenes
from tkinter.filedialog import askopenfile
# PARTE 2: https://www.youtube.com/watch?v=y8PR4lTAh5E

root = tk.Tk() # El inicio de la ventana del GUI (todo va entre este y el mainloop)

canvas = tk.Canvas(root, width=800, height=500) # Objeto "Canvas" que le asigna el tamaño a la ventana del GUI
canvas.grid(columnspan=3, rowspan=3) # Divide la ventana en 3 columnas y 3 filas (transparentes)

#Agregarle el logo:
logo = Image.open('Logo.png') # Abre la imagen
logo = ImageTk.PhotoImage(logo) # Convierte la imagen en una imagen de TKinter
logo_label = tk.Label(image=logo) # La pone en un widget de tipo "Label"
logo_label.image = logo # Esta es como para "activar la imagen"
logo_label.grid(column=0, row=0) # La acomoda en una columna y fila de la ventana

#Instrucciones de uso de la GUI:
instructions = tk.Label(root, text="Selecciona un documento para firmar. (Agregarle instrucciones...).", font="Raleway")
instructions.grid(columnspan=1, column=0, row=1)

# Función para abrir un archivo
def open_file():
    browse_text.set("Cargando...") # Cambia el texto del botón mientras busca el archivo
    file = askopenfile(parent=root, mode='rb', title="Elige un archivo", filetypes=[("Pdf file", "*.pdf")]) # Esto limita a que solo se suban PDFs
    if file: # Si sí elige un archivo, ejecuta lo siguiente:
        read_pdf = PyPDF2.PdfFileReader(file) # Lee el archivo PDF

        browse_text.set("Cargar archivo")

#Browse button
browse_text = tk.StringVar() # Le pone texto al botón
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda:open_file(), font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
browse_text.set("Cargar archivo") # Modifica el texto del botón
browse_btn.grid(column=1, row=0)

root.mainloop() # El fin de la ventana del GUI
