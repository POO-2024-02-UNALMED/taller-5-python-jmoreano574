class Zona:
    def __init__(self, nombre = None, zoo = None):
        self._nombre = nombre
        self._zoo = [zoo]
        self._animales = []
    
    def setNombre(self, nombre):
        self._nombre = nombre
    def setZoo(self, zoo):
        if self._zoo[0] == None:
            self._zoo[0] = zoo

    def getNombre(self):
        return self._nombre
    def getZoo(self):
        return self._zoo[0]
    def getAnimales(self):
        return self._animales
    
    def agregarAnimales(self, animal):
        self._animales.append(animal)
    
    def cantidadAnimales(self):
        return len(self._animales)
    
    def __str__(self):
        return self._nombre