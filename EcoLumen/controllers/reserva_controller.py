from flask import render_template, request, jsonify
from models.reserva_model import nova_reserva, usuario_existe, conflito_quarto, listar_reservas

def reservar(request):
    nome = request.form["nome"]
    email = request.form["email"]
    quarto = request.form["quarto"]
    check_in = request.form["checkIn"]
    check_out = request.form["checkOut"]
    hospedes = int(request.form["hospedes"])

    if not usuario_existe(email):
        return jsonify({"status": "erro", "mensagem": "Usuario não cadastrado. Faça seu cadastro primeiro!"}), 400
    
    if conflito_quarto(quarto, check_in, check_out):
        return jsonify({"status": "erro", "mensagem": "Quarto já reservado nesse período!"}), 400
        
    nova_reserva(nome, email, quarto, check_in, check_out, hospedes)
    return jsonify({"status": "sucesso", "mensagem": "Reserva feita com sucesso!"}), 200


def lista_reservas_html():
    usuarios = listar_reservas()
    tabela_html = "<h2>Lista de Reservas</h2><table border='1'><tr><th>ID</th><th>Nome</th><th>Email</th><th>quarto</th><th>check_in</th><th>check_out</th><th>hospedes</th></tr>"
    for u in usuarios:
        tabela_html += f"<tr><td>{u[0]}</td><td>{u[1]}</td><td>{u[2]}</td><td>{u[3]}</td><td>{u[4]}</td><td>{u[5]}</td><td>{u[6]}</td></tr>"
    tabela_html += "</table>"
    return tabela_html
