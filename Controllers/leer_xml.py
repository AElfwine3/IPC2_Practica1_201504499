from sys import path
from os import getcwd
import xml.etree.ElementTree as ET

path.append(getcwd()+'\\Juegos')
path.append(getcwd()+'\\Use-cases')

import ListaPlataformas
import Plataforma
import ListaJuegos
import Juego

lista_plataformas = ListaPlataformas.Lista_plataformas()
lista_juegos = ListaJuegos.Lista_juegos()

def parse_xml(file_path):
    print("")
    tree = ET.parse(file_path)
    root = tree.getroot()
    print(root.tag)
    if root.tag == "JuegosViejos":
        for listado in root:
            print(listado.tag)
            for objeto in listado:
                print('\t', objeto.tag)
                codigo = 0
                nombre = ""
                platas = []
                for atributo in objeto:
                    print('\t\t', atributo.tag, atributo.text)
                    if listado.tag == "ListaPlataformas":
                        if atributo.tag == "codigo":
                            codigo = int(atributo.text)
                        if atributo.tag == "nombre":
                            nombre = atributo.text
                        if codigo != 0 and nombre != "":
                            plataforma = Plataforma.Plataforma(codigo, nombre)
                            lista_plataformas.agregar(plataforma)
                    if listado.tag == "ListadoJuegos":
                        if atributo.tag == "codigo":
                            codigo = int(atributo.text)
                        if atributo.tag == "nombre":
                            nombre = atributo.text
                        if atributo.tag == "Plataformas":
                            for referencia in atributo:
                                for atributos in referencia:
                                    platas.append(atributos.text)
                                    print('\t\t\t', atributos.tag, atributos.text)
                        if codigo != 0 and nombre != "" and platas != []:
                            juego = Juego.Juego(codigo, nombre, platas)
                            lista_juegos.agregar(juego)
            print("")
        lista_plataformas.ordenar()
        lista_juegos.ordenar()
        return lista_plataformas, lista_juegos
    else:
        print("Hay un problema con el documento.")
