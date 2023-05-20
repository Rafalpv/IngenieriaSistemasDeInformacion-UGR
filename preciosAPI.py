import requests

url = 'https://sedeaplicaciones.minetur.gob.es/ServiciosRESTCarburantes/PreciosCarburantes/EstacionesTerrestres/'
response = requests.get(url)
response_json = response.json()

def filter_func(element, provincia):
    return element['Provincia'] == provincia

def filtrarPorProvincia(provincia):
    filtered_data = filter(lambda x: filter_func(x, provincia), response_json['ListaEESSPrecio'])
    filtered_list = [
    {
        element['Provincia'],
        element['Precio Gasolina 95 E5'],
        element['Rótulo']
    }
    for element in filtered_data
]
    
    return filtered_list