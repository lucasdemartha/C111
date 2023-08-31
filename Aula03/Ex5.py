import numpy as np

matriz = np.random.randint(0, 10, (5, 6))

linhas = matriz.shape[0]
colunas = matriz.shape[1]

total_elementos = linhas * colunas

if total_elementos % 2 == 0:
  print("A matriz pode se tornar um vetor com numero par de elementos")
else:
  print("A matriz pode se tornar um vetor com numero ímpar de elementos")