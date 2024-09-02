import json

# Carrega os dados do arquivo JSON

with open('3-faturamento_mensal.json', 'r') as f:
    faturamento_diario = json.load(f)

# Inicializa as variáveis para armazenar o menor e o maior valor de faturamento

menor_faturamento = float('inf')
maior_faturamento = 0

# Inicializa a variável para contar os dias com faturamento acima da média

dias_acima_media = 0

# Calcula a soma total do faturamento e o número de dias com faturamento

soma_faturamento = 0
dias_com_faturamento = 0
for dia, valor in faturamento_diario.items():
    if valor > 0:
        soma_faturamento += valor
        dias_com_faturamento += 1
        # Atualiza o menor e o maior valor de faturamento

        if valor < menor_faturamento:
            menor_faturamento = valor
        if valor > maior_faturamento:
            maior_faturamento = valor

# Calcula a média mensal de faturamento

media_mensal = soma_faturamento / dias_com_faturamento

# Conta os dias com faturamento acima da média

for dia, valor in faturamento_diario.items():
    if valor > media_mensal:
        dias_acima_media += 1

# Imprime os resultados

print(f"Menor valor de faturamento: {menor_faturamento}")
print(f"Maior valor de faturamento: {maior_faturamento}")
print(f"Número de dias com faturamento acima da média: {dias_acima_media}")
