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

def criar_tabela_reservas():
    conexao = bd_config()
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reservas (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL,
            quarto VARCHAR(100) NOT NULL,
            check_in DATE NOT NULL,
            check_out DATE NOT NULL,
            numero_hospedes INT NOT NULL
        );
    """)
    conexao.commit()
    cursor.close()
    conexao.close()

def usuario_existe(email):
    conexao = bd_config()
    cursor = conexao.cursor()
    cursor.execute("SELECT id FROM usuarios WHERE email = %s", (email,))
    existe = cursor.fetchone()
    cursor.close()
    conexao.close()
    return existe is not None

def conflito_quarto(quarto, check_in, check_out):
    conexao = bd_config()
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT id FROM reservas 
        WHERE quarto = %s 
            AND NOT (check_out <= %s OR check_in >= %s)
    """, (quarto, check_in, check_out))
    conflito = cursor.fetchone()
    cursor.close()
    conexao.close()
    return conflito is not None

def nova_reserva(nome, email, quarto, check_in, check_out, num_hospedes):
    conexao = bd_config()
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO reservas (nome, email, quarto, check_in, check_out, numero_hospedes)
        VALUES(%s, %s, %s, %s, %s, %s)
    """, (nome, email, quarto, check_in, check_out, num_hospedes))
    conexao.commit()
    cursor.close()
    conexao.close()
    return "Reserva criada com sucesso"

def listar_reservas():
    conexao = bd_config()
    cursor = conexao.cursor()
    cursor.execute("SELECT id, nome, email, quarto, check_in, check_out, numero_hospedes FROM reservas")
    reservas = cursor.fetchall()
    cursor.close()
    conexao.close()
    return reservas

def listar_reservas_por_email(email):
    email = str(email)
    conexao = bd_config()
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT id, nome, email, quarto, check_in, check_out, numero_hospedes
        FROM reservas
        WHERE email = %s
        ORDER BY check_in ASC
    """, (email,))
    reservas = cursor.fetchall()
    cursor.close()
    conexao.close()
    return reservas

def verificar_reserva_por_data(email, dia_atividade):
    email = str(email)
    conexao = bd_config()
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT id, nome, email, quarto, check_in, check_out
        FROM reservas
        WHERE email = %s
        AND %s BETWEEN check_in AND check_out
    """, (email, dia_atividade))
    reserva = cursor.fetchone()
    cursor.close()
    conexao.close()
    return reserva