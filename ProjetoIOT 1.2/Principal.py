import tkinter as tk

def on_button_click():
    pass

janela = tk.Tk()
janela.title("Controle de Água")
janela.geometry("325x525")

janela.iconbitmap("ICO1.ico")

janela.resizable(False, False)

img1 = tk.PhotoImage(file="ICO2.png")
img2 = tk.PhotoImage(file="ICO3.png")

small_font = ("Arial", 8, "bold")

label_codigo = tk.Label(janela, text="Código: 002", font=small_font)
label_codigo.pack(anchor='w', padx=(10, 0), pady=(10, 0))

label_mac = tk.Label(janela, text="MAC: 23:45:67:89:01:1", font=small_font)
label_mac.pack(anchor='w', padx=(10, 0), pady=(5, 0))

label_descricao = tk.Label(janela, text="Descrição: teste 02", font=small_font)
label_descricao.pack(anchor='w', padx=(10, 0), pady=(5, 0))

frame_botoes = tk.Frame(janela)
frame_botoes.pack(side='top', anchor='e', pady=(10, 0))

button_img1 = tk.Button(frame_botoes, image=img1, borderwidth=0, command=on_button_click, cursor="hand2")
button_img1.pack(side='left', padx=(0, 5))

button_img2 = tk.Button(frame_botoes, image=img2, borderwidth=0, command=on_button_click, cursor="hand2")
button_img2.pack(side='left', padx=(5, 10))

label_dia = tk.Label(janela, text="Consumo do dia atual:           0L", font=small_font)
label_dia.pack(anchor='w', padx=(10, 0), pady=(10, 0))

label_mes_atual = tk.Label(janela, text="Consumo do mês atual:         0L", font=small_font)
label_mes_atual.pack(anchor='w', padx=(10, 0), pady=(5, 0))

label_mes_anterior = tk.Label(janela, text="Consumo do mês anterior:    0L", font=small_font)
label_mes_anterior.pack(anchor='w', padx=(10, 0), pady=(5, 0))

label_vazia = tk.Label(janela, text="", font=small_font)
label_vazia.pack(pady=(5, 0))

label_custo_dia = tk.Label(janela, text="Custo do dia atual:             R$0.0", font=small_font)
label_custo_dia.pack(anchor='w', padx=(10, 0), pady=(10, 0))

label_custo_mes_atual = tk.Label(janela, text="Custo do mês atual:            R$0.0", font=small_font)
label_custo_mes_atual.pack(anchor='w', padx=(10, 0), pady=(5, 0))

label_custo_mes_anterior = tk.Label(janela, text="Custo do mês anterior:        R$0.0", font=small_font)
label_custo_mes_anterior.pack(anchor='w', padx=(10, 0), pady=(5, 0))

janela.mainloop()