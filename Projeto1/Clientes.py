from Banco import Banco

class Clientes:
    def __init__(self, idcliente=0, nome="", telefone="", email="", endereco=""):
        self.idcliente = idcliente
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def insertCliente(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("""
            INSERT INTO clientes (nome, telefone, email, endereco)
            VALUES (?, ?, ?, ?)
            """, (self.nome, self.telefone, self.email, self.endereco))
            banco.conexao.commit()
            c.close()
            return "Cliente cadastrado com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na inserção do cliente: {e}"

    def updateCliente(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("""
            UPDATE clientes
            SET nome = ?, telefone = ?, email = ?, endereco = ?
            WHERE idcliente = ?
            """, (self.nome, self.telefone, self.email, self.endereco, self.idcliente))
            banco.conexao.commit()
            c.close()
            return "Cliente atualizado com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na alteração do cliente: {e}"

    def deleteCliente(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("DELETE FROM clientes WHERE idcliente = ?", (self.idcliente,))
            banco.conexao.commit()
            c.close()
            return "Cliente excluído com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na exclusão do cliente: {e}"

    def selectCliente(self, idcliente):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("SELECT * FROM clientes WHERE idcliente = ?", (idcliente,))
            row = c.fetchone()
            if row:
                self.idcliente, self.nome, self.telefone, self.email, self.endereco = row
            c.close()
            return "Busca feita com sucesso!" if row else "Cliente não encontrado."
        except Exception as e:
            return f"Ocorreu um erro na busca do cliente: {e}"