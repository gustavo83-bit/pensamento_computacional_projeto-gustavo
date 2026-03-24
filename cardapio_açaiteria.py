while True:
    print("\n--- CARDÁPIO DA AÇAITÉRIA ---")
    print("1 - Açaí pequeno - R$15")
    print("2 - Açaí médio - R$20")
    print("3 - Açaí grande - R$25")
    print("4 - Suco - R$7")
    print("5 - finalizar pedido")
    print("0 - Sair")

    opcao = input("Escolha um item: ")


    if opcao == "1":
        print("Você escolheu Açaí pequeno - R$15")

    elif opcao == "2":
        print("Você escolheu Açaí médio - R$20")

    elif opcao == "3":
        print("Você escolheu Açaí grande - R$25")

    elif opcao == "4":
        print("Você escolheu Suco - R$7")

        quantidade = int(input("Quantos você quer? "))

        

    elif opcao == "5":
        print("pedido finalizado! Obrigado por escolher a nossa açaitéría!")
    elif opcao == "0":
        print("Encerrando o cardápio...")
        break

    else:
        print("Opção inválida!")

