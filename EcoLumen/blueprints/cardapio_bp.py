from flask import Blueprint, render_template, request, session, redirect, url_for

cardapio_bp = Blueprint("cardapio_bp", __name__)

@cardapio_bp.route("/cardapio_digital")
def exibirTela():
    return render_template("cardapio/cardapio.html")