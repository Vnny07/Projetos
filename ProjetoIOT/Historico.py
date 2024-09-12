import tkinter as tk
from tkinter import PhotoImage

def abrir_historico():
    historico_window = tk.Toplevel()
    historico_window.title("Histórico")
    historico_window.configure(bg='black')

    def centralizar_janela(janela, largura, altura):
        tela_largura = janela.winfo_screenwidth()
        tela_altura = janela.winfo_screenheight()
        pos_x = (tela_largura // 2) - (largura // 2)
        pos_y = (tela_altura // 2) - (altura // 2)
        janela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")

    centralizar_janela(historico_window, 500, 300)

    historico_window.iconbitmap(r"9087035.ico")

    title_image = PhotoImage(file=r"Titulo3.png")
    title_label = tk.Label(historico_window, image=title_image, bg='black')
    title_label.image = title_image
    title_label.pack(pady=20)

    main_frame = tk.Frame(historico_window, bg='black')
    main_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

    def criar_linha(label_text):
        linha_frame = tk.Frame(main_frame, bg='black')
        linha_frame.pack(pady=5)

        label = tk.Label(linha_frame, text=label_text, font=("Arial", 14), fg="#ADD8E6", bg='black')
        label.pack(side=tk.LEFT, padx=(20, 5))

        entry = tk.Entry(linha_frame, font=("Arial", 14), fg="#ADD8E6", bg='black', borderwidth=2, relief='raised', width=20, state='readonly')
        entry.pack(side=tk.LEFT, padx=5)

        return entry

    consumo_entry = criar_linha("Consumo Total:")
    pico_entry = criar_linha("Pico de Consumo:")
    vazamentos_entry = criar_linha("Vazamentos Detectados:")
    litros_entry = criar_linha("Litros Economizados:")

    historico_window.mainloop()