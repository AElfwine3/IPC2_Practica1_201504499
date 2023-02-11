# a class named Juego with attributes named: codigo, nombre, plataformas
# the class must have a method named: __init__ that receives the values ​​for the attributes

class Juego:
    def __init__(self, codigo: int, nombre: str, plataformas: list):
        self.codigo = codigo
        self.nombre = nombre
        self.plataformas = plataformas
        self.siguiente = None
    
    # method that returns the object itself as a dictionary
    def to_dict(self):
        return {k: v for k, v in self.__dict__.items() if k != 'siguiente'}