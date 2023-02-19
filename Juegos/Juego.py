class Juego:
    def __init__(self, codigo: int, nombre: str, plataformas: list):
        self.codigo = codigo
        self.nombre = nombre
        self.plataformas = plataformas
        self.siguiente = None
    
    def to_dict(self):
        return {k: v for k, v in self.__dict__.items() if k != 'siguiente'}