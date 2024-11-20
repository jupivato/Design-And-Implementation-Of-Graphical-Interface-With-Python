with open("notas.txt", "w") as file:
    file.write("João: 8\n")
    file.write("Maria: 9\n")
    file.write("Ana: 7\n")
    file.write("Carlos: 10\n")
    file.write("Beatriz: 8\n")
    file.write("Luiz: 6\n")
    file.write("Fernanda: 7\n")
    file.write("Rafael: 9\n")
    file.write("Gabriela: 10\n")


with open("notas.txt", "a") as file:
    file.write("Lucas: 8\n")  


with open("notas.txt", "r") as file:
    conteudo = file.read()

print("Conteúdo atualizado do arquivo:")
print(conteudo)