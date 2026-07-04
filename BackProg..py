import numpy as np
rng = np.random.default_rng()

def sgm(x):
    return 1 / (1 + np.exp(-x))

X = np.array([ [0,0,1],[0,1,1],[1,0,1],[1,1,1] ])
D = np.array([0,1,1,0])
W1 = 2 * rng.random((4,3)) - 1
W2 = 2 * rng.random((1,4)) - 1
alpha = 0.01

for n in range(0,10000):

    for e in range(0,4):
        V1 = W1@X[e]
        Y1 = sgm(V1)
        V2 = W2@Y1
        Y2 = sgm(V2)

        E = D[e] - Y2
        DELTA = Y2*(1 - Y2)*E
        E1 = np.transpose(W2)@DELTA
        DELTA1 = Y1*(1 - Y1)*E1

        W2 = W2 + alpha*np.outer(DELTA,Y1)
        W1 = W1 + alpha*np.outer(DELTA1,X[e])
