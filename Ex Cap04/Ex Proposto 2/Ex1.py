import numpy as np

# Definir a semente para garantir reprodutibilidade
np.random.seed(5)

# Criar um array de 10 números aleatórios entre 0 e 1 (positivos e negativos)
array_floats = (np.random.rand(10) - 0.5) * 2

# Multiplicar os valores por 100
array_floats *= 100

# Criar um novo vetor apenas com a parte inteira dos números
array_inteiros = np.floor(array_floats).astype(int)

print("Array de floats:")
print(array_floats)
print("Array de inteiros:")
print(array_inteiros)
