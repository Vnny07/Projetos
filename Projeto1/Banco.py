import sqlite3

class Banco:
    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.createTables()

    def createTables(self):
        try:
            with self.conexao as conn:
                c = conn.cursor()

                c.execute("""
                CREATE TABLE IF NOT EXISTS usuarios (
                    idusuario INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    telefone TEXT,
                    email TEXT,
                    usuario TEXT,
                    senha TEXT
                )
                """)

                c.execute("""
                CREATE TABLE IF NOT EXISTS cidades (
                    idcidade INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    estado TEXT
                )
                """)

                c.execute("""
                CREATE TABLE IF NOT EXISTS clientes (
                    idcliente INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    telefone TEXT,
                    email TEXT
                )
                """)

                conn.commit()
        except sqlite3.Error as e:
            print(f"Erro ao criar tabelas: {e}")

    def close(self):
        if self.conexao:
            self.conexao.close()