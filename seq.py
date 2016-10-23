import numpy as np
def longseq(A):
	N = len(A)
	B = np.ones(N)
	for k in range(N):
		if k==0:
			B[k] = 1
		elif A[k-1]<=A[k]:
			B[k] = B[k-1] + 1
	return B

A  = np.random.randint(10, size=10)

print A
print longseq(A)
