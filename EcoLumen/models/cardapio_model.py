import psycopg2
from config import Config
from datetime import datetime

def bd_config():
    return psycopg2.connect(
        host=Config.DB_HOST,
        database=Config.DB_NAME,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD,
        port=Config.DB_PORT
    )

def criar_tabela_refeicoes():
    conexao = bd_config()
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS refeicoes(
            id SERIAL PRIMARY KEY,
            email VARCHAR(100) NOT NULL,
            refeicao VARCHAR(100) NOT NULL,
            quantidade INT NOT NULL,
            data_registro TIMESTAMP DEFAULT NOW()
        );
    """)
    conexao.commit()
    cursor.close()
    conexao.close()

def add_refeicao(email, refeicao, quantidade):
    conexao = bd_config()
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO refeicoes(email, refeicao, quantidade)
        VALUES(%s, %s, %s)
    """, (email, refeicao, quantidade))
    conexao.commit()
    cursor.close()
    conexao.close()
    return "Refeição adicionada com sucesso"

def listar_refeicoes():
    conexao = bd_config()
    cursor = conexao.cursor()
    cursor.execute("SELECT id, email, refeicao, quantidade, TO_CHAR(data_registro, 'DD/MM/YYYY') AS data_registro FROM refeicoes")
    refeicoes = cursor.fetchall()
    cursor.close()
    conexao.close()
    return refeicoes

def drop_tabela_refeicoes():
    conexao = bd_config()
    cursor = conexao.cursor()
    cursor.execute("DROP TABLE IF EXISTS refeicoes;")
    conexao.commit()
    cursor.close()
    conexao.close()