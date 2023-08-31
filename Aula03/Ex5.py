import numpy as np
'''
matriz = np.random.randint(0, 10, (5, 6))

linhas = matriz.shape[0]
colunas = matriz.shape[1]

total_elementos = linhas * colunas

if total_elementos % 2 == 0:
  print("A matriz pode se tornar um vetor com numero par de elementos")
else:
  print("A matriz pode se tornar um vetor com numero ímpar de elementos")
'''

# Criar uma matriz 4x5 de exemplo
matriz = np.array([[1, 2, 3, 4, 5],
                   [6, 7, 8, 9, 10],
                   [11, 12, 13, 14, 15],
                   [16, 17, 18, 19, 20]])

# Obter número de linhas e colunas
num_linhas, num_colunas = matriz.shape

# Calcular o produto entre o número de linhas e colunas
produto = num_linhas * num_colunas

# Verificar se o produto é par ou ímpar
resultado = "par" if produto % 2 == 0 else "ímpar"

print("Matriz:")
print(matriz)
print(f"Numero de linhas: {num_linhas}")
print(f"Numero de colunas: {num_colunas}")
print(f"Produto (linhas x colunas): {produto}")
print(f"A matriz poderia se tornar um vetor com um numero {resultado} de elementos.")