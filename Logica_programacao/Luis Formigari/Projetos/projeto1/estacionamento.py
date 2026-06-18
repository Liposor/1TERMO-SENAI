vagas = 500
ocupadas = 0

tags_ativas = ["123", "321", "555"]

while True:
    print("\nVagas disponíveis:", vagas - ocupadas)

    print("\n1 - Entrada Ticket")
    print("2 - Entrada TAG")
    print("3 - Saída")
    print("0 - Sair")

    op = input("Opção: ")
    if op == "1":
        if ocupadas < vagas:
            ocupadas += 1
            print("Ticket emitido. Entrada liberada.")
        else:
            print("Estacionamento lotado!")

    elif op == "2":
        tag = input("Digite o número da TAG: ")

        if tag in tags_ativas:
            if ocupadas < vagas:
                ocupadas += 1
                print("TAG válida. Entrada liberada.")
            else:
                print("Estacionamento lotado!")
        else:
            print("TAG inválida!")


    elif op == "3":
        if ocupadas > 0:
            horas = float(input("Horas estacionado: "))

            if horas <= 0.25:
                valor = 0
            elif horas <= 3:
                valor = 15
            else:
                valor = 15 + (horas - 3) * 3

            print("Valor a pagar: R$", round(valor, 2))

            pago = input("Pago? (S/N): ")

            if pago == "S":
                ocupadas -= 1
                print("Saída liberada.")
            else:
                print("Pagamento pendente.")

        else:
            print("Nenhum carro no estacionamento.")

    elif op == "0":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida.")
