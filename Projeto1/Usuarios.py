from tkinter import messagebox
from Banco import Banco

class Usuarios:
    def __init__(self, idusuario=0, nome="", telefone="", email="", usuario="", senha=""):
        self.idusuario = idusuario
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.usuario = usuario
        self.senha = senha

    def insertUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("""
            INSERT INTO usuarios (nome, telefone, email, usuario, senha)
            VALUES (?, ?, ?, ?, ?)
            """, (self.nome, self.telefone, self.email, self.usuario, self.senha))
            banco.conexao.commit()
            c.close()
            messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro na inserção do usuário: {e}")

    def updateUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("""
            UPDATE usuarios
            SET nome = ?, telefone = ?, email = ?, usuario = ?, senha = ?
            WHERE idusuario = ?
            """, (self.nome, self.telefone, self.email, self.usuario, self.senha, self.idusuario))
            banco.conexao.commit()
            c.close()
            messagebox.showinfo("Sucesso", "Usuário atualizado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro na alteração do usuário: {e}")

    def deleteUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("DELETE FROM usuarios WHERE idusuario = ?", (self.idusuario,))
            banco.conexao.commit()
            c.close()
            messagebox.showinfo("Sucesso", "Usuário excluído com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro na exclusão do usuário: {e}")

    def selectUser(self, idusuario):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("SELECT * FROM usuarios WHERE idusuario = ?", (idusuario,))
            row = c.fetchone()
            if row:
                self.idusuario, self.nome, self.telefone, self.email, self.usuario, self.senha = row
            c.close()
            messagebox.showinfo("Sucesso", "Busca feita com sucesso!") if row else messagebox.showwarning("Aviso", "Usuário não encontrado.")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro na busca do usuário: {e}")