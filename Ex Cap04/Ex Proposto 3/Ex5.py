import numpy as np

# CARREGANDO UM DATASET
dataset = np.loadtxt('C:/Users/User/Desktop/C111/Ex Cap04/Ex Proposto 3/doc/space.csv', delimiter=';', dtype=str, encoding='utf-8')

# Pular a primeira linha (cabeçalho)
data = dataset[1:]

# Criar um dicionário para armazenar as contagens de missões por empresa
contagem_missões_por_empresa = {}

# Iterar pelos dados e contar as missões por empresa
for linha in data:
    empresa = linha[1]  # A empresa está na coluna de índice 1
    if empresa in contagem_missões_por_empresa:
        contagem_missões_por_empresa[empresa] += 1
    else:
        contagem_missões_por_empresa[empresa] = 1

# Mostrar as informações
for empresa, quantidade in contagem_missões_por_empresa.items():
    print(f"A empresa '{empresa}' realizou {quantidade} missioes espaciais.")
