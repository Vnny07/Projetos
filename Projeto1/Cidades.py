from tkinter import *
from tkinter import ttk
from Usuarios import Usuarios
from Banco import Banco

class CidadesApplication:
    def __init__(self, master=None):
        self.fonte = ("Verdana", "8")

        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()

        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()

        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()

        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()

        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()

        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()

        self.titulo = Label(self.container1, text="Cadastro de Cidades")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack()

        self.lblidusuario = Label(self.container2, text="Código do Usuário:", font=self.fonte, width=15)
        self.lblidusuario.pack(side=LEFT)
        self.txtidusuario = Entry(self.container2)
        self.txtidusuario["width"] = 10
        self.txtidusuario["font"] = self.fonte
        self.txtidusuario.pack(side=LEFT)
        self.btnBuscar = Button(self.container2, text="Buscar", font=self.fonte, width=10)
        self.btnBuscar["command"] = self.buscarUsuario
        self.btnBuscar.pack(side=RIGHT)

        self.lblnome = Label(self.container3, text="Nome:", font=self.fonte, width=10)
        self.lblnome.pack(side=LEFT)
        self.txtnome = Entry(self.container3)
        self.txtnome["width"] = 25
        self.txtnome["font"] = self.fonte
        self.txtnome.pack(side=LEFT)

        self.lbluf = Label(self.container4, text="UF:", font=self.fonte, width=10)
        self.lbluf.pack(side=LEFT)
        self.txtuf = Entry(self.container4)
        self.txtuf["width"] = 10
        self.txtuf["font"] = self.fonte
        self.txtuf.pack(side=LEFT)

        self.bntInsert = Button(self.container5, text="Inserir Cidade", font=self.fonte, width=15)
        self.bntInsert["command"] = self.inserirCidade
        self.bntInsert.pack(side=LEFT)

        self.bntAlterar = Button(self.container5, text="Alterar Cidade", font=self.fonte, width=15)
        self.bntAlterar["command"] = self.alterarCidade
        self.bntAlterar.pack(side=LEFT)

        self.bntExcluir = Button(self.container5, text="Excluir Cidade", font=self.fonte, width=15)
        self.bntExcluir["command"] = self.excluirCidade
        self.bntExcluir.pack(side=LEFT)

        self.lblmsg = Label(self.container6, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()

        self.tree = ttk.Treeview(self.container6, columns=("idusuario", "nome", "uf"), show='headings')
        self.tree.heading("idusuario", text="Código")
        self.tree.heading("nome", text="Nome")
        self.tree.heading("uf", text="UF")

        self.tree.column("idusuario", width=100)
        self.tree.column("nome", width=100)
        self.tree.column("uf", width=100)

        self.tree.pack()

        self.listarCidades()

    def inserirCidade(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("INSERT INTO cidades (idusuario, uf) VALUES (?, ?)",
                      (self.txtidusuario.get(), self.txtuf.get()))
            banco.conexao.commit()
            c.close()
            self.lblmsg["text"] = "Cidade inserida com sucesso!"
            self.listarCidades()
        except:
            self.lblmsg["text"] = ""

    def alterarCidade(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("UPDATE cidades SET uf = ? WHERE idusuario = ?",
                      (self.txtuf.get(), self.txtidusuario.get()))
            banco.conexao.commit()
            c.close()
            self.lblmsg["text"] = "Cidade alterada com sucesso!"
            self.listarCidades()
        except:
            self.lblmsg["text"] = ""

    def excluirCidade(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("DELETE FROM cidades WHERE idusuario = ?", (self.txtidusuario.get(),))
            banco.conexao.commit()
            c.close()
            self.lblmsg["text"] = "Cidade excluída com sucesso!"
            self.listarCidades()
        except:
            self.lblmsg["text"] = ""

    def buscarUsuario(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("SELECT nome FROM usuarios WHERE idusuario = ?", (self.txtidusuario.get(),))
            resultado = c.fetchone()
            if resultado:
                self.txtnome.delete(0, END)
                self.txtnome.insert(0, resultado[0])
            else:
                self.lblmsg["text"] = "Usuário não encontrado."
            c.close()
        except:
            self.lblmsg["text"] = ""

    def listarCidades(self):
        self.tree.delete(*self.tree.get_children())
        banco = Banco()
        c = banco.conexao.cursor()
        c.execute("""SELECT u.idusuario, u.nome, c.uf 
            FROM cidades c 
            JOIN usuarios u ON c.idusuario = u.idusuario""")
        cidades = c.fetchall()
        for c in cidades:
            self.tree.insert("", END, values=(c[0], c[1], c[2]))
        c.close()

root = Tk()
root.title("Cadastro de Cidades")
app = CidadesApplication(master=root)
root.mainloop()