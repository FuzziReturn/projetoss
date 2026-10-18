# ⚡ Calculadora de Consumo de Energia e Custo Mensal

Projeto em Python desenvolvido para calcular o consumo elétrico mensal (em kWh) e estimar o custo em reais (R$) de eletrodomésticos, utilizando como referência a tarifa média de energia de **São Paulo (Enel SP)**.


### 🚀 Tecnologias Utilizadas
* **Python 3** (Linguagem de programação)


### 🛠️ Funcionalidades
- Entrada do nome do aparelho doméstico.
- Leitura da potência em watts ($W$).
- Leitura das horas médias de uso por dia.
- Cálculo automático do consumo mensal ($kWh$):
  $$\text{consumoMensal} = \frac{\text{potencia} \times \text{horasDia} \times 30}{1000}$$
- Cálculo do custo estimado mensal ($R\$$) com base na tarifa de São Paulo ($\text{R\$ } 0,78\text{/kWh}$):
  $$\text{custoEstimado} = \text{consumoMensal} \times 0.78$$

### 💻 Como Executar o Projeto

1. **Clone este repositório:**
   ```Terminal
  [https://github.com/FuzziReturn/projetos/tree/main/consumo-energia]