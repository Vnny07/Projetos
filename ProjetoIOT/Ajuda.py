import tkinter as tk

def janela_ajuda():
    janela_ajuda = tk.Toplevel()
    janela_ajuda.title("Ajuda")
    janela_ajuda.geometry("350x300")
    janela_ajuda.resizable(False, False)
    janela_ajuda.iconbitmap("Icon.ico")

    frame_texto = tk.Frame(janela_ajuda)
    frame_texto.pack(expand=True, fill="both")

    label_texto = tk.Label(frame_texto, text=(
        "Controle de Água Residencial\n\n"
        "Monitoramento em Tempo Real:\n"
        "- Acompanhe o fluxo de água em tempo real e\n"
        "  fique de olho no uso da água em casa.\n\n"
        "Histórico de Consumo:\n"
        "- Consulte os dados detalhados do seu consumo\n"
        "  e tenha controle total sobre a economia.\n\n"
        "Limite de Consumo:\n"
        "- Configure alertas personalizados para evitar\n"
        "  desperdícios e manter o uso sustentável.\n\n"
        "Precisa de mais ajuda? Fale com o suporte:\n"
        "suportecontroleagua@gmail.com"
    ), justify="center", padx=10, pady=10, font=("Arial", 10))

    label_texto.pack(expand=True, fill="both")

    janela_ajuda.mainloop()