import numpy as np

# Define a semente (seed)
np.random.seed(10)

# Cria uma matriz 4x4 de números inteiros aleatórios entre 1 e 50
mtz = np.random.randint(1, 50, 16) # 16 numeros aleatorios entre 1 e 50
mtz = mtz.reshape(4, 4) # transforma o array em uma matriz 4x4

# Calcula a média das linhas e colunas
media_linhas = np.mean(mtz, axis=1)
media_colunas = np.mean(mtz, axis=0)

# Encontra o maior valor entre as médias das linhas e das colunas
maior_media_linhas = np.max(media_linhas)
maior_media_colunas = np.max(media_colunas)

# Imprime as médias das linhas e das colunas
print("Media das Linhas:")
for i, media in enumerate(media_linhas):
    print(f"Linhas {i + 1}: {media}")

print("\nMedia das Colunas:")
for i, media in enumerate(media_colunas):
    print(f"Coluna {i + 1}: {media}")

# Imprime o maior valor entre as médias das linhas e das colunas
print("\nMaior Media das Linhas:", maior_media_linhas)
print("Maior Media das Colunas:", maior_media_colunas)
