from sys import path
from os import getcwd

path.append(getcwd()+'\\Juegos')
import Plataforma

class Lista_plataformas:
    def __init__(self):
        self.cabeza = None
    
    def agregar(self, nueva_plataforma: Plataforma.Plataforma):
        if self.cabeza is None:
            self.cabeza = nueva_plataforma
        else:
            nodo_actual = self.cabeza
            while nodo_actual.siguiente is not None:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nueva_plataforma

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
                    nodo_actual.codigo = nodo_siguiente.codigo
                    nodo_actual.nombre = nodo_siguiente.nombre
                    nodo_siguiente.codigo = aux_codigo
                    nodo_siguiente.nombre = aux_nombre
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