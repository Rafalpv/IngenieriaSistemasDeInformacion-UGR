import requests
from bs4 import BeautifulSoup

def listaPrecios(): 
    url = 'https://combustibles.observatorioprecios.com/gasolinera/repsol-avenida-andalucia-s-n.1/'
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    prices_aux = soup.find_all('mark')
    prices = []

    for p in prices_aux:
        prices.append(p.text)

    return prices




