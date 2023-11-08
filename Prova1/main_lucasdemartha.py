import numpy as np

dataset = np.loadtxt(r'C:\Users\lucas\OneDrive\Desktop\C111\Prova1\shopping_trends.csv', delimiter=',', dtype=str, encoding='utf-8')

#Exercicio 1

idade = np.array(dataset[1:, 1], dtype=float)
media_idade = np.mean(idade)

print('Exercicio 1')
print(f'A media de idades e: {media_idade:.2f}')

print('=============================================================')

#Exercicio 2

valor = dataset[1:, 5]
CemOuMais = np.sum(np.array(dataset)[1:, 5] >= '100')

print('Exercicio 2')
print(f'Clientes que gastaram 100 ou mais em compras: {CemOuMais}')

print('=============================================================')

#Exercicio 3

itens = dataset[1:, 3]
total = len(itens)
maior = np.argmin(itens)
porcentagem = (maior * 100) / total

print('Exercicio 3')
print(f'A porcentagem do item menos vendido e: {porcentagem:.2f}%')

print('=============================================================')

#Exercicio 4

pagamento = dataset[1:, 16]
total = len(pagamento)
CemOuMais = np.sum(np.array(dataset)[1:, 16] == 'Venmo')
porcentagem = (CemOuMais * 100) / total

print('Exercicio 4')
print(f'A porcentagem de compras utilizando Venmo e: {porcentagem:.2f}%')

print('=============================================================')

#Exercicio 5

cor = dataset[1:, 8]
estacao = dataset[1:, 9]
verao = np.where(estacao == 'Summer')
maior = np.argmax(cor[verao])
corMaior = cor[verao][maior]

print('Exercicio 5')
print(f'A cor mais usada no verao e: {corMaior}')