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
        "Rótulo": element['Rótulo'],
        "Municipio": element['Municipio'],
        "Direccion": element['Dirección'],
        "Precio Gasolina 95 E5":  element['Precio Gasolina 95 E5'],
        "Precio Gasolina 98 E5": element['Precio Gasolina 98 E5'],
        "Precio Gasoleo A": element['Precio Gasoleo A']
    }
    for element in filtered_data
]
    
    return filtered_list