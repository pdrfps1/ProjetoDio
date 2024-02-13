import textwrap


def menu():
    menu = """\n
    ============== Menu ==============
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar conta
    [nu]\tNovo usuario
    [q]\tSair
    =>"""
    return input(textwrap.dedent(menu))


def depositar (saldo, valor, extrato, /):
    if valor > 0:
        saldo -= valor
        extrato += f"Saque: R${valor:.2f}\n"
        print ("\n === Depósito realizado com sucesso! ===")
    else:
        print ("\n@@@ Operação falhou! O valor informado é invalido. @@@")
    return saldo, extrato
        
def sacar (*, saldo, valor, extrato, limite, numeroDeSaques, LIMITE_SAQUES):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numeroDeSaques >= LIMITE_SAQUES
                
    if excedeu_saldo:
        print("\n@@@ Operação falhou! Voce não tem saldo suficiente. @@@")
                    
    if excedeu_limite:
        print ("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
                    
    if excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
    elif valor > 0:
        saldo -= valor 
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numeroDeSaques += 1
        print ("\n=== Saque Realizado com sucesso! ===")
    else:
        print ("\n@@@ Operação falhou! O valor informado é invalido. @@@")
    
    return saldo, extrato    
        
def exibir_extrato(saldo, /, *, extrato):     
    print ("\n==================Extrato==================")
    print ("Não foram realizadas movimentações." if not extrato else extrato)
    print (f"\nSaldo: R${saldo:.2f}")
    print ("===========================================")
            
def criar_usuario(usuario):
    cpf = input("Informe o seu cpf (somente numero): ")
    usuario = filtrar_usuario(cpf,usuario)
    
    if usuario:
        print ("\n@@@ Já existe usuario com esse CPF! @@@")
        return
    
    nome = input ("Informe o nome completo")
    data_nasc = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereco (Rua e numero): ")
    usuario.append ({"nome":nome, "data_nasc": data_nasc,"cpf": cpf, "endereco": endereco})
    
    print ("=== Usuario criado com sucesso! ===")

def filtrar_usuario(cpf, usuario):
    usuario_filtrado = [usuario for usuario in usuario if usuario["cpf"] == cpf]    
    return usuario_filtrado[0] if usuario_filtrado else None

def criar_contas(agencia, numero_conta, usuario):
    cpf = input("Informe o cpf do usuario: ")
    usuario = filtrar_usuario(cpf, usuario)
    
    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia,"numero_conta": numero_conta,"usuario": usuario}
    print ("\n@@@ Usuario não encontrado, fluxo de criação de conta encerrado! @@@")
    
def listar_contas (contas):
    for conta in contas:
        linha = f"""\
            Agencia:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t\t{conta[['usuario']['nome']]}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))
        
def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0 
    limite = 500
    extrato = ""
    numeroDeSaques = 0
    usuario=[]
    contas=[]
    

    while True:
        opcao = input (menu)
        if opcao == "d":    
            valor = float(input('Digite o valor do depósito: '))
            saldo, extrato = depositar (saldo, valor, extrato)
            
        elif opcao == "s":
            sacar(saldo)
            
        elif opcao == "e":
            exibir_extrato(saldo, extrato = extrato)
            
        elif opcao == "nu":
            criar_usuario(usuario)
        
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_contas(AGENCIA, numero_conta, usuario)
            
            if conta:
                contas.append(conta)
                
        elif opcao == "lc":
            listar_contas(contas)
            
        elif opcao == "q":
            print('Saindo...')
            break
        else:
            print("Operação invalida, por favor selecione novamente a operação desejada.")
main()