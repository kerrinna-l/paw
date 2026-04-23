from flask import Flask, render_template, url_for, request, redirect
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/email')
@app.route('/faleconosco')
@app.route('/contato')
def contato():
    dados = {"nome" : "Alba", "email" : "alba.lopes@ifrn.edu.br"}
    return render_template('contato.html', dados = dados)
    # nome = "Alba Lopes" 
    # email = 'alba.lopes@ifrn.edu.br'
    # return render_template('contato.html', nome = nome, email = email)

@app.route('/usuario', defaults = {"nome" : "Desconhecido", "sobrenome" : "Desconhecido"})
@app.route('/usuario/<nome>/<sobrenome>')
def usuario(nome, sobrenome):
    info = {"nome" : nome, "sobrenome" : sobrenome}
    return render_template('usuario.html', info = info)

@app.route('/semestre/<int:x>')
def semestre(x):
    dados = {}
    dados["atual"] = x
    dados["anterior"] = x - 1
    return render_template('semestre.html', dados = dados)

@app.route('/perfil/', defaults = {"perfil" : "Desconhecido"})
@app.route('/perfil/<perfil>')
def perfil(perfil):
    return render_template('perfil.html', perfil=perfil)

@app.route('/dados')
def dados():
    return render_template('dados.html')

@app.route('/recebedados', methods=['POST', 'GET']) 
def recebedados():
    nome = request.form['nome']
    sobrenome = request.form['sobrenome']
    email = request.form['email']
    estado = request.form.getlist('escola')
    data_nasc = request.form['data_nasc'] 
    data_objeto = datetime.strptime(data_nasc, '%Y-%m-%d')
    data_formatada = data_objeto.strftime('%d/%m/%Y')
    return render_template('recebedados.html', nome=nome, sobrenome=sobrenome, email=email, data_nasc=data_formatada, estado=estado)

@app.route('/verificaridade/<int:idade>')
def verificaridade(idade):
    if idade >= 18:
        return 'Você é MAIOR de idade.'
    else:
        return 'Você é MENOR de idade.'
    
@app.route('/verificaridade2/<int:idade>')
def verificaridade2(idade):
    return render_template('idade.html', idade=idade)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/verificarlogin', methods=['POST'])
def verificarlogin():
    usuario = request.form.get('login')
    senha = request.form.get('senha')
    if usuario == 'admin' and senha == '12345':
        return redirect(url_for('arearestrita'))
    else:
        return redirect(url_for('acessonegado'))

@app.route('/arearestrita')
def arearestrita():
    return render_template('arearestrita.html')

@app.route('/acessonegado')
def acessonegado():
    return render_template('acessonegado.html')

@app.route('/exemplolaco')
def exemplolaco():
    return render_template('exemplolaco.html')

@app.route('/produtos')
def produtos():
    itens = [
        {'nome': 'Teclado', 'preco': '200', 'imagem': 'https://m.media-amazon.com/images/I/61B8ljXNedL._AC_SX679_.jpg'},
        {'nome': 'Smartphone', 'preco': '1500', 'imagem': 'https://m.media-amazon.com/images/I/61WYeXatWNL._AC_SX679_.jpg'},
        {'nome': 'Pen-drive', 'preco': '50', 'imagem': 'https://m.media-amazon.com/images/I/41dXz6DHSFL._AC_SX679_.jpg'},
    ]
    qtd = len(itens)

    return render_template('produtos.html', itens=itens, qtd=qtd)

if __name__ == '__main__':
    app.run()