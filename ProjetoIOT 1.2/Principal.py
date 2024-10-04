import tkinter as tk

def on_button_click():
    pass

janela = tk.Tk()
janela.title("Controle de Água")
janela.geometry("325x525")

janela.iconbitmap("ICO1.ico")
janela.resizable(False, False)

bg_img = tk.PhotoImage(file="IMG1.png")
label_bg = tk.Label(janela, image=bg_img)
label_bg.place(relx=0.5, rely=0.8, anchor='center')

img1 = tk.PhotoImage(file="ICO2.png")
img2 = tk.PhotoImage(file="ICO3.png")

small_font = ("Arial", 8, "bold")
img_esquerda = tk.PhotoImage(file="IMG2.png")

frame_info = tk.Frame(janela)
frame_info.pack(anchor='w', padx=(10, 0), pady=(5, 0))

label_img = tk.Label(frame_info, image=img_esquerda)
label_img.grid(row=0, column=0, rowspan=3, padx=(0, 5), pady=(5, 0), sticky="n")

label_codigo = tk.Label(frame_info, text="Código: 002", font=small_font)
label_codigo.grid(row=0, column=1, sticky="w")

label_mac = tk.Label(frame_info, text="MAC: 23:45:67:89:01:1", font=small_font)
label_mac.grid(row=1, column=1, sticky="w")

label_descricao = tk.Label(frame_info, text="Descrição: teste 02", font=small_font)
label_descricao.grid(row=2, column=1, sticky="w")

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

text_box = tk.Text(janela, height=1, width=8, font=("Arial", 10))
text_box.place(relx=0.5, rely=0.74, anchor='center')

text_box.config(state='disabled')

janela.mainloop()