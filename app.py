import hashlib
from flask import Flask, jsonify, render_template, request, redirect, session, flash
import datetime
import mysql.connector
from data.conexao import Conexao
from model.controler_mensagem import Descricao

app = Flask(__name__)

lista_mensagem = [

]

# Página inicial: renderiza o HTML
@app.route("/")
def index():
    return render_template("index.html")

# Quando clicar no action do formulario irá ser post pois enviara as informações
@app.route("/abrir_pagina")
def abrir_pagina():
    descricao = Descricao.recuperar_mensagens()
    
    # Enviar as mensagens para o template
    # return render_template ("pagina_inicial.html")
    return render_template("requisitos.html", descricoes = descricao) 


# Rota para pegar dados do HTML É POST para Mandar pro HTML é GET
@app.route("/post/descricao" , methods = ["POST"])
def post_mensagem():

    # Para pegar o campo do úsuario no HTML
    # Peguei as informações vinda do formulario
    descricao = request.form.get("descricao")
    nivel = request.form.get("nivel")
    valor = request.form.get("valor")
    
    # Cadastrando a mensagem usando a classe mensagem
    Descricao.cadastrardescricao(descricao, nivel, valor )
    
    
    # Redireiona para a pagina inicial
    return redirect("/abrir_pagina")

# Rota para excluir um comentário
@app.route("/delete/descricao/<codigo>")
def delete_descricao(codigo):

    # Chamando a função para deletar
    Descricao.deletar_descricao(codigo)
    return redirect("/abrir_pagina")

# Rota para atualizar a situação como resolvida
@app.route("/resolvida/descricao/<codigo>")
def descricao_resolvida(codigo):

    # Chamando a função para deletar
    Descricao.resolver_descricao(codigo)
    return redirect("/abrir_pagina")

# Rota para atualizar a situação como pendente
@app.route("/pendente/descricao/<codigo>")
def descricao_pendente(codigo):

    # Chamando a função para deletar
    Descricao.pendente_descricao(codigo)
    return redirect("/abrir_pagina")

if __name__ == "__main__":
    app.run(debug=True)