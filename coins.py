import numpy as np
#minimum number of coins to get a sum of N and values v
#objective is to minimize,
#	minsum(Nj)
#	sub. to -> sum(Njvj) = Val
#	for each j, if vj<=Val, eval. minsum(Val - vj) + 1
#	if minsum(Val - vj)+1 > minsum(Val), reject, else return
#	let the coins be 1,2 and 5

v = np.array([1,2,5])
def min_coins(Val):
	out = 1000000*np.ones(Val+1)
	for k in range(1,Val+1):
		if k<=v[2]:
			if k==v[2] or k==v[1] or k==v[0]:
				out[k] = 1
			elif k ==0:
				out[k] = 0
			else:
				out[k] = 2				
		else:
			for j in range(len(v)):	
				if v[j] <= k:
					if out[k - v[j]] + 1< out[k]:
						somen = out[k - v[j]] + 1
					out[k] = somen
	
	return out[Val]

print min_coins(9924)
