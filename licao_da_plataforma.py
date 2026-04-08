import getpass

# =========================
# FUNÇÃO DE SAUDAÇÃO
# =========================
def saudar(nome):
    print(f"Olá, {nome}! Bem-vindo ao mundo da programação.")


# =========================
# VERIFICAR IDADE
# =========================
def verificar_idade():
    print("\n--- Verificação de Idade ---")
    try:
        idade = int(input("Digite sua idade: "))
        
        if idade < 18:
            print("Você é menor de idade.")
        elif idade <= 65:
            print("Você é adulto.")
        else:
            print("Você é idoso.")
    
    except ValueError:
        print("Por favor, digite um número válido!")


# =========================
# DICIONÁRIO DE FRUTAS
# =========================
def consultar_fruta():
    print("\n--- Consulta de Frutas ---")

    preco_frutas = {
        "maçã": 2.5,
        "banana": 1.8,
        "laranja": 3.0
    }

    fruta = input("Digite o nome da fruta: ").lower()

    preco = preco_frutas.get(fruta)

    if preco is not None:
        print(f"O preço da {fruta} é R${preco}")
    else:
        print("Fruta não encontrada.")


# =========================
# SISTEMA AÇAITERIA
# =========================
def sistema_acai():
    total = 0

    while True:
        print("\n--- CARDÁPIO DA AÇAITÉRIA ---")
        print("1 - Açaí pequeno - R$15")
        print("2 - Açaí médio - R$20")
        print("3 - Açaí grande - R$25")
        print("4 - Suco - R$7")
        print("5 - Finalizar pedido")
        print("0 - Voltar")

        opcao = input("Escolha um item: ")

        if opcao == "1":
            total += 15
            print("Açaí pequeno adicionado!")
        elif opcao == "2":
            total += 20
            print("Açaí médio adicionado!")
        elif opcao == "3":
            total += 25
            print("Açaí grande adicionado!")
        elif opcao == "4":
            try:
                quantidade = int(input("Quantos sucos deseja? "))
                total += 7 * quantidade
                print(f"{quantidade} suco(s) adicionado(s)!")
            except ValueError:
                print("Digite um número válido!")
        elif opcao == "5":
            print(f"\nTotal do pedido: R${total}")
            print("Pedido finalizado! Obrigado!")
            break
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")


# =========================
# SISTEMA DE LOGIN
# =========================
def sistema_login():
    senha_padrao = "vocacao2025"
    tentativas = 3

    print("\n--- Sistema de Login ---")
    usuario = input("Digite seu usuário: ")

    while tentativas > 0:
        senha = getpass.getpass("Digite sua senha: ")

        if senha == senha_padrao:
            print(f"\nBem-vindo, {usuario}!")
            return
        else:
            tentativas -= 1
            print(f"Senha incorreta! Tentativas restantes: {tentativas}")

    print("\nAcesso bloqueado!")


# =========================
# MENU PRINCIPAL
# =========================
def menu_principal():
    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1 - Saudação")
        print("2 - Verificar idade")
        print("3 - Consultar frutas")
        print("4 - Sistema da açaíteria")
        print("5 - Sistema de login")
        print("0 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Digite seu nome: ")
            saudar(nome)

        elif escolha == "2":
            verificar_idade()

        elif escolha == "3":
            consultar_fruta()

        elif escolha == "4":
            sistema_acai()

        elif escolha == "5":
            sistema_login()

        elif escolha == "0":
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida!")


# =========================
# EXECUÇÃO
# =========================
menu_principal()