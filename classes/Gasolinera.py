from classes.Combustible import Combustible
from data.preciosAPI import *

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
            combustible4 = Combustible("Gasoleo Premiun",g['Precio Gasoleo Premium'],"","") 
            
            combustibles.append(combustible1)
            combustibles.append(combustible2)
            combustibles.append(combustible3)
            combustibles.append(combustible4)
            
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
            combustible4 = Combustible("Gasoleo Premiun",g['Precio Gasoleo Premium'],"","") 
            
            combustibles.append(combustible1)
            combustibles.append(combustible2)
            combustibles.append(combustible3)
            combustibles.append(combustible4)
            
            gasolinera = Gasolinera(g['Rótulo'],g['Municipio'],provincia,g['Direccion'],g['codPostal'],combustibles)
            gasolinerasProvincia.append(gasolinera)   
            
        return gasolinerasProvincia