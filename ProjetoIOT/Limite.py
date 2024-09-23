import tkinter as tk
import tkinter.messagebox as messagebox
import os

if 'Iniciador' not in os.environ:
    tk.messagebox.showerror("Erro", "Ocorreu um erro durante a execução do programa.")
    exit()

limite_aplicado = False

def janela_limite():
    def fechar_janela():
        if not limite_aplicado:
            resposta = messagebox.askquestion("Sair", "Algumas alterações não foram aplicadas.\n"
                                                   "Deseja sair mesmo assim?")
            if resposta == "yes":
                janela_limite.destroy()
        else:
            janela_limite.destroy()

    janela_limite = tk.Toplevel()
    janela_limite.title("Limite de Consumo")
    janela_limite.geometry("250x125")
    janela_limite.iconbitmap("ICO1.ico")
    janela_limite.resizable(False, False)

    label_limite = tk.Label(janela_limite, text="Defina o limite de consumo (L):")
    label_limite.pack(pady=10)

    entrada_limite = tk.Entry(janela_limite, width=20)
    entrada_limite.pack(pady=5)

    frame_botoes = tk.Frame(janela_limite)
    frame_botoes.pack(pady=5)

    btn_aplicar = tk.Button(frame_botoes, text="Aplicar", width=10)
    btn_aplicar.pack(side=tk.LEFT, padx=5)

    btn_ok = tk.Button(frame_botoes, text="OK", width=10, command=fechar_janela)
    btn_ok.pack(side=tk.LEFT, padx=5)

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    janela_limite()
    root.mainloop()