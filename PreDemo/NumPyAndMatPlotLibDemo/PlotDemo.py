import numpy as np
import matplotlib.pyplot as plt
def zuNi(x):
    return np.exp(-x)* np.sin(2*np.pi*x)

a = np.arange(0.0, 5, 0.02)
plt.plot(a, np.sin(2*np.pi*a), a, zuNi(a), '--')
plt.show()
a = np.random.randn(2, 5)
b = np.random.randn(5, 3)
print(np.matmul(a,b))
