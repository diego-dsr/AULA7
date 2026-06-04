contato = {}
contato["Nome"] = input("Digite o nome: ")
contato["Telefone"] = input("Digite o telefone: ")
contato["Email"] = input("Digite o email: ")
print(contato)
x= input("O que desja alterar? ")
contato[x] = input("Digite a nova informação: ")
print(contato)

