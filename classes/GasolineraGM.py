from geopy.geocoders import Nominatim
from data.ruta import obtener_ruta

class GasolineraGM:
    def __init__(self,nombre=None,direccion=None,horario=None,rating=None):
        self.nombre = nombre
        self.direccion = direccion
        self.horario = horario
        self.rating = rating
        
    def getGasolinerasRuta(self,origen, destino):

        api_key = "AIzaSyAK1BA-W17qGtv78Y8UsjFkfPqcC3TUHvc"  # Tu API key de Google Maps

        geolocator = Nominatim(user_agent="my-app")
        city1 = origen
        location1 = geolocator.geocode(city1)
        latitude1, longitude1 = location1.latitude, location1.longitude
        cords_origen = str(latitude1)+","+str(longitude1)

        city2 = destino
        location2 = geolocator.geocode(city2)
        latitude2, longitude2 = location2.latitude, location2.longitude
        coords_destino = str(latitude2)+","+str(longitude2)

        gasolineras_encontradas = obtener_ruta(cords_origen, coords_destino, api_key)
        
        gasolinerasGM = []
        for gasolinera in gasolineras_encontradas:
            nombre, direccion, opening_hours, rating = gasolinera
            gasolinerasGM.append(GasolineraGM(nombre, direccion, opening_hours, rating))

        return gasolinerasGM
    
