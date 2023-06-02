from data.dieselGasolina import *
from classes.Combustible import Combustible

class Entidad:
    def __init__(self, combustibles=None, imagen_link=None):
        self.combustibles = combustibles
        self.imagen_link = imagen_link
    
    def obtenerDatosEntidades(self):
        precios = preciosPorEntidad()
        imagenes = imagenesGasolineras()
        
        entidades = []
        
        for i in range(len(imagenes)):
            combustibles = []
            imagen = imagenes[i]
            for j in range(5):
                nombre = precios[j*9]
                precio = precios[(j*9)+1+i]
                combustible = Combustible(nombre,precio,"","")
                combustibles.append(combustible)
                
            entidad = Entidad(combustibles,imagen)
            entidades.append(entidad)
    
        return entidades