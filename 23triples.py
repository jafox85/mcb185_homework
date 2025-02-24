import math
a = 1
for b in range(1,100):
	for a in range(b,100):
		c = math.sqrt(a ** 2 + b ** 2)
		if c % 1 == 0: print(a, b, int(c))
	