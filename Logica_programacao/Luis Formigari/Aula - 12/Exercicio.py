# componentes 
# tk: Tk() janela
# lb: Label() rotulo
# bt: Button() botao
# et: entry() caixa de texto

#Exercicio: crie uma interace gráfica que calcule a média de três notas digitadas pelo usuário. A interface deve conter campos para o usuário inserir as notas e um botão para calcular a média. Ao clicar no botão, a média deve ser exibida em uma mensagem.

import tkinter as tk
from tkinter import messagebox



def CalcularMedia():
    v1 = int(campo_1.get())
    v2 = int(campo_2.get())
    v3 = int(campo_3.get())
    v4 = (v1 + v2 + v3) / 3
    
    
    if v4 == 0:
        messagebox.showwarning("Aviso", "redigite seus Números! O resultado foi: 0")
    else:
        messagebox.showinfo("Calculado!", f"Aqui está seu resultado: {v4}!")
        
app = tk.Tk()
app.title = ("exemplo 1")
app.geometry("350x350")

lbl_titulo = tk.Label(app, font=("Arial", 14, "bold"), text="Calcule a média a baixo!")
campo_1 = tk.Entry(app, font=("Arial", 14, "bold"))
campo_2 = tk.Entry(app, font=("Arial", 14, "bold"))
campo_3 = tk.Entry(app, font=("Arial", 14, "bold"))
btn_calcular = tk.Button(app, text="Calcular", font=("Arial", 14, "bold"), bg="#00ff22", command=CalcularMedia,)

lbl_titulo.pack(padx=5)
campo_1.pack(pady=20)
campo_2.pack(pady=20)
campo_3.pack(pady=20)
btn_calcular.pack(pady=20)

app.mainloop()
   