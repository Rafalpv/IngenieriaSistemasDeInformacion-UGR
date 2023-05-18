import requests

url = 'https://sedeaplicaciones.minetur.gob.es/ServiciosRESTCarburantes/PreciosCarburantes/EstacionesTerrestres/'
response = requests.get(url)
response_json = response.json()

def filter_func(element):
    return element['Provincia'] == 'GRANADA'

# Filtrar los elementos utilizando la función de filtro
filtered_data = filter(filter_func, response_json['ListaEESSPrecio'])

# Convertir el iterador a una lista
filtered_list = list(filtered_data)

# Imprimir los elementos filtrados
for element in filtered_list:
    print(element)
