import numpy as np

# CARREGANDO UM DATASET
dataset = np.loadtxt(r'C:\Users\lucas\OneDrive\Desktop\C111\Exemplo Avaliacao 1\doc\paises.csv', delimiter = ';', dtype = str, encoding='utf-8')
america_sul_caribe = dataset[1:, 1]
america_sul_caribe_GDP = np.array(dataset[1:, 8], dtype=np.int32)
GDP = 0
pos = 0
for i in range(len(america_sul_caribe)):
    if america_sul_caribe[i] == 'LATIN AMER. & CARIB    ' and america_sul_caribe_GDP[i] > int(GDP):
        pos = i+1
        GDP = america_sul_caribe_GDP[i]
        
print(dataset[pos, 0])