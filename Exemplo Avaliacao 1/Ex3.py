import numpy as np

# CARREGANDO UM DATASET
dataset = np.loadtxt(r'C:\Users\lucas\OneDrive\Desktop\C111\Exemplo Avaliacao 1\doc\paises.csv', delimiter = ';', dtype = str, encoding='utf-8')

literacy = np.array(dataset[1:, 9], dtype=float)
print(round(np.mean(literacy), 2))