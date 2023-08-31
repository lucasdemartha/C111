import numpy as np
'''
#arr = np.array([1, 2, 3, 4, 5])
arr = np.arange(1, 4, 1)
#arr2 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.arange(1, 7, 1).reshape(2,3)

print(arr)
print(type(arr))
print(arr2)
'''

#ORDENACAO DE ELEMENTOS
#print(np.flip(np.sort(arr)))

#Concatenacao no numpy
arr1 = np.arange(1,7,1)
arr2 = np.arange(11, 17, 1)
arr3 = np.concatenate((arr1, arr2))
print(arr3)

'''
#operacao elemento a elemento
print(arr1 + arr2)
print(arr1 * arr2)
print(arr1 - arr2)
'''