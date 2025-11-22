from flask import Blueprint, render_template, request, session, redirect, url_for
from controllers.cardapio_controller import salvar_refeicao, listar_refeiçoes_html
from models.usuario_model import buscar_usuario_email

cardapio_bp = Blueprint("cardapio_bp", __name__)

@cardapio_bp.route("/cardapio_digital", methods=["GET","POST"])
def pagina_refeicao():
    if request.method == "POST":
        return salvar_refeicao()
    return render_template("cardapio/cardapio.html")

@cardapio_bp.route("/refeiçoes_cozinha")
def ver_bd():
    return listar_refeiçoes_html()