
import json

from time import sleep

id = 0



usuarios = "usuarios.json"



usuariologado = ""

setorlogado = ""







def carregar_dados():

    try:

        with open(usuarios, 'r', encoding='utf-8') as f:

            return json.load(f)

    except (FileNotFoundError, json.JSONDecodeError):

        return []

   

def salvar_dados(dados):

    with open(usuarios, 'w', encoding='utf-8') as f:

        json.dump(dados, f, indent=4, ensure_ascii=False)



def cadastro():

    print("\n CADASTRO ")

    usuario = input("Digite o nome de usuário: ")

    Setor = input("Digite a Setor: ")

   

    dados = carregar_dados()

   

   

    if any(u['usuario'] == usuario for u in dados):

        print("Erro: Este usuário já existe!")

    else:

        dados.append({"usuario": usuario, "Setor": Setor, "NR10": False, "NR35": False, "Brigada": False})

        salvar_dados(dados)

        print("Usuário cadastrado com sucesso!")



def Verificacao():

    print("Verificando seus dados...")

    dados = carregar_dados()

    sleep(1)

    print("Dados Carregados: ")

   

    Nr10 = any(u['usuario'] == usuariologado and u['NR10'] == True for u in dados)

    Nr35 = any(u['usuario'] == usuariologado and u['NR35'] == True for u in dados)

    Brigada = any(u['usuario'] == usuariologado and u['Brigada'] == True for u in dados)

   

   

    if Nr10:

        print("NR10: Ok")

    else:

        verificao = input("Você deseja verificar o NR10? (Sim | Não)")

        if verificao == "Sim":

            print("A norma NR-10 (Segurança em Instalações e Serviços em Eletricidade) estabelece requisitos e condições mínimas para garantir a segurança e a saúde dos trabalhadores que interagem, direta ou indiretamente, com instalações elétricas e serviços com eletricidade. Ela abrange etapas de projeto, geração, transmissão, distribuição e consumo. ")

            dados.append({"usuario": usuariologado, "Setor": setorlogado, "NR10": True, "NR35": Nr35, "Brigada": Brigada})

            salvar_dados(dados)

            sleep(5)

            print("Prosseguindo para a próxima")

        else:

            print("Prosseguindo para a próxima.")

            dados.append({"usuario": usuariologado, "Setor": setorlogado, "NR10": False, "NR35": Nr35, "Brigada": Brigada})

            salvar_dados(dados)

   

   

   

    print("NR35: ")

    print("Brigada: ")

   

   



def login():

    print("\n LOGIN ")

    usuario = input("Usuário: ")

    Setor = input("Setor: ")

   

    dados = carregar_dados()

   



    autenticado = any(u['usuario'] == usuario and u['Setor'] == Setor for u in dados)

   

    if autenticado:

        usuariologado = usuario

        setorlogado = Setor

        print(f"Bem-vindo, {usuario}! Login realizado.")

        Verificacao()

       

    else:

        print("Usuário ou Setor incorretos.")

       



def menu():

    while True:



        opcao = input("Seja bem-vindo! O que deseja fazer? (Login | Cadastro | Sair): ").capitalize()



        if opcao == "Cadastro":

            cadastro()

        elif opcao == "Login":

            login()

        elif opcao == "Sair":

            print("Saindo do sistema...")

            break

        else:

            print("Opção inválida! Tente novamente.")









menu()

