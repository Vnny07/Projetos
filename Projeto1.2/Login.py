import tkinter as tk
from tkinter import messagebox
import sqlite3
from Menu import MenuApp
from Usuarios import UsuariosApp

# E-MAIL E SENHA PARA O LOGIN -> vinicius@email.com | 123456

class LoginApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Entrar")
        self.master.geometry("300x210")

        label = tk.Label(master, text="Efetue o login", font=("Arial", 24, "bold"))
        label.pack(pady=10)

        frame = tk.Frame(master)
        frame.pack(pady=10)

        self.label_email = tk.Label(frame, text="E-mail:")
        self.label_email.grid(row=0, column=0, padx=5, pady=5)

        self.entry_email = tk.Entry(frame)
        self.entry_email.grid(row=0, column=1, padx=5, pady=5)

        self.label_senha = tk.Label(frame, text="Senha:")
        self.label_senha.grid(row=1, column=0, padx=5, pady=5)

        self.entry_senha = tk.Entry(frame, show="*")
        self.entry_senha.grid(row=1, column=1, padx=5, pady=5)

        button_frame = tk.Frame(master)
        button_frame.pack(pady=10)

        self.login_button = tk.Button(button_frame, text="Login", command=self.fazer_login)
        self.login_button.grid(row=0, column=0, padx=5)

        self.cadastro_button = tk.Button(button_frame, text="Cadastrar", command=self.abrir_cadastro_usuarios)
        self.cadastro_button.grid(row=0, column=1, padx=5)

    def abrir_cadastro_usuarios(self):
        janela_usuarios = tk.Toplevel()
        app = UsuariosApp(janela_usuarios)
        janela_usuarios.mainloop()

    def fazer_login(self):
        email = self.entry_email.get()
        senha = self.entry_senha.get()

        conn = sqlite3.connect('banco.db')
        c = conn.cursor()

        c.execute("SELECT * FROM usuarios WHERE email = ? AND senha = ?", (email, senha))
        usuario = c.fetchone()

        if usuario:
            messagebox.showinfo("Sucesso", "Login efetuado com sucesso!")
            self.master.destroy()
            self.abrir_menu()
        else:
            messagebox.showerror("Erro", "E-mail ou senha incorretos!")

        conn.close()

    def abrir_menu(self):
        menu_root = tk.Tk()
        app = MenuApp(menu_root)
        menu_root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()