from classes.GasolineraGM import GasolineraGM

class Ruta:
    def __init__(self,ciudad_partida,ciudad_destino,gasolineras=None):
        self.ciudad_partida = ciudad_partida
        self.ciudad_destino = ciudad_destino
        self.gasolineras = gasolineras
        
    def getRuta(self):
        gasolineras = GasolineraGM()
        gasolinerasGM = gasolineras.getGasolinerasRuta(self.ciudad_partida,self.ciudad_destino)
        gasolinerasRuta = Ruta(self.ciudad_partida,self.ciudad_destino,gasolinerasGM)
        
        return gasolinerasRuta