import numpy as np

# Define a semente (seed)
np.random.seed(10)

# Cria uma matriz 4x4 de números inteiros aleatórios entre 1 e 50
mtz = np.random.randint(1, 50, 16) # 16 numeros aleatorios entre 1 e 50
mtz = mtz.reshape(4, 4) # transforma o array em uma matriz 4x4

# Imprime a matriz
for i in mtz:
    print(i)
