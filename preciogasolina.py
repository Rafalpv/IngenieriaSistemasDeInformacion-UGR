import requests
from bs4 import BeautifulSoup

def listaPrecios(): 
    url = 'https://combustibles.observatorioprecios.com/gasolinera/repsol-avenida-andalucia-s-n.1/'
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    prices = soup.find_all('mark')

    return prices