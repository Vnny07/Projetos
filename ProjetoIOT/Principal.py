import tkinter as tk
from tkinter import PhotoImage
from Ajuda import abrir_ajuda
from Fluxo import abrir_fluxo
from Historico import abrir_historico

def centralizar_janela(janela, largura, altura):
    tela_largura = janela.winfo_screenwidth()
    tela_altura = janela.winfo_screenheight()

    pos_x = (tela_largura // 2) - (largura // 2)
    pos_y = (tela_altura // 2) - (altura // 2)

    janela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")

root = tk.Tk()
root.title("Iniciador")
root.configure(bg='black')

centralizar_janela(root, 415, 350)

root.iconbitmap(r"9087035.ico")

title_image = PhotoImage(file=r"Titulo.png")
title_label = tk.Label(root, image=title_image, bg='black')
title_label.pack(pady=20)

button_frame = tk.Frame(root, bg='black')
button_frame.pack(pady=20)

button_width = 30

ver_fluxo_button = tk.Button(
    button_frame,
    text="Exibir Fluxo Atual",
    font=("Arial", 16),
    fg="#ADD8E6",
    bg='black',
    borderwidth=2,
    relief='raised',
    width=button_width,
    command=abrir_fluxo
)
ver_fluxo_button.pack(pady=10)

ver_historico_button = tk.Button(
    button_frame,
    text="Exibir Histórico de Consumo",
    font=("Arial", 16),
    fg="#ADD8E6",
    bg='black',
    borderwidth=2,
    relief='raised',
    width=button_width,
    command=abrir_historico
)
ver_historico_button.pack(pady=10)

help_button = tk.Button(
    root,
    text="Ajuda",
    font=("Arial", 10),
    fg="#ADD8E6",
    bg='black',
    borderwidth=2,
    relief='raised',
    command=abrir_ajuda
)
help_button.pack(side=tk.BOTTOM, pady=10)

root.mainloop()