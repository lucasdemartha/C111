import matplotlib.pyplot as plt
import pandas as pd

# Reading dataset
df_nike = pd.read_csv(r'C:\Users\User\Desktop\C111\Estudos prova2\nike.csv', delimiter=',')

# Printing columns name
print(df_nike.columns)

print()

print(df_nike.head())

print()

# Question 1
print('-------------- Question 1 --------------')
priceColumn = df_nike['price']
maxPriceFiltering = priceColumn == priceColumn.max()

productInfo = df_nike[['name','sub_title','price']]
productInfo = productInfo[maxPriceFiltering]

name = productInfo['name']
subtitle = productInfo['sub_title']
price = productInfo['price']

print(f'Name: {name[68]} and\nSub-title: {subtitle[68]}')

# Question 2
print()
print('-------------- Question 2 --------------')
subTitleColumn = df_nike['sub_title']
setFiltering = subTitleColumn.str.contains('Set')

priceSet = priceColumn[setFiltering]

print(priceSet)
meanSetPrice = priceSet.mean()
print(f'The mean price of a Set is: {meanSetPrice}')

# Question 3
print()
print('-------------- Question 3 --------------')
colorColumn = df_nike['color']
colorBlackFiltering = colorColumn.str.contains('Black').to_list()

newColorBlackFiltering = []
for element in colorBlackFiltering:
    if element == True:
        newColorBlackFiltering.append(False)
    else:
        newColorBlackFiltering.append(True)

notBlackProducts = len(df_nike[newColorBlackFiltering])

numProducts = len(df_nike)

print(f'Percentage: {100 * float(notBlackProducts)/numProducts} %')

# Question 4
print()
print('-------------- Question 4 --------------')
nameColumn = df_nike['name']
airJordanFiltering = nameColumn.str.contains('Air Jordan')

airJordanProducts = df_nike[['name', 'availability']][airJordanFiltering]
airJordanNotAvailableFiltering = airJordanProducts['availability'].str.contains('OutOfStock')
airJordanNotAvailable = airJordanProducts[airJordanNotAvailableFiltering]
print(airJordanNotAvailable['name'])