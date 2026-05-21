def nome():
    nome = input("Digite seu nome: ")
    return nome
print(f"Olá, {nome()}!")

def valores():
    print("Digite Três valores: ")
    a = int(input("Digite o primeiro valor: "))
    b = int(input("Digite o segundo valor: "))
    c = int(input("Digite o terceiro valor: "))
    return a, b, c
print(f"Valores: {max(valores())}!")

def dobro():
    numero = input("escreva o valor que deseja dobrar:") 
    return numero * 2

print(dobro())