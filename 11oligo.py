import math
def tm(A,T,C,G):
	if A + T + C + G <= 13: return (A+T) * 2 + (C+G) * 4
	return 64.9 + 41 * (C+G - 16.4) / (A+T+C+G)
print(tm(5,7,3,4))