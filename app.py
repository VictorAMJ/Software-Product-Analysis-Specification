from config import app
from cadastro.rotasCadastro import cadastro

app.register_blueprint(cadastro)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
    