numero = int(input("Digite um número: "))

contador = 0
soma = 0
media = 0
maior = numero
negativo = 0

while(True):
    if(numero > maior):
        maior = numero
        
    contador += 1
    soma += numero
    media += numero
    
    if (numero < 0):
        negativo = numero
        break
    numero = int(input("Digite um número: "))
    
print("Maior número: ", maior)
print("Soma: ", soma)
print("Média: ", media/contador)
print("Numeros negativos: ", negativo)
    