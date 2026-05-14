# Exercicio 3:
# Escrever um programa mais simples com testes de tratamento de erros, ocmo por exemplo, solicitar ao usuario
# um número. O programa deve tratar os seguintes erros:
    
# - ValueError: se o usuario digitar um valor que não seja um número
# - ZeroDivisionError: se o usuário digitar zero como divisor.


print("exercicio 3")
entrada = ""

# Ele vai funcionar eternamente até o usuário digitar "fim"
while entrada != "fim":
    try:
        nu1 = int(input("Digite o primeiro número...  "))
        nu2 = int(input("Digite o segundo número...  "))

        print(f"Estes são seus números {nu1:.2f} e {nu2:.2f}")
        
        print("Agora iremos dividir outros números")
        nu3 = int(input("Digite o primeiro número...  "))
        nu4 = int(input("Digite o segundo número...  "))
        resultado = nu3 / nu4
        print(f"O resultado da divisão é {resultado:.2f}")
        entrada = input("Digite a 'fim' se quiser finalizar: ")

    except ZeroDivisionError:
        print("Erro: Não é possível dividir por zero.")

    except ValueError:
        print("Erro: Entrada Inválida. Por favor, digite um número inteiro.")
        
