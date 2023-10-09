import numpy as np

# CARREGANDO UM DATASET
dataset = np.loadtxt('C:/Users/User/Desktop/C111/Ex Cap04/Ex Proposto 3/doc/space.csv', delimiter=';', dtype=str, encoding='utf-8')

# Pular a primeira linha (cabeçalho)
data = dataset[1:]

# Filtrar missões realizadas pela SpaceX
spacex_missions = data[data[:, 1] == 'SpaceX']

# Encontrar a missão mais cara
max_cost_index = np.argmax(spacex_missions[:, 6].astype(float))
most_expensive_mission = spacex_missions[max_cost_index]

print("A missao mais cara da SpaceX foi:", most_expensive_mission)
