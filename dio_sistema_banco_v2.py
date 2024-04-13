import textwrap

def menu ():
    menuss = "\n[d]\tDepositar\n[s]\tSacar\n[e]\tExtrato\n[nc]\tNova conta\n[lc]\tListar contas\n[nu]\tNovo usuario\n[q]\tSair\n ==> "
    opc = input(menuss)
    return opc

def deposito(saldo, valor, extrato):

    if valor>0:
        saldo = saldo + valor
        extrato = True
        print("Extrato: {:.2f}".format(saldo))
        
    else:
        print("Valor invalido")
    
    return saldo, extrato

def saque (saldo, valor, limite, numero_saques, limite_saques):
    if(valor > saldo):
        print("Saldo Insuficiente para Saque")
    elif(valor > limite):
        print("Limite de Valor de Saque Excedido")  
    elif(numero_saques >= limite_saques):
        print("Limite de Saques Excedido")
    elif(valor <= 0):
        print("Valor invalido")
    else:
        saldo = saldo - valor
        numero_saques = numero_saques + 1
        print("Saque Realizado!")
        print("Extrato: {:.2f}".format(saldo))
    return saldo, numero_saques

def extrato_s(saldo, extrato):
    if extrato:
        return("Extrato: {:.2f}".format(saldo))
    else:
        return("Nao ha extrato disponivel")
    
def criar_usuario(usuarios):
    cpf = input("Insira o CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Usuario ja cadastrado")
        return None
    
    nome=input("Insira o nome: ")
    data_nascimento = input("Insira a data de nascimento: ")
    endereco = input("Insira o endereco: ")

    usuarios.append({"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento, "endereco": endereco})
    print("Usuario cadastrado com sucesso")

def filtrar_usuario(cpf, usuarios):
    usuario_filtro = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuario_filtro[0] if usuario_filtro else None
    
def nova_conta(agencia, numero_conta, usuarios):
    cpf = input("Insira o CPF do usuario: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print ("conta criada com sucesso")
        return {"agencia": agencia, "numero_conta": "numero_conta", "usuario": usuario}

def listar_contas(contas):
    for conta in contas:
        print("Agencia: {}".format(conta["agencia"]))
        print("Numero da Conta: {}".format(conta["numero_conta"]))
        print("Usuario: {}".format(conta["usuario"]["nome"]))
        print("CPF: {}".format(conta["usuario"]["cpf"]))
        print("Data de Nascimento: {}".format(conta["usuario"]["data_nascimento"]))
        print("Endereco: {}".format(conta["usuario"]["endereco"]))
        print("\n")

def main():
    LIMITE_SAQUES = 3
    saldo = 0.0
    limite = 500.0
    extrato = False
    numero_saques = 0
    AGENCIA = "0001"
    usuarios = []
    contas = []
    while True:
        opcao = menu()
        if opcao == "d":
            valor = float(input("Insira o valor do deposito: "))
            saldo, extrato = deposito(saldo, valor, extrato)
        elif opcao == "s":
            valor = float(input("Insira o valor do saque: "))
            saldo, numero_saques = saque(saldo, valor, limite, numero_saques, LIMITE_SAQUES)
        elif opcao == "e":
            print(extrato_s(saldo, extrato))
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = nova_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "nu":
            criar_usuario(usuarios)
        elif opcao == "q":
            break
        else:
            print("Opcao invalida")




main()