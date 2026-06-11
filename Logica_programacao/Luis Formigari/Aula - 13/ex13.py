#Exercício - Crie uma aplicação que faça o cálculo de idade de pessoas
# Deve pergntar o nome da pessoa e o ano de nascimento

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


# Criação de interface
janela = tk.Tk()
janela.title("Calculo de idade")
janela.geometry("900x400")
janela.configure(bg="Black")

# Variáveis Globais
nome = ""
ano_nascimento = ""


# Função calcular idade
def CalcularIdade():
    global nome
    global ano_nascimento
    
    nome = ent_nome.get()
    ano_nascimento = int(com_ano.get())
    
    pontuacao = 0
    
    if nome == "":
        messagebox.showerror("Erro!", "Porfavor digite o seu nome!")
        pontuacao =+1
    if ano_nascimento == "":
        messagebox.showerror("Erro!", "Porfavor digite o ano de nascimento!")
        pontuacao =+1
        
    if pontuacao > 0:
        print("Verificado e possuí algo nulo, erros já enviados!")
    else:
        idade = 2026 - ano_nascimento
        text = f"Olá {nome}\nVocê tem {idade} anos!"
        messagebox.showinfo("Message", text)
        

        


# Criação de Labels
lbl_nome = tk.Label(janela, font=("Ariel", 20), bg="black", fg="white", text="Digite seu Nome:")
lbl_idade = tk.Label(janela, font=("Ariel", 20), bg="black", fg="white", text="Selecione seu ano de Nascimento:")

# Entry
ent_nome = tk.Entry(janela, font=("Ariel", 20), bg="grey", fg="white")

# Criação de Buttons
button_Close = tk.Button(janela, font=("Arial", 24), fg="White", bg="#f38ba8", text="Fechar", command=janela.destroy)
btn_calcular = tk.Button(janela, font=("Ariel", 20), bg="gray", fg="white", text="Calcular Idade", command=CalcularIdade)

# Combo box
## Lista de opções
opcoes = [
    "2025", "2024", "2023", "2022", "2021", "2020", "2019", "2018", "2017", "2016", 
    "2015", "2014", "2013", "2012", "2011", "2010", "2009", "2008", "2007", "2006", 
    "2005", "2004", "2003", "2002", "2001", "2000", "1999", "1998", "1997", "1996", 
    "1995", "1994", "1993", "1992", "1991", "1990", "1889", "1988", "1987", "1986", 
    "1985", "1984", "1983", "1982", "1981", "1980", "1979", "1978", "1977", "1976", 
    "1975", "1974", "1973", "1972", "1971", "1970"
]

## Style
style = ttk.Style()
style.theme_use('clam')

style.configure("Custom.TCombobox",
                fieldbackground="gray",  
                background="gray",       
                foreground="White")

com_ano = ttk.Combobox(janela, values=opcoes, font=("Arial", 14), style="Custom.TCombobox")


# Gerando o Grid
lbl_nome.grid(row=0, column=0, pady=30, padx=10)
lbl_idade.grid(row=1, column=0, padx=30, pady=10)

ent_nome.grid(row=0, column=1, padx=30, pady=10)

com_ano.grid(row=1, column=1, padx=30, pady=10)

btn_calcular.grid(row=2, column=1, padx=30, pady=10)
button_Close.grid(row=2, column=0, padx=30, pady=10)




janela.mainloop()