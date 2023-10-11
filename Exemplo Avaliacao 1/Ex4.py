import numpy as np

# CARREGANDO UM DATASET
dataset = np.loadtxt(r'C:\Users\lucas\OneDrive\Desktop\C111\Exemplo Avaliacao 1\doc\paises.csv', delimiter = ';', dtype = str, encoding='utf-8')
america_norte = np.char.find(dataset[1:, 1], 'NORTHERN AMERICA')
total = america_norte.size - np.count_nonzero(america_norte)
print(total)