import tkinter as tk
from tkinter import filedialog
from sys import path
from os import getcwd

path.append(getcwd()+'\\Controllers')
import leer_xml, escribir_xml

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    if not file_path.endswith(".xml"):
        print("Elija un archivo valido!")
    else:
        lista_plataformas, lista_juegos = leer_xml.parse_xml(file_path)
        escribir_xml.escribir_xml(lista_plataformas, lista_juegos)