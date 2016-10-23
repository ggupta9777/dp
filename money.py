import numpy as np
def money(M):
        m = len(M)
        n = len(M[0])
        N = np.zeros([m,n])
        for j in range(m):
                for k in range(n):
                        temp1, temp2 = 100000, 100000
                        if (j==0) and (k==0):
                                N[j,k] = 0
                        else:
                                if  j != 0:
                                        temp1 = N[j-1,k]+ M[j,k]
                                if k != 0:
                                        temp2 = N[j, k-1] + M[j,k]
                                N[j,k] = min(temp1,temp2)
        return N

M = np.random.randint(10, size=(5,5))
#M = np.diag([10,22,3,12])
print M, "\n",money(M)

