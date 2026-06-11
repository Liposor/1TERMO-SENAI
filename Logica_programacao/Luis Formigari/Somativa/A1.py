# Foco: print, input, operações matemáticas e f-strings



import tkinter as tk
from tkinter import messagebox
from tkinter import ttk 
from tkinter import simpledialog
import sys

janela = tk.Tk()
janela.title("Calculo de idade")
janela.geometry("900x400")
janela.configure(bg="Black")

professor vou deixar fora de # propositalmente, para com que você veja mais facilmente, cada questão é só retirar a # utilizei a mesma tela para todas as questões para não
ter que ficar criando varias janelas!


# 1. Registro de Operador: Peça o nome do operador e o turno (A, B ou C). Exiba:
# "Operador [Nome] registrado no Turno [Turno]. Boa jornada!"
# def cadastro():
#     nome = ent_nome.get()
#     turno = turnin.get()
#     pontuacao = 0
#     if nome == "":
#         pontuacao =+1
#     if turno == "":
#         pontuacao =+1
#     if pontuacao > 0:
#         messagebox.showerror("Erro", "Escreva seu nome ou turno")
#     else:
#         texto = f"Operador {nome}, registrado no turno {turno}.\nBoa Jornada!"
#         messagebox.showinfo("Mensagem", texto)
#     ent_nome.delete(0, tk.END)
#     turnin.set("")
    
# #labels
# lbl_titulo = tk.Label(janela, font=("Arial", 30), fg="White", bg="Black", text="Registro de Operador").grid(row=0, column=1, padx=30, pady=10)
# lbl_nome = tk.Label(janela, font=("Arial", 20), fg="White", bg="Black", text="Digite o Nome de Usuário:").grid(row=1, column=0, padx=30, pady=10)
# lbl_turno = tk.Label(janela, font=("Arial", 20 ), fg="White", bg="Black", text="Selecione seu Turno:").grid(row=2, column=0, padx=30, pady=10)
# #entry
# ent_nome = tk.Entry(janela, font=("Arial", 14), fg="black", bg="white")
# opcoes = ["A", "B", "C"]
# turnin = ttk.Combobox(janela, values=opcoes, font=("Arial", 14), style="Custom.TCombobox")
# #button 
# btn_cadastro = tk.Button(janela, font=("Arial", 20), fg="White", bg="gray", command=cadastro, text="Cadastre-se").grid(row=3, column=1, padx=30,pady=10)

# ent_nome.grid(row=1, column=1, padx=30, pady=10)
# turnin.grid(row=2, column=1, padx=30, pady=10)



# 2. Cálculo de Produção: Peça a quantidade de peças produzidas em 1 hora. Calcule e
# exiba quantas peças serão produzidas em um turno de 8 horas.

# def calcular():
#     peças = int(ent_num.get()) * 8

#     if peças == 0:
#         messagebox.showerror("erro", "Digite a quantidade de peças")
#     else:
#         texto = f"Você produz {peças} peças em 8 horas!"
#         messagebox.showinfo("mensagem", texto)


# lbl_Titulo = tk.Label(janela, font=("Arial", 30), fg="White", bg="Black", text="Calculadora de Produção").grid(row=0, column=0, padx=30, pady=10)
# lbl_Num = tk.Label(janela, font=("Arial", 20), bg="black", fg="white", text="Digite quantas peças foram produzidas (1 hora):").grid(row=1, column=0, padx=30,pady=10)
# ent_num = tk.Entry(janela, font=("Arial", 14), bg="White", fg="black")
# ent_num.grid(row=2, column=0, padx=30, pady=10)
# btn_calculo = tk.Button(janela, font=("Arial", 20), bg="gray", fg="white", text="Calcular", command=calcular).grid(row=3, padx=30, pady=0)


# 3. Conversor de Unidade: O sistema lê uma pressão em Bar. Converta para PSI (1 Bar
# ≈ 14.5 PSI) e exiba com duas casas decimais.
# def calcular():
#     psi = float(ent_bar.get()) * 14.5

