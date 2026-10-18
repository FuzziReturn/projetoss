
TOTAL_ENTREVISTADOS = 10  

qtd_excelente = 0
qtd_ruim = 0

print("=== PESQUISA DE SATISFAÇÃO - TUDOWEB ===")

for i in range(1, TOTAL_ENTREVISTADOS + 1):
    print(f"\n--- Entrevistado {i} de {TOTAL_ENTREVISTADOS} ---")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    
    print("Opinião: 1- EXCELENTE | 2- BOM | 3- RUIM")
    opiniao = int(input("Opção: "))
    
   
    match opiniao:
        case 1:
            qtd_excelente += 1
        case 3:
            qtd_ruim += 1


print("\n=== RESULTADO ===")
print(f"a) Quantidade de respostas 'EXCELENTE': {qtd_excelente}")
print(f"b) Quantidade de respostas 'RUIM': {qtd_ruim}")