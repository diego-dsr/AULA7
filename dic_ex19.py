estoque = {"maça": 10, "banana": 5, "laranja": 8}

for fruta, quantidade in estoque.items():
    x= input("O que desja saber? ")

    if x == fruta:
        print(f"A quantidade de {fruta} em estoque é: {quantidade}")