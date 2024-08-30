from tkinter import *
from tkinter import messagebox
from Banco import Banco
from tkinter import ttk
import sqlite3

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

    def fetchAllUsers():
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("SELECT idusuario, nome, email FROM usuarios")
            rows = c.fetchall()
            c.close()
            return rows
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro na busca dos usuários: {e}")
            return []

class UsuariosApp:
    def __init__(self, master=None):
        self.master = master
        self.master.title('Cadastro de Usuarios')
        self.master.geometry('600x600')

        self.fonte = ("Verdana", "8")

        self.container1 = Frame(master, pady=10)
        self.container1.pack()

        self.container2 = Frame(master, padx=20, pady=5)
        self.container2.pack()

        self.container3 = Frame(master, padx=20, pady=5)
        self.container3.pack()

        self.container4 = Frame(master, padx=20, pady=5)
        self.container4.pack()

        self.container5 = Frame(master, padx=20, pady=5)
        self.container5.pack()

        self.container6 = Frame(master, padx=20, pady=5)
        self.container6.pack()

        self.container7 = Frame(master, padx=20, pady=5)
        self.container7.pack()

        self.container8 = Frame(master, padx=20, pady=10)
        self.container8.pack()

        self.container9 = Frame(master, pady=15)
        self.container9.pack()

        self.container10 = Frame(master, pady=15)
        self.container10.pack()

        self.titulo = Label(self.container1, text="Informe os dados:", font=("Calibri", "9", "bold"))
        self.titulo.pack()

        self.lblidusuario = Label(self.container2, text="Código:", font=self.fonte, width=10)
        self.lblidusuario.pack(side=LEFT)
        self.txtidusuario = Entry(self.container2, width=10, font=self.fonte)
        self.txtidusuario.pack(side=LEFT)
        self.btnBuscar = Button(self.container2, text="Buscar", font=self.fonte, width=10, command=self.buscarUsuario)
        self.btnBuscar.pack(side=RIGHT)

        self.lblnome = Label(self.container3, text="Nome:", font=self.fonte, width=10)
        self.lblnome.pack(side=LEFT)
        self.txtnome = Entry(self.container3, width=25, font=self.fonte)
        self.txtnome.pack(side=LEFT)

        self.lbltelefone = Label(self.container4, text="Telefone:", font=self.fonte, width=10)
        self.lbltelefone.pack(side=LEFT)
        self.txttelefone = Entry(self.container4, width=25, font=self.fonte)
        self.txttelefone.pack(side=LEFT)

        self.lblemail = Label(self.container5, text="E-mail:", font=self.fonte, width=10)
        self.lblemail.pack(side=LEFT)
        self.txtemail = Entry(self.container5, width=25, font=self.fonte)
        self.txtemail.pack(side=LEFT)

        self.lblusuario = Label(self.container6, text="Usuário:", font=self.fonte, width=10)
        self.lblusuario.pack(side=LEFT)
        self.txtusuario = Entry(self.container6, width=25, font=self.fonte)
        self.txtusuario.pack(side=LEFT)

        self.lblsenha = Label(self.container7, text="Senha:", font=self.fonte, width=10)
        self.lblsenha.pack(side=LEFT)
        self.txtsenha = Entry(self.container7, width=25, show="*", font=self.fonte)
        self.txtsenha.pack(side=LEFT)

        self.bntInsert = Button(self.container8, text="Inserir", font=self.fonte, width=12, command=self.inserirUsuario)
        self.bntInsert.pack(side=LEFT)
        self.bntAlterar = Button(self.container8, text="Alterar", font=self.fonte, width=12,
                                 command=self.alterarUsuario)
        self.bntAlterar.pack(side=LEFT)
        self.bntExcluir = Button(self.container8, text="Excluir", font=self.fonte, width=12,
                                 command=self.excluirUsuario)
        self.bntExcluir.pack(side=LEFT)

        self.lblmsg = Label(self.container9, text="", font=("Verdana", "9", "italic"))
        self.lblmsg.pack()

        self.listaUsuarios = ttk.Treeview(self.container10, columns=("id", "nome", "email"), show="headings")
        self.listaUsuarios.heading("id", text="ID")
        self.listaUsuarios.heading("nome", text="Nome")
        self.listaUsuarios.heading("email", text="E-mail")
        self.listaUsuarios.column("id", width=50)
        self.listaUsuarios.column("nome", width=200)
        self.listaUsuarios.column("email", width=200)
        self.listaUsuarios.pack()

        self.carregarUsuarios()

    def carregarUsuarios(self):
        for row in Usuarios.fetchAllUsers():
            self.listaUsuarios.insert("", "end", values=row)

    def inserirUsuario(self):
        user = Usuarios(nome=self.txtnome.get(), telefone=self.txttelefone.get(), email=self.txtemail.get(),
                        usuario=self.txtusuario.get(), senha=self.txtsenha.get())
        self.lblmsg["text"] = user.insertUser()
        self.limparCamposUsuario()

    def alterarUsuario(self):
        user = Usuarios(idusuario=self.txtidusuario.get(), nome=self.txtnome.get(), telefone=self.txttelefone.get(),
                        email=self.txtemail.get(), usuario=self.txtusuario.get(), senha=self.txtsenha.get())
        self.lblmsg["text"] = user.updateUser()
        self.limparCamposUsuario()

    def excluirUsuario(self):
        user = Usuarios(idusuario=self.txtidusuario.get())
        self.lblmsg["text"] = user.deleteUser()
        self.limparCamposUsuario()

    def buscarUsuario(self):
        user = Usuarios()
        idusuario = self.txtidusuario.get()
        self.lblmsg["text"] = user.selectUser(idusuario)
        if user.idusuario:
            self.txtidusuario.delete(0, END)
            self.txtidusuario.insert(INSERT, user.idusuario)
            self.txtnome.delete(0, END)
            self.txtnome.insert(INSERT, user.nome)
            self.txttelefone.delete(0, END)
            self.txttelefone.insert(INSERT, user.telefone)
            self.txtemail.delete(0, END)
            self.txtemail.insert(INSERT, user.email)
            self.txtusuario.delete(0, END)
            self.txtusuario.insert(INSERT, user.usuario)
            self.txtsenha.delete(0, END)
            self.txtsenha.insert(INSERT, user.senha)

    def limparCamposUsuario(self):
        self.txtidusuario.delete(0, END)
        self.txtnome.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtusuario.delete(0, END)
        self.txtsenha.delete(0, END)

if __name__ == "__main__":
    root = Tk()
    app = UsuariosApp(master=root)
    root.mainloop()