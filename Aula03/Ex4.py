import numpy as np

mtz1 = np.ones((3, 4), dtype=int)
print("Matriz 3x4: \n", mtz1)
mtz2 = mtz1.ravel() #ou mtz1.flatten()
print("Matrix 1-D: \n", mtz2)