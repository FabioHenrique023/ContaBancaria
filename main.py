from ContaBancaria import ContaBancaria

#<-- FUNÇÃO CONTA -->

conta = ContaBancaria.conta('12345', 'João', 1000.0, 500.0)

print(f"\nTipo da conta: ", conta['tipo_conta'])
print("Número da conta: ", conta['numero'])
print("Titular da conta: ", conta['titular'])
print("Saldo da conta: ", conta['saldo'])
print("Limite da conta: ", conta['limite'])

print("\n")

#<-- FUNÇÃO EXTRATO -->

#ContaBancaria.extrato(conta)

#<-- FUNÇÃO DEPOSITO -->

# deposito = ContaBancaria.depositar(conta, 200.0)
# print("Saldo antes do saque:", conta['saldo'])
# print("Limite disponível:", conta['limite'])


#<-- FUNÇÃO SAQUE -->

# tipo_conta = int(input("Selecione o tipo de conta (1 para Poupança, 2 para Corrente): "))
# valor_saque = float(input("Digite o valor a sacar: "))
# ContaBancaria.saca(conta, tipo_conta, valor_saque)
# print("Saldo após o saque:", conta['saldo'])
# print("Limite após o saque:", conta['limite'])