import tkinter as tk
from Cidades import CidadesApp
from Clientes import ClientesApp
from Usuarios import UsuariosApp

def MenuApp(root):
    root.geometry("400x300")
    root.title("Cadastro")

    label = tk.Label(root, text="Menu principal", font=("Arial", 24, "bold"))
    label.pack(pady=20)

    def abrir_cadastro_cidades():
        janela_cidades = tk.Toplevel()
        app = CidadesApp(janela_cidades)
        janela_cidades.mainloop()

    def abrir_cadastro_clientes():
        janela_clientes = tk.Toplevel()
        app = ClientesApp(janela_clientes)
        janela_clientes.mainloop()

    def abrir_cadastro_usuarios():
        janela_usuarios = tk.Toplevel()
        app = UsuariosApp(janela_usuarios)
        janela_usuarios.mainloop()

    button_frame = tk.Frame(root)

    button1 = tk.Button(button_frame, text="Usuários", width=20, command=abrir_cadastro_usuarios)
    button1.pack(pady=10)

    button2 = tk.Button(button_frame, text="Cidades", width=20, command=abrir_cadastro_cidades)
    button2.pack(pady=10)

    button3 = tk.Button(button_frame, text="Clientes", width=20, command=abrir_cadastro_clientes)
    button3.pack(pady=10)

    button_frame.pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    MenuApp(root)
    root.mainloop()