from app import app
from flask import render_template, request
from api import requestCoin

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/converter", methods=['POST'])
def converter():
    valor = request.form.get('valor')
    moeda = request.form.get('moeda')
    match moeda:
        case "dolar":
            conversao_moeda = float(valor) * float(requestCoin.dolar_real)
        case "euro":
            conversao_moeda = float(valor) * float(requestCoin.euro_real)
        case "bitcoin":
            conversao_moeda = float(valor) * float(requestCoin.bitcoin_real)
        case _:
            conversao_moeda = 0

    return render_template("index.html", conversao = f"{conversao_moeda:.2f}")