#     if psi == 0:
#         messagebox.showerror("Erro", "Coloque a quantidade de Bar!")
#     else:
#         texto = f"O Valor em psi é: {psi:.2f}"
#         messagebox.showinfo("Mensagem", texto)

# lbl_titulo = tk.Label(janela, bg="black", fg="white", text="Calculadora de Bar -> PSI", font=("Arial", 30)).grid(column=0, row=0, padx=20, pady=10)
# lbl_bar = tk.Label(janela, bg="black", fg="white", font=("Arial", 20), text="Quantidade de Bar").grid(column=0, row=1, padx=20, pady=10)
# ent_bar = tk.Entry(janela, bg="White", fg="Black", font=("Arial", 14))
# ent_bar.grid(column=0, row=2, padx=20, pady=10)
# btn_calcular = tk.Button(janela, bg="gray", fg="white", font=("Arial", 20), text="Calcular", command=calcular).grid(column=0, row=3, padx=20, pady=10)


# 4. Média de Qualidade: Peça 3 notas de inspeção de uma peça (0 a 10). Exiba a média
# aritmética simples delas.
# def calcular():
#     v1 = int(ent_1.get())
#     v2 = int(ent_2.get())
#     v3 = int(ent_3.get())
#     media = (v1 + v2 + v3) / 3

#     if media == 0:
#         messagebox.showerror("Erro", "Coloque os números!")
#     else:
#        texto = f"A nota em media é: {media}"
#        messagebox.showinfo("Mensagem", texto)

# lbl_Titulo = tk.Label(janela, bg="black", fg="white", font=("Arial", 30), text="Calculadora de média").grid(row=0, column=1, padx=20, pady=10)
# lbl_1 = tk.Label(janela, bg="black", fg="White", font=("Arial", 20), text="Peça 1").grid(row=1, column=0, padx=20, pady=10)
# ent_1 = tk.Entry(janela, bg="white", fg="black", font=("Arial", 20))
# ent_1.grid(row=1, column=1, padx=20, pady=10)
# lbl_2 = tk.Label(janela, bg="black", fg="White", font=("Arial", 20), text="Peça 2").grid(row=2, column=0, padx=20, pady=10)
# ent_2 = tk.Entry(janela, bg="white", fg="black", font=("Arial", 20))
# ent_2.grid(row=2, column=1, padx=20, pady=10)
# lbl_3 = tk.Label(janela, bg="black", fg="White", font=("Arial", 20), text="Peça 3").grid(row=3, column=0, padx=20, pady=10)
# ent_3 = tk.Entry(janela, bg="white", fg="black", font=("Arial", 20))
# ent_3.grid(row=3, column=1, padx=20, pady=10)
# btn_calcular = tk.Button(janela, bg="gray", fg="white", font=("Arial", 20),text="Calcular", command=calcular).grid(row=4, column=1, padx=20, pady=10)


# 5. Termostato Inteligente: Peça a temperatura de um motor.
# ● Abaixo de 40°C: "Baixa carga".
# ● Entre 40°C e 70°C: "Normal".
# ● Acima de 70°C: "ALERTA: Resfriamento Ativado!".
# def verificar():
#     temperatura = int(ent_temp.get())

#     if temperatura <= 40:
#         messagebox.showinfo("Abaixo", "A Temperatura está abaixo de 40 graus!\n Baixa carga!")
#     elif temperatura <= 70:
#         messagebox.showinfo("Normal", "A Temperatura está entre Entre 40°C e 70°C!\n Carga Normal!")
#     else:
#         messagebox.showinfo("Acima", "A Temperatura está Acima de 70°C!\n Ativando resfriamento...")
#         messagebox.showwarning("Resfriamento", "Resfriamento ativado!")

