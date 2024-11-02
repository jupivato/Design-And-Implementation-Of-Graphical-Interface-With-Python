altura = float(input("Digite a altura: "))
sexo = (input("Digite o sexo (f/m): "))

if sexo == "m":
    peso_ideal = (72.7 * altura) - 58
elif sexo == "f":
    peso_ideal = (62.1 * altura) - 44.7
else:
    print("Opcao invalida")
    
print("Peso ideal: ", peso_ideal)