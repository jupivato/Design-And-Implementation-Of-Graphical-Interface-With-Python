valor_conta = float(input("Digite o valor da conta: "))
percentual_desconto = float(input("Digite o percentual de desconto: "))
valor_conta = valor_conta - (valor_conta * percentual_desconto / 100)
print(f"{valor_conta:.2f}")