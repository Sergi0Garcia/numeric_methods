
import numpy as np
import matplotlib.pyplot as plt

def xnew(x):
    return (2*x**2+3)/5
X0 = 0
X1 = 0
itera = 0
X0array = np.zeros(100)
X1array = np.zeros(100)
xexe = np.zeros(100)

for i in range(100):
    X1 = xnew(X0)
    xexe[i] = i
    X0array[i] = X0
    X1array[i] = X1
    if abs(X1-X0) < 0.000001:
       break
    X0 = X1
    itera += 1
plt.plot(xexe, X0array, X1array)
plt.grid()
