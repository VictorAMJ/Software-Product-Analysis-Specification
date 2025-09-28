from flask import Blueprint, render_template, request, session, redirect, url_for
from controllers.reserva_controller import reservar, nova_reserva, lista_reservas_html

reserva_bp = Blueprint("reserva_bp", __name__)

@reserva_bp.route("/reserva", methods=["GET", "POST"])
def pagina_reserva():
    if request.method == "POST":
        return reservar(request)
    return render_template("reserva/reserva_quarto.html")

@reserva_bp.route("/reservas")
def usuarios():
    return lista_reservas_html()