# lbl_titulo = tk.Label(janela, bg="black", fg="white", font=("Arial", 30), text="Termostrato Inteligente").grid(row=0, column=1, padx=20, pady=10)
# lbl_temp = tk.Label(janela, bg="black", fg="white", font=("Arial", 20), text="Digite a Temperatura (Motor):").grid(row=1, column=0, padx=20, pady=10)
# ent_temp = tk.Entry(janela, bg="white", fg="black", font=("Arial", 20))
# ent_temp.grid(row=1, column=1, padx=20, pady=10)
# btn_verificar = tk.Button(janela, bg="gray", fg="white", font=("Arial", 20), text="Verificar", command=verificar).grid(row=2, column=1, padx=20, pady=10)


# 6. Classificador de Lotes: O usuário insere o código do produto. Se começar com "A",
# exiba "Alimentos". Se "E", "Eletrônicos". Para qualquer outro, "Desconhecido".def classificar():
    
# def classificar():    
#     codigo = ent_codigo.get().strip()
#     if codigo == "":
#         messagebox.showerror("Erro", "Digite o código do produto.")
#     elif codigo.upper().startswith("E"):
#         messagebox.showinfo("Classificação", "Eletrônicos")
#     elif codigo.upper().startswith("A"):
#         messagebox.showinfo("Classificação", "Alimentos")
#     else:
#         messagebox.showinfo("Classificação", "Desconhecido")
#     ent_codigo.delete(0, tk.END)

# lbl_titulo = tk.Label(janela, bg="black", fg="white", font=("Arial", 30), text="Classificador de Lotes").grid(row=0, column=1, padx=20, pady=10)
# lbl_codigo = tk.Label(janela, bg="black", fg="white", font=("Arial", 20), text="Digite o Código:").grid(row=1, column=0, padx=20, pady=10)
# ent_codigo = tk.Entry(janela, bg="white", fg="black", font=("Arial", 20))
# ent_codigo.grid(row=1, column=1, padx=20, pady=10)
# btn_classificar = tk.Button(janela, bg="gray", fg="white", font=("Arial", 20), text="Classificar", command=classificar).grid(row=2, column=1, padx=20, pady=10)


# 7. Segurança de Operação: A máquina só liga se o sensor_porta == "fechada" E o
# botao_emergencia == "desligado". Peça esses dois inputs e diga se a máquina pode
# iniciar.
# def iniciar():
#     sensor = ent_sensor.get()
#     emergencia = ent_Emergencia.get()
#     if sensor == "" or emergencia == "":
#         messagebox.showerror("Erro", "Digite se o sensor está fechado ou se o botão está ativo!.")
#     elif sensor == "fechada" and emergencia == "desligado":
#         messagebox.showinfo("Rodou", "A Máquina Iniciou!\nPassou pelo sistema de segurança!")
        
# lbl_titulo = tk.Label(janela, bg="black", fg="white", font=("Arial", 30), text="Classificador de Lotes").grid(row=0, column=1, padx=20, pady=10)
# lbl_sensor = tk.Label(janela, bg="black", fg="white", font=("Arial", 20), text="Sensor da Porta:").grid(row=1, column=0, padx=20, pady=10)
# ent_sensor = tk.Entry(janela, bg="white", fg="black", font=("Arial", 20))
# ent_sensor.grid(row=1, column=1, padx=20, pady=10)
# lbl_Emergencia = tk.Label(janela, bg="black", fg="white", font=("Arial", 20), text="Botao de Emergencia:").grid(row=2, column=0, padx=20, pady=10)
# ent_Emergencia = tk.Entry(janela, bg="white", fg="black", font=("Arial", 20))
# ent_Emergencia.grid(row=2, column=1, padx=20, pady=10)

# btn_iniciar = tk.Button(janela, bg="gray", fg="white", font=("Arial", 20), text="Iniciar", command=iniciar).grid(row=3, column=1, padx=20, pady=10)


# 8. Cálculo de Descarte: Peça o total de peças produzidas e o total de defeituosas. Se
# o descarte for maior que 5% do total, exiba "Revisar Processo", caso contrário,
# "Processo Otimizado".

