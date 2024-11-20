import pandas as pd

dados = {
    "Nome": ["Carlos", "Pedro", "Ana", "Fernanda"],
    "Idade": [25, 35, 28, 45],
    "Salário": [2500, 3500, 2800, 4200]
}
df = pd.DataFrame(dados)

idade_maior_30 = df[df["Idade"] > 30]
print("Empregados com idade maior que 30:")
print(idade_maior_30)

salario_maior_3000 = df[df["Salário"] > 3000]
print("\nEmpregados com salário maior que 3000:")
print(salario_maior_3000)