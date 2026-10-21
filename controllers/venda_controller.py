from flask import request, render_template,render_template_string
from models.venda import Venda

def cadastrar():
    produto = request.form["produto"]
    quantidade = request.form["qtd"]
    preco = request.form["preco"]
    venda = Venda(produto,quantidade,preco)
    venda.salvar()
    return render_template("sucesso.html",produto=produto)

def listar():
    vendas = Venda.listar()
    return render_template("listar.html",vendas=vendas)

def importar():
    if request.method == "GET":
        return render_template("importar.html")
    if request.method == "POST":
        return render_template_string("<h1>funcionou<h1>")