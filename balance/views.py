from balance import app
from flask import render_template

@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route("/nuevo", methods=["GET", "POST"])
def nuevo():
    return "Pagina de alta de movimiento"

@app.route("/borrar/<int:id>", methods=["GET", "POST"])
def borrar(id):
    return f"Pagina de borrado de {id}"
