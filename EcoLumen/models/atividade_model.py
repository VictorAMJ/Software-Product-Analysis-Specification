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

def criar_tabela_atividades():
    conexao = bd_config()
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS atividades (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            atividade VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL,
            dia DATE NOT NULL,
            participantes INT NOT NULL
        );
    """)
    conexao.commit()
    cursor.close()
    conexao.close()


def nova_atividade(nome, atividade, email, dia, participantes):
    conexao = bd_config()
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO atividades (nome, atividade, email, dia, participantes)
        VALUES(%s, %s, %s, %s, %s)
    """, (nome, atividade, email, dia, participantes))
    conexao.commit()
    cursor.close()
    conexao.close()
    return "Atividade criada com sucesso"

def listar_atividades():
    conexao = bd_config()
    cursor = conexao.cursor()
    cursor.execute("SELECT id, nome, atividade, email, dia, participantes FROM atividades")
    atividades = cursor.fetchall()
    cursor.close()
    conexao.close()
    return atividades

def listar_por_email(email):
    email = str(email)
    conexao = bd_config()
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT id, nome, atividade, email, dia, participantes 
        FROM atividades
        WHERE email = %s
        ORDER BY dia ASC
    """, (email,))
    atividades = cursor.fetchall()
    cursor.close()
    conexao.close()
    return atividades

def atualizar_atividade(nome, participantes, id):
    conexao = bd_config()
    cursor = conexao.cursor()
    cursor.execute("""
        UPDATE atividades
        SET nome = %s, participantes = %s
        WHERE id = %s
    """, (nome, participantes, id))
    conexao.commit()
    cursor.close()
    conexao.close()
    return "Atualizado com sucesso"

def deletar_atividade(id):
    conexao = bd_config()
    cursor = conexao.cursor()
    cursor.execute("""
        DELETE FROM atividades
        WHERE id = %s
        RETURNING id
    """, (id,))
    conexao.commit()
    cursor.close()
    conexao.close()
    return "Deletado com sucesso"