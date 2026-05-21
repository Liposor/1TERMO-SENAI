import json
from time import sleep

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
    print("\n--- CADASTRO ---")
    usuario = input("Digite o nome de usuário: ")
    Setor = input("Digite o Setor: ")
   
    dados = carregar_dados()
   
    if any(u['usuario'] == usuario for u in dados):
        print("Erro: Este usuário já existe!")
    else:
        dados.append({"usuario": usuario, "Setor": Setor, "NR10": False, "NR35": False, "Brigada": False})
        salvar_dados(dados)
        print("Usuário cadastrado com sucesso!")

def Verificacao():
    print("\nVerificando seus dados...")
    sleep(1)
    
    dados = carregar_dados()
    
    # Encontra o índice do usuário logado na lista de dados
    usuario_index = None
    for i, u in enumerate(dados):
        if u['usuario'] == usuariologado:
            usuario_index = i
            break

    if usuario_index is None:
        print("Erro: Usuário não encontrado na base de dados.")
        return

    user_data = dados[usuario_index]

    # --- VERIFICAÇÃO NR10 ---
    if user_data['NR10']:
        print("NR10: Ok")
    else:
        verificao = input("Você deseja verificar o NR10? (Sim | Não): ").capitalize()
        if verificao == "Sim":
            print("\nA norma NR-10 (Segurança em Instalações e Serviços em Eletricidade) estabelece requisitos e condições mínimas para garantir a segurança e a saúde dos trabalhadores que interagem com instalações elétricas.")
            user_data['NR10'] = True
            salvar_dados(dados)
            sleep(3)
        print("Prosseguindo para a próxima...\n")

    # --- VERIFICAÇÃO NR35 ---
    if user_data['NR35']:
        print("NR35: Ok")
    else:
        verificao = input("Você deseja verificar o NR35? (Sim | Não): ").capitalize()
        if verificao == "Sim":
            print("\nA norma NR-35 estabelece os requisitos mínimos e as medidas de proteção para o trabalho em altura, envolvendo o planejamento, a organização e a execução, de forma a garantir a segurança e a saúde dos trabalhadores envolvidos direta ou indiretamente com esta atividade.")
            user_data['NR35'] = True
            salvar_dados(dados)
            sleep(3)
        print("Prosseguindo para a próxima...\n")

    # --- VERIFICAÇÃO BRIGADA ---
    if user_data['Brigada']:
        print("Brigada: Ok")
    else:
        verificao = input("Você deseja verificar a Brigada de Incêndio? (Sim | Não): ").capitalize()
        if verificao == "Sim":
            print("\nA Brigada de Incêndio é um grupo organizado de pessoas treinadas e capacitadas para atuar na prevenção, combate a princípio de incêndio, abandono de área e primeiros socorros dentro de uma empresa ou estabelecimento.")
            user_data['Brigada'] = True
            salvar_dados(dados)
            sleep(3)
        print("Verificações concluídas.\n")

def login():
    global usuariologado, setorlogado  # Necessário para alterar as variáveis globais
    
    print("\n--- LOGIN ---")
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
        opcao = input("\nSeja bem-vindo! O que deseja fazer? (Login | Cadastro | Sair): ").capitalize()

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
