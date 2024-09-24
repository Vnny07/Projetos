import tkinter as tk
import subprocess
import urllib.request
import sys
import os

os.environ['Iniciador'] = '1'

def verificar_conexao(url="http://www.google.com"):
    try:
        urllib.request.urlopen(url, timeout=5)
        return True
    except urllib.request.URLError:
        return False

def atualizar_status_conexao(label_status):
    conectado = verificar_conexao()

    if conectado:
        label_status.config(text="Conexão bem-sucedida!")
        label_status.after(1500, lambda: subprocess.Popen(['python', 'Principal.py']))
        label_status.after(1500, lambda: janela_conexao.master.destroy())
    else:
        label_status.after(3000, lambda: label_status.config(text="Não foi possível conectar 🙁"))
        label_status.after(5000, lambda: atualizar_status_conexao(label_status))

def janela_conexao():
    global janela_conexao
    janela_conexao = tk.Toplevel()
    janela_conexao.title("Iniciador")
    janela_conexao.geometry("250x65")
    janela_conexao.iconbitmap("ICO1.ico")
    janela_conexao.resizable(False, False)

    label_status = tk.Label(janela_conexao, text="Conectando...", font=("Arial", 12))
    label_status.pack(pady=20)

    janela_conexao.after(2000, lambda: atualizar_status_conexao(label_status))

    janela_conexao.protocol("WM_DELETE_WINDOW", lambda: sys.exit())
    janela_conexao.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    janela_conexao()