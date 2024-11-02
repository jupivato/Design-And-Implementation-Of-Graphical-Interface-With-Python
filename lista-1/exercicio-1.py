valor_conta = int(input("Digite o valor da conta: "))
percentual_desconto = int(input("Digite o percentual de desconto: "))
valor_conta = valor_conta - (valor_conta * percentual_desconto / 100)
print(valor_conta)