import sqlite3

class Banco():
    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.createTables()

    def createTables(self):
        c = self.conexao.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS usuarios (
                    idusuario INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    telefone TEXT,
                    email TEXT,
                    usuario TEXT,
                    senha TEXT
                )""")

        c.execute("""CREATE TABLE IF NOT EXISTS cidades (
                    idcidade INTEGER PRIMARY KEY AUTOINCREMENT,
                    idusuario INTEGER,
                    uf TEXT,
                    FOREIGN KEY (idusuario) REFERENCES usuarios(idusuario)
                )""")
        self.conexao.commit()
        c.close()