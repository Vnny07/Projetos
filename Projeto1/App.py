from tkinter import *
from tkinter import ttk
from Usuarios import Usuarios
from Cidades import Cidades
from Clientes import Clientes

class Application:
    def __init__(self, master=None):
        self.master = master
        self.master.title('Cadastro')
        self.master.geometry('300x350')

        self.notebook = ttk.Notebook(master)
        self.notebook.pack(fill=BOTH, expand=TRUE)

        self.frame_usuarios = Frame(self.notebook)
        self.frame_cidades = Frame(self.notebook)
        self.frame_clientes = Frame(self.notebook)

        self.notebook.add(self.frame_usuarios, text='Usuários')
        self.notebook.add(self.frame_cidades, text='Cidades')
        self.notebook.add(self.frame_clientes, text='Clientes')

        self.add_usuarios_content()
        self.add_cidades_content()
        self.add_clientes_content()

    def add_usuarios_content(self):
        self.fonte = ("Verdana", "8")

        self.container1 = Frame(self.frame_usuarios, pady=10)
        self.container1.pack()

        self.container2 = Frame(self.frame_usuarios, padx=20, pady=5)
        self.container2.pack()

        self.container3 = Frame(self.frame_usuarios, padx=20, pady=5)
        self.container3.pack()

        self.container4 = Frame(self.frame_usuarios, padx=20, pady=5)
        self.container4.pack()

        self.container5 = Frame(self.frame_usuarios, padx=20, pady=5)
        self.container5.pack()

        self.container6 = Frame(self.frame_usuarios, padx=20, pady=5)
        self.container6.pack()

        self.container7 = Frame(self.frame_usuarios, padx=20, pady=5)
        self.container7.pack()

        self.container8 = Frame(self.frame_usuarios, padx=20, pady=10)
        self.container8.pack()

        self.container9 = Frame(self.frame_usuarios, pady=15)
        self.container9.pack()

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
        self.bntAlterar = Button(self.container8, text="Alterar", font=self.fonte, width=12, command=self.alterarUsuario)
        self.bntAlterar.pack(side=LEFT)
        self.bntExcluir = Button(self.container8, text="Excluir", font=self.fonte, width=12, command=self.excluirUsuario)
        self.bntExcluir.pack(side=LEFT)

        self.lblmsg = Label(self.container9, text="", font=("Verdana", "9", "italic"))
        self.lblmsg.pack()

    def add_cidades_content(self):
        self.fonte = ("Verdana", "8")

        self.container1 = Frame(self.frame_cidades, pady=10)
        self.container1.pack()

        self.container2 = Frame(self.frame_cidades, padx=20, pady=5)
        self.container2.pack()

        self.container3 = Frame(self.frame_cidades, padx=20, pady=5)
        self.container3.pack()

        self.container4 = Frame(self.frame_cidades, padx=20, pady=5)
        self.container4.pack()

        self.container6 = Frame(self.frame_cidades, padx=20, pady=5)
        self.container6.pack()

        self.container7 = Frame(self.frame_cidades, padx=20, pady=5)
        self.container7.pack()

        self.container8 = Frame(self.frame_cidades, padx=20, pady=10)
        self.container8.pack()

        self.container9 = Frame(self.frame_cidades, pady=15)
        self.container9.pack()

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

    def add_clientes_content(self):
        self.fonte = ("Verdana", "8")

        self.container1 = Frame(self.frame_clientes, pady=10)
        self.container1.pack()

        self.container2 = Frame(self.frame_clientes, padx=20, pady=5)
        self.container2.pack()

        self.container3 = Frame(self.frame_clientes, padx=20, pady=5)
        self.container3.pack()

        self.container4 = Frame(self.frame_clientes, padx=20, pady=5)
        self.container4.pack()

        self.container5 = Frame(self.frame_clientes, padx=20, pady=5)
        self.container5.pack()

        self.container10 = Frame(self.frame_clientes, padx=20, pady=5)
        self.container10.pack()

        self.container11 = Frame(self.frame_clientes, pady=5, padx=20)
        self.container11.pack()

        self.container6 = Frame(self.frame_clientes, padx=20, pady=5)
        self.container6.pack()

        self.container7 = Frame(self.frame_clientes, padx=20, pady=5)
        self.container7.pack()

        self.container8 = Frame(self.frame_clientes, padx=20, pady=8)
        self.container8.pack()

        self.container9 = Frame(self.frame_clientes, pady=15)
        self.container9.pack()

        self.titulo = Label(self.container1, text="Informe os dados:", font=("Calibri", "9", "bold"))
        self.titulo.pack()

        self.lblidcliente = Label(self.container2, text="Código:", font=self.fonte, width=10)
        self.lblidcliente.pack(side=LEFT)
        self.txtidcliente = Entry(self.container2, width=10, font=self.fonte)
        self.txtidcliente.pack(side=LEFT)
        self.btnBuscarCliente = Button(self.container2, text="Buscar", font=self.fonte, width=10, command=self.buscarCliente)
        self.btnBuscarCliente.pack(side=RIGHT)

        self.lblnomecliente = Label(self.container3, text="Nome:", font=self.fonte, width=10)
        self.lblnomecliente.pack(side=LEFT)
        self.txtnomecliente = Entry(self.container3, width=25, font=self.fonte)
        self.txtnomecliente.pack(side=LEFT)

        self.lbltelefonecliente = Label(self.container4, text="Telefone:", font=self.fonte, width=10)
        self.lbltelefonecliente.pack(side=LEFT)
        self.txttelefonecliente = Entry(self.container4, width=25, font=self.fonte)
        self.txttelefonecliente.pack(side=LEFT)

        self.lblenderecocliente = Label(self.container5, text="Endereço:", font=self.fonte, width=10)
        self.lblenderecocliente.pack(side=LEFT)
        self.txtenderecocliente = Entry(self.container5, width=25, font=self.fonte)
        self.txtenderecocliente.pack(side=LEFT)

        self.lblcpfcliente = Label(self.container10, text="CPF:", font=self.fonte, width=10)
        self.lblcpfcliente.pack(side=LEFT)
        self.txtcpfcliente = Entry(self.container10, width=25, font=self.fonte)
        self.txtcpfcliente.pack(side=LEFT)

        self.lblcidadecliente = Label(self.container11, text="Cidade:", font=self.fonte, width=10)
        self.lblcidadecliente.pack(side=LEFT)
        self.txtcidadecliente = Entry(self.container11, width=25, font=self.fonte)
        self.txtcidadecliente.pack(side=LEFT)

        self.bntInsertCliente = Button(self.container8, text="Inserir", font=self.fonte, width=12, command=self.inserirCliente)
        self.bntInsertCliente.pack(side=LEFT)
        self.bntAlterarCliente = Button(self.container8, text="Alterar", font=self.fonte, width=12, command=self.alterarCliente)
        self.bntAlterarCliente.pack(side=LEFT)
        self.bntExcluirCliente = Button(self.container8, text="Excluir", font=self.fonte, width=12, command=self.excluirCliente)
        self.bntExcluirCliente.pack(side=LEFT)

        self.lblmsgCliente = Label(self.container9, text="", font=("Verdana", "9", "italic"))
        self.lblmsgCliente.pack()

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

    def inserirCidade(self):
        cidade = Cidades(nome=self.txtnomecidade.get(), estado=self.txtestado.get())
        self.lblmsgCidade["text"] = cidade.insertCidade()
        self.limparCamposCidade()

    def alterarCidade(self):
        cidade = Cidades(idcidade=self.txtidcidade.get(), nome=self.txtnomecidade.get(), estado=self.txtestado.get())
        self.lblmsgCidade["text"] = cidade.updateCidade()
        self.limparCamposCidade()

    def excluirCidade(self):
        cidade = Cidades(idcidade=self.txtidcidade.get())
        self.lblmsgCidade["text"] = cidade.deleteCidade()
        self.limparCamposCidade()

    def buscarCidade(self):
        cidade = Cidades()
        idcidade = self.txtidcidade.get()
        self.lblmsgCidade["text"] = cidade.selectCidade(idcidade)
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

    def inserirCliente(self):
        cliente = Clientes(nome=self.txtnomecliente.get(), telefone=self.txttelefonecliente.get(), endereco=self.txtenderecocliente.get(), cpf=self.txtcpfcliente.get(), cidade=self.txtcidadecliente.get())
        self.lblmsgCliente["text"] = cliente.insertCliente()
        self.limparCamposCliente()

    def alterarCliente(self):
        cliente = Clientes(idcliente=self.txtidcliente.get(), nome=self.txtnomecliente.get(), telefone=self.txttelefonecliente.get(), endereco=self.txtenderecocliente.get(), cpf=self.txtcpfcliente.get(), cidade=self.txtcidadecliente.get())
        self.lblmsgCliente["text"] = cliente.updateCliente()
        self.limparCamposCliente()

    def excluirCliente(self):
        cliente = Clientes(idcliente=self.txtidcliente.get())
        self.lblmsgCliente["text"] = cliente.deleteCliente()
        self.limparCamposCliente()

    def buscarCliente(self):
        cliente = Clientes()
        idcliente = self.txtidcliente.get()
        self.lblmsgCliente["text"] = cliente.selectCliente(idcliente)
        if cliente.idcliente:
            self.txtidcliente.delete(0, END)
            self.txtidcliente.insert(INSERT, cliente.idcliente)
            self.txtnomecliente.delete(0, END)
            self.txtnomecliente.insert(INSERT, cliente.nome)
            self.txttelefonecliente.delete(0, END)
            self.txttelefonecliente.insert(INSERT, cliente.telefone)
            self.txtenderecocliente.delete(0, END)
            self.txtenderecocliente.insert(INSERT, cliente.endereco)
            self.txtcpfcliente.delete(0, END)
            self.txtcpfcliente.insert(INSERT, cliente.cpf)
            self.txtcidadecliente.delete(0, END)
            self.txtcidadecliente.insert(INSERT, cliente.cidade)

    def limparCamposCliente(self):
        self.txtidcliente.delete(0, END)
        self.txtnomecliente.delete(0, END)
        self.txttelefonecliente.delete(0, END)
        self.txtenderecocliente.delete(0, END)
        self.txtcpfcliente.delete(0, END)
        self.txtcidadecliente.delete(0, END)

if __name__ == "__main__":
    root = Tk()
    app = Application(master=root)
    root.mainloop()