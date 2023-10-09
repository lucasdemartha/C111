import numpy as np

# CARREGANDO UM DATASET
dataset = np.loadtxt('C:/Users/User/Desktop/C111/Ex Cap04/Ex Proposto 3/doc/space.csv', delimiter=';', dtype=str, encoding='utf-8')

# Pular a primeira linha (cabeçalho)
data = dataset[1:]

# Encontrar as linhas onde "USA" está presente em qualquer parte da coluna
usa_indices = np.char.find(data[:, 2], 'USA')

# Filtrar as linhas onde "USA" foi encontrado (usa_indices >= 0)
usa_missions = data[usa_indices >= 0]

# Contar o número de missões espaciais dos EUA encontradas
num_usa_missions = usa_missions.shape[0]

print("Numero de missoes espaciais realizadas pelos EUA:", num_usa_missions)
