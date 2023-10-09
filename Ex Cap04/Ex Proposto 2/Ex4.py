import numpy as np

# Define a semente (seed)
np.random.seed(10)

# Cria uma matriz 4x4 de números inteiros aleatórios entre 1 e 50
mtz = np.random.randint(1, 50, 16)  # 16 números aleatórios entre 1 e 50
mtz = mtz.reshape(4, 4)  # transforma o array em uma matriz 4x4

# Conta a quantidade de vezes que cada número aparece na matriz
unique_numbers, counts = np.unique(mtz, return_counts=True)

# Mostra a quantidade de aparições de cada número
for num, count in zip(unique_numbers, counts):
    print(f"Numero {num} aparece {count} vezes")

# Mostra apenas os números que aparecem duas vezes
print("\nNumeros que aparecem duas vezes:")
for num, count in zip(unique_numbers, counts):
    if count == 2:
        print(num)
