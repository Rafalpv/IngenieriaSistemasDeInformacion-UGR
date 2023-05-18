import os 
from flask import Flask, render_template, redirect, url_for, request
from precioGasolinaSpain import listaPreciosGasolinaSpain, listaNombreCombustibles, fecha

app = Flask(__name__)

@app.route("/")
def hello_world():
    name=os.environ.get("NAME","World")
    return redirect(url_for("index"))

@app.route("/index")
def index():
    preciosSpain = listaPreciosGasolinaSpain()
    nombresCombustibles = listaNombreCombustibles()
    fechaPrecio = fecha()
    return render_template("index.html", preciosSpain_web=preciosSpain, nombresCombustibles_web=nombresCombustibles, fecha_web=fechaPrecio)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))