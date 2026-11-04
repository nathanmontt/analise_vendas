with open("pedidos.csv", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        dados = linha.strip().split(";")
        print(dados)