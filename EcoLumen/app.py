from flask import Flask
from config import Config
from models.usuario_model import criar_tabela_usuarios
from models.reserva_model import criar_tabela_reservas
from models.atividade_model import criar_tabela_atividades
from blueprints.usuario_bp import usuario_bp
from blueprints.reserva_bp import reserva_bp
from blueprints.atividade_bp import atividade_bp
from blueprints.consumo_bp import consumo_bp
from blueprints.cardapio_bp import cardapio_bp


app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = "9b1d2e4f7a5c8d3e9a0b6c4d2e8f7a3c"

criar_tabela_usuarios()
criar_tabela_reservas()
criar_tabela_atividades()


from flask import Flask, render_template, jsonify
from models.usuario_model import bd_config
from models.reserva_model import bd_config

def limpar_bd():
    conexao = bd_config()
    cursor = conexao.cursor()
    cursor.execute("TRUNCATE TABLE reservas RESTART IDENTITY CASCADE;")
    cursor.execute("TRUNCATE TABLE usuarios RESTART IDENTITY CASCADE;")
    conexao.commit()
    cursor.close()
    conexao.close()
    return "Banco de dados limpo com sucesso!"

@app.route("/limpar")
def pagina_limpar():
    return render_template("NAOMEXER/limpar_bd.html")

@app.route("/limpar_bd", methods=["POST"])
def rota_limpar_bd():
    mensagem = limpar_bd()
    return jsonify({"mensagem": mensagem})

app.register_blueprint(usuario_bp)
app.register_blueprint(reserva_bp)
app.register_blueprint(atividade_bp)
app.register_blueprint(consumo_bp)
app.register_blueprint(cardapio_bp)

if __name__ == "__main__":
    app.run(debug=True)
