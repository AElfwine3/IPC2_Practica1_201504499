# A class named Plataforma with the following attributes: codigo, nombre.
# The class must have a method called __init__ that receives the values ​​for the attributes.

class Plataforma:
    def __init__(self, codigo: int, nombre: str):
        self.codigo = codigo
        self.nombre = nombre
        self.siguiente = None
    
    def to_dict(self):
        return {k: v for k, v in self.__dict__.items() if k != 'siguiente'}