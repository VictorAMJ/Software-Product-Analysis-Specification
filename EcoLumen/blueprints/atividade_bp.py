from flask import Blueprint, render_template, request
from controllers.atividade_controller import inscrever, listar_atividades_html, listar_atividades_hospede, atualizar_atividade_hospede, deletar_atividade_hospede


atividade_bp = Blueprint("atividade_bp", __name__)

@atividade_bp.route("/atividades", methods=["GET", "POST"])
def pagina_atividade():
    if request.method == "POST":
        return inscrever(request)
    return render_template("atividade/atividade_recreativa.html")

@atividade_bp.route("/atividadess")
def usuarios_geral():
    return listar_atividades_html()

@atividade_bp.route("/atividades/suas_atividades")
def pagina_suas_atividades():
    return render_template("atividade/atividade_inscritas.html")

@atividade_bp.route("/api/atividades/suas_atividades")
def api_atividades_hospede():
    return listar_atividades_hospede()

@atividade_bp.route("/atividades/<int:id>", methods=["PUT"])
def atualizar(id):
    return atualizar_atividade_hospede(request, id)

@atividade_bp.route("/atividades/<int:id>", methods=["DELETE"])
def deletar(id):
    return deletar_atividade_hospede(id)