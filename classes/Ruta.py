from classes.GasolineraGM import GasolineraGM
from data.distancias import * 

class Ruta:
    def __init__(self,ciudad_partida=None,ciudad_destino=None,gasolineras=None):
        self.ciudad_partida = ciudad_partida
        self.ciudad_destino = ciudad_destino
        self.gasolineras = gasolineras
        
    def getRuta(self):
        gasolineras = GasolineraGM()
        gasolinerasGM = gasolineras.getGasolinerasRuta(self.ciudad_partida,self.ciudad_destino)
        gasolinerasRuta = Ruta(self.ciudad_partida,self.ciudad_destino,gasolinerasGM)
        
        return gasolinerasRuta
    
    def getDistanciaEntreCiudades(self):
        return distanciaEntreCiudades(self.ciudad_partida,self.ciudad_destino)
    
    def getTiempoEntreCiudades(self):
        return tiempoEntreCiudades(self.ciudad_partida,self.ciudad_destino)
    
    def informacionRuta(self):
        distancia = self.getDistanciaEntreCiudades() 
        tiempo = self.getTiempoEntreCiudades()
        if(distancia != None and tiempo != None):
            return "La Distancia entre " + self.ciudad_partida + " y " + self.ciudad_destino + " es de " + str(distancia) + ". El Tiempo estimado en carretera es de " + str(tiempo)
        else:
            return ""