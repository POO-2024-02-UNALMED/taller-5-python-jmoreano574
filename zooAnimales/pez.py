from .animal import Animal

class Pez(Animal):
    _listado = []
    salmones = 0
    bacalaos = 0
    def __init__(self, nombre = None, edad = None, habitat = None, genero = None, color = None, cantidad = None, zona = None):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._colorEscamas = color
        self._cantidadAletas = cantidad
        self._zona = zona
        Pez._listado.append(self)
        super()
    
    def setColorEscamas(self, color):
        self._colorEscamas = color
    def setCantidadAletas(self, aletas):
        self._cantidadAletas = aletas

    def getColorEscamas(self):
        return self._colorEscamas
    def getCantidadAletas(self):
        return self._cantidadAletas
    
    @classmethod
    def cantidadPeces(cls):
        return len(cls._listado)
    
    def movimiento(self):
        return "nadar"
    
    def crearSalmon(nombre, edad, genero):
        laferte = Pez(nombre, edad, "oceano", genero, "rojo", 6)
        Pez.salmones += 1
        return laferte
    def crearBacalao(nombre, edad, genero):
        sheng = Pez(nombre, edad, "oceano", genero, "gris", 6)
        Pez.bacalaos += 1
        return sheng
    
    