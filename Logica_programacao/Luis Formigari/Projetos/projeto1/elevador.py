


andar_atual = 0
capacidade_maxima = 5

def mover_elevador(origem, destino):
    global andar_atual
    while andar_atual != origem:
        if andar_atual < origem:
            andar_atual += 1
            print(f"Subindo... Andar {andar_atual}")
        else:
            andar_atual -= 1
            print(f"Descendo... Andar {andar_atual}")

    print(f"Parou no andar {andar_atual} para embarque")
    while andar_atual != destino:
        if andar_atual < destino:
            andar_atual += 1
            print(f"Subindo... Andar {andar_atual}")
        else:
            andar_atual -= 1
            print(f"Descendo... Andar {andar_atual}")

    print(f"Parou no andar {andar_atual} para desembarque")


while True:
    print("\n===== SISTEMA DE ELEVADOR =====")
    print(f"Andar atual: {andar_atual}")

    pessoas = int(input("Quantidade de pessoas (1 a 5): "))

    if pessoas < 1 or pessoas > capacidade_maxima:
        print("Quantidade invalida! O elevador aguenta até 5 pessoas.")
        continue

    origem = int(input("Andar onde o elevador foi chamado (0 a 10): "))
    destino = int(input("Andar de destino (0 a 10): "))

    if origem < 0 or origem > 10 or destino < 0 or destino > 10:
        print("Andar invalidox!")
        continue

    print(f"\nPessoas no elevador: {pessoas}")

    mover_elevador(origem, destino)

    print(f"Andar atual: {andar_atual}")
    print(f"Pessoas transportadas: {pessoas}")

    continuar = input("\nDeseja realizar mais chamadas? (S/N): ").upper()

    if continuar != "S":
        print("Sistema encerrado")
        break
