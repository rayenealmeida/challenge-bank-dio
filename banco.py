menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Quanto quer depositar? "))

        if valor > 0 :
            saldo += valor
            extrato = extrato + f"Depósito: R$ {valor:.2f}\n"
        else:
            print("\nValor inválido!")
        

    elif opcao == "2":
        valor = float(input("Quanto quer sacar? "))

        if valor > saldo:
            print("\nNão tem saldo suficiente!")
        
        elif valor > limite:
            print("\nLimite de valor diário excedido!")

        elif numero_saques >= LIMITE_SAQUES:
            print("\nLimite de saque diário excedido!")

        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque concluído! valor do saque: {valor} \nsaldo restante: {saldo}")

        else:
            print("Algo deu errado!")
        

    elif opcao == "3":
        print(f"\nSaldo: R$ {saldo:.2f}")        
        if not extrato:
            print("\nNão há movimentações")

    elif opcao == "4":
        break

    else:
        print("Operação inválida, por favor selecione a operação correta")
