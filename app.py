from flask import Flask, render_template, url_for, request
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

if __name__ == '__main__':
    app.run()