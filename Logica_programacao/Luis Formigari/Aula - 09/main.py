# tratamento de erros com python
# ERROS COMUNS: 
# - ZeroDivisionError: divisão por zero
# - ValueError: conversão de tipo inválida
# - IndexError: acesso a índice fora do limite
# - KeyError: acesso a chave inexistente em dicionário

# Exemplo de tratamento de erros
# print("Exemplo de tratamento de erros")
# try:
#   num1 = int(input("Digite o primeiro número..."))
#   num2 = int(input("Digite o segundo número..."))
#   resultado = num1 / num2

print("Exemplo de tratamento de erros")
try:
    num1 = int(input("Digite o primeiro número..."))
    num2 = int(input("Digite o segundo número..."))
    resultado = num1 / num2
    print(f"O resultado da divisão é: {resultado:.2f}")

except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")

except ValueError:
    print("Erro: Entrada Inválida. Por favor, digite um número inteiro.")
    
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
    
except NameError:
    print("Error: Variável não definida.")
    
if num1 > 100:
    print("O número digitado é maior que 100.")
    for i in range (1,6):
        print(f"{num1} x {i} = {num1 * 1}")
        if num1 * 1 > 1000:
            print("O resultado da multiplicação é maior que 1000.")
            try:
                pass
            except Exception as e:
                print(f"Ocorreu um erro inesperado: {e}")
                

    
    
else:
    print("O número é menor ou igual que 100")
    
# exercicio 1:
# Escreva um programa que solicite ao usuário um número inteiro e
# calcule a media de uma lista de números.  O programa deve tratar
# os seguintes erros:
    
# - Valuerror: se o usuário digitar um valor que não seja um número
# inteiro.
    
