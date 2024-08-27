from Usuarios import Usuarios
from tkinter import *
from tkinter import ttk

class Application:
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

        self.container7 = Frame(master)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()

        self.container9 = Frame(master)
        self.container9["pady"] = 15
        self.container9.pack()

        self.container11 = Frame(master)
        self.container11["padx"] = 20
        self.container11["pady"] = 5
        self.container11.pack()

        self.container10 = Frame(master)
        self.container10["padx"] = 20
        self.container10["pady"] = 5
        self.container10.pack()

        self.titulo = Label(self.container1, text="Informe os dados :")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack()

        self.lblidusuario = Label(self.container2, text="Código:", font=self.fonte, width=10)
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

        self.lbltelefone = Label(self.container4, text="Telefone:", font=self.fonte, width=10)
        self.lbltelefone.pack(side=LEFT)
        self.txttelefone = Entry(self.container4)
        self.txttelefone["width"] = 25
        self.txttelefone["font"] = self.fonte
        self.txttelefone.pack(side=LEFT)

        self.lblemail = Label(self.container5, text="E-mail:", font=self.fonte, width=10)
        self.lblemail.pack(side=LEFT)
        self.txtemail = Entry(self.container5)
        self.txtemail["width"] = 25
        self.txtemail["font"] = self.fonte
        self.txtemail.pack(side=LEFT)

        self.lblusuario = Label(self.container6, text="Usuário:", font=self.fonte, width=10)
        self.lblusuario.pack(side=LEFT)
        self.txtusuario = Entry(self.container6)
        self.txtusuario["width"] = 25
        self.txtusuario["font"] = self.fonte
        self.txtusuario.pack(side=LEFT)

        self.lblsenha = Label(self.container7, text="Senha:", font=self.fonte, width=10)
        self.lblsenha.pack(side=LEFT)
        self.txtsenha = Entry(self.container7)
        self.txtsenha["width"] = 25
        self.txtsenha["show"] = "*"
        self.txtsenha["font"] = self.fonte
        self.txtsenha.pack(side=LEFT)

        self.bntInsert = Button(self.container9, text="Inserir", font=self.fonte, width=12)
        self.bntInsert["command"] = self.inserirUsuario
        self.bntInsert.pack(side=LEFT)

        self.bntCidades = Button(self.container9, text="Inserir Cidade", font=self.fonte, width=12)
        self.bntCidades["command"] = self.abrirTelaCidades
        self.bntCidades.pack(side=LEFT)

        self.bntAlterar = Button(self.container9, text="Alterar", font=self.fonte, width=12)
        self.bntAlterar["command"] = self.alterarUsuario
        self.bntAlterar.pack(side=LEFT)

        self.bntExcluir = Button(self.container9, text="Excluir", font=self.fonte, width=12)
        self.bntExcluir["command"] = self.excluirUsuario
        self.bntExcluir.pack(side=LEFT)

        self.lblmsg = Label(self.container10, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()

        self.tree = ttk.Treeview(self.container11, columns=("id", "nome", "email"), show='headings')
        self.tree.heading("id", text="Código")
        self.tree.heading("nome", text="Nome")
        self.tree.heading("email", text="E-mail")

        self.tree.column("id", width=100)
        self.tree.column("nome", width=100)
        self.tree.column("email", width=200)

        self.tree.pack()

        self.listarUsuarios()

    def inserirUsuario(self):
        user = Usuarios(nome=self.txtnome.get(), telefone=self.txttelefone.get(),
                        email=self.txtemail.get(), usuario=self.txtusuario.get(),
                        senha=self.txtsenha.get())
        msg = user.insertUser()
        self.lblmsg["text"] = msg
        self.listarUsuarios()

    def alterarUsuario(self):
        user = Usuarios(idusuario=self.txtidusuario.get(), nome=self.txtnome.get(), telefone=self.txttelefone.get(),
                        email=self.txtemail.get(), usuario=self.txtusuario.get(),
                        senha=self.txtsenha.get())
        msg = user.updateUser()
        self.lblmsg["text"] = msg
        self.listarUsuarios()

    def excluirUsuario(self):
        user = Usuarios(idusuario=self.txtidusuario.get())
        msg = user.deleteUser()
        self.lblmsg["text"] = msg
        self.listarUsuarios()

    def buscarUsuario(self):
        user = Usuarios()
        user.selectUser(int(self.txtidusuario.get()))
        self.txtnome.delete(0, END)
        self.txtnome.insert(0, user.nome)
        self.txttelefone.delete(0, END)
        self.txttelefone.insert(0, user.telefone)
        self.txtemail.delete(0, END)
        self.txtemail.insert(0, user.email)
        self.txtusuario.delete(0, END)
        self.txtusuario.insert(0, user.usuario)
        self.txtsenha.delete(0, END)
        self.txtsenha.insert(0, user.senha)
        self.lblmsg["text"] = "Usuário encontrado"

    def listarUsuarios(self):
        self.tree.delete(*self.tree.get_children())
        user = Usuarios()
        usuarios = user.listUsers()
        for u in usuarios:
            self.tree.insert("", END, values=(u[0], u[1], u[2]))

    def abrirTelaCidades(self):
        import Cidades
        Cidades.root = Tk()
        Cidades.root.title("Cadastro de Cidades")
        CidadesApplication(master=Cidades.root)

root = Tk()
root.title("Cadastro de Usuário")
app = Application(master=root)
root.mainloop()