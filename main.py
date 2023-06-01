import os
from flask import Flask, render_template, redirect, url_for, request
from dieselGasolina import fecha
from distancias import distanciaEntreCiudades

from classes.Combustible import Combustible
from classes.Gasolinera import Gasolinera
from classes.Entidad import Entidad
from classes.Ruta import Ruta

provincias_espana = [
    '', 'ALBACETE', 'ALICANTE', 'ALMERÍA', 'ARABA/ÁLAVA', 'ASTURIAS', 'ÁVILA', 'BADAJOZ', 'BARCELONA',
    'BURGOS', 'CÁCERES', 'CÁDIZ', 'CANTABRIA', 'CASTELLÓN / CASTELLÓ', 'CEUTA', 'CIUDAD REAL', 'CÓRDOBA', 'CUENCA',
    'GIRONA', 'GRANADA', 'GUADALAJARA', 'GIPUZKOA', 'HUELVA', 'HUESCA', 'ISLAS BALEARES', 'JAÉN',
    'CORUÑA (A)', 'RIOJA (LA)', 'PALMAS (LAS)', 'LEÓN', 'LLEIDA', 'LUGO', 'MADRID', 'MÁLAGA', 'MELILLA', 'MURCIA',
    'NAVARRA', 'ORENSE', 'PALENCIA', 'PONTEVEDRA', 'SALAMANCA', 'SANTA CRUZ DE TENERIFE', 'SEGOVIA',
    'SEVILLA', 'SORIA', 'TARRAGONA', 'TERUEL', 'TOLEDO', 'VALENCIA / VALÈNCIA', 'VALLADOLID', 'VIZCAYA',
    'ZAMORA', 'ZARAGOZA'
]

app = Flask(__name__)

@app.route("/")
def hello_world():
    return redirect(url_for("index"))


@app.route('/index.html')
def index():
    
    combustiblesEspaña = Combustible()
    entidades = Entidad()
    preciosCombustiblesEspaña = combustiblesEspaña.getDatosCombustibles()
    
    fechaPrecio = fecha()
    preciosEntidades = entidades.obtenerDatosEntidades()
    
    provincia = request.args.get('provincia')
    codPostal = request.args.get('codPostal')

    gasolinerasFiltrada = Gasolinera()    

    if (provincia == ''):
        gasolineras = gasolinerasFiltrada.getGasolinerasCodPostal(codPostal)
    else:
        gasolineras = gasolinerasFiltrada.getGasolinerasProvincia(provincia)

    return render_template('index.html', preciosCombustibles_web=preciosCombustiblesEspaña, fechaPrecio_web=fechaPrecio, preciosEntidades_web=preciosEntidades, provicinciasEspana_web=provincias_espana, gasolineras_web=gasolineras)


@app.route('/buscar_gasolineras', methods=['POST'])
def buscarGasolinerasProvincias():
    provincia = request.form['provincia']
    codPostal = request.form['codPostal']

    return redirect(url_for('index', provincia=provincia, codPostal=codPostal))


@app.route('/ciudades.html')
def ciudades():  
    mensaje = request.args.get('mensaje')
    ciudadPartida = request.args.get('ciudadPartida')
    ciudadDestino = request.args.get('ciudadDestino')
    
    if(mensaje == 'No se pudo obtener la distancia entre las ciudades'):
        ruta = Ruta()
        rutaCiudades = ruta.getRuta()
    else:
        ruta = Ruta(ciudadPartida,ciudadDestino)
        rutaCiudades = ruta.getRuta()
    
    return render_template('ciudades.html', mensaje_web=mensaje if mensaje is not None else "", rutaCiudades_web=rutaCiudades)


@app.route("/procesar_formulario", methods=['POST'])
def formularioCiudades():
    ciudadPartida = request.form.get('ciudad_partida')
    ciudadDestino = request.form.get('ciudad_destino')
    
    kms = distanciaEntreCiudades(ciudadPartida, ciudadDestino)
    if (kms == 'No se pudo obtener la distancia entre las ciudades'):
        mensaje = kms
    else:
        mensaje = "La distancia por Carretera entre " + \
            ciudadPartida + " y " + ciudadDestino + " es de " + kms


    return redirect(url_for('ciudades', ciudadPartida=ciudadPartida, ciudadDestino=ciudadDestino, mensaje=mensaje,))


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get('PORT', 8080)))
