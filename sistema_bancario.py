menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
"""

saldo = 0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
LIMITE_MAXIMO_SAQUE = 500

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor que deseja depositar: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")


    elif opcao == "2":
        valor = float(input("Informe o valor que deseja sacar: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > LIMITE_MAXIMO_SAQUE
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        if excedeu_saldo:
            print("Operação falhou! O seu saldo não é suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O seu limite não é suficiente.")
        elif excedeu_saques:
            print("Operação falhou! Você atingiu o número máximo de saques diário.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")


    elif opcao == "3":
        print("\n     Extrato     ")
        print("Não foram realizadas movimentações em sua conta." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("          ")


    elif opcao == "4":
        break


    else:
        print("Operação inválida, por favor selecione uma operação válida.")
