from flask import render_template, request, redirect, session, url_for
import re
from models.usuario_model import inserir_usuario, buscar_usuario_email, listar_usuarios

def cadastrar_usuario(request):
    nome = request.form["name"]
    email = request.form["email"]
    senha = request.form["password"]
    confirma_senha = request.form["confirm_password"]
    cpf = request.form["cpf"]
    telefone = request.form["telephone"]

    if senha != confirma_senha:
        return "Erro: Senhas não coincidem!", 400

    cpf_numeros = re.sub(r"\D", "", cpf)
    if len(cpf_numeros) != 11:
        return "Erro: CPF inválido! Deve ter 11 números.", 400
          
    telefone_numeros = re.sub(r"\D", "", telefone)
    if len(telefone_numeros) < 10 or len(telefone_numeros) > 11:
        return "Erro: Telefone inválido! Deve ter 10 ou 11 números.", 400 

    inserir_usuario(nome, email, senha, cpf_numeros, telefone_numeros)
    return "Cadastro realizado com sucesso!"

def login_usuario(request):
    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]

        usuario = buscar_usuario_email(email)
        if usuario and usuario[1] == senha:
            session["email"] = usuario[0]
            return redirect("/home")
        else:
            return "Email ou senha incorretos!"
    return render_template("usuario/login.html")

def lista_usuarios_html():
    usuarios = listar_usuarios()
    tabela_html = "<h2>Lista de Usuários</h2><table border='1'><tr><th>ID</th><th>Nome</th><th>Email</th><th>CPF</th><th>Telefone</th></tr>"
    for u in usuarios:
        tabela_html += f"<tr><td>{u[0]}</td><td>{u[1]}</td><td>{u[2]}</td><td>{u[3]}</td><td>{u[4]}</td></tr>"
    tabela_html += "</table>"
    return tabela_html
