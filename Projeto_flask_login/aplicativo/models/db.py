import mysql.connector
from mysql.connector import Error
from flask import flash


def conectar(var_info=None, desconect=False, register=False, login=False):
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            database="cadastros",
            user="root",
            password="")
        cursor = conexao.cursor()
        print('\033[7:32m(Conectado ao servidor [MySQL])\033[m')

        if desconect:
            conexao.close()
            print('\033[31mConexão com o servidor encerrada\033[m')

        if register:
            email = var_info['email']
            senha = var_info['senha']
            senha_conf = var_info['conf_senha']
            cursor.execute("select * from usuarios where email = '" + email + "';")
            verificador = cursor.fetchone()
            if verificador is None:
                cursor.execute("insert into usuarios values ( default, '" + email + "', " + senha + " );")
                conexao.commit()
                flash('Cadastro Criado')
            else:
                flash('Este endereço de e-mail já foi cadastrado')

        if login:
            email = var_info['email']
            senha = var_info['senha']
            cursor.execute("select * from usuarios where email = '" + email + "' and " + senha + ";")
            verificador = cursor.fetchone()
            if verificador is None:
                flash('E-mail não cadastrado')
            else:
                flash('Seja Bem vindo(a)!')

    except Error as erro:
        print('\033[31mNão foi possível conectar ao servidor\033[m')
        opcao = str(input('\033[7mVer informações sobre o erro [S/N]?\033[m '))

        if opcao.upper() == 'S':
            print('\033[7mCod:\033[m ', erro.errno)
            print('\033[7mMsg:\033[m ', erro.msg)
        if opcao.upper() == 'N':
            quit()
