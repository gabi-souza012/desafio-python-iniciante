import json

# Abrindo o arquivo de vendas
with open("vendas.json", "r") as arquivo:
    dados = json.load(arquivo)

# Criando as variáveis para guardar as comissões
joao = 0
maria = 0
carlos = 0
ana = 0

# Percorrendo todas as vendas
for venda in dados["vendas"]:

    vendedor = venda["vendedor"]
    valor = venda["valor"]

    # Verificando a porcentagem da comissão
    if valor < 100:
        comissao = 0
    elif valor < 500:
        comissao = valor * 0.01
    else:
        comissao = valor * 0.05

    # Somando a comissão de cada vendedor
    if vendedor == "João Silva":
        joao = joao + comissao

    elif vendedor == "Maria Souza":
        maria = maria + comissao

    elif vendedor == "Carlos Oliveira":
        carlos = carlos + comissao

    elif vendedor == "Ana Lima":
        ana = ana + comissao


# Mostrando o resultado
print("Comissão dos vendedores")
print("-----------------------")

print("João Silva: R$", round(joao, 2))
print("Maria Souza: R$", round(maria, 2))
print("Carlos Oliveira: R$", round(carlos, 2))
print("Ana Lima: R$", round(ana, 2))
