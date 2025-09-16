from flask import Blueprint, render_template, request, jsonify
from model import criar_cadastro, listar_usuarios

cadastro = Blueprint('cadastro', __name__)

@cadastro.route("/")
def index():
    return render_template("cadastro.html")

@cadastro.route("/cadastrar", methods=["POST"])
def create_cadastrar():
    try:
        nome = request.form["name"]
        email = request.form["email"]
        senha = request.form["password"]
        confirma_senha = request.form["confirm_password"]
        cpf = request.form["cpf"]
        telefone = request.form["telephone"]

        dados = {
            "name":nome, 
            "email":email, 
            "password":senha, 
            "confirm_password":confirma_senha, 
            "cpf":cpf, 
            "telephone":telefone
        }

        resposta, status_code = criar_cadastro(dados)
        return jsonify(resposta), status_code
    except Exception as e:
        return jsonify({'erro': f'Erro inesperado ao cadastrar usuario:{str(e)}'}), 500


@cadastro.route("/usuarios", methods=["GET"])
def get_usuarios():
    try:
        return listar_usuarios()
    except Exception as e:
        return jsonify({'erro': f'Erro inesperado ao listar usuarios: {str(e)}'}), 500