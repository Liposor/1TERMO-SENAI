# exercicio 1:
# Escreva um programa que solicite ao usuário um número inteiro e
# calcule a media de uma lista de números.  O programa deve tratar
# os seguintes erros:
    
# - Valuerror: se o usuário digitar um valor que não seja um número
# inteiro.

print("Exercício 1")


lista = 0
numerosDigi = 0

numeros = int(input("Digite quantos numeros para média...   "))
for i in range(numeros):
    try:
        num = int(input("Digite o número...  "))
        lista += num
        numerosDigi += 1
        
    except ValueError:
        print("Erro: Entrada Inválida. Por favor, digite um número inteiro.")
        num = int(input("Digite o número...  "))
        lista += num
        numerosDigi += 1
        
        

resultado = lista / numerosDigi     
print(f"O resultado da divisão é: {resultado:.2f}")