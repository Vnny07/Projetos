import tkinter as tk
from tkinter import ttk

def janela_historico():
    janela_historico = tk.Toplevel()
    janela_historico.title("Histórico de Consumo")
    janela_historico.geometry("500x400")
    janela_historico.resizable(False, False)
    janela_historico.iconbitmap("ICO1.ico")

    colunas = ("data", "hora", "volume")
    tabela_historico = ttk.Treeview(janela_historico, columns=colunas, show="headings")

    tabela_historico.heading("data", text="Data")
    tabela_historico.heading("hora", text="Hora")
    tabela_historico.heading("volume", text="Volume de Água (L)")

    tabela_historico.column("data", width=150)
    tabela_historico.column("hora", width=100)
    tabela_historico.column("volume", width=150)

    tabela_historico.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    janela_historico()
    root.mainloop()