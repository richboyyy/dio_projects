# Constantes
LIMITE_SAQUES = 3
LIMITE = 500

# Funções
def depositar(saldo, extrato):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacar(saldo, extrato, numero_saques):
    valor = float(input("Informe o valor do saque: "))
    
    if valor <= 0:
        print("Operação falhou! O valor informado é inválido.")
    elif valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif valor > LIMITE:
        print("Operação falhou! O valor do saque excede o limite.")
    elif numero_saques >= LIMITE_SAQUES:
        print("Operação falhou! Número máximo de saques excedido.")
    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def exibir_menu():
    menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """
    return input(menu)

# Variáveis iniciais
saldo = 0
extrato = ""
numero_saques = 0

# Loop principal
while True:
    opcao = exibir_menu()

    if opcao == "d":
        saldo, extrato = depositar(saldo, extrato)

    elif opcao == "s":
        saldo, extrato, numero_saques = sacar(saldo, extrato, numero_saques)

    elif opcao == "e":
        exibir_extrato(saldo, extrato)

    elif opcao == "q":
        print("Saindo... Obrigado por usar nosso sistema!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
