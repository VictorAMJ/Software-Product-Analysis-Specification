from flask import Blueprint, render_template

consumo_bp = Blueprint('consumo_bp', __name__)

@consumo_bp.route('/monitorar_consumo')
def monitorar_consumo():
    return render_template('consumo/monitorar_consumo.html')










