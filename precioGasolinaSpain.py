import requests
from bs4 import BeautifulSoup

def listaPreciosGasolinaSpain(): 
    url = 'https://www.dieselogasolina.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    td_elements = soup.find_all('td', class_='font-dsdigital')
    precios = []
    for td in td_elements:
        precio = td.strong.text.strip()
        precios.append(precio)

    return precios

def listaNombreCombustibles():
    url = 'https://www.dieselogasolina.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    tipos_combustible = []
    combustibles = soup.find_all('a', title='Ver gasolineras')
    
    for c in combustibles:
        tipo_combustible = c.text.strip()
        print(tipo_combustible)
        tipos_combustible.append(tipo_combustible)
    
    return tipos_combustible

