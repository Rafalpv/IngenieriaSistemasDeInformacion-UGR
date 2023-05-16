import os 
from flask import Flask, render_template, redirect, url_for, request
from preciogasolina import listaPrecios 

app = Flask(__name__)

@app.route("/")
def hello_world():
    name=os.environ.get("NAME","World")
    return redirect(url_for("index"))

@app.route("/index")
def index():
    precios = listaPrecios()
    return render_template("index.html",precios_web="precios")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))