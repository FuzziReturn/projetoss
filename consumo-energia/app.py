# Valor de referência da tarifa de energia em São Paulo (Enel SP)
TARIFA_KWH_SP = 0.78  # em R$/kWh

# Entrada de dados
aparelho = input("Digite o nome do aparelho (ex.: Micro-ondas): ")
potencia = float(input("Digite a potência do aparelho em watts (W): "))
horas_dia = float(input("Digite o tempo médio de uso diário em horas: "))

# Processamento / Cálculos
consumo_mensal = (potencia * horas_dia * 30) / 1000
custo_estimado = consumo_mensal * TARIFA_KWH_SP

# Saída de dados
print(f"\n--- Resultado para {aparelho} ---")
print(f"Consumo mensal estimado: {consumo_mensal:.2f} kWh")
print(f"Custo mensal estimado (Referência SP - R$ {TARIFA_KWH_SP}/kWh): R$ {custo_estimado:.2f}")