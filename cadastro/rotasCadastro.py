from flask import Blueprint, request, jsonify
from cadastro.modelCadastro import criar_cadastro, exibir_usuarios, exibir_idusuario, atualizar_usuario, deletar_usuario, UsuarioNaoEncontrado

cadastro = Blueprint('cadastro', __name__)

@cadastro.route("/cadastrar", methods=["POST"])
def create_cadastro():
    try:
        senha = request.form.get("password")
        confirmar_senha = request.form.get("confirm_password")
        cpf = "".join(filter(str.isdigit, request.form.get("cpf", "")))
        tel = "".join(filter(str.isdigit, request.form.get("telephone", "")))

        if senha != confirmar_senha:
            return jsonify({"erro": "As senhas são diferentes!"}), 400

        if not cpf.isdigit() or len(cpf) != 11:
            return jsonify({"erro": "CPF inválido. Deve conter 11 números."}), 400
        
        if not tel.isdigit() or len(tel) not in [10, 11]:
            return jsonify({"erro": "Telefone inválido. Verifique a quantidade de números"}), 400

        dados = {
            "nome": request.form.get("name"),
            "email": request.form.get("email"),
            "senha": senha,
            "cpf": cpf,
            "telefone": tel
        }
        
        resposta, status_code = criar_cadastro(dados)
        return jsonify(resposta), status_code
    except Exception as e:
        return jsonify({'erro': f'Erro inesperado ao cadastrar usuário: {str(e)}'}), 500


@cadastro.route("/cadastrar", methods=["GET"])
def get_usuarios():
    try:
        usuarios = exibir_usuarios()
        return jsonify(usuarios), 200
    except Exception as e:
        return jsonify({'erro': f'Erro inesperado ao mostrar usuários: {str(e)}'}), 500
    

@cadastro.route("/cadastrar/<int:id_usuario>", methods=["GET"])
def getID_usuario(id_usuario):
    try:
        usuario = exibir_idusuario(id_usuario)
        return jsonify(usuario), 200
    except UsuarioNaoEncontrado as e:
        return jsonify({'erro': str(e)}), 404
    except Exception as e:
        return jsonify({'erro': str(e)}), 500
    

@cadastro.route("/cadastrar/<int:id_usuario>/atualizar", methods=["POST"])
def update_usuario(id_usuario):
    try:
        dados = {
            "nome": request.form.get("name"),
            "email": request.form.get("email"),
            "senha": request.form.get("password"),
            "cpf": request.form.get("cpf"),
            "telefone": request.form.get("telephone")
        }
        usuario, status_code = atualizar_usuario(id_usuario, dados)
        return jsonify(usuario), status_code
    except UsuarioNaoEncontrado as e:
        return jsonify({'erro': str(e)}), 404
    except Exception as e:
        return jsonify({'erro': f'Erro inesperado ao atualizar usuário: {str(e)}'}), 500
    

@cadastro.route("/cadastrar/<int:id_usuario>/deletar", methods=["POST"])
def delete_usuario(id_usuario):
    try:
        resposta, status_code = deletar_usuario(id_usuario)
        return jsonify(resposta), status_code
    except UsuarioNaoEncontrado as e:
        return jsonify({'erro': str(e)}), 404
    except Exception as e:
        return jsonify({'erro': f'Erro inesperado ao deletar usuário: {str(e)}'}), 500
    