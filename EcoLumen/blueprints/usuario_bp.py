from flask import Blueprint, render_template, request, session, redirect, url_for
from controllers.usuario_controller import cadastrar_usuario, login_usuario, lista_usuarios_html

usuario_bp = Blueprint("usuario_bp", __name__)

@usuario_bp.route("/")
def home_publica():
    return render_template("usuario/home_publico.html")

@usuario_bp.route("/home")
def home_privada():
    if "email" not in session:
        return redirect(url_for("usuario_bp.login"))
    return render_template("usuario/home_privada.html")

@usuario_bp.route("/cadastro/")
def cadastro():
    return render_template("usuario/cadastro.html")

@usuario_bp.route("/cadastrar", methods=["POST"])
def cadastrar():
    return cadastrar_usuario(request)

@usuario_bp.route("/login", methods=["GET", "POST"])
def login():
    return login_usuario(request)

@usuario_bp.route("/usuarios")
def usuarios():
    return lista_usuarios_html()

@usuario_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("usuario_bp.login"))

