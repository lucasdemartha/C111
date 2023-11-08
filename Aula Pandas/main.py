import numpy as np
import pandas as pd

'''
#PANDAS SERIES
#DEVEMOS PASSAR UMA LISTA DE CHAVES E UMA LISTA DE VALORES

dic = {'a': 10, 'b': 20, 'c': 30}
series1 = pd.Series(dic)
print(series1)
print(type(series1))
#ACESSANDO UM VALOR DA SERIES
print(series1['b'])
#ACESSANNDO UMA LISTA DE INDICES
print(series1[['a', 'c']])

#CALCULANDO MEDIA DOS ELEMENTOS DA SERIES
print(np.mean(series1))

#CONDICIONAL
print(series1[series1 > 25])


#PANDAS DATAFRAME
np.random.seed(10)
df = pd.DataFrame(
    data = np.random.randint(1, 50, [5, 4]),
    index = ['A', 'B', 'C', 'D', 'E'],
    columns = ['W', 'X', 'Y', 'Z']
)
print(df)

#ACESSANDO UMA UNICA COLUNA
print(df['X'])
#ACESSANDO MULTIPLAS COLUNAS
print(df[['W', 'Y']])

#SLICING COM LOC (INDICES CUSTOMIZAVEIS)
df2 = df.loc[['A', 'B'], ['X', 'Y', 'Z']]
print(df2)

#SLICING COM ILOC (INDICES NUMERICOS)
df3 = df.iloc[0:2, 1:]
print(df3)
'''
#LENDO UM ARQUIVO .CSV

paises = pd.read_csv(r'C:\Users\lucas\OneDrive\Desktop\C111\Aula Pandas\paises.csv', delimiter=';')
#print(paises)
print(paises.head(5))
print(paises.tail(5))
print(paises.columns)
