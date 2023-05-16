import requests
from bs4 import BeautifulSoup4

def listaPrecios(): 
    url = 'https://combustibles.observatorioprecios.com/gasolinera/repsol-avenida-andalucia-s-n.1/'
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup4(content, 'html.parser')
    prices = soup.find_all('mark')

    return prices