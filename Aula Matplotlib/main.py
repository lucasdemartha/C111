import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#Fazendo um plot com matplotlib
#
# x = np.array([1, 2, 3, 4])
# y = x*2 #broadcasting
# y2 = x**2
#
# plt.plot(x, y, '*--g', x, y2, 'o-b', linewidth=3, markersize=20)# gerando o grafico
#
# plt.show()#mostrando o grafico
#Fazendo um dashboard
x = np.array([1, 2, 3, 4])
y = x*2 #broadcasting
y2 = x**2
#subplot 1
plt.subplot(1, 2, 1)
plt.plot(x, y)
#subplot 2
plt.subplot(1, 2, 2)
plt.plot(x, y2)
plt.show()