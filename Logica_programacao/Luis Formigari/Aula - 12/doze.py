# componentes 
# tk: Tk() janela
# lb: Label() rotulo
# bt: Button() botao
# et: entry() caixa de texto

import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
janela.title("Minha primeira janela GUI")
janela.geometry("400x200")


usuario = ""

def mostrar_mensagem():
    messagebox.showinfo("Sucesso!",  "Você clicou no botão!!!!!!!!!!!!!!!")
    
lbl_67 = tk.Label(janela, text="Bem-vindo a nossa aula de Tkinter", font=("Arial", 14, "bold"))
btn_67 = tk.Button(janela, text="Clique Aqui!", font=("Arial", 14, "bold"), bg="#2ecc71", fg="white", command=mostrar_mensagem)
btn_close = tk.Button(janela, text="Fechar", font=("Arial", 14, "bold"), bg="#cc2e2e", command=janela.destroy)


lbl_67.pack(pady=20)
btn_67.pack(padx=20)
btn_close.pack(pady=20)



janela.mainloop()