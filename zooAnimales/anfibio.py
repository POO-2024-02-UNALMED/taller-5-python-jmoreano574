from .animal import Animal

class Anfibio(Animal):
    _listado = []
    ranas = 0
    salamandras = 0
    def __init__(self, nombre = None, edad = None, habitat = None, genero = None, color = None, veneno = None, zona = None):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._colorPiel = color
        self._venenoso = veneno
        self._zona = zona
        Anfibio._listado.append(self)
        super()
    
    def setColorPiel(self, color):
        self._colorPiel = color
    def setVenenoso(self, veneno):
        self._venenoso = veneno

    def getColorPiel(self):
        return self._colorPiel
    def isVenenoso(self):
        return self._venenoso
    
    @classmethod
    def cantidadAnfibios(cls):
        return len(cls._listado)
    
    def movimiento(self):
        return "saltar"
    
    def crearRana(nombre, edad, genero):
        rene = Anfibio(nombre, edad, "selva", genero, "rojo", True)
        Anfibio.ranas += 1
        return rene
    def crearSalamandra(nombre, edad, genero):
        chorizard = Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)
        Anfibio.salamandras += 1
        return chorizard
    
    