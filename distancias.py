import requests
from bs4 import BeautifulSoup

URL = 'https://www.distanciasentreciudades.com/distancia-'

def distanciaEntreCiudades(origen, destino):
    try:
        nuevaURL = getNuevaURL(origen, destino)
        response = requests.get(nuevaURL)
        soup = BeautifulSoup(response.text, 'html.parser')

        kmsCarretera = soup.find('strong', class_='kmsruta').text
        return str(kmsCarretera)
    except AttributeError:
        return "No se pudo obtener la distancia entre las ciudades"

def getNuevaURL(origen,destino):
    nuevoOrigen = convertir_string(origen)
    nuevoDestino = convertir_string(destino)
    nuevaURL = URL + nuevoOrigen + "-a-" + nuevoDestino
    return nuevaURL
    
def convertir_string(texto):
    texto = texto.lower()
    texto = texto.replace(" ", "-")
    texto = texto.replace("ñ", "n")
    return texto
