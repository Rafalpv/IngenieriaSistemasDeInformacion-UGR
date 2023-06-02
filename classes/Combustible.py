from data.dieselGasolina import *

class Combustible:
    def __init__(self, nombre=None, precio_litro_actual=None, precio_litro_pasado=None, precio_litro_maxHistorico=None):
        self.nombre = nombre
        self.precio_litro_actual = precio_litro_actual
        self.precio_litro_pasado = precio_litro_pasado
        self.precio_litro_maxHistorico = precio_litro_maxHistorico
        
    def getDatosCombustibles(self):
        precios = listaPreciosGasolinaSpain()
        nombres = listaNombreCombustibles()

        combustibles = []
        for i in range(len(nombres)):
            nombre = nombres[i]
            precio_litro_actual = precios[i * 3]
            precio_litro_pasado = precios[i * 3 + 1]
            precio_litro_maxHistorico = precios[i * 3 + 2]

            combustible = Combustible(nombre, precio_litro_actual, precio_litro_pasado, precio_litro_maxHistorico)
            combustibles.append(combustible)
        
        return combustibles
    
