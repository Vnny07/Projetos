from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from Banco import Banco
import sqlite3

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

class ClientesApp:
    def __init__(self, master=None):
        self.master = master
        self.master.title('Cadastro de Clientes')
        self.master.geometry('350x350')

        self.fonte = ("Verdana", "8")

        self.container1 = Frame(self.master, pady=10)
        self.container1.pack()

        self.container2 = Frame(self.master, padx=20, pady=5)
        self.container2.pack()

        self.container3 = Frame(self.master, padx=20, pady=5)
        self.container3.pack()

        self.container4 = Frame(self.master, padx=20, pady=5)
        self.container4.pack()

        self.container5 = Frame(self.master, padx=20, pady=5)
        self.container5.pack()

        self.container10 = Frame(self.master, padx=20, pady=5)
        self.container10.pack()

        self.container11 = Frame(self.master, padx=20, pady=5)
        self.container11.pack()

        self.container6 = Frame(self.master, padx=20, pady=5)
        self.container6.pack()

        self.container7 = Frame(self.master, padx=20, pady=5)
        self.container7.pack()

        self.container8 = Frame(self.master, padx=20, pady=10)
        self.container8.pack()

        self.container9 = Frame(self.master, pady=15)
        self.container9.pack()

        self.titulo = Label(self.container1, text="Informe os dados:", font=("Calibri", "9", "bold"))
        self.titulo.pack()

        self.lblidcliente = Label(self.container2, text="Código:", font=self.fonte, width=10)
        self.lblidcliente.pack(side=LEFT)
        self.txtidcliente = Entry(self.container2, width=10, font=self.fonte)
        self.txtidcliente.pack(side=LEFT)
        self.btnBuscarCliente = Button(self.container2, text="Buscar", font=self.fonte, width=10,
                                       command=self.buscarCliente)
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
        self.cmbcidadecliente = ttk.Combobox(self.container11, width=23, font=self.fonte)
        self.cmbcidadecliente.pack(side=LEFT)
        self.mostrarcidades()

        self.bntInsertCliente = Button(self.container8, text="Inserir", font=self.fonte, width=12,
                                       command=self.inserirCliente)
        self.bntInsertCliente.pack(side=LEFT)
        self.bntAlterarCliente = Button(self.container8, text="Alterar", font=self.fonte, width=12,
                                        command=self.alterarCliente)
        self.bntAlterarCliente.pack(side=LEFT)
        self.bntExcluirCliente = Button(self.container8, text="Excluir", font=self.fonte, width=12,
                                        command=self.excluirCliente)
        self.bntExcluirCliente.pack(side=LEFT)

        self.lblmsgCliente = Label(self.container9, text="", font=("Verdana", "9", "italic"))
        self.lblmsgCliente.pack()

    def mostrarcidades(self):
        banco = None
        try:
            banco = Banco()
            conn = banco.conexao

            cursor = conn.cursor()

            cursor.execute("SELECT nome FROM cidades")

            cidades = cursor.fetchall()

            self.cmbcidadecliente['values'] = []

            for cidade in cidades:
                self.cmbcidadecliente['values'] = (*self.cmbcidadecliente['values'], cidade[0])

        except sqlite3.Error as e:
            print(f"Erro ao buscar as cidades: {e}")

        finally:
            if banco:
                banco.close()

    def inserirCliente(self):
        cliente = Clientes(nome=self.txtnomecliente.get(), telefone=self.txttelefonecliente.get(), endereco=self.txtenderecocliente.get(), cpf=self.txtcpfcliente.get(), cidade=self.cmbcidadecliente.get())
        self.lblmsgCliente["text"] = cliente.insertCliente()
        self.limparCamposCliente()

    def alterarCliente(self):
        cliente = Clientes(idcliente=self.txtidcliente.get(), nome=self.txtnomecliente.get(), telefone=self.txttelefonecliente.get(), endereco=self.txtenderecocliente.get(), cpf=self.txtcpfcliente.get(), cidade=self.cmbcidadecliente.get())
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
            self.cmbcidadecliente.set(cliente.cidade)

    def limparCamposCliente(self):
        self.txtidcliente.delete(0, END)
        self.txtnomecliente.delete(0, END)
        self.txttelefonecliente.delete(0, END)
        self.txtenderecocliente.delete(0, END)
        self.txtcpfcliente.delete(0, END)
        self.cmbcidadecliente.set('')

if __name__ == "__main__":
    root = Tk()
    app = ClientesApp(master=root)
    root.mainloop()