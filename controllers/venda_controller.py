from flask import request, render_template
from models.venda import Venda

def cadastrar():
    produto = request.form["produto"]
    quantidade = request.form["qtd"]
    preco = request.form["preco"]
    venda = Venda(produto,quantidade,preco)
    venda.salvar()
    return render_template("sucesso.html",produto=produto)

def listar():
    vendas_ctrl = Venda.listar()
    return render_template("listar.html",vendas_tpl=vendas_ctrl)