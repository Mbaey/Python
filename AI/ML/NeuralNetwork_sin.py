import numpy as np
import matplotlib.pyplot as plt


def zuNi(x):
    return np.exp(-x) * np.sin(2 * np.pi * x)

def sigmod(x):
    return 1/(1+np.exp(x))

if __name__ == "__main__":
    # x = np.arange(0.0, 5, 0.02)   #??
    x=  np.random.randn(250,1)
    x.reshape(250,1)
    print(x.shape)
    y = np.sin(x)

    w2 = np.random.randn(1, 3)
    print(w2.shape)
    b2 = np.random.randn(1, 3)
    w1, b1= np.random.randn(2)
    print(w1.shape)
    w3 = np.random.randn(3,1)
    b3 = np.random.randn(3, 1)
    a1 = sigmod(w1*x+b1)
    # print(a1)
    a2 = sigmod(a1*w2+b2)
    print(a2.shape, w3.shape)

    a3 = sigmod(np.matmul(a2 * w3)+ b3)

    plt.plot(x, np.sin(2*np.pi*x), x, a3, '--')
    # plt.show()
