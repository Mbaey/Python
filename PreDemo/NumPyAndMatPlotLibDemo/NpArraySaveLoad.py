import numpy as np
import os
# a = np.arange(100).reshape( 5, 20)
# os.mkdir('data')
# np.save('data/a.npy', a)
# np.savetxt('data/a.csv', a, fmt='%d', delimiter=',')

# a = np.load('data/a.npy')
a = np.loadtxt('data/a.csv', delimiter=',')
print(a)