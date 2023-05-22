import os 
from flask import Flask, render_template, redirect, url_for, request
from diseslGasolina import listaPreciosGasolinaSpain, listaNombreCombustibles, fecha, preciosPorMarca, imagenesGasolineras
from preciosAPI import filtrarPorProvincia
from distancias import distanciaEntreCiudades
from mapa import getMapa

provincias_espana = [
    'ALBACETE', 'ALICANTE', 'ALMERÍA','ARABA/ÁLAVA', 'ASTURIAS', 'ÁVILA', 'BADAJOZ', 'BARCELONA',
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
    preciosSpain = listaPreciosGasolinaSpain()
    nombresCombustibles = listaNombreCombustibles()
    fechaPrecio = fecha()
    listaPreciosPorMarca = preciosPorMarca()
    imagenes = imagenesGasolineras()
    provincia = request.args.get('provincia')
    gasolinerasProvincia = filtrarPorProvincia(provincia)
    return render_template('index.html', preciosSpain_web=preciosSpain, nombresCombustibles_web=nombresCombustibles, fechaPrecio_web=fechaPrecio, preciosPorMarca_web=listaPreciosPorMarca,imagenes_web=imagenes,provicinciasEspana_web=provincias_espana,gasolineasPronvincia_web=gasolinerasProvincia)
            
@app.route('/buscar_gasolineras', methods=['POST'])
def buscarGasolinerasProvincias():
    provincia = request.form['provincia']
    return redirect(url_for('index',provincia=provincia))

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
    
    getMapa(ciudadPartida,ciudadDestino)
    
    return redirect(url_for('ciudades', mensaje=mensaje))
    
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get('PORT', 8080)))