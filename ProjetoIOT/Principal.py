import tkinter as tk
import Ajuda
import Fluxo
import Limite
import Historico

def abrir_ajuda():
    Ajuda.janela_ajuda()

def abrir_fluxo():
    Fluxo.janela_fluxo()

def abrir_limite():
    Limite.janela_limite()

def abrir_historico():
    Historico.janela_historico()

janela = tk.Tk()
janela.title("Controle de Água")
janela.geometry("275x305")
janela.resizable(False, False)

imagem = tk.PhotoImage(file="Img.png")
janela.iconbitmap("Icon.ico")

label_imagem = tk.Label(janela, image=imagem)
label_imagem.pack(pady=10)

btn_fluxo = tk.Button(janela, text="Fluxo Atual", width=20, command=abrir_fluxo)
btn_fluxo.pack(pady=5)

btn_historico = tk.Button(janela, text="Histórico de Consumo", width=20, command=abrir_historico)
btn_historico.pack(pady=5)

btn_limite = tk.Button(janela, text="Limite de Consumo", width=20, command=abrir_limite)
btn_limite.pack(pady=5)

btn_ajuda = tk.Button(janela, text="Ajuda", width=10, font=("Arial", 8), command=abrir_ajuda)
btn_ajuda.pack(pady=5)

janela.mainloop()