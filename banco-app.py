from datetime import datetime

saldo  =  2000
valor_saque = 0
valor_deposito = 0
extrato = ""
LIMITE_SAQUE = 3
AGENCIA = "0001"
contador_saque = 0
limite = 500
usuarios = []
numero_conta = 1
contas =[]


def  realizar_saque(*, saldo, valor_saque, extrato, limite, contador_saque, LIMITE_SAQUE):
    data_hora_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    saldo_exedido = valor_saque > saldo
    saldo_limite = valor_saque > limite
    saques_exedido = contador_saque >= LIMITE_SAQUE
    
    if  saldo_exedido: 
        print("Operação falhou? Saldo Insuficiente")
    elif saldo_limite:    
        print("Operação falhou: Valor do saque excede o limite máximo de 500 reais.")
    elif saques_exedido:
        print("Operação falhou: Limite de saques excedido.")    
    elif valor_saque > 0: 
        saldo -= valor_saque
        contador_saque += 1
        extrato += F"{'Saque:':<15} {'R$':>1} {valor_saque:>10.2f} {'Data:':<7} {data_hora_atual}\n"
        print(f"Saque realizado com sucesso. Saldo: {saldo}")
    else:
        print("Operação falhou: Valor inválido. Saque não realizado.")

    return saldo, extrato, contador_saque

def realizar_deposito(saldo, valor_deposito, extrato, /):

    data_hora_atual_deposito = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += F"{'Deposito:':<15} {'R$'} {valor_deposito:>10.2f}{'Data:':<7} {data_hora_atual_deposito}\n"
        
        print(f"Depósito realizado com sucesso. Saldo: {saldo}")
    else:    
        print("Valor inválido. Depósito não realizado.")

    return saldo, extrato


def  exibir_extrato(saldo, *, extrato):  
    

    
    print(f"{'Tipo':<15}{'Valor':>15}")

   
    
    print("-" * 30)
    
    if valor_saque == 0 and valor_deposito == 0:

        print(f"{'Nenhuma transação realizada.':^30}")
    
    else:
        
        print(f"\n{extrato.center(30, '#')}")
    
    
    print("-" * 30)
    
    print(f"{'Saldo atual:':<15} R$ {saldo:>10.2f}")
    
    print("#" * 30)

    return saldo, extrato

def filtrar_usuarios(usuarios, cpf):
    usuario_filtrado = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuario_filtrado[0] if usuario_filtrado else None

def cadastrar_usuario(usuarios):


    cpf = input("Digite seu CPF: ")
    usuario = filtrar_usuarios(usuarios, cpf)

    if usuario:
        print("Usuário já cadastrado!")
        
        return
    
    nome = input("Digite seu nome completo: ")
    data_nascimento = input("Data de nascimento (dd-mm-aaaa): ")
    endereco = input("Digite o endereço (rua,numero - bairro - cidade/estado): ")
    usuarios.append({"cpf": cpf, "nome": nome, "data_nascimento": data_nascimento, "endereço": endereco})
        
    print("usuario cadastrado com sucesso")


def criar_conta(agencia, usuarios):
    global numero_conta
    cpf = input("cpf do usuarios")
    usuario = filtrar_usuarios(usuarios, cpf)

    if usuario:
        print(f"Conta criada com sucesso.")
        return {"agencia": AGENCIA, "numero_conta": numero_conta, "usuario": usuario}
    else:
        print("Usuário não encontrado!")
        
def listar_conta(conta):
    for conta in contas:
        print(f"Conta: {conta['numero_conta']}")
        print(f"Agencia: {conta['agencia']}")
        print(f"Usuário: {conta['usuario']['nome']}")
        print(f"CPF: {conta['usuario']['cpf']}")
        print(f"Endereço: {conta['usuario']['endereço']}")
        print(f"Data de Nascimento: {conta['usuario']['data_nascimento']}")


def exibir_menu():

    global saldo, contador_saque, limite, extrato, LIMITE_SAQUE, valor_saque
    opcao = 0
    while opcao != 7:
        print("Bem-vindo  a  área do cliente no que posso ajuda-lo hoje")
        print("1 -  Saque")
        print("2 -  Depósito")
        print("3 -  Extrato")
        print("4 - Cadastrar usuario")
        print("5 -  Criar conta")
        print("6 -  listar contas")
        print("7 -  Sair")

        opcao = int(input("digite a opção desejada: "))

        if opcao == 1:
            valor_saque = float(input("Digite o valor que deseja sacar: "))        
            saldo, extrato, contador_saque = realizar_saque(
                saldo=saldo,
                valor_saque=valor_saque,
                extrato=extrato,
                limite=limite,
                contador_saque=contador_saque,
                LIMITE_SAQUE=LIMITE_SAQUE,
            )
        elif opcao == 2:
            valor_deposito = float(input("Digite o valor que deseja depositar"))
            saldo, extrato = realizar_deposito(saldo, valor_deposito, extrato)
            
        elif opcao == 3:
            saldo, extrato = exibir_extrato(saldo, extrato=extrato)

        elif opcao == 4:
            cadastrar_usuario(usuarios) 

        elif opcao == 5:
            global numero_conta
            conta = criar_conta(AGENCIA, usuarios)
            if conta:
                contas.append(conta)
                numero_conta += 1
            
        
        elif opcao == 6:
            listar_conta(contas)

        elif opcao == 7:
            print("Até logo!")
        else:
            print("Opção inválida!")
            exibir_menu()

exibir_menu()