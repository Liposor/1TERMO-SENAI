# Foco: print, input, operações matemáticas e f-strings

# Registro de Veículo: Peça o modelo do veículo e a placa.
# ○ Exiba: "Veículo [Modelo] de placa [Placa] registrado no sistema. Boa
# viagem!"

# nome = input("Digite o modelo do veiculo: ")
# placa = input("Diigte a placa do veiculo:  ")
# print(f"Veiculo {nome} de placa {placa} registrado no sistema. Boa viagem!")




# 2. Cálculo de Autonomia: Peça a capacidade do tanque de combustível (em litros) e
# o consumo médio do caminhão (km/l).

# capacidade = float(input("Digite a capacidade do tanque em Litros: "))
# consumo = float(input("Digite o consumo médio do caminhão (km/l): "))
# reusltado = capacidade * consumo
# print(f"A sua Autonomia é de: {reusltado} km")


# 3. Conversor de Moeda (Frete Internacional): O sistema lê o valor de um frete em
# Dólar (USD).
# ○ Converta para Real (BRL) considerando a taxa de $1,00~USD \approx
# 5,00~BRL$ e exiba com duas casas decimais.

# frete = float(input("Digite o valor do frete em USD: "))
# taxa = 5.00
# frete_brl = frete * taxa
# print(f"Valor do frete em brl: R$ {frete_brl:.2f}")


# 4. Média de Entrega: Peça o tempo de entrega (em horas) de 3 rotas diferentes
# realizadas por um motorista.
# ○ Exiba a média aritmética simples do tempo dessas entregas.
# rota1 = float(input("Tempo da rota 1 (horas): "))
# rota2 = float(input("Tempo da rota 2 (horas): "))
# rota3 = float(input("Tempo da rota 3 (horas): "))
# media = (rota1 + rota2 + rota3) / 3

# print(f"Média de tempo das entregas: {media:.2f} horas")



# Foco: if, elif, else e operadores lógicos

# 5. Monitor de Carga: Peça o peso atual de um caminhão em toneladas.
# ○ Abaixo de 10t: "Carga Leve".
# ○ Entre 10t e 25t: "Carga padrão".
# ○ Acima de 25t: "ALERTA: Excesso de Peso!".

# peso = float(input("Digite o peso do caminhao (toneladas): "))
# if peso < 10:
#     print("Carga Leve")
# elif peso <= 25:
#     print("Carga padrao")
# else:
#     print("ALERTA: Excesso de Peso")



# 6. Classificador de Destino: O usuário insere o código da carga. Se começar com "N", exiba
# "Região Norte". Se começar com "S", "Região Sul". Para qualquer outro, "Região
# Internacional".

# codigo = input("Digite o codigo da carga: ").upper()
# if codigo.startswith("N"):
#     print("Região Norte")
# elif codigo.startswith("S"):
#     print("Região Sul")
# else:
#     print("Região Internacional")


# 7. Liberação de Saída: O caminhão só pode sair se o checklist == "concluído" E o
# motorista_identificado == "sim".
# ○ Peça esses dois inputs e informe se o veículo está autorizado a iniciar a rota.

# checklist = input("Checklist concluido? (sim/nao): ").lower()
# motorista = input("Motorista identificado? (sim/nao): ").lower()
# if checklist == "sim" and motorista == "sim":
#     print("Veiculo autorizado a iniciar a rota.")
# else:
#     print("Veiculo não autorizado a sair.")



# 8. Cálculo de Atrasos: Peça o total de entregas agendadas e o total de entregas realizadas
# com atraso.
# ○ Se o índice de atraso for maior que 10% do total, exiba "Necessário Otimizar
# Rotas", caso contrário, "Logística Eficiente".

# total = int(input("Total de entregas agendadas: "))
# entregas = int(input("Total de entregas com atraso: "))
# indice = (entregas / total) * 100
# print(f"Indice de atraso: {indice:.2f}%")
# if indice > 10:
#     print("Necessario Otimizar Rotas")
# else:
#     print("Logistica Eficiente")


