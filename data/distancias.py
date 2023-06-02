import requests
from bs4 import BeautifulSoup

URL = 'https://www.distanciasentreciudades.com/distancia-'

def distanciaEntreCiudades(origen, destino):
    try:
        nuevaURL = getNuevaURL(origen, destino)
        response = requests.get(nuevaURL)
        soup = BeautifulSoup(response.text, 'html.parser')

        kmsCarretera = soup.find('strong', class_='kmsruta').text
        return kmsCarretera
    except AttributeError:
        return None

def tiempoEntreCiudades(origen,destino):
    try:
        nuevaURL = getNuevaURL(origen, destino)
        response = requests.get(nuevaURL)
        soup = BeautifulSoup(response.text, 'html.parser')

        tiempo = soup.find('strong', id='tiempo').text
        return tiempo
    except AttributeError:
        return None

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
