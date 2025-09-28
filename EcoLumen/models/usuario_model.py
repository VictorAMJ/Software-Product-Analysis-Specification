import psycopg2
from config import Config

def bd_config():
    return psycopg2.connect(
        host=Config.DB_HOST,
        database=Config.DB_NAME,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD,
        port=Config.DB_PORT
    )

def criar_tabela_usuarios():
    conexao = bd_config()
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL,
            senha VARCHAR(100) NOT NULL,
            cpf CHAR(11) NOT NULL,
            telefone CHAR(11) NOT NULL
        );
    """)
    conexao.commit()
    cursor.close()
    conexao.close()

def inserir_usuario(nome, email, senha, cpf, telefone):
    conexao = bd_config()
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO usuarios (nome, email, senha, cpf, telefone)
        VALUES (%s, %s, %s, %s, %s)
    """, (nome, email, senha, cpf, telefone))
    conexao.commit()
    cursor.close()
    conexao.close()

def buscar_usuario_email(email):
    conexao = bd_config()
    cursor = conexao.cursor()
    cursor.execute("SELECT email, senha FROM usuarios WHERE email = %s", (email,))
    resultado = cursor.fetchone()
    cursor.close()
    conexao.close()
    return resultado

def listar_usuarios():
    conexao = bd_config()
    cursor = conexao.cursor()
    cursor.execute("SELECT id, nome, email, cpf, telefone FROM usuarios")
    usuarios = cursor.fetchall()
    cursor.close()
    conexao.close()
    return usuarios
