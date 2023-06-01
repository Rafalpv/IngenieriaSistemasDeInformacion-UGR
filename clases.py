from preciosAPI import *

class Combustible:
    def __init__(self, nombre, precio_litro_actual, precio_litro_pasado, precio_litro_maxHistorico):
        self.nombre = nombre
        self.precio_litro_actual = precio_litro_actual
        self.precio_litro_pasado = precio_litro_pasado
        self.precio_litro_maxHistorico = precio_litro_maxHistorico
        
class Entidad:
    def __init__(self, combustibles, imagen_link):
        self.combustibles = combustibles
        self.imagen_link = imagen_link
    
class Gasolinera:
    def __init__(self, nombre=None, municipio=None, provincia=None, ubicacion=None, cod_postal=None, combustibles=None):
        self.nombre = nombre
        self.municipio = municipio
        self.provincia = provincia
        self.cod_postal = cod_postal
        self.ubicacion = ubicacion
        self.combustibles = combustibles
        
    def getGasolinerasCodPostal(self,codPostal):
        gasolinerasJSON = filtrarPorCodPostal(codPostal)
        gasolinerasCodPostal = []
        
        for g in gasolinerasJSON:
            combustibles = []
            combustible1 = Combustible("Gasolina 95",g['Precio Gasolina 95 E5'],"","")
            combustible2 = Combustible("Gasolina 98",g['Precio Gasolina 98 E5'],"","")
            combustible3 = Combustible("Gasoleo A", g['Precio Gasoleo A'],"","")
            
            combustibles.append(combustible1)
            combustibles.append(combustible2)
            combustibles.append(combustible3)
            
            gasolinera = Gasolinera(g['Rótulo'],g['Municipio'],g['Provincia'],g['Direccion'],codPostal,combustibles)
            gasolinerasCodPostal.append(gasolinera)   
            
        return gasolinerasCodPostal
    
    def getGasolinerasProvincia(self,provincia):
        gasolinerasJSON = filtrarPorProvincia(provincia)
        gasolinerasProvincia = []
        
        for g in gasolinerasJSON:
            combustibles = []
            combustible1 = Combustible("Gasolina 95",g['Precio Gasolina 95 E5'],"","")
            combustible2 = Combustible("Gasolina 98",g['Precio Gasolina 98 E5'],"","")
            combustible3 = Combustible("Gasoleo A", g['Precio Gasoleo A'],"","")
            
            combustibles.append(combustible1)
            combustibles.append(combustible2)
            combustibles.append(combustible3)
            
            gasolinera = Gasolinera(g['Rótulo'],g['Municipio'],provincia,g['Direccion'],g['codPostal'],combustibles)
            gasolinerasProvincia.append(gasolinera)   
            
        return gasolinerasProvincia
        
        
class Gasolinera_GoogleMaps:
    def __init__(self,nombre,direccion,horario,rating):
        self.nombre = nombre
        self.direccion = direccion
        self.horario = horario
        self.rating = rating
    
class Ruta:
    def __init__(self,ciudad_partida,ciudad_destino,gasolineras):
        self.ciudad_partida = ciudad_partida
        self.ciudad_destino = ciudad_destino
        self.gasolineras = gasolineras