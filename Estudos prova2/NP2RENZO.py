import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

cars = pd.read_csv('electric_cars.csv', delimiter=',')


def delimiter():
    print('---------------------------------')


# Questão 1 - Mostre o(s) nome(s) e a(s) capacidade(s) de bateria do(s) veículo(s) que chega(m) de
# 0 a 100 km/h em menos de 3s;

print(f'Questão 1')
carrosRapidos = cars[cars['acceleration..0.100.'] < 3]

for index, row in carrosRapidos.iterrows():
    print("Nome do Veículo:", row['Car_name'])
    print("Capacidade da Bateria:", row['Battery'])
    print("-----------------------------")

delimiter()

# Questão 2 - Qual a eficiência média de um veículo elétrico segundo este dataset?

print(f'Questão 2')

mediaEficiencia = cars['Efficiency'].mean()
print(f'A média da eficiência dos veículos é: {mediaEficiencia}')

delimiter()

# Questão 3 - Qual é o carro elétrico mais barato da empresa Tesla?

print(f'Questão 3')

indiceMin = cars[cars['Car_name'].str.contains('Tesla')]['Price.DE.'].idxmin()
maisBarato = cars.loc[indiceMin]
print(f'O carro elétrico mais barato da emprsa Tesla é o:', maisBarato['Car_name'])

delimiter()

# Questão 4 - Trace um gráfico em barras ilustrando o(s) veículo(s) mais lento(s) e o(s) mais
# rápido(s) deste dataset (extremos);

print(f'Questão 4')

slowestCar = cars.loc[cars['Top_speed'].idxmin()]
fastestCar = cars.loc[cars['Top_speed'].idxmax()]

plt.bar(['Mais Lento', 'Mais Rápido'], [slowestCar['Top_speed'],
        fastestCar['Top_speed']], color=['blue', 'orange'])

plt.ylabel('Velocidade Máxima')
plt.title('Carro mais lento vs. Carro mais rápido')

plt.show()

delimiter()

# Questão 5 - Trace um gráfico de dispersão que ilustre a capacidade de bateria dos 4 carros mais
# velozes da empresa BYD;

print(f'Questão 5')

BYDCars = cars[cars['Car_name'].str.contains('BYD')]
BYDCars = cars.nlargest(4, 'Top_speed')
# print(BYDCars)

plt.scatter(BYDCars['Battery'], BYDCars['Top_speed'], color='purple',
            s=BYDCars['Battery'])

plt.xlabel('Capacidade da Bateria')
plt.ylabel('Velocidade Máxima')
plt.title(
    'Capacidade de bateria dos 4 carros mais velozes da BYD')

plt.show()

delimiter()
