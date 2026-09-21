from datetime import date
from datetime import datetime

# Pedir o valor da conta
valor = float(input("Digite o valor da conta: R$ "))

# Pedir a data de vencimento
data = input("Digite a data de vencimento (dd/mm/aaaa): ")

# Transformar a data em uma data que o Python consegue calcular
data_vencimento = datetime.strptime(data, "%d/%m/%Y").date()

# Pegar a data de hoje
data_hoje = date.today()

# Verificar se a conta está atrasada
if data_hoje > data_vencimento:

    # Calcular os dias de atraso
    dias_atraso = (data_hoje - data_vencimento).days

    # Calcular os juros
    juros = valor * 0.025 * dias_atraso

    # Calcular o valor final
    valor_final = valor + juros

    print("\nRESULTADO")
    print("Valor da conta: R$", valor)
    print("Dias de atraso:", dias_atraso)
    print("Juros: R$", round(juros, 2))
    print("Valor final: R$", round(valor_final, 2))

else:

    print("\nA conta não está atrasada.")
    print("Valor da conta: R$", valor)
