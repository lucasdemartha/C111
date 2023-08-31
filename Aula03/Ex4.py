import numpy as np

mtz1 = np.ones(12).reshape(3,4)
print("Matriz 3x4: \n", mtz1)
mtz2 = mtz1.ravel()
print("Matrix 1-D: \n", mtz2)