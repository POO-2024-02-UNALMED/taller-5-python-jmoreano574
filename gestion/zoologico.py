class Zoologico:  
    def __init__(self, nombre = None, ubicacion = None):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = []
    
    def setNombre(self, nombre):
        self._nombre = nombre
    def setUbicacion(self, ub):
        self._ubicacion = ub
    
    def getNombre(self):
        return self._nombre
    def getUbicacion(self):
        return self._ubicacion
    def getZona(self):
        return self._zonas

    def cantidadTotalAnimales(self):
        total = 0
        for zona in self._zonas:
            x = len(zona._animales)
            total += x
        return total
    
    def agregarZonas(self, zona):
        self._zonas.append(zona)
        zona.setZoo(self)

    def __str__(self):
        return self._nombre