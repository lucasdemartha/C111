import numpy as np

arr1 = np.arange(0, 51, 2)
arr2 = np.arange(100, 49, -2)

arr3 = sorted(np.concatenate((arr1, arr2)))
arr4 = np.unique(arr3)
print(np.flip(np.sort(arr4)))
