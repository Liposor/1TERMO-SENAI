
from datetime import datetime

funcionarios = []
treinamentos_em_dia = 0

def verificar_epi(setor):
    print("\nEPIs Obrigatórios:")

    if setor.lower() == "elétrica":
        print("- Luvas de alta tensão")
        print("- Botas dielétricas")

    elif setor.lower() == "trabalho em altura":
        print("- Cinturão de segurança")
        print("- Talabarte")

    else:
        print("- EPIs conforme procedimento do setor")

def verificar_reciclagem(ano_ultimo_treinamento):
    ano_atual = datetime.now().year

    if ano_atual - ano_ultimo_treinamento > 2:
        print("Treinamento Vencido! Encaminhar para reciclagem.")
        return False
    else:
        print("Treinamento Válido.")
        return True

quantidade = int(input("Quantos funcionários deseja cadastrar? "))

for i in range(quantidade):
    print(f"\nCadastro do Funcionário {i + 1}")

    nome = input("Nome: ")
    setor = input("Setor: ")

    nr10 = input("Possui treinamento NR-10? (S/N): ").upper()
    nr35 = input("Possui treinamento NR-35? (S/N): ").upper()
    brigada = input("Possui treinamento Brigada? (S/N): ").upper()

    ano_brigada = int(input("Ano do último treinamento da Brigada: "))

    print("\nVerificação de EPI")
    verificar_epi(setor)

    print("\nVerificação da Brigada")
    brigada_valida = verificar_reciclagem(ano_brigada)

    if (nr10 == "S" and nr35 == "S" and brigada == "S"
            and brigada_valida):
        treinamentos_em_dia += 1

    funcionario = {
        "nome": nome,
        "setor": setor,
        "nr10": nr10,
        "nr35": nr35,
        "brigada": brigada
    }

    funcionarios.append(funcionario)

print("\n========== RELATÓRIO GERAL ==========")
print("Total de funcionários cadastrados:", len(funcionarios))
print("Funcionários com treinamentos em dia:", treinamentos_em_dia)

print("\nLista de Funcionários:")
for funcionario in funcionarios:
    print(f"- {funcionario['nome']} | Setor: {funcionario['setor']}")
