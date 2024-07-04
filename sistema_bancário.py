 

escolha = int(input('''
    digite 1 - para Depósito
    digite 2 - para saque
    digite 3 - para extrato
    digite 4 - para sair
opção:  '''))


extrato_saque = ''
extrato_deposito = ''
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3
saldo = 0
saque = 0

while True:
    

    if escolha == 1:
        deposito = float(input('Digite qual valor deseja depositar: '))
        if deposito <= 0:
            print('valor inválido.')
        
        elif deposito > 0:
            extrato_deposito = 'Valor depositado: R$ ', deposito
            saldo += deposito
            print(f'''valor de R${deposito :.2f} depositado! \n''')                        
            menu = str(input('Deseja executar mais alguma ação? digite [s] para sim e [n] para não: ')).lower()
            
            if menu == 's':
                escolha = int(input('''
    digite 1 - para Depósito
    digite 2 - para saque
    digite 3 - para extrato
    digite 4 - para sair
opção:  '''))
                
            if menu == 'n':
                print('Obrigado por utilizar nosso serviços.')               
            
                break        
            
        
    elif escolha == 2:
        

        saque = float(input('Digite qual valor deseja sacar: '))

        if saque > limite:
            print('Limite de R$500,00 por saque excedido.') 

        if saque > saldo:
            print('saldo insuficiente')

        elif saque <= 0:
            print('valor inválido.')
        
        elif saque > 0 and saque < saldo and saque <= limite:
            extrato_saque = 'Valor sacado: R$', saque
            numero_saques += 1
            saldo -= saque
            print(f'saque de R${saque :.2f} concluído.  ')
            menu = str(input('Deseja executar mais alguma ação? digite [s] para sim e [n] para não: ')).lower()
            
            
            if menu == 's':
                escolha = int(input('''
    digite 1 - para Depósito
    digite 2 - para saque
    digite 3 - para extrato
    digite 4 - para sair
opção:  '''))
                
            if menu == 'n':
                print('Obrigado por utilizar nosso serviços.')   

                break

        if numero_saques == LIMITE_SAQUES:
            print('limite de saques excedido.')
            if menu == 's':
                escolha = int(input('''
    digite 1 - para Depósito
    digite 2 - indisponível
    digite 3 - para extrato
    digite 4 - para sair
opção:  '''))
                
            if menu == 'n':
                print('Obrigado por utilizar nosso serviços.')   

            break
                                   

    if escolha == 3:

        if extrato_deposito == '' and extrato_saque == '':
            print('nenhuma movimentação bancária realizada.'if not extrato else extrato)

            
        elif saque == 0:
            print(f'''aqui está seu extrato:
Valor depositado:R${extrato_deposito}                  

saldo : R${saldo :.2f}''')
            
        elif saque in extrato_saque and deposito in extrato_deposito :
            print(f'''aqui está seu extrato:
Valor depositado:R${extrato_deposito}
Valor sacado:R${extrato_saque}                  

saldo : R${saldo :.2f}''')
            
        menu = str(input('Deseja executar mais alguma ação? digite [s] para sim e [n] para não: ')).lower()
            
            
        if menu == 's':
            escolha = int(input('''
    digite 1 - para Depósito
    digite 2 - para saque
    digite 3 - para extrato
    digite 4 - para sair
opção:  '''))
          
            
        break
        
    if escolha == 4:
        print('Obrigado por utilizar nosso serviços.')
        break
    

    elif escolha < 1 and escolha > 4:
        print('operação inválida,selecione novamente a opção desejada.')
        



   

    


    


















