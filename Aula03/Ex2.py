import numpy as np

arr1 = np.arange(0, 51, 2)
arr2 = np.arange(100, 49, -2)

arr3 = sorted(np.concatenate((arr1, arr2)))
print(set(arr3))
