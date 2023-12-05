import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Importando o csv
dfPaises = pd.read_csv('Paises.csv', delimiter=';')
print(dfPaises.head(0))

# Exércicio 1
print('\033[1m' + 'Exercício 1' + '\033[0m \n')

LatinAme_Caribe = dfPaises.loc[dfPaises['Region'].str.contains('LATIN AMER. & CARIB')]
dfLatinAme_Caribe = LatinAme_Caribe.loc [:,['Country','Region','Population','Area (sq. mi.)']]
print(dfLatinAme_Caribe)

# Exércicio 2
print('\033[1m' + 'Exercício 2' + '\033[0m \n')

Region_uni = dfPaises['Region'].unique() 
CountRegion_uni = np.count_nonzero(Region_uni)

print(f'Quantidade de Regiões: {CountRegion_uni} \n')
print(f'Diferentes regiões do planeta: \n')
print(f'Quantidade de Regiões: {Region_uni} \n')


# Exércicio 3
print('\033[1m' + 'Exercício 3' + '\033[0m')
print()

globalLiteracy = dfPaises['Literacy (%)'].mean()
print(f'Taxa média de alfabetização do planeta = {globalLiteracy} % \n')


# Exércicio 4
print('\033[1m' + 'Exercício 4' + '\033[0m')
print()

northernAmerica = dfPaises.loc[dfPaises['Region'].str.contains('NORTHERN AMERICA')]
info_northernAmerica = northernAmerica.loc[:,['Country','Population','GDP ($ per capita)']]
print(info_northernAmerica)

country_low = info_northernAmerica['Country'].values[3]
gpd_low = info_northernAmerica['GDP ($ per capita)'].values[3]

country_high = info_northernAmerica['Country'].values[4]
gpd_high = info_northernAmerica['GDP ($ per capita)'].values[4]


plt.title(" Renda per Capita - Países da Norte America ")
plt.xlabel('Países')
plt.ylabel('Renda  per  capita  (GDP)')
plt.bar(country_low, gpd_low, color="Blue")
plt.bar(country_high, gpd_high, color="Green")
plt.show()