# 9. Validação de Calibragem: Um pneu de carga deve ter pressão entre 100 PSI e 110 PSI.
# ○ Peça a medida e diga se está dentro do padrão, acima ou abaixo do recomendado.

# pressao = float(input("Digite a pressão do pneu (PSI): "))
# if pressao < 100:
#     print("Abaixo do recomendado")
# elif pressao <= 110:
#     print("Dentro do padrão")
# else:
#     print("Acima do recomendado")


# Foco: for e while

# 10.Contagem de Embarque: Use um for para fazer uma contagem regressiva de 5
# até 1 para o fechamento do portão de embarque e finalize com "Portão Trancado!".

# for i in range(5, 0, -1):
#     print(i)
# print("Portão Trancado!")



# 11. Somatório de Fretes (Acumulador): Use um while para pedir o valor do frete de
# vários pedidos.
# ○ O loop para quando o usuário digitar 0. No fim, mostre o faturamento total
# acumulado.

# total = 0

# while True:
#     frete = float(input("digite o valor do frete (0 para encerrar): "))
#     if frete == 0:
#         break
#     total += frete
# print(f"Faturamento total: R$ {total:.2f}")


# 12.Monitoramento de Frota: Use um for para pedir a quilometragem de 5 veículos
# diferentes.
# ○ Ao final, mostre qual foi a maior quilometragem registrada.

# maior_km = 0

# for i in range(5):
#     km = float(input(f"digite a quilometragem do veiculo {i+1}: "))
#     if km > maior_km:
#         maior_km = km
# print(f"maior quilometragem registrada: {maior_km} km")


# 13.Sistema de Rastreio: Crie um while que peça o código de acesso do rastreador
# ("track99").
# ○ Enquanto o usuário errar, diga "Acesso Negado". Ele tem 3 tentativas. Se
# esgotar, exiba "Rastreamento Bloqueado".

# senha_correta = "track99"
# tentativas = 3

# while tentativas > 0:
#     senha = input("Digite o código de acesso: ")
#     if senha == senha_correta:
#         print("Acesso Liberado")
#         break
#     else:
#         tentativas -= 1
#         print("Acesso Negado")
# if tentativas == 0:
#     print("Rastreamento Bloqueado")



# Misturando tudo: Inputs, Ifs e Loops

# 14.Gerenciador de Combustível: Comece com um tanque de 500 litros. Crie um
# menu (while) onde o usuário pode: (1) Abastecer o tanque da base, (2) Retirar
# combustível para um caminhão ou (3) Sair.
# ○ Se o tanque da base ficar abaixo de 50 litros, avise: "Reserva Crítica!".

# tanque = 500
# while True:
#     print("\nTanque atual:", tanque, "litros")
#     print("1 - Abastecer tanque da base")
#     print("2 - Retirar combustível (caminhão)")
#     print("3 - Sair")

#     decisao = input("Escolha: ")
#     if decisao == "1":
#         litros = float(input("Quantos litros para abastecer? "))
#         tanque += litros
#         print("Tanque abastecido.")
#     elif decisao == "2":
#         litros = float(input("Quantos litros para retirar? "))

#         if litros <= tanque:
#             tanque -= litros
#             print("combustivel retirado.")
#         else:
#             print("Quantidade indisponivel!")

#     elif decisao == "3":
#         break
#     else:
#         print("Opção invalida!")

#     if tanque < 50:
#         print("Reserva critica, cuidado!")



# 15.Relatório de Inspeção de Pneus: Use um for para processar 5 pneus. Para cada
# um, peça a profundidade do sulco (em mm).
# ○ Se o pneu for aprovado (maior ou igual a 1.6mm), conte-o.
# ○ No final do loop, exiba o total de pneus aprovados e a porcentagem de
# conformidade da frota.

# aprovados = 0
# total_pneus = 5

# for i in range(5):
#     sulco = float(input(f"Profundidade do pneu {i+1} (mm): "))
#     if sulco >= 1.6:
#         aprovados += 1

# porcentagem = (aprovados / total_pneus) * 100
# print(f"\nPneus aprovados: {aprovados}")
# print(f"Conformidade da frota: {porcentagem:.2f}%")
