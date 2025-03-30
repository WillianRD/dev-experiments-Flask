from flask import Flask, render_template, request, url_for
from validarProduto import checkSize,checkCategory
from validarProduto import checkPrice, checkDesc, checkSizeEstoque,checkFornecedor
from validarProduto import caracteres, url
from models import mostrarDados, inserirDados

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        produto = request.form['produto']
        categoria = request.form['categoria']
        preco = request.form['preco']
        descricao = request.form['descricao']
        qtd = request.form['estoque']
        fornecedor= request.form['fornecedor']
        fabricacao= request.form['fabricacao']
        vencimento= request.form['vencimento']
        caracteristicas= request.form['caracteristicas']
        url_link_page = request.form['url_link_page']
    
        inserirDados(produto,categoria,preco,descricao,qtd,fabricacao,vencimento,caracteristicas,url_link_page)
        print(mostrarDados)
    return render_template('index.html')


