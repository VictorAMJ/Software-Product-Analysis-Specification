from flask import Flask
from controller import cadastro

app = Flask(__name__, static_folder="static", template_folder="templates")

app.register_blueprint(cadastro)

if __name__ == "__main__":
    app.run(debug=True)
