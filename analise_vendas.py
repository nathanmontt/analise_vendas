import csv

# deixando o arquivo aberto para uso
with open("pedidos.csv", "r", encoding="utf-8", newline="") as arquivo:

    # objeto especializado em ler registros CSV na forma de dicionário
    leitor = csv.DictReader(arquivo, delimiter=";")

    # antes da limpeza, mostrando cada linha do dicionario, além de outros testes
    for each_line in leitor:
        print(each_line)
        # print(each_line["pedido"])
        # print(each_line["peso_kg"])