# pip install mysql-connector-python
import mysql.connector
import sqlite3

def conectar():
    conexao = sqlite3.connect("venda.db")
    return conexao

def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS venda (
        id INT AUTO_INCREMENT PRIMARY KEY,
        produto VARCHAR(100) NOT NULL,
        quantidade INT NOT NULL,
        preco DECIMAL NOT NULL
    );
    """)
    conexao.commit()
    cursor.close()
    conexao.close()