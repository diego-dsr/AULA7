contatos = {"Diego": "123-456-7890", "Wal": "987-654-3210", "Bruce": "555-555-5555"}

nome = input("Digite o nome do contato: ")
if nome in contatos:
    print(f"O número de telefone de {nome} é: {contatos[nome]}")
else:
    print("Contato não encontrado.")