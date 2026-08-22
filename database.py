import sqlite3

DATABASE_NAME = "sistema_contas.db"

def conectar():
    return sqlite3.connect(DATABASE_NAME)

def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao TEXT NOT NULL,
            categoria TEXT NOT NULL,
            valor REAL NOT NULL,
            vencimento TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'PENDENTE'
        )
    """)
    conexao.commit()
    conexao.close()
    

