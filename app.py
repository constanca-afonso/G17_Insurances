  
from flask import Flask, render_template, request, session
from classes.cliente import Cliente
from classes.agente import Agente
from classes.tipo_apolice import Tipo_Apolice
from classes.apolice import Apolice
from classes.apolice_cliente import Apolice_Cliente
from classes.userlogin import Userlogin
from datafile import filename
from classes.userlogin import Userlogin
from subs.apps_gform import apps_gform 
from subs.apps_subform import apps_subform 
from subs.apps_userlogin import apps_userlogin

app = Flask(__name__)

Cliente.read(filename + 'sqlclassestabela.db')
Agente.read(filename + 'sqlclassestabela.db')
Tipo_Apolice.read(filename + 'sqlclassestabela.db')
Apolice.read(filename + 'sqlclassestabela.db')
Apolice_Cliente.read(filename + 'sqlclassestabela.db')
Userlogin.read(filename + 'sqlclassestabela.db')
app.secret_key = 'BAD_SECRET_KEY'

@app.route("/")
def index():
    return render_template("index.html", ulogin=session.get("user"))
@app.route("/login")
def login():
    return render_template("login.html", user= "", password="", ulogin=session.get("user"),resul = "")
@app.route("/logoff")
def logoff():
    session.pop("user",None)
    return render_template("index.html", ulogin=session.get("user"))
@app.route("/chklogin", methods=["post","get"])
def chklogin():
    user = request.form["user"]
    password = request.form["password"]
    resul = Userlogin.chk_password(user, password)
    if resul == "Valid":
        session["user"] = user
        return render_template("index.html", ulogin=session.get("user"))
    return render_template("login.html", user=user, password = password, ulogin=session.get("user"),resul = resul)

@app.route("/gform/<cname>", methods=["post","get"])
def gform(cname):
    return apps_gform(cname)
@app.route("/subform/<cname>", methods=["post","get"])
def subform(cname):
    return apps_subform(cname)
@app.route("/Userlogin", methods=["post","get"])
def userlogin():
    return apps_userlogin()
if __name__ == '__main__':
    app.run()
