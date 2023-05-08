from flask import Flask, render_template, request, flash
from Projeto_flask_login.aplicativo.models import db

app = Flask(__name__)
app.config['SECRET_KEY'] = "minha_key_wilson"


@app.route("/", methods=['GET'])
def index():
    return render_template('home.html')


@app.route('/cadastro', methods=['GET'])
def cadastro():
    return render_template('cadastro.html')


@app.route('/verificar', methods=['POST'])
def verificar_register():
    email = request.form.get('email')
    senha = request.form.get('senha')
    conf_senha = request.form.get('conf_senha')
    if senha == conf_senha:
        list_cadastro = {'email': email, 'senha': senha, 'conf_senha': conf_senha}
        db.conectar(var_info=list_cadastro, register=True)
    else:
        flash('As senhas não correspondem ')
    return render_template('cadastro.html')


@app.route('/verificar_login', methods=['POST'])
def verificar_login():
    email = request.form.get('email')
    senha = request.form.get('senha')
    list_login = {'email': email, 'senha': senha}
    db.conectar(var_info=list_login, login=True)
    return render_template('home.html')


@app.route('/voltar', methods=['POST'])
def voltar():
    return render_template('home.html')





