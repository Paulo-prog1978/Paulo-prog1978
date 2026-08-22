from database import conectar

def cadastrar_conta(descricao, valor):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contas (descricao, valor) VALUES (?, ?)", (descricao, valor))
    conn.commit()
    conn.close()

def listar_contas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contas")
    contas = cursor.fetchall()
    conn.close()
    return contas

def buscar_conta(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contas WHERE id=?", (id,))
    conta = cursor.fetchone()
    conn.close()
    return conta

def atualizar_conta(id, descricao, valor):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE contas SET descricao=?, valor=? WHERE id=?", (descricao, valor, id))
    conn.commit()
    conn.close()

def excluir_conta(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM contas WHERE id=?", (id,))
    conn.commit()
    conn.close()

def marcar_como_paga(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE contas SET status='paga' WHERE id=?", (id,))
    conn.commit()
    conn.close()

def contas_pendentes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contas WHERE status='pendente'")
    contas = cursor.fetchall()
    conn.close()
    return contas

def total_pendente():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(valor) FROM contas WHERE status='pendente'")
    total = cursor.fetchone()[0]
    conn.close()
    return total or 0

def total_pago():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(valor) FROM contas WHERE status='paga'")
    total = cursor.fetchone()[0]
    conn.close()
    return total or 0

