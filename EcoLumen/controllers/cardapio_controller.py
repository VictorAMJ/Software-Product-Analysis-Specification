from flask import render_template, request, jsonify
from models.cardapio_model import add_refeicao, listar_refeicoes
from models.reserva_model import verificar_pessoas_reserva
from datetime import datetime

def salvar_refeicao():
    data = request.get_json()
    refeicao = data.get("refeicoes", [])
    email = data.get("email")
    print("recebido:", refeicao)

    if not email:
        return jsonify({"erro": "Email não enviado"}), 400

    quantidade = verificar_pessoas_reserva(email)

    for r in refeicao:
        add_refeicao(email, r, quantidade)
    return jsonify({
        "status": "sucesso",
        "mensagem":"Refeição inserida com sucesso!",
    }), 200



def listar_refeiçoes_html():
    geral = listar_refeicoes()
    tabela_html ="<h2>Lista de Refeiçoes</h2><table border='1'><tr><th>ID</th><th>Email</th><th>Refeição</th><th>Quantidade</th><th>Data</th></tr>"
    for item in geral:
        tabela_html += f"<tr><td>{item[0]}</td><td>{item[1]}</td><td>{item[2]}</td><td>{item[3]}</td><td>{item[4]}</td></tr>"
    tabela_html += "</table>"
    return tabela_html