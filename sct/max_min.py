# Write a program to implement Fuzzy Relations(Max-Min composition)
import numpy as np
def max_min(R,S):
    r = np.zeros((R.shape[0],S.shape[1]))
    for i in range(R.shape[0]):
        for j in range(S.shape[1]):
            mm=0
            for k in range(R.shape[1]):
                mm = max(mm,min(R[i,k],S[k,j]))
            r[i,j]=mm
    return r
R = np.array([[0.7, 0.6], [0.8, 0.3]])
S = np.array([[0.8, 0.1, 0.4], [0.5, 0.6, 0.7]])
print(max_min(R,S))