# def calcular():
#     produzidas = int(ent_produzidas.get())
#     descartadas = int(ent_descartadas.get())

#     if produzidas == "" or descartadas == "":
#         messagebox.showerror("Erro", "Digite o que foi produzido e quantas descartadas!")
#     elif descartadas <= produzidas * 0.05:
#         messagebox.showinfo("Mensagem", "O Processo está otimizado!\n Parabéns!")
#     elif descartadas >= produzidas * 0.05:
#         messagebox.showinfo("Mensagem", "Revise o Processo\n Você está descartando mais que 5% do que produz!")

# lbl_titulo = tk.Label(janela, bg="black", fg="white", font=("Arial", 30), text="Calculadora de Descarte").grid(row=0, column=1, padx=20, pady=10)
# lbl_produzidas = tk.Label(janela, bg="black", fg="white", font=("Arial", 20), text="Total de peças produzidas:").grid(row=1, column=0, padx=20, pady=10)
# ent_produzidas = tk.Entry(janela, bg="white", fg="black", font=("Arial", 20))
# ent_produzidas.grid(row=1, column=1, padx=20, pady=10)
# lbl_descartadas = tk.Label(janela, bg="black", fg="white", font=("Arial", 20), text="Total de Defeituosas:").grid(row=2, column=0, padx=20, pady=10)
# ent_descartadas= tk.Entry(janela, bg="white", fg="black", font=("Arial", 20))
# ent_descartadas.grid(row=2, column=1, padx=20, pady=10)

# btn_calcular = tk.Button(janela, bg="gray", fg="white", font=("Arial", 20), text="Calcular", command=calcular).grid(row=3, column=1, padx=20, pady=10)


# 9. Validação de Medida: Uma peça deve ter entre 9.8mm e 10.2mm. Peça a medida e
# diga se está dentro da tolerância, acima ou abaixo.
# def verificar():
#     medida = float(ent_medida.get())

#     if medida == 0:
#         messagebox.showerror("Erro", "Digite a medida!")
#     elif medida >= 9.8 and medida <= 10.2:
#         messagebox.showinfo("Sucesso!", "Sua peça está dentro da Tolerância!")
#     elif medida < 9.8:
#         messagebox.showinfo("Mensagem", "Sua peça abaixo da tolerância!")
#     elif medida > 10.2:
#         messagebox.showinfo("Mensagem", "Sua peça acima da tolerância!")


# lbl_titulo = tk.Label(janela, bg="black", fg="white", font=("Arial", 30), text="Classificador de Lotes").grid(row=0, column=1, padx=20, pady=10)
# lbl_medida = tk.Label(janela, bg="black", fg="white", font=("Arial", 20), text="Digite o Código:").grid(row=1, column=0, padx=20, pady=10)
# ent_medida = tk.Entry(janela, bg="white", fg="black", font=("Arial", 20))
# ent_medida.grid(row=1, column=1, padx=20, pady=10)
# btn_verificar = tk.Button(janela, bg="gray", fg="white", font=("Arial", 20), text="Verificar", command=verificar).grid(row=2, column=1, padx=20, pady=10)


# 10.Contagem Regressiva de Setup: Use um for para fazer uma contagem regressiva
# de 10 até 1 para o início de uma prensa, e finalize com "Prensa Ativada!".
# tempo = 10

# def Iniciar():
#     global tempo
#     for i in range(10):
        
#         messagebox.showinfo("Contagem", f"Tempo: {tempo}")
#         tempo -= 1

#     if tempo == 0:
#         messagebox.showinfo("Prensa", "Prensa Ativa!")  

# lbl_titulo = tk.Label(janela, bg="black", fg="white", font=("Arial", 30), text="Contagem Regressiva").grid(row=0, column=1, padx=20, pady=10)
# btn_Iniciar = tk.Button(janela, bg="gray", fg="white", font=("Arial", 20), text="Verificar", command=Iniciar).grid(row=2, column=1, padx=20, pady=10)


