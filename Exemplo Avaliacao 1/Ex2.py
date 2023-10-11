import numpy as np

# CARREGANDO UM DATASET
dataset = np.loadtxt(r'C:\Users\lucas\OneDrive\Desktop\C111\Exemplo Avaliacao 1\doc\paises.csv', delimiter = ';', dtype = str, encoding='utf-8')

regions = np.unique(dataset[1:, 1])
qnt_regions = regions.size
print(f'Quantidade de regioes no dataset é de : {qnt_regions}')
for i in regions:
    print(i)