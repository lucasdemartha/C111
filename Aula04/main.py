import numpy as np

'''
#NUMEROS ALEATORIOS (RANDOM)
#RANDOM SEED
np.random.seed(10) # fixa a semente para que os numeros aleatorios sejam sempre os mesmos

arr = np.random.randint(1, 30, 15) # 15 numeros aleatorios entre 1 e 30
print(arr)

# EXTRAIR ELEMENTOS UNICOS
#print(set(arr)) # set() retorna os elementos unicos de um array
print(np.unique(arr, return_counts=True)) # retorna os elementos unicos e a quantidade de vezes que eles aparecem
'''
'''
# OPERACOES EM MATRIZES
mtz = np.random.randint(1, 20, 12) # 12 numeros aleatorios entre 1 e 20
mtz = mtz.reshape(3, 4) # transforma o array em uma matriz 3x4
print(mtz)
print(mtz.sum(axis = 0))
print(mtz.sum(axis = 1)[0])

# BROADCASTING
print(mtz*10)
print(mtz-3)

# CONDICIONAIS DO NUMPY
print(mtz%2==0) # retorna uma matriz booleana com True para os elementos pares e False para os impares
print(mtz[mtz%2==0]) # retorna uma matriz com os elementos pares
print(mtz[mtz<10]) # retorna uma matriz com os elementos menores que 10

# LIDANDO COM TEXTOS NO NUMPY
arr = np.array(['Lucas', 'Ana', 'Ari', 'Maycon'])
print(np.char.find(arr, 'A')) # retorna a posicao da primeira letra 'A' em cada elemento do array
print(arr[np.char.find(arr, 'A')>-1])
'''

# CARREGANDO UM DATASET
dataset = np.loadtxt('Aula04\doc\space.csv', delimiter = ';', dtype = str, encoding = 'utf-8')
print(dataset[0,:])