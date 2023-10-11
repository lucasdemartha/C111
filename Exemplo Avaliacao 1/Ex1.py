import numpy as np

# CARREGANDO UM DATASET
dataset = np.loadtxt(r'C:\Users\lucas\OneDrive\Desktop\C111\Exemplo Avaliacao 1\doc\paises.csv', delimiter = ';', dtype = str, encoding='utf-8')
arr = dataset[0:, 0:5]

print(arr)