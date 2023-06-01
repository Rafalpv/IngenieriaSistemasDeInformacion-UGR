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
        tipos_combustible.append(tipo_combustible)
    
    return tipos_combustible

def fecha():
    url = 'https://www.dieselogasolina.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    div_tabla = soup.find('div',class_='tabla_resumen_precios')
    p_element = div_tabla.find_next('p')
    fecha = p_element.get_text()
    
    return fecha


def preciosPorEntidad():
    url = 'https://www.dieselogasolina.com/'    
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    div = soup.find("div", class_="por_marcas")
    tbody = div.find("tbody")
    tds = tbody.find_all("td")
    
    precios = []
    for td in tds:
        precio = td.text.strip()
        precios.append(precio)
        
    return precios

def imagenesGasolineras():
    url = 'https://www.dieselogasolina.com/'    
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    div = soup.find("div", class_="por_marcas")
    imagenes = div.find_all("img")

    enlaces = []
    for imagen in imagenes:
        enlace = imagen["src"]
        enlaces.append(enlace)

    return enlaces


    