import xml.etree.ElementTree as ET

def escribir_xml(lista_plataformas, lista_juegos):

    root = ET.Element("JuegosViejos")

    listado_plataformas = ET.SubElement(root, "ListaPlataformas")

    for plataforma in lista_plataformas:
        hijo_plat = ET.SubElement(listado_plataformas, "Plataforma")
        ET.SubElement(hijo_plat, "codigo").text = str(plataforma['codigo'])
        ET.SubElement(hijo_plat, "nombre").text = plataforma['nombre']
    
    listado_juegos = ET.SubElement(root, "ListadoJuegos")
    for juego in lista_juegos:
        hijo_juegos = ET.SubElement(listado_juegos, "Juego")
        ET.SubElement(hijo_juegos, "codigo").text = str(juego['codigo'])
        ET.SubElement(hijo_juegos, "nombre").text = juego['nombre']
        platas = ET.SubElement(hijo_juegos, "Plataformas")
        for plataforma in juego['plataformas']:
            plata = ET.SubElement(platas, "Plataforma")
            ET.SubElement(plata, "codigo").text = plataforma

    tree = ET.ElementTree(root)
    tree.write("Salida.xml")
