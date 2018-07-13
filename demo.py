import numpy as np


def pagerank(S, d=0.85, r=1e-06):

    N = S.shape[0]
    e = np.ones((N, 1))
    p0 = 1./N * e
    p1 = e
    while np.sum(np.abs(p1-p0)) > r:
        p0, p1 = p1, d * np.dot(S, p0) + (1.-d)/N * e 

    return N, p1

if __name__ == "__main__":

    S = np.array([[0,1/2,0,0],
                [1/3,0,0,1/2],
                [1/3,0,1,1/2],
                [1/3,1/2,0,0]])

    N, p = pagerank(S)

    for i in range(N):
        print("pr(node{0}) = {1}".format(i, p[i]))
