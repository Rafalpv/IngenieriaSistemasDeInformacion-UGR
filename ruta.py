import requests
from geopy.geocoders import Nominatim

def obtener_ruta(origin, destination, api_key):
    api_key = "AIzaSyAK1BA-W17qGtv78Y8UsjFkfPqcC3TUHvc"  # Tu API key de Google Maps
    # Construye la URL de la solicitud
    url = f"https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&key={api_key}"

    # Realiza la solicitud HTTP
    response = requests.get(url)

    # Comprueba el código de estado de la respuesta
    if response.status_code == 200:
        # La solicitud se realizó con éxito
        data = response.json()

        # Verifica si se encontró una ruta válida
        if data["status"] == "OK":
            # Obtiene los pasos de la ruta
            steps = data["routes"][0]["legs"][0]["steps"]

            # Conjunto para almacenar gasolineras únicas encontradas
            gasolineras_encontradas = set()

            # Procesa cada paso de la ruta
            for i, step in enumerate(steps, 1):
                # Obtiene las coordenadas geográficas del paso
                start_location = step["start_location"]
                coordenadas = f"{start_location['lat']},{start_location['lng']}"

                # Buscar gasolineras en las coordenadas del paso
                buscar_gasolineras(coordenadas, api_key, gasolineras_encontradas)

            # Devolver las gasolineras encontradas
            return gasolineras_encontradas
        else:
            print("No se encontró una ruta válida.")
    else:
        # Ocurrió un error al realizar la solicitud
        print("Error en la solicitud:", response.status_code)


def buscar_gasolineras(coordenadas, api_key, gasolineras_encontradas):
    # Construye la URL de la solicitud de búsqueda
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={coordenadas}&radius=10000&type=gas_station&key={api_key}"

    # Realiza la solicitud HTTP
    response = requests.get(url)

    # Comprueba el código de estado de la respuesta
    if response.status_code == 200:
        # La solicitud se realizó con éxito
        data = response.json()

        # Procesa los resultados de búsqueda de gasolineras
        if data["status"] == "OK":
            # Itera sobre los resultados
            for result in data["results"]:
                nombre = result["name"]
                direccion = result["vicinity"]
                location = result['geometry']['location']

                # Convierte la ubicación en una tupla de coordenadas
                coordenadas_tupla = (location['lat'], location['lng'], nombre, direccion)

                # Verifica si la gasolinera ya se encontró anteriormente
                if coordenadas_tupla not in gasolineras_encontradas:
                    gasolineras_encontradas.add(coordenadas_tupla)
    else:
        # Ocurrió un error al realizar la solicitud
        print("Error en la solicitud:", response.status_code)

def getGasolinras(origen,destino):
    
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
    
    gasolineras_encontrada = obtener_ruta(cords_origen,coords_destino,api_key)
    
    return gasolineras_encontrada