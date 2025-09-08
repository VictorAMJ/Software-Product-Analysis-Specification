from flask import Flask, render_template, request
import re
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        port=3380,            
        user="userhotel",
        password="hotelpass",
        database="hotel_sustentavel"
    )

def criar_tabela_usuarios():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL,
            senha VARCHAR(100) NOT NULL,
            cpf CHAR(11) NOT NULL,
            telefone CHAR(11) NOT NULL
        );
    """)
    conn.commit()
    cursor.close()
    conn.close()
    
criar_tabela_usuarios()


@app.route("/")
def index():
    return render_template("cadastro.html")

@app.route("/cadastrar", methods=["POST"])
def cadastrar():

    nome = request.form["name"]
    email = request.form["email"]
    senha = request.form["password"]
    confirma_senha = request.form["confirm_password"]
    cpf = request.form["cpf"]
    telefone = request.form["telephone"]

    if senha != confirma_senha:
        return "<h2>Erro: Senhas não coincidem!</h2>"
    
    cpf_numeros = re.sub(r"\D", "", cpf)
    if len(cpf_numeros) != 11:
        return "<h2>Erro: CPF inválido! Deve conter 11 números.</h2>"
    
    telefone_numeros = re.sub(r"\D", "", telefone)
    if len(telefone_numeros) < 10 or len(telefone_numeros) > 11:
        return "<h2>Erro: Telefone inválido! Deve conter 10 ou 11 números.</h2>"
    

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO usuarios (nome, email, senha, cpf, telefone)
        VALUES (%s, %s, %s, %s, %s)
    """, (nome, email, senha, cpf_numeros, telefone_numeros))
    conn.commit()
    cursor.close()
    conn.close()
    return f"<h2>Cadastro realizado com sucesso!</h2><p>Nome: {nome}<br>Email: {email}<br>CPF: {cpf_numeros}<br>Telefone: {telefone_numeros}</p>"


@app.route("/usuarios")
def listar_usuarios():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, email, cpf, telefone FROM usuarios")
    usuarios = cursor.fetchall()
    cursor.close()
    conn.close()
    
    tabela_html = "<h2>Lista de Usuários</h2><table border='1'><tr><th>ID</th><th>Nome</th><th>Email</th><th>CPF</th><th>Telefone</th></tr>"
    for u in usuarios:
        tabela_html += f"<tr><td>{u[0]}</td><td>{u[1]}</td><td>{u[2]}</td><td>{u[3]}</td><td>{u[4]}</td></tr>"
    tabela_html += "</table>"

    return tabela_html

if __name__ == "__main__":
    app.run(debug=True)
