Usuarios = {
    "usuario":[{
        'nome': "Ana",
        'email': "ana@email.com",
        'senha': "1234abcd",
        'cpf':"12345678901",
        'telefone': "00123456789",
        'id': 1
    }]
}


def criar_cadastro(dados):
    usuario = {
        "nome": dados["nome"],
        "email": dados["email"],
        "senha": dados["senha"],
        "cpf": dados["cpf"],
        'telefone': dados["telefone"],
        'id': len(Usuarios["usuario"]) + 1
    }

    Usuarios["usuario"].append(usuario)
    return{"mensagem": "Cadastro feito com sucesso!", "usuario": usuario}, 201


def exibir_usuarios():
    return Usuarios["usuario"]

def exibir_idusuario(id_usuario):
    for usuario in Usuarios["usuario"]:
        if usuario["id"] == id_usuario:
            return(usuario), 200
    return{"mensagem": "Usuario não encontrado"}, 404


def atualizar_usuario(id_usuaro, dadoNovo):
    for usuario in Usuarios["usuario"]:
        if usuario["id"] == id_usuaro:
            usuario["nome"] = dadoNovo.get("nome", usuario["nome"])
            usuario["email"] = dadoNovo.get("email", usuario["email"])
            usuario["senha"] = dadoNovo.get("senha", usuario["senha"])
            usuario["cpf"] = dadoNovo.get("cpf", usuario["cpf"])
            usuario["telefone"] = dadoNovo.get("telefone", usuario["telefone"])
            return(usuario), 200
    return{"mensagem": "Usuario não encontrado"}, 404


def deletar_usuario(id_usuario):
    for usuario in Usuarios["usuario"]:
        if usuario["id"] == id_usuario:
            Usuarios["usuario"].remove(usuario)
            return{"mensagem": "Usuário deletado com sucesso!"}, 200
    return{"mensagem": "Usuário não encontrado."},404
