# revisão tkinter

## Bruno: 


# Imports

import tkinter as tk    
from tkinter import messagebox
from tkinter import ttk

## Váriaveis Globais.

NomeGlobal = ""
SesiGlobal = ""
EmGlobal = ""
Usuario = False

def Cadastrar():
    
    global NomeGlobal
    global SesiGlobal
    global EmGlobal  
    global Usuario 
    
    
    
    
    
    
    nome = ent_usuario.get()
    sesi = ent_sesi.get()
    Em = com_Em.get()
    
    pontuacao = 0
    
    if nome == "":
        pontuacao=+1
    
    if sesi == "":
        pontuacao=+1
        
    if Em == "":
        pontuacao=+1

    if pontuacao > 0:
        messagebox.showwarning("nome ou sesi vazio", "porfavor, digite um nome, seu sesi e seu ano")
    else:
        Usuario = True
        NomeGlobal = nome
        SesiGlobal = sesi
        EmGlobal = Em
        
        
        
        
        texto = f"Olá: {nome}\nVocê estuda no SESI: {sesi}\nNo ano: {Em}"
        messagebox.showinfo("Mensagem", texto)
        
    ent_usuario.delete(0, tk.END)
    ent_sesi.delete(0, tk.END)
    com_Em.set("")
    
def VerificarUsuario():
    global NomeGlobal
    global SesiGlobal
    global EmGlobal  
    global Usuario 
    
    if Usuario == True:
        texto = f"Olá: {NomeGlobal}\nVocê estuda no SESI: {SesiGlobal}\nNo ano: {EmGlobal}"
        messagebox.showinfo("Mensagem", texto)
    else:
        messagebox.showerror("error", "Nenhum Usuário Cadastrado!")
    


    

# 0 - Etapa Janela

janela = tk.Tk()
janela.title("Revisão Tkinter")
janela.geometry("900x400")
janela.configure(bg="Black")

#  1 - Etapa Componentes 
## Labels = Rótulos ou 'print'

lbl_usuario = tk.Label(janela, text="Digite o nome de Uusário:", font=("Arial", 20), fg="White", bg="Black")
lbl_sesi = tk.Label(janela, text="Digite o seu SESI:", font=("Arial", 20), fg="White", bg="Black")
lbl_EM = tk.Label(janela, font=("Arial", 20), fg="White", bg="Black", text="Selecione seu Ano:")

# 1.1 - Entry
ent_usuario = tk.Entry(janela, font=("Arial", 14), fg="White", bg="gray")
ent_sesi = tk.Entry(janela, font=("Arial", 14), fg="White", bg="gray")


# 1.2 - Button
button_print = tk.Button(janela, font=("Arial", 20), fg="White", bg="Gray", text="Verificar Usuário", command=VerificarUsuario)
button_SPrint = tk.Button(janela, font=("Arial", 20), fg="Black", bg="White", text="Cadastrar", command=Cadastrar)
button_Close = tk.Button(janela, font=("Arial", 24), fg="White", bg="#f38ba8", text="Fechar", command=janela.destroy)

# 1.3 - ComboBox
## Lista de opções
opcoes = ["1EM", "2EM", "3EM"]

## Style
style = ttk.Style()
style.theme_use('clam')

style.configure("Custom.TCombobox",
                fieldbackground="gray",  
                background="gray",       
                foreground="White")




com_Em = ttk.Combobox(janela, values=opcoes, font=("Arial", 14), style="Custom.TCombobox")



# 3 - Carregar label usuário
lbl_usuario.grid(row=0, column=0, padx=20, pady=30)
lbl_sesi.grid(row=1, column=0, padx=20, pady=30)
lbl_EM.grid(row=2, column=0, padx=20, pady=30)

ent_usuario.grid(row=0, column=1, padx=20, pady=10)
ent_sesi.grid(row=1, column=1, padx=20, pady=10)
com_Em.grid(row=2, column=1, padx=20, pady=10)

button_print.grid(row=3, column=0, padx=40, pady=10)
button_SPrint.grid(row=3, column=1, padx=40, pady=10)
button_Close.grid(row=0, column=2, padx=50, pady=10)




# 5 - Carregando a tela Final
janela.mainloop()