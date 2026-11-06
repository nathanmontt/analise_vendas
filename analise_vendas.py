# import csv

# # deixando o arquivo aberto para uso
# with open("pedidos.csv", "r", encoding="utf-8", newline="") as arquivo:

#     # objeto especializado em ler registros CSV na forma de dicionário
#     leitor = csv.DictReader(arquivo, delimiter=";")

#     # antes da limpeza, mostrando cada linha do dicionario, além de outros testes
#     for each_line in leitor:
#         print(each_line)
#         # print(each_line["pedido"])
#         # print(each_line["peso_kg"])

#     print(f"{'CLIENTE':<12} {'PESO':>10} {'PREÇO/KG':>12}")
#     print("-" * 36)

    
    
#     for linha in leitor:
#         print("Cliente:", linha["cliente"])
#         print("Peso:", linha["peso_kg"])
#         print("------------------")



import csv

with open("pedidos.csv", "r", encoding="utf-8", newline="") as arq:
    content = csv.DictReader(arq, delimiter=";")

    for each_line in content:
        pedido = each_line["pedido"].strip()
        cliente = each_line["cliente"].strip().capitalize()
        peso_kg = each_line["peso_kg"].strip()
        valor_kg = float(each_line["valor_kg"].strip().replace(",","."))
        status = each_line["status"].strip()

        print(f"{'PEDIDO':<12}{'CLIENTE':<12} {'PESO':>10} {'PREÇO/KG':>12}")
        print(f"{pedido}{cliente:>14}{"Sem peso" if not peso_kg else peso_kg:>18}{"R$" + format(valor_kg, '.2f'):>13}")
        print("-" * 48)
