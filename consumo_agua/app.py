print("=== SISTEMA DE CONSUMO DE ÁGUA ===")

tipo = input("Digite o tipo de imóvel (comercial, casa ou apartamento): ").lower()
consumo = float(input("Digite o consumo mensal de água em m³: "))

if tipo == "comercial":
    print("Tarifa comercial aplicada – consulte o plano corporativo.")

elif tipo == "apartamento" and consumo < 10:
    print("Consumo econômico – excelente controle de água!")

elif tipo == "apartamento" and consumo >= 10 and consumo <= 25:
    print("Consumo moderado – dentro do padrão residencial.")

else:
    print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")