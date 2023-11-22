import numpy as np
import pandas as pd

#LENDO UM ARQUIVO .CSV

dfPaises = pd.read_csv(r'C:\Users\User\Desktop\C111\Ex Cap05\paises.csv', delimiter=';')
print(dfPaises.head(0))


# Exercicio 1
print('Exercicio 1')
print('Letra A)')
paisesOceania = dfPaises.loc[dfPaises['Region'].str.contains("OCEANIA")]
print(paisesOceania['Country'])
print('=================================================================================================')

print('Letra B)')
quantPaisesOceania = len(paisesOceania['Country'])
print(f"Ha {quantPaisesOceania} paises da Oceania.")
print('=================================================================================================')

# Exercicio 2
print('Exercicio 2')
worldLiteracy = dfPaises.iloc[:,9]
serie_worldLiteracy = pd.Series(worldLiteracy)
print(f"A media da taxa de alfabetizacao do planeta e {serie_worldLiteracy.mean()}%.")
print('=================================================================================================')

# Exercicio 3
print('Exercicio 3')

indice = dfPaises['Population'].idxmax()
regiao = dfPaises['Region'].values[indice]
pais = dfPaises['Country'].values[indice]
maiorPopulacao = dfPaises['Population'].values[indice]

print(f" O pais com a maior populcao e a {pais}, que se localiza na {regiao}. A {pais} conta com uma população de {maiorPopulacao} habitantes.")
print('=================================================================================================')

# Exercicio 4
print('Exercicio 4')

p_SemCosta = dfPaises.loc[dfPaises['Coastline (coast/area ratio)'] == 0]
paisesSemCosta = p_SemCosta ['Country']
print(paisesSemCosta)

paisesSemCosta.to_csv('paisesSemCosta.csv', sep=';', header=False)