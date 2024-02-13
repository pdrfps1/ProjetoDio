menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=>"""

saldo = 0 
limite = 500
extrato = ""
numeroDeSaques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input (menu)

    if opcao == "d":
        print ("Deposito")
        valor = float(input('Digite o valor do depósito: '))
        
        if valor == 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            
    elif opcao == "s":
        valor = int(input ("Informe o valor do saque: "))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numeroDeSaques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Operação falhou! Voce não tem saldo suficiente.")
            
        if excedeu_limite:
            print ("Operação falhou! O valor do saque excede o limite.")
            
        if excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
            
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numeroDeSaques += 1
            
        else:
            print ("Operação falhou! O valor informado é inválido")
            
    elif opcao == "e":
        print ("\n==================Extrato==================")
        print ("Não foram realizadas movimentações." if not extrato else extrato)
        print (f"\nSaldo: R${saldo:.2f}")
        print ("===========================================")
    
    elif opcao == "q":
        print('Saindo...')
        break
    else:
        print("Operação invalida, por favor selecione novamente a operação desejada.")