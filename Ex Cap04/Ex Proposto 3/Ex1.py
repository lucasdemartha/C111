import numpy as np

# CARREGANDO UM DATASET
dataset = np.loadtxt('C:/Users/User/Desktop/C111/Ex Cap04/Ex Proposto 3/doc/space.csv', delimiter = ';', dtype = str, encoding = 'utf-8')

#mostrar quantas missoes deram certo

sucesso = dataset[dataset[:, 7] == 'Success']
print(sucesso.shape[0])
