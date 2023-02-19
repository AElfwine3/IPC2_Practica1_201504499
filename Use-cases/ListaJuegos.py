from sys import path
from os import getcwd

path.append(getcwd()+'\\Juegos')
import Juego

class Lista_juegos:
    def __init__(self):
        self.cabeza = None
    
    def agregar(self, nuevo_juego: Juego.Juego):
        if self.cabeza is None:
            self.cabeza = nuevo_juego
        else:
            nodo_actual = self.cabeza
            while nodo_actual.siguiente is not None:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_juego
     
    def ordenar(self):
        if self.cabeza is None:
            return
        nodo_actual = self.cabeza
        while nodo_actual.siguiente is not None:
            nodo_siguiente = nodo_actual.siguiente
            while nodo_siguiente is not None:
                if nodo_actual.codigo > nodo_siguiente.codigo:
                    aux_codigo = nodo_actual.codigo
                    aux_nombre = nodo_actual.nombre
                    aux_plataformas = nodo_actual.plataformas
                    nodo_actual.codigo = nodo_siguiente.codigo
                    nodo_actual.nombre = nodo_siguiente.nombre
                    nodo_actual.plataformas = nodo_siguiente.plataformas
                    nodo_siguiente.codigo = aux_codigo
                    nodo_siguiente.nombre = aux_nombre
                    nodo_siguiente.plataformas = aux_plataformas
                nodo_siguiente = nodo_siguiente.siguiente
            nodo_actual = nodo_actual.siguiente

    def recorrer(self, indice: int):
        nodo_actual = self.cabeza
        contador = 0
        while nodo_actual is not None:
            if contador == indice:
                return nodo_actual
            contador += 1
            nodo_actual = nodo_actual.siguiente
        return None

    def tamano(self):
        contador = 0
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            contador += 1
            nodo_actual = nodo_actual.siguiente
        return contador
    
    def mostrar(self):
        nodo_actual = self.cabeza
        lista = []
        while nodo_actual is not None:
            lista.append(nodo_actual.to_dict())
            nodo_actual = nodo_actual.siguiente
        return lista