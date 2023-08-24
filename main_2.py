
from db.db_utils import*

import sqlite3

conn = sqlite3.connect('db/database_alunos.db')
cursor = conn.cursor()

cursor.execute("""
DROP TABLE IF EXISTS Estudantes
""")

tabela(conn)

Estudantes = [
    ('Ana Silva', 'Computação', 2019),
    ('Pedro Mendes', 'Física', 2021),
    ('Carla Souza', 'Computação', 2020),
    ('João Alves', 'Matemática', 2018),
    ('Maria Oliveira', 'Química', 2022),
]
inscricao(conn, Estudantes)
conn.commit()

cursor.execute("SELECT * FROM Estudantes WHERE AnoIngresso BETWEEN 2019 AND 2020")
print(cursor.fetchall())

nova(conn, "Estudantes", "AnoIngresso", "Nome", 2023, "Maria Oliveira")
cursor.execute("SELECT * FROM Estudantes")
conn.commit()
print(cursor.fetchall())

lixo(conn, "Estudantes", "ID", 2)
cursor.execute("SELECT * FROM Estudantes")
conn.commit()
print(cursor.fetchall())

cursor.execute("SELECT * FROM Estudantes WHERE AnoIngresso > 2019 AND Curso = 'Computação'")
print(cursor.fetchall())

nova(conn, "Estudantes", "AnoIngresso", "Curso", 3045, "Computação")
cursor.execute("SELECT * FROM Estudantes")
conn.commit()
print(cursor.fetchall())

conn.close()