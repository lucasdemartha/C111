import numpy as np

print('#QUESTAO 1\n')
arr = np.loadtxt('paises.csv', delimiter=';', dtype=str)
data = arr[0:, 0:5]
print('\n--------------------------------------------------------\n')

print('#QUESTAO 2\n')
data_regions = np.unique(data[1:, 1])
num_data_regions = data_regions.size
print(f'Quantidade de regioes no dataset é de : {num_data_regions}')
for i in data_regions:
    print(i)

print('\n--------------------------------------------------------\n')

print('#QUESTAO 3\n')
literacy = np.array(arr[1:, 9], dtype=float)
print(round(np.mean(literacy), 2))
print('\n--------------------------------------------------------\n')

print('#QUESTAO 4\n')
north_america_countries = np.char.find(arr[1:, 1], 'NORTHERN AMERICA')
total = north_america_countries.size - np.count_nonzero(north_america_countries)
print(total)
print('\n--------------------------------------------------------\n')

print('#QUESTAO 5\n')
southCab = arr[1:, 1]
southCab_GDP = np.array(arr[1:, 8], dtype=np.int32)
GDP = 0
pos = 0
for i in range(len(southCab)):
    if southCab[i] == 'LATIN AMER. & CARIB    ' and southCab_GDP[i] > int(GDP):
        pos = i+1
        GDP = southCab_GDP[i]

print(arr[pos, 0])



