# componentes 
# tk: Tk() janela
# lb: Label() rotulo
# bt: Button() botao
# et: entry() caixa de texto

import tkinter as tk
from tkinter import messagebox



def saudar_usuario():
    nome = campo_nome.get()
    
    if nome == "":
        messagebox.showwarning("Aviso", "Por favor", "digite seu nome!")
    else:
        messagebox.showinfo("Saudações Alunos!", f"olá, {nome}! Seja bem-vindo ao mundo das interfaces gráficas!")
        
app = tk.Tk()
app.title = ("exemplo 1")
app.geometry("350x200")


campo_nome = tk.Entry(app, font=("Arial", 14, "bold"))
btn_saudar = tk.Button(app, text="Saudar", font=("Arial", 14, "bold"), bg="#e5ff00", command=saudar_usuario,)

campo_nome.pack(pady=20)
btn_saudar.pack(pady=20)

app.mainloop()
   