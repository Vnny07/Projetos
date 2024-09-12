import tkinter as tk
from tkinter import PhotoImage

def abrir_fluxo():
    fluxo_window = tk.Toplevel()
    fluxo_window.title("Fluxo")
    fluxo_window.configure(bg='black')

    def centralizar_janela(janela, largura, altura):
        tela_largura = janela.winfo_screenwidth()
        tela_altura = janela.winfo_screenheight()
        pos_x = (tela_largura // 2) - (largura // 2)
        pos_y = (tela_altura // 2) - (altura // 2)
        janela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")

    centralizar_janela(fluxo_window, 400, 225)

    fluxo_window.iconbitmap(r"9087035.ico")

    title_image = PhotoImage(file=r"Titulo2.png")
    title_label = tk.Label(fluxo_window, image=title_image, bg='black')
    title_label.image = title_image
    title_label.pack(pady=20)

    texto_frame = tk.Frame(fluxo_window, bg='black')
    texto_frame.pack(pady=20)

    fluxo_label = tk.Label(texto_frame, text="Fluxo:", font=("Arial", 14), fg="#ADD8E6", bg='black')
    fluxo_label.pack(side=tk.LEFT, padx=(20, 5))

    fluxo_text = tk.Entry(texto_frame, font=("Arial", 14), fg="#ADD8E6", bg='black', borderwidth=2, relief='raised', width=10, state='readonly')
    fluxo_text.pack(side=tk.LEFT, padx=5)

    unidade_label = tk.Label(texto_frame, text="L/min", font=("Arial", 14), fg="#ADD8E6", bg='black')
    unidade_label.pack(side=tk.LEFT, padx=(5, 20))

    atualizar_button = tk.Button(fluxo_window, text="Atualizar", font=("Arial", 14), fg="#ADD8E6", bg='black', borderwidth=2, relief='raised')
    atualizar_button.pack(pady=10)

    fluxo_window.mainloop()