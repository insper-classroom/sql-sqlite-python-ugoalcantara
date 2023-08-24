import sqlite3

conn = sqlite3.connect('db/database_alunos.db')

def tabela(conn):
   cursor = conn.cursor()
   cursor.execute("""
    CREATE TABLE IF NOT EXISTS Estudantes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Curso TEXT NOT NULL,
    AnoIngresso INTEGER
    );
""")
   
def inscricao(conn, Estudantes):
    conn.cursor().executemany("""
    INSERT INTO Estudantes (Nome, Curso, AnoIngresso)
    VALUES (?, ?, ?);
    """, Estudantes)

def consultas(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Livros")
    return cursor.fetchall()

def nova(conn, table, oq_atualização, ident, ja_atualizado, ident_name):
    cursor = conn.cursor()
    cursor.execute(f"UPDATE {table} SET {oq_atualização} = ? WHERE {ident} = ?", (ja_atualizado, ident_name))
    conn.commit()

def lixo(conn, table, ident, deletar):
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM {table} WHERE {ident} = ?", (deletar,))
    conn.commit()