# 11.Soma de Produção (Acumulador): Use um while para pedir o peso de várias caixas.
# O loop para quando o usuário digitar 0. No fim, mostre o peso total acumulado.

# Professor eu pesquisei na internet eu encontrei esse simpledialog, utilizei ele por ser mais fácil, acredito que era permitido!

# def Acumular():
#     peso_total = 0
#     while True:
#         peso = simpledialog.askfloat("Peso da Caixa", "Digite o peso da caixa (0 para finalizar):")
#         if peso is None:
#             break
#         if peso == 0:
#             break
#         peso_total += peso
#     messagebox.showinfo("Resultado", f"Peso total acumulado: {peso_total:.2f} kg")
# lbl_titulo = tk.Label(janela,bg="black",fg="white",font=("Arial", 30),text="Soma de Produção")
# lbl_titulo.grid(row=0, column=1, padx=20, pady=10)
# btn_Iniciar = tk.Button(janela, bg="gray", fg="white", font=("Arial", 20), text="Acumular", command=Acumular)
# btn_Iniciar.grid(row=2, column=1, padx=20, pady=10)


# 12.Múltiplas Leituras: Use um for para pedir a temperatura de 5 sensores diferentes.
# Ao final, mostre qual foi a maior temperatura lida.

# def descobrir():
# 	maior = 0
# 	for i in range(1, 6):
# 		temp = simpledialog.askfloat("Temperatura", f"Digite a temperatura do sensor {i}:")
# 		if temp is None:
# 			break
# 		if (maior == 0) or (temp > maior):
# 			maior = temp
# 	if maior == 0:
# 		messagebox.showinfo("Resultado", "Nenhuma temperatura foi informada.")
# 	else:
# 		messagebox.showinfo("Resultado", f"A maior temperatura lida foi: {maior:.2f}C")

# lbl_titulo = tk.Label(janela,bg="black",fg="white",font=("Arial", 30),text="Multiplas Leituras")
# lbl_titulo.grid(row=0, column=1, padx=20, pady=10)
# btn_Iniciar = tk.Button(janela, bg="gray", fg="white", font=("Arial", 20), text="Descobrir a Maior", command=descobrir)
# btn_Iniciar.grid(row=2, column=1, padx=20, pady=10)


# 13.Painel de Login: Crie um while que peça a senha do supervisor ("admin123").
# Enquanto ele errar, o programa diz "Acesso Negado". Ele tem apenas 3 tentativas.
# Se esgotar, exiba "Painel Bloqueado".
# erro = 0
# def Login():
#     global erro
#     senha = entry_senha.get()
#     if senha == "":
#         messagebox.showerror("Erro","Digite a senha!")
#     elif senha == "admin123":
#         messagebox.showinfo("Login", "Sucesso!\n Login Efetuado!")
#     else:
#         tentativas = 3 - erro
#         texto = f"Senha incorreta\n você ainda possuí {tentativas} tentativas"
#         messagebox.showerror("Erro!", texto)
#         erro += 1

#     if erro >= 3:
#         messagebox.showerror("Painel", "Painel Bloqueado!")
#         janela.destroy()


# lbl_Titulo = tk.Label(janela, fg="White", bg="black", font=("Ariel", 30), text="Login").grid(row=0, column=1, padx=30, pady=10)
# lbl_Nome = tk.Label(janela, fg="White", bg="black", font=("Ariel", 20), text="Nome de Usuário:").grid(row=1, column=0, padx=30, pady=10)
# lbl_Supervisor = tk.Label(janela, fg="White", bg="black", font=("Ariel", 25), text="Supervisor").grid(row=1, column=1, padx=30, pady=10)
# lbl_Senha = tk.Label(janela, fg="White", bg="black", font=("Ariel", 25), text="Senha").grid(row=2, column=0, padx=30, pady=10)
# entry_senha = tk.Entry(janela, fg="Black", bg="White", font=("Ariel", 14))
# entry_senha.grid(row=2, column=1, padx=30, pady=10)
# button_Login = tk.Button(janela, fg="White", bg="Gray", font=("Ariel", 20), text="Login", command=Login).grid(row=3, column=1, padx=30,pady=10)


