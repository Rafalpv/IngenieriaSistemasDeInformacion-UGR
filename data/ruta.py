import requests

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
                buscar_gasolineras(coordenadas, api_key,gasolineras_encontradas)

            # Devolver las gasolineras encontradas
            return gasolineras_encontradas
        else:
            print("No se encontró una ruta válida.")
    else:
        # Ocurrió un error al realizar la solicitud
        print("Error en la solicitud:", response.status_code)


def buscar_gasolineras(coordenadas, api_key, gasolineras_encontradas):
    # Construye la URL de la solicitud de búsqueda
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={coordenadas}&radius=4500&type=gas_station&key={api_key}"

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
                opening_hours = result.get(
                    'opening_hours', {}).get('open_now', None)
                rating = result.get('rating', None)

                gasolineras_encontradas.add((nombre, direccion, opening_hours, rating))
    else:
        # Ocurrió un error al realizar la solicitud
        print("Error en la solicitud:", response.status_code)
