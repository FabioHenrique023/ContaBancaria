class ContaBancaria:
    def conta(numero, titular, saldo, limite):
        
        print("Selecione o tipo de conta: ")
        print("1. Poupança")
        print("2. Corrente")
        
        tipo_conta = int(input("Selecione digitando a opção da conta: "))
        
        if tipo_conta == 1:
            tipo_conta = "Poupança"
        if tipo_conta == 2:
            tipo_conta = "Corrente"
            
        conta = {
                "tipo_conta":tipo_conta,
                "numero":numero, 
                "titular":titular, 
                "saldo":saldo, 
                "limite": limite
                }
        return conta
    
    def depositar(conta, valor):
        conta['saldo'] += valor
        
    def saca(conta, tipo_conta, valor):
        if tipo_conta == 1:
            tipo_conta = "Poupança"
        elif tipo_conta == 2:
            tipo_conta = "Corrente"
        else:
            print("Opção inválida.")
            return
        
        if tipo_conta == conta['tipo_conta']:
            if valor <= conta['saldo'] + conta['limite']:
                if valor <= conta['saldo']:
                    conta['saldo'] -= valor
                else:
                    limite_usado = valor - conta['saldo']
                    conta['saldo'] = 0
                    conta['limite'] -= limite_usado
                print(f"R${valor:.2f} sacados da conta {tipo_conta}.")
            else:
                print("Saldo e limite insuficientes.")
        else:
            print("Tipo de conta selecionado não corresponde à conta atual.")
            
    def extrato(conta):
        print("Extrato de conta: ")
        print(f"Número da Conta: {conta['numero']}")
        print(f"Saldo da Conta: R${conta['saldo']:.2f}")
            
        
        
  