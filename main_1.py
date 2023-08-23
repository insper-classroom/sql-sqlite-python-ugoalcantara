import sqlite3

# Exercício de Python - Sqlite

# Conexão com o banco de dados dentro da pasta "db"
conn = sqlite3.connect('db/database_alunos.db')
cursor = conn.cursor()

cursor.execute("""
DROP TABLE IF EXISTS Estudantes
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Estudantes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Curso TEXT NOT NULL,
    AnoIngresso INTEGER
    );
""")


Estudantes = [
    ('Ana Silva', 'Computação', 2019),
    ('Pedro Mendes', 'Física', 2021),
    ('Carla Souza', 'Computação', 2020),
    ('João Alves', 'Matemática', 2018),
    ('Maria Oliveira', 'Química', 2022),
]

cursor.executemany("""
INSERT INTO Estudantes (Nome, Curso, AnoIngresso)
VALUES (?, ?, ?);
""", Estudantes)
conn.commit()


cursor.execute("SELECT * FROM Estudantes WHERE AnoIngresso BETWEEN 2019 AND 2020")
print(cursor.fetchall())
conn.commit()


cursor.execute("UPDATE Estudantes SET AnoIngresso = ? WHERE Nome = ?", (2009, "Maria Oliveira"))
cursor.execute("SELECT * FROM Estudantes")
conn.commit()
print(cursor.fetchall())

    
cursor.execute("DELETE FROM Estudantes WHERE ID = ?", (1,))  
cursor.execute("SELECT * FROM Estudantes")
conn.commit()
print(cursor.fetchall()) 


cursor.execute("SELECT * FROM Estudantes WHERE AnoIngresso > 2019 AND Curso = 'Computação'")
conn.commit()
print(cursor.fetchall())


cursor.execute("UPDATE Estudantes SET AnoIngresso = ? WHERE Curso = ?", (4569, "Computação"))
cursor.execute("SELECT * FROM Estudantes")
conn.commit()
print(cursor.fetchall())

conn.close()