import tkinter as tk

def abrir_ajuda():
    ajuda_window = tk.Toplevel()
    ajuda_window.title("Ajuda")
    ajuda_window.configure(bg='black')

    def centralizar_janela(janela, largura, altura):
        tela_largura = janela.winfo_screenwidth()
        tela_altura = janela.winfo_screenheight()
        pos_x = (tela_largura // 2) - (largura // 2)
        pos_y = (tela_altura // 2) - (altura // 2)
        janela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")

    centralizar_janela(ajuda_window, 400, 350)

    ajuda_window.iconbitmap(r"9087035.ico")

    ajuda_texto = (
        "Este programa foi desenvolvido para monitorar e controlar o consumo de água em sua residência.\n\n"
        "Funcionalidades:\n"
        "- Exibir o fluxo de água atual\n"
        "- Visualizar o histórico de consumo\n\n"
        "Para mais informações, consulte a documentação ou entre em contato com o suporte:\n\n"
        "suportecontroleagua@gmail.com"
    )

    ajuda_label = tk.Label(
        ajuda_window,
        text=ajuda_texto,
        font=("Arial", 12),
        fg="#ADD8E6",
        bg='black',
        wraplength=350,
        justify="center",
        padx=20,
        pady=20
    )
    ajuda_label.pack(expand=True, padx=10, pady=10)

    fechar_button = tk.Button(
        ajuda_window,
        text="Fechar",
        font=("Arial", 10),
        fg="#ADD8E6",
        bg='black',
        borderwidth=2,
        relief='raised',
        command=ajuda_window.destroy
    )
    fechar_button.pack(pady=10)