import os 
from flask import Flask, render_template, redirect, url_for, request
from diseslGasolina import listaPreciosGasolinaSpain, listaNombreCombustibles, fecha, preciosPorMarca, imagenesGasolineras
from preciosAPI import filtrarPorProvincia
from distancias import distanciaEntreCiudades

provincias_espana = [
    'ÁLAVA', 'ALBACETE', 'ALICANTE', 'ALMERÍA', 'ASTURIAS', 'ÁVILA', 'BADAJOZ', 'BARCELONA',
    'BURGOS', 'CÁCERES', 'CÁDIZ', 'CANTABRIA', 'CASTELLÓN', 'CIUDAD REAL', 'CÓRDOBA', 'CUENCA',
    'GERONA', 'GRANADA', 'GUADALAJARA', 'GUIPÚZCOA', 'HUELVA', 'HUESCA', 'ISLAS BALEARES', 'JAÉN',
    'LA CORUÑA', 'LA RIOJA', 'LAS PALMAS', 'LEÓN', 'LÉRIDA', 'LUGO', 'MADRID', 'MÁLAGA', 'MURCIA',
    'NAVARRA', 'ORENSE', 'PALENCIA', 'PONTEVEDRA', 'SALAMANCA', 'SANTA CRUZ DE TENERIFE', 'SEGOVIA',
    'SEVILLA', 'SORIA', 'TARRAGONA', 'TERUEL', 'TOLEDO', 'VALENCIA', 'VALLADOLID', 'VIZCAYA',
    'ZAMORA', 'ZARAGOZA'
]

app = Flask(__name__)

@app.route("/")
def hello_world():
    return redirect(url_for("index"))


@app.route('/index.html')
def index():
    preciosSpain = listaPreciosGasolinaSpain()
    nombresCombustibles = listaNombreCombustibles()
    fechaPrecio = fecha()
    listaPreciosPorMarca = preciosPorMarca()
    imagenes = imagenesGasolineras()
    return render_template('index.html', preciosSpain_web=preciosSpain, nombresCombustibles_web=nombresCombustibles, fechaPrecio_web=fechaPrecio, preciosPorMarca_web=listaPreciosPorMarca,imagenes_web=imagenes,provicinciasEspana_web=provincias_espana)

@app.route('/ciudades.html')
def ciudades():
    mensaje = request.args.get('mensaje')
    return render_template('ciudades.html', mensaje_web = mensaje if mensaje is not None else "")

        
        
@app.route("/procesar_formulario", methods=['POST'])
def formularioCiudades():
    ciudadPartida = request.form.get('ciudad_partida')
    ciudadDestino = request.form.get('ciudad_destino')
    
    kms = distanciaEntreCiudades(ciudadPartida,ciudadDestino)
    mensaje = "La distancia por Carretera entre " + ciudadPartida + " y " + ciudadDestino + " es de " + kms
    return redirect(url_for('ciudades', mensaje=mensaje))
        
@app.route('/buscar_gasolineras', methods=['POST'])
def buscarGasolinerasProvincias():
    provincia = request.form['provincia']
    gasolinerasProvincia = filtrarPorProvincia(provincia)
    return redirect(url_for('index',gasolinerasProvincia_web=gasolinerasProvincia))

    
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get('PORT', 8080)))