# 14.Simulador de Estoque: Comece com estoque = 100. Crie um menu (while) onde o
# usuário pode: (1) Adicionar itens, (2) Remover itens ou (3) Sair. Se o estoque ficar
# abaixo de 10, avise: "Estoque Crítico!".

# def simulador_estoque():
#     estoque = 100
#     while True:
#         opcao = simpledialog.askinteger(
#             "Estoque",
#             "Escolha uma opção:\n1 - Adicionar itens\n2 - Remover itens\n3 - Sair"
#         )
#         if opcao is None:
#             break
#         if opcao == 1:
#             quantidade = simpledialog.askinteger("Adicionar Itens", "Quantos itens deseja adicionar?")
#             if quantidade == 0:
#                 continue
#             if quantidade < 0:
#                 messagebox.showerror("Erro", "Quantidade invalida!")
#                 continue
#             estoque += quantidade
#             messagebox.showinfo("Estoque", f"Estoque atualizado: {estoque}")
#         elif opcao == 2:
#             quantidade = simpledialog.askinteger("Remover Itens", "Quantos itens deseja remover?")
#             if quantidade == 0:
#                 continue
#             if quantidade < 0:
#                 messagebox.showerror("Erro", "Quantidade invalida!")
#                 continue
#             if quantidade > estoque:
#                 messagebox.showwarning("Erro", "Não há itens suficientes no estoque!")
#                 continue
#             estoque -= quantidade
#             if estoque < 10:
#                 messagebox.showwarning("Estoque Critico!", f"Estoque atualizado: {estoque}\nEstoque Critico!")
#             else:
#                 messagebox.showinfo("Estoque", f"Estoque atualizado: {estoque}")
#         elif opcao == 3:
#             break
#         else:
#             messagebox.showerror("Erro", "Opção inválida! Digite 1, 2 ou 3.")
#     messagebox.showinfo("Simulador de Estoque", "Encerrando simulador.")

# lbl_titulo = tk.Label(janela, bg="black", fg="white", font=("Arial", 30), text="Estoque")
# lbl_titulo.grid(row=0, column=1, padx=20, pady=10)
# btn_estoque = tk.Button(janela, bg="gray", fg="white", font=("Arial", 20), text="Abrir Estoque", command=simulador_estoque)
# btn_estoque.grid(row=2, column=1, padx=20, pady=10)



# 15.Relatório de Turno Completo: Use um for para processar 5 peças. Para cada peça,
# peça o diâmetro. Se a peça for aprovada (entre 19.9 e 20.1), conte-a. No final do
# loop, exiba o total de peças aprovadas e a porcentagem de eficiência do lote.

# def relatorio():
#     aprovadas = 0
#     total = 5
#     for i in range(1, total + 1):
#         while True:
#             diametro = simpledialog.askfloat("Diâmetro da peça", f"Digite o diâmetro da peça {i}:")
#             if diametro is None:
#                 messagebox.showinfo("Relatório", "Entrada cancelada.")
#                 return
#             if diametro <= 0:
#                 messagebox.showwarning("Valor inválido", "Por favor, informe um diâmetro positivo.")
#                 continue
#             break
#         if 19.9 <= diametro <= 20.1:
#             aprovadas += 1
#     eficiencia = (aprovadas / total) * 100
#     messagebox.showinfo("Resultado", f"Peças aprovadas: {aprovadas} de {total}\nEficiência do lote: {eficiencia:.1f}%")

# lbl_titulo = tk.Label(janela, bg="black", fg="white", font=("Arial", 30), text="Relatório de Turno")
# lbl_titulo.grid(row=0, column=1, padx=20, pady=10)
# btn_relatorio = tk.Button(janela, bg="gray", fg="white", font=("Arial", 20), text="Abrir Relatório", command=relatorio).grid(row=2, column=1, padx=20, pady=10)

janela.mainloop()
