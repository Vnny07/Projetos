import tkinter as tk

def janela_fluxo():
    janela_fluxo = tk.Toplevel()
    janela_fluxo.title("Fluxo Atual")
    janela_fluxo.geometry("270x100")
    janela_fluxo.resizable(False, False)
    janela_fluxo.iconbitmap("ICO1.ico")

    frame_fluxo = tk.Frame(janela_fluxo)
    frame_fluxo.pack(expand=True, fill="both", padx=10, pady=10)

    label_fluxo = tk.Label(frame_fluxo, text="Fluxo:", font=("Arial", 10))
    label_fluxo.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    caixa_fluxo = tk.Entry(frame_fluxo, width=15, font=("Arial", 12), state=tk.DISABLED, readonlybackground="white")
    caixa_fluxo.grid(row=0, column=1, padx=5, pady=5)

    label_unidade = tk.Label(frame_fluxo, text="L/min", font=("Arial", 10))
    label_unidade.grid(row=0, column=2, padx=5, pady=5, sticky="w")

    btn_atualizar = tk.Button(janela_fluxo, text="Atualizar", font=("Arial", 9))
    btn_atualizar.pack(side="bottom", pady=10)

    janela_fluxo.mainloop()