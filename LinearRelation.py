import numpy as np

X = np.array([ [1,2,3],[10,-2,4],[8,30,5],[2,2,2] ])
D = np.array([ [6,4],[12,10],[43,-20],[6,2] ])
W = np.array([ [0.1,0.5,-2],
               [3,-2.5,1.3] ])

alpha = 0.0001

for n in range(0,10000):
    for e in range(0,4):
        Y = W@X[e]
        E = D[e] - Y

        for i in range(0,2):
            for j in range(0,3):
                W[i][j] = W[i][j] + alpha*E[i]*X[e][j]

A = np.array([6,16,27])
print(W@A)
