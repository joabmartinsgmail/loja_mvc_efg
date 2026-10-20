from flask import Flask, render_template
from controllers.venda_controller import cadastrar
from controllers.venda_controller import listar
from database import criar_tabela
app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("formulario.html")

@app.route("/venda", methods=["POST"])
def salvar_venda():
    return cadastrar()

@app.route("/listar", methods=["GET"])
def listar_vendas():
    return listar()

criar_tabela()
app.run(debug=True)