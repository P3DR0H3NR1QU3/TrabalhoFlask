from flask import Flask, render_template, request, redirect, Blueprint, url_for
from utils import db
from flask_migrate import Migrate




app = Flask(__name__)
app.secret_key = "Minha_chave_Secreta"

conexao = "sqlite///meubanco.sqlite"

produtos = []

max = 0

@app.route('/')
def principal():
    return render_template('principal.html')

@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastrar.html')

@app.route('/cadastrar_enviar', methods=['POST'])
def cadastrar_enviar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    quantidade = request.form['quantidade']
    preco = request.form['preco']
    
    global max
    novo_Produto = {
        'id': max + 1,
        'nome' : nome,
        'categoria' : categoria,
        'quantidade': quantidade,
        'preco': preco
    }

    produtos.append(novo_Produto)

    max+=1

    return redirect('/cadastrar')

@app.route('/listar_produtos')
def listar():
    return render_template('listar.html', produtos = produtos)


@app.route('/editar/<int:id_produto>')
def editar(id_produto):
    dados_produto = [item for item in produtos if item['id'] == id_produto][0]
    return render_template('editar.html', dados_produto = dados_produto)  

@app.route('/editar_enviar', methods=['POST'])
def editar_enviar():
    id_produto = request.form['id_produto']
    nome = request.form['nome']
    categoria = request.form['categoria']
    quantidade = request.form['quantidade']
    preco = request.form['preco']

    dados_produto = [item for item in produtos if item['id'] == int(id_produto)][0]

    dados_produto['nome'] = nome
    dados_produto['categoria'] = categoria
    dados_produto['quantidade'] = quantidade
    dados_produto['preco'] = preco

    return redirect('/listar_produtos')

@app.route('/excluir/<int:id_produto>')
def excluir(id_produto):
    global produtos
    produtos = [item for item in produtos if item['id'] != id_produto]

    return redirect(('/listar_produtos'))


if __name__ == '__main__':
    app.run()