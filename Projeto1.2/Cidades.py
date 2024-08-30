from tkinter import *
from tkinter import messagebox
from Banco import Banco
from tkinter import ttk
import sqlite3

class Cidades:
    def __init__(self, idcidade=0, nome="", estado=""):
        self.idcidade = idcidade
        self.nome = nome
        self.estado = estado

    def insertCidade(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("""
            INSERT INTO cidades (nome, estado)
            VALUES (?, ?)
            """, (self.nome, self.estado))
            banco.conexao.commit()
            c.close()
            messagebox.showinfo("Sucesso", "Cidade cadastrada com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro na inserção da cidade: {e}")

    def updateCidade(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("""
            UPDATE cidades
            SET nome = ?, estado = ?
            WHERE idcidade = ?
            """, (self.nome, self.estado, self.idcidade))
            banco.conexao.commit()
            c.close()
            messagebox.showinfo("Sucesso", "Cidade atualizada com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro na alteração da cidade: {e}")

    def deleteCidade(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("DELETE FROM cidades WHERE idcidade = ?", (self.idcidade,))
            banco.conexao.commit()
            c.close()
            messagebox.showinfo("Sucesso", "Cidade excluída com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro na exclusão da cidade: {e}")

    def selectCidade(self, idcidade):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("SELECT * FROM cidades WHERE idcidade = ?", (idcidade,))
            row = c.fetchone()
            if row:
                self.idcidade, self.nome, self.estado = row
            c.close()
            messagebox.showinfo("Sucesso", "Busca feita com sucesso!") if row else messagebox.showwarning("Aviso", "Cidade não encontrada.")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro na busca da cidade: {e}")

    def fetchAllUsers():
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("SELECT idcidade, nome, estado FROM cidades")
            rows = c.fetchall()
            c.close()
            return rows
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro na busca das cidades: {e}")
            return []

class CidadesApp:
    def __init__(self, master=None):
        self.master = master
        self.master.title('Cadastro de Cidades')
        self.master.geometry('600x475')

        self.fonte = ("Verdana", "8")

        self.container1 = Frame(self.master, pady=10)
        self.container1.pack()

        self.container2 = Frame(self.master, padx=20, pady=5)
        self.container2.pack()

        self.container3 = Frame(self.master, padx=20, pady=5)
        self.container3.pack()

        self.container4 = Frame(self.master, padx=20, pady=5)
        self.container4.pack()

        self.container6 = Frame(self.master, padx=20, pady=5)
        self.container6.pack()

        self.container7 = Frame(self.master, padx=20, pady=5)
        self.container7.pack()

        self.container8 = Frame(self.master, padx=20, pady=10)
        self.container8.pack()

        self.container9 = Frame(self.master, pady=15)
        self.container9.pack()

        self.container10 = Frame(self.master, pady=15)
        self.container10.pack()

        self.titulo = Label(self.container1, text="Informe os dados:", font=("Calibri", "9", "bold"))
        self.titulo.pack()

        self.lblidcidade = Label(self.container2, text="Código:", font=self.fonte, width=10)
        self.lblidcidade.pack(side=LEFT)
        self.txtidcidade = Entry(self.container2, width=10, font=self.fonte)
        self.txtidcidade.pack(side=LEFT)
        self.btnBuscarCidade = Button(self.container2, text="Buscar", font=self.fonte, width=10, command=self.buscarCidade)
        self.btnBuscarCidade.pack(side=RIGHT)

        self.lblnomecidade = Label(self.container3, text="Nome:", font=self.fonte, width=10)
        self.lblnomecidade.pack(side=LEFT)
        self.txtnomecidade = Entry(self.container3, width=25, font=self.fonte)
        self.txtnomecidade.pack(side=LEFT)

        self.lblestado = Label(self.container4, text="UF:", font=self.fonte, width=10)
        self.lblestado.pack(side=LEFT)
        self.txtestado = Entry(self.container4, width=25, font=self.fonte)
        self.txtestado.pack(side=LEFT)

        self.bntInsertCidade = Button(self.container8, text="Inserir", font=self.fonte, width=12, command=self.inserirCidade)
        self.bntInsertCidade.pack(side=LEFT)
        self.bntAlterarCidade = Button(self.container8, text="Alterar", font=self.fonte, width=12, command=self.alterarCidade)
        self.bntAlterarCidade.pack(side=LEFT)
        self.bntExcluirCidade = Button(self.container8, text="Excluir", font=self.fonte, width=12, command=self.excluirCidade)
        self.bntExcluirCidade.pack(side=LEFT)

        self.lblmsgCidade = Label(self.container9, text="", font=("Verdana", "9", "italic"))
        self.lblmsgCidade.pack()

        self.listaCidades = ttk.Treeview(self.container10, columns=("id", "nome", "estado"), show="headings")
        self.listaCidades.heading("id", text="ID")
        self.listaCidades.heading("nome", text="Nome")
        self.listaCidades.heading("estado", text="E-mail")
        self.listaCidades.pack()

        self.carregarCidades()

    def carregarCidades(self):
        for row in Cidades.fetchAllUsers():
            self.listaCidades.insert("", "end", values=row)

    def inserirCidade(self):
        cidade = Cidades(nome=self.txtnomecidade.get(), estado=self.txtestado.get())
        cidade.insertCidade()
        self.limparCamposCidade()

    def alterarCidade(self):
        cidade = Cidades(idcidade=self.txtidcidade.get(), nome=self.txtnomecidade.get(), estado=self.txtestado.get())
        cidade.updateCidade()
        self.limparCamposCidade()

    def excluirCidade(self):
        cidade = Cidades(idcidade=self.txtidcidade.get())
        cidade.deleteCidade()
        self.limparCamposCidade()

    def buscarCidade(self):
        cidade = Cidades()
        idcidade = self.txtidcidade.get()
        cidade.selectCidade(idcidade)
        if cidade.idcidade:
            self.txtidcidade.delete(0, END)
            self.txtidcidade.insert(INSERT, cidade.idcidade)
            self.txtnomecidade.delete(0, END)
            self.txtnomecidade.insert(INSERT, cidade.nome)
            self.txtestado.delete(0, END)
            self.txtestado.insert(INSERT, cidade.estado)

    def limparCamposCidade(self):
        self.txtidcidade.delete(0, END)
        self.txtnomecidade.delete(0, END)
        self.txtestado.delete(0, END)

if __name__ == "__main__":
    root = Tk()
    app = CidadesApp(master=root)
    root.mainloop()