import matplotlib.pyplot as plt
import pandas as pd

df_countries = pd.read_csv(r'C:\Users\lucas\OneDrive\Desktop\C111\Ex Cap06\paises.csv', delimiter=';')
df_space = pd.read_csv(r'C:\Users\lucas\OneDrive\Desktop\C111\Ex Cap06\space.csv', delimiter=';')

print(df_space.columns)
print()
print(df_countries.columns)

print()

# Question 1
print(df_space.head())

locationColumn = df_space['Location']
locationFilteringUSA = locationColumn.str.contains('USA')
locationFilteringChina = locationColumn.str.contains('China')

companyColumn = df_space['Company Name']
companiesUSA = companyColumn[locationFilteringUSA].unique()
companiesChina = companyColumn[locationFilteringChina].unique()

print()
print('--------------------Question 1--------------------')
print()
print('USA companies:',companiesUSA)
print()
print('China companies:',companiesChina)
print()

plt.bar(['USA','China'], [companiesUSA.size,companiesChina.size], color='blue')
plt.title('Number of companies from USA and China')
plt.show()

# Question 2
print(df_countries.head())

regionColumn = df_countries['Region']
regionFiltering = regionColumn.str.contains('NORTHERN AMERICA')

countryInfo = df_countries[['Country', 'Deathrate', 'Birthrate']]
americaNorthernCountryInfo = countryInfo[regionFiltering]

plt.plot(americaNorthernCountryInfo['Country'], americaNorthernCountryInfo['Deathrate'], color='red')
plt.plot(americaNorthernCountryInfo['Country'], americaNorthernCountryInfo['Birthrate'], color='green')
plt.legend(['Deathrate', 'Birthrate'])
plt.title('Deathrate and Birthrate')
plt.show()