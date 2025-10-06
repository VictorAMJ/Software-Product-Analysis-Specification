from flask import Blueprint, render_template, request, session, redirect, url_for
from controllers.reserva_controller import reservar, lista_reservas_html, checkin_reservado
from datetime import datetime

reserva_bp = Blueprint("reserva_bp", __name__)

@reserva_bp.route("/reserva", methods=["GET", "POST"])
def pagina_reserva():
    if request.method == "POST":
        return reservar(request)
    return render_template("reserva/reserva_quarto.html")

@reserva_bp.route("/reservas")
def usuarios():
    return lista_reservas_html()


@reserva_bp.route("/reserva/pre-checkin")
def pre_checkin():
    email = session.get("email")
    if not email:
        return {"status": "erro", "mensagem": "Usuário não logado."}, 401

    reservas = checkin_reservado(email)
    if not reservas:
        return {"status": "vazio", "mensagem": "Nenhuma reserva futura encontrada."}, 200

    reservas_dict = [
        {
            "nome": r[1],
            "email": r[2],
            "quarto": r[3],
            "check_in": r[4].strftime("%Y-%m-%d"),
            "check_out": r[5].strftime("%Y-%m-%d"),
            "numero_hospedes": r[6]
        }
        for r in reservas
    ]

    return {"status": "sucesso", "reservas": reservas_dict}, 200

