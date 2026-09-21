import json

# Ler o arquivo JSON
arquivo = open("estoque.json", "r")
dados = json.load(arquivo)
arquivo.close()

# Mostrar os produtos
print("ESTOQUE")
print("-------")

for produto in dados["estoque"]:
    print("Código:", produto["codigoProduto"])
    print("Produto:", produto["descricaoProduto"])
    print("Quantidade:", produto["estoque"])
    print()

# Pedir o código do produto
codigo = int(input("Digite o código do produto: "))

# Procurar o produto
for produto in dados["estoque"]:

    if produto["codigoProduto"] == codigo:

        print("\nProduto encontrado")
        print("Produto:", produto["descricaoProduto"])
        print("Quantidade atual:", produto["estoque"])

        tipo = input("Digite E para entrada ou S para saída: ")
        quantidade = int(input("Digite a quantidade: "))
        descricao = input("Digite a descrição da movimentação: ")

        if tipo == "E":

            produto["estoque"] = produto["estoque"] + quantidade

        elif tipo == "S":

            if quantidade <= produto["estoque"]:
                produto["estoque"] = produto["estoque"] - quantidade
            else:
                print("Quantidade maior que o estoque.")

        else:
            print("Movimentação inválida.")

        print("\nMOVIMENTAÇÃO")
        print("Número: 1")
        print("Descrição:", descricao)
        print("Estoque final:", produto["estoque"])
