print("1=Incluir usuário")
print("2=Excluir usuário")
print("3=Consultar usuário")
print("4=Alterar usuário")
print("5=Listar todos os usuários que estão cadastrados")
print("9=Sair")

opcao = int(input("Digite a opção desejada: "))

while(opcao != 9):
    match opcao:
        case 1:
            print("1=Incluir usuário")
        case 2:
            print("2=Excluir usuário")
        case 3:
            print("3=Consultar usuário")
        case 4:
            print("4=Alterar usuário")
        case 5:
            print("5=Listar todos os usuários que estão cadastrados")
        case _:
            print("Opcao invalida")
            
    opcao = int(input("Digite a opção desejada: "))