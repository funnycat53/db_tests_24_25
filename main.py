import sqlite3
from flask import Flask, render_template, request
from dati import pievienot_skolenu, pievienot_skolotaju, pievienot_prieksmetu, iegut_skolenus, iegut_skolotajus


app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def index():
    skoleni_no_db = iegut_skolenus()
    skolotaji_no_db = iegut_skolotajus()

    if request.method == "POST":
        vards = request.form['name']
        uzvards = request.form['lastname']
        skolotajs_vards = request.form['sk_name']
        skolotajs_uzvards = request.form['sk_lastname']
        prieksmets = request.form['prieksmets']
        if vards and uzvards:
            pievienot_skolenu(vards, uzvards)
        if skolotajs_vards and skolotajs_uzvards:
            pievienot_skolotaju(skolotajs_vards, skolotajs_uzvards)
        if prieksmets:
            pievienot_prieksmetu(prieksmets)

        dati = f"Pievienots skolēns - {vards} {uzvards}, skolotājs - {skolotajs_vards} {skolotajs_uzvards}, mācību priekšmets - {prieksmets}"

        return render_template("index.html", aizsutitais = dati, skoleni = skoleni_no_db, skolotaji = skolotaji_no_db)
    
    # Get metode
    return render_template("index.html", skoleni = skoleni_no_db, skolotaji = skolotaji_no_db)

@app.route("/pievienot", methods=["POST", "GET"])
def pievienot():
    skolotaji = iegut_skolotajus()
    if request.method == "POST":
        print(request.form["skolotajs"])
    return render_template("pievienot.html", skolotaji = skolotaji)

@app.route("/atzimes")
def atzimes():
    return render_template("atzimes.html")



if __name__ == '__main__':
    app.run(port = 5000)