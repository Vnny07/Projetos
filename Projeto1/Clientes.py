from tkinter import messagebox
from Banco import Banco

class Clientes:
    def __init__(self, idcliente=0, nome="", telefone="", endereco="", cpf="", cidade=""):
        self.idcliente = idcliente
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco
        self.cpf = cpf
        self.cidade = cidade

    def insertCliente(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("""
            INSERT INTO clientes (nome, telefone, endereco, cpf, cidade)
            VALUES (?, ?, ?, ?, ?)
            """, (self.nome, self.telefone, self.endereco, self.cpf, self.cidade))
            banco.conexao.commit()
            c.close()
            messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro na inserção do cliente: {e}")

    def updateCliente(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("""
            UPDATE clientes
            SET nome = ?, telefone = ?, endereco = ?, cpf = ?, cidade = ?
            WHERE idcliente = ?
            """, (self.nome, self.telefone, self.endereco, self.cpf, self.cidade, self.idcliente))
            banco.conexao.commit()
            c.close()
            messagebox.showinfo("Sucesso", "Cliente atualizado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro na alteração do cliente: {e}")

    def deleteCliente(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("DELETE FROM clientes WHERE idcliente = ?", (self.idcliente,))
            banco.conexao.commit()
            c.close()
            messagebox.showinfo("Sucesso", "Cliente excluído com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro na exclusão do cliente: {e}")

    def selectCliente(self, idcliente):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("SELECT * FROM clientes WHERE idcliente = ?", (idcliente,))
            row = c.fetchone()
            if row:
                self.idcliente, self.nome, self.telefone, self.endereco, self.cpf, self.cidade = row
            c.close()
            messagebox.showinfo("Sucesso", "Busca feita com sucesso!") if row else messagebox.showwarning("Aviso", "Cliente não encontrado.")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro na busca do cliente: {e}")