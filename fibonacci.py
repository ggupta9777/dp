import numpy as np
def fibonacci_basic(N):
	if N<=2:
		return 1
	else:
		return fibonacci_basic(N-1) + fibonacci_basic(N-2)
def fib2(N):
	sums = np.zeros(N+1)
	for k in range(1,N+1):
		if k<=2:
			sums[k] = 1
		else:
			sums[k] = sums[k-1] + sums[k-2]
	return sums[N]
print fibonacci_basic(10)
print fib2(10)
