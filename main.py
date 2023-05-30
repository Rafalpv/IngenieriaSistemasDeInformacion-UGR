import os 
from flask import Flask, render_template, redirect, url_for, request
from dieselGasolina import obtenerDatosCombustibles, fecha, obtenerDatosEntidades
from preciosAPI import filtrarPorProvincia, filtrarPorCodPostal
from distancias import distanciaEntreCiudades
from ruta import getGasolinras

provincias_espana = [
    '','ALBACETE', 'ALICANTE', 'ALMERÍA','ARABA/ÁLAVA', 'ASTURIAS', 'ÁVILA', 'BADAJOZ', 'BARCELONA',
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
    preciosCombustibles = obtenerDatosCombustibles()
    fechaPrecio = fecha()
    preciosEntidades = obtenerDatosEntidades()
    provincia = request.args.get('provincia')
    codPostal = request.args.get('codPostal')
    
    if(provincia == ''):
        print("CODPOSTAL")
        gasolineras = filtrarPorCodPostal(codPostal)
    else:
        print("PROVINCIA")
        gasolineras = filtrarPorProvincia(provincia)
        
    return render_template('index.html', preciosCombustibles_web=preciosCombustibles, fechaPrecio_web=fechaPrecio, preciosEntidades_web=preciosEntidades,provicinciasEspana_web=provincias_espana,gasolineras_web=gasolineras)
            
@app.route('/buscar_gasolineras', methods=['POST'])
def buscarGasolinerasProvincias():
    provincia = request.form['provincia']
    codPostal = request.form['codPostal']
    
    return redirect(url_for('index',provincia=provincia,codPostal=codPostal))

@app.route('/ciudades.html')
def ciudades():
    mensaje = request.args.get('mensaje')
    gasolineras = request.args.get('gasolineras')
    return render_template('ciudades.html', mensaje_web = mensaje if mensaje is not None else "",gasolineras_web=gasolineras)

@app.route("/procesar_formulario", methods=['POST'])
def formularioCiudades():
    ciudadPartida = request.form.get('ciudad_partida')
    ciudadDestino = request.form.get('ciudad_destino')
    kms = distanciaEntreCiudades(ciudadPartida,ciudadDestino)
    mensaje = "La distancia por Carretera entre " + ciudadPartida + " y " + ciudadDestino + " es de " + kms
    
    gasolineras = getGasolinras(ciudadPartida,ciudadDestino)
    
    return redirect(url_for('ciudades', mensaje=mensaje,gasolineras=gasolineras))
    
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get('PORT', 8080)))