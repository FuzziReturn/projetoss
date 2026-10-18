# Solicita ao usuário o valor total da compra
valor = float(input("Digite o valor total da compra: R$ "))

# Verifica qual desconto deve ser aplicado
if valor < 200:
    desconto = 0.05  # 5% de desconto

elif valor < 300:
    desconto = 0.10  # 10% de desconto

else:
    desconto = 0.15  # 15% de desconto

# Calcula o valor do desconto
valor_desconto = valor * desconto

# Calcula o valor final da compra
valor_final = valor - valor_desconto

# Exibe os resultados
print("Valor da compra: R$", valor)
print("Percentual de desconto:", desconto * 100, "%")
print("Valor do desconto: R$", valor_desconto)
print("Valor final a pagar: R$", valor_final)