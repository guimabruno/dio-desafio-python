saldo  =  2000
valor_saque = 0
valor_deposito = 0
extrato = ""
LIMITE_SAQUE = 3
contador_saque = 0

def  realizar_saque():

    global valor_saque, saldo, extrato, contador_saque

    valor_saque = float(input("Informe o valor que  deseja sacar:   "))
    
    if  valor_saque  >=  saldo: 
        print("Operação falhou? Saldo Insuficiente")
    elif valor_saque > 500:    
        print("Operação falhou: Valor do saque excede o limite máximo de 500 reais.")
    elif contador_saque >= LIMITE_SAQUE:
        print("Operação falhou: Limite de saques excedido.")    
    elif valor_saque > 0: 
        saldo -= valor_saque
        contador_saque += 1
        extrato += F"{'Saque:':<15} {'R$':>1} {valor_saque:>10.2f}\n"
        print(f"Saque realizado com sucesso. Saldo: {saldo}")
    else:
        print("Operação falhou: Valor inválido. Saque não realizado.")

def realizar_deposito():

    global valor_deposito, saldo, extrato

    valor_deposito = float(input("Informe o valor que deseja depositar:  "))
    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += F"{'Deposito:':<15} {'R$'} {valor_deposito:>10.2f}\n"
    else:    
        print("Valor inválido. Depósito não realizado.")
         
    
    print(f"Depósito realizado com sucesso. Saldo: {saldo}")


def  exibir_extrato():
    global valor_deposito, saldo, extrato

    
    

    
    print(f"{'Tipo':<15}{'Valor':>15}")

   
    
    print("-" * 30)
    
    if valor_saque == 0 and valor_deposito == 0:

        print(f"{'Nenhuma transação realizada.':^30}")
    
    else:
        
        print(f"\n{extrato.center(30, '#')}")
    
    
    print("-" * 30)
    
    print(f"{'Saldo atual:':<15} R$ {saldo:>10.2f}")
    
    print("#" * 30)






def  exibir_menu():
    opcao = 0
    while opcao != 4:
        print("Bem-vindo  a  área do cliente no que posso ajuda-lo hoje")
        print("1 -  Saque")
        print("2 -  Depósito")
        print("3 -  Extrato")
        print("4 -  Sair")

        opcao = int(input("digite a opção desejada: "))

        if opcao == 1: 
            realizar_saque()
        elif opcao == 2:
            realizar_deposito()
        elif opcao == 3:
            exibir_extrato()
        elif opcao == 4:
            print("Até logo!")
        else:
            print("Opção inválida!")
            exibir_menu()

exibir_menu()