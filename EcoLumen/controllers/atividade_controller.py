from flask import render_template, request, jsonify, session
from models.atividade_model import nova_atividade, listar_atividades, listar_por_email, atualizar_atividade, deletar_atividade
from models.reserva_model import verificar_reserva_por_data
from datetime import datetime, date

def inscrever(request):
    nome = request.form["nome"]
    atividade = request.form["atividade"]
    email = request.form["email"]
    dia = request.form["dia"]
    participantes = int(request.form["participantes"])

    reserva = verificar_reserva_por_data(email, dia)

    if not reserva:
        return jsonify({"erro": "Você não possui uma reserva ativa para essa data."}), 400

    nova_atividade(nome, atividade, email, dia, participantes)
    return jsonify({"mensagem": "Atividade reservada com sucesso!"}), 200

def listar_atividades_html():
    geral = listar_atividades()
    tabela_html = "<h2>Lista de Atividades</h2><table border='1'><tr><th>ID</th><th>Nome</th><th>atividade</th><th>Email</th><th>dia</th><th>participantes</th></tr>"
    for pessoa in geral:
        tabela_html += f"<tr><td>{pessoa[0]}</td><td>{pessoa[1]}</td><td>{pessoa[2]}</td><td>{pessoa[3]}</td><td>{pessoa[4]}</td><td>{pessoa[5]}</td></tr>"
    tabela_html += "</table"
    return tabela_html

def listar_atividades_hospede():
    email = session.get("email")

    if not email:
        return jsonify({"erro": "Usuario não autenticado"}), 401
    
    atividades = listar_por_email(email)
    return jsonify(atividades)

def atualizar_atividade_hospede(request, id):
    dados = request.get_json()

    nome = dados.get("nome")
    participantes = dados.get("participantes")

    atualizar_atividade(nome, participantes, id)
    return jsonify({"mensagem": "Atividade atualizada com sucesso!"}), 200

def deletar_atividade_hospede(id):

    deletar_atividade(id)
    return jsonify({"mensagem": "Atividade excluída com sucesso!"}), 200
