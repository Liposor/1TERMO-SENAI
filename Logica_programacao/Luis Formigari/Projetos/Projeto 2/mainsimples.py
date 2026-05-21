# --- CONFIGURAÇÕES E BANCO DE DADOS SIMPLIFICADO ---
# Um dicionário facilita a manutenção caso novos setores sejam adicionados
EPIS_POR_SETOR = {
    "1": ("Elétrica", "Luvas de alta tensão e botas dielétricas."),
    "2": ("Trabalho em Altura", "Cinturão de segurança e talabarte.")
}

def verificar_epi(opcao_setor):
    """Retorna o nome do setor e os EPIs recomendados."""
    # .get() evita que o programa quebre caso a opção não exista
    setor, epis = EPIS_POR_SETOR.get(opcao_setor, ("Outro", "Consultar setor de segurança."))
    print(f"Setor: {setor}")
    print(f"EPIs recomendados: {epis}")

def alerta_reciclagem(ano_treino):
    """Verifica a validade do treinamento (máximo 2 anos)."""
    ANO_ATUAL = 2026
    if (ANO_ATUAL - ano_treino) > 2:
        print("MENSAGEM: Treinamento Vencido! Encaminhar para reciclagem.")
        return False
    
    print("MENSAGEM: Treinamento Válido.")
    return True

def sistema_sesmt():
    print("================================================================")
    print("  Sistema de Controle senaizin - Bem-vindo!")
    print("================================================================")
    
    total_cadastrados = 0
    total_em_dia = 0

    while True:
        # Coleta de dados básicos
        nome = input("\nNome do funcionário: ").strip()
        
        # Menu numérico para o setor (evita erros de digitação)
        print("Setores: [1] Elétrica | [2] Trabalho em Altura | [Outro] Qualquer tecla")
        opcao_setor = input("Escolha a opção do setor: ").strip()
        
        nr10 = input("Status NR-10 (OK/Pendente): ").strip().upper()
        nr35 = input("Status NR-35 (OK/Pendente): ").strip().upper()
        ano_brigada = int(input("Ano do último treinamento da Brigada: "))

        total_cadastrados += 1

        # Processamento e Resposta imediata
        print("\n--- RESULTADOS ---")
        verificar_epi(opcao_setor)
        brigada_em_dia = alerta_reciclagem(ano_brigada)

        # Verificação de conformidade total
        if nr10 == "OK" and nr35 == "OK" and brigada_em_dia:
            total_em_dia += 1

        # Condição de parada
        continuar = input("\nDeseja cadastrar outro funcionário? (S/N): ").strip().upper()
        if continuar not in ["S", "SIM"]:
            break

    # --- RELATÓRIO FINAL ---
    print("\n" + "="*40)
    print(f"{'RELATÓRIO GERAL':^40}")
    print("-" * 40)
    print(f"Total de cadastrados: {total_cadastrados}")
    print(f"Total em dia:         {total_em_dia}")
    print("="*40)

# Executa o sistema
if __name__ == "__main__":
    sistema_sesmt()