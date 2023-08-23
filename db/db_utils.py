import sqlite3

conn = sqlite3.connect('db/database_alunos.db')

def cria_tabela(conn):
   cursor = conn.cursor()
   cursor.execute("""
    CREATE TABLE IF NOT EXISTS Estudantes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Curso TEXT NOT NULL,
    AnodeIngresso INTEGER
    );
""")
   
def registro(conn, Estudantes):
    conn.cursor().executemany("""
    INSERT INTO Estudantes (Nome, Curso, AnodeIngresso)
    VALUES (?, ?, ?);
    """, Estudantes)

def consulta(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Livros")
    return cursor.fetchall()

def atualiza(conn, table, oq_atualização, ident, ja_atualizado, ident_name):
    cursor = conn.cursor()
    cursor.execute(f"UPDATE {table} SET {oq_atualização} = ? WHERE {ident} = ?", (ja_atualizado, ident_name))
    conn.commit()

def deleta (conn, table, ident, deletar):
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM {table} WHERE {ident} = ?", {deletar,})
    conn.commit()