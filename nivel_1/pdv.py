
historico = []

while True:
    valor = float(input("Digite o valor da compra: R$ "))

    if valor == 0:
        break

    if valor < 0:
        print("Valor inválido! Digite um valor positivo.")
        continue

    idade = int(input("Digite sua idade: "))

    if idade < 0:
        print("Idade inválida! Insira um valor válido novamente.")
        continue

    valor_original = valor
    calculo = valor

    if idade >= 65:
        calculo = calculo * 0.80

    if calculo > 100:
        calculo = calculo * 0.90

    desconto = valor_original - calculo

    print(f"O valor final é: R$ {calculo:.2f}")

    compra = [valor_original, desconto, calculo]
    historico.append(compra)


quantidade = len(historico)
total_bruto = 0
total_descontos = 0
total_final = 0

for compra in historico:
    total_bruto += compra[0]
    total_descontos += compra[1]
    total_final += compra[2]

print("\n===== RESUMO DO DIA =====")
print(f"Quantidade de compras: {quantidade}")
print(f"Total bruto: R$ {total_bruto:.2f}")
print(f"Total de descontos: R$ {total_descontos:.2f}")
print(f"Total final: R$ {total_final:.2f}")



