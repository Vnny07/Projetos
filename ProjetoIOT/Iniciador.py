import tkinter as tk
import subprocess
import urllib.request

def verificar_conexao(url="http://www.google.com"):
    try:
        urllib.request.urlopen(url, timeout=5)
        return True
    except urllib.request.URLError:
        return False

def janela_conexao():
    janela_conexao = tk.Toplevel()
    janela_conexao.title("Iniciando")
    janela_conexao.geometry("250x65")
    janela_conexao.iconbitmap("Icon.ico")
    janela_conexao.resizable(False, False)

    label_status = tk.Label(janela_conexao, text="Conectando...", font=("Arial", 12))
    label_status.pack(pady=20)

    conectado = verificar_conexao()

    if conectado:
        label_status.config(text="Conexão bem-sucedida!")
        janela_conexao.after(1500, lambda: subprocess.Popen(['python', 'Principal.py']))
        janela_conexao.after(1500, janela_conexao.destroy)
    else:
        label_status.config(text="Não foi possível conectar.")
        janela_conexao.after(3000, janela_conexao.destroy)

    janela_conexao.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    janela_conexao()